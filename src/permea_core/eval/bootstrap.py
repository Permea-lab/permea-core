"""Cluster-level bootstrap inference.

Ported from permea-bbb-audit/harness/honest_eval.py (read-only source).

The independent unit under identity control is the CLUSTER, not the row: rows within a
cluster are near-duplicates and carry no independent information. Row-level resampling
therefore understates the CI. `resample_unit: cluster` is the permea-eval/1.0 default;
choosing `row` emits PERMEA-W003.
"""

from __future__ import annotations

import numpy as np

from permea_core.eval.engine import ALL_METRICS, metrics_at

# The interval's tail percentiles, and the confidence level they imply. These are the SINGLE
# source of the level: `paired_bootstrap` reads the percentiles, and everything that reports
# "95% CI" derives the 95 from CI_LEVEL_PCT rather than restating a literal. Widen or narrow
# the interval by editing the percentiles here and the reported level follows automatically.
CI_PERCENTILE_LO = 2.5
CI_PERCENTILE_HI = 97.5
CI_LEVEL_PCT = CI_PERCENTILE_HI - CI_PERCENTILE_LO  # 95.0


def make_cluster_resampler(groups: np.ndarray | None):
    """resample(rng, n) -> row indices, resampling CLUSTERS with replacement."""
    if groups is None:
        return lambda rng, n: rng.integers(0, n, n)
    groups = np.asarray(groups)
    uniq = np.unique(groups)
    members = [np.where(groups == c)[0] for c in uniq]

    def resample(rng, n=None):
        drawn = rng.integers(0, len(uniq), len(uniq))
        return np.concatenate([members[j] for j in drawn])

    return resample


def paired_bootstrap(y, oof_a, thr_a, oof_b, thr_b, n_boot=2000, seed=0, groups=None):
    """All-metric PAIRED bootstrap at FIXED thresholds. Returns key -> (median, lo, hi).

    Paired: A and B are evaluated on the SAME resample indices, so the correlation
    between conditions is retained. Unpaired comparison inflates the interval.

    Fixed thresholds: re-tuning per condition would make the delta measure threshold
    movement rather than generalisation loss (PERMEA-W005).
    """
    rng = np.random.default_rng(seed)
    n = len(y)
    resample = make_cluster_resampler(groups)
    acc = {k: [] for k in ALL_METRICS}
    for _ in range(n_boot):
        idx = resample(rng, n)
        yb = y[idx]
        if len(np.unique(yb)) < 2:
            continue
        ma = metrics_at(yb, oof_a[idx], thr_a)
        mb = metrics_at(yb, oof_b[idx], thr_b)
        for k in ALL_METRICS:
            acc[k].append(mb[k] - ma[k])
    out = {}
    for k in ALL_METRICS:
        d = np.array(acc[k], dtype=float)
        out[k] = (
            float(np.nanmedian(d)),
            float(np.nanpercentile(d, CI_PERCENTILE_LO)),
            float(np.nanpercentile(d, CI_PERCENTILE_HI)),
        )
    return out
