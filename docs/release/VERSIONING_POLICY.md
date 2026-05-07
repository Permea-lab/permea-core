# Versioning Policy

## 1. Purpose

This document defines Permea Core's initial versioning policy.

The goal is to make docs, schemas, benchmark contracts, result artifacts, release packages, paper-support artifacts, and derivative project records citeable and interpretable without overstating release readiness or scientific validation.

## 2. What Gets Versioned

Permea should version:

- core docs
- schemas
- benchmark contracts
- result artifact schemas
- run manifest schemas
- evidence ladder revisions
- release packages
- derivative project registry entries
- paper-support artifacts

Versioning a document or artifact does not mean the underlying science is validated.

## 3. Versioning Principles

Versions should:

- identify what changed
- preserve interpretation of prior outputs
- distinguish draft, internal-review, release-candidate, and public-release states
- avoid changing benchmark meaning silently
- keep citations tied to the exact artifact used
- record claim, dataset, and release limitations
- avoid implying dataset redistribution or public release approval without review

## 4. Version Naming Conventions

### Docs v0.x

Early governance and policy docs may use `v0.x` labels while they are still evolving.

Example:

- `CLAIM_REGISTRY v0.1`
- `DATASET_POLICY v0.1`

### Schema Versions

Schemas should use explicit version fields when possible.

Example:

- `result-artifact-schema: 0.1`
- `run-manifest-schema: 0.1`

### Benchmark Contract Versions

Benchmark contracts should record task, dataset, split, metric, artifact, and evidence-level assumptions.

Any change that affects comparability should create a new contract version.

### Release Candidate Versions

Release candidates may use:

- `v0.x-rc.1`
- `v0.x-rc.2`

Release candidates are not final public releases.

### Public Release Versions

Public releases should use stable tags only after release review and required approval.

Example:

- `v0.1.0`
- `v1.0.0`

Do not tag public release versions for datasets, paper packages, or derivative projects until release gates are complete.

## 5. Breaking vs Non-Breaking Changes

Breaking changes include:

- changing benchmark task definition
- changing split protocol
- changing metric definition
- changing required schema fields
- changing artifact meaning
- changing evidence ladder interpretation
- changing public release state
- changing dataset release posture

Non-breaking changes include:

- typo fixes
- clarifying wording without changing policy meaning
- adding examples that do not change requirements
- adding optional metadata fields

When uncertain, treat the change as potentially breaking and document the compatibility impact.

## 6. Schema Compatibility Rules

Schema changes should state:

- previous version
- new version
- required field changes
- optional field changes
- removed fields
- semantic changes
- migration notes
- compatibility with existing artifacts

Old artifacts should remain interpretable where possible.

## 7. Benchmark Reproducibility Implications

Benchmark result claims depend on the version of:

- benchmark contract
- dataset reference
- split protocol
- metric definition
- model or method
- run manifest
- result artifact schema
- evidence ladder

If any of these change, old and new results may not be directly comparable.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

## 8. Citation Implications

Users should cite the exact version, tag, commit, schema, benchmark contract, or artifact used.

Paper-specific claims should cite the relevant paper, preprint, manuscript, or evidence package, not Permea Core alone.

If no DOI or external archive exists, do not invent one. Use repository URL, tag, commit, and date where appropriate.

## 9. Changelog Requirements

Nontrivial version changes should record:

- version or tag
- date
- affected files
- change type
- compatibility impact
- claim impact
- dataset/artifact release impact
- reviewer or approver status
- links to pull requests, issues, or release records

Changelogs should not expose secrets, private data, restricted row-level artifacts, or confidential partner information.

## 10. Deprecated Version Handling

Deprecated versions should remain interpretable when possible.

Deprecation notes should state:

- what is deprecated
- why it is deprecated
- replacement, if any
- whether existing claims remain valid
- whether any artifact or dataset release concern exists
- whether citation remains acceptable for historical use

Deprecated does not mean invalidated unless the record says so.

## 11. Release Tagging Recommendations

Use release tags only when:

- release type is known
- release state is recorded
- required review gates are complete
- claim scope is clear
- dataset/artifact release posture is clear
- public-safe artifact review is complete where needed
- manual approval is recorded where required

Tags should point to the exact commit representing the release.

## 12. What Must Not Be Versioned as Public Release Without Approval

Do not version as public release without required review and approval:

- row-level datasets
- row-level labels
- row-level feature tables
- row-level predictions
- ranking tables
- split manifests
- group assignments
- sequence-pair leakage tables
- raw upstream mirrors
- partner-controlled wet-lab records
- paper/preprint packages
- public release claims
- derivative projects using official Permea branding

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Attribution does not equal authorship. Attribution does not equal endorsement. Archived does not mean validated. Permea-aligned does not mean Permea-validated.
