# Claim-To-Evidence Matrix

This matrix maps public claim categories to current evidence, status, and limitations. It is a claim-discipline surface, not a scientific result.

## Status Definitions

- Supported by Computational Evidence: current public artifacts, validators, or reproducible metadata workflows support the claim category.
- Partial Evidence: current artifacts support part of the claim category, but important review or extension work remains.
- Not Yet Demonstrated: the repository has not demonstrated the claim category.
- Out of Scope: the claim category should not be made from this repository.

## Matrix

| Claim | Evidence | Status | Limitations |
| --- | --- | --- | --- |
| Permea Core provides benchmark-first infrastructure for public artifact review. | [EVIDENCE-036](EVIDENCE-036-artifact-specification-layer.md), [EVIDENCE-038](EVIDENCE-038-artifact-validator-bundle.md) | Supported by Computational Evidence | Supports artifact structure and local checks; does not establish biological results. |
| Sequence-derived signal can be packaged for review using Permea-style artifacts. | [EVIDENCE-040](EVIDENCE-040-external-example-packages.md), public example packages | Partial Evidence | Current examples are reference fixtures; they do not establish biological effect or model superiority. |
| Candidate prioritization before wet-lab can be represented as a bounded public workflow. | [EVIDENCE-034](EVIDENCE-034-evaluation-bundle.md), [EVIDENCE-040](EVIDENCE-040-external-example-packages.md) | Partial Evidence | Workflow pattern exists; candidate outcomes are not validated by this repository. |
| Public artifact surfaces can be reproduced locally. | [EVIDENCE-032](EVIDENCE-032-reproducibility-bundle.md) | Supported by Computational Evidence | Reproduction covers public metadata and generated artifacts only. |
| Evaluation workflow is available as a transfer pattern. | [EVIDENCE-034](EVIDENCE-034-evaluation-bundle.md) | Supported by Computational Evidence | The packet is a template/reference workflow, not an experimental or performance result. |
| Specification compliance can be inspected with local validators. | [EVIDENCE-036](EVIDENCE-036-artifact-specification-layer.md), [EVIDENCE-038](EVIDENCE-038-artifact-validator-bundle.md) | Supported by Computational Evidence | Validator checks current public artifact expectations and may need extension as specs mature. |
| First-user quickstart path exists. | [EVIDENCE-042](EVIDENCE-042-quickstart-experience-layer.md) | Supported by Computational Evidence | Quickstart validates public examples and routes users to evidence surfaces; it does not create evidence. |
| Evidence navigation is discoverable and auditable. | [Evidence map](evidence-map.md), [evidence maturity model](evidence-maturity-model.md), `python3 scripts/permea_evidence.py` | Supported by Computational Evidence | Navigation summarizes existing evidence; it does not add scientific evidence. |
| Independent reproduction has occurred. | Current public docs and generated artifacts | Not Yet Demonstrated | No independent external reproduction record is present in this repository. |
| External validation has occurred. | Current public docs and generated artifacts | Not Yet Demonstrated | No external validation record is present in this repository. |
| Experimental validation has occurred. | Claim registry and public non-claims | Out of Scope | This repository does not claim experimental validation. |
| Therapeutic or clinical outcomes are demonstrated. | Claim registry and public non-claims | Out of Scope | This repository does not claim therapeutic outcomes or clinical evidence. |

## Unsupported Claims To Keep Explicit

- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
