# Result Artifact Schema

## Purpose

Permea result artifacts are not just outputs. They are the structured evidence surface that makes benchmarked work inspectable, reusable, and comparable across runs.

## Why result artifacts need structure

Without consistent artifact structure, results become difficult to compare, provenance is weakened, figures become detached from runs, and publication or benchmark reuse becomes fragile. A stable artifact schema keeps result packages tied to defined benchmark logic rather than presentation-only summaries.

## Minimum artifact set

The minimum contract-grade result set should include:

- `metrics.json`
- `predictions.csv`
- `ranking.csv`
- `summary.csv`
- `manifest.json`

Figures may be included as recommended support artifacts, but they are not mandatory core artifacts.

## Required artifact definitions

- `metrics.json` — scalar evaluation outputs for a defined run
- `predictions.csv` — row-level prediction outputs for the evaluated examples
- `ranking.csv` — ranked candidate outputs for prioritization workflows
- `summary.csv` — compact tabular summary for comparison surfaces
- `manifest.json` — provenance and run identity record that links the result package together

## Recommended metadata fields

Expected metadata fields will vary by artifact type, but Permea-style result surfaces will often benefit from fields such as:

- `run_id`
- `benchmark_id`
- `model_name`
- `artifact_type`
- `dataset_id`
- `config_id`
- `created_at`
- `source_type`
- `notes`

These fields should be used where they fit the current repository contract rather than imposed mechanically.

## Contract-grade vs exploratory artifacts

Contract-grade artifacts are outputs tied to a defined benchmark contract, defined rerun logic, and explicit provenance. They represent the current benchmark evidence surface.

Exploratory artifacts are useful internal outputs, draft figures, notebook exports, or analysis helpers that may inform benchmark work but should not be treated as current benchmark evidence by default.

This distinction matters because Permea needs to separate inspectable benchmark artifacts from useful but less stable analytical byproducts.

## Naming and organization principles

- use stable, descriptive file naming
- keep outputs linked to a run identifier
- avoid ambiguous names such as `final_v2_real`
- keep tables, metrics, figures, and manifests separated by type when practical

These principles are intentionally simple. Their purpose is to keep result packages readable, traceable, and reusable without overengineering the artifact layer.

## Why this matters for Permea

Permea is building toward benchmark-first development, standardization, paper-support readiness, external reuse, and clearer trust surfaces. A visible result artifact schema makes it easier for future evidence repos to emit comparable outputs and easier for outside reviewers to understand what a Permea result package actually represents.
