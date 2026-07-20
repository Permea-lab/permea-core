"""Tests for the diagnose rule engine (permea_core.diagnose)."""

from __future__ import annotations

import pytest

from permea_core.contracts.warnings import Severity
from permea_core.diagnose import DiagnosePolicy, diagnose
from permea_core.eval.bootstrap import CI_LEVEL_PCT
from permea_core.eval.run import EvalRun, MetricRow

GOOD_IDENTITY = {"alignment": "global", "denominator": "shorter_sequence", "gap_treatment": "free"}


def make_row(model, metric, *, delta_point, ci_lo, ci_hi, ci_excludes_zero):
    return MetricRow(
        model=model,
        metric=metric,
        A_mean=0.6,
        A_std=0.01,
        B_mean=0.6 + delta_point,
        B_std=0.01,
        delta_point=delta_point,
        delta_boot_median=delta_point,
        ci_lo=ci_lo,
        ci_hi=ci_hi,
        ci_excludes_zero=ci_excludes_zero,
    )


def make_run(
    *,
    headline=("rf", "pr_auc"),
    delta_point=-0.005,
    ci_lo=-0.008,
    ci_hi=-0.002,
    ci_excludes_zero=True,
    identity_definition=GOOD_IDENTITY,
    headline_condition="B",
    resample_unit="cluster",
    n_clusters=1000,
    n_boot=2000,
    ci_level_pct=CI_LEVEL_PCT,
    extra_rows=(),
):
    hm, hmet = headline
    rows = [make_row(hm, hmet, delta_point=delta_point, ci_lo=ci_lo, ci_hi=ci_hi,
                     ci_excludes_zero=ci_excludes_zero)]
    rows.extend(extra_rows)
    return EvalRun(
        representation="physchem",
        threshold_label="NA",
        seeds=(0, 1, 2, 3, 4),
        k=5,
        n_boot=n_boot,
        resample_unit=resample_unit,
        headline_condition=headline_condition,
        identity_definition=identity_definition,
        n=2959,
        pos=269,
        neg=2690,
        n_clusters=n_clusters,
        data_sha256="a" * 64,
        rows=tuple(rows),
        ci_level_pct=ci_level_pct,
    )


def fired_codes(diag):
    return [f.code for f in diag.fired]


def test_clean_run_fires_nothing():
    diag = diagnose(make_run())
    assert diag.fired == ()
    assert diag.summary.total == 0
    assert diag.context.headline_condition == "B"


def test_w001_identity_undeclared():
    assert "PERMEA-W001" in fired_codes(diagnose(make_run(identity_definition=None)))
    assert "PERMEA-W001" not in fired_codes(diagnose(make_run(identity_definition=GOOD_IDENTITY)))


def test_w002_headline_not_b():
    diag = diagnose(make_run(headline_condition="A"))
    assert "PERMEA-W002" in fired_codes(diag)
    assert "PERMEA-W002" not in fired_codes(diagnose(make_run(headline_condition="B")))


def test_w003_row_resampling():
    assert "PERMEA-W003" in fired_codes(diagnose(make_run(resample_unit="row")))
    assert "PERMEA-W003" not in fired_codes(diagnose(make_run(resample_unit="cluster")))


def test_w101_material_leakage_fires():
    diag = diagnose(make_run(delta_point=-0.0444, ci_lo=-0.0742, ci_hi=-0.0068,
                             ci_excludes_zero=True))
    codes = fired_codes(diag)
    assert "PERMEA-W101" in codes
    assert "PERMEA-W501" not in codes  # mutually exclusive on the headline row
    fw = next(f for f in diag.fired if f.code == "PERMEA-W101")
    assert fw.severity is Severity.CRITICAL
    assert fw.title == "material similarity leakage"
    assert fw.evidence.model == "rf" and fw.evidence.metric == "pr_auc"
    assert fw.evidence.delta_point == -0.0444
    assert fw.evidence.threshold_used == 0.02


def test_w101_materiality_floor_blocks_small_but_significant():
    # significant (CI excludes zero) but |delta| < 0.02 -> not material, and not inconclusive
    diag = diagnose(make_run(delta_point=-0.005, ci_lo=-0.009, ci_hi=-0.001,
                             ci_excludes_zero=True))
    assert "PERMEA-W101" not in fired_codes(diag)
    assert "PERMEA-W501" not in fired_codes(diag)


def test_w101_positive_delta_does_not_fire():
    diag = diagnose(make_run(delta_point=0.05, ci_lo=0.03, ci_hi=0.07, ci_excludes_zero=True))
    assert "PERMEA-W101" not in fired_codes(diag)


def test_w501_inconclusive_fires():
    diag = diagnose(make_run(delta_point=-0.03, ci_lo=-0.06, ci_hi=0.01, ci_excludes_zero=False))
    codes = fired_codes(diag)
    assert "PERMEA-W501" in codes
    assert "PERMEA-W101" not in codes


