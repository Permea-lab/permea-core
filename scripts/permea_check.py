#!/usr/bin/env python3
"""Run the public Permea artifact validator."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.validation.artifact_validator import (  # noqa: E402
    FAIL,
    render_summary,
    summarize_results,
    validate_artifact,
    validate_builtin_artifacts,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "artifact",
        nargs="?",
        help="optional repo-relative artifact file or output-package directory to validate",
    )
    args = parser.parse_args()

    if args.artifact:
        result = validate_artifact(args.artifact, ROOT)
        summary = summarize_results([result])
    else:
        summary = validate_builtin_artifacts(ROOT)

    print(render_summary(summary), end="")
    return 1 if summary["status"] == FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
