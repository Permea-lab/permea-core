from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH_DOCS = (
    "docs/research/README.md",
    "docs/research/research-package-registry.md",
    "docs/research/research-package-lifecycle.md",
    "docs/research/research-package-template.md",
    "docs/research/research-package-governance.md",
    "docs/research/research-package-assembly.md",
)
TOUCHED_PUBLIC_FILES = (
    *RESEARCH_DOCS,
    "schemas/research-package.schema.json",
    "scripts/permea_research.py",
    "tests/test_research_package_layer.py",
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/p-core-046-research-package-layer-v0.md",
)
REQUIRED_STATUSES = (
    "Proposed",
    "Draft Package",
    "Internally Reproducible",
    "Public Review Package",
    "External Review Ready",
    "Submitted",
    "Published",
    "Superseded",
    "Archived",
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


def test_research_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_research.py")]
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
    assert "Permea Core research package registry" in first
    assert "Research Package Framework Ready" in first
    assert "Registered research packages: 1" in first
    assert "Active/public-review research packages: 0" in first
    assert "Proposed research packages: 1" in first
    assert "Draft research packages: 0" in first
    assert "Submitted research packages: 0" in first
    assert "Published research packages: 0" in first
    assert "Status: PASS" in first


def test_research_docs_exist_and_link_each_other() -> None:
    for path in RESEARCH_DOCS:
        assert (ROOT / path).exists()

    readme = (ROOT / "docs/research/README.md").read_text(encoding="utf-8")
    for target in (
        "research-package-registry.md",
        "research-package-lifecycle.md",
        "research-package-template.md",
        "research-package-assembly.md",
        "research-package-governance.md",
    ):
        assert target in readme


def test_schema_validity_and_required_fields() -> None:
    schema = json.loads(
        (ROOT / "schemas/research-package.schema.json").read_text(encoding="utf-8")
    )

    assert schema["type"] == "object"
    assert schema["title"] == "Permea Research Package"
    for field in (
        "research_package_id",
        "title",
        "purpose",
        "package_type",
        "status",
        "linked_evidence",
        "linked_benchmarks",
        "linked_datasets",
        "linked_specifications",
        "linked_claims",
        "reproducibility_status",
        "validation_status",
        "claim_boundaries",
        "limitations",
        "version",
    ):
        assert field in schema["required"]
        assert field in schema["properties"]


def test_lifecycle_statuses_match_schema_statuses() -> None:
    lifecycle = (ROOT / "docs/research/research-package-lifecycle.md").read_text(
        encoding="utf-8"
    )
    schema = json.loads(
        (ROOT / "schemas/research-package.schema.json").read_text(encoding="utf-8")
    )
    schema_statuses = tuple(schema["properties"]["status"]["enum"])

    assert schema_statuses == REQUIRED_STATUSES
    for status in REQUIRED_STATUSES:
        assert status in lifecycle


def test_registry_structure_contains_required_columns_and_entries() -> None:
    registry = (ROOT / "docs/research/research-package-registry.md").read_text(
        encoding="utf-8"
    )

    for heading in (
        "Research package ID",
        "Title",
        "Purpose",
        "Package type",
        "Status",
        "Linked evidence",
        "Linked benchmarks",
        "Linked datasets",
        "Linked specifications",
        "Linked claims",
        "Reproducibility status",
        "Validation status",
        "Limitations",
    ):
        assert heading in registry
    assert "`permea_core_public_artifact_package_v0`" in registry
    assert "No active public-review research package is claimed" in registry


def test_assembly_guide_coverage() -> None:
    assembly = (ROOT / "docs/research/research-package-assembly.md").read_text(
        encoding="utf-8"
    )

    for phrase in (
        "evidence assets",
        "benchmark cards",
        "dataset cards",
        "specification records",
        "validation outputs",
        "claim registry entries",
        "reproducibility outputs",
        "README -> QUICKSTART -> EVIDENCE -> BENCHMARKS -> DATASETS -> RESEARCH PACKAGE -> CLAIMS -> VALIDATION",
    ):
        assert phrase in assembly


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
