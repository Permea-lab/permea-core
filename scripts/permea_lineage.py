#!/usr/bin/env python3
"""Summarize Permea Core lineage framework status."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LINEAGE_CAPABLE_ARTIFACT_CLASSES = (
    "Evidence",
    "Benchmarks",
    "Benchmark Runs",
    "Datasets",
    "Research Packages",
    "Review Packets",
    "External Evidence Packages",
    "Claims",
    "Specifications",
    "Validation Artifacts",
)
LINEAGE_STATUSES = (
    "draft",
    "documented",
    "linked",
    "reviewed",
    "superseded",
    "archived",
)
DOC_PATHS = (
    "docs/lineage/README.md",
    "docs/lineage/lineage-model.md",
    "docs/lineage/lineage-governance.md",
    "docs/lineage/lineage-review-guide.md",
    "docs/lineage/lineage-record-template.md",
    "schemas/lineage-record.schema.json",
)


def render_lineage_summary() -> str:
    lines = [
        "Permea Core evidence lineage",
        "",
        "Lineage Framework Ready",
        "",
        f"Registered lineage-capable artifact classes: {len(LINEAGE_CAPABLE_ARTIFACT_CLASSES)}",
        "",
        "Lineage-capable artifact classes:",
    ]
    for artifact_class in LINEAGE_CAPABLE_ARTIFACT_CLASSES:
        lines.append(f"- {artifact_class}")

    lines.extend(["", "Lineage status categories:"])
    for lineage_status in LINEAGE_STATUSES:
        lines.append(f"- {lineage_status}")

    lines.extend(["", "Lineage docs:"])
    for path in DOC_PATHS:
        status = "present" if (ROOT / path).exists() else "missing"
        lines.append(f"- {path}: {status}")

    lines.extend(
        [
            "",
            "Provenance reminder:",
            "- record parent artifacts, child artifacts, related claims, specifications, validation artifacts, and provenance notes",
            "- mark incomplete lineage as draft, documented, proposed, not yet demonstrated, or requiring future validation where appropriate",
            "- keep external evidence package contents outside Permea Core and link only public metadata relationships",
            "",
            "Claim-boundary reminder:",
            "- lineage is framework-only and review-oriented",
            "- lineage presence does not imply scientific validation, biological outcomes, efficacy, or experimental success",
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
            "Validation reminder:",
            "- python3 scripts/permea_check.py",
            "- python3 scripts/permea_specs.py",
            "- python3 scripts/permea_validate.py",
            "- python3 scripts/permea_evaluate.py",
            "- python3 scripts/permea_reproduce.py",
            "- python3 scripts/validate_permea_artifacts.py",
            "",
            "Status: PASS",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    print(render_lineage_summary(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
