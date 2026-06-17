from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW_DOCS = (
    "docs/review/README.md",
    "docs/review/public-review-packet.md",
    "docs/review/public-review-packet-template.md",
    "docs/review/public-review-packet-assembly.md",
    "docs/review/public-review-packet-governance.md",
    "docs/review/public-review-checklist.md",
)
TOUCHED_PUBLIC_FILES = (
    *REVIEW_DOCS,
    "schemas/public-review-packet.schema.json",
    "scripts/permea_review.py",
    "tests/test_public_review_packet_layer.py",
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/p-core-047-public-review-packet-layer-v0.md",
)
REQUIRED_PATH = (
    "README",
    "QUICKSTART",
    "REVIEW PACKET",
    "EVIDENCE",
    "BENCHMARKS",
    "DATASETS",
    "RESEARCH",
    "CLAIMS",
    "VALIDATION",
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
    "experimental " + "validation",
    "clinical " + "evidence",
    "expression " + "improvement",
)
BOUNDARY_MARKERS = (
    "no ",
    "not ",
    "does not ",
    "without ",
    "prohibited ",
    "out of scope",
    "not yet demonstrated",
    "future ",
    "requires future",
    "requiring future",
    "unsupported",
)


def test_public_review_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_review.py")]
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
    assert "Permea Core public review packet" in first
    assert "Public Review Packet Ready" in first
    assert "README -> QUICKSTART -> REVIEW PACKET -> EVIDENCE -> BENCHMARKS -> DATASETS -> RESEARCH -> CLAIMS -> VALIDATION" in first
    assert "python3 scripts/permea_review.py" in first
    assert "python3 scripts/permea_research.py" in first
    assert "python3 scripts/permea_validate.py" in first
    assert "Status: PASS" in first


def test_public_review_docs_exist_and_link_each_other() -> None:
    for path in REVIEW_DOCS:
        assert (ROOT / path).exists()

    readme = (ROOT / "docs/review/README.md").read_text(encoding="utf-8")
    for target in (
        "public-review-packet.md",
        "public-review-packet-template.md",
        "public-review-packet-assembly.md",
        "public-review-packet-governance.md",
        "public-review-checklist.md",
    ):
        assert target in readme


def test_schema_validity_and_required_fields() -> None:
    schema = json.loads(
        (ROOT / "schemas/public-review-packet.schema.json").read_text(
            encoding="utf-8"
        )
    )

    assert schema["type"] == "object"
    assert schema["title"] == "Permea Public Review Packet"
    for field in (
        "packet_id",
        "title",
        "purpose",
        "intended_reviewer",
        "review_objective",
        "required_reading_path",
        "required_commands",
        "linked_evidence",
        "linked_benchmarks",
        "linked_datasets",
        "linked_research_packages",
        "linked_claims",
        "validation_summary",
        "unsupported_claims",
        "limitations",
        "version",
    ):
        assert field in schema["required"]
        assert field in schema["properties"]


def test_packet_template_structure() -> None:
    template = (ROOT / "docs/review/public-review-packet-template.md").read_text(
        encoding="utf-8"
    )

    for heading in (
        "Packet ID",
        "Title",
        "Purpose",
        "Intended Reviewer",
        "Review Objective",
        "Required Reading Path",
        "Required Commands",
        "Evidence Summary",
        "Benchmark Summary",
        "Dataset Summary",
        "Research Package Summary",
        "Claim Boundary Summary",
        "Validation Summary",
        "Unsupported Claims",
        "Limitations",
        "Version",
        "Maintainer Notes",
    ):
        assert f"## {heading}" in template


def test_checklist_coverage() -> None:
    checklist = (ROOT / "docs/review/public-review-checklist.md").read_text(
        encoding="utf-8"
    )

    for heading in (
        "Repository Orientation",
        "Quickstart Execution",
        "Evidence Review",
        "Benchmark Review",
        "Dataset Review",
        "Research Package Review",
        "Claim Registry Review",
        "Validation / Reproducibility Review",
        "Unsupported Claims Review",
        "Public-Safety Boundary Review",
        "Final Reviewer Notes",
    ):
        assert f"## {heading}" in checklist


def test_required_review_path_coverage() -> None:
    packet = (ROOT / "docs/review/public-review-packet.md").read_text(
        encoding="utf-8"
    )
    assembly = (ROOT / "docs/review/public-review-packet-assembly.md").read_text(
        encoding="utf-8"
    )
    combined = f"{packet}\n{assembly}"

    path_text = " -> ".join(REQUIRED_PATH)
    assert path_text in combined
    for term in REQUIRED_PATH:
        assert term in combined


def test_public_safe_boundary_scan_for_touched_files() -> None:
    combined = _combined_touched_text()
    lowered = combined.lower()

    for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
        assert term.lower() not in lowered


def test_prohibited_claim_scan_for_touched_files() -> None:
    combined = _combined_touched_text()
    lowered = combined.lower()

    for phrase in PROHIBITED_AFFIRMATIVE_CLAIMS:
        phrase_lower = phrase.lower()
        for match in re.finditer(re.escape(phrase_lower), lowered):
            context = lowered[max(0, match.start() - 256) : match.end() + 160]
            assert any(marker in context for marker in BOUNDARY_MARKERS), context


def _combined_touched_text() -> str:
    return "\n".join(
        (ROOT / path).read_text(encoding="utf-8") for path in TOUCHED_PUBLIC_FILES
    )
