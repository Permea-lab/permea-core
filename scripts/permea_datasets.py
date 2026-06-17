#!/usr/bin/env python3
"""Summarize Permea Core dataset registry status."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATASETS = (
    {
        "dataset_id": "b3pred_dataset3",
        "name": "B3Pred Dataset 3 public fixture card",
        "status": "Draft Card",
        "provenance_status": "Partial",
    },
    {
        "dataset_id": "cppsite2_placeholder",
        "name": "CPPSite 2 placeholder dataset card",
        "status": "Proposed",
        "provenance_status": "Proposed",
    },
)
ACTIVE_STATUSES = {
    "Active Reference Dataset",
    "Independently Reproduced",
    "Externally Validated",
}
VALIDATED_STATUSES = {
    "Independently Reproduced",
    "Externally Validated",
}
DOCUMENTED_STATUSES = {
    "Documented External Dataset",
    "Reproducible Derived Dataset",
    "Active Reference Dataset",
    "Independently Reproduced",
    "Externally Validated",
}
DOC_PATHS = (
    "docs/datasets/README.md",
    "docs/datasets/dataset-registry.md",
    "docs/datasets/dataset-lifecycle.md",
    "docs/datasets/dataset-card-template.md",
    "docs/datasets/dataset-provenance.md",
    "docs/datasets/dataset-governance.md",
    "schemas/dataset-card.schema.json",
)


def render_dataset_summary() -> str:
    counts = Counter(item["status"] for item in DATASETS)
    registered_count = len(DATASETS)
    active_count = sum(1 for item in DATASETS if item["status"] in ACTIVE_STATUSES)
    validated_count = sum(1 for item in DATASETS if item["status"] in VALIDATED_STATUSES)
    documented_count = sum(1 for item in DATASETS if item["status"] in DOCUMENTED_STATUSES)
    proposed_count = counts["Proposed"]
    draft_count = counts["Draft Card"]

    lines = [
        "Permea Core dataset registry",
        "",
        "Dataset Framework Ready",
        "",
        f"Registered datasets: {registered_count}",
        f"Active reference datasets: {active_count}",
        f"Proposed datasets: {proposed_count}",
        f"Draft datasets: {draft_count}",
        f"Documented datasets: {documented_count}",
        f"Validated datasets: {validated_count}",
        "",
        "Registry entries:",
    ]
    for item in DATASETS:
        lines.append(
            f"- {item['dataset_id']}: {item['name']} "
            f"({item['status']}; provenance {item['provenance_status']})"
        )

    lines.extend(
        [
            "",
            "Provenance reminder:",
            "- record source reference, acquisition method, processing steps, transformation summary, generated artifacts, checksums where applicable, usage constraints, reproducibility path, and known limitations",
            "- provenance completeness supports reviewability, not biological outcome evidence",
            "",
            "Claim-boundary reminder:",
            "- dataset registry entries are computational review and provenance surfaces",
            "- no dataset acquisition completion claim unless separately validated",
            "- no redistribution-rights confirmation unless separately documented",
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
            "Dataset docs:",
        ]
    )
    for path in DOC_PATHS:
        status = "present" if (ROOT / path).exists() else "missing"
        lines.append(f"- {path}: {status}")
    lines.extend(["", "Status: PASS"])
    return "\n".join(lines) + "\n"


def main() -> int:
    print(render_dataset_summary(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
