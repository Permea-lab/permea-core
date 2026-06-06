# Permea Frontier Model Tool Layer

Status: Public documentation

## Opening Thesis

The Frontier Model Tool Layer is a future-facing interface and specification layer for sequence-first delivery engineering.

It describes how model-assisted tools may eventually interact with Permea Core contracts for datasets, benchmarks, evidence cards, candidate reports, and reproducibility checks. It does not claim that model outputs are scientific truth, experimental validation, or clinical evidence.

The layer should make assistive tools more traceable, reviewable, and bounded by public evidence.

## Purpose

Permea Core defines public technical contracts for delivery engineering. Future tool surfaces should call those contracts rather than inventing separate workflows for each interface.

The Frontier Model Tool Layer is intended to define:

- what tool actions are allowed
- what inputs and outputs should look like
- what provenance must be recorded
- what evidence is required before a claim is shown
- what review status applies to generated artifacts
- what information must never be exposed publicly

This layer should support researcher productivity without weakening scientific discipline.

## Potential Tool Capabilities

Future tools may support:

- sequence feature extraction
- dataset card generation
- benchmark preparation
- candidate prioritization reports
- evidence card drafting
- reproducibility checks
- claim-boundary review
- benchmark-summary drafting

These capabilities should be assistive. They should prepare structured artifacts for review, not bypass review.

## Sequence Feature Extraction

Tool surfaces may help compute or summarize sequence-derived descriptors used by benchmark tasks.

Expected boundaries:

- descriptor definitions should be documented
- feature calculations should be reproducible
- feature values should not be treated as causal mechanism proof by themselves
- feature outputs should link to the benchmark task that uses them
- candidate-level outputs should respect data release posture

## Dataset Card Generation

Tool surfaces may help draft dataset cards from public sources or contributor-provided metadata.

Expected boundaries:

- sources and citations must remain attached
- label definitions must be explicit
- unknown assay context should be marked unknown
- release posture must be recorded
- generated cards should begin as drafts
- human review is required before benchmark-ready status

## Benchmark Preparation

Tool surfaces may help prepare benchmark task definitions, run manifests, and configuration summaries.

Expected boundaries:

- task versions should be explicit
- dataset versions should be explicit
- split policies should be documented
- baseline expectations should be preserved
- output artifacts should follow Permea Core schemas
- unsupported claims should be excluded from generated summaries

## Candidate Prioritization Reports

Tool surfaces may help assemble candidate reports for sequence-first dry-lab screening.

Expected boundaries:

- reports should name the benchmark task and dataset version
- rankings should be described as prioritization under a defined task
- evidence cards and feature summaries should be linked where relevant
- uncertainty and risk flags should be visible
- private or sensitive candidate data should not be exposed in public artifacts
- reports should not imply guaranteed delivery or therapeutic effect

## Evidence Card Drafting

Tool surfaces may help draft evidence cards from public literature, databases, or contributor notes.

Expected boundaries:

- the original source claim must remain separate from interpretation
- citations must be traceable
- biological context should be preserved
- limitations should be explicit
- extraction confidence and review status should be recorded
- draft evidence cards require human scientific review

## Reproducibility Checks

Tool surfaces may help check whether a benchmark package contains the expected files and provenance.

Checks may include:

- benchmark task version exists
- dataset version exists
- run manifest is present
- metrics are present
- output artifacts are listed
- configuration or feature set is recorded
- claim boundaries are included
- public/private release status is clear

These checks improve review readiness. They do not prove biological validity.

## Guardrails

All model-assisted outputs should follow these guardrails:

- model outputs are assistive
- human scientific review is required
- no unsupported biological claims
- no clinical claims
- no private data leakage
- no closed or untraceable evidence
- no claim that benchmark metrics prove transport, mechanism, safety, or therapeutic effect
- no claim that candidate ranking guarantees experimental performance
- no release of restricted row-level data without approval

The layer should prefer incomplete but traceable artifacts over polished artifacts with unclear evidence.

## Relationship to Permea Core

Permea Core supplies the contracts:

- dataset cards
- evidence cards
- benchmark tasks
- run manifests
- result artifacts
- contribution objects
- public-safe release policies

The Frontier Model Tool Layer should sit on top of those contracts. It should not create a parallel evidence standard.

## Relationship to Benchmarks

Tool-assisted workflows should remain benchmark-first.

A generated candidate report, evidence card, or benchmark summary should identify the relevant task, dataset, metric set, provenance, and limitations. If a tool cannot identify those elements, the output should remain draft or exploratory.

## Relationship to the Delivery Dataset Commons

The Delivery Dataset Commons provides source-aware dataset cards and evidence provenance.

The Frontier Model Tool Layer may help draft or check those objects, but it should not promote a dataset to benchmark-ready status without review.

## Relationship to Evidence Packages

Sequence-first evidence packages can provide concrete benchmark runs, feature sets, outputs, and provenance records.

The Frontier Model Tool Layer should be able to consume those public artifacts to draft explanations, summaries, and checks. It should preserve the package's claim boundaries and should not generalize beyond the defined benchmark task.

## Limitations and Non-Claims

The Frontier Model Tool Layer does not claim that model-assisted output is correct by default.

It does not claim wet-lab validation.

It does not claim clinical performance.

It does not claim universal prediction.

It does not claim that delivery is solved.

It does not replace scientific review, benchmark execution, dataset curation, or experimental follow-up.

Its role is to define how future assistive interfaces can remain traceable, public-safe, benchmark-aware, and scientifically bounded.

## Closing

Frontier tools are useful only when they are grounded in evidence, provenance, and review.

Permea's tool layer should make delivery engineering faster without making claims less disciplined.
