from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.sources.registry import (
    validate_source_entry,
    validate_source_registry_file,
)


def test_current_source_registry_passes() -> None:
    result = validate_source_registry_file(ROOT / "sources" / "registry.yaml")

    assert result.passed
    assert result.entries_checked == 7


def test_individual_source_files_pass() -> None:
    source_paths = sorted((ROOT / "sources").glob("*.yaml"))
    source_paths = [path for path in source_paths if path.name != "registry.yaml"]

    assert len(source_paths) == 7
    for source_path in source_paths:
        result = validate_source_registry_file(source_path)
        assert result.passed, source_path
        assert result.entries_checked == 1


def test_missing_required_field_fails(tmp_path: Path) -> None:
    payload = yaml.safe_load((ROOT / "sources" / "registry.yaml").read_text())
    del payload["sources"][0]["claim_boundary"]
    registry_path = tmp_path / "missing_required.yaml"
    registry_path.write_text(yaml.safe_dump(payload), encoding="utf-8")

    result = validate_source_registry_file(registry_path)

    assert not result.passed
    assert any(error.field == "claim_boundary" for error in result.errors)


def test_invalid_priority_fails() -> None:
    entry = _valid_entry()
    entry["priority"] = "urgent"

    errors = validate_source_entry(entry)

    assert any(error.field == "priority" for error in errors)


def test_invalid_current_status_fails() -> None:
    entry = _valid_entry()
    entry["current_status"] = "downloaded"

    errors = validate_source_entry(entry)

    assert any(error.field == "current_status" for error in errors)


def test_invalid_acquisition_mode_fails() -> None:
    entry = _valid_entry()
    entry["acquisition_mode"] = "scrape-now"

    errors = validate_source_entry(entry)

    assert any(error.field == "acquisition_mode" for error in errors)


def test_cli_validates_default_registry_and_source_files() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_source_registry.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS source registry validation" in completed.stdout
    assert "8 file(s), 14 source entries" in completed.stdout


def _valid_entry() -> dict[str, object]:
    payload = yaml.safe_load((ROOT / "sources" / "registry.yaml").read_text())
    return dict(payload["sources"][0])
