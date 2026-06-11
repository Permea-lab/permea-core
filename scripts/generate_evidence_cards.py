#!/usr/bin/env python3
"""Generate deterministic public-safe example evidence cards."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.benchmarks.evidence_cards import (  # noqa: E402
    DEFAULT_EVIDENCE_CARD_DIR,
    DEFAULT_EVIDENCE_CARD_INPUTS,
    generate_evidence_cards_file,
    generate_evidence_cards_for_inputs,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Permea example evidence card JSON."
    )
    parser.add_argument(
        "input_path",
        nargs="?",
        help="Optional single benchmark YAML path.",
    )
    parser.add_argument(
        "output_path",
        nargs="?",
        help="Optional output JSON path for a single benchmark YAML path.",
    )
    args = parser.parse_args()

    if bool(args.input_path) != bool(args.output_path):
        print("FAIL evidence card generation: provide both input_path and output_path.")
        return 2

    if args.input_path and args.output_path:
        result = generate_evidence_cards_file(
            ROOT / args.input_path,
            ROOT / args.output_path,
        )
        if result.passed:
            print(
                "PASS evidence card generation: "
                f"{result.benchmark_id} -> {result.output_path}"
            )
            return 0
        print(f"FAIL evidence card generation: {result.message}")
        return 1

    result = generate_evidence_cards_for_inputs(
        tuple(ROOT / path for path in DEFAULT_EVIDENCE_CARD_INPUTS),
        ROOT / DEFAULT_EVIDENCE_CARD_DIR,
    )
    if result.passed:
        print(f"PASS evidence card generation: {result.message}")
        for generated in result.generated:
            print(f"- {generated.benchmark_id}: {generated.output_path}")
        return 0

    print(f"FAIL evidence card generation: {result.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
