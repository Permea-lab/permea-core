"""Dataset loading against the permea-eval/1.0 record contract."""

from __future__ import annotations

import csv
import hashlib

import numpy as np


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_dataset(path: str):
    """Returns (rows, ids, y, sequences). Column names are the declared contract."""
    # TODO(permea-eval/1.0 contract): this tightens the input contract vs the canonical
    # honest_eval.load_data by REQUIRING a "sequence" column. A physchem-only CSV (no
    # "sequence") would KeyError here where the canonical harness succeeded. Decide later
    # whether "sequence" is mandatory or optional in the record contract. Behavior
    # unchanged for now.
    rows = list(csv.DictReader(open(path)))
    ids = [r["sequence_id"] for r in rows]
    y = np.array([int(r["label"]) for r in rows])
    seqs = [r["sequence"] for r in rows]
    return rows, ids, y, seqs
