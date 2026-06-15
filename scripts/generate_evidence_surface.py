#!/usr/bin/env python3
"""Generate the public Permea Core evidence surface README."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.surface.evidence_surface import (  # noqa: E402
    DEFAULT_EVIDENCE_SURFACE_PATH,
    PASS,
    write_evidence_surface,
)


def main() -> int:
    try:
        result = write_evidence_surface(DEFAULT_EVIDENCE_SURFACE_PATH, ROOT)
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"FAIL evidence surface generation: {exc}")
        return 1

    print(
        "PASS evidence surface generation: "
        f"{result['surface_id']} -> {result['output_path']}"
    )
    print(f"- readme: {result['output_path']}")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
