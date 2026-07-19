"""Physicochemical and compositional sequence representations.

Ported from permea-bbb-audit (Paper 1 harness, DOI 10.5281/zenodo.21134112), which is
read-only. The five physchem descriptors are the ones the paper reports, and they are
Biopython-backed.

WARNING — do NOT source these from permea-signal-ml. Its `physicochemical.py` computes
pI as `7.0 + charge/len*3.0`, a placeholder its own docstring disclaims. Using it would
silently change every downstream number.

This module also replaces the six copy-pasted `comp_vec` / `AAS` definitions scattered
across the audit harness with a single implementation.
"""

from __future__ import annotations

import numpy as np

#: The 20 canonical amino acids, in the fixed order used for composition vectors.
AAS = "ACDEFGHIKLMNPQRSTVWY"

#: Physchem feature columns, in the order the Paper 1 harness materialised them.
#: Order is load-bearing: downstream diagnostics index length positionally.
PHYSCHEM_COLS = ("length", "charge", "gravy", "pI", "aromaticity")


def composition(sequence: str) -> np.ndarray:
    """20-dim amino-acid frequency vector (fractions, sums to 1 for non-empty input)."""
    n = len(sequence)
    if n == 0:
        return np.zeros(len(AAS), dtype=float)
    counts = np.array([sequence.count(a) for a in AAS], dtype=float)
    return counts / n


def composition_matrix(sequences: list[str]) -> np.ndarray:
    """(N, 20) composition matrix, row-aligned to `sequences`."""
    return np.vstack([composition(s) for s in sequences])


def physchem_matrix(rows: list[dict]) -> np.ndarray:
    """(N, 5) physchem matrix read from precomputed dataset columns.

    The columns are materialised by the dataset adapter (Biopython-backed) rather than
    recomputed here, so that the values are byte-identical to the canonical dataset and
    covered by its sha256.
    """
    return np.array(
        [[float(r[c]) for c in PHYSCHEM_COLS] for r in rows],
        dtype=float,
    )


def length_matrix(rows: list[dict]) -> np.ndarray:
    """(N, 1) sequence length.

    Named accessor rather than a positional slice. The audit harness did
    `physchem[:, 0:1]  # PHYSCHEM_COLS[0] == "length"`, a positional coupling to another
    module's column order; this is the seam that replaces it.
    """
    return np.array([[float(r["length"])] for r in rows], dtype=float)
