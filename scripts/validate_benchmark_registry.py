#!/usr/bin/env python3
"""Validate Permea benchmark registry YAML files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.benchmarks.registry import validate_registry_file


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a Permea benchmark registry YAML file."
    )
    parser.add_argument(
        "registry_path",
        nargs="?",
        default="benchmarks/registry.yaml",
        help="Path to a registry YAML file. Defaults to benchmarks/registry.yaml.",
    )
    args = parser.parse_args()

    result = validate_registry_file(ROOT / args.registry_path)
    if result.passed:
        print(
            "PASS benchmark registry validation: "
            f"{result.path} ({result.entries_checked} entries)"
        )
        return 0

    print(f"FAIL benchmark registry validation: {result.path}")
    for error in result.errors:
        print(f"- {error.entry}: {error.field}: {error.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
