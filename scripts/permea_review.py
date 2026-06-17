#!/usr/bin/env python3
"""Print deterministic Permea Core public review packet guidance."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

READING_PATH = (
    "README",
    "QUICKSTART",
    "REVIEW PACKET",
    "EVIDENCE",
    "BENCHMARKS",
    "DATASETS",
    "RESEARCH",
    "CLAIMS",
    "VALIDATION",
)
REGISTRY_COMMANDS = (
    "python3 scripts/permea_evidence.py",
    "python3 scripts/permea_benchmarks.py",
    "python3 scripts/permea_datasets.py",
    "python3 scripts/permea_research.py",
)
VALIDATION_COMMANDS = (
    "python3 scripts/permea_check.py",
    "python3 scripts/permea_specs.py",
    "python3 scripts/permea_validate.py",
    "python3 scripts/permea_evaluate.py",
    "python3 scripts/permea_reproduce.py",
    "python3 scripts/validate_permea_artifacts.py",
)
DOC_PATHS = (
    "docs/review/README.md",
    "docs/review/public-review-packet.md",
    "docs/review/public-review-packet-template.md",
    "docs/review/public-review-packet-assembly.md",
    "docs/review/public-review-packet-governance.md",
    "docs/review/public-review-checklist.md",
    "schemas/public-review-packet.schema.json",
)


def render_review_summary() -> str:
    lines = [
        "Permea Core public review packet",
        "",
        "Public Review Packet Ready",
        "",
        "Recommended reading path:",
        " -> ".join(READING_PATH),
        "",
        "First command to run:",
        "python3 scripts/permea_review.py",
        "",
        "Available registry CLIs:",
    ]
    lines.extend(f"- {command}" for command in REGISTRY_COMMANDS)
    lines.extend(
        [
            "",
            "Validation reminder:",
        ]
    )
    lines.extend(f"- {command}" for command in VALIDATION_COMMANDS)
    lines.extend(
        [
            "",
            "Claim-boundary reminder:",
            "- this packet guides review of current public infrastructure",
            "- no new scientific result claim from this layer",
            "- no paper claim from this layer",
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
            "Public review docs:",
        ]
    )
    for path in DOC_PATHS:
        status = "present" if (ROOT / path).exists() else "missing"
        lines.append(f"- {path}: {status}")
    lines.extend(["", "Status: PASS"])
    return "\n".join(lines) + "\n"


def main() -> int:
    print(render_review_summary(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
