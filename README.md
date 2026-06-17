<div align="center">
  <img src="assets/Permea Logo_Main.png" alt="Permea symbol" width="300" />
  <br />
  <img src="assets/Permea_text_logo_color.png" alt="Permea wordmark" width="320" />
</div>

<div align="center">

# Permea Core

Open execution layer for sequence-first biological delivery engineering.

Benchmark-first infrastructure for reproducible, computational delivery evidence.

<p align="center">

![Sequence-first](https://img.shields.io/badge/Sequence--first-0F766E?style=flat-square)
![Delivery](https://img.shields.io/badge/Delivery-14B8A6?style=flat-square)
![Benchmarks](https://img.shields.io/badge/Benchmarks-115E59?style=flat-square)
![Reproducible](https://img.shields.io/badge/Reproducible-334155?style=flat-square)
![Open infrastructure](https://img.shields.io/badge/Open%20infrastructure-1E293B?style=flat-square)
</p>

</div>

## Overview

Permea Core is an open technical foundation for making biological delivery more benchmarkable, reproducible, and evidence-backed. It organizes delivery-related datasets, benchmark tasks, run manifests, output cards, and contribution workflows so researchers can compare sequence-first delivery hypotheses before wet-lab validation.

Permea is not another single predictor. Permea Core is the public execution layer for benchmark-first delivery engineering: shared specifications, reusable artifacts, and reproducible workflows for computational evidence before experimental follow-up.

## Quickstart

Run the first-user demo from the repository root:

```bash
python3 scripts/permea_demo.py
```

The demo discovers public example packages, runs local validation, links evidence and claim-boundary surfaces, and prints next recommended commands. See [Quickstart](QUICKSTART.md), [Evidence index](docs/evidence/evidence-index.md), and [Claim registry](docs/claims/claim-registry.md).

## Evidence And Claims

After the quickstart, review the evidence path:

```bash
python3 scripts/permea_evidence.py
```

Start with [Evidence map](docs/evidence/evidence-map.md), then review [Claim-to-evidence matrix](docs/evidence/claim-to-evidence-matrix.md), [Evidence maturity model](docs/evidence/evidence-maturity-model.md), [Evidence timeline](docs/evidence/evidence-timeline.md), [Benchmark registry](docs/benchmarks/benchmark-registry.md), [Claim registry](docs/claims/claim-registry.md), and [Validation](#documentation-map).

## Benchmarks

Review the benchmark framework:

```bash
python3 scripts/permea_benchmarks.py
```

The benchmark path is [Quickstart](QUICKSTART.md) -> [Evidence](docs/evidence/evidence-map.md) -> [Benchmarks](docs/benchmarks/README.md) -> [Claims](docs/claims/claim-registry.md) -> validation commands.

## Why This Exists

Delivery is one of the bottlenecks for next-generation therapeutics. Peptides, RNA systems, mRNA designs, protein therapeutics, gene-editing payloads, and targeted biologics all depend on reaching the right biological context, but delivery evidence is still fragmented across datasets, papers, predictors, assays, and internal pipelines.

That fragmentation makes results hard to compare:

- dataset sources and label definitions are often unclear
- benchmark tasks, split policies, and metrics differ across projects
- assays and biological contexts are not always comparable
- candidate rankings can be difficult to audit
- dry-lab evidence is rarely packaged for reuse before experimental follow-up

Permea Core exists to create public technical defaults for this problem: dataset cards, benchmark cards, evidence cards, run manifests, output formats, and contribution workflows that make delivery-related computational evidence easier to inspect and reproduce.

## What Permea Core Provides

Permea Core is early-stage public infrastructure. Some components are present as specifications and documentation, while others are roadmap surfaces that will grow as benchmark contracts stabilize.

The intended execution stack includes:

- **Benchmark Registry**: task definitions, dataset references, label schemas, metrics, baseline requirements, output artifacts, versions, and claim boundaries.
- **Dataset Assembly**: loading, validation, schema normalization, feature-extraction inputs, label checks, and source attribution.
- **Baseline Runner**: reproducible baseline configurations for transparent benchmark execution.
- **Evaluation Engine**: aggregate metrics, ranking behavior, sensitivity summaries, and limitation notes.
- **Provenance Tracking**: run identifiers, benchmark versions, dataset versions, code versions, configuration hashes, feature sets, and artifact lists.
- **Output Formatter**: standard benchmark packages for review, reproduction, and publication-safe summaries.
- **Dataset Cards**: public records for dataset source, labels, readiness, limitations, and provenance.
- **Benchmark Cards**: scoped benchmark definitions with inputs, metrics, splits, baselines, and claim boundaries.
- **Evidence Cards**: structured literature or computational evidence with uncertainty and review status.
- **Run Manifests**: reproducibility records for how a result was produced.
- **Contribution Workflows**: review paths for dataset cards, benchmark tasks, evidence cards, feature descriptors, baselines, reproduction reports, and documentation improvements.

## What Permea Core Is Not

Permea Core is not another single BBB predictor.

It does not claim that delivery is solved. It does not claim wet-lab validation. It does not make clinical or therapeutic effect claims. It does not claim universal delivery prediction. It does not claim state-of-the-art status.

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

## Current Scope

Permea Core is an early-stage public foundation. Current work focuses on delivery-related sequence features, benchmark surfaces, run specifications, and candidate prioritization before wet-lab.

The first public computational evidence package is [`permea-signal-ml`](https://github.com/Permea-lab/permea-signal-ml). Permea Core provides the benchmark/specification/execution-layer foundation that future evidence packages can reuse.

Wet-lab validation is a future or external validation path, not a current claim of this repository.

## Relationship to `permea-signal-ml`

- [`permea-core`](https://github.com/Permea-lab/permea-core): benchmark, specification, and execution-layer foundation.
- [`permea-signal-ml`](https://github.com/Permea-lab/permea-signal-ml): first computational evidence package for a reproducible benchmark-oriented demonstration.

`permea-signal-ml` shows how bounded sequence-derived delivery-related signal can be packaged for reproduction and review. `permea-core` defines the reusable infrastructure that should support many future benchmark tasks and contribution objects.

## Related Repositories

- [`permea-core`](https://github.com/Permea-lab/permea-core): open execution layer, benchmark contracts, public movement entry point, and contribution specs.
- [`permea-signal-ml`](https://github.com/Permea-lab/permea-signal-ml): first evidence package and BBB benchmark support repository.

`permea-signal-ml` is a first concrete evidence package. `permea-core` is the reusable infrastructure layer that should support many future benchmark tasks and contribution objects.

## Documentation Map

Core project documents:

- [Open This First](OPEN_THIS_FIRST.md)
- [Review Hub](REVIEW_HUB.md)
- [Evidence Layer](docs/evidence/README.md)
- [Evidence Map](docs/evidence/evidence-map.md)
- [Claim-to-Evidence Matrix](docs/evidence/claim-to-evidence-matrix.md)
- [Evidence Maturity Model](docs/evidence/evidence-maturity-model.md)
- [Evidence Timeline](docs/evidence/evidence-timeline.md)
- [Benchmark Layer](docs/benchmarks/README.md)
- [Benchmark Registry](docs/benchmarks/benchmark-registry.md)
- [Benchmark Lifecycle](docs/benchmarks/benchmark-lifecycle.md)
- [Benchmark Card Template](docs/benchmarks/benchmark-card-template.md)
- [Benchmark Governance](docs/benchmarks/benchmark-governance.md)
- [Claim Registry](docs/claims/claim-registry.md)
- [External Examples](examples/README.md)
- [Decision Records](docs/decisions/README.md)
- [Manifesto](MANIFESTO.md)
- [Delivery Taxonomy](docs/DELIVERY-TAXONOMY.md)
- [Evidence Ladder](docs/EVIDENCE-LADDER.md)
- [Claim Boundary](docs/CLAIM_BOUNDARY.md)
- [Roadmap](docs/ROADMAP.md)
- [ADR-0001: Open-Source-First](docs/adr/ADR-0001-open-source-first.md)
- [ADR-0002: Benchmark-First](docs/adr/ADR-0002-benchmark-first.md)
- [ADR-001: Project Breadcrumb and Review Hub Standard](docs/adr/ADR-001-project-breadcrumb-and-review-hub-standard.md)

Scientific governance:

- [Claim Registry](docs/scientific-governance/CLAIM_REGISTRY.md)
- [Dataset Policy](docs/scientific-governance/DATASET_POLICY.md)
- [Public-Safe Artifact Policy](docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md)
- [Reproducibility Guide](docs/scientific-governance/REPRODUCIBILITY_GUIDE.md)
- [Paper Alignment Policy](docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md)

Open-source operating docs:

- [Project Documentation Operating Standard](docs/runbooks/project-documentation-operating-standard.md)
- [P-DOC-001 Project Operating System Adoption Report](docs/reports/p-doc-001-project-operating-system-adoption-v0.md)
- [OSS Operating Docs Map](docs/OSS_OPERATING_DOCS_MAP.md)
- [OSS Operating PR Summary](docs/OSS_OPERATING_PR_SUMMARY.md)
- [Release Review Process](docs/release/RELEASE_REVIEW_PROCESS.md)
- [Public Release Checklist](docs/release/PUBLIC_RELEASE_CHECKLIST.md)
- [Release Ownership Matrix](docs/release/RELEASE_OWNERSHIP_MATRIX.md)
- [Versioning Policy](docs/release/VERSIONING_POLICY.md)
- [Archive and Deprecation Policy](docs/release/ARCHIVE_AND_DEPRECATION_POLICY.md)
- [Attribution Policy](docs/release/ATTRIBUTION_POLICY.md)

Artifact specs:

- [Public Artifact Specifications](docs/specs/README.md)
- [Dataset Card Spec](docs/specs/DATASET_CARD_SPEC.md)
- [Benchmark Task Spec](docs/specs/BENCHMARK_TASK_SPEC.md)
- [Evidence Card Spec](docs/specs/EVIDENCE_CARD_SPEC.md)
- [Run Manifest Spec](docs/specs/RUN_MANIFEST_SPEC.md)

Benchmark registry and examples:

- [Benchmark Registry](docs/benchmarks/BENCHMARK_REGISTRY.md)
- [Online Data Source Registry](docs/data/ONLINE_DATA_SOURCE_REGISTRY.md)
- [Acquisition and Fallback Plan](docs/data/ACQUISITION_AND_FALLBACK_PLAN.md)
- [Examples README](docs/examples/README.md)
- [Example Output Package](docs/examples/EXAMPLE_OUTPUT_PACKAGE.md)

Validate the benchmark registry scaffold:

```bash
python3 scripts/validate_benchmark_registry.py
```

Validate the source registry scaffold:

```bash
python3 scripts/validate_source_registry.py
```

Validate all current local registry and artifact layers:

```bash
python3 scripts/validate_permea_artifacts.py
```

Reproduce all public artifact surfaces:

```bash
python3 scripts/permea_reproduce.py
```

Validate the public reproducibility bundle:

```bash
python3 scripts/permea_validate.py
```

Check public artifact examples against the current Permea artifact standards:

```bash
python3 scripts/permea_check.py
```

Run the first-user quickstart demo:

```bash
python3 scripts/permea_demo.py
```

Copyable external examples are available at [External Examples](examples/README.md).

Run the deterministic benchmark dry-run:

```bash
python3 scripts/run_permea_dry_run.py
```

Generate the public artifact index:

```bash
python3 scripts/generate_artifact_index.py
```

Validate run manifest examples:

```bash
python3 scripts/validate_run_manifests.py
```

Generate public-safe benchmark card examples from the registry scaffold:

```bash
python3 scripts/generate_benchmark_card.py
```

Generate all current deterministic artifact examples:

```bash
python3 scripts/generate_permea_artifacts.py
```

Generate the public demo packet:

```bash
python3 scripts/generate_demo_packet.py
```

Generate the public evidence matrix:

```bash
python3 scripts/generate_evidence_matrix.py
```

Generate the public evaluation packet:

```bash
python3 scripts/permea_evaluate.py
```

Inspect the public artifact specification registry:

```bash
python3 scripts/permea_specs.py
```

Current generated artifacts are indexed at [Public Artifact Index](docs/examples/generated/ARTIFACT_INDEX.md).

Generated benchmark dry-run reports are available under [Generated Benchmark Dry-Run Reports](docs/examples/generated/dry_runs/README.md).

The generated public demo packet is available at [Public Demo Packet](docs/examples/generated/DEMO_PACKET.md).

The generated public evidence matrix is available at [Public Evidence Matrix](docs/examples/generated/EVIDENCE_MATRIX.md).

Quick local setup starts at [Quickstart](QUICKSTART.md). The reproducibility contract is documented in [Reproducibility](REPRODUCIBILITY.md). The generated reproducibility report is available at [Public Reproducibility Report](docs/examples/generated/REPRODUCIBILITY_REPORT.md).

The public evaluation pattern is documented in [Evaluation Bundle](EVALUATION.md). The generated evaluation packet is available at [Public Evaluation Packet](docs/examples/generated/EVALUATION_PACKET.md).

Generate run manifest examples:

```bash
python3 scripts/generate_run_manifests.py
```

Contributor and community docs:

- [Contribution Objects](docs/CONTRIBUTION_OBJECTS.md)
- [Community Roadmap](docs/COMMUNITY_ROADMAP.md)
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

- **Dataset Card**: describe a dataset source, labels, provenance, readiness, and limitations.
- **Benchmark Task**: define inputs, labels, metrics, split policy, baselines, and expected outputs.
- **Evidence Card**: structure literature or computational evidence with uncertainty and review status.
- **Feature Descriptor**: document a sequence-derived descriptor, computation method, limitations, and references.
- **Baseline Model**: add a comparable model or configuration with reproducible evaluation.
- **Reproduction Report**: report whether a benchmark run or evidence package reproduces as documented.
- **Documentation improvement**: clarify specs, contribution paths, limitations, or release guidance.

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Community standards are in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), security reporting is in [SECURITY.md](SECURITY.md), and support guidance is in [SUPPORT.md](SUPPORT.md).

For public contribution surfaces, see [Contribution Objects](docs/CONTRIBUTION_OBJECTS.md), [Claim Boundary](docs/CLAIM_BOUNDARY.md), and [Community Roadmap](docs/COMMUNITY_ROADMAP.md).

## Claim Boundaries

Permea public materials should preserve clear evidence levels:

- computational evidence only unless otherwise stated
- candidate prioritization before wet-lab
- no wet-lab validation claim
- no clinical or therapeutic effect claim
- no universal delivery prediction claim
- no state-of-the-art claim
- no delivery-is-solved claim

Benchmark metrics summarize behavior under a defined computational task. They do not prove transport, mechanism, safety, therapeutic effect, or generalization beyond the benchmark scope.

## Status

Permea Core is active early-stage open infrastructure. The first evidence package exists in `permea-signal-ml`, and benchmark, dataset, and community documentation are being expanded.

This README does not make any public submission or readiness claim. Public releases, papers, and external postings should follow the repository's release and claim-review policies.

## License, Citation, and Contact

- License: [LICENSE](LICENSE)
- Citation metadata: [CITATION.cff](CITATION.cff)
- Contact: a.kim@permea.us
