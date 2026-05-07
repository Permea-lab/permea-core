# Dataset Policy

## 1. Purpose

This document defines the first Permea Core dataset policy for dataset intake, provenance, release review, and public redistribution boundaries.

The policy exists because open scientific work can still include restricted data, unclear source terms, partner-controlled records, or row-level artifacts that should not be published without review.

This document is not legal advice and does not make final licensing conclusions.

## 2. Dataset Categories

### Public Source Datasets

Datasets distributed by a public source with visible source, citation, and use terms.

Public source does not automatically mean Permea may redistribute row-level copies.

### Third-Party Datasets

Datasets obtained from external projects, publications, databases, websites, collaborators, or benchmark portals.

These require source, license, attribution, and redistribution review.

### Derived Feature Tables

Tables generated from source records, such as sequence-derived descriptors or engineered feature matrices.

Derived features may still expose source-derived row-level records and should be treated cautiously.

### Row-Level Predictions

Per-record model outputs, scores, labels, or ranking values.

These may reveal row-level dataset contents or source-derived structure and require review before public release.

### Aggregate Metrics

Scalar or summary-level results such as ROC-AUC, PR-AUC, MCC, counts, grouped summaries, and non-row-level charts.

Aggregate metrics are often safer than row-level artifacts, but still require claim-boundary review.

### Wet-Lab Contributed Data

Experimental records contributed by collaborators, partners, universities, nonprofits, or internal wet-lab work.

These require explicit ownership, confidentiality, authorship, attribution, and release decisions.

### Private / Confidential Datasets

Datasets with confidentiality, privacy, partner, institutional, unpublished, or contractual restrictions.

These must not be published without explicit approval.

## 3. Dataset Intake Requirements

Before a dataset enters a public or evidence repository, record:

- dataset name
- source URL or source reference
- source organization or authors
- access date
- source version, if available
- original citation, if available
- license or terms, if available
- redistribution terms, if available
- row-level release status
- derived artifact release status
- known privacy, biosafety, confidentiality, or partner constraints
- intended benchmark use

If any of these are unknown, mark them as unresolved rather than assuming permission.

## 4. Provenance Manifest Requirements

Every benchmark-grade dataset surface should have a provenance record that identifies:

- dataset reference
- source identity
- source access path
- processing script or process
- code revision
- config reference
- generated artifact paths
- label definition
- split policy
- known limitations
- release status

The run-level provenance expectations should align with `docs/RUN-MANIFEST-SCHEMA.md`.

## 5. License / Redistribution Review Requirements

Before publishing row-level data or derived row-level artifacts, confirm:

- source license
- source terms of use
- redistribution permission
- required attribution wording
- whether derived data are covered by source terms
- whether row-level predictions or rankings are considered derivative artifacts
- whether partner/manual/legal review is required

Do not infer redistribution permission from article access alone.

## 6. Row-Level Artifact Restrictions

The following should be held unless release permission is explicit:

- row-level sequence datasets
- row-level labels
- row-level feature tables
- row-level predictions
- ranking tables
- split manifests
- group assignments
- leakage-audit pair tables
- raw upstream dataset mirrors
- partner-controlled wet-lab records

Use aggregate summaries and path-level descriptions when row-level release is unresolved.

## 7. B3Pred/B3Pdb-Style Lineage Caution

Some Permea evidence work may trace to B3Pred/B3Pdb-style BBB-penetrating peptide benchmark lineages.

For such datasets:

- cite the relevant source papers and portals where appropriate
- record the exact source path and access date when available
- distinguish article license from dataset redistribution terms
- do not assume local processed datasets can be redistributed
- keep row-level release unresolved until source terms are documented
- state label-source criteria and dataset construction limits where known

## 8. Wet-Lab Partner Dataset Handling

Wet-lab partner data require explicit handling decisions before use or release:

- ownership
- confidentiality
- consent or institutional limits, where relevant
- authorship and contribution credit
- publication permission
- release permission
- embargo or review windows
- assay context and evidence tier

Wet-lab data must not be used to imply validation beyond the documented assay, context, and evidence tier.

## 9. Dataset Contribution Checklist

Before proposing a dataset contribution, provide:

- source identity
- source citation
- license or terms
- redistribution status
- data type and schema
- whether records are row-level
- whether records are derived from restricted sources
- intended benchmark or documentation use
- known limitations
- suggested release posture

Do not include restricted data directly in an issue or pull request.

## 10. Dataset Release Checklist

Before public release, confirm:

- source and license documented
- redistribution permission documented
- attribution wording documented
- row-level release status approved
- derived artifact release status approved
- benchmark claim boundaries reviewed
- sensitive data absent
- secrets absent
- manifest complete
- maintainer/manual approval recorded

If any item remains unresolved, release aggregate summaries only or hold the artifact.

## 11. Dataset Removal / Correction Process

If a dataset or artifact appears to violate source, license, privacy, confidentiality, or release boundaries:

1. Stop further public distribution where feasible.
2. Notify maintainers privately if sensitive details are involved.
3. Preserve enough metadata to audit the issue without exposing restricted content.
4. Remove or restrict the affected artifact if needed.
5. Document the correction in public-safe terms.
6. Update manifests, release notes, and claims affected by the change.

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.
