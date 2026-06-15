#!/usr/bin/env python3
"""Generate the public Permea Core evidence matrix."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.evidence.matrix import (  # noqa: E402
    DEFAULT_EVIDENCE_MATRIX_OUTPUT_DIR,
    PASS,
    write_evidence_matrix,
)


def main() -> int:
    try:
        result = write_evidence_matrix(DEFAULT_EVIDENCE_MATRIX_OUTPUT_DIR, ROOT)
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"FAIL evidence matrix generation: {exc}")
        return 1

    print(
        "PASS evidence matrix generation: "
        f"{result['matrix_id']} -> {result['output_paths']['markdown']}"
    )
    for label, path in result["output_paths"].items():
        print(f"- {label}: {path}")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
