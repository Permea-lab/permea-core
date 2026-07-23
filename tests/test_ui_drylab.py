"""Tests for the Drylab web UI layer (permea_ui).

The load-bearing claims here are not "the server returns 200". They are:
  - the demo's W501 -> W101 flip is a real property of the engine, not a story we tell;
  - narration that fails a guardrail is never rendered, in any failure mode;
  - the UI is downstream of everything and upstream of nothing.
"""

from __future__ import annotations

import ast
import json
import logging
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from permea_core.contracts.warnings import Status, WARNINGS
from permea_explain import guardrails
from permea_explain.providers.base import ProviderResponse
from permea_ui import fixtures, runner
from permea_ui.app import app

ROOT = Path(__file__).resolve().parents[1]

#: Matches the settings fixtures._FAMILY_SIZE was chosen against. Lowering n_boot here
#: would widen the CIs and could flip W501/W101 on its own -- which is precisely the
#: confound the flip test exists to rule out.
RUN_KW = {"seeds": 2, "k": 3, "n_boot": 400}


@pytest.fixture(scope="module")
def example(tmp_path_factory) -> dict[str, Path]:
    return fixtures.write_example(tmp_path_factory.mktemp("drylab_example"))


class FakeProvider:
    """Returns canned text so guardrail behaviour can be tested without a live model."""

    name = "fake"
    model_id = "fake-model"

    def __init__(self, text: str) -> None:
        self._text = text

    def complete(self, system, user, *, max_tokens, temperature=None, stop=None):
        return ProviderResponse(text=self._text, provider=self.name, model_id=self.model_id)


# --------------------------------------------------------------------------------------
# The demo claim
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "clustering,expected",
    [("naive", "PERMEA-W501"), ("family", "PERMEA-W101")],
)
def test_clustering_honesty_flips_the_verdict(example, clustering, expected):
    """Same rows, same settings, same code -- only the cluster assignment differs.

    This is the demo. If it ever fails, the fixture has drifted and the demo is telling a
    story the engine no longer supports; fix the fixture, never the assertion.
    """
    diagnosis = runner.run_diagnosis(
        example["dataset"], example[clustering],
        identity_definition={"alignment": "global"}, **RUN_KW,
    )
    codes = [f["code"] for f in diagnosis["fired"]]
    assert expected in codes, f"{clustering} clustering fired {codes}, expected {expected}"


def test_flip_holds_the_dataset_constant(example):
    """The two runs must differ only in clustering -- same data, same n, same cluster count.

    Without this, the flip could be dismissed as "the second run used different data".
    """
    a = runner.run_diagnosis(example["dataset"], example["naive"], **RUN_KW)
    b = runner.run_diagnosis(example["dataset"], example["family"], **RUN_KW)
    for key in ("data_sha256", "n", "pos", "neg", "n_clusters"):
        assert a["context"][key] == b["context"][key], f"{key} differs between the two runs"


# --------------------------------------------------------------------------------------
# Narration is never rendered unless it passed
# --------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def diagnosis(example) -> dict:
    return runner.run_diagnosis(
        example["dataset"], example["family"],
        identity_definition={"alignment": "global"}, **RUN_KW,
    )


def test_guardrail_failure_yields_withheld_and_no_text(diagnosis):
    bad = "정확도는 99.7% 였고 PERMEA-W999 경고가 발생했습니다."
    n = runner.narrate_diagnosis(diagnosis, provider=FakeProvider(bad))
    assert n.status == "withheld"
    assert n.text is None, "withheld narration must not carry renderable prose"
    assert "offending output" not in (n.detail or ""), "detail must not leak the bad prose"


