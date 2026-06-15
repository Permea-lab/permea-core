#!/usr/bin/env python3
"""Print the public Permea Core artifact specification registry."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.specs.registry import (  # noqa: E402
    PASS,
    collect_spec_registry,
    render_spec_registry,
)


def main() -> int:
    try:
        registry = collect_spec_registry(ROOT)
    except Exception as exc:  # pragma: no cover - defensive CLI reporting
        print(f"FAIL artifact specification registry: {exc}")
        return 1

    print(render_spec_registry(registry), end="")
    return 0 if registry["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())

