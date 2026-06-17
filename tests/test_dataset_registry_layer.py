from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET_DOCS = (
    "docs/datasets/README.md",
    "docs/datasets/dataset-registry.md",
    "docs/datasets/dataset-lifecycle.md",
    "docs/datasets/dataset-card-template.md",
    "docs/datasets/dataset-governance.md",
    "docs/datasets/dataset-provenance.md",
)
TOUCHED_PUBLIC_FILES = (
    *DATASET_DOCS,
    "schemas/dataset-card.schema.json",
    "schemas/dataset_card.schema.json",
    "scripts/permea_datasets.py",
    "tests/test_dataset_registry_layer.py",
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/p-core-045-dataset-registry-layer-v0.md",
)
SCHEMA_PATHS = (
    "schemas/dataset-card.schema.json",
    "schemas/dataset_card.schema.json",
)
REQUIRED_STATUSES = (
    "Proposed",
    "Draft Card",
    "Documented External Dataset",
    "Reproducible Derived Dataset",
    "Active Reference Dataset",
    "Independently Reproduced",
    "Externally Validated",
    "Deprecated",
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
)


def test_dataset_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_datasets.py")]
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
    assert "Permea Core dataset registry" in first
    assert "Dataset Framework Ready" in first
    assert "Registered datasets: 2" in first
    assert "Active reference datasets: 0" in first
    assert "Proposed datasets: 1" in first
    assert "Draft datasets: 1" in first
    assert "Documented datasets: 0" in first
    assert "Validated datasets: 0" in first
    assert "Status: PASS" in first


def test_dataset_docs_exist_and_link_each_other() -> None:
    for path in DATASET_DOCS:
        assert (ROOT / path).exists()

    readme = (ROOT / "docs/datasets/README.md").read_text(encoding="utf-8")
    for target in (
        "dataset-registry.md",
        "dataset-lifecycle.md",
        "dataset-card-template.md",
        "dataset-provenance.md",
        "dataset-governance.md",
    ):
        assert target in readme


def test_schema_validity_and_required_fields() -> None:
    schemas = [
        json.loads((ROOT / path).read_text(encoding="utf-8")) for path in SCHEMA_PATHS
    ]

    assert schemas[0] == schemas[1]
    for schema in schemas:
        assert schema["type"] == "object"
        assert schema["title"] == "Permea Dataset Card"
        for field in (
            "dataset_id",
            "name",
            "purpose",
            "source_type",
            "intended_use",
            "status",
            "provenance_record",
            "linked_benchmarks",
            "linked_evidence",
            "claim_boundaries",
            "limitations",
            "version",
        ):
            assert field in schema["required"]
            assert field in schema["properties"]


def test_lifecycle_statuses_match_schema_statuses() -> None:
    lifecycle = (ROOT / "docs/datasets/dataset-lifecycle.md").read_text(
        encoding="utf-8"
    )
    schema = json.loads((ROOT / "schemas/dataset_card.schema.json").read_text())
    schema_statuses = tuple(schema["properties"]["status"]["enum"])

    assert schema_statuses == REQUIRED_STATUSES
    for status in REQUIRED_STATUSES:
        assert status in lifecycle


def test_registry_structure_contains_required_columns_and_entries() -> None:
    registry = (ROOT / "docs/datasets/dataset-registry.md").read_text(
        encoding="utf-8"
    )

    for heading in (
        "Dataset ID",
        "Dataset name",
        "Source type",
        "Intended use",
        "Status",
        "Linked evidence",
        "Linked benchmarks",
        "Linked claims",
        "Linked specifications",
        "Provenance status",
        "Validation status",
        "Limitations",
    ):
        assert heading in registry
    assert "`b3pred_dataset3`" in registry
    assert "`cppsite2_placeholder`" in registry
    assert "No active reference dataset is claimed" in registry


def test_provenance_section_coverage() -> None:
    provenance = (ROOT / "docs/datasets/dataset-provenance.md").read_text(
        encoding="utf-8"
    )

    for phrase in (
        "Source reference",
        "Acquisition method",
        "Processing steps",
        "Transformation summary",
        "Generated artifacts",
        "Checksums where applicable",
        "License / usage constraints",
        "Reproducibility path",
        "Known limitations",
    ):
        assert phrase in provenance


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