def test_narration_quoting_the_data_sha256_is_not_withheld(diagnosis):
    """A narration that faithfully quotes the report's data_sha256 must render, not be withheld.

    Regression for #0030 over the demo fixture (fixtures._SEED = 20260721), whose sha256 is
    digit-first -- 41dba61b...8004d. The old identifier strip left that leading "41" behind as
    a bare, untraceable number, so the number-provenance gate withheld the narration ~1 in 4
    live runs. Symmetric blanking removes the hash whole. No live API: the hash is the only
    numeric-looking content and a FakeProvider supplies the prose.
    """
    sha = diagnosis["context"]["data_sha256"]
    text = f"이 진단의 데이터 해시는 {sha} 입니다."
    # The crux: the quoted hash contributes no standalone numeric token for the gate to check.
    assert guardrails.numbers_in_narrative(text) == []
    n = runner.narrate_diagnosis(diagnosis, provider=FakeProvider(text))
    assert n.status == "ok", f"expected ok, got {n.status}: {n.detail}"
    assert n.text == text


def test_withheld_narration_logs_offending_prose_for_operator(diagnosis, caplog):
    """Design 1 (#0034): a withheld narration's offending prose is logged SERVER-SIDE for
    operator adjudication, while the returned Narration -- and therefore the HTTP response --
    still carries none of it. The browser redaction is unchanged; only observability is added.
    """
    bad = "정확도는 99.7% 였고 PERMEA-W999 경고가 발생했습니다."  # fabricated number + unfired code
    with caplog.at_level(logging.WARNING, logger="permea_ui.narration"):
        n = runner.narrate_diagnosis(diagnosis, provider=FakeProvider(bad))

    # What the browser gets: withheld, no prose, no offending text leaked into the detail.
    assert n.status == "withheld"
    assert n.text is None, "withheld narration must not carry renderable prose"
    assert "offending output" not in (n.detail or "")
    assert bad not in (n.detail or ""), "offending prose must not reach the returned Narration"

    # What the operator gets: the full offending prose, on the dedicated server-side logger.
    records = [r for r in caplog.records if r.name == "permea_ui.narration"]
    assert records, "expected a WARNING on the 'permea_ui.narration' logger"
    logged = "\n".join(r.getMessage() for r in records)
    assert bad in logged, "offending prose must be present in the operator log"
    assert "source_report_sha256=" in logged, "log must carry the report hash for adjudication"


def test_missing_credentials_yields_unavailable(diagnosis, monkeypatch):
    for var in ("PERMEA_LLM_TOKEN", "PERMEA_LLM_ENDPOINT_ID", "PERMEA_LLM_BASE_URL"):
        monkeypatch.delenv(var, raising=False)
    n = runner.narrate_diagnosis(diagnosis)
    assert n.status == "unavailable"
    assert n.text is None


def test_transport_failure_yields_error_not_an_exception(diagnosis):
    class Boom:
        name, model_id = "boom", "boom-1"

        def complete(self, *a, **kw):
            raise TimeoutError("upstream timed out")

    n = runner.narrate_diagnosis(diagnosis, provider=Boom())
    assert n.status == "error"
    assert n.text is None
    assert "TimeoutError" in (n.detail or "")


def test_only_ok_status_ever_carries_text(diagnosis, monkeypatch):
    """Whatever the status, text is non-None only for `ok`. The UI keys off this.

    The `None` case must stay offline: with the three vars set it would select the
    configured provider and bill a real call from the test suite. Cleared here so the
    branch deterministically takes the `unavailable` path, as at
    test_missing_credentials_yields_unavailable.
    """
    for var in ("PERMEA_LLM_TOKEN", "PERMEA_LLM_ENDPOINT_ID", "PERMEA_LLM_BASE_URL"):
        monkeypatch.delenv(var, raising=False)
    for provider in (FakeProvider("정확도는 99.7% 입니다."), None):
        n = runner.narrate_diagnosis(diagnosis, provider=provider)
        assert (n.text is not None) == (n.status == "ok")


# --------------------------------------------------------------------------------------
# Input contract
# --------------------------------------------------------------------------------------
_GOOD_HEADER = "sequence_id,sequence,label,length,charge,gravy,pI,aromaticity"


def _write(tmp_path, csv_text, tsv_text):
    (tmp_path / "d.csv").write_text(csv_text)
    (tmp_path / "c.tsv").write_text(tsv_text)
    return tmp_path / "d.csv", tmp_path / "c.tsv"


