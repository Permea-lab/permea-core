#!/usr/bin/env python3
"""Generate public-safe Permea acquisition manifests from YAML metadata."""

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
    DEFAULT_GENERATED_ACQUISITION_MANIFEST_DIR,
    generate_acquisition_manifests,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Permea acquisition manifest Markdown examples."
    )
    parser.add_argument(
        "manifest_dir",
        nargs="?",
        default=str(DEFAULT_ACQUISITION_MANIFEST_DIR),
        help="Directory containing acquisition manifest YAML files.",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default=str(DEFAULT_GENERATED_ACQUISITION_MANIFEST_DIR),
        help="Output directory for generated Markdown files.",
    )
    args = parser.parse_args()

    result = generate_acquisition_manifests(
        _resolve_path(args.manifest_dir),
        _resolve_path(args.output_dir),
    )
    if result.passed:
        print(f"PASS acquisition manifest generation: {result.message}")
        for generated in result.generated:
            print(f"- {generated.manifest_id}: {generated.output_path}")
        return 0

    print(f"FAIL acquisition manifest generation: {result.message}")
    return 1


def _resolve_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


if __name__ == "__main__":
    raise SystemExit(main())
