# Permea Core Specification

## Title

Permea Core: Product and System Specification

## Purpose

Permea Core is an open toolkit and benchmark-oriented technical foundation for sequence-first delivery and mRNA expression engineering. Its purpose is to establish a public technical foundation for defining benchmark tasks, standardizing interfaces, and supporting reproducible workflows in open development.

The repository is intended to make technical work easier to inspect, compare, and extend. It is not intended to imply validated biological performance.

## Problem Statement

Work on delivery-aware sequence modeling is often difficult to audit or compare across teams. Common issues include inconsistent task framing, weak provenance, tightly coupled evaluation logic, and results that cannot be rerun from repository state.

This creates a practical problem: even when methods appear related, it is often unclear whether they are solving the same benchmark task, using comparable inputs, or being evaluated under comparable rules.

Permea Core addresses this problem by defining shared repository-level contracts for benchmark specification, execution, evaluation, and provenance.

The current standard-layer companion docs include `DELIVERY-TAXONOMY.md`, `EVIDENCE-LADDER.md`, `BENCHMARK-CONTRACT.md`, and `RESULT-ARTIFACT-SCHEMA.md`.

## Intended Users

Permea Core is intended for:

- computational biology and bio-ML researchers who need inspectable benchmark tasks
- ML engineers building baseline or learned methods against explicit task definitions
- technical contributors who need stable repository contracts before extending the system
- reviewers, grant evaluators, and program stakeholders assessing whether the repository represents a credible technical program

## Non-Goals

Permea Core does not aim, in its current stage, to provide:

- wet-lab validation claims
- biological efficacy claims
- a full end-user product for non-technical operators
- proprietary data systems hidden behind a nominally public repository
- broad platform features unrelated to benchmark execution, provenance, or reproducible workflows

## System Scope

Permea Core covers the repository surfaces required to support a benchmark-first technical program for sequence-first delivery and mRNA expression engineering.

In scope:

- benchmark definitions and versioned task identifiers
- typed interfaces for inputs, outputs, and evaluation surfaces
- reference execution paths for baseline methods
- provenance-aware result capture
- specifications and architecture documents that govern repository growth

Out of scope for the current stage:

- wet-lab operations
- undocumented private pipelines
- clinical or product claims
- generalized laboratory operations software

## Core Capabilities

### 1. Benchmark Definition

The system should define benchmark tasks with explicit identifiers, versions, expected inputs, expected outputs, and evaluation rules.

### 2. Data and Interface Contracts

The system should define how input records, delivery context, derived datasets, and evaluation targets are represented so that benchmark workflows are inspectable and rerunnable.

### 3. Baseline Execution

The system should support reference execution paths for baseline methods through standard interfaces rather than benchmark-specific ad hoc scripts.

### 4. Evaluation

The system should compute benchmark metrics through versioned evaluation logic so outputs remain comparable across runs.

### 5. Provenance

The system should record benchmark version, dataset reference, code revision, configuration reference, execution timestamp, and output artifact references for each benchmarked run.

### 6. Documentation as Contract

The repository documentation should specify the technical intent and boundaries of the system clearly enough that external contributors can understand how the repository is meant to evolve.

## Inputs and Outputs

### Inputs

Permea Core is expected to work with the following input categories:

- sequence records and associated metadata
- delivery-context descriptors or conditioning variables
- target labels or benchmark outcomes
- run configurations for preprocessing, execution, and evaluation
- repository-local specifications that define benchmark and metric behavior

These inputs may vary by benchmark, but they must be described through explicit interfaces rather than implicit notebook assumptions.

### Outputs

Permea Core is expected to produce:

- benchmark-ready datasets or dataset references
- standardized model or baseline outputs
- machine-readable metric summaries
- provenance records for benchmarked runs
- result artifacts that can be compared across benchmark versions

## Repository Surfaces

The repository is organized as a set of explicit surfaces:

- `README.md`: top-level project positioning and orientation
- `MANIFESTO.md`: project principles and operating commitments
- `docs/`: specifications, architecture documents, ADRs, and roadmap
- `research/`: research framing and benchmark rationale
- `src/`: implementation surfaces for benchmark execution and evaluation
- `notebooks/`: exploratory analysis that should inform, not replace, reproducible workflows
- `results/`: benchmark outputs and associated result artifacts
- `assets/`: visual assets used by project documentation

These surfaces should remain aligned. Specifications should match implementation intent, and results should map back to defined benchmark and provenance contracts.

## Milestones

### Milestone 1: Repository Contract

- finalize specification, architecture, and ADR set
- align terminology and repository boundaries
- define the baseline standards for open-source-first, benchmark-first development

### Milestone 2: Benchmark Execution Skeleton

- establish module and interface contracts for benchmark execution
- define provenance and result artifact expectations
- support a first end-to-end reproducible workflow

### Milestone 3: Reference Benchmarks

- publish explicit benchmark definitions
- run reference baselines through standard execution paths
- produce comparable result artifacts with provenance

## Success Criteria

Permea Core should be considered successful in its early stage if:

- benchmark tasks are defined clearly enough for an external technical reviewer to understand what is being measured
- reproducible workflows are possible from repository state and explicit configuration
- result artifacts are tied to stable provenance
- repository documents use consistent terminology and reflect actual system boundaries
- the repository reads as a credible public technical foundation for an open toolkit and benchmarks program
