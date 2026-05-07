# Paper Alignment Policy

## 1. Purpose

This policy defines how Permea papers, preprints, READMEs, websites, supplements, release notes, and benchmark artifacts must stay aligned.

The goal is to prevent public-facing materials from making claims that exceed the evidence, dataset rights, reproducibility state, or release approval status.

## 2. Scope

This policy applies to:

- Permea Core README and docs
- evidence repository READMEs
- manuscripts
- preprints
- supplements
- public-safe artifact manifests
- benchmark reports
- source-to-claim reviews
- release notes
- websites, decks, and outreach materials controlled by Permea

## 3. Paper / Preprint / README Alignment Principle

Public materials must describe the same claim state.

If a manuscript says a package is internal-review only, the README, website, or release notes must not imply public submission readiness. If the README describes a benchmark as narrow and exploratory, the paper must not describe it as broad validation.

## 4. Source-to-Claim Alignment Rule

Every material scientific or benchmark claim should map to:

- a source citation
- a benchmark contract
- a dataset/source record
- a run manifest
- a result artifact
- a public-safe artifact manifest
- a documented evidence level
- or an explicit future ambition

Unsupported claims should be narrowed, marked as provisional, or removed before public release.

## 5. Claim Registry Dependency

Claim language should follow `docs/scientific-governance/CLAIM_REGISTRY.md`.

The claim registry controls:

- allowed claim classes
- restricted claims requiring evidence
- prohibited claims
- AlphaFold-for-Delivery usage
- benchmark-scoped claim requirements
- README / paper / website alignment expectations

## 6. Evidence Ladder Dependency

Claim strength should follow `docs/EVIDENCE-LADDER.md`.

Computational evidence, reproducible benchmark evidence, literature-grounded plausibility, in vitro evidence, and stronger validation are different evidence levels. A paper must not collapse these levels into a stronger claim.

## 7. Benchmark Contract Dependency

Benchmark result claims should follow `docs/BENCHMARK-CONTRACT.md`.

Each benchmark claim should state the task, dataset, split policy, metrics, model, and provenance context needed to interpret the result.

## 8. Result Artifact Schema Dependency

Result-supported claims should be traceable to artifacts consistent with `docs/RESULT-ARTIFACT-SCHEMA.md`.

Metrics, predictions, rankings, summaries, figures, and manifests should not be presented as interchangeable. Row-level artifacts require release review before public exposure.

## 9. Dataset / Public-Safe Artifact Dependency

Dataset and artifact wording should follow:

- `docs/scientific-governance/DATASET_POLICY.md`
- `docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md`

If row-level data or derived artifacts are blocked, the manuscript, supplement, README, and release notes must say so consistently.

## 10. Required Alignment Checks

Before public release, check:

- title: does it avoid overclaiming scope or validation?
- abstract: does it match evidence level and dataset limits?
- README claims: do they match manuscript and release state?
- metrics: are dataset, split, metric, model, artifact, and evidence level stated?
- dataset scope: are source, lineage, and redistribution limits visible?
- split protocol: is evaluation described consistently?
- limitations: are dataset, reproducibility, and validation limits explicit?
- data/code availability: does wording distinguish code, aggregate artifacts, and row-level data?
- supplement: does it avoid exposing restricted row-level artifacts?
- release notes: do they match the approved release decision?

## 11. Prohibited Mismatches

Do not allow:

- paper says Hold but README says ready
- manuscript says internal-review only but website implies public preprint readiness
- benchmark-limited result described as general performance
- dry-lab result described as wet-lab validation
- literature rationale described as experimental confirmation
- row-level data treated as publicly releasable without review
- aggregate metrics described as full reproducibility if row-level data are blocked
- code availability described as dataset availability
- preprint release implied before public release gates pass

## 12. Paper Versioning Policy

Paper drafts should use explicit version labels.

Recommended states:

- draft
- internal review
- public-safe candidate
- preprint candidate
- released
- corrected / withdrawn

Older manuscript versions should not be overwritten unless the repo has a deliberate archival policy. Version-specific audits should remain traceable to the draft they reviewed.

## 13. Preprint Readiness Gate

A preprint cannot be marked ready until:

- source-to-claim review is complete
- dataset/source/license status is documented
- row-level artifact release status is decided
- public-safe artifact manifest is complete
- supplement/export package is reviewed
- README and release notes are aligned
- claim registry review passes
- manual/founder/maintainer approval is recorded where required

Until these gates pass, status should remain Hold / not submission-ready.

## 14. Reviewer / Source-to-Claim Review Process

Paper reviewers should check:

- every major claim has a source or artifact
- direct evidence and adjacent context are separated
- benchmark metrics are interpreted conservatively
- dataset terms are not overstated
- row-level artifacts are not exposed without permission
- limitations match the evidence level
- README and paper claims are synchronized

Source-to-claim reviews should record unresolved claims rather than silently smoothing them over.

## 15. Update Process

Update this policy when:

- claim registry rules change
- evidence ladder levels change
- dataset policy changes
- release review gates change
- paper versioning practices change
- a mismatch is found between paper, README, website, or release language

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Public release must not include row-level restricted artifacts unless explicit permission and review are documented.
