from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.specs.registry import (  # noqa: E402
    NON_CLAIMS,
    PASS,
    SPEC_ROWS,
    collect_spec_registry,
    render_spec_registry,
)


REQUIRED_SPEC_SECTIONS = (
    "## Overview",
    "## Purpose",
    "## Required fields",
    "## Recommended fields",
    "## Field definitions",
    "## Example structure",
    "## Validation expectations",
    "## Claim boundaries",
    "## Limitations",
    "## Extension points",
)

REQUIRED_SCHEMA_KEYS = (
    "$id",
    "title",
    "type",
    "required",
    "properties",
    "additionalProperties",
)

DOC_LINK_TARGETS = (
    "docs/specs/README.md",
    "docs/specs/SPEC_DATASET_CARD.md",
    "docs/specs/SPEC_BENCHMARK_CARD.md",
    "docs/specs/SPEC_EVIDENCE_CARD.md",
    "docs/specs/SPEC_RUN_MANIFEST.md",
    "docs/specs/SPEC_OUTPUT_PACKAGE.md",
)


def test_spec_registry_collects_all_specs() -> None:
    registry = collect_spec_registry(ROOT)

    assert registry["status"] == PASS
    assert len(registry["specifications"]) == 5
    assert all(item["spec_exists"] for item in registry["specifications"])
    assert all(item["schema_exists"] for item in registry["specifications"])


def test_spec_registry_render_lists_paths_and_non_claims() -> None:
    rendered = render_spec_registry(collect_spec_registry(ROOT))

    for row in SPEC_ROWS:
        assert row["spec_path"] in rendered
        assert row["schema_path"] in rendered
        assert row["family"] in rendered
    for claim in NON_CLAIMS:
        assert claim in rendered


def test_spec_markdown_files_include_required_sections() -> None:
    for row in SPEC_ROWS:
        text = (ROOT / row["spec_path"]).read_text(encoding="utf-8")
        for section in REQUIRED_SPEC_SECTIONS:
            assert section in text


def test_schema_files_include_required_structure() -> None:
    for row in SPEC_ROWS:
        payload = json.loads((ROOT / row["schema_path"]).read_text(encoding="utf-8"))
        for key in REQUIRED_SCHEMA_KEYS:
            assert key in payload
        assert payload["type"] == "object"
        assert isinstance(payload["required"], list)
        assert isinstance(payload["properties"], dict)
        assert "claim_boundary" in payload["required"]
        assert "claim_boundary" in payload["properties"]


def test_specs_cli_exits_zero_and_prints_registry() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "permea_specs.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS Permea artifact specification registry" in completed.stdout
    assert "docs/specs/README.md" in completed.stdout


def test_required_non_claims_are_public() -> None:
    combined = "\n".join(
        (ROOT / row["spec_path"]).read_text(encoding="utf-8") for row in SPEC_ROWS
    )
    combined += "\n" + (ROOT / "docs/specs/README.md").read_text(encoding="utf-8")
    combined += "\n" + (ROOT / "docs/reports/p-core-036-artifact-specification-layer.md").read_text(encoding="utf-8")

    for claim in NON_CLAIMS:
        assert claim in combined


def test_documentation_links_to_spec_layer() -> None:
    files = [
        ROOT / "README.md",
        ROOT / "QUICKSTART.md",
        ROOT / "EVALUATION.md",
        ROOT / "REPRODUCIBILITY.md",
    ]
    combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

    assert "docs/specs/README.md" in combined
    for target in DOC_LINK_TARGETS:
        assert (ROOT / target).exists()


def test_generated_surface_links_to_specs_after_generation() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_evidence_surface.py")],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    generated = (ROOT / "docs/examples/generated/README.md").read_text(encoding="utf-8")

    assert "../../../docs/specs/README.md" in generated

