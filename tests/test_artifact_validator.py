from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.validator.checks import FAMILY_CHECKS, check_artifacts
from permea_core.validator.report import render_check_report

REQUIRED_NON_CLAIMS = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no clinical efficacy claim",
    "no model performance claim",
    "no SOTA claim",
    "no solved-delivery claim",
)

FORBIDDEN_PHRASES = (
    "AI " + "Champion",
    "H" + "100",
    "K-" + "EXAONE",
    "Chat" + "GPT",
    "Co" + "dex",
    "local" + "-only",
    "assigned " + "GPU",
    "cloud " + "credits",
    "API " + "key",
)


def test_validator_all_families_passes() -> None:
    report = check_artifacts(ROOT)
    assert report["status"] == "PASS"
    assert report["checked_families"] == list(FAMILY_CHECKS)
    assert report["failed_checks"] == []
    assert report["non_claim_boundary_status"] == "PASS"


def test_validator_each_required_family_passes() -> None:
    for family in FAMILY_CHECKS:
        report = check_artifacts(ROOT, family=family)
        assert report["status"] == "PASS"
        assert report["checked_families"] == [family]
        assert report["checked_files"]


def test_validator_report_structure_is_deterministic() -> None:
    report = check_artifacts(ROOT, family="dataset_card")
    rendered = render_check_report(report)
    assert rendered.startswith("PASS Permea artifact check\n")
    assert "Checked artifact families:" in rendered
    assert "Checked files:" in rendered
    assert "Failed checks:" in rendered
    assert "Warnings:" in rendered
    assert "Non-claim boundary status: PASS" in rendered


def test_validator_cli_all_exits_zero() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/permea_check.py", "--all"],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0
    assert "PASS Permea artifact check" in result.stdout
    assert "dataset_card" in result.stdout
    assert "output_package" in result.stdout


def test_validator_cli_family_exits_zero() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/permea_check.py", "--family", "evidence_card"],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0
    assert "docs/examples/generated/evidence_cards/" in result.stdout


def test_validation_docs_include_required_sections_and_non_claims() -> None:
    text = (ROOT / "docs/specs/VALIDATION.md").read_text(encoding="utf-8")
    for section in (
        "## Overview",
        "## Purpose",
        "## Supported artifact families",
        "## CLI usage",
        "## Validation checks",
        "## Report format",
        "## Expected PASS/FAIL behavior",
        "## How researchers/developers should use this",
        "## Claim-boundary validation",
        "## Limitations",
        "## Next evidence steps",
    ):
        assert section in text
    for claim in REQUIRED_NON_CLAIMS:
        assert claim in text


def test_documentation_links_to_validator() -> None:
    expected = "docs/specs/VALIDATION.md"
    for rel_path in ("README.md", "QUICKSTART.md", "EVALUATION.md", "REPRODUCIBILITY.md"):
        assert expected in (ROOT / rel_path).read_text(encoding="utf-8")
    assert "VALIDATION.md" in (ROOT / "docs/specs/README.md").read_text(encoding="utf-8")


def test_validator_public_text_avoids_forbidden_phrases() -> None:
    paths = [
        ROOT / "docs/specs/VALIDATION.md",
        ROOT / "docs/reports/p-core-038-artifact-validator-layer.md",
        ROOT / "scripts/permea_check.py",
        ROOT / "src/permea_core/validator/checks.py",
        ROOT / "src/permea_core/validator/report.py",
        ROOT / "tests/test_artifact_validator.py",
    ]
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for phrase in FORBIDDEN_PHRASES:
            assert phrase not in text
