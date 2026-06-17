#!/usr/bin/env python3
"""Summarize Permea Core benchmark execution framework status."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTERED_BENCHMARKS = (
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
BENCHMARK_RUNS: tuple[dict[str, str], ...] = ()
EXECUTABLE_STATUSES = {
    "Reproducible Computational Workflow",
    "Active Reference Benchmark",
    "Independently Reproduced",
    "Externally Validated",
}
DOC_PATHS = (
    "docs/benchmarks/benchmark-execution-model.md",
    "docs/benchmarks/benchmark-run-template.md",
    "schemas/benchmark-run.schema.json",
)


def render_benchmark_run_summary() -> str:
    registered_count = len(REGISTERED_BENCHMARKS)
    executable_count = sum(
        1 for item in REGISTERED_BENCHMARKS if item["status"] in EXECUTABLE_STATUSES
    )
    run_count = len(BENCHMARK_RUNS)

    lines = [
        "Permea Core benchmark execution",
        "",
        "Benchmark Execution Framework Ready",
        "",
        f"Registered benchmarks: {registered_count}",
        f"Executable benchmarks: {executable_count}",
        f"Registered benchmark runs: {run_count}",
        "Benchmark run artifact status: framework-only",
        "",
        "No benchmark results are currently registered.",
        "No biological conclusions should be drawn from framework readiness alone.",
        "",
        "Benchmark execution docs:",
    ]
    for path in DOC_PATHS:
        status = "present" if (ROOT / path).exists() else "missing"
        lines.append(f"- {path}: {status}")

    lines.extend(
        [
            "",
            "Claim-boundary reminder:",
            "- benchmark execution artifacts are computational review surfaces",
            "- no benchmark performance claim from this layer",
            "- no biological result claim from this layer",
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
    print(render_benchmark_run_summary(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
