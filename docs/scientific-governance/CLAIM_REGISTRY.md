# Claim Registry

## 1. Purpose

This document defines the first Permea Core claim registry. Its purpose is to keep project statements tied to evidence, provenance, and release boundaries.

The registry applies to README text, docs, websites, manuscripts, issue comments, release notes, benchmark reports, and outreach material managed by Permea.

## 2. Claim Registry Principle

Every public-facing claim should be traceable to one of the following:

- a project principle
- a benchmark contract
- a result artifact
- a run manifest
- a dataset/source record
- a literature source
- a documented experimental result
- an explicit future ambition

If the supporting surface is missing, the claim should be narrowed, marked as provisional, or removed.

## 3. Allowed Claim Classes

### Vision / Ambition

Vision claims describe what Permea is trying to build. They must not be written as achieved performance.

Allowed example:

- "Permea is building toward an open benchmark-first foundation for sequence-first delivery engineering."

### Hypothesis

Hypothesis claims describe a testable possibility. They require cautious wording.

Allowed example:

- "Sequence-derived features may contain signal relevant to a specific delivery-related benchmark."

### Literature-Supported Rationale

Literature-supported claims describe background context grounded in external sources. They should cite or reference the supporting source.

Allowed example:

- "Biological barriers such as the BBB are important delivery constraints for large-molecule therapeutics."

### Computational Evidence

Computational evidence claims describe model outputs, exploratory analyses, or computational signal. They do not establish biological truth.

Allowed example:

- "This analysis detected computational signal in the evaluated dataset and split."

### Benchmark-Scoped Result

Benchmark-scoped result claims describe metrics tied to a benchmark contract, model, dataset, split, artifact, and evidence level.

Allowed example:

- "Model X achieved metric Y on dataset Z under split policy S, with artifacts A and evidence level L."

### Reproducibility Claim

Reproducibility claims describe whether a workflow can be rerun from documented code, data references, config, and manifests.

Allowed example:

- "This run is reproducible from the recorded code revision, config reference, dataset reference, and result manifest."

### Wet-Lab Validation Claim

Wet-lab validation claims require documented experimental evidence. They must name the assay context and limits.

Current default:

- not allowed unless documented in an approved evidence surface.

### Translational / Clinical Claim

Translational and clinical claims require appropriate evidence and review. Permea Core does not currently support clinical efficacy claims.

Current default:

- prohibited unless explicitly validated and approved through a future release process.

## 4. Current Allowed Permea Claims

Current Permea Core claims may state that:

- Permea Core is an open toolkit and benchmarks foundation.
- Permea Core is benchmark-first and open-source-first.
- Permea Core defines repository-level contracts for benchmark tasks, result artifacts, provenance, and evidence interpretation.
- Permea Core is intended to make future work easier to inspect, compare, and extend.
- Benchmark evidence is not equivalent to biological validation.
- Current project claims must remain scoped to documented evidence level.

## 5. Restricted Claims Requiring Evidence

The following require specific support before use:

- model performance claims
- benchmark superiority claims
- reproducibility claims
- dataset reuse or redistribution claims
- biological mechanism claims
- wet-lab validation claims
- public release readiness claims
- paper/preprint readiness claims
- partner or collaborator claims

Each claim must identify its evidence surface before publication.

## 6. Prohibited Claims Unless Explicitly Validated

Do not claim:

- completed wet-lab validation unless documented
- clinical efficacy
- therapeutic efficacy
- universal delivery prediction
- production-grade drug delivery platform status
- AlphaFold-level performance, adoption, or standardization
- dataset redistribution permission without source/license approval
- leakage-free status unless the audit and scope are explicitly documented
- robust generalization unless the benchmark and external validation evidence support it

## 7. "AlphaFold for Delivery" Usage Rule

"AlphaFold for Delivery" may be used only as ambition or positioning.

Allowed:

- "Permea is motivated by the long-term ambition of building open infrastructure for delivery engineering."
- "AlphaFold for Delivery may describe the scale of ambition, not achieved maturity."

Not allowed:

- "Permea is the AlphaFold of delivery."
- "Permea has achieved AlphaFold-level performance."
- "Permea is the field standard for delivery prediction."

## 8. Benchmark-Scoped Claim Rule

Every result claim must specify:

- dataset
- split
- metric
- model
- artifact
- evidence level

A benchmark claim without these fields is incomplete and should not be used as a public performance claim.

## 9. README / Paper / Website Alignment Rule

README, paper, website, release-note, and outreach claims must remain aligned.

If a manuscript narrows a claim, the README and website should not keep broader wording. If a release policy blocks an artifact, no public text should imply that artifact is available.

## 10. Claim Review Checklist

Before publishing or merging a claim, check:

- What is the exact claim?
- Is it vision, hypothesis, literature context, computational evidence, benchmark result, reproducibility, wet-lab validation, or clinical claim?
- What evidence supports it?
- Does it name dataset, split, metric, model, artifact, and evidence level where needed?
- Does it imply more than the evidence supports?
- Does it conflict with dataset/source/license limits?
- Does it conflict with README, manuscript, or release wording?
- Does it require founder, maintainer, legal, partner, or manual approval?

## 11. Examples of Acceptable and Unacceptable Wording

Acceptable:

- "Permea Core defines benchmark and provenance standards for sequence-first delivery work."
- "Benchmark evidence may support bounded candidate-prioritization claims."
- "This result is scoped to the documented dataset, split, model, metric, and artifact."
- "Dataset redistribution remains unresolved until source/license review is complete."

Unacceptable:

- "Permea predicts delivery universally."
- "Permea is clinically validated."
- "Permea has wet-lab validated these candidates" unless documented.
- "The dataset can be redistributed" unless explicitly approved.
- "Permea is the AlphaFold of delivery" as an achieved status.

## 12. Update Process

This registry should be updated when:

- a new benchmark family is added
- a manuscript changes public claim language
- a dataset or release policy changes
- a wet-lab result changes the evidence tier
- README, website, or outreach wording changes
- maintainers identify repeated claim-risk patterns

Updates should preserve conservative wording and should not make final legal, clinical, or validation conclusions without appropriate review.
