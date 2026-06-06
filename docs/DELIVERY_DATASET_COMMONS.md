# Permea Delivery Dataset Commons

Status: Public documentation

## Opening Thesis

Delivery evidence needs a dataset commons because delivery claims are only useful when the data behind them can be inspected, compared, and reused under clear boundaries.

Permea's Delivery Dataset Commons is a public structure for dataset cards, evidence provenance, benchmark task linkage, release posture, review status, and limitations. It is not a claim that all delivery evidence is equivalent, complete, experimentally validated, or ready for clinical interpretation.

The commons exists to make sequence-first delivery engineering more benchmarkable. It helps contributors turn scattered papers, databases, supplements, and benchmark candidates into reviewable objects that can support reproducible dry-lab screening and candidate prioritization before experimental follow-up.

## Why Delivery Evidence Needs a Commons

Delivery evidence is fragmented across assay types, biological contexts, molecule classes, label definitions, and source formats. A sequence labeled positive in one source may reflect a specific assay, payload context, organism, cell type, threshold, or reporting convention. Treating that label as universal biological truth can produce misleading benchmarks.

A dataset commons gives each dataset a public context record:

- where the data came from
- what input objects it contains
- what the labels mean
- what the labels do not mean
- what task family the data may support
- what metrics may be appropriate
- what release or reuse boundaries apply
- what review state the dataset has reached

The goal is not to flatten biology into one universal prediction task. The goal is to make each benchmark surface explicit enough to reproduce and critique.

## Scope of the Commons

The commons may include delivery-relevant dataset candidates across task families such as:

- BBB peptide benchmark surfaces
- CPP and membrane penetration benchmark surfaces
- localization and targeting proxy tasks
- RNA and mRNA delivery-adjacent tasks
- sequence-linked delivery evidence from public literature
- negative, ambiguous, or failed evidence where release rights and source context are clear

Each dataset should remain scoped to its source, label policy, assay context, and limitations. A dataset card may describe a dataset candidate before it becomes benchmark-ready.

The commons should prioritize reviewable public structure over bulk data accumulation. Raw row-level data should only be included when the source license, contributor rights, privacy posture, and release policy support public distribution.

## Dataset Cards

A dataset card is the primary contribution object for the commons.

Required fields should include:

- dataset name
- task family
- source and citation
- sequence type or input object
- label definition
- positive criteria
- negative criteria
- assay or evidence context
- inclusion and exclusion criteria
- known limitations
- suggested metrics
- allowed outputs or release posture
- contributor
- review status

Dataset cards should separate source claims from Permea interpretation. They should avoid strengthening a source beyond what the cited evidence supports.

## Benchmark Task Linkage

A dataset becomes more useful when it can be linked to an executable benchmark task.

Benchmark linkage should define:

- benchmark task name
- input schema
- label schema
- split policy
- baseline expectations
- metric set
- output artifacts
- non-claims
- provenance requirements

Not every dataset card should become an executable benchmark immediately. Some cards may remain as literature pointers, evidence-card collections, or benchmark candidates until label quality, source rights, and task boundaries are clear.

## Evidence Provenance

Every dataset card should preserve provenance.

Provenance may include:

- source paper, database, supplement, or repository
- source version or access date when relevant
- sequence identifiers or source identifiers
- label extraction method
- curation notes
- reviewer notes
- known transformations
- release boundary

Provenance should be strong enough for reviewers to understand how a label entered the commons. It should also make uncertainty visible. Unknown assay context, unclear negatives, duplicated sequences, derived labels, and mixed source conventions should be documented rather than hidden.

## Permissible Data Boundaries

Public commons contributions may include:

- public citations and source references
- public dataset cards
- public aggregate summaries
- public schemas, task definitions, and limitations
- row-level public data only when rights and release posture are clear

Public commons contributions should not include:

- private or proprietary sequences without release rights
- restricted row-level datasets
- sensitive candidate rankings
- partner-controlled data
- credentials or environment values
- private workflow notes
- unsupported clinical or therapeutic claims

When release status is unclear, contributors should provide a schema-level or aggregate-level description and request maintainer review before adding data.

## Quality Levels

The commons should distinguish evidence maturity.

| Level | Name | Meaning |
| --- | --- | --- |
| Level 0 | Source pointer | A potentially relevant source, dataset, or claim has been identified. |
| Level 1 | Evidence card draft | Source evidence has been converted into a structured draft object. |
| Level 2 | Dataset card proposal | A dataset candidate has source, label, task, and limitation context. |
| Level 3 | Review-ready dataset card | The card has enough detail for maintainer or community review. |
| Level 4 | Benchmark-linked dataset | The dataset is linked to a defined benchmark task and release posture. |
| Level 5 | Benchmark-ready dataset | The dataset has defined labels, splits, metrics, provenance, and output expectations. |
| Level 6 | Reproducible benchmark package | The dataset supports a documented run with outputs, metrics, and provenance. |

These levels describe documentation and reproducibility maturity. They do not imply wet-lab validation, clinical relevance, or universal delivery prediction.

## Contribution Path

Contributors can help the commons by:

- proposing a dataset card
- improving source attribution
- clarifying label definitions
- adding limitations or assay context
- linking a dataset card to a benchmark task
- drafting evidence cards from public sources
- submitting a reproduction report for a benchmark-linked dataset

Good contributions are narrow, source-aware, and explicit about uncertainty. They should make a dataset easier to review before making it larger.

## Support for Benchmark-First Delivery Engineering

The commons supports benchmark-first delivery engineering by turning source evidence into structured benchmark inputs.

It helps Permea answer:

- What task is this data suitable for?
- What does each label mean?
- What evidence level supports the label?
- What split policy is appropriate?
- What metrics summarize the task fairly?
- What outputs can be released publicly?
- What claims are outside the dataset boundary?

This structure supports dry-lab screening and evidence-backed prioritization before experimental follow-up. It also makes negative, ambiguous, and partial evidence easier to preserve in reusable form.

## Limitations and Non-Claims

The Delivery Dataset Commons does not solve delivery.

It does not claim wet-lab validation.

It does not claim clinical performance.

It does not claim universal prediction.

It does not claim that all sources, assays, or labels are comparable.

It does not claim that a benchmark-ready dataset proves transport, mechanism, safety, therapeutic effect, or generalization beyond its defined task.

The commons is a public technical foundation for organizing delivery evidence. Its value depends on source clarity, review discipline, reproducibility, and conservative interpretation.

## Closing

Delivery engineering needs more than isolated datasets.

It needs a commons where dataset evidence can become inspectable, benchmarkable, and reusable.
