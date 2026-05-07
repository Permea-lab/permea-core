# Derivative Project Policy

## 1. Purpose

This document defines Permea Core's initial derivative project policy.

The goal is to let future Permea-aligned projects reuse Permea Core standards while preventing inherited overclaims, unsafe dataset release, unclear branding, and ambiguous governance.

This policy is an operating policy. It does not make legal conclusions about trademark ownership, employment, institutional IP, dataset licensing, university policy, or authorship disputes.

## 2. What Counts as a Derivative Project

A derivative project is any repository, package, website, benchmark, dataset, analysis, educational example, collaboration workspace, or community fork that uses or claims alignment with Permea Core standards, code, schemas, policies, branding, or evidence framing.

Examples include:

- paper/evidence repositories
- benchmark repositories
- dataset repositories
- method or model repositories
- wet-lab collaboration repositories
- educational examples
- project pages
- forks or downstream community projects

Permea-aligned does not mean Permea-validated.

## 3. Project Categories

### Evidence Repo

A repository supporting a specific manuscript, benchmark result package, source-to-claim review, or paper-support artifact set.

Example: `permea-signal-ml`.

### Benchmark Repo

A repository defining or running benchmark tasks, split protocols, metric surfaces, baseline comparisons, or benchmark-specific reproducibility packages.

### Dataset Repo

A repository containing dataset cards, provenance records, public-safe dataset views, or approved dataset releases.

Dataset repos require strong source/license, attribution, row-level release, and public-safe artifact review.

### Method / Model Repo

A repository implementing methods, models, feature extractors, tooling, or evaluation code aligned with Permea benchmark contracts.

### Validation / Wet-Lab Collaboration Repo

A repository for assay planning, experimental collaboration, protocol review, wet-lab-derived records, or partner work.

Wet-lab collaboration interest does not equal wet-lab validation.

### Educational / Example Repo

A repository containing tutorials, examples, teaching materials, or minimal demos.

Examples must not imply validated biological performance or public dataset redistribution unless separately approved.

### Website / Project-Page Repo

A repository for public-facing project pages, documentation sites, dashboards, or outreach material.

Website claims must remain aligned with the claim registry and release state.

### Independent Community Fork

A fork or downstream project that uses Permea materials independently.

Independent forks should avoid implying official Permea approval, validation, or release authority.

## 4. Permea Core Alignment Requirements

Permea-aligned projects should:

- identify their scope and evidence level
- link to relevant Permea Core policies
- declare dataset and release posture
- keep claims bounded by evidence
- separate aggregate and row-level artifacts
- follow benchmark and result artifact schemas where relevant
- record release decisions
- state whether they are official, aligned, or independent

Derivative projects must not inherit claim authority automatically.

## 5. Claim Registry Inheritance

Derivative projects that use Permea Core framing should follow `docs/scientific-governance/CLAIM_REGISTRY.md`.

They must not claim:

- AlphaFold-level performance, adoption, or standardization
- completed wet-lab validation unless documented
- clinical efficacy
- therapeutic efficacy
- universal delivery prediction
- production-grade drug delivery platform status
- dataset redistribution permission without source/license approval
- robust generalization without benchmark and external validation support

Project-specific claims require project-specific evidence.

## 6. Dataset / Public-Safe Artifact Policy Inheritance

Derivative projects should follow:

- `docs/scientific-governance/DATASET_POLICY.md`
- `docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md`

They should treat the following as hold or blocked unless explicit permission and review are documented:

- row-level sequence datasets
- row-level labels
- row-level feature tables
- row-level predictions
- ranking tables
- split manifests
- group assignments
- sequence-pair leakage tables
- raw upstream dataset mirrors
- partner-controlled wet-lab records

Public source access does not automatically imply redistribution permission.

## 7. Benchmark / Result Schema Inheritance

Derivative benchmark, method, and evidence projects should follow:

- `docs/BENCHMARK-CONTRACT.md`
- `docs/RESULT-ARTIFACT-SCHEMA.md`
- `docs/RUN-MANIFEST-SCHEMA.md`
- `docs/scientific-governance/REPRODUCIBILITY_GUIDE.md`

