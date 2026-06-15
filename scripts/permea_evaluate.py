#!/usr/bin/env python3
"""Generate the public Permea Core evaluation packet."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.evaluation.bundle import (  # noqa: E402
    DEFAULT_EVALUATION_OUTPUT_DIR,
    PASS,
    write_evaluation_packet,
)


def main() -> int:
    try:
        result = write_evaluation_packet(DEFAULT_EVALUATION_OUTPUT_DIR, ROOT)
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"FAIL evaluation packet generation: {exc}")
        return 1

    print(
        "PASS evaluation packet generation: "
        f"{result['bundle_name']} -> {result['output_paths']['markdown']}"
    )
    print("- referenced input families:")
    for item in result["reference_inputs"]:
        print(f"  - {item['path']}")
    print("- generated outputs:")
    for label, path in result["output_paths"].items():
        print(f"  - {label}: {path}")
    print("- next validation: python3 scripts/permea_validate.py")
    print("- next reproduction: python3 scripts/permea_reproduce.py")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())

