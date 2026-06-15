#!/usr/bin/env python3
"""Check public Permea example artifacts against lightweight spec expectations."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.validator.checks import FAIL, check_artifacts  # noqa: E402
from permea_core.validator.report import render_check_report  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check public Permea artifact examples.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--all", action="store_true", help="Check all supported artifact families.")
    mode.add_argument("--family", choices=[
        "dataset_card",
        "benchmark_card",
        "evidence_card",
        "run_manifest",
        "output_package",
    ])
    mode.add_argument("--file", help="Check one known public artifact file.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = check_artifacts(
            ROOT,
            family=args.family,
            file_path=args.file,
        )
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"FAIL Permea artifact check: {exc}")
        return 1

    print(render_check_report(report), end="")
    return 1 if report["status"] == FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
