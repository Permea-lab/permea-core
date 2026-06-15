# Dataset Card Specification

## Overview

A dataset card is a public metadata record for a dataset source, dataset candidate, or dataset-shaped input used by a Permea artifact workflow.

## Purpose

Dataset cards make source context, label policy, readiness, provenance, and limitations inspectable before a dataset is connected to a benchmark card or evaluation packet.

## Required fields

- `dataset_id`
- `dataset_name`
- `source`
- `label_schema`
- `limitations`
- `claim_boundary`

## Recommended fields

- `readiness_level`
- `provenance`
- `license_notes`
- `related_benchmark_cards`
- `review_status`

## Field definitions

- `dataset_id`: stable identifier for the dataset card.
- `dataset_name`: human-readable dataset name.
- `source`: citation, URL, accession, repository, or public source reference.
- `label_schema`: label names, allowed values, missing-label policy, and source of labels.
- `limitations`: source, label, release, assay-context, or coverage limits.
- `claim_boundary`: explicit statement of what the card does and does not support.

## Example structure

```yaml
dataset_id: example_dataset_card
dataset_name: Example public dataset card
source:
  citation: Public source citation or URL
label_schema:
  primary_label: example_label
  allowed_values:
    - positive
    - negative
limitations:
  - source_context_requires_review
claim_boundary: Metadata record only; no dataset download or biological-performance claim.
```

## Validation expectations

Validation should confirm required fields, public-safe source references, relative paths, explicit limitations, and explicit claim boundaries. Validation should not infer access rights or execute acquisition.

## Claim boundaries

Dataset cards can support source transparency and benchmark readiness review. They do not prove delivery, mechanism, safety, therapeutic effect, generalization, data access rights, or data acquisition status.

## Limitations

A dataset card can be complete as metadata while the underlying source remains restricted, incomplete, ambiguous, or unsuitable for a benchmark task.

## Extension points

External contributors may add task level label policy, split constraints, source-review status, release posture, and provenance fields while preserving the required fields.
