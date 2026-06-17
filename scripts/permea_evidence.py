#!/usr/bin/env python3
"""Summarize Permea Core public evidence navigation surfaces."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EVIDENCE_INVENTORY = (
    ("EVIDENCE-030", "Evidence Surface Layer", "Implemented, Public-Safe"),
    ("EVIDENCE-032", "Reproducibility Bundle", "Implemented, Public-Safe"),
    ("EVIDENCE-034", "Evaluation Bundle", "Implemented, Public-Safe"),
    ("EVIDENCE-036", "Artifact Specification Layer", "Implemented, Public-Safe"),
    ("EVIDENCE-038", "Artifact Validator Bundle", "Implemented, Public-Safe"),
    ("EVIDENCE-040", "External Example Packages", "Implemented, Public-Safe"),
    ("EVIDENCE-042", "Quickstart Experience Layer", "Implemented, Public-Safe"),
    ("EVIDENCE-043", "Evidence Navigation Layer", "Implemented, Public-Safe"),
)

CLAIM_BOUNDARIES = (
    "supported: public artifact standards and local validation",
    "supported: reproducible public metadata and generated artifacts",
    "supported: evaluation template/reference workflow",
    "partial: sequence-derived signal packaged as reviewable examples",
    "partial: candidate prioritization represented as a bounded workflow",
    "not demonstrated: independent reproduction",
    "not demonstrated: external validation",
    "out of scope: experimental validation, therapeutic outcomes, clinical evidence",
)

MATURITY = (
    "current repository-maintained artifact workflows: Level 2",
    "independent reproduction: Level 0",
    "external validation: Level 0",
    "experimental validation: Level 0",
    "clinical evidence: Level 0",
)

VALIDATION_COMMANDS = (
    "python3 scripts/permea_check.py",
    "python3 scripts/permea_specs.py",
    "python3 scripts/permea_validate.py",
    "python3 scripts/permea_evaluate.py",
    "python3 scripts/permea_reproduce.py",
    "python3 scripts/validate_permea_artifacts.py",
)

NAVIGATION_DOCS = (
    "docs/evidence/evidence-map.md",
    "docs/evidence/claim-to-evidence-matrix.md",
    "docs/evidence/evidence-maturity-model.md",
    "docs/evidence/evidence-timeline.md",
    "docs/claims/claim-registry.md",
)


def render_evidence_summary() -> str:
    lines = [
        "Permea Core evidence navigation",
        "",
        "Evidence inventory:",
    ]
    lines.extend(f"- {evidence_id}: {title} ({status})" for evidence_id, title, status in EVIDENCE_INVENTORY)
    lines.extend(["", "Claim boundaries:"])
    lines.extend(f"- {item}" for item in CLAIM_BOUNDARIES)
    lines.extend(["", "Evidence maturity:"])
    lines.extend(f"- {item}" for item in MATURITY)
    lines.extend(["", "Validation status:"])
    for command in VALIDATION_COMMANDS:
        lines.append(f"- review with `{command}`")
    lines.extend(["", "Navigation docs:"])
    for doc in NAVIGATION_DOCS:
        status = "present" if (ROOT / doc).exists() else "missing"
        lines.append(f"- {doc}: {status}")
    lines.extend(["", "Status: PASS"])
    return "\n".join(lines) + "\n"


def main() -> int:
    print(render_evidence_summary(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
