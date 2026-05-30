# Run Manifest Walkthrough

This walkthrough explains the example manifest in
[`examples/run_manifest.example.yaml`](../examples/run_manifest.example.yaml).
For the field-by-field contract, see
[`RUN-MANIFEST-SCHEMA.md`](RUN-MANIFEST-SCHEMA.md).

## What The Example Represents

The example records one completed benchmark execution:

- `benchmark_id` names the benchmark family: `mrna_expression_baseline`.
- `benchmark_version` records the benchmark contract version used for the run.
- `run_id` gives this specific execution a stable identifier.
- `dataset_ref`, `code_revision`, and `config_ref` identify the exact inputs,
  source revision, and configuration used to produce the result.
- `execution_timestamp` records when the run happened.
- `output_artifacts` points to the files emitted by the run.
- `metrics_summary` captures the top-line machine-readable metrics.

Together, those fields let a reviewer answer three basic reproducibility
questions: what was run, what inputs and code produced it, and where are the
outputs recorded?

## Reading The Artifacts

The example lists two artifacts:

- `predictions` points to per-record benchmark predictions.
- `evaluation_report` points to a machine-readable metrics summary.

The manifest is not intended to contain every result directly. It is the
provenance anchor that connects the benchmark run to the generated artifacts.

## Reading The Metrics

`metrics_summary` contains compact values for comparison and indexing. In the
example, `pearson_r` and `mae` are placeholders that show the expected shape of
the summary. Detailed results can live in the referenced evaluation artifact.
