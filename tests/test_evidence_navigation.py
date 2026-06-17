from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DOCS = (
    "docs/evidence/evidence-map.md",
    "docs/evidence/claim-to-evidence-matrix.md",
    "docs/evidence/evidence-maturity-model.md",
    "docs/evidence/evidence-timeline.md",
    "docs/evidence/README.md",
    "docs/evidence/evidence-index.md",
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "scripts/permea_evidence.py",
)
EXPECTED_EVIDENCE_IDS = (
    "EVIDENCE-030",
    "EVIDENCE-032",
    "EVIDENCE-034",
    "EVIDENCE-036",
    "EVIDENCE-038",
    "EVIDENCE-040",
    "EVIDENCE-042",
    "EVIDENCE-043",
)
REQUIRED_MATRIX_STATUSES = (
    "Supported by Computational Evidence",
    "Partial Evidence",
    "Not Yet Demonstrated",
    "Out of Scope",
)
PROHIBITED_PUBLIC_SAFETY_TERMS = (
    "AI " + "Champion",
    "H" + "100",
    "KO" + "RA",
    "private " + "infrastructure",
    "sponsor" + "ship",
    "cloud " + "credits",
    "private " + "repositories",
    "local-only " + "workflows",
    "Chat" + "GPT",
    "Co" + "dex",
)
PROHIBITED_AFFIRMATIVE_CLAIMS = (
    "wet-lab " + "validation",
    "biological " + "efficacy",
    "therapeutic " + "outcomes",
    "BBB " + "success",
    "solved " + "delivery",
    "SOTA " + "performance",
    "experimental " + "validation",
)
BOUNDARY_MARKERS = (
    "no ",
    "not ",
    "does not ",
    "without ",
    "unsupported ",
    "out of scope",
    "level 5",
    "future evidence",
)


def test_evidence_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_evidence.py")]
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
    assert "Permea Core evidence navigation" in first
    assert "Evidence inventory:" in first
    assert "Claim boundaries:" in first
    assert "Evidence maturity:" in first
    assert "Validation status:" in first
    assert "Status: PASS" in first


def test_evidence_inventory_structure_contains_current_ids() -> None:
    evidence_map = (ROOT / "docs/evidence/evidence-map.md").read_text(encoding="utf-8")

    for evidence_id in EXPECTED_EVIDENCE_IDS:
        assert evidence_id in evidence_map
        assert evidence_id in (ROOT / "docs/evidence/evidence-index.md").read_text(
            encoding="utf-8"
        )

    assert "Evidence ID | Evidence title | Related reports" in evidence_map
    assert "Where Future Evidence Should Accumulate" in evidence_map


def test_claim_matrix_uses_required_statuses() -> None:
    matrix = (ROOT / "docs/evidence/claim-to-evidence-matrix.md").read_text(
        encoding="utf-8"
    )

    for status in REQUIRED_MATRIX_STATUSES:
        assert status in matrix
    for claim in (
        "Sequence-derived signal",
        "Candidate prioritization",
        "Public artifact surfaces can be reproduced locally",
        "Specification compliance can be inspected with local validators",
    ):
        assert claim in matrix


def test_maturity_model_references_all_levels_and_current_assets() -> None:
    model = (ROOT / "docs/evidence/evidence-maturity-model.md").read_text(
        encoding="utf-8"
    )

    for level in range(7):
        assert f"Level {level}" in model
    for asset in (
        "Reproducibility bundle",
        "Evaluation bundle",
        "Artifact validator bundle",
        "Evidence navigation layer",
    ):
        assert asset in model


def test_public_safe_boundary_scan_for_evidence_navigation_files() -> None:
    combined = _combined_evidence_text()
    lowered = combined.lower()

    for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
        assert term.lower() not in lowered

    for phrase in PROHIBITED_AFFIRMATIVE_CLAIMS:
        phrase_lower = phrase.lower()
        start = 0
        while True:
            index = lowered.find(phrase_lower, start)
            if index == -1:
                break
            context = lowered[max(0, index - 256) : index + len(phrase_lower) + 160]
            assert any(marker in context for marker in BOUNDARY_MARKERS), context
            start = index + len(phrase_lower)


def _combined_evidence_text() -> str:
    return "\n".join(
        (ROOT / path).read_text(encoding="utf-8") for path in EVIDENCE_DOCS
    )
