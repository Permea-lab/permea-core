#!/usr/bin/env python3
"""Review Permea Core public artifact consistency."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.consistency.artifacts import (  # noqa: E402
    PASS,
    render_json,
    render_summary,
    validate_artifact_consistency,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        action="store_true",
        help="print deterministic JSON instead of the human-readable summary",
    )
    args = parser.parse_args()

    result = validate_artifact_consistency(ROOT)
    print(render_json(result) if args.json else render_summary(result), end="")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
