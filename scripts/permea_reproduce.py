#!/usr/bin/env python3
"""Reproduce Permea Core public artifact surfaces."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.reproducibility.bundle import PASS, write_reproducibility_report  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="write only the reproducibility report without rerunning all generators",
    )
    args = parser.parse_args()

    steps: list[tuple[str, list[str]]] = []
    if not args.report_only:
        steps.append(("generate public artifact surfaces", [sys.executable, "scripts/generate_permea_artifacts.py"]))
        steps.append(("generate evaluation packet", [sys.executable, "scripts/permea_evaluate.py"]))
    steps.append(("write reproducibility report", [sys.executable, "scripts/permea_reproduce.py", "--report-only"]))

    if args.report_only:
        try:
            result = write_reproducibility_report(root_path=ROOT)
        except Exception as exc:  # pragma: no cover - defensive CLI reporting
            print(f"FAIL reproducibility report generation: {exc}")
            return 1
        print(
            "PASS reproducibility report generation: "
            f"{result['run_name']} -> {result['output_paths']['markdown']}"
        )
        for label, path in result["output_paths"].items():
            print(f"- {label}: {path}")
        return 0 if result["status"] == PASS else 1

    print("Running Permea Core public reproduction...")
    for label, command in steps:
        completed = subprocess.run(command, cwd=ROOT, check=False, text=True)
        status = PASS if completed.returncode == 0 else "FAIL"
        print(f"- {status} {label}: {' '.join(command)}")
        if completed.returncode != 0:
            return completed.returncode
    print("PASS Permea public reproduction")
    print("- evidence surface: docs/examples/generated/README.md")
    print("- evaluation packet: docs/examples/generated/EVALUATION_PACKET.md")
    print("- reproducibility report: docs/examples/generated/REPRODUCIBILITY_REPORT.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
