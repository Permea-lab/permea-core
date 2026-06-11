#!/usr/bin/env python3
"""Validate Permea dataset card YAML files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.datasets.cards import (  # noqa: E402
    DEFAULT_DATASET_CARD_DIR,
    validate_dataset_card_file,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Permea dataset cards.")
    parser.add_argument(
        "dataset_card_dir",
        nargs="?",
        default=str(DEFAULT_DATASET_CARD_DIR),
        help="Directory containing dataset card YAML files.",
    )
    args = parser.parse_args()

    card_dir = _resolve_path(args.dataset_card_dir)
    results = [validate_dataset_card_file(path) for path in sorted(card_dir.glob("*.yaml"))]

    failed = [result for result in results if not result.passed]
    if not failed and results:
        print(f"PASS dataset card validation: {len(results)} card(s)")
        return 0

    if not results:
        print(f"FAIL dataset card validation: no YAML files found in {card_dir}")
        return 1

    print("FAIL dataset card validation")
    for result in failed:
        print(f"{result.path}:")
        for error in result.errors:
            print(f"- {error.entry}: {error.field}: {error.message}")
    return 1


def _resolve_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


if __name__ == "__main__":
    raise SystemExit(main())
