#!/usr/bin/env python3
"""Check generated review packet coverage consistency."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.review_packets.coverage import (  # noqa: E402
    PASS,
    check_review_packet_coverage,
    render_coverage_summary,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        action="store_true",
        help="print deterministic JSON instead of a human-readable summary",
    )
    args = parser.parse_args()

    result = check_review_packet_coverage(ROOT)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_coverage_summary(result), end="")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