@pytest.mark.parametrize(
    "csv_text,tsv_text,needle",
    [
        ("sequence_id,sequence,label\nx,AAA,1\n", "x\tc1\n", "missing required column"),
        (_GOOD_HEADER + "\n", "x\tc1\n", "no data rows"),
        (_GOOD_HEADER + "\nx,A,1,1,1,1,1,1\ny,A,0,1,1,1,1,1\n", "x\tc1\n",
         "no row in the cluster"),
        (_GOOD_HEADER + "\nx,A,1,1,1,1,1,1\n", "", "Cluster TSV is empty"),
    ],
)
def test_bad_input_is_rejected_with_an_actionable_message(tmp_path, csv_text, tsv_text, needle):
    ds, cl = _write(tmp_path, csv_text, tsv_text)
    with pytest.raises(runner.InputError) as exc:
        runner.validate_inputs(ds, cl)
    assert needle in str(exc.value)


def test_valid_example_passes_validation(example):
    runner.validate_inputs(example["dataset"], example["family"])  # must not raise


def test_upload_endpoint_rejects_bad_input_before_queueing(tmp_path):
    ds, cl = _write(tmp_path, "sequence_id,sequence,label\nx,AAA,1\n", "x\tc1\n")
    with TestClient(app) as client:
        r = client.post(
            "/api/jobs",
            files={"dataset": ds.open("rb"), "clusters": cl.open("rb")},
        )
    assert r.status_code == 400
    assert "missing required column" in r.json()["detail"]


# --------------------------------------------------------------------------------------
# Registry surface + disclosure
# --------------------------------------------------------------------------------------
def test_catalog_exposes_reserved_codes_too():
    """Reserved codes must reach the client. A viewer who cannot see that W403/W404 have
    no firing logic will read a clean report as a broader all-clear than it is."""
    with TestClient(app) as client:
        codes = client.get("/api/warnings").json()["codes"]
    by_code = {c["code"]: c for c in codes}
    assert len(codes) == len(WARNINGS)
    assert by_code["PERMEA-W403"]["status"] == str(Status.RESERVED)
    assert by_code["PERMEA-W404"]["status"] == str(Status.RESERVED)
    assert {c["code"] for c in codes if c["status"] == str(Status.ACTIVE)} == {
        w.code for w in WARNINGS if w.status is Status.ACTIVE
    }


def test_example_label_disclaims_the_synthetic_data():
    with TestClient(app) as client:
        label = client.get("/api/status").json()["example_label"]
    assert "B3Pred" in label and "SYNTHETIC" in label.upper()


def test_model_identity_is_not_served_to_clients(diagnosis):
    """The configured adapter hides which model answers; the UI must not undo that."""
    from permea_ui.app import _narration_payload

    n = runner.narrate_diagnosis(diagnosis, provider=FakeProvider("숫자 없는 문장입니다."))
    payload = _narration_payload(n)
    assert "model_id" not in payload
    assert payload["authoritative"] is False
    assert "fake-model" not in json.dumps(payload)


# --------------------------------------------------------------------------------------
# Dependency direction
# --------------------------------------------------------------------------------------
def _imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            found.add(node.module.split(".")[0])
    return found


def test_engine_and_explain_never_import_the_ui():
    """permea_ui is a viewer. Nothing upstream may depend on it."""
    offenders = [
        str(p.relative_to(ROOT))
        for root in (ROOT / "src" / "permea_core", ROOT / "permea_explain")
        for p in root.rglob("*.py")
        if "permea_ui" in _imports(p)
    ]
    assert not offenders, f"upstream packages import permea_ui: {offenders}"


def test_importing_the_engine_does_not_pull_the_web_stack():
    """A `permea bench diagnose` install must not need fastapi to exist."""
    import subprocess

    code = (
        "import sys, permea_core.diagnose, permea_core.eval.run\n"
        "banned = {'permea_ui','fastapi','uvicorn','starlette'}\n"
        "bad = sorted(m for m in sys.modules if m.split('.')[0] in banned)\n"
        "print(';'.join(bad)); sys.exit(1 if bad else 0)\n"
    )
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert r.returncode == 0, f"engine import pulled the web stack: {r.stdout.strip()!r}"
