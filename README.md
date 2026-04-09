<<<<<<< HEAD
# Permea Core

Permea is an open initiative building tools, benchmarks, and reproducible workflows for sequence-first delivery and mRNA expression engineering.

## Why Permea exists

Biological engineering workflows are becoming increasingly powerful, but many of the core design processes remain closed, expensive, and difficult to reproduce.

Permea starts from a simple belief:

**delivery and expression should be treated as engineering problems at the sequence level, not only as formulation or carrier problems.**

Our goal is to help open this design space through transparent tooling, reproducible baselines, and practical engineering workflows.

## What this repository is

`permea-core` is the main repository for the Permea project.

This repository will contain:

- core project documentation
- technical specifications and design documents
- baseline ML workflows and reproducible experiments
- benchmark plans for sequence-first delivery / expression engineering
- early open tooling for mRNA structure design and related biological engineering tasks

## Current scope

Permea is currently focused on building the foundation for an open engineering stack in:

- sequence-based delivery design
- mRNA structure engineering
- reproducible candidate ranking workflows
- benchmark-first biological AI development

## Open source first

Permea is built on the belief that foundational infrastructure for next-generation bioengineering should become more open, more inspectable, and more reproducible.

We are not trying to create another black-box platform.

We are building open groundwork that can lower barriers for researchers, startups, and future collaborators.

## Status

This repository is in its early build phase.

Initial contents will include:

- project manifesto
- technical roadmap
- design specifications
- prior ML experiment summaries
- benchmark and architecture drafts

## Long-term vision

Permea aims to become an open standard layer for sequence-first delivery and expression engineering.

The long-term vision is to support a new generation of biological design workflows that are:

- open by default
- modular by design
- benchmarked in public
- extensible toward real-world translational use

## Contact

Project page: https://github.com/Permea-lab
=======
<div align="center">
  <img src="assets/Permea Logo_Main.png" alt="Permea symbol" width="180" />
  <br />
  <img src="assets/Permea_text_logo_color.png" alt="Permea wordmark" width="320" />
</div>

<div align="center">

# PERMEA CORE

Open toolkit and benchmarks for sequence-first delivery and mRNA expression engineering.

Open by default. Reproducible by design.

`Sequence-first` `Delivery engineering` `mRNA design` `Benchmarks` `Reproducible workflows` `Open bio AI` `Benchmark-first`

</div>

## Intro

Permea Core is a public technical foundation for sequence-first delivery and mRNA expression engineering. The repository is being built as an open toolkit and benchmarks program: a disciplined workspace for specifications, architecture decisions, research framing, and reproducible workflows.

The project is early stage by design. The current priority is to make benchmark definitions, system boundaries, and evaluation assumptions explicit before expanding implementation scope.

## Repository Documents

- [Manifesto](MANIFESTO.md)
- [Specification](docs/SPEC.md)
- [Architecture Design](docs/DD-ARCHITECTURE.md)
- [ADR-0001: Open-Source-First](docs/adr/ADR-0001-open-source-first.md)
- [ADR-0002: Benchmark-First](docs/adr/ADR-0002-benchmark-first.md)

## Why Permea Exists

Work related to delivery-aware sequence modeling is often difficult to compare across papers, internal pipelines, and one-off analyses. Task definitions vary, provenance is frequently incomplete, and evaluation logic is rarely organized for external reuse.

Permea exists to address that gap with a benchmark-first approach:

- define benchmark tasks clearly
- expose assumptions and interfaces directly in the repository
- support reproducible workflows rather than presentation-only results
- make the work inspectable by outside technical contributors

## What Permea Core Is

Permea Core is the base open-source layer of the project. It is intended to provide:

- benchmark definitions for sequence-first delivery and mRNA expression engineering
- repository-level contracts for data, execution, and evaluation
- architecture and decision records that govern repository growth
- a public technical foundation for reproducible workflows and future reference implementations

It is not a claim of validated biological performance. It is the technical program that should make later work legible and comparable.

## Current Scope

The current scope is deliberately narrow:

- establish project principles and repository standards
- specify benchmark-oriented system boundaries
- define architecture and decision records
- align future implementation work around reproducibility and provenance

## Why Open Source

Permea is open-source-first because the value of an open toolkit and benchmarks program depends on inspection. If benchmark tasks, evaluation logic, and reproducible workflows are not visible, they are difficult to trust, extend, or compare.

Open development also imposes useful discipline:

- assumptions must be written down
- benchmark definitions must be stable enough to review
- claims must remain tied to methods and artifacts
- repository growth must stay legible to external contributors

## Repository Structure

The repository is organized around a small number of durable surfaces:

```text
README.md
MANIFESTO.md
docs/
examples/
research/
notebooks/
results/
src/
assets/
```

- `README.md`: project landing page and top-level orientation
- `MANIFESTO.md`: project principles and operating commitments
- `docs/`: specifications, architecture, roadmap, and ADRs
- `examples/`: repository-aligned reference examples
- `research/`: research summaries and benchmark framing
- `notebooks/`: exploratory analysis tied to future reproducible workflows
- `results/`: benchmark outputs and repository-level result artifacts
- `src/`: implementation surfaces for benchmark execution and evaluation
- `assets/`: project identity and visual assets

## Long-Term Vision

Permea Core is intended to become a credible public technical foundation for sequence-first delivery and mRNA expression engineering. If the repository succeeds, it should make benchmark tasks easier to define, baseline methods easier to rerun, and technical decisions easier to audit.

The long-term goal is not breadth for its own sake. The goal is an exact, reusable open toolkit and benchmarks program.

## Status

Permea Core is in repository formation. The documentation set is being established first so that later implementation work can follow a consistent benchmark-first and open-source-first structure. The repository does not currently present wet-lab validation, biological performance claims, or mature benchmark outputs.
>>>>>>> 1fb3175 (docs: establish initial Permea Core documentation baseline)
