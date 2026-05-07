# Archive and Deprecation Policy

## 1. Purpose

This document defines Permea Core's initial archive, deprecation, correction, and withdrawal policy.

The goal is to preserve useful scientific and technical history while preventing stale artifacts, unsafe datasets, unsupported claims, or deprecated projects from being mistaken for current validated work.

## 2. Archive Principles

Archives should:

- preserve what was released
- record release state and limitations
- keep citations interpretable
- distinguish historical records from current recommendations
- avoid exposing restricted data or sensitive information
- preserve correction and withdrawal context in public-safe terms

Archived does not mean validated.

## 3. What Should Be Archived

Archive candidates include:

- public releases
- approved docs releases
- schema versions
- benchmark contract versions
- result artifact schemas
- run manifest schemas
- public-safe aggregate result packages
- release records
- correction records
- deprecated project records
- paper-support packages that passed release review

Archive records should link to tags, commits, release notes, and review records where possible.

## 4. What Should Not Be Publicly Archived Without Review

Do not publicly archive without review:

- row-level datasets
- row-level labels
- row-level feature tables
- row-level predictions
- ranking tables
- split manifests
- group assignments
- sequence-pair leakage tables
- raw upstream dataset mirrors
- partner-controlled wet-lab records
- confidential reviewer notes
- private correspondence
- secrets or credentials
- unpublished partner-sensitive material

If source/license, privacy, confidentiality, or release status is unresolved, hold the artifact or archive only a public-safe description.

## 5. Deprecation States

### Active

Current and maintained.

### Superseded

Replaced by a newer version, but still historically valid for its original scope.

### Deprecated

No longer recommended. May have a replacement, stale assumptions, policy gaps, or known limitations.

### Archived

Preserved for history. Not necessarily current.

### Withdrawn

Removed from recommendation or public use because of serious claim, dataset, artifact, security, confidentiality, or policy issue.

### Corrected

Updated after an error or unsafe claim/artifact issue. The correction record should explain the change in public-safe terms.

## 6. Correction Process

When correction is needed:

1. Identify affected files, claims, artifacts, releases, and citations.
2. Classify the issue: claim, dataset, artifact, reproducibility, security, paper alignment, attribution, or release status.
3. Stop further public distribution where feasible if sensitive or unsafe material is involved.
4. Remove or narrow unsupported claims.
5. Restrict unsafe artifacts where appropriate.
6. Publish a public-safe correction note if needed.
7. Update release records, project registry entries, and citations where relevant.
8. Record remaining caveats.

Avoid exposing secrets, restricted row-level data, or confidential partner information while correcting.

## 7. Withdrawal Process

Withdrawal may be needed when a release or artifact:

- exposes restricted data
- exposes secrets or private information
- makes unsupported validation or clinical claims
- violates dataset/source/release boundaries
- uses official branding without approval
- creates material public confusion
- cannot be corrected safely in place

Withdrawal records should state:

- what was withdrawn
- why it was withdrawn in public-safe terms
- replacement or correction, if any
- citation guidance for historical references
- whether artifacts remain available, restricted, or removed

## 8. Dataset / Artifact Withdrawal Cautions

Dataset and artifact withdrawal requires special care.

If a release contains row-level or source-derived artifacts with unresolved permission:

- hold public distribution
- preserve only public-safe metadata where feasible
- avoid reposting the restricted content in issues or correction notes
- update dataset/provenance records
- update public-safe artifact manifests
- update affected claims

This policy does not make final legal conclusions about dataset licensing or redistribution.

## 9. Paper / Preprint Correction Alignment

Paper and preprint corrections should align:

- manuscript text
- README claims
- supplement
- data/code availability wording
- source-to-claim review
- public-safe artifact manifest
- release notes
- citation guidance

If a paper says a package is Hold or internal-review only, public docs must not imply public submission readiness.

## 10. Derivative Project Archive / Deprecation Process

For derivative projects:

1. Update `docs/derivatives/PROJECT_REGISTRY.md`.
2. Record project status: active, superseded, deprecated, archived, withdrawn, or corrected.
3. State whether claims remain valid for historical context.
4. State whether official or aligned branding remains appropriate.
5. Link replacement project, if any.
6. Record dataset/artifact release caveats.
7. Preserve public-safe correction context.

Permea-aligned does not mean Permea-validated.

## 11. Recordkeeping Requirements

Archive, correction, deprecation, and withdrawal records should include:

- affected project or artifact
- version, tag, commit, or release
- status
- reason
- claim impact
- dataset/artifact impact
- citation impact
- replacement or correction
- reviewers or approvers
- manual approval status
- remaining blockers

## 12. No-Go Conditions

Do not publicly archive or retain as current if:

- restricted row-level artifacts are exposed without permission
- source/license/redistribution status is unresolved for included row-level artifacts
- claims exceed evidence level
- dry-lab results are described as wet-lab validation
- clinical efficacy is implied
- universal delivery prediction is implied
- AlphaFold-level performance, adoption, or standardization is implied
- public release approval is missing
- confidential or partner-sensitive information is exposed

## 13. Manual Approval Requirements

Manual approval is required for:

- withdrawing public releases
- archiving paper-support packages
- archiving or releasing dataset artifacts
- correcting public validation, clinical, or public-readiness claims
- deprecating official Permea projects
- changing public citation guidance for major releases
- publishing partner-sensitive corrections

Exact approver roster remains deferred until governance assigns it.

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Attribution does not equal authorship. Attribution does not equal endorsement. Archived does not mean validated. Permea-aligned does not mean Permea-validated.
