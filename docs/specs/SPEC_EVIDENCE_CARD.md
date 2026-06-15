# Evidence Card Specification

## Overview

An evidence card is a public record that captures source-backed evidence, uncertainty, review status, and related artifact links.

## Purpose

Evidence cards make literature, dataset, method, or benchmark evidence inspectable without expanding claims beyond the source and artifact context.

## Required fields

- `evidence_id`
- `source`
- `evidence_type`
- `extracted_claim`
- `limitations`
- `review_status`
- `claim_boundary`

## Recommended fields

- `related_artifacts`
- `support_level`
- `source_context`
- `uncertainty_notes`
- `reviewer_notes`

## Field definitions

- `evidence_id`: stable identifier for the evidence card.
- `source`: citation, URL, accession, repository, or public source reference.
- `evidence_type`: literature statement, dataset label, method note, benchmark result, or other bounded category.
- `extracted_claim`: narrow source-context statement.
- `limitations`: uncertainty, source, assay-context, review, or applicability limits.
- `review_status`: draft, reviewed, benchmark-linked, retired, or another public status.
- `claim_boundary`: explicit statement of what the evidence card can support.

## Example structure

```yaml
evidence_id: example_evidence_card
source:
  citation: Public source citation or URL
evidence_type: literature_statement
extracted_claim: Source reports a delivery-related observation under its stated context.
limitations:
  - source_context_should_not_be_generalized
review_status: draft
claim_boundary: Source-context evidence record only; no biological-performance claim.
```

## Validation expectations

Validation should confirm required fields, source context, review status, limitations, related artifact paths when present, and explicit claim boundaries. Validation should not reinterpret source evidence.

## Claim boundaries

Evidence cards can document source-backed evidence and uncertainty. They do not convert a source statement into biological validation, therapeutic effect, general delivery prediction, or best-performance status.

## Limitations

Evidence cards depend on source quality, context completeness, extraction quality, and review status.

## Extension points

External contributors may add support levels, source-context structure, uncertainty categories, reviewer notes, and related artifact links while preserving the required fields.

