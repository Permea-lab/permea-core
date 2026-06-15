from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.reproducibility.bundle import (
    ARTIFACT_LINEAGE,
    NON_CLAIMS,
    PASS,
    REQUIRED_REPORT_SECTIONS,
    collect_reproducibility_report,
    render_reproducibility_report,
    validate_reproducibility_bundle,
    write_reproducibility_report,
)


REQUIRED_JSON_KEYS = (
    "run_name",
    "generated_at",
    "commands",
    "generated_artifacts",
    "validation_checks",
    "artifact_lineage",
    "non_claims",
    "limitations",
    "status",
)

UNSUPPORTED_CLAIM_PHRASE_PARTS = (
    ("wet-lab", "validated"),
    ("clinical", "efficacy"),
    ("universal", "prediction"),
    ("AlphaFold-level", "maturity"),
    ("solved", "delivery"),
    ("bioRxiv", "readiness"),
    ("data has already been", "downloaded"),
    ("acquisition has been", "executed"),
    ("redistribution rights have been", "confirmed"),
    ("model performance has been", "measured"),
)


def test_reproducibility_report_generation_returns_pass() -> None:
    report = collect_reproducibility_report(ROOT)

    assert report["status"] == PASS
    assert report["run_name"] == "permea_core_public_reproducibility_bundle"


def test_report_markdown_includes_required_sections() -> None:
    rendered = render_reproducibility_report(collect_reproducibility_report(ROOT))

    for section in REQUIRED_REPORT_SECTIONS:
        assert section in rendered


def test_report_json_includes_required_keys(tmp_path: Path) -> None:
    result = write_reproducibility_report(tmp_path, ROOT)
    payload = json.loads((tmp_path / "REPRODUCIBILITY_REPORT.json").read_text())

    for key in REQUIRED_JSON_KEYS:
        assert key in payload
    assert payload["status"] == PASS
    assert payload["output_paths"] == result["output_paths"]


def test_artifact_lineage_matches_required_order() -> None:
    report = collect_reproducibility_report(ROOT)

    assert [item["path"] for item in report["artifact_lineage"]] == [
        path for _label, path in ARTIFACT_LINEAGE
    ]


def test_report_includes_explicit_non_claims() -> None:
    rendered = render_reproducibility_report(collect_reproducibility_report(ROOT))

    for claim in NON_CLAIMS:
        assert f"- {claim}" in rendered


def test_paths_are_relative_public_safe(tmp_path: Path) -> None:
    result = write_reproducibility_report(tmp_path, ROOT)
    rendered = render_reproducibility_report(result)

    assert str(ROOT) not in rendered
    for key in ("generated_artifacts", "artifact_lineage"):
        for item in result[key]:
            assert not item["path"].startswith("/")


def test_reproducibility_bundle_validation_passes() -> None:
    write_reproducibility_report(root_path=ROOT)
    result = validate_reproducibility_bundle(ROOT)

    assert result["status"] == PASS
    assert all(check["status"] == PASS for check in result["checks"])


def test_reproduce_cli_exits_zero() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "permea_reproduce.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS Permea public reproduction" in completed.stdout


def test_validate_cli_exits_zero() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "permea_reproduce.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "permea_validate.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS reproducibility bundle validation" in completed.stdout


def test_unsupported_claim_phrases_are_absent() -> None:
    rendered = render_reproducibility_report(collect_reproducibility_report(ROOT))
    payload = json.dumps(collect_reproducibility_report(ROOT), sort_keys=True)
    combined = f"{rendered}\n{payload}"

    for parts in UNSUPPORTED_CLAIM_PHRASE_PARTS:
        assert " ".join(parts) not in combined
