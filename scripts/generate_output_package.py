#!/usr/bin/env python3
"""Generate a deterministic public-safe example output package."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.benchmarks.output_package import (  # noqa: E402
    DEFAULT_OUTPUT_PACKAGE_DIR,
    DEFAULT_OUTPUT_PACKAGE_INPUT,
    generate_output_package,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a Permea example benchmark output package."
    )
    parser.add_argument(
        "input_path",
        nargs="?",
        default=str(DEFAULT_OUTPUT_PACKAGE_INPUT),
        help="Benchmark YAML path. Defaults to benchmarks/bbb_b3pred_dataset3.yaml.",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default=str(DEFAULT_OUTPUT_PACKAGE_DIR),
        help=(
            "Output package directory. Defaults to "
            "docs/examples/generated/output_packages/bbb_b3pred_dataset3/."
        ),
    )
    args = parser.parse_args()

    result = generate_output_package(ROOT / args.input_path, ROOT / args.output_dir)
    if result.passed:
        print(
            "PASS output package generation: "
            f"{result.benchmark_id} -> {result.output_dir}"
        )
        for path in result.files_written:
            print(f"- {path}")
        return 0

    print(f"FAIL output package generation: {result.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