Benchmark claims should identify dataset, split, metric, model, artifact, and evidence level.

## 8. Release Review Inheritance

Derivative projects should follow:

- `docs/release/RELEASE_REVIEW_PROCESS.md`
- `docs/release/PUBLIC_RELEASE_CHECKLIST.md`
- `docs/release/RELEASE_OWNERSHIP_MATRIX.md`

Public release is blocked when source/license status, row-level artifact status, claim support, paper alignment, or manual approval remains unresolved.

## 9. Branding / Name Usage Guidance

### Official Permea Project

An official Permea project is maintained under Permea governance, uses approved naming, and has an assigned maintainer and release path.

Official status requires founder/manual approval until a fuller governance roster exists.

### Permea-Aligned Project

A Permea-aligned project uses Permea Core standards or policies but is not necessarily an official Permea project.

It should state that alignment does not imply Permea validation, release approval, or endorsement of claims.

### Independent Fork

An independent fork may use open-source materials according to the applicable license, but it must not imply official Permea endorsement, validation, partner status, release approval, or project ownership.

Independent forks should use independent naming when official status is not approved.

## 10. Required Project Metadata

Derivative projects should record:

- project name
- project type
- scope
- maintainer
- repo URL
- evidence level
- dataset policy status
- public-safe artifact status
- release status
- paper/preprint linkage
- branding status
- claim registry alignment status
- known blockers
- manual approval status, if required

## 11. Project Approval Lifecycle

### Proposed

Idea or draft repo under discussion. Not public-release approved.

### Incubating

Scoped work has started, but release, claim, dataset, or governance surfaces may still be incomplete.

### Active

Maintained project with assigned scope, maintainer, policy alignment, and release records.

### Archived

No active maintenance expected. Claims and release state should remain frozen or marked historical.

### Deprecated

Project should no longer be used as the recommended route because a replacement, correction, policy issue, or scope change exists.

## 12. When Founder / Manual Approval Is Required

Founder/manual approval is required when a derivative project:

- uses official Permea branding
- publishes public release candidates
- supports a paper or preprint
- releases row-level or derived dataset artifacts
- makes wet-lab, partner, public-readiness, or validation-adjacent claims
- involves university, nonprofit, lab, company, or institutional collaboration
- creates ambiguity about authorship, governance, or release ownership
- may affect Permea's public scientific reputation

## 13. When University / Nonprofit Collaboration Agreement Is Required

Separate agreement or documented manual review is required when a university, nonprofit, lab, or institutional collaborator contributes:

- wet-lab data
- partner-controlled datasets
- protocols or materials
- unpublished results
- confidential information
- institutional branding or affiliation
- publication-sensitive review
- data with ownership, consent, embargo, transfer, or IP constraints

This policy does not decide institutional policy, material transfer terms, IP ownership, or publication rights.

## 14. What Derivative Projects Must Not Claim

Derivative projects must not claim:

- official Permea status unless approved
- Permea validation unless documented and approved
- AlphaFold-level performance, adoption, or standardization
- completed wet-lab validation unless documented
- clinical efficacy
- therapeutic efficacy
- universal delivery prediction
- production-grade drug delivery platform status
- dataset redistribution permission without source/license approval
- release approval without recorded release review
- paper/preprint readiness without paper alignment and manual approval

## 15. Correction / Deprecation Process

If a derivative project makes unsupported claims, exposes restricted artifacts, creates branding confusion, or violates release boundaries:

1. Identify affected repo, files, artifacts, and claims.
2. Stop or hold public release where feasible.
3. Notify maintainers privately if sensitive details are involved.
4. Correct public-facing claims in public-safe language.
5. Remove or restrict unsafe artifacts where appropriate.
6. Update the project registry.
7. Record whether the project is corrected, archived, deprecated, or withdrawn.

Avoid exposing sensitive details in public issues or release notes.

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Derivative projects must not inherit claim authority automatically. Permea-aligned does not mean Permea-validated. Wet-lab collaboration interest does not equal wet-lab validation.
