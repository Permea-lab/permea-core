# Permea Integrations

Permea integrations describe how external public evidence packages connect to Permea Core without copying raw datasets, notebooks, bulky experiment code, or package-specific sprawl into Core.

Integration docs are review surfaces. They help reviewers understand package purpose, linked Core layers, reproducibility paths, validation paths, claim boundaries, and limitations.

## Start Here

- [Permea Signal ML integration](permea-signal-ml.md)
- [External evidence package template](external-evidence-package-template.md)
- [External evidence package governance](external-evidence-package-governance.md)

## Review Command

```bash
python3 scripts/permea_signal.py
```

The command prints registered external evidence packages, linked Permea Core layers, claim-boundary reminders, validation reminders, and integration documentation paths.

## Current Public Position

Permea Core may reference adjacent public evidence packages, but Core remains the operating layer for standards, registries, schemas, review paths, and claim boundaries.

External evidence packages remain responsible for their own package-specific code, generated artifacts, reproducibility commands, and release posture.

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
