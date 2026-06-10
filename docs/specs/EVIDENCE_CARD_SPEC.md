# Evidence Card Spec

Status: Public specification

## Purpose

An evidence card is a structured public record for literature, method, dataset, or benchmark evidence. It preserves source context, extracted claims, uncertainty, review status, and links to related dataset cards or benchmark tasks.

Evidence cards help contributors make delivery-related evidence inspectable. They do not strengthen a source beyond what it supports, and they do not turn computational or literature evidence into biological validation.

## Required Fields

### Evidence Card ID

Provide a stable identifier.

Example:

```yaml
evidence_card_id: ec_public_bbb_source_001
```

### Source Citation

Identify the source clearly.

Include:

- paper, database, supplement, repository, or public record
- citation, DOI, URL, or accession where available
- source version or access date when useful

### Source Type

Describe the source category.

Examples:

- peer-reviewed paper
- preprint
- public database
- benchmark repository
- supplementary table
- method documentation

### Delivery Context

Describe the delivery-related context.

Examples:

- blood-brain barrier
- membrane penetration
- cargo delivery
- localization
- delivery-adjacent expression proxy

### Molecule / Sequence / Cargo

Record the molecule, sequence, cargo, or input object when available and public-safe.

If the source does not provide this detail, mark it as unknown. Do not infer sensitive or unavailable details.

### Assay or Evidence Type

Describe the evidence type.

Examples:

- assay result
- benchmark label
- literature statement
- computational result
- method description
- review statement

### Extracted Claim

Write a narrow extracted claim that stays close to the source.

The extracted claim should preserve:

- source wording where practical
- assay or benchmark context
- molecule or sequence context
- limitations and uncertainty

### Support Level

Assign a support level.

Suggested levels:

- source pointer
- extracted evidence draft
- reviewed source evidence
- benchmark-linked evidence
- reproducible computational evidence
- external validation evidence

Support levels describe evidence status. They do not imply broad delivery, therapeutic, or clinical claims.

### Uncertainty / Limitations

Record uncertainty and limits.

Examples:

- assay context incomplete
- source claim is narrow
- benchmark label is source-defined
- sample size is limited
- negative examples may be uncertain
- cargo context differs from target use

### Related Dataset or Benchmark Task

Link the evidence card to related public objects.

Examples:

- dataset card path
- benchmark task path
- run manifest path
- candidate report path

### Review Status

State the review status.

Examples:

- draft
- maintainer-reviewed
- community-reviewed
- benchmark-linked
- retired

### Public Claim Boundary

An evidence card can document source-backed evidence and uncertainty. It does not convert a source claim into wet-lab validation, clinical effectiveness, broad prediction across delivery contexts, a claim that delivery is solved, or best-performance status.

## Minimal Example Skeleton

```yaml
evidence_card_id: ec_public_bbb_source_001
source_citation:
  citation: "Public source citation or URL"
  source_type: peer_reviewed_paper
  version_or_access_date: "2026-06-10"
delivery_context: blood_brain_barrier
molecule_sequence_cargo:
  molecule_type: peptide
  sequence_or_identifier: public_source_identifier
  cargo_context: unknown
assay_or_evidence_type: benchmark_label
extracted_claim:
  text: "Source reports a BBB-related label for the referenced sequence under its stated context."
  source_context_preserved: true
support_level: extracted_evidence_draft
uncertainty_limitations:
  - assay_context_requires_review
  - extracted_claim_should_not_be_generalized_beyond_source_context
related_objects:
  dataset_card: docs/specs/DATASET_CARD_SPEC.md
  benchmark_task: docs/specs/BENCHMARK_TASK_SPEC.md
review_status: draft
public_claim_boundary: "Source-backed evidence record only; no wet-lab, clinical, universal, or solved-delivery claim."
```
