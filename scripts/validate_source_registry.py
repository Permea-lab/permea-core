#!/usr/bin/env python3
"""Validate Permea source registry YAML files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.sources.registry import validate_source_registry_file


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Permea source registry YAML files."
    )
    parser.add_argument(
        "registry_path",
        nargs="?",
        default="sources/registry.yaml",
        help="Path to a registry YAML file. Defaults to sources/registry.yaml.",
    )
    args = parser.parse_args()

    registry_path = _resolve_path(args.registry_path)
    results = [validate_source_registry_file(registry_path)]

    source_dir = registry_path.parent
    if source_dir.exists():
        for source_path in sorted(source_dir.glob("*.yaml")):
            if source_path.resolve() == registry_path.resolve():
                continue
            results.append(validate_source_registry_file(source_path))

    failed = [result for result in results if not result.passed]
    if not failed:
        entries = sum(result.entries_checked for result in results)
        print(
            "PASS source registry validation: "
            f"{len(results)} file(s), {entries} source entr"
            f"{'y' if entries == 1 else 'ies'}"
        )
        return 0

    print("FAIL source registry validation")
    for result in failed:
        print(f"{result.path}:")
        for error in result.errors:
            print(f"- {error.entry}: {error.field}: {error.message}")
    return 1


def _resolve_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


if __name__ == "__main__":
    raise SystemExit(main())
