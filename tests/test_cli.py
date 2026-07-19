"""Tests for the `permea` CLI dispatcher and the Diagnosis.to_dict() contract."""

from __future__ import annotations

import json

import numpy as np
import pytest

from permea_core.cli._format import render_text
from permea_core.cli.main import main
from permea_core.diagnose import diagnose
from permea_core.eval.bootstrap import CI_LEVEL_PCT
from permea_core.eval.run import EvalRun, MetricRow

REGISTRY_ORDER = ["PERMEA-W001", "PERMEA-W002", "PERMEA-W003",
                  "PERMEA-W101", "PERMEA-W501", "PERMEA-W502"]


# ---------------- fast, deterministic (hand-built EvalRun, no engine) ----------------
def _row(model, metric, *, delta, lo, hi, excl):
    return MetricRow(model=model, metric=metric, A_mean=0.6, A_std=0.01,
                     B_mean=0.6 + delta, B_std=0.01, delta_point=delta,
                     delta_boot_median=delta, ci_lo=lo, ci_hi=hi, ci_excludes_zero=excl)


def _run(**kw):
    return EvalRun(
        representation="physchem", threshold_label="NA", seeds=(0, 1), k=5, n_boot=2000,
        resample_unit=kw.get("resample_unit", "row"),
        headline_condition=kw.get("headline_condition", "A"),
        identity_definition=kw.get("identity_definition", None),
        n=2959, pos=269, neg=2690, n_clusters=kw.get("n_clusters", 40),
        data_sha256="a" * 64,
        rows=(_row("rf", "pr_auc", delta=-0.0444, lo=-0.0742, hi=-0.0068, excl=True),),
    )


def test_to_dict_shape_and_json_roundtrip():
    diag = diagnose(_run())
    d = diag.to_dict()
    # top-level closed shape
    assert set(d) == {"context", "summary", "fired"}
    # context is a closed shape too -- this is the canonical report contract, so a field
    # added or dropped here is a contract change and must be a deliberate edit to this line.
    assert set(d["context"]) == {
        "representation", "headline_condition", "identity_definition", "resample_unit",
        "ci_level_pct", "n", "pos", "neg", "n_clusters", "data_sha256",
    }
    # The CI level is carried as a real number, at the level the bootstrap actually used.
    assert d["context"]["ci_level_pct"] == CI_LEVEL_PCT == 95.0
    assert d["summary"]["total"] == len(d["fired"])
    # severity serialized as plain string, not an enum
    for f in d["fired"]:
        assert isinstance(f["severity"], str)
        assert set(f) == {"code", "title", "severity", "evidence", "evidence_str"}
    # every fired code is in the catalog order and present in the object
    assert [f["code"] for f in d["fired"]] == [w.code for w in diag.fired]
    # faithful JSON round-trip (no non-serializable leftovers)
    assert json.loads(json.dumps(d)) == d


def test_render_text_lists_codes_in_registry_order():
    diag = diagnose(_run(identity_definition=None, headline_condition="A",
                         resample_unit="row", n_clusters=40))
    text = render_text(diag, "fixture.csv")
    codes = [ln.split("]")[1].split()[0] for ln in text.splitlines() if ln.startswith("[")]
    assert codes == [c for c in REGISTRY_ORDER if c in codes]
    assert "PERMEA-W001" in codes  # identity None
    assert diag.fired[0].evidence_str in text


def test_render_text_no_warnings():
    clean = EvalRun(
        representation="physchem", threshold_label="NA", seeds=(0, 1), k=5, n_boot=2000,
        resample_unit="cluster", headline_condition="B",
        identity_definition={"alignment": "global"}, n=2959, pos=269, neg=2690,
        n_clusters=1000, data_sha256="a" * 64,
        rows=(_row("rf", "pr_auc", delta=-0.005, lo=-0.009, hi=-0.001, excl=True),),
    )
    assert "No warnings fired." in render_text(diagnose(clean), "x.csv")


