from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXECUTION_DOCS = (
    "docs/benchmarks/benchmark-execution-model.md",
    "docs/benchmarks/benchmark-run-template.md",
)
TOUCHED_PUBLIC_FILES = (
    *EXECUTION_DOCS,
    "docs/benchmarks/README.md",
    "docs/benchmarks/benchmark-registry.md",
    "docs/benchmarks/benchmark-lifecycle.md",
    "docs/benchmarks/benchmark-governance.md",
    "schemas/benchmark-run.schema.json",
    "scripts/permea_benchmark_run.py",
    "tests/test_benchmark_execution_layer.py",
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/p-core-048-benchmark-execution-layer-v0.md",
)
REQUIRED_SCHEMA_FIELDS = (
    "benchmark_run_id",
    "benchmark_id",
    "name",
    "purpose",
    "status",
    "dataset_links",
    "benchmark_card_link",
    "evaluation_protocol",
    "metrics",
    "reproducibility_path",
    "validation_outputs",
    "evidence_links",
    "claim_boundaries",
    "limitations",
    "version",
)
ALLOWED_STATUSES = (
    "planned",
    "draft",
    "executed",
    "validated",
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
    "do not ",
)


def test_benchmark_execution_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_benchmark_run.py")]
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
    assert "Permea Core benchmark execution" in first
    assert "Benchmark Execution Framework Ready" in first
    assert "Registered benchmarks: 2" in first
    assert "Executable benchmarks: 0" in first
    assert "Registered benchmark runs: 0" in first
    assert "No benchmark results are currently registered." in first
    assert "No biological conclusions should be drawn from framework readiness alone." in first
    assert "Status: PASS" in first


def test_benchmark_execution_docs_exist_and_are_linked() -> None:
    for path in EXECUTION_DOCS:
        assert (ROOT / path).exists()

    readme = (ROOT / "docs/benchmarks/README.md").read_text(encoding="utf-8")
    assert "benchmark-execution-model.md" in readme
    assert "benchmark-run-template.md" in readme


def test_benchmark_run_schema_validity_required_fields_and_statuses() -> None:
    schema = json.loads(
        (ROOT / "schemas/benchmark-run.schema.json").read_text(encoding="utf-8")
    )

    assert schema["title"] == "Permea Benchmark Run"
    assert schema["type"] == "object"
    assert tuple(schema["properties"]["status"]["enum"]) == ALLOWED_STATUSES
    for field in REQUIRED_SCHEMA_FIELDS:
        assert field in schema["required"]
        assert field in schema["properties"]


def test_benchmark_run_template_structure() -> None:
    template = (ROOT / "docs/benchmarks/benchmark-run-template.md").read_text(
        encoding="utf-8"
    )

    for heading in (
        "Benchmark Run ID",
        "Benchmark ID",
        "Benchmark Name",
        "Run Purpose",
        "Dataset Links",
        "Benchmark Card Link",
        "Evaluation Protocol",
        "Metrics",
        "Execution Environment Summary",
        "Reproducibility Path",
        "Validation Outputs",
        "Evidence Links",
        "Claim Boundaries",
        "Limitations",
        "Status",
        "Version",
        "Maintainer Notes",
    ):
        assert f"## {heading}" in template
    for status in ALLOWED_STATUSES:
        assert f"- {status}" in template


def test_readme_and_review_hub_path_coverage() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    open_first = (ROOT / "OPEN_THIS_FIRST.md").read_text(encoding="utf-8")
    review_hub = (ROOT / "REVIEW_HUB.md").read_text(encoding="utf-8")

    assert "BENCHMARK EXECUTION" in readme
    assert "scripts/permea_benchmark_run.py" in readme
    assert "Benchmark Execution Layer: Implemented" in open_first
    assert "Benchmark Execution Layer" in review_hub
    assert "scripts/permea_benchmark_run.py" in review_hub


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


def test_benchmark_execution_model_covers_required_topics() -> None:
    model = (ROOT / "docs/benchmarks/benchmark-execution-model.md").read_text(
        encoding="utf-8"
    )

    for phrase in (
        "purpose",
        "Registry Versus Run",
        "Required Execution Metadata",
        "Required Dataset Links",
        "Required Benchmark Card Links",
        "Required Evidence Links",
        "Required Validation Outputs",
        "Reproducibility Requirements",
        "Claim Boundaries",
        "Limitations",
        "No-Result State",
        "Framework readiness does not imply biological benchmark results",
    ):
        assert phrase in model


def _combined_touched_text() -> str:
    return "\n".join(
        (ROOT / path).read_text(encoding="utf-8") for path in TOUCHED_PUBLIC_FILES
    )
