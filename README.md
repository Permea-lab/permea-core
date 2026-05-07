<div align="center"> <img src="assets/Permea Logo_Main.png" alt="Permea symbol" width="300" /> <br /> <img src="assets/Permea_text_logo_color.png" alt="Permea wordmark" width="320" /> </div>
<div align="center">

# PERMEA CORE

Open toolkit and benchmarks for sequence-first delivery and mRNA expression engineering.

Open by default. Reproducible by design.

<p align="center">

![Sequence-first](https://img.shields.io/badge/Sequence--first-0F766E?style=flat-square)
![Delivery](https://img.shields.io/badge/Delivery-14B8A6?style=flat-square)
![mRNA](https://img.shields.io/badge/mRNA-0EA5A4?style=flat-square)
![Benchmarks](https://img.shields.io/badge/Benchmarks-115E59?style=flat-square)
![Reproducible](https://img.shields.io/badge/Reproducible-334155?style=flat-square)
![Foundation](https://img.shields.io/badge/Foundation-1E293B?style=flat-square)
</p>

</div>

## Intro

Permea Core is a public technical foundation for sequence-first delivery and mRNA expression engineering.

It is being built as an open toolkit and benchmarks program: a disciplined repository for specifications, architecture decisions, research framing, and reproducible workflows.

## Why Permea Exists

Work related to delivery-aware sequence modeling is often difficult to compare across papers, internal pipelines, and one-off analyses. Task definitions vary, provenance is frequently incomplete, and evaluation logic is rarely organized for external reuse.

Permea exists to address that gap with a benchmark-first approach:

- define benchmark tasks clearly
- expose assumptions and interfaces directly in the repository
- support reproducible workflows rather than presentation-only results
- make the work inspectable by outside technical contributors

<br>

<div align="center">
  <img src="assets/core_biological_barrier_bottleneck.png" alt="Biological barrier bottleneck" width="900" />
</div>

<p align="center"><em>Biological barriers such as the BBB, the cell membrane, <br> and the nuclear membrane remain major delivery constraints for large-molecule therapeutics.</em></p>

<br>

## What Permea Core Is

Permea Core is the base open-source layer of the Permea project. It is intended to provide:

- benchmark definitions for sequence-first delivery and mRNA expression engineering
- repository-level contracts for data, execution, and evaluation
- architecture and decision records that govern repository growth
- a public technical foundation for reproducible workflows and future reference implementations

It is not a claim of validated biological performance. It is the technical program that should make later work legible and comparable.

## Repository Documents

- [Manifesto](MANIFESTO.md)
- [Specification](docs/SPEC.md)
- [Architecture Design](docs/DD-ARCHITECTURE.md)
- [Delivery Taxonomy](docs/DELIVERY-TAXONOMY.md)
- [Evidence Ladder](docs/EVIDENCE-LADDER.md)
- [Benchmark Contract](docs/BENCHMARK-CONTRACT.md)
- [Result Artifact Schema](docs/RESULT-ARTIFACT-SCHEMA.md)
- [ADR-0001: Open-Source-First](docs/adr/ADR-0001-open-source-first.md)
- [ADR-0002: Benchmark-First](docs/adr/ADR-0002-benchmark-first.md)

## Permea OSS Operating System

Permea Core provides governance and operating infrastructure for open scientific OSS work. It does not claim completed wet-lab validation, clinical efficacy, or dataset redistribution rights. "AlphaFold for Delivery" may be used only as an ambition or positioning phrase, not as a claim of achieved maturity.

Core community files:

- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security](SECURITY.md)
- [Support](SUPPORT.md)
- [Citation](CITATION.cff)
- [OSS Operating Docs Map](docs/OSS_OPERATING_DOCS_MAP.md)

Scientific governance:

- [Claim Registry](docs/scientific-governance/CLAIM_REGISTRY.md)
- [Dataset Policy](docs/scientific-governance/DATASET_POLICY.md)
- [Public-Safe Artifact Policy](docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md)
- [Reproducibility Guide](docs/scientific-governance/REPRODUCIBILITY_GUIDE.md)
- [Paper Alignment Policy](docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md)

Release, attribution, and archive governance:

- [Release Review Process](docs/release/RELEASE_REVIEW_PROCESS.md)
- [Public Release Checklist](docs/release/PUBLIC_RELEASE_CHECKLIST.md)
- [Release Ownership Matrix](docs/release/RELEASE_OWNERSHIP_MATRIX.md)
- [Versioning Policy](docs/release/VERSIONING_POLICY.md)
- [Archive and Deprecation Policy](docs/release/ARCHIVE_AND_DEPRECATION_POLICY.md)
- [Attribution Policy](docs/release/ATTRIBUTION_POLICY.md)

Contributor, reviewer, and community governance:

- [Contributor Levels](docs/contributors/CONTRIBUTOR_LEVELS.md)
- [Authorship Policy](docs/contributors/AUTHORSHIP_POLICY.md)
- [Dry-Lab Contribution Policy](docs/contributors/DRY_LAB_CONTRIBUTION_POLICY.md)
- [Wet-Lab Collaboration Policy](docs/contributors/WET_LAB_COLLABORATION_POLICY.md)
- [Community Governance](docs/community/COMMUNITY_GOVERNANCE.md)
- [Maintainer Guide](docs/community/MAINTAINER_GUIDE.md)
- [Reviewer Workflow](docs/community/REVIEWER_WORKFLOW.md)
- [Reviewer Credit Policy](docs/community/REVIEWER_CREDIT_POLICY.md)

Derivative project governance:

- [Derivative Project Policy](docs/derivatives/DERIVATIVE_PROJECT_POLICY.md)
- [Project Registry](docs/derivatives/PROJECT_REGISTRY.md)
- [Derivative Review Checklist](docs/derivatives/DERIVATIVE_REVIEW_CHECKLIST.md)

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
