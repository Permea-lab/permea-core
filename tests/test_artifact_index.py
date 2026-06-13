from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.index.artifact_index import (
    ARTIFACT_FAMILIES,
    NON_CLAIMS,
    collect_artifact_paths,
    generate_artifact_index,
    render_artifact_index,
)


REQUIRED_SECTIONS = (
    "## Overview",
    "## Unified Commands",
    "## Registry Inputs",
    "## Generated Benchmark Cards",
    "## Generated Dataset Cards",
    "## Generated Acquisition Manifests",
    "## Generated Evidence Cards",
    "## Generated Output Packages",
    "## Generated Run Manifests",
    "## Validation Boundary",
    "## Explicit Non-Claims",
    "## Next Steps",
)


def test_generator_writes_artifact_index(tmp_path: Path) -> None:
    output_path = tmp_path / "ARTIFACT_INDEX.md"

    result = generate_artifact_index(output_path, ROOT)

    assert result["passed"] is True
    assert output_path.exists()
    assert "# Permea Core Public Artifact Index" in output_path.read_text(
        encoding="utf-8"
    )


def test_generated_index_includes_required_sections() -> None:
    rendered = render_artifact_index(collect_artifact_paths(ROOT))

    for section in REQUIRED_SECTIONS:
        assert section in rendered


def test_generated_index_includes_expected_artifact_families() -> None:
    index = collect_artifact_paths(ROOT)

    assert set(index["artifact_families"]) == {
        key for _title, key, _directory in ARTIFACT_FAMILIES
    }
    assert "docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md" in index[
        "artifact_families"
    ]["benchmark_cards"]["paths"]
    assert (
        "docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml"
        in index["artifact_families"]["output_packages"]["paths"]
    )


def test_generated_index_includes_explicit_non_claims() -> None:
    rendered = render_artifact_index(collect_artifact_paths(ROOT))

    for claim in NON_CLAIMS:
        assert f"- {claim}" in rendered


def test_generated_index_uses_relative_paths_only() -> None:
    index = collect_artifact_paths(ROOT)
    rendered = render_artifact_index(index)

    assert str(ROOT) not in rendered
    for item in index["registry_inputs"]:
        assert not item["path"].startswith("/")
    for family in index["artifact_families"].values():
        assert not family["root"].startswith("/")
        assert all(not path.startswith("/") for path in family["paths"])


def test_generated_index_avoids_unsupported_public_claim_phrasing() -> None:
    rendered = render_artifact_index(collect_artifact_paths(ROOT)).lower()
    blocked_parts = (
        ("alpha", "fold"),
        ("state", "of", "the", "art"),
        ("clinical", "efficacy"),
        ("solved", "delivery"),
    )

    for parts in blocked_parts:
        assert " ".join(parts) not in rendered


def test_cli_exits_zero_and_writes_default_index() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_artifact_index.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS artifact index generation" in completed.stdout
    assert (ROOT / "docs" / "examples" / "generated" / "ARTIFACT_INDEX.md").exists()
