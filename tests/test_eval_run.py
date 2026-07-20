"""Focused tests for the honest-evaluation orchestrator (permea_core.eval.run)."""

from __future__ import annotations

import numpy as np
import pytest

from permea_core.eval.bootstrap import CI_LEVEL_PCT, CI_PERCENTILE_HI, CI_PERCENTILE_LO
from permea_core.eval.engine import ALL_METRICS
from permea_core.eval.run import EvalRun, MetricRow, align_groups, run, run_from_dataset


def _synthetic(n_pos=12, n_neg=24, dim=5, seed=7):
    rng = np.random.default_rng(seed)
    # separable-ish signal so metrics are non-degenerate
    Xp = rng.normal(0.6, 1.0, size=(n_pos, dim))
    Xn = rng.normal(-0.6, 1.0, size=(n_neg, dim))
    X = np.vstack([Xp, Xn])
    y = np.array([1] * n_pos + [0] * n_neg)
    # deterministic within-class clusters of size 1..3
    groups = np.empty(len(y), dtype=int)
    gid = 0
    for label in (1, 0):
        idx = np.where(y == label)[0]
        i = 0
        j = 0
        sizes = [1, 2, 3, 2]
        while i < len(idx):
            s = sizes[j % len(sizes)]
            for kk in idx[i : i + s]:
                groups[kk] = gid
            gid += 1
            i += s
            j += 1
    return X, y, groups


def test_run_structure_and_derived_fields():
    X, y, groups = _synthetic()
    res = run(X, y, groups, seeds=(0, 1), k=3, n_boot=200)

    assert isinstance(res, EvalRun)
    # 3 default models x 7 metrics
    assert len(res.rows) == 3 * len(ALL_METRICS)
    assert {r.model for r in res.rows} == {"dummy", "logreg", "rf"}
    assert {r.metric for r in res.rows} == set(ALL_METRICS)

    # run-level fields
    assert res.n == len(y)
    assert res.pos == int((y == 1).sum())
    assert res.neg == int((y == 0).sum())
    assert res.n_clusters == len(np.unique(groups))
    assert res.seeds == (0, 1)
    assert res.k == 3
    assert res.n_boot == 200
    assert res.resample_unit == "cluster"
    assert res.headline_condition == "B"

    for r in res.rows:
        assert isinstance(r, MetricRow)
        # delta_point is exactly B_mean - A_mean
        assert r.delta_point == pytest.approx(r.B_mean - r.A_mean, abs=0, rel=0)
        # bootstrap present -> CI fields populated and ci_excludes_zero consistent
        assert r.ci_lo is not None and r.ci_hi is not None
        assert r.ci_excludes_zero == bool(r.ci_lo > 0 or r.ci_hi < 0)


def test_run_nboot_zero_leaves_ci_none():
    X, y, groups = _synthetic()
    res = run(X, y, groups, seeds=(0,), k=3, n_boot=0)
    for r in res.rows:
        assert r.delta_boot_median is None
        assert r.ci_lo is None and r.ci_hi is None
        assert r.ci_excludes_zero is None
    # No interval was built, so no level is claimed.
    assert res.ci_level_pct is None


def test_ci_level_pct_comes_from_the_bootstrap_percentiles():
    """The recorded level must be the one the interval was actually built at.

    Asserted against the bootstrap's own percentiles rather than a literal 95, so widening
    the interval can never leave the run reporting a level it did not use.
    """
    X, y, groups = _synthetic()
    res = run(X, y, groups, seeds=(0,), k=3, n_boot=50)

    assert res.ci_level_pct == CI_PERCENTILE_HI - CI_PERCENTILE_LO
    assert res.ci_level_pct == CI_LEVEL_PCT
    # And, today, that interval is the conventional 95%.
    assert res.ci_level_pct == 95.0


def test_resample_unit_row_is_recorded():
    X, y, groups = _synthetic()
    res = run(X, y, groups, seeds=(0,), k=3, n_boot=50, resample_unit="row")
    assert res.resample_unit == "row"


def test_align_groups_contiguous_and_missing():
    ids = ["a", "b", "c", "d"]
    mapping = {"a": "clZ", "b": "clZ", "c": "clQ", "d": "clZ"}
    g = align_groups(mapping, ids)
    # first-seen order: clZ->0, clQ->1
    assert list(g) == [0, 0, 1, 0]
    with pytest.raises(ValueError):
        align_groups({"a": "clZ"}, ids)


def _write_fixture(tmp_path, n_pos=9, n_neg=18):
    rng = np.random.default_rng(3)
    data = tmp_path / "data.csv"
    clusters = tmp_path / "clusters.tsv"
    cols = ["length", "charge", "gravy", "pI", "aromaticity"]
    lines = ["sequence_id,sequence,label," + ",".join(cols)]
    cl_lines = []
    idx = 0
    gid = 0
    for label, count, mu in ((1, n_pos, 0.7), (0, n_neg, -0.7)):
        for c in range(count):
            idx += 1
            sid = f"s{idx:04d}"
            feats = rng.normal(mu, 1.0, size=len(cols))
            lines.append(f"{sid},AAAA,{label}," + ",".join(f"{v:.6f}" for v in feats))
            cl_lines.append(f"{sid}\tcl{gid}")
            if c % 2 == 1:  # clusters of size ~2
                gid += 1
        gid += 1
    data.write_text("\n".join(lines) + "\n")
    clusters.write_text("\n".join(cl_lines) + "\n")
    return str(data), str(clusters)


def test_run_from_dataset_smoke(tmp_path):
    data_path, clusters_path = _write_fixture(tmp_path)
    res = run_from_dataset(data_path, clusters_path, seeds=(0, 1), k=3, n_boot=100)
    assert isinstance(res, EvalRun)
    assert res.representation == "physchem"
    assert res.n == 27 and res.pos == 9 and res.neg == 18
    assert res.data_sha256 is not None and len(res.data_sha256) == 64
    assert len(res.rows) == 3 * len(ALL_METRICS)


def test_run_from_dataset_rejects_non_physchem(tmp_path):
    data_path, clusters_path = _write_fixture(tmp_path)
    with pytest.raises(ValueError):
        run_from_dataset(data_path, clusters_path, representation="esm2_35m")
