# Example Output Package

Status: Public documentation

## Purpose

This document shows a public-safe example of a standard Permea output package.

It uses placeholder values, toy candidate identifiers, and schema-level examples only. It does not include real private paths, private run identifiers, server metadata, unpublished candidate sequences, or unreleased candidate details.

## What An Output Package Is

An output package is the reviewable artifact bundle produced by a Permea benchmark run.

It should make a computational result inspectable by connecting metrics, ranking outputs, provenance, benchmark context, evidence cards, and limitations.

An output package supports computational review. It does not establish wet-lab validation, clinical performance, broad biological mechanism, safety, therapeutic effect, or general delivery prediction.

## Example Package Tree

```text
example_output_package/
  metrics.json
  ranking.csv
  manifest.yaml
  benchmark_card.md
  evidence_cards.json
  limitations.md
```

## File Descriptions

### metrics.json

Aggregate benchmark metrics for the defined task, dataset version, split policy, and model or baseline.

Use this file for public-safe summary metrics, not for unsupported performance claims.

### ranking.csv

Candidate ranking output when the benchmark task supports ranking.

Use toy candidate identifiers in examples. Real candidate-level outputs should follow the release posture for the benchmark and dataset.

### manifest.yaml

A run provenance record that describes the benchmark task, dataset version, repository commit, configuration identifier, feature set, model or baseline, split policy, output paths, and public-safe runtime summary.

The manifest should not include private hostnames, local filesystem paths, credentials, authentication values, or private infrastructure notes.

### benchmark_card.md

A human-readable benchmark summary covering task purpose, dataset context, metric set, baselines, limitations, and claim boundary.

### evidence_cards.json

Structured evidence card references or embedded public-safe evidence card summaries.

Evidence cards should preserve source context, uncertainty, and review status.

### limitations.md

Plain-language limitations for the run and output package.

This file should state what the benchmark does not prove and where interpretation should remain narrow.

## Minimal Pseudo-Examples

### metrics.json

```json
{
  "benchmark_id": "permea_example_benchmark_001",
  "task_name": "example_delivery_prioritization_v1",
  "model_or_baseline": "logistic_regression_baseline",
  "split_policy": "stratified_kfold_placeholder",
  "metrics": {
    "pr_auc": 0.00,
    "roc_auc": 0.00,
    "mcc": 0.00,
    "f1": 0.00
  },
  "notes": [
    "Placeholder numbers only.",
    "Metrics summarize a defined computational task only."
  ]
}
```

### ranking.csv

```csv
candidate_id,rank,score,review_status
toy_candidate_001,1,0.00,example_only
toy_candidate_002,2,0.00,example_only
toy_candidate_003,3,0.00,example_only
```

### manifest.yaml

```yaml
run_id: example_public_run_001
timestamp: "2026-06-11T00:00:00Z"
repository_commit: 0000000000000000000000000000000000000000
dataset:
  dataset_card_path: docs/specs/DATASET_CARD_SPEC.md
  dataset_version: "example"
  label_version: "example"
  release_posture: public_example
benchmark_task:
  benchmark_task_path: docs/specs/BENCHMARK_TASK_SPEC.md
  task_version: "example"
  task_type: binary_classification
configuration:
  config_identifier: public_example_config
feature_set:
  - sequence_length
  - charge_summary
  - hydrophobicity_summary
model_or_baseline:
  family: logistic_regression
  role: transparent_baseline
split_policy:
  method: stratified_kfold_placeholder
metrics_output_path: example_output_package/metrics.json
ranking_output_path: example_output_package/ranking.csv
benchmark_card_path: example_output_package/benchmark_card.md
evidence_card_paths:
  - example_output_package/evidence_cards.json
runtime_environment_summary:
  os_family: linux
  language_runtime: python_3_x
  environment_reference: public_environment_file
public_private_boundary:
  excludes_private_host_details: true
  excludes_credentials: true
  excludes_unreleased_candidate_details: true
public_claim_boundary: "Computational output package only; no wet-lab, clinical, universal, or solved-delivery claim."
```

### benchmark_card.md

```markdown
# Example Benchmark Card

## Task

example_delivery_prioritization_v1

## Dataset Context

Placeholder dataset card reference for example use only.

## Metric Set

- PR-AUC
- ROC-AUC
- MCC
- F1

## Baseline

Transparent baseline placeholder.

## Limitations

- Placeholder example only.
- Dataset, labels, split policy, and metric set require review before real use.
- Aggregate metrics do not prove delivery, mechanism, safety, or therapeutic effect.

## Claim Boundary

Computational benchmark review only.
```

### evidence_cards.json

```json
[
  {
    "evidence_card_id": "ec_example_001",
    "source_citation": "Public source citation placeholder",
    "delivery_context": "example_delivery_context",
    "assay_or_evidence_type": "benchmark_label",
    "extracted_claim": "Example source reports a delivery-related label under its stated context.",
    "support_level": "example_only",
    "review_status": "draft",
    "limitations": [
      "Placeholder example only.",
      "Do not generalize beyond the stated source context."
    ]
  }
]
```

## Public/Private Boundary

Public output packages should exclude:

- private server details
- credentials or authentication values
- proprietary candidate details
- unreviewed claims
- unreleased candidate sequences
- local filesystem paths
- private infrastructure notes

Use placeholder values in examples and review release posture before publishing candidate-level outputs.

## Claim Boundary

An output package supports computational review.

An output package does not establish wet-lab validation, clinical validation, therapeutic effect, biological mechanism, safety, universal prediction, or a claim that delivery is solved.

## Relationship To Specs

This example should be read with:

- [Run Manifest Spec](../specs/RUN_MANIFEST_SPEC.md)
- [Evidence Card Spec](../specs/EVIDENCE_CARD_SPEC.md)
- [Benchmark Task Spec](../specs/BENCHMARK_TASK_SPEC.md)
- [Dataset Card Spec](../specs/DATASET_CARD_SPEC.md)

The specs define required fields and interpretation boundaries. This document only shows one public-safe package shape.
