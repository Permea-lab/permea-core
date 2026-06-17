# Evidence Maturity Model

This model defines evidence maturity levels for Permea Core. It separates documented workflows and reproducible computational artifacts from independent, external, experimental, and clinical evidence.

## Levels

| Level | Name | Definition |
| --- | --- | --- |
| Level 0 | No evidence | No public artifact, report, validator, or claim-boundary record exists. |
| Level 1 | Documented workflow | Public documentation describes a workflow, claim boundary, or artifact path. |
| Level 2 | Reproducible computational evidence | Public artifacts can be generated, validated, or reproduced locally without private assets. |
| Level 3 | Independent reproduction | An independent reviewer or external group has reproduced the public computational workflow and recorded the result. |
| Level 4 | External validation | A public external validation record exists beyond repository-maintained examples. |
| Level 5 | Experimental validation | Experimental evidence exists and is linked to public claim boundaries. |
| Level 6 | Clinical evidence | Clinical evidence exists and is linked to public claim boundaries. |

## Current Asset Mapping

| Asset | Current level | Rationale | Limitation |
| --- | --- | --- | --- |
| Evidence surface and generated artifact navigation | Level 2 | Generated public surfaces exist and can be regenerated locally. | Navigation is not scientific evidence. |
| Reproducibility bundle | Level 2 | Public artifact surfaces can be reproduced and validated locally. | Covers metadata and generated artifacts only. |
| Evaluation bundle | Level 2 | Template/reference evaluation packet can be generated and validated locally. | Does not establish biological, experimental, or performance results. |
| Artifact specifications | Level 2 | Specs and schemas exist and can be inspected with `python3 scripts/permea_specs.py`. | Lightweight schemas may need stricter future enforcement. |
| Artifact validator bundle | Level 2 | Current public artifacts can be checked with `python3 scripts/permea_check.py`. | Validator checks structure and claim-boundary hygiene. |
| External example packages | Level 2 | Copyable examples validate locally as public-safe reference packages. | Examples are fixtures, not outcome evidence. |
| Quickstart experience | Level 2 | First-user command validates examples and routes to evidence surfaces. | Demo does not create new evidence. |
| Evidence navigation layer | Level 2 | Evidence map, matrix, maturity model, timeline, and CLI summarize current evidence deterministically. | It organizes existing evidence only. |
| Independent reproduction | Level 0 | No independent reproduction record is present in this repository. | Future evidence should add dated reproduction reports. |
| External validation | Level 0 | No external validation record is present in this repository. | Future evidence should link external validation records if available. |
| Experimental validation | Level 0 | No experimental validation claim is made by this repository. | This remains unsupported until public evidence exists. |
| Clinical evidence | Level 0 | No clinical evidence claim is made by this repository. | This is outside current repository evidence. |

## Current Public Position

Permea Core currently sits at Level 2 for repository-maintained public artifact workflows. Level 3 and above are not yet demonstrated in this repository.

## Future Evidence Accumulation

- Level 3 evidence should accumulate as independent reproduction reports.
- Level 4 evidence should accumulate as external validation records.
- Level 5 evidence should accumulate only with explicit experimental evidence and updated claim boundaries.
- Level 6 evidence should accumulate only with clinical evidence and appropriate governance.
