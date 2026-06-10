# Run Manifest Spec

Status: Public specification

## Purpose

A run manifest is the public provenance record for a reproducible benchmark run. It records what was run, against which dataset and benchmark task, from which repository commit, with which configuration, and where the outputs are stored.

Run manifests support reproducible benchmark workflows and computational evidence. They do not prove biological transport, mechanism, safety, therapeutic effect, clinical performance, or generalization beyond the benchmark scope.

## Required Fields

### Run ID

Provide a unique run identifier.

Example:

```yaml
run_id: run_bbb_peptide_prioritization_2026_06_10_a
```

### Timestamp

Record when the run was executed. Use ISO 8601 UTC when possible.

### Repository Commit

Record the public repository commit used for the run.

Use a git commit SHA or another precise public revision identifier.

### Dataset Version

Record the dataset card and dataset version.

Include:

- dataset card path
- dataset version
- label version if separate
- release posture

### Benchmark Task

Record the benchmark task and version.

Include:

- benchmark task path
- task version
- task type

### Config Hash

Record a hash or stable identifier for the run configuration.

The config hash should identify settings needed for reproducibility without exposing credentials, sensitive values, or private host details.

### Feature Set

List the feature set used by the run.

Examples:

- sequence length
- charge summary
- hydrophobicity summary
- aromaticity
- task level public descriptors

### Model / Baseline

Record the model or baseline used.

Include:

- model family
- version or configuration identifier
- training policy
- baseline role

### Split Policy

Record the split policy used for evaluation.

Include:

- split method
- seed policy where relevant
- folds or holdout definition
- grouping or leakage-control notes

### Metrics Output Path

Record the path to aggregate metrics.

Example:

```yaml
metrics_output_path: results/run_id/metrics.json
```

### Ranking Output Path

Record the path to candidate rankings when applicable.

Example:

```yaml
ranking_output_path: results/run_id/ranking.csv
```

### Benchmark Card Path

Record the path to the benchmark card or benchmark summary.

### Evidence Card Path

Record evidence card paths when the run emits or references evidence cards.

This field may be empty when evidence cards are not part of the run.

### Runtime / Environment Summary

Provide a public-safe runtime summary without private host details.

Allowed examples:

- operating system family
- language runtime version
- package lock or environment file reference
- hardware class if broadly stated and not private-resource-specific

Do not include:

- private hostnames
- local filesystem paths
- credentials
- authentication values
- private infrastructure notes
- private resource or support details

### Public / Private Boundary

The run manifest should expose enough information for reproducibility and audit while excluding private infrastructure, credentials, restricted row-level data, and sensitive candidate information.

## Minimal YAML Example

```yaml
run_id: run_bbb_peptide_prioritization_2026_06_10_a
timestamp: "2026-06-10T00:00:00Z"
repository_commit: 0000000000000000000000000000000000000000
dataset:
  dataset_card_path: docs/specs/DATASET_CARD_SPEC.md
  dataset_version: "0.1.0"
  label_version: "0.1.0"
  release_posture: public_review
benchmark_task:
  benchmark_task_path: docs/specs/BENCHMARK_TASK_SPEC.md
  task_version: "0.1.0"
  task_type: binary_classification
config_hash: sha256_public_config_hash_placeholder
feature_set:
  - sequence_length
  - charge_summary
  - hydrophobicity_summary
  - aromaticity
model_or_baseline:
  family: logistic_regression
  version: baseline_v1
  role: transparent_baseline
split_policy:
  method: stratified_kfold
  folds: 5
  seed_policy: fixed_seed_recorded
metrics_output_path: results/run_bbb_peptide_prioritization_2026_06_10_a/metrics.json
ranking_output_path: results/run_bbb_peptide_prioritization_2026_06_10_a/ranking.csv
benchmark_card_path: results/run_bbb_peptide_prioritization_2026_06_10_a/benchmark_card.md
evidence_card_paths:
  - results/run_bbb_peptide_prioritization_2026_06_10_a/evidence_cards.json
runtime_environment_summary:
  os_family: linux
  language_runtime: python_3_x
  environment_reference: requirements_or_lockfile_reference
public_private_boundary:
  excludes_private_host_details: true
  excludes_credentials: true
  excludes_sensitive_candidate_data: true
public_claim_boundary: "Reproducible computational run only; no wet-lab, clinical, universal, or solved-delivery claim."
```
