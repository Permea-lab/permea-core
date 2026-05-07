# Reproducibility Guide

## 1. Purpose

This guide defines Permea Core's initial reproducibility expectations for dry-lab evidence.

Reproducibility means that a benchmark or analysis can be understood, rerun, audited, and interpreted from documented code, data references, configuration, run manifests, and result artifacts.

Reproducibility is not biological validation.

## 2. Reproducibility Levels

### Level 0 - Documented Rationale

The task, hypothesis, or design rationale is written down, but no runnable artifact is provided.

### Level 1 - Inspectable Analysis

Code, notebooks, or scripts are available for inspection, but rerun conditions may be incomplete.

### Level 2 - Rerunnable Workflow

The workflow includes code, data references, configuration, and instructions sufficient for a technical contributor to rerun the analysis under documented conditions.

### Level 3 - Benchmark-Grade Reproducibility

The workflow aligns with a benchmark contract, emits a run manifest, and produces result artifacts following the documented schema.

### Level 4 - Independent Reproduction

An independent contributor can reproduce the key aggregate results from the documented repository state and allowed data access path.

## 3. Required Run Manifest

Benchmark-grade runs should include a run manifest consistent with `docs/RUN-MANIFEST-SCHEMA.md`.

At minimum, the manifest should record:

- benchmark id
- benchmark version
- run id
- dataset reference
- code revision
- config reference
- execution timestamp
- output artifacts
- metrics summary

## 4. Required Result Artifact Schema

Result artifacts should align with `docs/RESULT-ARTIFACT-SCHEMA.md`.

Expected artifact classes include:

- metrics
- predictions, when release-safe
- rankings, when release-safe
- summaries
- manifests
- aggregate figures, when reviewed

Row-level artifacts may be generated internally but should not be published unless release permission is documented.

## 5. Benchmark Contract Alignment

Benchmark-grade work should align with `docs/BENCHMARK-CONTRACT.md` and define:

- task name
- benchmark id
- biological or delivery context
- input schema
- target definition
- split policy
- metrics
- baseline models
- provenance requirements
- output artifact expectations

Claims should not outrun the benchmark contract.

## 6. Environment Capture

Reproducible work should record:

- operating system or runtime context where relevant
- language and package versions
- lockfile or environment file where practical
- command or entrypoint
- config file
- random seeds when used
- code revision
- data reference

If exact environment capture is unavailable, state the limitation.

## 7. Data Availability Constraints

Reproducibility depends on data access, but not every data artifact is public-safe.

When row-level data cannot be redistributed:

- cite or reference the source where permitted
- describe processing at a high level
- provide aggregate metrics and summaries where safe
- document what is held back
- avoid exposing row-level sequences, labels, predictions, rankings, split manifests, group assignments, or leakage tables

Dataset redistribution remains unresolved unless source/license review explicitly permits it.

## 8. Aggregate vs Row-Level Reproducibility Distinction

Aggregate reproducibility means readers can inspect metrics, figures, summaries, manifests, and code paths without seeing restricted row-level records.

Row-level reproducibility means readers can rerun from individual records. This requires explicit data access and release permission.

Permea should distinguish these states rather than implying full public rerunability when row-level data are restricted.

## 9. Reproducibility Review Checklist

Before describing work as reproducible, check:

- Is the benchmark contract defined?
- Is the dataset reference identified?
- Is the code revision recorded?
- Is the config recorded?
- Is the environment described?
- Is the run manifest present?
- Are result artifacts listed?
- Are metrics tied to a split and model?
- Are row-level artifacts release-safe?
- Are aggregate artifacts sufficient for public review?
- Are limitations documented?

## 10. What Counts as Reproducible for Dry-Lab Evidence

Dry-lab evidence may be considered reproducible when:

- a reviewer can identify the benchmark task
- the dataset reference and release status are clear
- the code and config are available or described
- the run manifest anchors the run
- result artifacts are traceable
- metrics are tied to split, model, and artifact
- limitations are explicit

The evidence level should be interpreted using `docs/EVIDENCE-LADDER.md`.

## 11. What Does Not Count as Biological Validation

The following do not constitute biological validation:

- benchmark metrics alone
- computational scores
- candidate rankings
- cross-validation results
- leakage-aware sensitivity analyses
- reproducible dry-lab workflows
- literature-grounded plausibility

Wet-lab validation claims require documented experimental evidence in the relevant assay and context.

## 12. Links to Existing Docs

Related Permea Core docs:

- `docs/BENCHMARK-CONTRACT.md`
- `docs/RESULT-ARTIFACT-SCHEMA.md`
- `docs/RUN-MANIFEST-SCHEMA.md`
- `docs/EVIDENCE-LADDER.md`

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.
