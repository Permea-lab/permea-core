#!/usr/bin/env python3
"""Validate run manifest YAML examples."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.runs.manifests import (  # noqa: E402
    DEFAULT_RUN_MANIFEST_DIR,
    validate_run_manifest_dir,
)


def main() -> int:
    result = validate_run_manifest_dir(DEFAULT_RUN_MANIFEST_DIR)
    if result.passed:
        print(f"PASS run manifest validation: {result.message}")
        return 0

    print(f"FAIL run manifest validation: {result.message}")
    for item in result.results:
        for error in getattr(item, "errors", ()):
            print(f"- {item.path}: {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
