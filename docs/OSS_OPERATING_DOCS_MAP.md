# Permea Core OSS Operating Docs Map v0.1

## 1. Purpose

This map defines the target documentation architecture for Permea Core as the public OSS operating foundation for Permea.

Permea Core should define the durable open scientific operating layer for:

- OSS governance
- contributor workflow
- dry-lab contribution
- wet-lab collaboration
- authorship and contributor credit
- scientific evidence management
- benchmark contracts
- result artifact schemas
- dataset policy
- public-safe artifact policy
- paper/preprint alignment
- derivative project governance
- release review
- reproducibility
- claim hygiene

This document is a planning map. It does not itself implement every policy.

## 2. Current Repo Role

Permea Core is the public technical foundation for sequence-first delivery and mRNA expression engineering. It should remain the durable standards, contracts, and governance repository for the broader Permea ecosystem.

Current role:

- define benchmark-first project principles
- define reusable benchmark and result artifact contracts
- define evidence and claim-boundary standards
- provide a stable foundation for evidence repos and derivative projects

Current non-role:

- not a claim of validated biological performance
- not a public proof of universal delivery prediction
- not a production-grade drug delivery platform
- not the first-paper evidence repository

## 3. Permea-Core vs Permea-Signal-ML vs Local-Only Context Boundaries

### Permea Core

Permea Core should contain durable public operating standards:

- project governance
- contributor policy
- scientific claim and evidence policy
- benchmark contracts
- dataset and artifact release policy
- reproducibility standards
- derivative project rules
- release review process

### Permea Signal ML

`permea-signal-ml` should remain the first BBB evidence/paper package repository:

- manuscript and supplement drafts
- BBB-related benchmark artifacts
- source-to-claim audits
- public-safe artifact manifests for the first paper
- paper-specific release blockers
- paper-specific review packets

### Private Local Operator Context

Private local operator context should remain outside public repos.

It may contain project memory, local operating notes, and nonpublic coordination rules. It must not be committed.

## 4. Existing Docs Inventory

Existing root-level docs:

- `README.md`
- `LICENSE`
- `MANIFESTO.md`

Existing core docs:

- `docs/SPEC.md`
- `docs/DD-ARCHITECTURE.md`
- `docs/DELIVERY-TAXONOMY.md`
- `docs/EVIDENCE-LADDER.md`
- `docs/BENCHMARK-CONTRACT.md`
- `docs/RESULT-ARTIFACT-SCHEMA.md`
- `docs/RUN-MANIFEST-SCHEMA.md`
- `docs/ROADMAP.md`

Existing ADRs:

- `docs/adr/ADR-0001-open-source-first.md`
- `docs/adr/ADR-0002-benchmark-first.md`

## 5. Missing Docs Inventory

Missing root-level OSS docs:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `SUPPORT.md`
- `CITATION.cff`

Missing scientific governance docs:

- `CLAIM_REGISTRY.md`
- `DATASET_POLICY.md`
- `PUBLIC_SAFE_ARTIFACT_POLICY.md`
- `PAPER_ALIGNMENT_POLICY.md`
- `REPRODUCIBILITY_GUIDE.md`

Missing community and contributor docs:

- `COMMUNITY_GOVERNANCE.md`
- `MAINTAINER_GUIDE.md`
- `REVIEWER_WORKFLOW.md`
- `CONTRIBUTOR_LEVELS.md`
- `AUTHORSHIP_POLICY.md`
- `DRY_LAB_CONTRIBUTION_POLICY.md`
- `WET_LAB_COLLABORATION_POLICY.md`

Missing derivative and release docs:

- `DERIVATIVE_PROJECT_POLICY.md`
- `RELEASE_REVIEW_PROCESS.md`

Optional future docs:

- `MODEL_CARD.md`
- `DATASET_CARD.md`

## 6. Target Root-Level Docs

Root-level docs should orient outside contributors quickly:

- `README.md` - project overview and document index
- `LICENSE` - software/content license
- `CONTRIBUTING.md` - how to contribute
- `CODE_OF_CONDUCT.md` - participation standards
- `SECURITY.md` - vulnerability and sensitive-data reporting
- `SUPPORT.md` - where to ask questions or get help
- `CITATION.cff` - citation metadata for the project

