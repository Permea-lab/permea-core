# Permea Contribution Objects

Status: Public documentation

## Purpose

Permea Core is an open execution layer for delivery engineering. Contributions should therefore be more structured than general suggestions or one-off files.

This document defines the public contribution objects that make delivery evidence easier to inspect, compare, reproduce, and extend.

## Why Contribution Objects Matter

Delivery evidence is fragmented across datasets, papers, assays, predictors, and internal workflows. A contribution object gives each proposed addition a common structure: source, task, label meaning, provenance, limitations, review status, and claim boundaries.

Structured contribution objects help Permea remain open without weakening scientific discipline. They make it possible to accept useful early contributions while still distinguishing draft evidence, benchmark-ready datasets, reproducible runs, and later external validation.

## Dataset Card

What it is: A structured description of a dataset or dataset candidate.

Who contributes it: Researchers, data curators, computational biologists, delivery scientists, and contributors who can document a public source clearly.

Required fields:

- dataset name
- task family
- source and citation
- sequence type or input object
- label definition
- positive criteria
- negative criteria
- assay context
- known limitations
- suggested metrics
- allowed outputs or release posture
- contributor
- review status

Review criteria:

- source attribution is clear
- label meaning is bounded and does not imply universal biological truth
- assay context is described when known
- limitations are explicit
- public/private data status is clear
- no unsupported validation or performance claim is made

## Benchmark Task

What it is: A proposed executable task that connects a dataset card to input schemas, label schemas, split policy, baseline models, metrics, outputs, and non-claims.

Required fields:

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

Metrics, split, and label expectations:

- labels should be treated as benchmark labels with provenance
- split policy should be explicit enough to reproduce
- metrics should match task type and class balance
- baseline models should be transparent before complex models are introduced
- outputs should include aggregate summaries and provenance

Review criteria:

- task boundary is clear
- dataset and label assumptions are inspectable
- metrics and baselines are appropriate for the task
- outputs support reproduction
- non-claims prevent overinterpretation

## Evidence Card

What it is: A structured source-backed evidence object extracted from a paper, database, supplement, or reviewed public source.

Required fields:

- source paper or database
- molecule or sequence reference
- barrier or task
- assay type
- cargo context
- organism or cell context
- reported outcome
- evidence strength
- limitations
- citation
- extraction method
- human review status

Source and citation expectations:

- cite the source clearly enough for reviewers to inspect
- separate the source claim from Permea interpretation
- preserve limitations, uncertainty, and assay context
- mark draft extractions as drafts until reviewed

Review criteria:

- source is identifiable
- extraction does not strengthen the original claim
- biological context is not omitted when claim-relevant
- evidence strength and limitations are explicit

## Run Manifest

What it is: A provenance record for a computational benchmark run.

Required fields:

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

Reproducibility expectations:

- enough configuration is recorded to rerun the analysis
- outputs are tied to a known task and dataset version
- deviations from expected commands or metrics are documented
- public outputs avoid restricted row-level artifacts unless release status is clear

## Feature Descriptor

What it is: A definition of a feature or descriptor used in a delivery benchmark.

Required fields:

- descriptor name
- biological or computational rationale
- input requirements
- calculation method
- units or value range where applicable
- implementation reference
- limitations

Documentation expectations:

- explain what the descriptor measures
- explain what it does not prove
- avoid causal mechanism claims from descriptor values alone
- include enough detail for reproducible feature extraction

### Example: GRAVY

GRAVY stands for **Grand Average of Hydropathy**. It is a sequence-derived
summary of residue hydropathy values, usually computed by averaging a
hydropathy scale such as Kyte-Doolittle across all residues in a peptide or
protein sequence.

For Permea-style benchmark work, a GRAVY descriptor note should include:

- **Input**: an amino-acid sequence with the alphabet and preprocessing policy
  made explicit
- **Calculation**: the hydropathy table used and the averaging rule
- **Interpretation**: higher values generally indicate a more hydrophobic
  sequence summary, while lower values indicate a more hydrophilic summary
- **Reproducibility**: the implementation reference, version, and any sequence
  normalization rules
- **Limits**: GRAVY is a coarse physicochemical summary, not direct evidence of
  transport, uptake mechanism, tissue penetration, or therapeutic effect

GRAVY can be useful as one transparent feature in delivery-related benchmark
analysis, especially when compared alongside charge, length, aromaticity, and
other sequence-derived descriptors. However, descriptor values alone should not
be treated as causal mechanism proof or as a substitute for assay context and
experimental validation.

## Baseline Model

What it is: A reproducible baseline implementation or configuration for a benchmark task.

Required fields:

- model family
- task
- input features
- training configuration
- split policy
- metrics
- output artifacts
- limitations

Evaluation expectations:

- compare against simple baselines when relevant
- report aggregate metrics with task context
- include provenance and configuration
- avoid claims beyond the dataset, split, and metrics used

## Candidate Report

What it is: An exportable prioritization summary for candidate sequences.

Public/private caution:

- candidate reports may include sensitive sequences, rankings, or row-level outputs
- public examples should use safe example inputs or approved public data
- private or proprietary candidate data should not be uploaded to public issues or PRs

Appropriate use:

- summarize candidate ranking under a defined benchmark task
- include feature profiles, evidence cards, risk flags, and limitations
- support prioritization before experimental follow-up
- avoid implying guaranteed delivery, therapeutic effect, or medical advice

## Reproduction Report

What it is: A report confirming or challenging a benchmark run.

Required fields:

- benchmark or task
- repository commit
- environment
- command run
- output artifacts
- observed metrics
- expected metrics if known
- deviations
- logs or excerpts
- reviewer notes

## Contribution Levels

| Level | Contribution | Meaning |
| --- | --- | --- |
| Level 0 | Literature pointer | A source or claim is suggested for review. |
| Level 1 | Evidence card draft | A source is converted into a structured evidence object. |
| Level 2 | Dataset card proposal | A dataset candidate is described with source, labels, and limitations. |
| Level 3 | Benchmark task proposal | A task is proposed with input schema, label schema, metrics, and outputs. |
| Level 4 | Reproducible run manifest | A benchmark run is submitted with provenance. |
| Level 5 | Community-reviewed benchmark | A task and run package pass community review. |
| Level 6 | Externally validated extension | Later evidence extends a benchmark direction beyond computational-only status. |

## Claim Boundaries

Contribution objects should preserve conservative evidence levels:

- computational evidence only unless otherwise stated
- candidate prioritization before experimental follow-up
- no wet-lab validation claim
- no clinical or therapeutic effect claim
- no universal prediction claim
- no state-of-the-art claim
- no claim of maturity comparable to AlphaFold

## Public / Private Data Caution

Public contributions should not include private or proprietary data unless the contributor has rights to share it.

Do not upload secrets, credentials, private sequences, partner-controlled data, restricted row-level datasets, or sensitive candidate rankings.

When release status is unclear, describe the proposed contribution at aggregate or schema level and ask maintainers for review.

## Next Steps for Contributors

1. Read [CONTRIBUTING.md](../CONTRIBUTING.md).
2. Choose the issue template matching the contribution object.
3. Keep the first proposal narrow and reviewable.
4. Include source attribution, limitations, and non-claims.
5. Open a PR only after the contribution object is clear enough to review.
