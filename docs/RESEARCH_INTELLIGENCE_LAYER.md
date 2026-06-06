# Permea Research Intelligence Layer

Status: Public documentation

## Opening Thesis

Permea's Research Intelligence Layer is a structured layer over delivery literature, datasets, evidence cards, claims, benchmark summaries, and candidate explanations.

Its purpose is to make delivery evidence easier to inspect and reuse. It is not a replacement for scientific review, experimental validation, or expert judgment. It should preserve uncertainty, source context, and claim boundaries.

## What the Layer Organizes

The layer connects public research objects:

- papers and source records
- dataset cards
- evidence cards
- claims and citations
- benchmark tasks
- benchmark summaries
- candidate explanations
- limitation notes
- reproducibility records

The layer should help reviewers move from source material to structured evidence without losing context. It should make it easier to see which claim came from which source, which dataset supports which benchmark, and which candidate explanation is backed by which evidence objects.

## Paper-to-Evidence-Card Workflow

At the conceptual level, a paper-to-evidence-card workflow should:

1. Identify a public source.
2. Extract delivery-relevant entities, such as sequences, molecules, assays, barriers, contexts, and reported outcomes.
3. Preserve the source claim separately from any Permea interpretation.
4. Record citation, source section, and extraction notes.
5. Document limitations, uncertainty, and missing context.
6. Assign draft review status.
7. Promote the evidence card only after human scientific review.

Evidence cards should not strengthen the source claim. If a paper reports a context-specific assay result, the evidence card should keep that context attached to the claim.

## Claim-to-Source Checking

Claim-to-source checking links each public claim to supporting sources and evidence level.

Checks should ask:

- Is the source identifiable?
- Does the claim match the source language and context?
- Is the assay or dataset context preserved?
- Are limitations and uncertainty visible?
- Is the evidence level stated correctly?
- Does the claim avoid unsupported biological, clinical, or universal language?

This workflow helps prevent overinterpretation. It does not establish automated scientific truth.

## Candidate-to-Explanation Workflow

Candidate explanations should describe why a candidate was prioritized under a defined benchmark task.

A candidate-to-explanation workflow may include:

1. Candidate sequence or input object.
2. Benchmark task and dataset version.
3. Feature or descriptor summary.
4. Ranking or score context.
5. Relevant evidence cards.
6. Risk flags and uncertainty.
7. Non-claims and review status.
8. Exportable candidate report.

Candidate explanations support prioritization before experimental follow-up. They do not prove delivery, mechanism, safety, therapeutic effect, or clinical performance.

## Dataset-to-Dataset-Card Workflow

A dataset-to-dataset-card workflow should convert a public source or dataset candidate into a reviewable dataset card.

Core steps:

1. Identify the source and citation.
2. Define the input object and task family.
3. Document label meaning and label origin.
4. Describe positive and negative criteria.
5. Record assay context and biological context when known.
6. Document inclusion, exclusion, and deduplication rules.
7. State release posture and permissible outputs.
8. Mark review status and open questions.

Dataset cards should make a dataset easier to evaluate before it is used in a benchmark.

## Benchmark-to-Summary Workflow

A benchmark-to-summary workflow should turn run outputs into public-safe review summaries.

Summaries may include:

- benchmark task version
- dataset version
- split policy
- feature set
- baseline or model family
- aggregate metrics
- ranking behavior where applicable
- output artifact list
- limitations
- provenance notes
- claim boundaries

Aggregate benchmark summaries should not expose restricted row-level data. They should also avoid implying that metrics prove biological transport or therapeutic utility.

## Public-Safe Scope

The Research Intelligence Layer should remain public-safe by design.

It may include:

- public source references
- public evidence-card schemas
- public dataset-card schemas
- public benchmark-summary formats
- public claim-boundary checks
- aggregate benchmark summaries
- review status fields

It should not include:

- restricted row-level data without release approval
- private candidate sequences
- sensitive rankings
- proprietary source material
- credentials or secrets
- private execution context
- unsupported clinical or therapeutic claims

When in doubt, the layer should preserve the question in public-safe form and defer release until review.

## Relationship to Permea Core

Permea Core defines the public contracts for evidence objects, dataset cards, benchmark tasks, run manifests, and output packages.

The Research Intelligence Layer sits above those contracts. It helps connect source evidence to benchmark-ready objects and candidate explanations while keeping provenance and limitations attached.

It should be compatible with the Delivery Dataset Commons, Benchmark Execution Layer, contribution objects, and evidence packages such as sequence-first benchmark support repositories.

## Limitations and Non-Claims

The Research Intelligence Layer does not automate scientific truth.

It does not replace human scientific review.

It does not claim wet-lab validation.

It does not claim clinical validity or therapeutic effect.

It does not prove delivery, mechanism, safety, or generalization beyond a defined benchmark.

It does not turn literature mentions into benchmark-ready evidence without review.

Its role is to make evidence extraction, claim checking, candidate explanation, and benchmark summarization more structured and reproducible.

## Closing

Delivery research needs structured memory.

The Research Intelligence Layer is Permea's public specification for turning scattered sources into reviewable evidence objects, benchmark summaries, and bounded candidate explanations.