## 7. Target `docs/core/`

Target purpose: stable system and architecture docs.

Candidate contents:

- `docs/core/SPEC.md`
- `docs/core/DD-ARCHITECTURE.md`
- `docs/core/DELIVERY-TAXONOMY.md`
- `docs/core/ROADMAP.md`
- `docs/core/ADR_INDEX.md`

Existing docs may be moved later only through a deliberate migration task. Until then, existing root `docs/` paths should remain stable.

## 8. Target `docs/benchmarks/`

Target purpose: reusable benchmark execution and artifact contracts.

Candidate contents:

- `docs/benchmarks/BENCHMARK_CONTRACT.md`
- `docs/benchmarks/RUN_MANIFEST_SCHEMA.md`
- `docs/benchmarks/RESULT_ARTIFACT_SCHEMA.md`
- `docs/benchmarks/REPRODUCIBILITY_GUIDE.md`
- `docs/benchmarks/BENCHMARK_TASK_TEMPLATE.md`
- `docs/benchmarks/BASELINE_REQUIREMENTS.md`

## 9. Target `docs/scientific-governance/`

Target purpose: keep scientific claims tied to evidence.

Candidate contents:

- `docs/scientific-governance/EVIDENCE_LADDER.md`
- `docs/scientific-governance/CLAIM_REGISTRY.md`
- `docs/scientific-governance/DATASET_POLICY.md`
- `docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md`
- `docs/scientific-governance/PAPER_ALIGNMENT_POLICY.md`
- `docs/scientific-governance/CLAIM_BOUNDARY_CHECKLIST.md`

## 10. Target `docs/community/`

Target purpose: define public community operating rules.

Candidate contents:

- `docs/community/COMMUNITY_GOVERNANCE.md`
- `docs/community/MAINTAINER_GUIDE.md`
- `docs/community/REVIEWER_WORKFLOW.md`
- `docs/community/SUPPORT_MODEL.md`
- `docs/community/MODERATION_PROCESS.md`

## 11. Target `docs/contributors/`

Target purpose: define contribution modes, review expectations, and credit boundaries.

Candidate contents:

- `docs/contributors/CONTRIBUTOR_LEVELS.md`
- `docs/contributors/AUTHORSHIP_POLICY.md`
- `docs/contributors/DRY_LAB_CONTRIBUTION_POLICY.md`
- `docs/contributors/WET_LAB_COLLABORATION_POLICY.md`
- `docs/contributors/REVIEW_CREDIT_POLICY.md`

## 12. Target `docs/derivatives/`

Target purpose: define how downstream projects may use Permea Core.

Candidate contents:

- `docs/derivatives/DERIVATIVE_PROJECT_POLICY.md`
- `docs/derivatives/DERIVATIVE_PROJECT_TEMPLATE.md`
- `docs/derivatives/ATTRIBUTION_REQUIREMENTS.md`
- `docs/derivatives/CLAIM_INHERITANCE_RULES.md`

## 13. Target `docs/release/`

Target purpose: define public-release gates and checklists.

Candidate contents:

- `docs/release/RELEASE_REVIEW_PROCESS.md`
- `docs/release/PUBLIC_RELEASE_CHECKLIST.md`
- `docs/release/ARTIFACT_RELEASE_MATRIX.md`
- `docs/release/VERSIONING_POLICY.md`
- `docs/release/ARCHIVE_POLICY.md`

## 14. Target `docs/paper-alignment/`

Target purpose: keep papers, READMEs, GitHub docs, and claims aligned.

Candidate contents:

- `docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md`
- `docs/paper-alignment/PREPRINT_READINESS_CHECKLIST.md`
- `docs/paper-alignment/SOURCE_TO_CLAIM_REVIEW.md`
- `docs/paper-alignment/README_CLAIM_SYNC_CHECKLIST.md`

## 15. Claim Hygiene Docs Map

Core claim-hygiene docs should include:

