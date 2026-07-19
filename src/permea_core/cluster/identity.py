"""Identity clustering for identity-controlled splitting.

Ported from permea-bbb-audit/harness/build_identity_clusters.py (read-only source,
DOI 10.5281/zenodo.21134112). Behaviour is preserved exactly; the CLI is replaced by
function signatures.

Clustering is decoupled from evaluation: a backend produces a mapping
{sequence_id -> cluster_id}, and the evaluator consumes group labels. Any tool that can
emit that mapping is usable, which is what makes the harness cluster-agnostic.

Backends:
  mmseqs  — MMseqs2 easy-cluster. The paper's headline backend.
  align   — Biopython global alignment, greedy representative clustering. Reference
            cross-check, pure-Python.
  proxy   — difflib ratio + k-mer prefilter. Fast, v0 only, label as proxy.

NOTE ON COMPARABILITY (permea-eval/1.0 non-claims): these backends do NOT agree at the
same nominal threshold, and neither do different MMseqs2 versions. The identity
threshold alone does not determine the clustering — the alignment mode, the denominator
and the gap treatment do too. That is why `IdentityDefinition` is a required, declared
field rather than an implicit convention.
"""

from __future__ import annotations

import collections
import difflib
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np

#: Permea's own identity convention, as used in Paper 1: global alignment, identity
#: measured over the SHORTER sequence, gaps free. Declared, not assumed.
PERMEA_IDENTITY_DEFINITION = {
    "alignment": "global",
    "denominator": "shorter_sequence",
    "gap_treatment": "free",
}


@dataclass(frozen=True)
class ClusterAssignment:
    """A materialised clustering. `id2cluster` maps sequence_id -> cluster_id."""

    id2cluster: dict[str, str]
    tool: str
    tool_version: str
    identity_threshold: float
    identity_definition: dict[str, str]

    @property
    def n_clusters(self) -> int:
        return len(set(self.id2cluster.values()))

    @property
    def n_singletons(self) -> int:
        sizes = collections.Counter(self.id2cluster.values())
        return sum(1 for v in sizes.values() if v == 1)

    @property
    def largest(self) -> int:
        return max(collections.Counter(self.id2cluster.values()).values())

    def groups(self, ids: Sequence[str]) -> np.ndarray:
        """Dense integer group labels aligned to `ids`, for grouped CV."""
        missing = [s for s in ids if s not in self.id2cluster]
        if missing:
            raise KeyError(
                f"cluster assignment is missing {len(missing)} sequence_id(s), "
                f"e.g. {missing[:3]}"
            )
        uniq: dict[str, int] = {}
        out = np.empty(len(ids), dtype=int)
        for i, s in enumerate(ids):
            c = self.id2cluster[s]
            out[i] = uniq.setdefault(c, len(uniq))
        return out

    def write_tsv(self, path: str, order: Iterable[str]) -> None:
        with open(path, "w") as f:
            for sid in order:
                f.write(f"{sid}\t{self.id2cluster[sid]}\n")


def mmseqs_version() -> str:
    try:
        out = subprocess.run(
            ["mmseqs", "version"], capture_output=True, text=True, check=True
        )
        return out.stdout.strip()
    except Exception:
        return "unknown"


