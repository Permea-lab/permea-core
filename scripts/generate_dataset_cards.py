#!/usr/bin/env python3
"""Generate public-safe Permea dataset cards from YAML metadata."""

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
    DEFAULT_GENERATED_DATASET_CARD_DIR,
    generate_dataset_cards,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Permea dataset card Markdown examples."
    )
    parser.add_argument(
        "dataset_card_dir",
        nargs="?",
        default=str(DEFAULT_DATASET_CARD_DIR),
        help="Directory containing dataset card YAML files.",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default=str(DEFAULT_GENERATED_DATASET_CARD_DIR),
        help="Output directory for generated Markdown files.",
    )
    args = parser.parse_args()

    result = generate_dataset_cards(
        _resolve_path(args.dataset_card_dir),
        _resolve_path(args.output_dir),
    )
    if result.passed:
        print(f"PASS dataset card generation: {result.message}")
        for generated in result.generated:
            print(f"- {generated.dataset_id}: {generated.output_path}")
        return 0

    print(f"FAIL dataset card generation: {result.message}")
    return 1


def _resolve_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


if __name__ == "__main__":
    raise SystemExit(main())
