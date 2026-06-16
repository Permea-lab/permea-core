# Evidence Index

This index maps current public evidence surfaces to reports, generated artifacts, decisions, validations, supported claims, unsupported claims, limitations, and next evidence steps.

## Evidence Entries

| Evidence ID | Title | Status | Source task/group | Primary report | Validation surface |
| --- | --- | --- | --- | --- | --- |
| EVIDENCE-030 | Evidence Surface Layer | Implemented, Public-Safe | Group P-CORE-030 | [Generated evidence surface](../examples/generated/README.md) | `python3 scripts/generate_evidence_surface.py` |
| EVIDENCE-032 | Reproducibility Bundle | Implemented, Public-Safe | Group P-CORE-032 | [Reproducibility report](../examples/generated/REPRODUCIBILITY_REPORT.md) | `python3 scripts/permea_reproduce.py` and `python3 scripts/permea_validate.py` |
| EVIDENCE-034 | Evaluation Bundle | Implemented, Public-Safe | Group P-CORE-034 | [Evaluation packet](../examples/generated/EVALUATION_PACKET.md) | `python3 scripts/permea_evaluate.py` and `python3 scripts/permea_validate.py` |
| EVIDENCE-036 | Artifact Specification Layer | Implemented, Public-Safe | Group P-CORE-036 | [Artifact specification report](../reports/p-core-036-artifact-specification-layer.md) | `python3 scripts/permea_specs.py` |
| EVIDENCE-038 | Artifact Validator Bundle | Implemented, Public-Safe | Group P-CORE-038 | [Artifact validator report](../reports/p-core-038-artifact-validator-bundle-v0.md) | `python3 scripts/permea_check.py` |

## Detailed Mapping

### EVIDENCE-030: Evidence Surface Layer

- Evidence ID: EVIDENCE-030
- Status: Implemented, Public-Safe
- Source task/group: Group P-CORE-030
- Primary report: [Generated evidence surface](../examples/generated/README.md)
- Primary generated artifacts: [Demo packet](../examples/generated/DEMO_PACKET.md), [Artifact index](../examples/generated/ARTIFACT_INDEX.md), [Evidence matrix](../examples/generated/EVIDENCE_MATRIX.md), [Dry-run report](../examples/generated/dry_runs/example_benchmark_dry_run.md)
- Primary docs: [README](../../README.md), [Quickstart](../../QUICKSTART.md)
- Relevant decisions: [DEC-002](../decisions/DEC-002-evidence-bundle-before-claims.md), [DEC-006](../decisions/DEC-006-project-memory-layer-required-for-continuation.md)
- Validation surface: `python3 scripts/generate_evidence_surface.py`
- Supported public claims: Permea Core has a public navigation surface for generated artifact review.
- Unsupported claims: no biological validation, model performance, source acquisition, or redistribution-rights claim.
- Limitations: The surface indexes public artifacts and commands; it does not create new scientific evidence.
- Next evidence step: Keep evidence records synchronized with new generated surfaces.

### EVIDENCE-032: Reproducibility Bundle

- Evidence ID: EVIDENCE-032
- Status: Implemented, Public-Safe
- Source task/group: Group P-CORE-032
- Primary report: [Reproducibility report](../examples/generated/REPRODUCIBILITY_REPORT.md)
- Primary generated artifacts: [Reproducibility report JSON](../examples/generated/REPRODUCIBILITY_REPORT.json), [Generated evidence surface](../examples/generated/README.md)
- Primary docs: [Reproducibility guide](../../REPRODUCIBILITY.md), [Quickstart](../../QUICKSTART.md)
- Relevant decisions: [DEC-001](../decisions/DEC-001-reproducibility-first-program-structure.md), [DEC-002](../decisions/DEC-002-evidence-bundle-before-claims.md)
- Validation surface: `python3 scripts/permea_reproduce.py` and `python3 scripts/permea_validate.py`
- Supported public claims: Public artifact surfaces can be regenerated and validated locally.
- Unsupported claims: no dataset download, acquisition execution, model scoring, or performance measurement.
- Limitations: Reproducibility is currently for public metadata and generated examples.
- Next evidence step: Add evidence records when new reproducible artifact families are merged.

### EVIDENCE-034: Evaluation Bundle

- Evidence ID: EVIDENCE-034
- Status: Implemented, Public-Safe
- Source task/group: Group P-CORE-034
- Primary report: [Evaluation packet](../examples/generated/EVALUATION_PACKET.md)
- Primary generated artifacts: [Evaluation packet JSON](../examples/generated/EVALUATION_PACKET.json), [Artifact index](../examples/generated/ARTIFACT_INDEX.md)
- Primary docs: [Evaluation guide](../../EVALUATION.md), [Generated evidence surface](../examples/generated/README.md)
- Relevant decisions: [DEC-003](../decisions/DEC-003-evaluation-bundle-as-user-transfer-layer.md), [DEC-005](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)
- Validation surface: `python3 scripts/permea_evaluate.py` and `python3 scripts/permea_validate.py`
- Supported public claims: Permea Core provides a template/reference evaluation packet for artifact-system extension.
- Unsupported claims: no completed evaluation result, biological performance, clinical effectiveness, or model-performance claim.
- Limitations: The packet transfers an artifact pattern; it does not prove an experimental or model result.
- Next evidence step: Keep evaluation evidence linked to future public input-family examples.

### EVIDENCE-036: Artifact Specification Layer

- Evidence ID: EVIDENCE-036
- Status: Implemented, Public-Safe
- Source task/group: Group P-CORE-036
- Primary report: [Artifact specification report](../reports/p-core-036-artifact-specification-layer.md)
- Primary generated artifacts: [Specification registry output](../../scripts/permea_specs.py), [Schemas](../../schemas/)
- Primary docs: [Public artifact specifications](../specs/README.md)
- Relevant decisions: [DEC-004](../decisions/DEC-004-specification-layer-for-permea-standard.md), [DEC-005](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)
- Validation surface: `python3 scripts/permea_specs.py`
- Supported public claims: Permea Core defines public artifact standards and lightweight schemas for current artifact families.
- Unsupported claims: no source access confirmation, redistribution-rights confirmation, biological validation, or model-performance claim.
- Limitations: The specification layer defines structure; it is not a validator bundle by itself.
- Next evidence step: Keep validator checks aligned with future artifact families.

### EVIDENCE-038: Artifact Validator Bundle

- Evidence ID: EVIDENCE-038
- Status: Implemented, Public-Safe
- Source task/group: Group P-CORE-038
- Primary report: [Artifact validator report](../reports/p-core-038-artifact-validator-bundle-v0.md)
- Primary generated artifacts: built-in public dataset-card, benchmark-card, evidence-card, run-manifest, and output-package examples under [generated examples](../examples/generated/README.md)
- Primary docs: [Public artifact specifications](../specs/README.md), [Claim registry](../claims/claim-registry.md)
- Relevant decisions: [DEC-004](../decisions/DEC-004-specification-layer-for-permea-standard.md), [DEC-005](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)
- Validation surface: `python3 scripts/permea_check.py`
- Supported public claims: Permea Core can check current public artifact examples against lightweight structure, non-claim, claim-boundary, repo-relative path, and evidence-linkage expectations.
- Unsupported claims: no source access confirmation, redistribution-rights confirmation, biological validation, clinical effectiveness, or model-performance claim.
- Limitations: The validator checks current public example artifacts and structural expectations; it is not a scientific result validator.
- Next evidence step: Extend validator coverage when new artifact families or stricter schemas are introduced.