def cluster_mmseqs(
    seqs: list[tuple[str, str]], min_seq_id: float, cov: float = 0.8
) -> dict[str, str]:
    """MMseqs2 easy-cluster with the short-peptide settings used in Paper 1.

    Peptides are 5-30 aa; MMseqs2 needs small k and high sensitivity in that regime.
    These flags are reproduced verbatim from the frozen harness -- changing any of them
    changes the clustering and therefore the headline numbers.
    """
    if not shutil.which("mmseqs"):
        raise RuntimeError(
            "mmseqs not found. `brew install mmseqs2` or "
            "`conda install -c bioconda mmseqs2`. The pure-Python `align` backend "
            "needs no external binary."
        )
    tmp = tempfile.mkdtemp(prefix="permea_mmseqs_")
    try:
        fa = os.path.join(tmp, "in.fasta")
        with open(fa, "w") as f:
            for sid, s in seqs:
                f.write(f">{sid}\n{s}\n")
        out = os.path.join(tmp, "clu")
        subprocess.run(
            [
                "mmseqs", "easy-cluster", fa, out, os.path.join(tmp, "tmp"),
                "--min-seq-id", str(min_seq_id),
                "-c", str(cov), "--cov-mode", "0",
                "-k", "5", "-s", "7.5", "--cluster-mode", "0", "-v", "1",
            ],
            check=True,
            capture_output=True,
        )
        id2cluster: dict[str, str] = {}
        with open(out + "_cluster.tsv") as f:  # rep<TAB>member
            for line in f:
                rep, mem = line.rstrip("\n").split("\t")
                id2cluster[mem] = rep
        return id2cluster
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def cluster_align(
    seqs: list[tuple[str, str]], min_seq_id: float, k: int = 3
) -> dict[str, str]:
    """Biopython global-alignment identity, greedy representative clustering.

    Identity is match_count / len(shorter), with free gaps -- the PERMEA_IDENTITY_DEFINITION.
    """
    from Bio.Align import PairwiseAligner

    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 1
    aligner.mismatch_score = 0
    aligner.open_gap_score = -1
    aligner.extend_gap_score = -1

    def identity(a: str, b: str) -> float:
        return aligner.score(a, b) / min(len(a), len(b))

    def kmers(s: str) -> set[str]:
        return {s[i : i + k] for i in range(len(s) - k + 1)} if len(s) >= k else {s}

    return _greedy_cluster(seqs, min_seq_id, kmers, identity)


def cluster_proxy(
    seqs: list[tuple[str, str]], min_seq_id: float, k: int = 3
) -> dict[str, str]:
    """difflib ratio + k-mer prefilter. FAST, v0 only -- always label results as proxy."""

    def kmers(s: str) -> set[str]:
        return {s[i : i + k] for i in range(len(s) - k + 1)} if len(s) >= k else {s}

    def identity(a: str, b: str) -> float:
        return difflib.SequenceMatcher(None, a, b).ratio()

    return _greedy_cluster(seqs, min_seq_id, kmers, identity)


def _greedy_cluster(seqs, min_seq_id, kmers, identity) -> dict[str, str]:
    """Shared greedy representative clustering, longest-first, with a k-mer prefilter."""
    order = sorted(range(len(seqs)), key=lambda i: -len(seqs[i][1]))
    reps: list[int] = []
    kmer_index: dict[str, list[int]] = collections.defaultdict(list)
    id2cluster: dict[str, str] = {}
    for i in order:
        sid, s = seqs[i]
        ks = kmers(s)
        cand: set[int] = set()
        for km in ks:
            cand.update(kmer_index[km])
        best, best_sim = None, 0.0
        for rj in cand:
            sim = identity(s, seqs[reps[rj]][1])
            if sim > best_sim:
                best_sim, best = sim, rj
        if best is not None and best_sim >= min_seq_id:
            id2cluster[sid] = seqs[reps[best]][0]
        else:
            rj = len(reps)
            reps.append(i)
            for km in ks:
                kmer_index[km].append(rj)
            id2cluster[sid] = sid
    return id2cluster


_BACKENDS = {"mmseqs": cluster_mmseqs, "align": cluster_align, "proxy": cluster_proxy}


def build_clusters(
    seqs: list[tuple[str, str]],
    method: str = "mmseqs",
    min_seq_id: float = 0.4,
    cov: float = 0.8,
) -> ClusterAssignment:
    """Cluster `seqs` [(sequence_id, sequence), ...] and return a ClusterAssignment."""
    if method not in _BACKENDS:
        raise ValueError(f"unknown method {method!r}; choose from {sorted(_BACKENDS)}")
    if method == "mmseqs":
        id2c = cluster_mmseqs(seqs, min_seq_id, cov)
        version = mmseqs_version()
    else:
        id2c = _BACKENDS[method](seqs, min_seq_id)
        import Bio

        version = f"biopython-{Bio.__version__}" if method == "align" else "stdlib-difflib"
    return ClusterAssignment(
        id2cluster=id2c,
        tool={"mmseqs": "mmseqs2", "align": "pairwise_align", "proxy": "proxy_difflib"}[method],
        tool_version=version,
        identity_threshold=min_seq_id,
        identity_definition=dict(PERMEA_IDENTITY_DEFINITION),
    )


def read_clusters_tsv(path: str) -> dict[str, str]:
    """Read a sequence_id<TAB>cluster_id TSV produced by any tool."""
    m: dict[str, str] = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            sid, cid = line.split("\t")[:2]
            m[sid] = cid
    return m
