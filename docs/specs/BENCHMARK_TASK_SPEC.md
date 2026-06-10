# Benchmark Task Spec

Status: Public specification

## Purpose

A benchmark task defines the computational surface that connects a dataset card to inputs, labels, split policy, baselines, metrics, output artifacts, and claim boundaries.

Benchmark tasks make Permea results easier to compare and reproduce. They support bounded computational evidence and candidate prioritization before wet-lab work, not biological validation or clinical claims.

## Required Fields

### Task Name

Provide a stable task name.

Example:

```yaml
task_name: bbb_peptide_prioritization_v1
```

### Task Type

Describe the computational task type.

Examples:

- binary classification
- multiclass classification
- regression
- ranking
- retrieval
- evidence extraction

### Biological Barrier / Delivery Context

Describe the delivery context represented by the task.

Examples:

- blood-brain barrier
- membrane penetration
- subcellular localization
- delivery-adjacent RNA expression proxy

### Dataset Card Link

Link the benchmark task to one or more dataset cards.

Include:

- dataset card path or URL
- dataset version
- label version if separate
- release posture

### Split Policy

Define how data is split for evaluation.

Include:

- split method
- random seed policy where relevant
- leakage checks
- grouping policy
- repeated-run policy if used

### Baseline Models

List required baselines before stronger model comparisons.

Examples:

- dummy baseline
- logistic regression
- random forest
- simple descriptor threshold
- published baseline if reproducible and public

### Metric Set

Define the metrics used to evaluate the task.

Include:

- primary metric
- secondary metrics
- class imbalance considerations
- ranking metrics if applicable
- calibration or threshold reporting if applicable

### Output Artifacts

List expected output artifacts.

Recommended outputs:

- `metrics.json`
- `ranking.csv`
- `manifest.yaml`
- `benchmark_card.md`
- `evidence_cards.json` when applicable

### Run Manifest Requirements

State what every run manifest must record.

Include:

- run ID
- repository commit
- dataset version
- benchmark task version
- config hash
- feature set
- model or baseline
- split policy
- output artifact paths
- runtime or environment summary without private host details

### Limitations

List task level limits.

Examples:

- source-scoped label definitions
- class imbalance
- limited barrier context
- missing assay context
- descriptor limitations
- restricted data release posture

### Public Claim Boundary

A benchmark task can define a reproducible computational benchmark surface. It does not establish wet-lab validation, clinical effectiveness, broad prediction across delivery contexts, a claim that delivery is solved, or best-performance status unless separately supported by a specific benchmark comparison and review.

## Minimal Example Skeleton

```yaml
task_name: bbb_peptide_prioritization_v1
task_type: binary_classification
biological_barrier_delivery_context: blood_brain_barrier
dataset_card:
  path: docs/specs/examples/public_bbb_dataset_card.yaml
  dataset_version: "0.1.0"
  release_posture: public_review
split_policy:
  method: stratified_kfold
  folds: 5
  random_seed_policy: fixed_seed_recorded_in_manifest
  leakage_checks:
    - exact_sequence_duplicate_check
baseline_models:
  - dummy
  - logistic_regression
  - random_forest
metric_set:
  primary: pr_auc
  secondary:
    - roc_auc
    - mcc
    - f1
output_artifacts:
  - metrics.json
  - ranking.csv
  - manifest.yaml
  - benchmark_card.md
run_manifest_requirements:
  - run_id
  - repository_commit
  - dataset_version
  - benchmark_task
  - config_hash
  - feature_set
  - model_or_baseline
  - split_policy
  - output_artifact_paths
limitations:
  - labels_are_source_defined_benchmark_labels
  - benchmark_results_do_not_prove_transport_or_mechanism
public_claim_boundary: "Computational benchmark evidence only; supports candidate prioritization before wet-lab work."
```
