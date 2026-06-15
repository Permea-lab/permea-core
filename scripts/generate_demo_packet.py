#!/usr/bin/env python3
"""Generate the public Permea Core demo packet."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.demo.packet import (  # noqa: E402
    DEFAULT_DEMO_PACKET_OUTPUT_DIR,
    PASS,
    write_demo_packet,
)


def main() -> int:
    try:
        result = write_demo_packet(DEFAULT_DEMO_PACKET_OUTPUT_DIR, ROOT)
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"FAIL demo packet generation: {exc}")
        return 1

    print(
        "PASS demo packet generation: "
        f"{result['packet_id']} -> {result['output_paths']['markdown']}"
    )
    for label, path in result["output_paths"].items():
        print(f"- {label}: {path}")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
