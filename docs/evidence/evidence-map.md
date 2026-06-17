# Evidence Navigation Map

This map is the reviewer-facing inventory for Permea Core evidence assets. It helps a new researcher, reviewer, collaborator, investor, or partner find what evidence exists, what it supports, and where future evidence should accumulate.

This map does not create new scientific evidence.

## Evidence Inventory

| Evidence ID | Evidence title | Related reports | Related validators | Related specifications | Related claims | Current evidence status |
| --- | --- | --- | --- | --- | --- | --- |
| EVIDENCE-030 | Evidence Surface Layer | [Generated evidence surface](../examples/generated/README.md) | `python3 scripts/generate_evidence_surface.py` | [Artifact specs](../specs/README.md) | Generated evidence navigation exists | Implemented, Public-Safe |
| EVIDENCE-032 | Reproducibility Bundle | [Reproducibility report](../examples/generated/REPRODUCIBILITY_REPORT.md) | `python3 scripts/permea_reproduce.py`, `python3 scripts/permea_validate.py` | [Run manifest spec](../specs/RUN_MANIFEST_SPEC.md) | Public reproduction path exists | Implemented, Public-Safe |
| EVIDENCE-034 | Evaluation Bundle | [Evaluation packet](../examples/generated/EVALUATION_PACKET.md) | `python3 scripts/permea_evaluate.py`, `python3 scripts/permea_validate.py` | [Output package spec](../specs/SPEC_OUTPUT_PACKAGE.md) | Evaluation transfer pattern exists | Implemented, Public-Safe |
| EVIDENCE-036 | Artifact Specification Layer | [Artifact specification report](../reports/p-core-036-artifact-specification-layer.md) | `python3 scripts/permea_specs.py` | [Public artifact specs](../specs/README.md), [schemas](../../schemas/) | Artifact standards exist | Implemented, Public-Safe |
| EVIDENCE-038 | Artifact Validator Bundle | [Artifact validator report](../reports/p-core-038-artifact-validator-bundle-v0.md) | `python3 scripts/permea_check.py` | [Public artifact specs](../specs/README.md) | Artifact examples can be checked against Permea standards | Implemented, Public-Safe |
| EVIDENCE-040 | External Example Packages | [External examples report](../reports/p-core-040-external-example-packages-v0.md) | `python3 scripts/permea_check.py examples/synthetic_reference_example` | [Public artifact specs](../specs/README.md) | External examples demonstrate the standard | Implemented, Public-Safe |
| EVIDENCE-042 | Quickstart Experience Layer | [Quickstart experience report](../reports/p-core-042-quickstart-experience-layer-v0.md) | `python3 scripts/permea_demo.py` | [Public artifact specs](../specs/README.md) | First-user validation path exists | Implemented, Public-Safe |
| EVIDENCE-043 | Evidence Navigation Layer | [Evidence map](evidence-map.md), [claim-to-evidence matrix](claim-to-evidence-matrix.md), [maturity model](evidence-maturity-model.md), [timeline](evidence-timeline.md) | `python3 scripts/permea_evidence.py` | [Evidence card spec](../specs/EVIDENCE_CARD_SPEC.md), [claim registry](../claims/claim-registry.md) | Evidence is discoverable, auditable, and extensible | Implemented, Public-Safe |

## Fast Review Path

1. Start with this evidence map.
2. Open the [claim-to-evidence matrix](claim-to-evidence-matrix.md).
3. Open the [evidence maturity model](evidence-maturity-model.md).
4. Open the [evidence timeline](evidence-timeline.md).
5. Run `python3 scripts/permea_evidence.py`.
6. Use the [claim registry](../claims/claim-registry.md) to check supported and unsupported public claims.

## Where Future Evidence Should Accumulate

- New evidence records should be added under `docs/evidence/`.
- New public reports should be added under `docs/reports/`.
- New generated evidence surfaces should remain under `docs/examples/generated/`.
- Claim changes should update [claim registry](../claims/claim-registry.md) and link to an evidence record.
- New validators should be reachable from this map, the review hub, and the relevant evidence record.

## Explicit Non-Claims

- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
