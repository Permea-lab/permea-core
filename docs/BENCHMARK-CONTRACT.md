# Benchmark Contract

## Purpose

A Permea benchmark contract exists to make delivery-related modeling work legible, comparable, reproducible, and bounded in interpretation. It is the compact standard layer that defines what a benchmarked task is expected to contain and how its outputs should be read.

## Why benchmark contracts are needed

Without explicit benchmark contracts, adjacent work becomes hard to compare, hard to rerun, vulnerable to overclaiming, and too dependent on local or hidden conventions. A benchmark contract reduces ambiguity by making the task surface, evaluation surface, and provenance surface explicit.

## Core benchmark components

- task definition
- dataset surface
- input schema
- output schema
- split / evaluation policy
- baseline definitions
- metrics
- provenance requirements
- result artifact requirements

## Minimum contract fields

The exact fields may vary by benchmark, but a valid Permea benchmark surface should define at least:

- `benchmark_id`
- `task_name`
- `biological_context`
- `barrier_context`
- `input_schema`
- `target_definition`
- `split_policy`
- `metrics`
- `baseline_models`
- `provenance_required`
- `output_artifacts`

Compact example:

```yaml
benchmark_id: bbb_peptide_v1
task_name: permeability_related_signal_prioritization
biological_context: peptide_sequence_modeling
barrier_context: blood_brain_barrier
input_schema:
  - sequence
  - label
split_policy: stratified_kfold_5
metrics:
  - roc_auc
  - pr_auc
  - mcc
baseline_models:
  - dummy
  - logistic_regression
  - random_forest
provenance_required: true
output_artifacts:
  - metrics.json
  - predictions.csv
  - ranking.csv
  - summary.csv
  - manifest.json
```

## Evaluation rules

- metrics must be tied to a defined split policy
- class imbalance must be acknowledged where relevant
- baseline comparisons are required for interpretation
- benchmark reports should separate exploratory outputs from contract-grade results

These rules exist so that benchmark results remain interpretable as benchmark evidence rather than detached performance claims.

## Provenance requirements

Benchmark-grade results should be linked to:

- dataset identity
- config identity
- run identity
- model identity
- output artifacts

If these links are missing, the result may still be useful internally, but it should not be treated as a canonical benchmark surface.

## Imported vs regenerated distinction

Imported legacy artifacts are useful for continuity and comparison. They help preserve context and allow earlier work to remain visible.

Regenerated current-contract artifacts define the current benchmark evidence surface. When Permea describes present benchmark behavior or current evidence status, regenerated artifacts should be treated as the authoritative public reference point.

## Claim-boundary rules

- benchmark evidence is not equivalent to biological validation
- strong model metrics do not imply universal delivery predictability
- benchmark artifacts support bounded candidate-prioritization claims only at the current stage

These rules should constrain interpretation across docs, figures, summaries, and external-facing benchmark narratives.

## Why this matters for Permea

Permea is trying to build sequence-first delivery work on benchmark-first infrastructure rather than on isolated analyses. A benchmark contract helps make future wedges comparable, supports standard-setting ambition without overstating maturity, and strengthens public technical credibility by making benchmarked work easier to inspect and reuse.
