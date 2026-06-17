#!/usr/bin/env python3
"""Run the first-user Permea Core quickstart demo."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.validation.artifact_validator import (  # noqa: E402
    PASS,
    validate_artifact,
)

EXAMPLES_ROOT = ROOT / "examples"
EXAMPLE_PACKAGE_FILES = (
    "README.md",
    "dataset_card.json",
    "benchmark_card.json",
    "evidence_card.json",
    "run_manifest.json",
    "output_package.json",
    "validation_result.json",
)
EVIDENCE_LINKS = (
    "docs/evidence/evidence-index.md",
    "docs/claims/claim-registry.md",
    "docs/CLAIM_BOUNDARY.md",
)
NEXT_COMMANDS = (
    "python3 scripts/permea_check.py",
    "python3 scripts/permea_validate.py",
    "python3 scripts/permea_specs.py",
)


def discover_example_packages() -> list[Path]:
    """Return deterministic public example packages."""
    packages: list[Path] = []
    for candidate in sorted(EXAMPLES_ROOT.iterdir()):
        if not candidate.is_dir():
            continue
        if all((candidate / name).exists() for name in EXAMPLE_PACKAGE_FILES):
            packages.append(candidate)
    return packages


def render_demo() -> tuple[int, str]:
    """Run discovery and validation, returning an exit code plus output."""
    lines = [
        "Permea Core quickstart demo",
        "",
        "What Permea Core is:",
        "- A public execution and specification layer for benchmark-first delivery evidence artifacts.",
        "- It helps researchers and developers inspect, validate, and reproduce structured example packages.",
        "",
        "What the example packages demonstrate:",
        "- dataset cards, benchmark cards, evidence cards, run manifests, and output packages",
        "- repo-relative paths, explicit non-claims, and validator-compatible package structure",
        "",
        "Example package discovery:",
    ]

    packages = discover_example_packages()
    if not packages:
        lines.append("- none found")
        lines.append("")
        lines.append("Status: FAIL")
        return 1, "\n".join(lines) + "\n"

    for package in packages:
        lines.append(f"- {package.relative_to(ROOT)}")

    lines.extend(["", "Validator execution:"])
    status = PASS
    for package in packages:
        result = validate_artifact(package, ROOT)
        if result["status"] != PASS:
            status = result["status"]
        lines.append(
            f"- {result['artifact_path']}: {result['status']} "
            f"({len(result['checks'])} checks)"
        )

    lines.extend(
        [
            "",
            "Evidence and claim boundaries:",
            *[f"- {link}" for link in EVIDENCE_LINKS],
            "",
            "What is not claimed:",
            "- no dataset downloaded",
            "- no acquisition executed",
            "- no redistribution rights confirmed",
            "- no wet-lab validation by Permea",
            "- no clinical efficacy claim",
            "- no model performance claim",
            "- no SOTA claim",
            "- no solved-delivery claim",
            "",
            "What output to expect:",
            f"- {len(packages)} example packages discovered",
            f"- validator status: {status}",
            "",
            "Next recommended commands:",
            *[f"- {command}" for command in NEXT_COMMANDS],
            "",
            f"Status: {status}",
        ]
    )
    return 0 if status == PASS else 1, "\n".join(lines) + "\n"


def main() -> int:
    exit_code, output = render_demo()
    print(output, end="")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
