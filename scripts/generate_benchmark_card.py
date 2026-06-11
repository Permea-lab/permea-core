#!/usr/bin/env python3
"""Generate public-safe Permea benchmark cards from registry metadata."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.benchmarks.cards import (  # noqa: E402
    DEFAULT_BENCHMARK_CARD_DIR,
    generate_benchmark_card_file,
    generate_benchmark_cards_from_registry,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Permea benchmark card Markdown."
    )
    parser.add_argument(
        "input_path",
        nargs="?",
        help="Optional single benchmark YAML path.",
    )
    parser.add_argument(
        "output_path",
        nargs="?",
        help="Optional Markdown output path for a single benchmark YAML path.",
    )
    args = parser.parse_args()

    if bool(args.input_path) != bool(args.output_path):
        print("FAIL benchmark card generation: provide both input_path and output_path.")
        return 2

    if args.input_path and args.output_path:
        result = generate_benchmark_card_file(ROOT / args.input_path, ROOT / args.output_path)
        if result.passed:
            print(
                "PASS benchmark card generation: "
                f"{result.benchmark_id} -> {result.output_path}"
            )
            return 0
        print(f"FAIL benchmark card generation: {result.message}")
        return 1

    result = generate_benchmark_cards_from_registry(
        ROOT / "benchmarks" / "registry.yaml",
        ROOT / DEFAULT_BENCHMARK_CARD_DIR,
    )
    if result.passed:
        print(f"PASS benchmark card generation: {result.message}")
        for generated in result.generated:
            print(f"- {generated.benchmark_id}: {generated.output_path}")
        return 0

    print(f"FAIL benchmark card generation: {result.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
