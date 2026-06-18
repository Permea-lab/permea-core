from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINEAGE_DOCS = (
    "docs/lineage/README.md",
    "docs/lineage/lineage-model.md",
    "docs/lineage/lineage-governance.md",
    "docs/lineage/lineage-review-guide.md",
    "docs/lineage/lineage-record-template.md",
)
TOUCHED_PUBLIC_FILES = (
    *LINEAGE_DOCS,
    "schemas/lineage-record.schema.json",
    "scripts/permea_lineage.py",
    "tests/test_evidence_lineage_layer.py",
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/p-core-050-evidence-lineage-layer-v0.md",
)
REQUIRED_SCHEMA_FIELDS = (
    "lineage_record_id",
    "artifact_type",
    "artifact_id",
    "parent_artifacts",
    "child_artifacts",
    "related_claims",
    "lineage_status",
    "provenance_notes",
    "version",
)
ALLOWED_LINEAGE_STATUSES = (
    "draft",
    "documented",
    "linked",
    "reviewed",
    "superseded",
    "archived",
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
    "framework-only",
    "computational-only",
    "do not ",
)


def test_lineage_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_lineage.py")]
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
    assert "Permea Core evidence lineage" in first
    assert "Lineage Framework Ready" in first
    assert "Registered lineage-capable artifact classes: 10" in first
    assert "External Evidence Packages" in first
    assert "Status: PASS" in first


def test_lineage_docs_exist_and_link_each_other() -> None:
    for path in LINEAGE_DOCS:
        assert (ROOT / path).exists()

    readme = (ROOT / "docs/lineage/README.md").read_text(encoding="utf-8")
    for target in (
        "lineage-model.md",
        "lineage-governance.md",
        "lineage-review-guide.md",
        "lineage-record-template.md",
    ):
        assert target in readme


def test_lineage_schema_validity_required_fields_and_statuses() -> None:
    schema = json.loads(
        (ROOT / "schemas/lineage-record.schema.json").read_text(encoding="utf-8")
    )

    assert schema["title"] == "Permea Lineage Record"
    assert schema["type"] == "object"
    assert tuple(schema["properties"]["lineage_status"]["enum"]) == ALLOWED_LINEAGE_STATUSES
    for field in REQUIRED_SCHEMA_FIELDS:
        assert field in schema["required"]
        assert field in schema["properties"]


def test_lineage_template_structure() -> None:
    template = (ROOT / "docs/lineage/lineage-record-template.md").read_text(
        encoding="utf-8"
    )

    for heading in (
        "Lineage Record ID",
        "Artifact Type",
        "Artifact ID",
        "Parent Artifacts",
        "Child Artifacts",
        "Related Evidence",
        "Related Benchmarks",
        "Related Datasets",
        "Related Research Packages",
        "Related Review Packets",
        "Related External Evidence Packages",
        "Related Claims",
        "Related Specifications",
        "Validation Artifacts",
        "Provenance Notes",
        "Lineage Status",
        "Version",
        "Maintainer Notes",
    ):
        assert f"## {heading}" in template
    for status in ALLOWED_LINEAGE_STATUSES:
        assert f"- {status}" in template


def test_readme_and_review_hub_lineage_path_coverage() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    open_first = (ROOT / "OPEN_THIS_FIRST.md").read_text(encoding="utf-8")
    review_hub = (ROOT / "REVIEW_HUB.md").read_text(encoding="utf-8")

    assert "LINEAGE" in readme
    assert "scripts/permea_lineage.py" in readme
    assert "README -> QUICKSTART -> REVIEW PACKET -> RESEARCH -> DATASETS -> BENCHMARKS -> EVIDENCE -> CLAIMS -> LINEAGE -> VALIDATION" in readme
    assert "Evidence Lineage Layer: Implemented" in open_first
    assert "Evidence Lineage Layer" in review_hub
    assert "scripts/permea_lineage.py" in review_hub


def test_lineage_model_and_review_guide_cover_required_topics() -> None:
    model = (ROOT / "docs/lineage/lineage-model.md").read_text(encoding="utf-8")
    guide = (ROOT / "docs/lineage/lineage-review-guide.md").read_text(
        encoding="utf-8"
    )

    for phrase in (
        "Evidence",
        "Benchmarks",
        "Benchmark Runs",
        "Datasets",
        "Research Packages",
        "Review Packets",
        "External Evidence Packages",
        "Claims",
        "Specifications",
        "Validation Artifacts",
        "Lineage presence does not imply biological validity, efficacy, or experimental confirmation.",
    ):
        assert phrase in model

    for phrase in (
        "README -> REVIEW PACKET -> RESEARCH -> DATASETS -> BENCHMARKS -> EVIDENCE -> CLAIMS -> LINEAGE",
        "Lineage Completeness Checks",
        "Provenance Checks",
        "Unsupported Claim Checks",
        "Limitations Review",
    ):
        assert phrase in guide


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
