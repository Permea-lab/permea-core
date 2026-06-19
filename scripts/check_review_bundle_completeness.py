#!/usr/bin/env python3
"""Check public review bundle completeness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.review_packets.bundle_completeness import (  # noqa: E402
    DEFAULT_SAMPLE_BUNDLE,
    PASS,
    check_review_bundle_completeness,
    check_review_bundle_file,
    render_bundle_completeness_summary,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "bundle_path",
        nargs="?",
        help="optional path to a review bundle text file; defaults to the built-in public sample",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="print deterministic JSON instead of a human-readable summary",
    )
    args = parser.parse_args()

    result = (
        check_review_bundle_file(Path(args.bundle_path))
        if args.bundle_path
        else check_review_bundle_completeness(DEFAULT_SAMPLE_BUNDLE)
    )
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_bundle_completeness_summary(result), end="")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
