"""Synthetic demo inputs that exercise the W501 -> W101 flip.

WHAT THIS IS NOT: this is not B3Pred. No PermeaBench dataset is vendored in this repo
(see ``acquisition_manifests/b3pred_dataset3.yaml``: acquisition_mode
``no-redistribution-source-card-only``), so the UI ships a synthetic stand-in instead of
implying a redistribution right it does not have. Every surface that renders this fixture
must say so -- ``EXAMPLE_LABEL`` exists to make that hard to forget.

WHAT IT DEMONSTRATES: one dataset, two cluster assignments over the SAME rows.

  clusters_naive.tsv   near-duplicates scattered across clusters. Grouped CV still lets a
                       model memorize a family from its own siblings, so condition B looks
                       like condition A, the paired-bootstrap CI straddles zero, and
                       diagnose fires PERMEA-W501 (inconclusive).

  clusters_family.tsv  near-duplicates held together, which is what an identity-aware
                       clustering (mmseqs-style) would produce. B can no longer memorize,
                       the headline metric drops materially, the CI clears zero, and
                       diagnose fires PERMEA-W101 (material similarity leakage).

The point of the demo is that the FIRST run is the reassuring one and the second is the
indictment: nothing about the model, the metric, or the code changed between them -- only
the honesty of the clustering. That is the whole argument for an evaluation commons.

Structure: ``_FAMILIES`` near-duplicate families of ``_FAMILY_SIZE`` rows each. A family's
label is drawn independently of its centroid, so label is only weakly learnable from the
physchem features themselves and strongly learnable by memorizing which family a row
belongs to. That gap is the leakage the flip exposes.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from permea_core.represent.physchem import PHYSCHEM_COLS

#: Rendered by every UI surface that shows fixture-derived results. Not decoration.
EXAMPLE_LABEL = "SYNTHETIC EXAMPLE - not B3Pred, not any real dataset"

_FAMILIES = 60  # >= DiagnosePolicy.min_clusters (50), so W502 stays quiet
#: 3 rows/family = 180 rows. Chosen by sweeping the POPULATION, never the statistics: at
#: this size the naive run's paired-bootstrap CI genuinely straddles zero (W501
#: inconclusive) while the family run's does not (W101). Widening a CI by cutting n_boot
#: or seeds would manufacture the same code by weakening the evidence -- the opposite of
#: what this tool exists to argue for. Verified at seeds=(0,1), k=3, n_boot=400.
_FAMILY_SIZE = 3
_SEED = 20260721


def _matrix(rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build (features, labels, family_ids) for the near-duplicate population."""
    centroids = rng.normal(0.0, 1.0, size=(_FAMILIES, len(PHYSCHEM_COLS)))
    # Label correlates only weakly with the centroid: a real signal exists, but it is far
    # weaker than the "which family is this" shortcut a leaky split leaves available.
    logit = centroids[:, 0] * 0.45
    family_labels = (rng.random(_FAMILIES) < 1.0 / (1.0 + np.exp(-logit))).astype(int)

    feats, labels, families = [], [], []
    for fam in range(_FAMILIES):
        for _ in range(_FAMILY_SIZE):
            # Within-family jitter is an order of magnitude below between-family spread --
            # these are near-duplicates, the thing identity clustering exists to catch.
            feats.append(centroids[fam] + rng.normal(0.0, 0.08, size=len(PHYSCHEM_COLS)))
            labels.append(family_labels[fam])
            families.append(fam)
    return np.asarray(feats), np.asarray(labels), np.asarray(families)


def write_example(dest: Path) -> dict[str, Path]:
    """Write the demo CSV and both cluster TSVs into ``dest``. Returns their paths.

    Deterministic: fixed seed, so the demo tells the same story every time it is loaded.
    """
    dest.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(_SEED)
    X, y, families = _matrix(rng)
    ids = [f"seq{i:04d}" for i in range(len(y))]

    header = "sequence_id,sequence,label," + ",".join(PHYSCHEM_COLS)
    rows = [
        # The `sequence` column is required by the loader but never read for physchem --
        # load.py reads the precomputed columns and recomputes nothing from the residues.
        f"{sid},SYNTHETIC,{int(lbl)}," + ",".join(f"{v:.6f}" for v in feat)
        for sid, lbl, feat in zip(ids, y, X)
    ]
    csv_path = dest / "example_dataset.csv"
    csv_path.write_text("\n".join([header, *rows]) + "\n", encoding="utf-8")

    family_path = dest / "clusters_family.tsv"
    family_path.write_text(
        "\n".join(f"{sid}\tfam{fam:03d}" for sid, fam in zip(ids, families)) + "\n",
        encoding="utf-8",
    )

    # The naive assignment keeps the SAME cluster count -- so the flip cannot be dismissed
    # as "the second run just had fewer clusters". Only the membership differs.
    scattered = rng.permutation(len(ids)) % _FAMILIES
    naive_path = dest / "clusters_naive.tsv"
    naive_path.write_text(
        "\n".join(f"{sid}\tcl{c:03d}" for sid, c in zip(ids, scattered)) + "\n",
        encoding="utf-8",
    )

    return {"dataset": csv_path, "family": family_path, "naive": naive_path}
