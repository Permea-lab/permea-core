from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.acquisition.manifests import (
    generate_acquisition_manifest_file,
    render_acquisition_manifest,
    validate_acquisition_manifest,
    validate_acquisition_manifest_file,
)


def test_current_acquisition_manifests_pass() -> None:
    manifest_paths = sorted((ROOT / "acquisition_manifests").glob("*.yaml"))

    assert len(manifest_paths) == 2
    for manifest_path in manifest_paths:
        result = validate_acquisition_manifest_file(manifest_path)
        assert result.passed, manifest_path


def test_missing_required_field_fails(tmp_path: Path) -> None:
    payload = _valid_manifest()
    del payload["claim_boundary"]
    manifest_path = tmp_path / "missing_required.yaml"
    manifest_path.write_text(yaml.safe_dump(payload), encoding="utf-8")

    result = validate_acquisition_manifest_file(manifest_path)

    assert not result.passed
    assert any(error.field == "claim_boundary" for error in result.errors)


def test_invalid_acquisition_mode_fails() -> None:
    manifest = _valid_manifest()
    manifest["acquisition_mode"] = "scrape-now"

    errors = validate_acquisition_manifest(manifest)

    assert any(error.field == "acquisition_mode" for error in errors)


def test_invalid_acquisition_status_fails() -> None:
    manifest = _valid_manifest()
    manifest["acquisition_status"] = "executed"

    errors = validate_acquisition_manifest(manifest)

    assert any(error.field == "acquisition_status" for error in errors)


def test_invalid_redistribution_status_fails() -> None:
    manifest = _valid_manifest()
    manifest["redistribution_status"] = "confirmed"

    errors = validate_acquisition_manifest(manifest)

    assert any(error.field == "redistribution_status" for error in errors)


def test_rendered_markdown_includes_required_sections() -> None:
    text = render_acquisition_manifest(_valid_manifest())

    for section in (
        "## Manifest ID",
        "## Dataset ID",
        "## Source IDs",
        "## Acquisition Mode",
        "## Acquisition Status",
        "## Redistribution Status",
        "## Explicit Non-Claims",
        "## Fallback Strategy",
    ):
        assert section in text


def test_rendered_markdown_includes_explicit_non_claims() -> None:
    text = render_acquisition_manifest(_valid_manifest())

    assert "no dataset downloaded" in text
    assert "no acquisition executed" in text
    assert "no redistribution rights confirmed" in text
    assert "no wet-lab validation by Permea" in text


def test_generate_acquisition_manifest_file_writes_markdown(tmp_path: Path) -> None:
    output_path = tmp_path / "b3pred_dataset3.md"

    result = generate_acquisition_manifest_file(
        ROOT / "acquisition_manifests" / "b3pred_dataset3.yaml",
        output_path,
    )

    assert result.passed
    assert "# Acquisition Manifest:" in output_path.read_text(encoding="utf-8")


def test_cli_validates_and_generates_acquisition_manifests() -> None:
    validate = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_acquisition_manifests.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    generate = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_acquisition_manifests.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert validate.returncode == 0
    assert "PASS acquisition manifest validation: 2 manifest(s)" in validate.stdout
    assert generate.returncode == 0
    assert (
        "PASS acquisition manifest generation: Generated 2 acquisition manifest(s)."
        in generate.stdout
    )


def _valid_manifest() -> dict[str, object]:
    return yaml.safe_load(
        (ROOT / "acquisition_manifests" / "b3pred_dataset3.yaml").read_text()
    )
