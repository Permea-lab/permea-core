from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.benchmarks.registry import validate_registry_file


def test_current_registry_passes() -> None:
    result = validate_registry_file(ROOT / "benchmarks" / "registry.yaml")

    assert result.passed
    assert result.entries_checked == 2


def test_missing_required_field_fails(tmp_path: Path) -> None:
    payload = yaml.safe_load((ROOT / "benchmarks" / "registry.yaml").read_text())
    del payload["benchmarks"][0]["claim_boundary"]
    registry_path = tmp_path / "missing_required.yaml"
    registry_path.write_text(yaml.safe_dump(payload), encoding="utf-8")

    result = validate_registry_file(registry_path)

    assert not result.passed
    assert any(error.field == "claim_boundary" for error in result.errors)


def test_invalid_maturity_level_fails(tmp_path: Path) -> None:
    payload = yaml.safe_load((ROOT / "benchmarks" / "registry.yaml").read_text())
    payload["benchmarks"][0]["maturity_level"] = "registry-candidate"
    registry_path = tmp_path / "invalid_maturity.yaml"
    registry_path.write_text(yaml.safe_dump(payload), encoding="utf-8")

    result = validate_registry_file(registry_path)

    assert not result.passed
    assert any(error.field == "maturity_level" for error in result.errors)
