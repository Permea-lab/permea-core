#!/usr/bin/env python3
"""Run the deterministic Permea Core benchmark dry-run."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.dry_run.orchestrator import (  # noqa: E402
    DEFAULT_DRY_RUN_OUTPUT_DIR,
    PASS,
    write_dry_run_outputs,
)


def main() -> int:
    try:
        result = write_dry_run_outputs(DEFAULT_DRY_RUN_OUTPUT_DIR, ROOT)
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"FAIL benchmark dry-run: {exc}")
        return 1

    print(
        "PASS benchmark dry-run: "
        f"{result['dry_run_id']} -> {result['output_paths']['markdown']}"
    )
    for label, path in result["output_paths"].items():
        print(f"- {label}: {path}")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
