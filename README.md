<div align="center">
  <img src="assets/Permea Logo_Main.png" alt="Permea symbol" width="300" />
  <br />
  <img src="assets/Permea_text_logo_color.png" alt="Permea wordmark" width="320" />
</div>

<div align="center">

# Permea Core

The open execution layer for delivery engineering.

Making delivery evidence benchmarkable, reproducible, and reusable.

<p align="center">

![Sequence-first](https://img.shields.io/badge/Sequence--first-0F766E?style=flat-square)
![Delivery](https://img.shields.io/badge/Delivery-14B8A6?style=flat-square)
![Benchmarks](https://img.shields.io/badge/Benchmarks-115E59?style=flat-square)
![Reproducible](https://img.shields.io/badge/Reproducible-334155?style=flat-square)
![Open infrastructure](https://img.shields.io/badge/Open%20infrastructure-1E293B?style=flat-square)
</p>

</div>

## Overview

Permea is building the open execution layer for delivery engineering: shared datasets, benchmark contracts, run manifests, evidence cards, and reproducible workflows for computational delivery research.

Permea Core turns scattered delivery evidence into benchmarked, reproducible, evidence-backed dry-lab workflows. It begins with sequence-first delivery benchmarks and expands across delivery task families while keeping claims tied to explicit datasets, metrics, provenance, and limitations.

## Why Permea Exists

Delivery is one of the bottlenecks for next-generation therapeutics. Peptides, RNA systems, mRNA designs, protein therapeutics, gene-editing payloads, and targeted biologics all depend on reaching the right biological context, but delivery evidence is still fragmented across datasets, papers, predictors, assays, and internal pipelines.

That fragmentation makes results hard to compare:

- dataset sources and label definitions are often unclear
- predictors can use different task definitions and split policies
- assays and biological contexts are not always comparable
- candidate rankings can be difficult to audit
- dry-lab evidence is rarely packaged for reuse before experimental follow-up

Permea exists to make delivery evidence benchmarkable and reusable. The goal is not to replace experimental work. The goal is to make the path into experimental work more structured, inspectable, and evidence-backed.

## What Permea Core Is

Permea Core is the public movement entry point and technical foundation for reusable delivery-engineering workflows. It is intended to provide:

- an open execution layer for delivery benchmark tasks
- a delivery dataset commons built around dataset cards and evidence cards
- a benchmark registry for task definitions, metrics, and claim boundaries
- baseline and evaluation runners for reproducible computational evidence
- provenance and output-package conventions
- the backend foundation for a future DryLab workbench
- a research intelligence layer for structured claims, sources, and candidate explanations
- an open contribution model for delivery evidence

The repository currently emphasizes specifications, benchmark contracts, governance, and reproducibility docs. Implementation surfaces can grow over time as the public contracts stabilize.

## What Permea Core Is Not

Permea Core is not another single BBB predictor.

It does not claim that delivery is solved. It does not claim wet-lab validation. It does not make clinical or therapeutic effect claims. It does not claim universal delivery prediction. It does not claim state-of-the-art status. It does not claim maturity comparable to AlphaFold.

"AlphaFold-for-Delivery" is an ambition and infrastructure direction: a shorthand for making delivery engineering more benchmarkable, reproducible, explainable, and executable. It is not an achieved-status claim.

## Core Architecture

Permea Core is organized around an execution stack:

1. **Benchmark Registry**: task definitions, dataset references, label schemas, metrics, baseline requirements, output artifacts, versions, and claim boundaries.
2. **Dataset Assembly**: loading, validation, schema normalization, feature-extraction inputs, label checks, and source attribution.
3. **Baseline Runner**: reproducible baseline configurations for transparent benchmark execution.
4. **Evaluation Engine**: aggregate metrics, ranking behavior, sensitivity summaries, and limitation notes.
5. **Provenance Tracking**: run identifiers, benchmark versions, dataset versions, code versions, configuration hashes, feature sets, and artifact lists.
6. **Output Formatter**: standard benchmark packages for review, reproduction, and publication-safe summaries.
7. **API / Tool Layer Foundation**: stable contracts that future CLI, API, web, and model-assisted interfaces can call.
8. **DryLab Surface**: a future user-facing workflow for candidate prioritization before experimental follow-up.

Existing technical docs:

- [Specification](docs/SPEC.md)
- [Architecture Design](docs/DD-ARCHITECTURE.md)
- [Benchmark Contract](docs/BENCHMARK-CONTRACT.md)
- [Result Artifact Schema](docs/RESULT-ARTIFACT-SCHEMA.md)
- [Run Manifest Schema](docs/RUN-MANIFEST-SCHEMA.md)
- [Run Manifest Walkthrough](docs/RUN-MANIFEST-WALKTHROUGH.md)

## Dry-Lab Workflow

A Permea dry-lab run should be explicit and reproducible:

1. Define the benchmark task.
2. Assemble the dataset.
3. Extract sequence features.
4. Run baselines or models.
5. Evaluate metrics.
6. Rank candidates where the task supports ranking.
7. Generate evidence cards.
8. Export a reviewable package.

This workflow supports candidate prioritization before experimental work. It does not establish biological transport, mechanism, safety, or therapeutic performance.

## Standard Output Artifacts

Permea benchmark runs should produce structured outputs such as:

- `metrics.json`
- `ranking.csv`
- `manifest.yaml`
- `benchmark_card.md`
- `evidence_cards.json`
- figures or summary reports where applicable

These artifacts should separate aggregate public summaries from review-required row-level artifacts, candidate-specific reports, and provenance records.

## Current Benchmark Roadmap

Permea starts with sequence-first delivery benchmarks and expands carefully across task families. Not every roadmap item is complete yet.

Current and planned directions:

- BBB peptide benchmark
- CPP / membrane penetration benchmark
- localization / targeting proxy tasks
- RNA and delivery-adjacent benchmark surfaces
- literature evidence graph for structured claims, sources, and evidence cards

Each task should remain bounded by its data source, label policy, split policy, metric set, limitations, and release posture.

## Related Repositories

- [`permea-core`](https://github.com/Permea-lab/permea-core): open execution layer, benchmark contracts, public movement entry point, and contribution specs.
- [`permea-signal-ml`](https://github.com/Permea-lab/permea-signal-ml): first evidence package and BBB benchmark support repository.

`permea-signal-ml` is a first concrete evidence package. `permea-core` is the reusable infrastructure layer that should support many future benchmark tasks and contribution objects.

## Documentation Map

Core project documents:

- [Manifesto](MANIFESTO.md)
- [Delivery Taxonomy](docs/DELIVERY-TAXONOMY.md)
- [Evidence Ladder](docs/EVIDENCE-LADDER.md)
- [Roadmap](docs/ROADMAP.md)
- [ADR-0001: Open-Source-First](docs/adr/ADR-0001-open-source-first.md)
- [ADR-0002: Benchmark-First](docs/adr/ADR-0002-benchmark-first.md)

Scientific governance:

- [Claim Registry](docs/scientific-governance/CLAIM_REGISTRY.md)
- [Dataset Policy](docs/scientific-governance/DATASET_POLICY.md)
- [Public-Safe Artifact Policy](docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md)
- [Reproducibility Guide](docs/scientific-governance/REPRODUCIBILITY_GUIDE.md)
- [Paper Alignment Policy](docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md)

Open-source operating docs:

- [OSS Operating Docs Map](docs/OSS_OPERATING_DOCS_MAP.md)
- [OSS Operating PR Summary](docs/OSS_OPERATING_PR_SUMMARY.md)
- [Release Review Process](docs/release/RELEASE_REVIEW_PROCESS.md)
- [Public Release Checklist](docs/release/PUBLIC_RELEASE_CHECKLIST.md)
- [Release Ownership Matrix](docs/release/RELEASE_OWNERSHIP_MATRIX.md)
- [Versioning Policy](docs/release/VERSIONING_POLICY.md)
- [Archive and Deprecation Policy](docs/release/ARCHIVE_AND_DEPRECATION_POLICY.md)
- [Attribution Policy](docs/release/ATTRIBUTION_POLICY.md)

Contributor and community docs:

- [Contribution Objects](docs/CONTRIBUTION_OBJECTS.md)
- [Contributor Levels](docs/contributors/CONTRIBUTOR_LEVELS.md)
- [Authorship Policy](docs/contributors/AUTHORSHIP_POLICY.md)
- [Dry-Lab Contribution Policy](docs/contributors/DRY_LAB_CONTRIBUTION_POLICY.md)
- [Wet-Lab Collaboration Policy](docs/contributors/WET_LAB_COLLABORATION_POLICY.md)
- [Community Governance](docs/community/COMMUNITY_GOVERNANCE.md)
- [Maintainer Guide](docs/community/MAINTAINER_GUIDE.md)
- [Reviewer Workflow](docs/community/REVIEWER_WORKFLOW.md)
- [Reviewer Credit Policy](docs/community/REVIEWER_CREDIT_POLICY.md)

Planned public docs:

- [Permea Manifesto](docs/PERMEA_MANIFESTO.md)
- [Scientific Thesis](docs/SCIENTIFIC_THESIS.md)
- [Delivery Dataset Commons](docs/DELIVERY_DATASET_COMMONS.md)
- [Benchmark Execution Layer](docs/BENCHMARK_EXECUTION_LAYER.md)
- [Research Intelligence Layer](docs/RESEARCH_INTELLIGENCE_LAYER.md)
- [Frontier Model Tool Layer](docs/FRONTIER_MODEL_TOOL_LAYER.md)
- Open Movement and Community

These planned docs are not linked here until they exist in the repository.

## How to Contribute

Permea needs contributions that make delivery evidence easier to inspect, compare, reproduce, and extend.

Useful contribution paths include:

- propose a dataset card
- propose a benchmark task
- add an evidence card
- document a feature descriptor
- add a baseline model or baseline configuration
- submit a reproduction report
- improve documentation

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Community standards are in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), security reporting is in [SECURITY.md](SECURITY.md), and support guidance is in [SUPPORT.md](SUPPORT.md).

## Claim Boundaries

Permea public materials should preserve clear evidence levels:

- computational evidence only unless otherwise stated
- candidate prioritization before experimental follow-up
- no wet-lab validation claim
- no clinical or therapeutic effect claim
- no universal prediction claim
- no state-of-the-art claim
- AlphaFold-for-Delivery is ambition and infrastructure direction, not achieved status

Benchmark metrics summarize behavior under a defined computational task. They do not prove transport, mechanism, safety, therapeutic effect, or generalization beyond the benchmark scope.

## Status

Permea Core is active early-stage open infrastructure. The first evidence package exists in `permea-signal-ml`, and benchmark, dataset, and community documentation are being expanded.

This README does not make any public submission or readiness claim. Public releases, papers, and external postings should follow the repository's release and claim-review policies.

## License, Citation, and Contact

- License: [LICENSE](LICENSE)
- Citation metadata: [CITATION.cff](CITATION.cff)
- Contact: a.kim@permea.us
