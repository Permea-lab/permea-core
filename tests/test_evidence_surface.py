from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.generation import artifacts as generation_artifacts
from permea_core.surface.evidence_surface import (
    EXPLICIT_NON_CLAIMS,
    PASS,
    collect_evidence_surface,
    render_evidence_surface,
    write_evidence_surface,
)
from permea_core.validation import artifacts as validation_artifacts


REQUIRED_MARKDOWN_SECTIONS = (
    "## Overview",
    "## One-command demo",
    "## Core generated surfaces",
    "## Artifact families",
    "## Reproducibility commands",
    "## Validation commands",
    "## Explicit Non-Claims",
    "## Limitations",
    "## Next Evidence Steps",
)

REQUIRED_LINKS = (
    "DEMO_PACKET.md",
    "ARTIFACT_INDEX.md",
    "EVIDENCE_MATRIX.md",
    "dry_runs/example_benchmark_dry_run.md",
    "benchmark_cards/",
    "dataset_cards/",
    "acquisition_manifests/",
    "evidence_cards/",
    "output_packages/",
    "run_manifests/",
)

UNSUPPORTED_CLAIM_PHRASE_PARTS = (
    ("wet-lab", "validated"),
    ("clinical", "efficacy exists"),
    ("universal", "predictor"),
    ("solved", "delivery"),
    ("bioRxiv", "ready"),
    ("data has been", "downloaded"),
    ("redistribution rights have been", "confirmed"),
    ("acquisition has been", "executed"),
    ("model performance has been", "measured"),
)


def test_evidence_surface_generation_returns_pass() -> None:
    surface = collect_evidence_surface(ROOT)

    assert surface["status"] == PASS
    assert surface["surface_id"] == "permea_core_public_evidence_surface"


def test_generated_readme_includes_required_sections() -> None:
    rendered = render_evidence_surface(collect_evidence_surface(ROOT))

    for section in REQUIRED_MARKDOWN_SECTIONS:
        assert section in rendered


def test_generated_readme_includes_required_links() -> None:
    rendered = render_evidence_surface(collect_evidence_surface(ROOT))

    for link in REQUIRED_LINKS:
        assert f"]({link})" in rendered


def test_generated_readme_includes_explicit_non_claims() -> None:
    rendered = render_evidence_surface(collect_evidence_surface(ROOT))

    for claim in EXPLICIT_NON_CLAIMS:
        assert f"- {claim}" in rendered


def test_generated_readme_uses_relative_public_safe_paths(tmp_path: Path) -> None:
    output = tmp_path / "README.md"
    result = write_evidence_surface(output, ROOT)
    rendered = output.read_text(encoding="utf-8")

    assert str(ROOT) not in rendered
    assert not result["output_path"].startswith("/")
    for key in ("primary_entry_points", "artifact_families"):
        for item in result[key]:
            assert not item["path"].startswith("/")


def test_unified_generation_includes_evidence_surface_generation() -> None:
    names = [name for name, _command in generation_artifacts.GENERATION_STEPS]

    assert "evidence surface generation" in names


def test_unified_validation_includes_evidence_surface_presence() -> None:
    names = [name for name, _command in validation_artifacts.VALIDATION_STEPS]

    assert "evidence surface generation" in names


def test_cli_exits_zero_and_writes_readme() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_evidence_surface.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS evidence surface generation" in completed.stdout
    assert (ROOT / "docs" / "examples" / "generated" / "README.md").exists()


def test_unsupported_claim_phrases_are_absent() -> None:
    rendered = render_evidence_surface(collect_evidence_surface(ROOT))

    for parts in UNSUPPORTED_CLAIM_PHRASE_PARTS:
        phrase = " ".join(parts)
        assert phrase not in rendered
