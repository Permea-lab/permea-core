# Contributing to Permea Core

## Welcome and Project Scope

Permea Core is an open toolkit and benchmarks foundation for sequence-first delivery and mRNA expression engineering.

The project is benchmark-first, documentation-as-contract, and open-source-first. Contributions should improve the clarity, reproducibility, provenance, reviewability, or governance of Permea's technical surfaces.

Permea Core is not a claim of validated biological performance, clinical efficacy, universal delivery prediction, or production-grade drug delivery platform status.

## Permea Core vs Evidence Repos

Permea Core contains durable public operating standards:

- benchmark contracts
- result artifact schemas
- run manifest expectations
- evidence and claim-boundary rules
- reproducibility standards
- contributor and community governance
- dataset and public artifact policies
- release review policies

Evidence repositories, such as `permea-signal-ml`, contain project-specific evidence packages:

- manuscript and supplement drafts
- benchmark runs and result artifacts
- paper-specific source-to-claim audits
- review packets
- artifact manifests and release blockers

Do not move paper-specific evidence, restricted row-level data, or local orchestration context into Permea Core without prior review.

## Contribution Types

Useful contributions include:

- documentation improvements
- code that supports reproducible benchmark workflows
- benchmark contracts
- result artifact schemas
- run manifest and provenance improvements
- reproducibility tooling
- dataset and provenance policy improvements
- public-safe artifact policy improvements
- claim review and source-to-claim review
- dry-lab analysis that stays within documented evidence boundaries
- reviewer feedback on clarity, assumptions, or reproducibility

## What Not to Contribute Without Prior Discussion

Please open an issue before contributing:

- row-level restricted datasets
- unlicensed or unclear-license data
- private, confidential, or partner-controlled data
- secrets, credentials, API keys, tokens, or private keys
- human subject data or privacy-sensitive records
- biological validation claims
- wet-lab validation claims
- medical, therapeutic, or clinical claims
- claims that Permea has achieved AlphaFold-level performance, adoption, or standardization
- broad universal delivery prediction claims

If in doubt, do not upload the material. Open a minimal issue describing the question without exposing restricted content.

## Issue Guidelines

Good issues should include:

- the document, benchmark, schema, or workflow being discussed
- the current ambiguity or problem
- the proposed change or question
- any relevant repo path
- whether the issue touches data, artifacts, claims, or release readiness

Use conservative language for scientific issues. Distinguish observed repo facts from interpretation, policy decisions, and future work.

## PR Guidelines

Pull requests should:

- stay scoped to one document family or technical change
- explain why the change is needed
- list files changed
- describe any claim-boundary impact
- describe any dataset or artifact-release impact
- avoid unrelated formatting churn
- avoid adding data unless explicitly reviewed first

For benchmark or result-schema changes, include how the change affects provenance, rerunability, and comparison across runs.

## Claim Hygiene Checklist

Before submitting a contribution, check that it does not imply:

- completed wet-lab validation unless documented
- clinical efficacy
- therapeutic efficacy
- universal delivery prediction
- production-grade drug delivery platform status
- AlphaFold-level performance, adoption, or standardization
- dataset redistribution permission without source/license approval
- benchmark performance beyond the dataset, split, metric, and evidence level actually used

Permea may use "AlphaFold for Delivery" as an ambition or positioning phrase only. It must not be written as an achieved status.

Benchmark claims must remain scoped to:

- dataset
- split
- metric
- benchmark contract
- evidence level
- provenance state
- release boundary

## Dataset and Artifact Safety Checklist

Before adding any data or result artifact, confirm:

- the source and license are known
- redistribution terms are documented
- row-level records are allowed for public release
- private or partner-controlled data are not included
- secrets and credentials are not included
- generated artifacts do not reveal restricted row-level data
- rankings, predictions, split manifests, and group assignments are reviewed before public release

When source terms are unclear, use aggregate descriptions and path-level references rather than uploading row-level data.

## Review Process

Maintainers may review contributions for:

- technical correctness
- consistency with existing benchmark contracts
- reproducibility and provenance
- claim hygiene
- data and artifact safety
- public-readiness boundaries
- community conduct

Review may request narrower wording even when a stronger claim feels plausible. This is intentional; Permea prefers evidence-bounded claims.

## Authorship Note

Contribution credit and paper authorship are related but not automatic.

Software, documentation, benchmark, review, data, and scientific contributions may be recognized in different ways. Formal authorship criteria will be defined separately in a future authorship policy and may require manual review.

Do not assume a merged pull request creates paper authorship.

## Code of Conduct

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Security and Support

For sensitive disclosures, see [SECURITY.md](SECURITY.md).

For questions and support scope, see [SUPPORT.md](SUPPORT.md).
