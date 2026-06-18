from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.consistency.artifacts import (  # noqa: E402
    PASS,
    Artifact,
    _missing_local_link_issues,
    discover_artifacts,
    validate_artifact_consistency,
)

TOUCHED_PUBLIC_FILES = (
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/architecture/README.md",
    "docs/artifacts/README.md",
    "docs/reports/README.md",
    "docs/reports/p-core-053-artifact-consistency-system-v0.md",
    "scripts/permea_artifacts.py",
    "src/permea_core/consistency/artifacts.py",
    "tests/test_artifact_consistency_system.py",
    "tests/test_review_navigation_consistency.py",
)
PROHIBITED_PUBLIC_SAFETY_TERMS = (
    "AI " + "Champion",
    "H" + "100",
    "K-" + "EXAONE",
    "KO" + "RA",
    "private " + "doctrine",
    "private " + "infrastructure",
    "sponsor" + "ship",
    "cloud " + "credits",
    "private " + "repositories",
    "local-only " + "workflows",
    "Chat" + "GPT",
    "Co" + "dex",
    "prompt " + "workflow",
    "private " + "handoff",
)
PROHIBITED_AFFIRMATIVE_CLAIMS = (
    "wet-lab " + "validation",
    "biological " + "efficacy",
    "therapeutic " + "outcomes",
    "BBB " + "success",
    "solved " + "delivery",
    "SOTA " + "performance",
    "clinical " + "efficacy",
    "clinical " + "evidence",
    "in-vivo",
    "in vivo",
)
BOUNDARY_MARKERS = (
    "no ",
    "not ",
    "does not ",
    "do not ",
    "without ",
    "prohibited ",
    "out of scope",
    "not yet demonstrated",
    "future ",
    "non-claim",
)


def test_artifact_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts/permea_artifacts.py")]
    first = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout
    second = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout

    assert first == second
    assert "Permea Core artifact consistency" in first
    assert "Artifact Consistency System Ready" in first
    assert "Status: PASS" in first
    assert "Consistency issues: 0" in first


def test_artifact_cli_json_output_is_structurally_valid() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/permea_artifacts.py"), "--json"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    payload = json.loads(completed.stdout)

    assert payload["status"] == PASS
    assert payload["issue_count"] == 0
    assert payload["artifact_count"] >= 80
    assert "docs/artifacts/README.md" in payload["required_review_surfaces"]


def test_artifact_inventory_discovers_public_surfaces() -> None:
    paths = {artifact.path for artifact in discover_artifacts(ROOT)}

    for expected in (
        "README.md",
        "OPEN_THIS_FIRST.md",
        "REVIEW_HUB.md",
        "docs/artifacts/README.md",
        "docs/architecture/README.md",
        "docs/reports/README.md",
        "docs/reports/p-core-053-artifact-consistency-system-v0.md",
        "docs/evidence/evidence-map.md",
    ):
        assert expected in paths


def test_current_repo_artifact_consistency_passes() -> None:
    result = validate_artifact_consistency(ROOT)

    assert result["status"] == PASS
    assert result["issue_count"] == 0
    assert result["artifact_count"] >= 80


def test_missing_local_link_detection_on_synthetic_artifact(tmp_path: Path) -> None:
    source = tmp_path / "README.md"
    source.write_text(
        "# Synthetic\n\n[Missing target](docs/missing.md)\n[Anchor](#local)\n",
        encoding="utf-8",
    )

    issues = _missing_local_link_issues(tmp_path, [Artifact("README.md", "root")])

    assert len(issues) == 1
    assert issues[0].code == "MISSING_LINK"
    assert "docs/missing.md" in issues[0].message


def test_reports_index_covers_all_public_reports() -> None:
    reports_index = (ROOT / "docs/reports/README.md").read_text(encoding="utf-8")

    for report in sorted((ROOT / "docs/reports").glob("*.md")):
        if report.name == "README.md":
            continue
        assert report.name in reports_index


def test_public_safe_boundary_scan_for_artifact_consistency_files() -> None:
    lowered = _combined_touched_text().lower()

    for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
        assert term.lower() not in lowered


def test_prohibited_claim_scan_for_artifact_consistency_files() -> None:
    lowered = _combined_touched_text().lower()

    for phrase in PROHIBITED_AFFIRMATIVE_CLAIMS:
        phrase_lower = phrase.lower()
        for match in re.finditer(re.escape(phrase_lower), lowered):
            context = lowered[max(0, match.start() - 256) : match.end() + 160]
            assert any(marker in context for marker in BOUNDARY_MARKERS), context


def _combined_touched_text() -> str:
    return "\n".join(
        (ROOT / path).read_text(encoding="utf-8") for path in TOUCHED_PUBLIC_FILES
    )
