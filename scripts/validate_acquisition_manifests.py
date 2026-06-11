#!/usr/bin/env python3
"""Validate Permea acquisition manifest YAML files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.acquisition.manifests import (  # noqa: E402
    DEFAULT_ACQUISITION_MANIFEST_DIR,
    validate_acquisition_manifest_file,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Permea acquisition manifests."
    )
    parser.add_argument(
        "manifest_dir",
        nargs="?",
        default=str(DEFAULT_ACQUISITION_MANIFEST_DIR),
        help="Directory containing acquisition manifest YAML files.",
    )
    args = parser.parse_args()

    manifest_dir = _resolve_path(args.manifest_dir)
    results = [
        validate_acquisition_manifest_file(path)
        for path in sorted(manifest_dir.glob("*.yaml"))
    ]

    failed = [result for result in results if not result.passed]
    if not failed and results:
        print(f"PASS acquisition manifest validation: {len(results)} manifest(s)")
        return 0

    if not results:
        print(
            "FAIL acquisition manifest validation: "
            f"no YAML files found in {manifest_dir}"
        )
        return 1

    print("FAIL acquisition manifest validation")
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
