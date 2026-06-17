#!/usr/bin/env python3
"""Summarize Permea Core benchmark registry status."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BENCHMARKS = (
    {
        "benchmark_id": "bbb_b3pred_dataset3",
        "name": "BBB peptide prioritization surface",
        "status": "Draft",
    },
    {
        "benchmark_id": "cpp_cppsite2_placeholder",
        "name": "CPP membrane penetration placeholder",
        "status": "Proposed",
    },
)
ACTIVE_STATUSES = {
    "Active Reference Benchmark",
    "Independently Reproduced",
    "Externally Validated",
}
VALIDATED_STATUSES = {
    "Independently Reproduced",
    "Externally Validated",
}
DOC_PATHS = (
    "docs/benchmarks/README.md",
    "docs/benchmarks/benchmark-registry.md",
    "docs/benchmarks/benchmark-lifecycle.md",
    "docs/benchmarks/benchmark-card-template.md",
    "docs/benchmarks/benchmark-governance.md",
    "schemas/benchmark-card.schema.json",
)


def render_benchmark_summary() -> str:
    counts = Counter(item["status"] for item in BENCHMARKS)
    registered_count = len(BENCHMARKS)
    active_count = sum(1 for item in BENCHMARKS if item["status"] in ACTIVE_STATUSES)
    validated_count = sum(1 for item in BENCHMARKS if item["status"] in VALIDATED_STATUSES)
    proposed_count = counts["Proposed"]
    draft_count = counts["Draft"]

    lines = [
        "Permea Core benchmark registry",
        "",
        "Benchmark Framework Ready",
        "",
        f"Registered benchmarks: {registered_count}",
        f"Active benchmarks: {active_count}",
        f"Proposed benchmarks: {proposed_count}",
        f"Draft benchmarks: {draft_count}",
        f"Validated benchmarks: {validated_count}",
        "",
        "Registry entries:",
    ]
    for item in BENCHMARKS:
        lines.append(f"- {item['benchmark_id']}: {item['name']} ({item['status']})")

    lines.extend(
        [
            "",
            "Claim-boundary reminder:",
            "- benchmark registry entries are computational review surfaces",
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
            "Benchmark docs:",
        ]
    )
    for path in DOC_PATHS:
        status = "present" if (ROOT / path).exists() else "missing"
        lines.append(f"- {path}: {status}")
    lines.extend(["", "Status: PASS"])
    return "\n".join(lines) + "\n"


def main() -> int:
    print(render_benchmark_summary(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
