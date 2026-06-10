# Permea Contribution Objects

Status: Public documentation

## Purpose

Permea Core is an open execution layer for delivery engineering. Contributions should be structured enough to make delivery evidence inspectable, reproducible, and bounded in interpretation.

This document defines the public contribution objects that make Permea useful as a community movement: Dataset Card, Benchmark Task, Evidence Card, Run Manifest, Feature Descriptor, Baseline Model, and Candidate Report.

Each object should make clear what is being contributed, why it matters, what a contributor should provide, how reviewers should evaluate it, and what public claim boundary applies.

## Dataset Card

What it is: A structured description of a dataset or dataset candidate.

Why it matters: Dataset cards make source, label meaning, assay context, provenance, limitations, and release posture visible before a dataset becomes part of a benchmark surface.

What a contributor should provide:

- dataset name
- task family
- source and citation
- sequence type or input object
- label definition
- positive and negative criteria
- assay or evidence context where known
- inclusion and exclusion criteria
- known limitations
- suggested metrics
- allowed outputs or release posture
- contributor name or handle
- review status

Review criteria:

- source attribution is clear
- label meaning is bounded and does not imply universal biological truth
- assay or evidence context is described where relevant
- limitations and missing context are explicit
- public release posture is clear
- no unsupported validation or performance claim is made

Public claim boundary: A dataset card can support dataset transparency and benchmark readiness review. It does not prove delivery, mechanism, safety, therapeutic effect, or clinical performance.

## Benchmark Task

What it is: A proposed executable task that connects a dataset card to input schemas, label schemas, split policy, baseline models, metrics, outputs, and non-claims.

Why it matters: Benchmark tasks make computational delivery evidence comparable by fixing what is being measured and how results should be interpreted.

What a contributor should provide:

- task name
- task family
- dataset card link or source reference
- input schema
- label schema
- split policy
- baseline models
- metrics
- output artifacts
- non-claims
- reviewer notes

Review criteria:

- task boundary is clear
- dataset and label assumptions are inspectable
- metrics and baselines are appropriate for the task
- split policy is explicit enough to reproduce
- outputs include aggregate summaries and provenance
- non-claims prevent overinterpretation

Public claim boundary: A benchmark task can define a computational benchmark surface. It does not establish biological truth, universal prediction, or external validation by itself.

## Evidence Card

What it is: A structured source-backed evidence object extracted from a paper, database, supplement, or reviewed public source.

Why it matters: Evidence cards preserve source context so delivery-related statements can be reviewed without losing citation, assay, limitation, or uncertainty details.

What a contributor should provide:

- source paper, database, or public record
- molecule or sequence reference
- barrier or task context
- assay or evidence type
- cargo context where relevant
- organism, cell, or experimental context where relevant
- reported outcome
- evidence strength
- limitations
- citation
- extraction notes
- review status

Review criteria:

- source is identifiable
- extraction does not strengthen the original claim
- biological context is not omitted when claim-relevant
- evidence strength and limitations are explicit
- draft evidence is marked as draft until reviewed

Public claim boundary: An evidence card can document source-backed evidence and uncertainty. It does not upgrade a source claim into wet-lab validation, clinical evidence, or a general delivery claim.

## Run Manifest

What it is: A provenance record for a computational benchmark run.

Why it matters: Run manifests make results rerunnable by recording the benchmark task, dataset version, code version, configuration, features, metrics, and output artifacts.

What a contributor should provide:

- run ID
- benchmark task
- dataset version
- code version
- configuration
- feature set
- model or baseline
- metrics
- output artifacts
- reproducibility notes
- deviations from expected commands or settings

Review criteria:

- enough configuration is recorded to rerun the analysis
- outputs are tied to a known task and dataset version
- metrics match the benchmark task
- deviations are documented
- public outputs avoid restricted row-level artifacts unless release status is clear

Public claim boundary: A run manifest supports reproducibility review for a computational run. It does not prove biological transport, mechanism, safety, or therapeutic effect.

## Feature Descriptor

What it is: A definition of a sequence-derived descriptor or benchmark descriptor used in a delivery benchmark.

Why it matters: Feature descriptors make derived inputs auditable, reproducible, and easier to compare across baseline models and benchmark tasks.

What a contributor should provide:

- descriptor name
- biological or computational rationale
- input requirements
- calculation method
- units or value range where applicable
- implementation reference
- version or parameter choices where relevant
- limitations

Review criteria:

- descriptor meaning is clear
- calculation method is reproducible
- input assumptions are explicit
- limitations are visible
- descriptor values are not treated as causal proof

Public claim boundary: A feature descriptor can explain how a sequence-derived delivery-related signal is computed. It does not establish mechanism or validation on its own.

## Baseline Model

What it is: A reproducible baseline implementation or configuration for a benchmark task.

Why it matters: Baseline models give benchmark tasks a transparent comparison point before more complex methods are introduced.

What a contributor should provide:

- model family
- task
- input features
- training configuration
- split policy
- metrics
- output artifacts
- environment or version notes
- limitations

Review criteria:

- configuration is reproducible
- comparison is tied to the defined benchmark task
- aggregate metrics are reported with task context
- provenance and output artifacts are included
- limitations and failure modes are explicit

Public claim boundary: A baseline model can support benchmark comparison under a defined task. It does not justify broad best-performance, wet-lab, clinical, or universal prediction claims.

## Candidate Report

What it is: An exportable prioritization summary for candidate sequences or input objects.

Why it matters: Candidate reports help reviewers understand why a candidate was prioritized before wet-lab work, including benchmark context, feature profile, evidence cards, risk flags, and limitations.

What a contributor should provide:

- candidate identifier or approved public example input
- benchmark task and dataset version
- ranking or score context
- feature profile
- related evidence cards
- risk flags
- uncertainty and limitations
- non-claims
- review status

Review criteria:

- candidate context is tied to a defined benchmark task
- ranking or score is not presented as biological proof
- evidence cards and limitations are linked
- sensitive sequences or row-level outputs are not exposed without approval
- report language remains appropriate for candidate prioritization before wet-lab work

Public claim boundary: A candidate report can support prioritization and review. It does not guarantee delivery, therapeutic effect, safety, or clinical relevance.

## General Public Boundary

All contribution objects should preserve conservative evidence levels:

- computational evidence only unless otherwise stated
- candidate prioritization before wet-lab work
- no wet-lab validation claim
- no clinical or therapeutic effect claim
- no universal delivery prediction claim
- no unsupported best-performance claim
- no solved-delivery claim

When release status is unclear, describe the proposed contribution at aggregate or schema level and ask maintainers for review.

## Next Steps for Contributors

1. Read [CONTRIBUTING.md](../CONTRIBUTING.md).
2. Choose the contribution object that matches the proposed work.
3. Keep the first proposal narrow and reviewable.
4. Include source attribution, limitations, and non-claims.
5. Open a PR only after the contribution object is clear enough to review.
