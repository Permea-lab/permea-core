# Project Registry

## 1. Purpose

This registry tracks Permea Core, official Permea projects, Permea-aligned projects, and future derivative project placeholders.

The registry is intended to make project scope, status, evidence level, dataset posture, public release state, and paper/preprint linkage visible.

## 2. Registry Status Note

This is an initial registry scaffold.

Entries are descriptive and should not be read as release approval, public readiness, dataset redistribution permission, wet-lab validation, clinical validation, or endorsement beyond the recorded status.

Permea-aligned does not mean Permea-validated.

## 3. Project Registry Table Template

| Project | Type | Repo | Status | Maintainer | Evidence Level | Dataset Policy | Public Release Status | Paper/Preprint Link | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Project name | evidence / benchmark / dataset / method / wet-lab / example / website / fork | URL or TBD | proposed / incubating / active / archived / deprecated | name or TBD | level or TBD | clear / unresolved / N/A | draft / internal review / public-safe candidate / hold / approved / released | path / DOI / TBD / N/A | public-safe notes |

## 4. Initial Known Projects

| Project | Type | Repo | Status | Maintainer | Evidence Level | Dataset Policy | Public Release Status | Paper/Preprint Link | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| permea-core | core governance / standards | `https://github.com/Permea-lab/permea-core` | active | TBD | policy / benchmark standards, not empirical validation | N/A for row-level data by default | public docs in progress; releases require review | N/A | Public OSS operating foundation. Not a claim of biological validation. |
| permea-signal-ml | evidence / paper support | `https://github.com/Permea-lab/permea-signal-ml` | active / internal paper preparation | TBD | benchmark-scoped computational evidence for first BBB-focused paper package | dataset redistribution unresolved; row-level artifacts blocked unless permission is documented | public bioRxiv status hold / not submission-ready as of current known state | internal manuscript/supplement paths in that repo | Paper-specific evidence repo; must follow source-to-claim and public-safe artifact restrictions. |

## 5. Future Placeholder Projects

| Project | Type | Repo | Status | Maintainer | Evidence Level | Dataset Policy | Public Release Status | Paper/Preprint Link | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| permea-benchmarks | benchmark repo | TBD | proposed | TBD | benchmark contract / reproducibility standards | TBD | draft | N/A | Future reusable benchmark task and baseline surfaces. |
| permea-datasets | dataset repo | TBD | proposed | TBD | dataset/provenance standards | source/license review required | hold until policy and permission are clear | N/A | Must not expose row-level restricted artifacts without explicit permission. |
| permea-examples | educational/example repo | TBD | proposed | TBD | examples only | likely N/A or public-safe only | draft | N/A | Must avoid implying validation or production readiness. |
| permea-web | website/project page repo | TBD | proposed | TBD | public communication only | N/A unless artifacts are published | hold until claim alignment review | TBD | Website claims must match repo and paper status. |

## 6. How to Propose a New Project

To propose a new project, provide:

- project name
- project type
- intended scope
- proposed maintainer
- repo URL or proposed location
- evidence level
- dataset and artifact policy status
- public release target, if any
- paper/preprint linkage, if any
- branding status: official Permea, Permea-aligned, or independent fork
- known blockers
- required reviewers

High-impact projects require founder/manual approval before public release or official branding.

## 7. How to Update Registry Entries

Update registry entries when:

- a project changes status
- a maintainer changes
- evidence level changes
- dataset policy status changes
- public release status changes
- paper/preprint linkage changes
- project branding status changes
- a project is archived, corrected, or deprecated

Registry changes that affect public claims or release status should pass claim and release review.

## 8. Archive / Deprecation Rules

Archive or deprecate a project when:

- it is no longer maintained
- a safer or clearer replacement exists
- unsupported claims cannot be corrected promptly
- release or dataset policy problems remain unresolved
- branding or governance scope is unclear
- the project should no longer be used as a current reference

Deprecation notes should be public-safe and should avoid exposing sensitive details.

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Derivative projects must not inherit claim authority automatically. Permea-aligned does not mean Permea-validated. Wet-lab collaboration interest does not equal wet-lab validation.
