# Benchmark Card: bbb_b3pred_dataset3

> Generated from Permea benchmark registry metadata. This card is a public-safe benchmark summary, not a record of dataset acquisition, model execution, or validation results.

## Benchmark ID

bbb_b3pred_dataset3

## Task Name

bbb_peptide_prioritization_v1

## Delivery Context

blood_brain_barrier_peptide_prioritization

## Maturity Level

baseline-ready

## Dataset Card

docs/specs/DATASET_CARD_SPEC.md

## Benchmark Task Spec

docs/specs/BENCHMARK_TASK_SPEC.md

## Split Policy

- method: stratified_kfold
- leakage_checks:
  - exact_sequence_duplicate_check
  - source_group_review

## Metrics

- primary: pr_auc
- secondary:
  - roc_auc
  - mcc
  - f1

## Baseline Models

- dummy
- logistic_regression
- random_forest

## Output Artifacts

- metrics.json
- ranking.csv
- manifest.yaml
- benchmark_card.md
- evidence_cards.json

## Limitations

- source_attribution_and_redistribution_require_review
- labels_are_source_defined_benchmark_labels
- aggregate_metrics_do_not_prove_transport_or_mechanism

## Claim Boundary

Computational benchmark evidence only; supports candidate prioritization before wet-lab work.
