# Public Claim Registry

This registry maps public claim types to evidence dependencies, non-claims, wording guidance, limitations, and review rules.

## Supported Public Claims

Permea Core public materials may state that the repository currently has:

- an implemented generated evidence surface
- an implemented reproducibility bundle for public generated artifacts
- an implemented template/reference evaluation bundle
- public artifact specifications and lightweight schemas for current artifact families
- an artifact validator command for checking current public examples against structural, non-claim, claim-boundary, and evidence-linkage expectations
- external reference example packages that demonstrate how to use the artifact standard
- a deterministic quickstart demo that discovers example packages, runs validation, links evidence surfaces, and prints next commands
- public decision records for major program choices
- public claim-boundary and documentation memory surfaces

## Unsupported Public Claims

Permea Core public materials must not claim:

- no dataset download
- no acquisition execution
- no redistribution-rights confirmation
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA status claim
- no solved delivery claim
- no broad delivery prediction claim
- no production readiness for biological or clinical use

## Evidence Dependencies

| Claim type | Required evidence dependency |
| --- | --- |
| Generated evidence navigation exists | [EVIDENCE-030](../evidence/EVIDENCE-030-evidence-surface-layer.md) |
| Public reproduction path exists | [EVIDENCE-032](../evidence/EVIDENCE-032-reproducibility-bundle.md) |
| Evaluation transfer pattern exists | [EVIDENCE-034](../evidence/EVIDENCE-034-evaluation-bundle.md) |
| Artifact standards exist | [EVIDENCE-036](../evidence/EVIDENCE-036-artifact-specification-layer.md) |
| Artifact examples can be checked against Permea standards | [EVIDENCE-038](../evidence/EVIDENCE-038-artifact-validator-bundle.md) |
| External example packages demonstrate the standard | [EVIDENCE-040](../evidence/EVIDENCE-040-external-example-packages.md) |
| Quickstart command provides a first-user validation path | [EVIDENCE-042](../evidence/EVIDENCE-042-quickstart-experience-layer.md) |
| Claim-boundary discipline exists | [DEC-005](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md) and [Claim Boundary](../CLAIM_BOUNDARY.md) |

## Required Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Claim-Boundary Wording Guidance

Prefer:

- public evidence framework
- evidence-centric research program
- generated public artifact surface
- reproducibility bundle
- evaluation template/reference workflow
- artifact specification layer
- first-user quickstart demo
- project memory layer
- decision layer

Avoid wording that implies biological validation, clinical readiness, model superiority, or completed source acquisition.

## Known Limitations

- Current evidence is documentation, metadata, generated artifacts, and local validation.
- Validator-assisted review checks structure and claim-boundary hygiene for public examples; it does not establish scientific performance.
- Current evidence does not include dataset download, acquisition execution, model scoring, wet-lab results, clinical results, or redistribution-rights confirmation.
- Decision records explain why directions were chosen; they are not evidence of scientific performance.

## Review / Update Rule

If a public claim is added or changed, update this registry or link the claim to an existing evidence record. If the claim cannot be tied to evidence, narrow or remove it.
