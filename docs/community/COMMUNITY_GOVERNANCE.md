# Community Governance

## 1. Purpose

This document defines Permea Core's initial community governance model.

The goal is to make project decisions legible while preserving open scientific collaboration, conservative claim discipline, dataset/release safety, and clear escalation paths.

This is a project operating document. It does not make legal conclusions about employment, institutional policy, IP ownership, clinical claims, or authorship disputes.

## 2. Governance Principles

Permea governance should be:

- open-source-first
- benchmark-first
- evidence-bounded
- reproducibility-aware
- public-safe by default
- explicit about dataset and release limits
- respectful of contributor credit without promising authorship automatically
- conservative when scientific claims, data rights, or public release status are uncertain

## 3. Governance Scope

Governance applies to:

- project contribution workflow
- reviewer and maintainer responsibilities
- claim-changing changes
- dataset/provenance-sensitive changes
- benchmark and result schema changes
- paper, preprint, and release alignment
- wet-lab collaboration claim handling
- derivative project approval boundaries
- public artifact release decisions

Governance does not replace legal, institutional, clinical, journal, or partner review where those are required.

## 4. Role Taxonomy

### User / Community Member

Uses the project, reads documentation, opens questions, or follows public discussions.

### Contributor

Submits issues, documentation, code, benchmark proposals, reproducibility work, dataset/provenance notes, claim review, or scientific feedback.

Contributor status does not automatically grant maintainer rights, release approval rights, or paper authorship.

### Trusted Contributor

Has a record of useful, careful contributions and may be asked to review scoped changes.

Trusted contributor status is descriptive and does not automatically grant merge authority.

### Reviewer

Reviews a defined surface such as claims, scientific framing, reproducibility, benchmark contracts, dataset/provenance status, source-to-claim alignment, or wet-lab protocol framing.

Review does not equal peer review, external validation, wet-lab validation, or clinical endorsement.

### Maintainer

Has explicit stewardship responsibility for repo health, triage, review coordination, merge decisions, and policy enforcement within assigned scope.

Maintainer rights are assigned explicitly and are not automatic from contribution volume, affiliation, paper authorship, or collaboration status.

### Release Approver

Reviews whether a proposed public release passed the required claim, dataset, artifact, reproducibility, paper alignment, and public-safe gates.

Release approver status may be scoped by release type.

### Founder / Manual Approver

Handles high-impact decisions where exact policy or roster is still evolving, including major public release, dataset, authorship, partner, preprint, and strategic decisions.

Founder/manual approval is a project decision record, not a legal conclusion.

## 5. Decision Types

### Routine Docs / Code

Low-risk documentation or code changes that do not alter public claims, data release state, benchmark semantics, or paper/preprint readiness.

### Benchmark / Schema Changes

Changes to benchmark contracts, run manifests, result artifact schemas, split policy, metric definitions, or result interpretation.

### Dataset / Provenance Changes

Changes that add, describe, transform, release, or reclassify source datasets, processed datasets, row-level artifacts, partner data, or provenance records.

### Claim-Changing Changes

Changes that alter README, website, paper, release-note, benchmark, or outreach claims.

### Paper / Preprint Changes

Changes to manuscripts, supplements, source-to-claim reviews, preprint status, paper support packages, or public-readiness statements.

### Release / Publication Changes

Changes that publish or approve docs, code, artifacts, datasets, paper packages, preprints, tags, or derivative outputs.

### Wet-Lab Collaboration Claims

Changes that reference assay design, experimental data, wet-lab partner status, validation, biological performance, in vivo work, or clinical implications.

### Derivative Project Approvals

Decisions about downstream projects using Permea Core names, standards, artifacts, claims, or release language.

## 6. Decision Rights by Role

Community members and contributors may propose changes and raise concerns.

Trusted contributors may review scoped changes when asked.

Reviewers may recommend approval, request changes, or mark blockers within their review area.

Maintainers may merge routine changes and coordinate review for higher-risk changes.

Release approvers may approve scoped public release only after required gates pass.

Founder/manual approvers handle unresolved high-impact decisions, including dataset release posture, public preprint readiness, major partner-sensitive claims, and authorship approval where required.

No role may:

- publish restricted row-level artifacts without documented permission and review
- claim dataset redistribution permission without source/license approval
- claim completed wet-lab validation unless documented
- claim clinical efficacy
- claim AlphaFold-level performance, adoption, or standardization
- make legal conclusions about employment, IP ownership, institutional policy, or authorship disputes

## 7. Escalation Path

Escalate when a change touches:

- high-risk scientific claims
- dataset/source/license uncertainty
- row-level artifacts
- public release readiness
- paper/preprint readiness
- wet-lab validation language
- partner or institution-sensitive information
- authorship or contributor-credit conflict
- security, privacy, or sensitive data exposure

Default escalation path:

1. Request clarification in the issue or pull request.
2. Assign the relevant reviewer type.
3. Mark blockers explicitly.
4. Route unresolved items to a maintainer.
5. Route high-impact unresolved items to founder/manual approval.
6. Record the decision and remaining caveats.

Avoid posting sensitive details in public threads.

## 8. Conflict / Dispute Placeholder

Conflicts should be handled through documented, respectful, private-first escalation when sensitive information is involved.

Until a more formal dispute process exists, maintainers and founder/manual approvers should coordinate resolution without making public accusations or exposing private correspondence.

This governance document does not decide legal IP ownership, employment status, university policy, or authorship disputes.

## 9. Recordkeeping Requirements

Nontrivial decisions should record:

- decision type
- affected repo and paths
- reviewers involved
- claim review status
- dataset/provenance review status
- reproducibility review status
- benchmark/result review status
- paper alignment status
- public-safe artifact status
- release state, if relevant
- manual approval status, if relevant
- unresolved blockers
- final decision
- commit, pull request, issue, or release reference

Records should be public-safe and should not expose secrets, private data, restricted row-level data, or confidential partner information.

## 10. What Governance Does Not Decide

Permea community governance does not decide:

- legal IP ownership
- employment status
- institutional authorship rules
- university or partner policy
- material transfer terms
- clinical or medical claims
- therapeutic efficacy
- regulatory status

Where these topics matter, the project should pause public claims or releases until the appropriate manual, legal, institutional, or partner review is complete.

## 11. Link Map to Other Policy Docs

Core governance references:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `SUPPORT.md`
- `docs/contributors/CONTRIBUTOR_LEVELS.md`
- `docs/contributors/AUTHORSHIP_POLICY.md`
- `docs/contributors/DRY_LAB_CONTRIBUTION_POLICY.md`
- `docs/contributors/WET_LAB_COLLABORATION_POLICY.md`
- `docs/scientific-governance/CLAIM_REGISTRY.md`
- `docs/scientific-governance/DATASET_POLICY.md`
- `docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md`
- `docs/scientific-governance/REPRODUCIBILITY_GUIDE.md`
- `docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md`
- `docs/release/RELEASE_REVIEW_PROCESS.md`
- `docs/release/PUBLIC_RELEASE_CHECKLIST.md`
- `docs/EVIDENCE-LADDER.md`
- `docs/BENCHMARK-CONTRACT.md`
- `docs/RESULT-ARTIFACT-SCHEMA.md`
- `docs/RUN-MANIFEST-SCHEMA.md`

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Review does not equal peer review. Reviewer input does not equal external validation. Wet-lab protocol discussion does not equal wet-lab validation.
