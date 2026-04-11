# Run Manifest Schema

## Purpose

The run manifest is the canonical provenance artifact for a benchmark execution in Permea Core. It records the minimum information required to identify what was run, against which dataset reference, from which code state, with which configuration, and what artifacts and summary metrics were produced.

The schema is intentionally narrow. It is designed to support reproducibility and audit before broader execution infrastructure exists.

## Required Fields

- `benchmark_id`: stable benchmark identifier
- `benchmark_version`: explicit benchmark version string
- `run_id`: unique identifier for the execution instance
- `dataset_ref`: dataset or dataset manifest reference used by the run
- `code_revision`: repository revision or commit identifier
- `config_ref`: path or identifier for the configuration used by the run
- `execution_timestamp`: execution timestamp in ISO 8601 format
- `output_artifacts`: list of structured artifact references emitted by the run
- `metrics_summary`: machine-readable summary of top-level metric values

## Field Semantics

### `benchmark_id`

Identifies the benchmark family or task. This value should be stable across reruns of the same logical benchmark.

### `benchmark_version`

Identifies the version of the benchmark contract, including task semantics, schema expectations, or evaluation logic.

### `run_id`

Identifies a single execution instance. This should be unique enough to distinguish repeated runs of the same benchmark and configuration.

### `dataset_ref`

Points to the dataset version, manifest, or derived dataset artifact used during the run. This field should make the input surface auditable even when datasets are represented indirectly.

### `code_revision`

Records the repository revision associated with the run. In most cases this should be a git commit SHA or a similarly precise revision identifier.

### `config_ref`

Points to the configuration used to produce the run. The configuration may be a file path, URI, or versioned internal reference.

### `execution_timestamp`

Records when the run was executed. Use ISO 8601 UTC timestamps where possible.

### `output_artifacts`

Lists the main artifacts produced by the run. Each artifact entry should include:

- `artifact_type`
- `path`
- `description` as optional supporting context

### `metrics_summary`

Provides a compact summary of machine-readable metrics for comparison and indexing. Detailed evaluation artifacts may exist separately, but the manifest should include the top-line values needed to identify the run outcome.

## Example Shape

```yaml
benchmark_id: "mrna_expression_baseline"
benchmark_version: "0.1.0"
run_id: "2026-04-10-baseline-a"
dataset_ref: "datasets/expression_panel/v0.1.0/train_manifest.yaml"
code_revision: "9f31c8d"
config_ref: "configs/baselines/expression_baseline_v1.yaml"
execution_timestamp: "2026-04-10T09:15:00Z"
output_artifacts:
  - artifact_type: "predictions"
    path: "results/2026-04-10-baseline-a/predictions.parquet"
    description: "Per-record predictions for the benchmark split."
metrics_summary:
  pearson_r: 0.0
  mae: 0.0
```

## Notes

- The manifest does not replace richer result artifacts; it anchors them.
- Additional fields may be added later, but only if they improve reproducibility or auditability.
- Result summaries without a corresponding manifest should not be treated as canonical benchmark outputs.
