#!/usr/bin/env python3
"""Generate deterministic run manifest Markdown examples."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.runs.manifests import (  # noqa: E402
    DEFAULT_GENERATED_RUN_MANIFEST_DIR,
    DEFAULT_RUN_MANIFEST_DIR,
    generate_run_manifests,
)


def main() -> int:
    result = generate_run_manifests(
        DEFAULT_RUN_MANIFEST_DIR,
        DEFAULT_GENERATED_RUN_MANIFEST_DIR,
    )
    if result.passed:
        print(f"PASS run manifest generation: {result.message}")
        for item in result.results:
            print(f"- {item.output_path}")
        return 0

    print(f"FAIL run manifest generation: {result.message}")
    for item in result.results:
        print(f"- {item.input_path}: {item.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
