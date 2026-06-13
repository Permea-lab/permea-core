from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.runs.manifests import (
    REQUIRED_NON_CLAIMS,
    generate_run_manifest_file,
    render_run_manifest,
    validate_run_manifest,
    validate_run_manifest_file,
)


def test_current_run_manifests_pass() -> None:
    manifest_paths = sorted((ROOT / "run_manifests").glob("*.yaml"))

    assert len(manifest_paths) == 1
    for manifest_path in manifest_paths:
        result = validate_run_manifest_file(manifest_path)
        assert result.passed, result.errors


def test_missing_required_field_fails(tmp_path: Path) -> None:
    payload = _valid_manifest()
    del payload["claim_boundary"]
    manifest_path = tmp_path / "missing_required.yaml"
    manifest_path.write_text(yaml.safe_dump(payload), encoding="utf-8")

    result = validate_run_manifest_file(manifest_path)

    assert not result.passed
    assert any("claim_boundary" in error for error in result.errors)


def test_invalid_run_type_fails() -> None:
    manifest = _valid_manifest()
    manifest["run_type"] = "real-model-run"

    errors = validate_run_manifest(manifest)

    assert any("run_type" in error for error in errors)


def test_invalid_artifact_status_fails() -> None:
    manifest = _valid_manifest()
    manifest["artifact_status"] = "production-result"

    errors = validate_run_manifest(manifest)

    assert any("artifact_status" in error for error in errors)


def test_rendered_markdown_includes_required_sections() -> None:
    text = render_run_manifest(_valid_manifest())

    for section in (
        "## Run ID",
        "## Run Type",
        "## Artifact Status",
        "## Generated Artifacts",
        "## Validation Steps",
        "## Explicit Non-Claims",
        "## Claim Boundary",
    ):
        assert section in text


def test_rendered_markdown_includes_explicit_non_claims() -> None:
    text = render_run_manifest(_valid_manifest())

    for non_claim in REQUIRED_NON_CLAIMS:
        assert non_claim in text


def test_generate_run_manifest_file_writes_markdown(tmp_path: Path) -> None:
    output_path = tmp_path / "example_artifact_generation.md"

    result = generate_run_manifest_file(
        ROOT / "run_manifests" / "example_artifact_generation.yaml",
        output_path,
    )

    assert result.passed
    assert "# Run Manifest:" in output_path.read_text(encoding="utf-8")


def test_cli_validates_and_generates_run_manifests() -> None:
    validate = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_run_manifests.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    generate = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_run_manifests.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert validate.returncode == 0
    assert "PASS run manifest validation: Validated 1 run manifest(s)." in validate.stdout
    assert generate.returncode == 0
    assert "PASS run manifest generation: Generated 1 run manifest(s)." in generate.stdout


def _valid_manifest() -> dict[str, object]:
    return yaml.safe_load(
        (ROOT / "run_manifests" / "example_artifact_generation.yaml").read_text()
    )
