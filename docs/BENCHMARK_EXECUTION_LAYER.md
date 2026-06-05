# Permea Benchmark Execution Layer

## Opening Thesis

Permea is not another predictor. It is an execution layer for delivery benchmarks.

The execution layer defines, assembles, runs, evaluates, records, and exports delivery benchmark workflows.

This is how delivery evidence becomes reproducible and comparable. A benchmark result should be more than a score; it should carry task definition, dataset context, feature context, metrics, provenance, limitations, and exportable artifacts.

## Core Architecture

The Benchmark Execution Layer has six core components:

- Benchmark Registry
- Dataset Assembly
- Baseline Runner
- Evaluation Engine
- Provenance Tracking
- Output Formatter

Optional product and integration surfaces can sit on top:

- CLI
- API
- web workbench
- frontier model tool layer

All surfaces should call the same backend contracts.

## Benchmark Registry

The Benchmark Registry defines:

- task definitions
- dataset references
- label schema
- metrics
- baseline model requirements
- output artifacts
- claim boundaries
- versioning

The registry should answer basic questions before a run starts:

- What is the task?
- What data source and label schema are being used?
- What inputs are allowed?
- What metrics are appropriate?
- What baselines are required?
- What outputs will be produced?
- What claims are not supported by this benchmark?

Versioning matters because delivery tasks evolve. A benchmark task should be rerunnable under a known version.

## Dataset Assembly

Dataset Assembly turns dataset cards and source records into run-ready benchmark inputs.

Responsibilities:

- loading
- validation
- schema normalization
- feature extraction input preparation
- label validation
- source attribution
- public/private boundary handling

Dataset assembly should preserve source context. It should not silently convert source labels into universal biological claims. It should also separate public-safe aggregate outputs from row-level or restricted artifacts that require review.

## Baseline Runner

Baseline models are the first execution standard.

Initial baseline families:

- dummy baseline
- logistic regression
- random forest

Future models can be added through extension points, but Permea should not begin from a state-of-the-art-first framing. Transparent baselines matter because they make the task inspectable, establish sanity checks, and reveal whether a benchmark surface contains learnable signal.

The baseline runner should support:

- model configuration
- feature selection
- split policy
- run reproducibility
- metric export
- candidate ranking when applicable

## Evaluation Engine

The Evaluation Engine computes benchmark metrics and summarizes limitations.

Metrics may include:

- ROC-AUC where ranking discrimination is relevant
- PR-AUC where class imbalance matters
- MCC for binary classification balance
- precision, recall, F1, or task-specific metrics where appropriate

Evaluation should account for:

- class imbalance
- aggregate metrics
- candidate prioritization outputs
- split policy
- sensitivity settings
- known limitations

Aggregate metrics do not prove biology. They summarize behavior under a defined computational task.

## Provenance Tracking

Every run should produce a provenance record.

Core fields:

- `run_id`
- `timestamp`
- `benchmark version`
- `dataset version`
- `code version`
- `config hash`
- `feature set`
- `model`
- `metrics`
- `output paths`
- `reproducibility notes`

Hardware may be recorded generically in public outputs when useful for reproducibility. Public outputs should avoid private resource attribution.

## Output Formatter

Standard artifacts:

- `metrics.json`
- `ranking.csv`
- `manifest.yaml`
- `benchmark_card.md`
- `evidence_cards.json`
- figures
- summary report

Output formatting should separate:

- aggregate public-safe summaries
- review-required row-level artifacts
- candidate-specific reports
- figures intended for public documentation
- provenance artifacts needed for reproducibility

## Dry-Lab Run Lifecycle

1. Select benchmark.
2. Assemble dataset.
3. Extract features.
4. Run baselines or models.
5. Evaluate.
6. Rank candidates.
7. Generate evidence cards.
8. Export package.

The lifecycle should be scriptable, reviewable, and eventually usable through CLI, API, web, and tool surfaces.

## Relationship to Permea DryLab

Permea Core is the backend execution layer.

Permea DryLab is the user-facing workbench.

DryLab should call the same contracts used by CLI, API, web, and frontier-model adapters. A user should get consistent benchmark behavior regardless of surface.

## Relationship to Permea Signal ML

Permea Signal ML is the first evidence package.

It validates the execution-layer concept on a BBB peptide benchmark surface with sequence-derived physicochemical features, baseline models, aggregate metrics, candidate prioritization outputs, and provenance tracking.

It is not the whole platform. It is the first wedge that demonstrates why a reusable execution layer matters.

## Public-Safe Non-Claims

Benchmark execution does not imply wet-lab validation.

Aggregate metrics do not imply clinical performance.

Candidate ranking supports prioritization, not guaranteed delivery.

Permea does not claim universal delivery prediction.

Feature importance should not be treated as causal biological mechanism by itself.

## Contributor Extension Model

Contributors should be able to:

- add benchmark task
- add dataset card
- add feature descriptor
- add baseline model
- add output formatter
- submit run manifest

Each extension should include documentation, provenance expectations, and claim boundaries.

## Closing

The benchmark execution layer is how Permea turns delivery research from isolated results into reproducible dry-lab engineering.
