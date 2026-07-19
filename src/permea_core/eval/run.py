"""Honest-evaluation orchestrator.

Re-creates the end-to-end glue that ``permea-bbb-audit/harness/honest_eval.py::main()``
had (dataset + clusters -> represent -> evaluate -> paired_bootstrap -> derived fields),
but returns a structured, closed Python result object instead of writing a CSV.

The engine, bootstrap, cluster, represent, and dataset-loading modules are reused VERBATIM:
this module adds only glue (cluster-mapping alignment, derived fields, result assembly) and
changes none of their numerics. ``run()`` is the reusable array-level unit that the CLI, the
Drylab web UI, tests, and the future diagnose layer all call -- one source of truth.

CLOSED-SCHEMA SEAM: ``EvalRun`` and ``MetricRow`` are frozen dataclasses with only typed,
enumerable fields -- no free-form dict, no narration slot. A future permea-eval/1.0 output
schema (additionalProperties: false, so LLM narration can never enter permea_core) maps 1:1
onto these fields. The schema is intentionally NOT built here; this is only the seam.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from permea_core.eval.bootstrap import CI_LEVEL_PCT, paired_bootstrap
from permea_core.eval.engine import ALL_METRICS, ModelSpec, default_models, evaluate


@dataclass(frozen=True, slots=True)
class MetricRow:
    """One (model, metric) result. Full precision; rounding is a serializer concern."""

    model: str
    metric: str
    A_mean: float
    A_std: float
    B_mean: float
    B_std: float
    delta_point: float  # B_mean - A_mean
    delta_boot_median: float | None  # None when n_boot == 0
    ci_lo: float | None
    ci_hi: float | None
    ci_excludes_zero: bool | None  # (ci_lo > 0 or ci_hi < 0); None when n_boot == 0


@dataclass(frozen=True, slots=True)
class EvalRun:
    """Structured result of one honest-evaluation run (closed; see module seam note)."""

    # run-level config / provenance
    representation: str
    threshold_label: str
    seeds: tuple[int, ...]
    k: int
    n_boot: int
    resample_unit: str  # "cluster" | "row"
    headline_condition: str  # "B" (recorded, not enforced -- diagnosed later)
    identity_definition: dict[str, str] | None
    # dataset shape
    n: int
    pos: int
    neg: int
    n_clusters: int
    data_sha256: str | None
    # results
    rows: tuple[MetricRow, ...]  # one per (model, metric)
    # The confidence level of every row's [ci_lo, ci_hi], as an integer-style percent (95.0
    # for a 2.5/97.5 percentile interval). Recorded rather than assumed: the CI bounds alone
    # do not say what level they were built at, so a reader -- or a narration layer -- has no
    # way to state "95% CI" from the numbers. Defaults to the level `paired_bootstrap`
    # actually uses; `run()` sets it to None when the bootstrap was skipped. Last in the
    # field order only because it carries a default.
    ci_level_pct: float | None = CI_LEVEL_PCT


def run(
    X: np.ndarray,
    y: np.ndarray,
    groups: np.ndarray,
    *,
    models: list[ModelSpec] | None = None,
    seeds: Sequence[int] = (0, 1, 2, 3, 4),
    k: int = 5,
    n_boot: int = 2000,
    representation: str = "physchem",
    threshold_label: str = "NA",
    resample_unit: str = "cluster",
    headline_condition: str = "B",
    identity_definition: dict[str, str] | None = None,
    data_sha256: str | None = None,
) -> EvalRun:
    """Run Conditions A and B for every model and assemble the structured result.

    Mirrors ``honest_eval.main()``'s inner loop exactly: per model, ``evaluate`` produces
    A/B out-of-fold predictions and per-seed metrics; the seed-0 out-of-fold scores feed a
    paired bootstrap at fixed thresholds. ``resample_unit="cluster"`` resamples clusters
    (the correct independent unit); ``"row"`` falls back to row-level (``groups=None`` to
    the bootstrap). ``n_boot == 0`` skips the bootstrap and leaves CI fields ``None``.
    """
    models = models or default_models()
    seeds = tuple(seeds)
    y = np.asarray(y)
    groups = np.asarray(groups)

    boot_groups = groups if resample_unit == "cluster" else None
    results = evaluate(X, y, groups, models=models, seeds=seeds, k=k)

    rows: list[MetricRow] = []
    for m in models:
        cond_a = results[m.name]["A"]
        cond_b = results[m.name]["B"]
        boot = (
            paired_bootstrap(
                y,
                cond_a.oofs[0],
                cond_a.thresholds[0],
                cond_b.oofs[0],
                cond_b.thresholds[0],
                n_boot=n_boot,
                seed=0,
                groups=boot_groups,
            )
            if n_boot > 0
            else None
        )
        for metric in ALL_METRICS:
            a_mean, a_std = cond_a.mean_std(metric)
            b_mean, b_std = cond_b.mean_std(metric)
            if boot is None:
                med = lo = hi = None
                ci_excl = None
            else:
                med, lo, hi = boot[metric]
                ci_excl = bool(lo > 0 or hi < 0)
            rows.append(
                MetricRow(
                    model=m.name,
                    metric=metric,
                    A_mean=a_mean,
                    A_std=a_std,
                    B_mean=b_mean,
                    B_std=b_std,
                    delta_point=b_mean - a_mean,
                    delta_boot_median=med,
                    ci_lo=lo,
                    ci_hi=hi,
                    ci_excludes_zero=ci_excl,
                )
            )

    n_clusters = int(len(np.unique(groups)))
    return EvalRun(
        representation=representation,
        threshold_label=threshold_label,
        seeds=seeds,
        k=k,
        n_boot=n_boot,
        resample_unit=resample_unit,
        headline_condition=headline_condition,
        identity_definition=identity_definition,
        n=int(len(y)),
        pos=int((y == 1).sum()),
        neg=int((y == 0).sum()),
        n_clusters=n_clusters,
        data_sha256=data_sha256,
        rows=tuple(rows),
        # From the bootstrap module itself, so the reported level cannot drift from the
        # percentiles the interval was actually built at. None when no interval exists.
        ci_level_pct=CI_LEVEL_PCT if n_boot > 0 else None,
    )


def align_groups(id2cluster: dict[str, str], ids: Sequence[str]) -> np.ndarray:
    """Map a {sequence_id -> cluster_id} TSV mapping to a row-aligned contiguous int array.

    Same alignment ``honest_eval.read_clusters`` did inline: cluster ids are assigned
    contiguous integers in first-seen order, aligned to ``ids``. Raises if any id is
    missing from the mapping.
    """
    missing = [s for s in ids if s not in id2cluster]
    if missing:
        raise ValueError(f"cluster mapping missing {len(missing)} sequence_id(s), e.g. {missing[0]!r}")
    uniq: dict[str, int] = {}
    groups = np.empty(len(ids), dtype=int)
    for i, s in enumerate(ids):
        c = id2cluster[s]
        uniq.setdefault(c, len(uniq))
        groups[i] = uniq[c]
    return groups


def run_from_dataset(
    data_path: str,
    clusters_path: str,
    *,
    representation: str = "physchem",
    seeds: Sequence[int] = (0, 1, 2, 3, 4),
    k: int = 5,
    n_boot: int = 2000,
    threshold_label: str = "NA",
    resample_unit: str = "cluster",
    identity_definition: dict[str, str] | None = None,
) -> EvalRun:
    """File-level wrapper mirroring ``honest_eval.main()``'s I/O glue (physchem only in v0).

    Loads the dataset CSV, builds the physchem representation, reads + aligns the cluster
    TSV, records the dataset sha256, then delegates to :func:`run`. Embedding (.npy)
    representations are reached via the array-level :func:`run` instead.
    """
    if representation != "physchem":
        raise ValueError(
            f"run_from_dataset supports representation='physchem' in v0; got {representation!r}. "
            "Use run() with a precomputed X for embeddings."
        )
    from permea_core.datasets.load import load_dataset, sha256
    from permea_core.represent.physchem import physchem_matrix
    from permea_core.cluster.identity import read_clusters_tsv

    rows, ids, y, _seqs = load_dataset(data_path)
    X = physchem_matrix(rows)
    groups = align_groups(read_clusters_tsv(clusters_path), ids)
    return run(
        X,
        y,
        groups,
        seeds=seeds,
        k=k,
        n_boot=n_boot,
        representation=representation,
        threshold_label=threshold_label,
        resample_unit=resample_unit,
        identity_definition=identity_definition,
        data_sha256=sha256(data_path),
    )
