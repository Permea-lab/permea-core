# Public Release Checklist

## 1. Purpose

This checklist defines Permea Core's initial public release checklist.

Use it before public releases of docs, code, schemas, benchmark artifacts, paper-support packages, datasets, preprints, or derivative projects.

Passing this checklist does not itself create legal, clinical, biological validation, or public preprint approval. Approval must be recorded separately where required.

## 2. General Public Release Checklist

- [ ] Release type is identified.
- [ ] Release state is identified.
- [ ] Files included are listed.
- [ ] Files excluded are listed.
- [ ] Reviewer roles are assigned where needed.
- [ ] Known blockers are documented.
- [ ] Public-facing status is accurate.
- [ ] Release notes match actual release contents.

## 3. Claim Hygiene Checklist

- [ ] Claims follow `docs/scientific-governance/CLAIM_REGISTRY.md`.
- [ ] Ambition is separated from achieved evidence.
- [ ] Benchmark claims state dataset, split, metric, model, artifact, and evidence level.
- [ ] Computational evidence is not described as biological validation.
- [ ] Wet-lab validation is not claimed unless documented.
- [ ] Clinical efficacy is not claimed.
- [ ] Universal delivery prediction is not claimed.
- [ ] Production-grade drug delivery platform status is not claimed.
- [ ] "AlphaFold for Delivery" is used only as ambition or positioning, if used at all.

## 4. Dataset / Provenance Checklist

- [ ] Dataset source is documented.
- [ ] Source citation or attribution is documented where available.
- [ ] Source version or access date is documented where available.
- [ ] License or terms are documented where available.
- [ ] Redistribution status is documented.
- [ ] Derived artifact status is documented.
- [ ] Unknown source/license items are marked unresolved.
- [ ] No final legal conclusions are made without appropriate review.

## 5. Row-Level Artifact Exclusion Checklist

Confirm the release does not include restricted or unresolved:

- [ ] row-level sequence datasets
- [ ] row-level labels
- [ ] row-level feature tables
- [ ] row-level predictions
- [ ] ranking tables
- [ ] split manifests
- [ ] group assignments
- [ ] sequence-pair leakage CSVs
- [ ] raw upstream dataset mirrors
- [ ] private or partner-controlled records

If any item is included, explicit permission and review must be documented.

## 6. Benchmark / Result Artifact Checklist

- [ ] Benchmark contract is identified.
- [ ] Dataset reference is identified.
- [ ] Split protocol is identified.
- [ ] Model or baseline is identified.
- [ ] Metrics are identified.
- [ ] Result artifacts are listed.
- [ ] Run manifest is present or limitation is documented.
- [ ] Aggregate and row-level artifacts are separated.
- [ ] Exploratory outputs are not presented as contract-grade results.

## 7. Reproducibility Checklist

- [ ] Code revision is recorded.
- [ ] Config or command is recorded.
- [ ] Environment is described.
- [ ] Data access constraints are described.
- [ ] Reproducibility level is stated.
- [ ] Aggregate vs row-level reproducibility is distinguished.
- [ ] Rerun limits are documented.
- [ ] Reproducibility is not described as biological validation.

## 8. Paper / Preprint Alignment Checklist

- [ ] Manuscript title matches claim scope.
- [ ] Abstract matches evidence level.
- [ ] README claims match manuscript claims.
- [ ] Dataset scope and limitations match across materials.
- [ ] Data/code availability wording is consistent.
- [ ] Supplement does not expose blocked artifacts.
- [ ] Source-to-claim review is complete or unresolved items are visible.
- [ ] Public preprint status is accurately marked.
- [ ] Hold status is not contradicted by any public-facing material.

## 9. README / Website / Deck Alignment Checklist

- [ ] README does not overstate paper readiness.
- [ ] Website does not overstate evidence level.
- [ ] Decks do not imply validation beyond documented evidence.
- [ ] Release notes do not broaden benchmark claims.
- [ ] Screenshots or figures do not reveal restricted row-level artifacts.

## 10. Security / Privacy / Secrets Checklist

- [ ] No secrets, credentials, API keys, tokens, or private keys are included.
- [ ] No private data are included.
- [ ] No confidential partner data are included.
- [ ] No nonpublic source terms are exposed.
- [ ] Sensitive findings are reported through private channels.
- [ ] Security review is complete where relevant.

## 11. Contributor / Authorship Acknowledgement Checklist

- [ ] Contributors are acknowledged according to current repo policy.
- [ ] Paper authorship is not promised by contribution alone.
- [ ] Authorship decisions are deferred to formal policy/manual review where needed.
- [ ] Wet-lab partner contributions are reviewed for ownership, confidentiality, and credit.
- [ ] Reviewer contributions are recorded where appropriate.

## 12. Final Manual Approval Checklist

- [ ] Maintainer approval recorded.
- [ ] Claim review approval recorded.
- [ ] Dataset/provenance review approval recorded where needed.
- [ ] Reproducibility review approval recorded where needed.
- [ ] Paper/source-to-claim approval recorded where needed.
- [ ] Founder/manual approval recorded where required.
- [ ] Release decision state recorded.

## 13. No-Go Conditions

Do not release publicly if:

- public status is still Hold
- source/license/redistribution status is unresolved for included row-level artifacts
- row-level restricted artifacts are included without explicit permission
- secrets or private data are present
- claims exceed evidence level
- dry-lab evidence is described as wet-lab validation
- clinical efficacy is implied
- universal delivery prediction is implied
- AlphaFold-level performance, adoption, or standardization is implied
- README, manuscript, website, supplement, or release notes contradict one another
- required manual approval is missing

## 14. Final Status Block Template

Use this template in release review records:

```text
Release type:
Release state:
Files included:
Files excluded:
Claim review:
Dataset/provenance review:
Artifact release review:
Reproducibility review:
Paper/preprint alignment review:
Manual approval:
No-go conditions present:
Final decision:
Known limitations:
Next required action:
```

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Public release must not include row-level restricted artifacts unless explicit permission and review are documented.
