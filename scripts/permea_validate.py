#!/usr/bin/env python3
"""Validate Permea Core public artifact surfaces."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.reproducibility.bundle import (  # noqa: E402
    PASS,
    validate_reproducibility_bundle,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bundle-only",
        action="store_true",
        help="validate only reproducibility bundle files and links",
    )
    args = parser.parse_args()

    if not args.bundle_only:
        completed = subprocess.run(
            [sys.executable, "scripts/validate_permea_artifacts.py"],
            cwd=ROOT,
            check=False,
            text=True,
        )
        print(f"- {'PASS' if completed.returncode == 0 else 'FAIL'} unified artifact validation")
        if completed.returncode != 0:
            return completed.returncode

    result = validate_reproducibility_bundle(ROOT)
    print(f"{result['status']} reproducibility bundle validation")
    for check in result["checks"]:
        print(f"- {check['status']} {check['name']}")
    return 0 if result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
