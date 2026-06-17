#!/usr/bin/env python3
"""Summarize Permea Core signal integration status."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXTERNAL_EVIDENCE_PACKAGES = (
    {
        "evidence_package_id": "permea_signal_ml_public_evidence_package",
        "package_name": "permea-signal-ml",
        "repository": "https://github.com/Permea-lab/permea-signal-ml",
        "status": "documented",
        "evidence_type": "computational evidence package",
    },
)
LINKED_CORE_LAYERS = (
    "Evidence Navigation Layer",
    "Dataset Registry Layer",
    "Benchmark Registry Layer",
    "Benchmark Execution Layer",
    "Research Package Layer",
    "Public Review Packet Layer",
    "Claim Registry",
    "Validation and Reproducibility Commands",
)
DOC_PATHS = (
    "docs/integrations/README.md",
    "docs/integrations/permea-signal-ml.md",
    "docs/integrations/external-evidence-package-template.md",
    "docs/integrations/external-evidence-package-governance.md",
    "schemas/external-evidence-package.schema.json",
)


def render_signal_summary() -> str:
    lines = [
        "Permea Core signal integration",
        "",
        "Signal Integration Layer Ready",
        "",
        f"Registered external evidence packages: {len(EXTERNAL_EVIDENCE_PACKAGES)}",
        "",
        "External evidence packages:",
    ]
    for package in EXTERNAL_EVIDENCE_PACKAGES:
        lines.append(
            "- {evidence_package_id}: {package_name} ({status}; {evidence_type})".format(
                **package
            )
        )
        lines.append(f"  repository: {package['repository']}")

    lines.extend(["", "Linked Permea Core layers:"])
    for layer in LINKED_CORE_LAYERS:
        lines.append(f"- {layer}")

    lines.extend(["", "Integration docs:"])
    for path in DOC_PATHS:
        status = "present" if (ROOT / path).exists() else "missing"
        lines.append(f"- {path}: {status}")

    lines.extend(
        [
            "",
            "Repository boundary reminder:",
            "- keep raw datasets, notebooks, bulky experiment code, and package-specific generated outputs outside Permea Core",
            "- use Permea Core for integration metadata, schemas, governance, review paths, and claim boundaries",
            "",
            "Claim-boundary reminder:",
            "- signal integration is computational-only and review-oriented",
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
    print(render_signal_summary(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
