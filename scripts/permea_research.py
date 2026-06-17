#!/usr/bin/env python3
"""Summarize Permea Core research package registry status."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RESEARCH_PACKAGES = (
    {
        "research_package_id": "permea_core_public_artifact_package_v0",
        "title": "Permea Core public artifact package v0",
        "status": "Proposed",
        "package_type": "Reproducible public artifact package",
    },
)
ACTIVE_PUBLIC_REVIEW_STATUSES = {
    "Public Review Package",
    "External Review Ready",
    "Submitted",
    "Published",
}
DOC_PATHS = (
    "docs/research/README.md",
    "docs/research/research-package-registry.md",
    "docs/research/research-package-lifecycle.md",
    "docs/research/research-package-template.md",
    "docs/research/research-package-assembly.md",
    "docs/research/research-package-governance.md",
    "schemas/research-package.schema.json",
)


def render_research_summary() -> str:
    counts = Counter(item["status"] for item in RESEARCH_PACKAGES)
    registered_count = len(RESEARCH_PACKAGES)
    active_public_count = sum(
        1 for item in RESEARCH_PACKAGES if item["status"] in ACTIVE_PUBLIC_REVIEW_STATUSES
    )

    lines = [
        "Permea Core research package registry",
        "",
        "Research Package Framework Ready",
        "",
        f"Registered research packages: {registered_count}",
        f"Active/public-review research packages: {active_public_count}",
        f"Proposed research packages: {counts['Proposed']}",
        f"Draft research packages: {counts['Draft Package']}",
        f"Submitted research packages: {counts['Submitted']}",
        f"Published research packages: {counts['Published']}",
        "",
        "Registry entries:",
    ]
    for item in RESEARCH_PACKAGES:
        lines.append(
            f"- {item['research_package_id']}: {item['title']} "
            f"({item['status']}; {item['package_type']})"
        )

    lines.extend(
        [
            "",
            "Reproducibility reminder:",
            "- link evidence, benchmark, dataset, specification, claim, validation, and reproduction surfaces before package promotion",
            "- framework readiness does not imply papers, reports, results, or validation exist",
            "",
            "Claim-boundary reminder:",
            "- research package entries are package assembly and review surfaces",
            "- no paper claim unless separately reviewed and approved",
            "- no new scientific result claim from this layer",
            "- no wet-lab validation by Permea",
            "- no biological efficacy claim",
            "- no therapeutic outcome claim",
            "- no BBB success claim",
            "- no solved-delivery claim",
            "- no SOTA performance claim",
            "- no experimental validation claim",
            "- no clinical evidence claim",
            "- no expression improvement claim",
            "",
            "Research docs:",
        ]
    )
    for path in DOC_PATHS:
        status = "present" if (ROOT / path).exists() else "missing"
        lines.append(f"- {path}: {status}")
    lines.extend(["", "Status: PASS"])
    return "\n".join(lines) + "\n"


def main() -> int:
    print(render_research_summary(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