def test_nboot_zero_silences_w101_and_w501():
    diag = diagnose(make_run(delta_point=-0.05, ci_lo=None, ci_hi=None,
                             ci_excludes_zero=None, n_boot=0))
    codes = fired_codes(diag)
    assert "PERMEA-W101" not in codes
    assert "PERMEA-W501" not in codes


def test_w502_min_clusters_boundary():
    assert "PERMEA-W502" in fired_codes(diagnose(make_run(n_clusters=49)))
    assert "PERMEA-W502" not in fired_codes(diagnose(make_run(n_clusters=50)))
    assert "PERMEA-W502" not in fired_codes(diagnose(make_run(n_clusters=1000)))


def test_missing_headline_raises():
    run = make_run(headline=("logreg", "roc_auc"))  # no (rf, pr_auc) row
    with pytest.raises(ValueError):
        diagnose(run)


def test_custom_policy_headline_and_thresholds():
    run = make_run(headline=("logreg", "mcc"), delta_point=-0.03,
                   ci_lo=-0.05, ci_hi=-0.01, ci_excludes_zero=True, n_clusters=200)
    pol = DiagnosePolicy(headline_model="logreg", headline_metric="mcc",
                         materiality_min_abs_delta=0.01, min_clusters=300)
    codes = fired_codes(diagnose(run, pol))
    assert "PERMEA-W101" in codes  # 0.03 >= 0.01 materiality
    assert "PERMEA-W502" in codes  # 200 < 300


def test_severity_summary_counts():
    # fire W001 (critical), W003 (warn), W101 (critical), W502 (warn)
    diag = diagnose(make_run(identity_definition=None, resample_unit="row",
                             delta_point=-0.0444, ci_lo=-0.07, ci_hi=-0.01,
                             ci_excludes_zero=True, n_clusters=40))
    assert diag.summary.critical == 2
    assert diag.summary.warn == 2
    assert diag.summary.info == 0
    assert diag.summary.total == 4


def test_fired_in_fixed_registry_order():
    diag = diagnose(make_run(identity_definition=None, headline_condition="A",
                             delta_point=-0.0444, ci_lo=-0.07, ci_hi=-0.01,
                             ci_excludes_zero=True, n_clusters=40))
    assert fired_codes(diag) == ["PERMEA-W001", "PERMEA-W002", "PERMEA-W101", "PERMEA-W502"]


def test_determinism():
    run = make_run(identity_definition=None, resample_unit="row",
                   delta_point=-0.0444, ci_lo=-0.07, ci_hi=-0.01,
                   ci_excludes_zero=True, n_clusters=40)
    assert diagnose(run) == diagnose(run)


def test_evidence_str_contains_only_numbers():
    diag = diagnose(make_run(delta_point=-0.0444, ci_lo=-0.0742, ci_hi=-0.0068,
                             ci_excludes_zero=True))
    fw = next(f for f in diag.fired if f.code == "PERMEA-W101")
    s = fw.evidence_str
    assert "rf/pr_auc" in s
    assert "-0.0444" in s and "-0.0742" in s and "-0.0068" in s and "0.02" in s


# --------------------------------------------------------------------------------------
# Confidence level: carried as a real number, sourced from the bootstrap
# --------------------------------------------------------------------------------------
def test_context_carries_the_confidence_level():
    diag = diagnose(make_run())
    assert diag.context.ci_level_pct == CI_LEVEL_PCT == 95.0
    assert diag.to_dict()["context"]["ci_level_pct"] == 95.0


def test_confidence_level_is_echoed_from_the_run_not_reinvented():
    """diagnose never computes the level -- it reports whatever the run recorded."""
    diag = diagnose(make_run(ci_level_pct=90.0))
    assert diag.context.ci_level_pct == 90.0


def test_evidence_str_derives_its_ci_label_from_the_run():
    """The '95%' in the evidence string is the run's level, not a literal in the template."""
    w101 = diagnose(make_run(delta_point=-0.0444, ci_lo=-0.0742, ci_hi=-0.0068,
                             ci_excludes_zero=True))
    assert "95% CI" in next(f for f in w101.fired if f.code == "PERMEA-W101").evidence_str

    w501 = diagnose(make_run(ci_lo=-0.01, ci_hi=0.02, ci_excludes_zero=False))
    assert "95% CI" in next(f for f in w501.fired if f.code == "PERMEA-W501").evidence_str

    # Change the level and the prose follows -- 95 is nowhere hardcoded.
    shifted = diagnose(make_run(delta_point=-0.0444, ci_lo=-0.0742, ci_hi=-0.0068,
                                ci_excludes_zero=True, ci_level_pct=99.0))
    s = next(f for f in shifted.fired if f.code == "PERMEA-W101").evidence_str
    assert "99% CI" in s and "95%" not in s


def test_ci_label_degrades_cleanly_without_a_level():
    diag = diagnose(make_run(delta_point=-0.0444, ci_lo=-0.0742, ci_hi=-0.0068,
                             ci_excludes_zero=True, ci_level_pct=None))
    s = next(f for f in diag.fired if f.code == "PERMEA-W101").evidence_str
    assert "CI [" in s and "% CI" not in s
    assert diag.to_dict()["context"]["ci_level_pct"] is None
