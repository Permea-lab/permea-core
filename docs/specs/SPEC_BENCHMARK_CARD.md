# Benchmark Card Specification

## Overview

A benchmark card is a public metadata record for a computational task definition and its expected review artifacts.

## Purpose

Benchmark cards connect dataset cards to task type, split policy, metric set, output artifacts, limitations, and claim boundaries.

## Required fields

- `benchmark_id`
- `task_type`
- `dataset_card_refs`
- `split_policy`
- `metric_set`
- `output_artifacts`
- `limitations`
- `claim_boundary`

## Recommended fields

- `baseline_policy`
- `feature_policy`
- `version`
- `related_evidence_cards`
- `review_status`

## Field definitions

- `benchmark_id`: stable identifier for the benchmark card.
- `task_type`: classification, regression, ranking, retrieval, extraction, or another bounded task type.
- `dataset_card_refs`: relative paths or public references to dataset cards.
- `split_policy`: split method, grouping policy, seed policy, and leakage-control notes.
- `metric_set`: primary and secondary metrics with task level rationale.
- `output_artifacts`: expected generated files for review.
- `limitations`: task, source, metric, or release limits.
- `claim_boundary`: explicit statement of what the benchmark can support.

## Example structure

```yaml
benchmark_id: example_benchmark_card
task_type: binary_classification
dataset_card_refs:
  - dataset_cards/example.yaml
split_policy:
  method: fixed_split
metric_set:
  primary: pr_auc
output_artifacts:
  - metrics.json
  - manifest.yaml
limitations:
  - source_defined_labels
claim_boundary: Computational benchmark definition only; no biological-performance claim.
```

## Validation expectations

Validation should confirm required fields, dataset-card references, metric definitions, output artifact names, limitations, and claim boundaries. Validation should not run models or measure performance.

## Claim boundaries

Benchmark cards define reproducible computational task surfaces. They do not establish biological transport, mechanism, safety, therapeutic effect, broad prediction, or best-performance status.

## Limitations

Benchmark cards depend on source labels, dataset readiness, metric fit, split design, and release posture.

## Extension points

External contributors may add baseline policy, feature policy, model-family constraints, reviewer notes, and task level metadata while preserving the required fields.
