# Release Ownership Matrix

## 1. Purpose

This matrix defines initial release ownership expectations for Permea Core and Permea-aligned projects.

The goal is to make release approval paths explicit while keeping exact person-by-person roster decisions deferred until governance assigns them.

## 2. Release Ownership Principle

Each release type should have named review roles before public release.

Higher-risk releases require more than routine maintainer review. Dataset, artifact, claim, paper, wet-lab, and derivative project releases require role-specific review and may require founder/manual approval.

Approval means the scoped release passed the recorded checks. It does not create legal, clinical, validation, authorship, or dataset redistribution conclusions.

## 3. Release Type vs Approver Matrix

| Release Type | Maintainer | Claim Reviewer | Dataset / Provenance Reviewer | Reproducibility Reviewer | Paper / Source-to-Claim Reviewer | Release Approver | Founder / Manual Approver |
| --- | --- | --- | --- | --- | --- | --- | --- |
| docs-only | required | required if claims change | required if data/release wording changes | optional | required if paper/public wording changes | optional | required if public-sensitive |
| code-only | required | required if claims change | required if data handling changes | required if reproducibility is claimed | optional | optional | required if high-impact |
| benchmark/schema | required | required | optional unless data scope changes | required | optional | optional | required if public benchmark standard changes are high-impact |
| result artifact | required | required | required if row-level or source-derived artifacts are involved | required | required if paper-supporting | required | required if public-sensitive or high-impact |
| dataset | required | required | required | required if reproducibility is claimed | required if paper-supporting | required | required |
| paper-support | required | required | required if data or artifacts are discussed | required if rerun claims are made | required | required | required for public preprint/package decisions |
| preprint/publication | required | required | required | required where reproducibility is claimed | required | required | required |
| derivative project | required | required | required if data/artifacts are involved | required if benchmark or result claims are involved | required if paper/preprint-linked | required | required for official branding or high-impact status |
| wet-lab collaboration | required | required | required | optional unless computational rerun claims are made | required if paper/preprint-linked | required | required |

If a release spans multiple types, use the strictest applicable row.

## 4. Role Definitions

### Maintainer

Verifies repo scope, file scope, review completeness, merge mechanics, and recordkeeping.

### Claim Reviewer

Checks `docs/scientific-governance/CLAIM_REGISTRY.md` and `docs/EVIDENCE-LADDER.md`.

### Dataset / Provenance Reviewer

Checks source, license, attribution, redistribution status, row-level artifact posture, and partner or institutional constraints.

### Reproducibility Reviewer

Checks run surfaces, environment capture, benchmark contract alignment, run manifest status, result artifacts, and reproducibility wording.

### Paper / Source-to-Claim Reviewer

Checks manuscript, supplement, README, website, release notes, citation support, source-to-claim mapping, and public-readiness wording.

### Release Approver

Confirms required gates have passed or blockers are recorded before release.

### Founder / Manual Approver

Handles high-impact release, dataset, public preprint, authorship, partner, official branding, wet-lab collaboration, and unresolved governance decisions.

## 5. Required Approvers by Release Type

Docs-only releases may be approved by a maintainer when they do not change claims, data posture, release state, paper status, or public-facing scientific interpretation.

Code-only releases require maintainer review and reproducibility review when the code supports benchmark or rerun claims.

Benchmark/schema releases require maintainer, claim, and reproducibility review.

Result artifact releases require maintainer, claim, reproducibility, and dataset/provenance review when artifacts are source-derived or row-level.

Dataset releases require maintainer, claim, dataset/provenance, public-safe artifact, release, and founder/manual approval.

Paper-support and preprint/publication releases require paper/source-to-claim, claim, dataset/provenance, release, and founder/manual approval.

Derivative project releases require derivative review, release review, and founder/manual approval when official branding, public release, paper linkage, dataset release, or partner-sensitive status is involved.

Wet-lab collaboration releases require claim, dataset/provenance, partner-sensitive review, release approval, and founder/manual approval before public claims.

## 6. Escalation Rules

Escalate when:

- reviewers disagree on release readiness
- source/license/redistribution status is unresolved
- row-level artifacts may be exposed
- claims imply stronger evidence than documented
- paper/preprint readiness is unclear
- official Permea branding is requested
- wet-lab collaboration, partner, or institutional data are involved
- authorship, reviewer credit, or contributor credit is disputed
- sensitive, private, or confidential information may be exposed

Escalation should route to maintainers first, then founder/manual approval for high-impact unresolved items.

## 7. Recordkeeping Requirements

Release ownership records should include:

- release type
- release state
- repo and paths
- included files
- excluded files
- required reviewers
- completed reviews
- blocking findings
- unresolved caveats
- manual approval status
- decision
- commit, tag, pull request, issue, or report reference

Records must be public-safe and must not expose secrets, private data, restricted row-level artifacts, or confidential partner information.

## 8. Deferred Exact Roster Note

This matrix defines roles, not a final people roster.

Exact maintainer, reviewer, release approver, founder/manual approver, legal/manual, partner, and institutional approval assignments remain deferred until governance records them.

Until the roster is explicit, high-impact or ambiguous releases should remain Hold or Internal Review.

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Derivative projects must not inherit claim authority automatically. Permea-aligned does not mean Permea-validated. Wet-lab collaboration interest does not equal wet-lab validation.