- `EVIDENCE_LADDER.md` - evidence levels and what they support
- `CLAIM_REGISTRY.md` - allowed, conditional, and prohibited claim phrases
- `CLAIM_BOUNDARY_CHECKLIST.md` - checklist before release or outreach
- `PAPER_ALIGNMENT_POLICY.md` - paper vs README vs release claim alignment

These docs should explicitly separate:

- computational evidence
- benchmark evidence
- literature-grounded plausibility
- wet-lab evidence
- stronger biological validation

## 16. Evidence and Benchmark Governance Docs Map

Core benchmark/evidence docs should include:

- benchmark contract
- run manifest schema
- result artifact schema
- reproducibility guide
- benchmark task template
- baseline requirements
- evidence ladder

These docs should define how evidence repos emit comparable, provenance-aware artifacts.

## 17. Dataset and Public-Safe Artifact Docs Map

Needed docs:

- `DATASET_POLICY.md`
- `PUBLIC_SAFE_ARTIFACT_POLICY.md`
- `ARTIFACT_RELEASE_MATRIX.md`

These should define:

- public vs private dataset surfaces
- row-level vs aggregate artifact boundaries
- source/license review expectations
- attribution requirements
- artifact blocklists and allowlist candidates
- release gates for row-level data and derived artifacts

## 18. Dry-Lab Contributor Docs Map

Needed docs:

- `DRY_LAB_CONTRIBUTION_POLICY.md`
- `CONTRIBUTING.md`
- `REVIEWER_WORKFLOW.md`
- `REPRODUCIBILITY_GUIDE.md`

Dry-lab contributors may contribute:

- benchmark definitions
- code
- reference baselines
- reproducibility improvements
- source-to-claim reviews
- documentation
- artifact/schema improvements

Dry-lab contribution docs must prevent overclaiming and require reproducible artifact discipline.

## 19. Wet-Lab Collaboration Docs Map

Needed docs:

- `WET_LAB_COLLABORATION_POLICY.md`
- `AUTHORSHIP_POLICY.md`
- `DATASET_POLICY.md`
- `CLAIM_REGISTRY.md`

Wet-lab collaboration docs should define:

- collaboration intake
- assay/data ownership
- claim boundaries
- authorship expectations
- release approval
- partner confidentiality boundaries
- how experimental evidence changes the evidence tier

These docs must not imply completed wet-lab validation.

## 20. Authorship and Credit Docs Map

Needed docs:

- `AUTHORSHIP_POLICY.md`
- `CONTRIBUTOR_LEVELS.md`
- `REVIEW_CREDIT_POLICY.md`
- `CITATION.cff`

These should separate:

- software contribution
- benchmark contribution
- paper contribution
- review contribution
- data/source contribution
- wet-lab collaboration
- maintainer stewardship

No contributor-facing doc should promise authorship without explicit policy criteria and manual decision.

## 21. Reviewer Workflow Docs Map

Needed docs:

- `REVIEWER_WORKFLOW.md`
- `CLAIM_BOUNDARY_CHECKLIST.md`
- `SOURCE_TO_CLAIM_REVIEW.md`
- `PUBLIC_RELEASE_CHECKLIST.md`

Reviewer workflow should define:

- what reviewers evaluate
- what reviewers must not assume
- how to report claim-boundary issues
- how source-to-claim review is performed
- how public-release blockers are logged

## 22. Maintainer and Community Governance Docs Map

Needed docs:

