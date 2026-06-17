from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTEGRATION_DOCS = (
    "docs/integrations/README.md",
    "docs/integrations/permea-signal-ml.md",
    "docs/integrations/external-evidence-package-template.md",
    "docs/integrations/external-evidence-package-governance.md",
)
TOUCHED_PUBLIC_FILES = (
    *INTEGRATION_DOCS,
    "schemas/external-evidence-package.schema.json",
    "scripts/permea_signal.py",
    "tests/test_signal_integration_layer.py",
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/p-core-049-signal-integration-layer-v0.md",
)
REQUIRED_SCHEMA_FIELDS = (
    "evidence_package_id",
    "package_name",
    "repository",
    "purpose",
    "evidence_type",
    "linked_datasets",
    "linked_benchmarks",
    "linked_research_packages",
    "linked_claims",
    "reproducibility_path",
    "validation_path",
    "claim_boundaries",
    "limitations",
    "status",
    "version",
)
ALLOWED_STATUSES = (
    "proposed",
    "documented",
    "reproducible_computational",
    "public_review_ready",
    "externally_validated",
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


def test_signal_integration_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_signal.py")]
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
    assert "Permea Core signal integration" in first
    assert "Signal Integration Layer Ready" in first
    assert "Registered external evidence packages: 1" in first
    assert "permea-signal-ml" in first
    assert "Evidence Navigation Layer" in first
    assert "Benchmark Execution Layer" in first
    assert "Status: PASS" in first


def test_integration_docs_exist_and_link_each_other() -> None:
    for path in INTEGRATION_DOCS:
        assert (ROOT / path).exists()

    readme = (ROOT / "docs/integrations/README.md").read_text(encoding="utf-8")
    for target in (
        "permea-signal-ml.md",
        "external-evidence-package-template.md",
        "external-evidence-package-governance.md",
    ):
        assert target in readme


def test_external_evidence_schema_validity_required_fields_and_statuses() -> None:
    schema = json.loads(
        (ROOT / "schemas/external-evidence-package.schema.json").read_text(
            encoding="utf-8"
        )
    )

    assert schema["title"] == "Permea External Evidence Package"
    assert schema["type"] == "object"
    assert tuple(schema["properties"]["status"]["enum"]) == ALLOWED_STATUSES
    for field in REQUIRED_SCHEMA_FIELDS:
        assert field in schema["required"]
        assert field in schema["properties"]


def test_external_evidence_package_template_structure() -> None:
    template = (
        ROOT / "docs/integrations/external-evidence-package-template.md"
    ).read_text(encoding="utf-8")

    for heading in (
        "Evidence Package ID",
        "Package Name",
        "Repository",
        "Purpose",
        "Evidence Type",
        "Linked Datasets",
        "Linked Benchmarks",
        "Linked Research Packages",
        "Linked Claims",
        "Reproducibility Path",
        "Validation Path",
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

    assert "SIGNAL INTEGRATION" in readme
    assert "scripts/permea_signal.py" in readme
    assert "Signal Integration Layer: Implemented" in open_first
    assert "Signal Integration Layer" in review_hub
    assert "scripts/permea_signal.py" in review_hub


def test_signal_integration_doc_covers_required_topics() -> None:
    doc = (ROOT / "docs/integrations/permea-signal-ml.md").read_text(
        encoding="utf-8"
    )

    for phrase in (
        "Purpose Of `permea-signal-ml`",
        "Relationship To `permea-core`",
        "Linked Evidence Categories",
        "Linked Dataset Registry Concepts",
        "Linked Benchmark Registry Concepts",
        "Linked Research Package Concepts",
        "Linked Public Review Packet Concepts",
        "What Belongs In `permea-core`",
        "What Belongs In `permea-signal-ml`",
        "Claim Boundaries",
        "Limitations",
        "Future Validation Path",
    ):
        assert phrase in doc


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
