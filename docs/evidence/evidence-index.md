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
| EVIDENCE-040 | External Example Packages | Implemented, Public-Safe | Group P-CORE-040 | [External examples report](../reports/p-core-040-external-example-packages-v0.md) | `python3 scripts/permea_check.py examples/synthetic_reference_example` |
| EVIDENCE-042 | Quickstart Experience Layer | Implemented, Public-Safe | Group P-CORE-042 | [Quickstart experience report](../reports/p-core-042-quickstart-experience-layer-v0.md) | `python3 scripts/permea_demo.py` |
| EVIDENCE-043 | Evidence Navigation Layer | Implemented, Public-Safe | Group P-CORE-043 | [Evidence map](evidence-map.md) | `python3 scripts/permea_evidence.py` |

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

### EVIDENCE-040: External Example Packages

- Evidence ID: EVIDENCE-040
- Status: Implemented, Public-Safe
- Source task/group: Group P-CORE-040
- Primary report: [External example packages report](../reports/p-core-040-external-example-packages-v0.md)
- Primary generated artifacts: [External examples](../../examples/README.md)
- Primary docs: [Public artifact specifications](../specs/README.md), [Artifact validator evidence](EVIDENCE-038-artifact-validator-bundle.md)
- Relevant decisions: [DEC-002](../decisions/DEC-002-evidence-bundle-before-claims.md), [DEC-004](../decisions/DEC-004-specification-layer-for-permea-standard.md), [DEC-005](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)
- Validation surface: `python3 scripts/permea_check.py examples/synthetic_reference_example`, `python3 scripts/permea_check.py examples/bbb_peptide_reference_example`, and `python3 scripts/permea_check.py examples/expression_engineering_reference_example`
- Supported public claims: Permea Core provides copyable public reference packages that demonstrate the artifact standard and validator compatibility.
- Unsupported claims: no biological performance, source-rights confirmation, wet-lab validation by Permea, clinical effectiveness, or model-performance claim.
- Limitations: The examples are reference fixtures only; they do not create biological or model evidence.
- Next evidence step: Add future examples only with public-safe fixture values, validator coverage, and explicit non-claims.

### EVIDENCE-042: Quickstart Experience Layer

- Evidence ID: EVIDENCE-042
- Status: Implemented, Public-Safe
- Source task/group: Group P-CORE-042
- Primary report: [Quickstart experience layer report](../reports/p-core-042-quickstart-experience-layer-v0.md)
- Primary docs: [Quickstart](../../QUICKSTART.md), [README](../../README.md), [Review hub](../../REVIEW_HUB.md)
- Primary command: `python3 scripts/permea_demo.py`
- Relevant evidence: [EVIDENCE-038](EVIDENCE-038-artifact-validator-bundle.md), [EVIDENCE-040](EVIDENCE-040-external-example-packages.md)
- Relevant decisions: [DEC-002](../decisions/DEC-002-evidence-bundle-before-claims.md), [DEC-005](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)
- Validation surface: `python3 scripts/permea_demo.py` and `python3 -m pytest tests/test_quickstart_experience.py`
- Supported public claims: Permea Core provides a deterministic first-user command that discovers example packages, runs validation, links evidence and claim-boundary surfaces, and prints next recommended commands.
- Unsupported claims: no dataset download, acquisition execution, redistribution-rights confirmation, biological validation, clinical effectiveness, model performance, or delivery outcome claim.
- Limitations: The quickstart demo validates public example package structure and claim-boundary hygiene; it does not create scientific results.
- Next evidence step: Keep quickstart output aligned with future example package and validator changes.

### EVIDENCE-043: Evidence Navigation Layer

- Evidence ID: EVIDENCE-043
- Status: Implemented, Public-Safe
- Source task/group: Group P-CORE-043
- Primary report: [Evidence map](evidence-map.md)
- Primary docs: [Claim-to-evidence matrix](claim-to-evidence-matrix.md), [Evidence maturity model](evidence-maturity-model.md), [Evidence timeline](evidence-timeline.md)
- Primary command: `python3 scripts/permea_evidence.py`
- Relevant evidence: [EVIDENCE-030](EVIDENCE-030-evidence-surface-layer.md), [EVIDENCE-032](EVIDENCE-032-reproducibility-bundle.md), [EVIDENCE-034](EVIDENCE-034-evaluation-bundle.md), [EVIDENCE-036](EVIDENCE-036-artifact-specification-layer.md), [EVIDENCE-038](EVIDENCE-038-artifact-validator-bundle.md), [EVIDENCE-040](EVIDENCE-040-external-example-packages.md), [EVIDENCE-042](EVIDENCE-042-quickstart-experience-layer.md)
- Relevant decisions: [DEC-002](../decisions/DEC-002-evidence-bundle-before-claims.md), [DEC-005](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)
- Validation surface: `python3 scripts/permea_evidence.py` and `python3 -m pytest tests/test_evidence_navigation.py`
- Supported public claims: Existing public evidence is discoverable, reviewable, auditable, and extensible through a navigation map, claim matrix, maturity model, timeline, and CLI.
- Unsupported claims: no biological efficacy, therapeutic outcome, BBB success, solved-delivery, SOTA performance, experimental validation, or clinical evidence claim.
- Limitations: The navigation layer organizes existing evidence only; it does not add scientific evidence.
- Next evidence step: Add new evidence records, reports, validators, and claim-registry links as evidence matures.