- `COMMUNITY_GOVERNANCE.md`
- `MAINTAINER_GUIDE.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `SUPPORT.md`

These should define:

- maintainer responsibilities
- decision rights
- moderation process
- issue/PR triage
- release approval
- security and sensitive-data handling
- dispute handling

## 23. Derivative Project Governance Docs Map

Needed docs:

- `DERIVATIVE_PROJECT_POLICY.md`
- `DERIVATIVE_PROJECT_TEMPLATE.md`
- `ATTRIBUTION_REQUIREMENTS.md`
- `CLAIM_INHERITANCE_RULES.md`

Derivative policy should define:

- what may be reused from Permea Core
- required attribution
- which claims do not transfer downstream
- public-safe artifact requirements
- release review expectations for derivative repos

## 24. Public vs Local-Only Artifact Boundary

Public repos may contain:

- OSS governance docs
- benchmark contracts
- evidence ladders
- release policies
- claim boundary docs
- reproducibility guides
- paper alignment policies

Private local operator context must remain outside public repos:

- private project source
- private operator instructions
- private source manifests
- private coordination notes
- local path memory
- nonpublic task context

Never commit private local operator context to `permea-core` or `permea-signal-ml`.

## 25. Implementation Priority Order

Priority 1 - contributor and safety basics:

1. `CONTRIBUTING.md`
2. `CODE_OF_CONDUCT.md`
3. `SECURITY.md`
4. `SUPPORT.md`

Priority 2 - scientific governance basics:

5. `CLAIM_REGISTRY.md`
6. `DATASET_POLICY.md`
7. `PUBLIC_SAFE_ARTIFACT_POLICY.md`
8. `REPRODUCIBILITY_GUIDE.md`

Priority 3 - paper/release alignment:

9. `PAPER_ALIGNMENT_POLICY.md`
10. `RELEASE_REVIEW_PROCESS.md`
11. `PUBLIC_RELEASE_CHECKLIST.md`

Priority 4 - contributor credit and collaboration:

12. `CONTRIBUTOR_LEVELS.md`
13. `AUTHORSHIP_POLICY.md`
14. `DRY_LAB_CONTRIBUTION_POLICY.md`
15. `WET_LAB_COLLABORATION_POLICY.md`

Priority 5 - community and derivatives:

16. `COMMUNITY_GOVERNANCE.md`
17. `MAINTAINER_GUIDE.md`
18. `REVIEWER_WORKFLOW.md`
19. `DERIVATIVE_PROJECT_POLICY.md`
20. `CITATION.cff`

## 26. Suggested Task Sequence

Suggested next tasks:

1. Create root-level OSS basics: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`.
2. Create scientific governance basics: `CLAIM_REGISTRY.md`, `DATASET_POLICY.md`, `PUBLIC_SAFE_ARTIFACT_POLICY.md`, `REPRODUCIBILITY_GUIDE.md`.
3. Create paper and release alignment: `PAPER_ALIGNMENT_POLICY.md`, `RELEASE_REVIEW_PROCESS.md`, `PUBLIC_RELEASE_CHECKLIST.md`.
4. Create contributor credit docs: `CONTRIBUTOR_LEVELS.md`, `AUTHORSHIP_POLICY.md`.
5. Create collaboration docs: `DRY_LAB_CONTRIBUTION_POLICY.md`, `WET_LAB_COLLABORATION_POLICY.md`.
6. Create maintainer/reviewer docs: `COMMUNITY_GOVERNANCE.md`, `MAINTAINER_GUIDE.md`, `REVIEWER_WORKFLOW.md`.
7. Create derivative project governance docs.
8. Update README document index after the docs exist.

Each task should happen in a clean worktree/branch and should avoid dirty main.

## 27. Open Questions

Open questions:

- Should existing hyphenated doc filenames be kept for stability or migrated to underscore-based names later?
- Should target folders be introduced immediately or after root-level policy docs exist?
- Which license/citation policy should govern docs vs code?
- How should `permea-core` define citation for derivative projects?
- What formal authorship threshold should apply to paper contributors?
- What minimum source/license review is required before public artifact release?
- Should release approval require a single maintainer, multiple maintainers, or founder/manual approval?
- How should wet-lab partner results be incorporated into the evidence ladder?

## 28. Explicit Claim-Boundary Reminder

AlphaFold for Delivery may be used as an ambition or positioning phrase, but Permea must not claim AlphaFold-level performance, adoption, or standardization.

Permea must not claim:

- clinical efficacy
- completed wet-lab validation
- universal delivery prediction
- production-grade drug delivery platform status
- dataset redistribution permission without source/license approval
- public preprint readiness without explicit readiness approval

Benchmark claims must remain scoped to:

- dataset
- split
- metric
- evidence level
- provenance state
- release boundary

Paper/preprint claims and GitHub README claims must remain aligned.
