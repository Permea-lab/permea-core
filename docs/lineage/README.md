# Permea Lineage

The lineage layer records how Permea Core artifacts should connect across evidence, datasets, benchmarks, benchmark runs, research packages, review packets, external evidence packages, specifications, validation artifacts, and claims.

Lineage records are review surfaces. They help reviewers trace where a claim originated, which artifacts reference it, and where provenance remains incomplete or not yet validated.

## Start Here

- [Lineage model](lineage-model.md)
- [Lineage governance](lineage-governance.md)
- [Lineage review guide](lineage-review-guide.md)
- [Lineage record template](lineage-record-template.md)

## Review Command

```bash
python3 scripts/permea_lineage.py
```

The command prints lineage-capable artifact classes, lineage status categories, documentation paths, provenance reminders, and claim-boundary reminders.

## Current Public Position

Permea Core can document relationships among public operating layers, but relationship presence is not a scientific result. A complete lineage record supports auditability and reproducibility review; it does not establish biological validity, efficacy, benchmark performance, or experimental confirmation.

## Explicit Non-Claims

- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
- no clinical evidence claim
- no expression improvement claim
