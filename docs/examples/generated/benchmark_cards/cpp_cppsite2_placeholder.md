# Benchmark Card: cpp_cppsite2_placeholder

> Generated from Permea benchmark registry metadata. This card is a public-safe benchmark summary, not a record of dataset acquisition, model execution, or validation results.

## Benchmark ID

cpp_cppsite2_placeholder

## Task Name

cpp_membrane_penetration_placeholder_v1

## Delivery Context

cell_penetrating_peptide_membrane_penetration

## Maturity Level

proposed

## Dataset Card

benchmarks/cpp_cppsite2_placeholder.yaml

## Benchmark Task Spec

docs/specs/BENCHMARK_TASK_SPEC.md

## Split Policy

- method: to_be_defined
- leakage_checks:
  - exact_sequence_duplicate_check
  - source_context_review

## Metrics

- primary: to_be_defined
- secondary:
  - roc_auc
  - pr_auc
  - mcc

## Baseline Models

- dummy
- logistic_regression

## Output Artifacts

- metrics.json
- ranking.csv
- manifest.yaml
- benchmark_card.md
- evidence_cards.json

## Limitations

- dataset_card_needed
- source_context_and_label_policy_require_review
- placeholder_entry_not_a_completed_benchmark

## Claim Boundary

Proposed computational benchmark surface only; no wet-lab, clinical, universal, or solved-delivery claim.
