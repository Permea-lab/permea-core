#!/usr/bin/env python3
"""Generate the public Permea Core artifact index."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.index.artifact_index import (  # noqa: E402
    DEFAULT_ARTIFACT_INDEX_PATH,
    generate_artifact_index,
)


def main() -> int:
    try:
        result = generate_artifact_index(DEFAULT_ARTIFACT_INDEX_PATH, ROOT)
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"FAIL artifact index generation: {exc}")
        return 1

    print(
        "PASS artifact index generation: "
        f"{result['output_path']} "
        f"({result['artifact_family_count']} families, "
        f"{result['generated_file_count']} generated files)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
