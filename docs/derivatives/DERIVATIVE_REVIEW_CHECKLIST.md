# Derivative Review Checklist

## 1. Purpose

This checklist is used before approving, listing, publicizing, or releasing a Permea derivative project.

Passing this checklist does not itself create legal, institutional, clinical, validation, or public release approval. Required approvals must be recorded separately.

## 2. Project Scope Checklist

- [ ] Project name is recorded.
- [ ] Project type is identified.
- [ ] Repo URL or proposed repo location is recorded.
- [ ] Maintainer is identified or marked TBD.
- [ ] Scope is specific and bounded.
- [ ] Official, Permea-aligned, or independent fork status is stated.
- [ ] Project status is proposed, incubating, active, archived, or deprecated.
- [ ] Known blockers are listed.

## 3. Claim Hygiene Checklist

- [ ] Claims follow `docs/scientific-governance/CLAIM_REGISTRY.md`.
- [ ] Project-specific claims have project-specific evidence.
- [ ] Benchmark claims state dataset, split, metric, model, artifact, and evidence level.
- [ ] "AlphaFold for Delivery" is used only as ambition or positioning, if used at all.
- [ ] No AlphaFold-level performance, adoption, or standardization is claimed.
- [ ] No clinical efficacy or therapeutic efficacy is claimed.
- [ ] No universal delivery prediction is claimed.
- [ ] No production-grade drug delivery platform status is claimed.
- [ ] Permea-aligned status is not described as Permea validation.

## 4. Dataset / Provenance Checklist

- [ ] Dataset sources are identified or marked unresolved.
- [ ] License, attribution, and redistribution terms are recorded or marked unresolved.
- [ ] Row-level and aggregate artifacts are separated.
- [ ] Derived artifacts are classified.
- [ ] Partner-controlled, private, or institutional data are identified.
- [ ] Dataset redistribution is not claimed unless source/license approval is documented.
- [ ] B3Pred/B3Pdb-style source lineage cautions are applied where relevant.

## 5. Public-Safe Artifact Checklist

- [ ] Artifacts are classified as safe, likely safe after review, hold, or do not publish without explicit permission.
- [ ] Release does not expose restricted row-level datasets.
- [ ] Release does not expose row-level labels, features, predictions, rankings, split manifests, group assignments, leakage tables, or raw upstream mirrors without permission.
- [ ] Public examples use aggregate summaries or public-safe synthetic examples where needed.
- [ ] Public-facing docs do not reveal secrets, private records, or confidential partner information.

## 6. Benchmark / Result Schema Checklist

- [ ] Benchmark task is defined where relevant.
- [ ] Split policy is documented where relevant.
- [ ] Metric definitions are documented where relevant.
- [ ] Model or method scope is documented where relevant.
- [ ] Result artifacts follow `docs/RESULT-ARTIFACT-SCHEMA.md`.
- [ ] Run records follow `docs/RUN-MANIFEST-SCHEMA.md` where needed.
- [ ] Imported and regenerated artifacts are distinguished.

## 7. Reproducibility Checklist

- [ ] Reproducibility level is stated.
- [ ] Code, config, data references, manifests, and limitations are recorded where relevant.
- [ ] Aggregate and row-level reproducibility are distinguished.
- [ ] Missing rerun surfaces are disclosed.
- [ ] Reproducibility is not described as biological validation.

## 8. Contributor / Authorship Checklist

- [ ] Contributors are credited according to `docs/contributors/CONTRIBUTOR_LEVELS.md`.
- [ ] Paper authorship is not promised by contribution alone.
- [ ] Authorship consideration follows `docs/contributors/AUTHORSHIP_POLICY.md`.
- [ ] Reviewer credit follows `docs/community/REVIEWER_CREDIT_POLICY.md`.
- [ ] Institutional or partner credit is approved before public use.
- [ ] Credit disputes or unresolved issues are recorded in public-safe terms.

## 9. Wet-Lab Collaboration Checklist

- [ ] Wet-lab collaboration level is stated if relevant.
- [ ] Protocol, assay, controls, readout, limitations, and evidence level are documented before validation claims.
- [ ] Data ownership, confidentiality, and release permission are recorded or marked unresolved.
- [ ] Partner or institutional approval is recorded where applicable.
- [ ] Wet-lab collaboration interest is not described as wet-lab validation.
- [ ] No in vivo, therapeutic, or clinical claims are made unless documented and approved.

## 10. Release Review Checklist

- [ ] Release type is identified.
- [ ] Required approvers are identified using `docs/release/RELEASE_OWNERSHIP_MATRIX.md`.
- [ ] Release state is draft, internal review, public-safe candidate, hold, approved, released, or withdrawn/corrected.
- [ ] Claim gate is complete or blockers are visible.
- [ ] Dataset/provenance gate is complete or blockers are visible.
- [ ] Public-safe artifact gate is complete or blockers are visible.
- [ ] Reproducibility gate is complete or blockers are visible.
- [ ] Paper alignment gate is complete or marked N/A.
- [ ] Manual approval is recorded where required.

## 11. Branding / Name-Use Checklist

- [ ] Official Permea status is approved before official branding is used.
- [ ] Permea-aligned status is clearly separated from Permea validation.
- [ ] Independent forks use independent naming unless approval exists.
- [ ] Project descriptions do not imply endorsement, validation, or release approval beyond recorded status.
- [ ] Website, README, paper, and release names are aligned.

## 12. No-Go Conditions

Do not approve or publicize a derivative project if:

- source/license/redistribution status is unresolved for included row-level artifacts
- restricted row-level artifacts are included without explicit permission
- claims exceed evidence level
- dry-lab evidence is described as wet-lab validation
- collaboration interest is described as validation
- clinical efficacy is implied
- universal delivery prediction is implied
- AlphaFold-level performance, adoption, or standardization is implied
- branding suggests official Permea approval without recorded approval
- required manual approval is missing
- sensitive, private, or confidential information is exposed

## 13. Approval Status Block Template

Use this template in derivative review records:

```text
Project:
Type:
Repo:
Status:
Maintainer:
Branding status:
Evidence level:
Dataset policy status:
Public-safe artifact status:
Release status:
Paper/preprint linkage:

Claim review:
Dataset/provenance review:
Public-safe artifact review:
Benchmark/result review:
Reproducibility review:
Contributor/authorship review:
Wet-lab/partner review:
Manual approval:

Decision:
Blockers:
Next action:
```

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Derivative projects must not inherit claim authority automatically. Permea-aligned does not mean Permea-validated. Wet-lab collaboration interest does not equal wet-lab validation.
