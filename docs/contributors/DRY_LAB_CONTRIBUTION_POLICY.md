# Dry-Lab Contribution Policy

## 1. Purpose

This document defines Permea Core's initial dry-lab contribution policy.

Dry-lab contributions are essential to Permea's benchmark-first scientific infrastructure, but they must remain bounded by reproducibility, provenance, dataset, and claim-hygiene requirements.

## 2. Dry-Lab-First Status

Permea is dry-lab-first today.

This means current public work emphasizes:

- computational benchmarks
- sequence-first analysis
- provenance-aware artifacts
- reproducible workflows
- source-to-claim review
- public-safe artifact policies

Dry-lab-first does not mean wet-lab validation has been completed.

## 3. Accepted Dry-Lab Contribution Types

Accepted dry-lab contributions include:

- feature extraction
- benchmark contracts
- split/metric review
- model baselines
- reproducibility scripts
- source-to-claim review
- artifact schema validation
- dataset/provenance documentation
- literature landscape review

Contributions should improve inspection, rerunability, interpretation, or claim discipline.

## 4. Required Metadata for Dry-Lab Contributions

Dry-lab contributions should document:

- contributor name or handle
- contribution type
- affected files or artifacts
- benchmark id, if relevant
- dataset reference, if relevant
- source references, if relevant
- code revision, if relevant
- config or command, if relevant
- result artifact paths, if relevant
- claim-boundary impact
- dataset/release impact

If metadata are missing, state the limitation.

## 5. Reproducibility Requirements

Dry-lab work should follow `docs/scientific-governance/REPRODUCIBILITY_GUIDE.md`.

Benchmark-grade contributions should provide:

- code or documented method
- configuration or command
- dataset reference
- run manifest
- result artifact list
- environment notes
- known limitations

Reproducibility claims should not be made if the rerun surface is incomplete.

## 6. Result Artifact Requirements

Result artifacts should align with `docs/RESULT-ARTIFACT-SCHEMA.md`.

Where relevant, contributors should distinguish:

- aggregate metrics
- aggregate figures
- summaries
- manifests
- row-level predictions
- rankings
- split manifests
- exploratory outputs

Row-level artifacts require release review before public exposure.

## 7. Claim Hygiene Requirements

Dry-lab contributions must follow `docs/scientific-governance/CLAIM_REGISTRY.md` and `docs/EVIDENCE-LADDER.md`.

Benchmark claims must identify:

- dataset
- split
- metric
- model
- artifact
- evidence level

Avoid broad claims from narrow computational evidence.

## 8. Dataset / Public-Safe Artifact Restrictions

Dry-lab contributors must follow:

- `docs/scientific-governance/DATASET_POLICY.md`
- `docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md`

Do not contribute without prior review:

- row-level restricted datasets
- unlicensed datasets
- row-level labels
- row-level predictions
- ranking tables
- split manifests
- group assignments
- leakage tables
- raw upstream mirrors
- private or partner-controlled data
- secrets or credentials

Use aggregate summaries and path-level references when row-level release is unresolved.

## 9. PR Review Path

Dry-lab pull requests should be reviewed for:

- technical correctness
- benchmark contract alignment
- reproducibility
- result artifact traceability
- dataset/provenance status
- public-safe artifact status
- claim hygiene
- paper/release alignment when relevant

High-risk PRs may require claim, dataset, reproducibility, paper, or manual approval before merge.

## 10. When Dry-Lab Contribution May Become Paper Contribution

A dry-lab contribution may support paper authorship consideration when it materially affects a specific manuscript through:

- central benchmark design
- substantial analysis
- key method implementation
- data curation/provenance work
- major result artifact generation
- substantive interpretation
- manuscript drafting or revision
- source-to-claim accountability

Paper contribution and authorship require the authorship policy and final manual approval.

## 11. What Dry-Lab Contribution Cannot Claim

Dry-lab contribution cannot claim:

- wet-lab validation
- clinical efficacy
- therapeutic efficacy
- universal prediction
- generalizable biological delivery
- production-grade drug delivery platform status
- dataset redistribution permission without source/license approval

Dry-lab evidence may support bounded benchmark or candidate-prioritization claims only when scoped to the documented dataset, split, metric, model, artifact, and evidence level.

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Dry-lab contributions do not equal biological validation. Wet-lab collaboration interest does not equal wet-lab validation.
