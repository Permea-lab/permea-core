# Maintainer Guide

## 1. Purpose

This guide defines initial maintainer expectations for Permea Core.

Maintainers protect repo health, contribution quality, claim discipline, dataset/release boundaries, and public-safe operating practice.

## 2. Maintainer Responsibilities

Maintainers are responsible for:

- triaging issues and pull requests
- keeping changes scoped to the correct repo
- enforcing contribution and code-of-conduct expectations
- checking whether a change affects claims, datasets, artifacts, releases, or paper alignment
- requesting appropriate reviewers
- preventing unsupported public claims
- preventing unsafe release of restricted data or sensitive artifacts
- preserving benchmark and result schema consistency
- recording significant decisions
- merging changes only after required checks pass

## 3. Maintainer Non-Responsibilities

Maintainers are not expected to:

- provide medical or clinical advice
- make legal conclusions about source licenses, IP ownership, employment, or institutional policy
- approve paper authorship automatically
- validate wet-lab claims without documented evidence
- guarantee dataset redistribution permission
- guarantee that dry-lab results generalize biologically
- act as sole approver for high-impact release decisions unless explicitly assigned

When these topics arise, maintainers should narrow claims, hold release, and escalate.

## 4. Review Checklist by PR Type

### Routine Docs / Code

- Does the change stay within repo scope?
- Does it avoid changing public scientific claims?
- Does it avoid touching datasets, row-level artifacts, or public release state?
- Does it follow `CONTRIBUTING.md`?

### Benchmark / Schema

- Does the change align with `docs/BENCHMARK-CONTRACT.md`?
- Does it preserve result artifact traceability?
- Does it affect run manifest requirements?
- Does it require a reproducibility reviewer?

### Dataset / Provenance

- Does the change involve source datasets, derived data, row-level records, labels, predictions, rankings, split manifests, or partner data?
- Does it follow `docs/scientific-governance/DATASET_POLICY.md`?
- Is source/license/redistribution status explicit?
- Are row-level artifacts held unless permission is documented?

### Claim-Changing

- Does the change follow `docs/scientific-governance/CLAIM_REGISTRY.md`?
- Does each result claim state dataset, split, metric, model, artifact, and evidence level?
- Does it avoid overstating validation, clinical relevance, or generalization?
- Does it need source-to-claim review?

### Paper / Release

- Does the change align with `docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md`?
- Does it pass the relevant release gates in `docs/release/RELEASE_REVIEW_PROCESS.md`?
- Does it need the public checklist in `docs/release/PUBLIC_RELEASE_CHECKLIST.md`?

## 5. Required Gates

### Claim Gate

Use `docs/scientific-governance/CLAIM_REGISTRY.md`.

Block or narrow claims that exceed evidence.

### Data / Provenance Gate

Use `docs/scientific-governance/DATASET_POLICY.md`.

Hold row-level or source-derived artifacts when source/license status is unresolved.

### Reproducibility Gate

Use `docs/scientific-governance/REPRODUCIBILITY_GUIDE.md`.

Do not allow reproducibility claims without code, config, data references, manifests, result artifacts, and limitations.

### Benchmark / Result Gate

Use `docs/BENCHMARK-CONTRACT.md`, `docs/RESULT-ARTIFACT-SCHEMA.md`, and `docs/RUN-MANIFEST-SCHEMA.md`.

Benchmark claims must stay tied to the benchmark surface.

### Paper Alignment Gate

Use `docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md`.

README, manuscript, supplement, website, release notes, and source-to-claim records must not contradict each other.

### Public-Safe Artifact Gate

Use `docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md`.

Do not publish restricted row-level artifacts without explicit permission and review.

## 6. How to Handle Row-Level Data Submissions

If a submission includes row-level datasets, labels, feature tables, predictions, rankings, split manifests, group assignments, leakage tables, raw upstream mirrors, or partner data:

1. Do not merge or publish by default.
2. Ask the contributor to identify source, license, attribution, and redistribution status.
3. Request dataset/provenance review.
4. Request public-safe artifact review.
5. Prefer aggregate summaries or path-level descriptions until permission is documented.
6. Escalate unresolved cases to founder/manual approval.

Do not infer redistribution permission from article availability or public download pages.

## 7. How to Handle Claim-Changing PRs

For claim-changing pull requests:

1. Identify the exact claim.
2. Classify it under the claim registry.
3. Ask for supporting source, dataset, metric, artifact, or evidence level.
4. Check README, paper, website, and release alignment.
5. Narrow, mark provisional, or remove unsupported claims.
6. Request claim review when the change affects public-facing language.

## 8. How to Handle Benchmark-Changing PRs

For benchmark-changing pull requests:

1. Identify affected task, dataset, split, metric, model, and artifact fields.
2. Check benchmark contract compatibility.
3. Check run manifest and result artifact schema implications.
4. Ask whether existing results become stale or incomparable.
5. Require limitations and migration notes where needed.

## 9. How to Handle Wet-Lab Claims

Wet-lab-related language requires caution.

If a PR references experimental data, assay results, validation, biological performance, in vivo findings, therapeutic effect, or clinical relevance:

1. Confirm documented experimental evidence exists.
2. Confirm assay context, controls, readout, limitations, and evidence level are stated.
3. Request wet-lab protocol or scientific review.
4. Request dataset/provenance review for contributed data.
5. Check partner, confidentiality, attribution, and release constraints.
6. Escalate unresolved claims before merge or release.

Wet-lab protocol discussion does not equal wet-lab validation.

## 10. How to Request Additional Reviewers

Ask for additional reviewers when a change touches:

- claim boundaries
- scientific interpretation
- reproducibility
- benchmark contracts
- dataset/provenance
- paper/source-to-claim alignment
- wet-lab protocol or assay claims
- public release
- security or sensitive exposure

The review request should state:

- review type
- affected files
- decision needed
- known blockers
- requested deadline, if any

## 11. Merge Guidance

Before merging, maintainers should confirm:

- only intended files changed
- required reviewers have responded
- blocking findings are resolved or explicitly deferred
- release state is not overstated
- no restricted or sensitive artifacts are exposed
- no unsupported claims were introduced
- recordkeeping is adequate for the change risk

Do not merge high-risk changes only because they are urgent.

## 12. Release Approval Handoff

Maintainers preparing a release should hand off:

- release type
- release state
- included files
- excluded files
- claim review status
- dataset/provenance review status
- public-safe artifact review status
- reproducibility review status
- paper alignment status
- remaining blockers
- manual approval status

Use `docs/release/RELEASE_REVIEW_PROCESS.md`.

## 13. Maintainer Conduct Expectations

Maintainers should:

- model respectful open scientific disagreement
- enforce `CODE_OF_CONDUCT.md`
- avoid public speculation about sensitive disputes
- ask for narrower wording when evidence is insufficient
- avoid promising authorship, release approval, validation, or dataset availability outside policy
- correct mistakes transparently and in public-safe terms

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.

Review does not equal peer review. Reviewer input does not equal external validation. Wet-lab protocol discussion does not equal wet-lab validation.
