# Permea Benchmark Registry

Status: Public documentation

## Purpose

The Permea benchmark registry is the public index for delivery-related benchmark surfaces that Permea Core can define, review, and eventually execute through reproducible workflows.

The registry is meant to make benchmark intent visible before a run starts: what task is being measured, which dataset card supports it, how splits and metrics should work, which baselines are expected, what artifacts should be exported, and what claims are not supported.

## What The Benchmark Registry Is

The benchmark registry is a structured catalog of proposed, candidate, and reproducible benchmark tasks.

Each registry entry should connect:

- a delivery context
- one or more dataset cards
- a benchmark task specification
- split and metric policies
- baseline expectations
- output artifacts
- limitations
- a public claim boundary

The registry does not make a benchmark mature by listing it. It records the current maturity level so contributors and reviewers can see what still needs curation, review, execution, or reproduction.

## Why Delivery Needs A Benchmark Registry

Delivery evidence is fragmented across papers, assays, sequence sets, predictors, repositories, and candidate reports. Without a registry, similar tasks can use different labels, split policies, metrics, and output formats while appearing comparable.

A registry helps delivery engineering become more reproducible by making these assumptions explicit:

- which biological barrier or proxy task is being modeled
- what the labels mean
- which source and dataset version are used
- what split policy controls leakage risk
- what metrics are appropriate for the label distribution
- which baselines should be run before stronger comparisons
- which outputs should be exported for review
- which claims remain outside the benchmark boundary

## Current Registry Status

The registry is early-stage public infrastructure.

Current Permea Core work defines the registry structure, maturity levels, entry fields, and relationship to public artifact specifications. Initial benchmark families should use proposed or candidate language until dataset cards, benchmark task specs, baseline outputs, and reproducibility checks support stronger maturity labels.

## Initial Benchmark Categories

### BBB Peptide Benchmark Surface

Purpose: define sequence-first computational tasks for blood-brain barrier related peptide evidence.

Current posture: initial benchmark surface. Use bounded language tied to dataset cards, source labels, split policy, metric set, and limitations.

### CPP / Membrane Penetration Prototype

Purpose: explore benchmark tasks around cell-penetrating peptide and membrane penetration evidence.

Current posture: prototype direction. Source context, label policy, and reproducibility requirements should be reviewed before any baseline-ready claim.

### Localization / Targeting Proxy Roadmap

Purpose: identify localization and targeting proxy tasks that may support delivery-adjacent benchmark surfaces.

Current posture: roadmap. Proxy tasks must state what they do and do not measure.

### Delivery-Adjacent RNA/Protein Design Roadmap

Purpose: track future sequence-derived benchmark surfaces related to RNA, protein, or expression contexts adjacent to delivery engineering.

Current posture: roadmap. Entries should avoid implying biological delivery performance unless independently supported.

### Literature Evidence Graph Support

Purpose: connect benchmark entries to structured evidence cards derived from public sources.

Current posture: support layer. Evidence cards preserve source context and uncertainty; they do not turn source statements into broad validation claims.

## Benchmark Maturity Levels

| Level | Name | Meaning |
| --- | --- | --- |
| 0 | proposed | A task idea or delivery context has been identified. |
| 1 | dataset-carded | One or more dataset cards describe source, labels, provenance, and limitations. |
| 2 | benchmark-candidate | A benchmark task spec exists with inputs, labels, splits, metrics, outputs, and claim boundary. |
| 3 | baseline-ready | Required baselines and expected output artifacts are defined. |
| 4 | reproducible | A public-safe run manifest and output package exist for review. |
| 5 | community-reviewed | Maintainers or community reviewers have reviewed the task, outputs, limitations, and claim boundary. |

Maturity levels describe documentation and reproducibility status. They do not imply wet-lab validation, clinical relevance, or general delivery prediction.

## Registry Entry Fields

Each registry entry should include:

- benchmark ID
- task name
- delivery context
- dataset card
- benchmark task spec
- split policy
- metric set
- baseline models
- output artifacts
- limitations
- claim boundary

Recommended optional fields:

- maturity level
- version
- review status
- related evidence cards
- contribution owner or reviewer
- release posture

## Minimal Example Registry Entry

```yaml
benchmark_id: permea_bbb_peptide_surface_001
task_name: bbb_peptide_prioritization_v1
maturity_level: benchmark-candidate
delivery_context: blood_brain_barrier_peptide_prioritization
dataset_card: docs/specs/DATASET_CARD_SPEC.md
benchmark_task_spec: docs/specs/BENCHMARK_TASK_SPEC.md
split_policy:
  method: stratified_kfold
  leakage_checks:
    - exact_sequence_duplicate_check
metric_set:
  primary: pr_auc
  secondary:
    - roc_auc
    - mcc
baseline_models:
  - dummy
  - logistic_regression
  - random_forest
output_artifacts:
  - metrics.json
  - ranking.csv
  - manifest.yaml
  - benchmark_card.md
  - evidence_cards.json
limitations:
  - labels_are_source_defined_benchmark_labels
  - assay_context_requires_review
  - benchmark_results_do_not_prove_transport_or_mechanism
claim_boundary: "Computational benchmark evidence only; supports candidate prioritization before wet-lab work."
```

This example is a schema illustration. It is not a completed benchmark record.

## Relationship To Specs

Registry entries should link to the public artifact specs:

- [Dataset Card Spec](../specs/DATASET_CARD_SPEC.md)
- [Benchmark Task Spec](../specs/BENCHMARK_TASK_SPEC.md)
- [Run Manifest Spec](../specs/RUN_MANIFEST_SPEC.md)
- [Evidence Card Spec](../specs/EVIDENCE_CARD_SPEC.md)

The registry should not duplicate those specs. It should point to them and record the maturity state of each benchmark surface.

## Public Claim Boundary

The benchmark registry supports public review of computational benchmark surfaces.

It does not establish wet-lab validation, biological transport, mechanism, safety, therapeutic effect, clinical performance, state-of-the-art performance, universal prediction, or a claim that delivery is solved.

Every registry entry should preserve its own limitation notes and claim boundary.

## Contribution Path

Contributors can help by proposing or improving:

- dataset cards
- benchmark task specs
- split policies
- metric sets
- baseline configurations
- output package examples
- evidence cards
- reproduction reports
- limitation notes

Start with [CONTRIBUTING.md](../../CONTRIBUTING.md), then use the relevant contribution object and artifact spec. Keep the first proposal narrow, source-backed, and explicit about limitations.
