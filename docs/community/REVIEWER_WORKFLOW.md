# Reviewer Workflow

## 1. Purpose

This document defines Permea Core's initial reviewer workflow.

Reviewers help keep contributions technically useful, scientifically bounded, reproducible, and public-safe. Review is a project quality process; it does not imply external peer review or validation.

## 2. Reviewer Types

### Claim Reviewer

Checks wording against `docs/scientific-governance/CLAIM_REGISTRY.md` and `docs/EVIDENCE-LADDER.md`.

### Scientific Reviewer

Checks scientific framing, literature context, interpretation, limitations, and evidence-tier discipline.

### Reproducibility Reviewer

Checks rerun surface, environment capture, config, run manifest, artifact traceability, and reproducibility wording.

### Benchmark Reviewer

Checks benchmark contract, task definition, split, metric, baseline, result schema, and comparability.

### Dataset / Provenance Reviewer

Checks source, license, lineage, attribution, row-level status, derived artifact status, and release posture.

### Paper / Source-to-Claim Reviewer

Checks manuscript, supplement, README, citation, artifact, and release language alignment.

### Wet-Lab Protocol Reviewer

Checks proposed assay or protocol framing, controls, readout, limitations, and whether wet-lab language is appropriately provisional.

Wet-lab protocol review does not equal completed wet-lab validation.

## 3. Review Request Lifecycle

1. A contributor or maintainer identifies review need.
2. The request states review type, affected files, and decision needed.
3. The reviewer checks the relevant policy docs and artifact surface.
4. Findings are marked as blocking, non-blocking, clarification, or future work.
5. The contributor responds or revises.
6. The reviewer clears, narrows, or escalates findings.
7. The maintainer records unresolved blockers before merge or release.

## 4. Review Checklist by Reviewer Type

### Claim Reviewer Checklist

- What is the exact claim?
- Is it vision, hypothesis, literature context, computational evidence, benchmark result, reproducibility, wet-lab validation, or clinical claim?
- Does it name dataset, split, metric, model, artifact, and evidence level where needed?
- Does it avoid AlphaFold-level maturity, clinical efficacy, universal prediction, and production-grade platform claims?
- Does it align with README, paper, website, and release wording?

### Scientific Reviewer Checklist

- Is interpretation bounded by evidence?
- Are limitations visible?
- Are comparator or literature claims supported?
- Are dry-lab results separated from wet-lab validation?
- Are biological or translational implications appropriately cautious?

### Reproducibility Reviewer Checklist

- Is the code/config/data reference documented?
- Is a run manifest required and present where needed?
- Do result artifacts match the schema?
- Are aggregate and row-level reproducibility separated?
- Are missing rerun surfaces disclosed?

### Benchmark Reviewer Checklist

- Is the benchmark task defined?
- Are dataset, split, metric, model, and artifact fields clear?
- Are baselines and comparisons scoped correctly?
- Does the change preserve comparability or explain changes?
- Are imported vs regenerated artifacts separated?

### Dataset / Provenance Reviewer Checklist

- Is the data source identified?
- Are license, attribution, and redistribution terms known?
- Are row-level and aggregate artifacts separated?
- Are derived artifacts classified?
- Are restricted or partner-controlled records held?
- Is release permission documented where needed?

### Paper / Source-to-Claim Reviewer Checklist

- Does every material claim map to a source, citation, artifact, or evidence record?
- Do title, abstract, README, supplement, and release notes agree?
- Are unresolved source or license issues visible?
- Are data/code availability statements conservative?
- Does the work avoid public-readiness claims before approval?

### Wet-Lab Protocol Reviewer Checklist

- Is the assay context defined?
- Are controls, readouts, replicates, and limitations described?
- Is data ownership or release permission known?
- Are claims tied to documented experimental evidence?
- Is collaboration interest separated from validation?

## 5. How to Mark Findings

### Blocking

Must be resolved before merge or release.

Use for unsupported claims, unsafe artifact exposure, missing provenance, contradictory release state, or evidence-level overreach.

### Non-Blocking

Should be addressed but does not prevent scoped merge.

Use when the issue is minor, low-risk, and does not affect claim, data, release, or reproducibility safety.

### Clarification

Requires an answer before the reviewer can decide risk.

Use when evidence, source, scope, or release state is unclear.

### Future Work

Useful improvement outside the current change.

Future work must not be used to defer a blocking safety issue.

## 6. Evidence-Level Review

Reviewers should use `docs/EVIDENCE-LADDER.md`.

Computational results, benchmark results, reproducibility, literature plausibility, in vitro evidence, and stronger biological validation are different evidence levels.

A claim must not imply a stronger evidence level than documented.

## 7. Source-to-Claim Review

Source-to-claim review should map:

- claim text
- manuscript or doc location
- supporting citation or source
- supporting internal artifact, if any
- dataset and release posture
- evidence level
- unresolved caveats
- required wording changes

Unsupported claims should be narrowed, marked provisional, or removed.

## 8. Dataset / Release-Risk Review

Dataset and release-risk review should check:

- source identity
- source terms
- attribution requirements
- row-level artifact status
- derived artifact status
- public-safe classification
- release approval status
- security or sensitive exposure risk

Do not approve public release of restricted row-level artifacts without explicit permission and review.

## 9. Review Response Template

Use this structure when practical:

```text
Review type:
Files reviewed:
Decision: approve / request changes / block / clarify

Blocking findings:
- ...

Non-blocking findings:
- ...

Clarifications:
- ...

Future work:
- ...

Claim/data/release risk:
Evidence level:
Manual escalation needed:
```

## 10. Reviewer Escalation Path

Escalate to a maintainer when:

- blocking findings are disputed
- source/license status is unclear
- row-level artifact exposure is possible
- a claim affects public-readiness, validation, or clinical interpretation
- wet-lab or partner-controlled data are involved
- paper authorship, credit, or acknowledgement issues arise

Escalate to founder/manual approval when high-impact release, dataset, partner, public preprint, or authorship decisions remain unresolved.

## 11. What Review Does Not Imply

Project review does not imply:

- external peer review
- journal review
- independent replication
- external validation
- wet-lab validation
- clinical endorsement
- regulatory review
- dataset redistribution permission
- paper authorship

Reviewers should make this explicit when approving scoped dry-lab or documentation changes.

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Review does not equal peer review. Reviewer input does not equal external validation. Wet-lab protocol discussion does not equal wet-lab validation.
