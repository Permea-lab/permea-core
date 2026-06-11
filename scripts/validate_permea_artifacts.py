#!/usr/bin/env python3
"""Run unified local validation for Permea Core artifacts."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.validation.artifacts import (  # noqa: E402
    PASS,
    format_validation_report,
    validate_permea_artifacts,
)


def main() -> int:
    result = validate_permea_artifacts()
    print(format_validation_report(result))
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
