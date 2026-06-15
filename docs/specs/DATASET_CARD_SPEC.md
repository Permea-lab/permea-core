# Dataset Card Spec

Status: Public specification

## Purpose

A dataset card is the public context record for a dataset or dataset candidate. It helps contributors describe source, labels, provenance, limitations, and benchmark readiness before the dataset is used in a Permea benchmark task.

Dataset cards support computational evidence and candidate prioritization before wet-lab work. They do not establish biological validation, clinical performance, or general delivery prediction.

## Required Fields

### Dataset Name

Provide a stable, human-readable dataset name.

Example:

```yaml
dataset_name: public_bbb_peptide_candidate_set
```

### Delivery Task

Describe the delivery-related task family the dataset may support.

Examples:

- BBB peptide prioritization
- cell-penetrating peptide benchmark
- localization proxy task
- RNA delivery-adjacent proxy task

### Biological Barrier or Proxy Task

Name the biological barrier, delivery context, or proxy task represented by the dataset.

Examples:

- blood-brain barrier
- membrane penetration
- subcellular localization
- targeting signal proxy

### Source / Citation

Identify the source clearly enough for review.

Include:

- paper, database, supplement, repository, or public record
- citation or URL
- source version or access date when useful

### License / Source Notes

State the public release posture and any known source restrictions.

Include:

- source license if known
- whether row-level data can be redistributed
- whether only aggregate or schema-level documentation is appropriate
- attribution requirements

### Sequence Type

Describe the sequence or input object.

Examples:

- peptide sequence
- protein sequence
- RNA sequence
- localization motif
- delivery-related descriptor input

### Label Schema

Define the label field or fields.

Include:

- label name
- allowed values
- label source
- whether labels are binary, multiclass, continuous, ranked, or categorical
- missing or ambiguous label policy

### Positive / Negative Definition

If applicable, define what counts as positive and negative.

Include:

- positive criteria
- negative criteria
- threshold or source rule if used
- ambiguous or excluded cases

### Assay / Source Context

Describe assay or source context when available.

Examples:

- assay type
- organism or cell context
- cargo or payload context
- experimental condition summary
- source claim context

If context is unknown, state that it is unknown rather than filling the gap with an inference.

### Dataset Readiness Level

Use a public readiness level.

| Level | Name | Meaning |
| --- | --- | --- |
| 0 | Source pointer | A potentially relevant source or dataset has been identified. |
| 1 | Evidence card draft | Source evidence has been converted into a draft evidence object. |
| 2 | Dataset card proposal | Source, labels, task, and limitations are described. |
| 3 | Review-ready dataset card | The card has enough detail for maintainer or community review. |
| 4 | Benchmark-linked dataset | The dataset is linked to a benchmark task and release posture. |
| 5 | Benchmark-ready dataset | Labels, splits, metrics, provenance, and outputs are defined. |
| 6 | Reproducible benchmark package | A documented run exists with outputs, metrics, and provenance. |

These levels describe documentation and reproducibility maturity. They do not imply wet-lab validation or clinical relevance.

### Known Limitations

List limitations that constrain interpretation.

Examples:

- unclear assay context
- class imbalance
- duplicate or near-duplicate sequences
- source-specific label conventions
- restricted release posture
- uncertain negative labels

### Recommended Metrics

Recommend metrics that fit the task and label schema.

Examples:

- ROC-AUC
- PR-AUC
- MCC
- F1
- precision at k
- Spearman correlation
- calibration summary

Metric choice should be tied to the benchmark task and class balance.

### Provenance Notes

Record how the dataset entered the benchmark surface.

Include:

- source identifier
- curation notes
- transformation notes
- reviewer notes
- version or date
- known exclusions

### Public Claim Boundary

A dataset card can support source transparency, dataset review, and benchmark readiness. It does not prove delivery, mechanism, safety, therapeutic effect, clinical performance, or broad prediction across delivery contexts.

## Minimal Example Skeleton

```yaml
dataset_name: public_bbb_peptide_candidate_set
delivery_task: bbb_peptide_prioritization
biological_barrier_or_proxy_task: blood_brain_barrier
source:
  citation: "Public source citation or URL"
  version_or_access_date: "2026-06-10"
license_source_notes:
  license: unknown
  redistribution: aggregate_or_schema_level_until_reviewed
sequence_type: peptide_sequence
label_schema:
  label_name: bbb_related_label
  label_type: binary
  allowed_values:
    - positive
    - negative
  missing_label_policy: exclude_until_reviewed
positive_negative_definition:
  positive: source_reports_bbb_related_positive_label
  negative: source_reports_bbb_related_negative_label
  ambiguous: hold_out_for_review
assay_source_context:
  assay_type: unknown
  organism_or_cell_context: unknown
dataset_readiness_level: 2
known_limitations:
  - source_context_requires_review
  - labels_are_benchmark_labels_not_biological_truth
recommended_metrics:
  - roc_auc
  - pr_auc
  - mcc
provenance_notes:
  source_identifier: source_id_or_url
  curation_notes: "Describe extraction and review status."
public_claim_boundary: "Computational benchmark context only; no wet-lab, clinical, universal, or solved-delivery claim."
```
