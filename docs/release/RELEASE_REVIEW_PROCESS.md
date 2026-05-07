# Release Review Process

## 1. Purpose

This document defines Permea Core's initial release review process.

The process exists to prevent premature public release, unsupported scientific claims, unsafe dataset exposure, and inconsistent paper/README/release wording.

## 2. Release Types

### Docs-Only

Documentation changes that do not alter claims, data, code behavior, or public artifact status.

### Code-Only

Code changes that do not publish new benchmark results or datasets.

### Benchmark-Schema Release

Changes to benchmark contracts, run manifests, result schemas, task definitions, or reproducibility requirements.

### Result-Artifact Release

Release of metrics, figures, summaries, predictions, rankings, manifests, or benchmark outputs.

### Paper-Support Release

Release of manuscripts, supplements, source-to-claim reviews, public-safe artifact manifests, or paper-specific reports.

### Dataset Release

Release of source datasets, processed datasets, derived features, labels, row-level predictions, split manifests, or dataset cards.

### Preprint Release

Release or submission of a public preprint package.

### Derivative Project Release

Release of downstream repositories or packages derived from Permea Core standards, code, or artifacts.

## 3. Release Review Roles

Release review may involve:

- maintainer: verifies repo scope, file scope, and merge/release mechanics
- claim reviewer: checks claim registry and evidence ladder alignment
- dataset/provenance reviewer: checks source, license, lineage, and release boundaries
- reproducibility reviewer: checks benchmark contract, run manifest, result artifacts, and rerun claims
- paper/source-to-claim reviewer: checks manuscript, supplement, README, and citation alignment
- founder/manual approver: resolves high-impact release, dataset, authorship, partner, or public preprint decisions

One person may hold multiple roles, but the decision record should state which checks were performed.

## 4. Release Gates

### Claim Gate

The release must pass `docs/scientific-governance/CLAIM_REGISTRY.md`.

Claims must not imply evidence stronger than what is documented.

### Dataset Gate

The release must pass `docs/scientific-governance/DATASET_POLICY.md`.

Source, license, attribution, redistribution, row-level status, and derived artifact status must be known or explicitly unresolved.

### Artifact Gate

The release must pass `docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md`.

Artifacts must be classified as safe, likely safe after review, hold, or do not publish without explicit permission.

### Reproducibility Gate

The release must pass `docs/scientific-governance/REPRODUCIBILITY_GUIDE.md`.

Reproducibility claims require code/config/data references, run manifests, result artifacts, and limitations.

### Paper Alignment Gate

The release must pass `docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md`.

README, manuscript, supplement, source-to-claim review, artifact manifest, and release notes must not contradict one another.

### Public-Safe Artifact Gate

The release must avoid exposing secrets, private data, restricted row-level datasets, row-level predictions, rankings, split manifests, group assignments, leakage tables, or raw upstream mirrors unless explicit permission and review are documented.

## 5. Row-Level Artifact Review Rule

Row-level artifacts require explicit review before public release.

This includes:

- row-level sequence records
- row-level labels
- row-level feature tables
- row-level predictions
- ranking tables
- split manifests
- group assignments
- sequence-pair leakage tables
- raw upstream dataset mirrors

If release permission is unclear, hold the artifact.

## 6. Dataset / License Unresolved Rule

If dataset source, license, attribution, redistribution permission, or derived artifact release status is unresolved, do not publish row-level data.

Permitted alternatives may include:

- code-only release
- docs-only release
- aggregate metric release after review
- aggregate figure release after review
- path-level artifact inventory
- public-safe manifest that explicitly marks blocked artifacts

This process does not make final legal conclusions.

## 7. Emergency Correction / Rollback Process

If a release exposes restricted data, secrets, or unsupported claims:

1. Stop further distribution where feasible.
2. Notify maintainers privately if sensitive details are involved.
3. Identify affected files, releases, docs, and claims.
4. Remove or restrict exposed content where appropriate.
5. Publish a public-safe correction note if needed.
6. Update manifests, release notes, and alignment docs.
7. Record the issue and prevention step.

Avoid posting sensitive details in public issue threads.

## 8. Release Decision States

Allowed release states:

- Draft: work in progress, not ready for broad review.
- Internal Review: suitable for internal or friendly review only.
- Public-Safe Candidate: candidate package with release risks reviewed but not approved.
- Hold: blocked by claim, dataset, artifact, reproducibility, legal/manual, or alignment issue.
- Approved: passed required gates and approval.
- Released: public release completed.
- Withdrawn/Corrected: release was corrected or withdrawn after issue discovery.

## 9. Recordkeeping Requirements

Each nontrivial release should record:

- release type
- release state
- files included
- files excluded
- claim review status
- dataset/provenance review status
- artifact review status
- reproducibility review status
- paper alignment status
- manual approval status
- known blockers
- release decision
- commit or tag reference

## 10. Required Links to Manifests / Reports

Release records should link to relevant:

- benchmark contract
- run manifest
- result artifact manifest
- public-safe artifact manifest
- dataset/source review
- source-to-claim review
- paper alignment review
- release checklist
- correction note, if applicable

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Public release must not include row-level restricted artifacts unless explicit permission and review are documented.