# ---------------- CLI integration (real engine on a small fixture) ----------------
def _write_fixture(tmp_path, n_pos=12, n_neg=18):
    rng = np.random.default_rng(5)
    data = tmp_path / "data.csv"
    clusters = tmp_path / "clusters.tsv"
    cols = ["length", "charge", "gravy", "pI", "aromaticity"]
    lines = ["sequence_id,sequence,label," + ",".join(cols)]
    cl = []
    idx = 0
    gid = 0
    for label, count, mu in ((1, n_pos, 0.7), (0, n_neg, -0.7)):
        for c in range(count):
            idx += 1
            sid = f"s{idx:04d}"
            feats = rng.normal(mu, 1.0, size=len(cols))
            lines.append(f"{sid},AAAA,{label}," + ",".join(f"{v:.6f}" for v in feats))
            cl.append(f"{sid}\tcl{gid}")
            if c % 2 == 1:
                gid += 1
        gid += 1
    data.write_text("\n".join(lines) + "\n")
    clusters.write_text("\n".join(cl) + "\n")
    return str(data), str(clusters)


@pytest.fixture(scope="module")
def fixture(tmp_path_factory):
    return _write_fixture(tmp_path_factory.mktemp("cli"))


def test_cli_exit_zero_and_text(fixture, capsys):
    data, clusters = fixture
    rc = main(["bench", "diagnose", data, clusters, "--seeds", "2", "--k", "3", "--n-boot", "50"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "PermeaBench diagnose" in out
    assert "PERMEA-W001" in out  # identity not declared -> always fires


def test_cli_json_roundtrips(fixture, capsys):
    data, clusters = fixture
    rc = main(["bench", "diagnose", data, clusters, "--seeds", "2", "--k", "3",
               "--n-boot", "50", "--json"])
    out = capsys.readouterr().out
    assert rc == 0
    obj = json.loads(out)
    assert set(obj) == {"context", "summary", "fired"}
    assert obj["context"]["representation"] == "physchem"
    assert obj["summary"]["total"] == len(obj["fired"])


def test_cli_fail_on_warn(fixture, capsys):
    data, clusters = fixture
    rc = main(["bench", "diagnose", data, clusters, "--seeds", "2", "--k", "3",
               "--n-boot", "50", "--fail-on-warn"])
    capsys.readouterr()
    assert rc == 1  # W001 fires (no identity declared)


def test_cli_policy_override_reaches_diagnose(fixture, capsys):
    data, clusters = fixture
    # force W502 by demanding an absurd cluster count
    rc = main(["bench", "diagnose", data, clusters, "--seeds", "2", "--k", "3",
               "--n-boot", "0", "--min-clusters", "999999"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "PERMEA-W502" in out


def test_cli_output_file(fixture, tmp_path, capsys):
    data, clusters = fixture
    out_path = tmp_path / "diag.json"
    rc = main(["bench", "diagnose", data, clusters, "--seeds", "2", "--k", "3",
               "--n-boot", "50", "--json", "-o", str(out_path)])
    assert rc == 0
    assert capsys.readouterr().out.strip() == ""  # nothing to stdout
    obj = json.loads(out_path.read_text())
    assert set(obj) == {"context", "summary", "fired"}


def test_cli_non_physchem_exit_2(fixture, capsys):
    data, clusters = fixture
    rc = main(["bench", "diagnose", data, clusters, "--representation", "esm2_35m"])
    err = capsys.readouterr().err
    assert rc == 2
    assert "error" in err.lower()


def test_cli_missing_headline_exit_2(fixture, capsys):
    data, clusters = fixture
    rc = main(["bench", "diagnose", data, clusters, "--seeds", "2", "--k", "3",
               "--n-boot", "0", "--headline-model", "does_not_exist"])
    err = capsys.readouterr().err
    assert rc == 2
    assert "headline" in err.lower()


def test_cli_bad_identity_json_exit_2(fixture, capsys):
    data, clusters = fixture
    rc = main(["bench", "diagnose", data, clusters, "--identity-definition", "{not json"])
    err = capsys.readouterr().err
    assert rc == 2
    assert "identity-definition" in err.lower()
