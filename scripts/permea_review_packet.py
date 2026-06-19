#!/usr/bin/env python3
"""Generate Permea Core public evidence review packets."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.review_packets import (  # noqa: E402
    generate_review_packets,
    render_summary,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="write packets without printing the human-readable summary",
    )
    args = parser.parse_args()

    result = generate_review_packets(ROOT)
    if not args.quiet:
        print(render_summary(result), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
