from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DOCS = (
    "docs/benchmarks/README.md",
    "docs/benchmarks/benchmark-registry.md",
    "docs/benchmarks/benchmark-lifecycle.md",
    "docs/benchmarks/benchmark-card-template.md",
    "docs/benchmarks/benchmark-governance.md",
)
TOUCHED_PUBLIC_FILES = (
    *BENCHMARK_DOCS,
    "schemas/benchmark-card.schema.json",
    "schemas/benchmark_card.schema.json",
    "scripts/permea_benchmarks.py",
    "tests/test_benchmark_registry_layer.py",
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/p-core-044-benchmark-registry-layer-v0.md",
)
SCHEMA_PATHS = (
    "schemas/benchmark-card.schema.json",
    "schemas/benchmark_card.schema.json",
)
REQUIRED_STATUSES = (
    "Proposed",
    "Draft",
    "Reproducible Computational Workflow",
    "Active Reference Benchmark",
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
    "level",
)


def test_benchmark_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_benchmarks.py")]
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
    assert "Permea Core benchmark registry" in first
    assert "Benchmark Framework Ready" in first
    assert "Registered benchmarks: 2" in first
    assert "Active benchmarks: 0" in first
    assert "Proposed benchmarks: 1" in first
    assert "Draft benchmarks: 1" in first
    assert "Status: PASS" in first


def test_benchmark_docs_exist_and_link_each_other() -> None:
    for path in BENCHMARK_DOCS:
        assert (ROOT / path).exists()

    readme = (ROOT / "docs/benchmarks/README.md").read_text(encoding="utf-8")
    for target in (
        "benchmark-registry.md",
        "benchmark-lifecycle.md",
        "benchmark-card-template.md",
        "benchmark-governance.md",
    ):
        assert target in readme


def test_schema_validity_and_required_fields() -> None:
    schemas = [
        json.loads((ROOT / path).read_text(encoding="utf-8")) for path in SCHEMA_PATHS
    ]

    assert schemas[0] == schemas[1]
    for schema in schemas:
        assert schema["type"] == "object"
        assert schema["title"] == "Permea Benchmark Card"
        for field in (
            "benchmark_id",
            "name",
            "purpose",
            "measured_property",
            "status",
            "evidence_links",
            "claim_boundaries",
            "limitations",
            "version",
        ):
            assert field in schema["required"]
            assert field in schema["properties"]


def test_lifecycle_statuses_match_schema_statuses() -> None:
    lifecycle = (ROOT / "docs/benchmarks/benchmark-lifecycle.md").read_text(
        encoding="utf-8"
    )
    schema = json.loads((ROOT / "schemas/benchmark_card.schema.json").read_text())
    schema_statuses = tuple(schema["properties"]["status"]["enum"])

    assert schema_statuses == REQUIRED_STATUSES
    for status in REQUIRED_STATUSES:
        assert status in lifecycle


def test_registry_structure_contains_required_columns_and_entries() -> None:
    registry = (ROOT / "docs/benchmarks/benchmark-registry.md").read_text(
        encoding="utf-8"
    )

    for heading in (
        "Benchmark ID",
        "Benchmark name",
        "Measured property",
        "Status",
        "Linked evidence",
        "Linked claims",
        "Linked specifications",
        "Validation status",
        "Limitations",
    ):
        assert heading in registry
    assert "`bbb_b3pred_dataset3`" in registry
    assert "`cpp_cppsite2_placeholder`" in registry
    assert "No active reference benchmark is claimed" in registry


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
