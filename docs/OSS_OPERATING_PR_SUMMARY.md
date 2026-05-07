# Permea Core OSS Operating System PR Summary

## 1. PR Purpose

This branch adds the first Permea Core OSS operating system: a public documentation layer for open scientific governance, contributor workflow, claim hygiene, dataset/release safety, paper alignment, derivative project governance, and citation/versioning/archive practice.

The branch is documentation-only. It does not add scientific results, model outputs, datasets, wet-lab evidence, or public preprint readiness claims.

## 2. What This Branch Adds

This branch adds:

- root OSS community files
- scientific governance policies
- paper and release alignment policies
- contributor, authorship, dry-lab, and wet-lab collaboration policies
- community, maintainer, reviewer, and reviewer credit policies
- derivative project governance
- citation, versioning, archive/deprecation, and attribution policies
- a README index for the operating docs

## 3. File Groups Added

Root files:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `SUPPORT.md`
- `CITATION.cff`

Planning and map:

- `docs/OSS_OPERATING_DOCS_MAP.md`

Scientific governance:

- `docs/scientific-governance/CLAIM_REGISTRY.md`
- `docs/scientific-governance/DATASET_POLICY.md`
- `docs/scientific-governance/PUBLIC_SAFE_ARTIFACT_POLICY.md`
- `docs/scientific-governance/REPRODUCIBILITY_GUIDE.md`

Paper and release:

- `docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md`
- `docs/release/RELEASE_REVIEW_PROCESS.md`
- `docs/release/PUBLIC_RELEASE_CHECKLIST.md`
- `docs/release/RELEASE_OWNERSHIP_MATRIX.md`
- `docs/release/VERSIONING_POLICY.md`
- `docs/release/ARCHIVE_AND_DEPRECATION_POLICY.md`
- `docs/release/ATTRIBUTION_POLICY.md`

Contributor and collaboration:

- `docs/contributors/CONTRIBUTOR_LEVELS.md`
- `docs/contributors/AUTHORSHIP_POLICY.md`
- `docs/contributors/DRY_LAB_CONTRIBUTION_POLICY.md`
- `docs/contributors/WET_LAB_COLLABORATION_POLICY.md`

Community governance:

- `docs/community/COMMUNITY_GOVERNANCE.md`
- `docs/community/MAINTAINER_GUIDE.md`
- `docs/community/REVIEWER_WORKFLOW.md`
- `docs/community/REVIEWER_CREDIT_POLICY.md`

Derivative projects:

- `docs/derivatives/DERIVATIVE_PROJECT_POLICY.md`
- `docs/derivatives/PROJECT_REGISTRY.md`
- `docs/derivatives/DERIVATIVE_REVIEW_CHECKLIST.md`

## 4. What This Branch Does Not Claim

This branch does not claim:

- completed wet-lab validation
- clinical efficacy
- therapeutic efficacy
- universal delivery prediction
- production-grade drug delivery platform status
- AlphaFold-level performance, adoption, or standardization
- dataset redistribution permission
- public preprint readiness
- legal conclusions about licensing, IP, employment, trademark, university policy, or authorship disputes

"AlphaFold for Delivery" may be used only as ambition or positioning, not as a maturity claim.

## 5. Review Checklist

- [ ] README index links resolve.
- [ ] Added docs are documentation-only.
- [ ] No data, model, result, figure, or benchmark artifacts are added.
- [ ] No secrets, credentials, private records, or restricted artifacts are exposed.
- [ ] Policy docs use consistent role and release terminology.
- [ ] Deferred items are visible rather than silently resolved.

## 6. Claim Hygiene Checklist

- [ ] Claims remain scoped to governance and operating infrastructure.
- [ ] Benchmark claims remain scoped to dataset, split, metric, model, artifact, and evidence level.
- [ ] No wet-lab validation is claimed unless documented.
- [ ] No clinical efficacy is claimed.
- [ ] No universal delivery prediction is claimed.
- [ ] No AlphaFold-level maturity, adoption, or standardization is claimed.
- [ ] Permea-aligned does not mean Permea-validated.

## 7. Dataset / Public-Safe Artifact Checklist

- [ ] Dataset redistribution permission is not claimed.
- [ ] Row-level datasets remain blocked unless explicit permission and review are documented.
- [ ] Row-level labels, features, predictions, rankings, split manifests, group assignments, leakage tables, and raw upstream mirrors remain held unless release-safe.
- [ ] Aggregate artifacts are still subject to claim-boundary review.
- [ ] Dataset/source/license uncertainty routes to Hold or manual review.

## 8. Contributor / Community Checklist

- [ ] GitHub contribution does not automatically grant authorship.
- [ ] Attribution does not equal authorship.
- [ ] Attribution does not equal endorsement.
- [ ] Reviewer input does not equal peer review or external validation.
- [ ] Wet-lab collaboration interest does not equal wet-lab validation.
- [ ] Maintainer, reviewer, release approver, and founder/manual approver roles are separated.

## 9. Release-Readiness Checklist

- [ ] Release gates are documented.
- [ ] Release ownership matrix is present.
- [ ] Public release no-go conditions are explicit.
- [ ] Versioning, archive, correction, withdrawal, and deprecation states are documented.
- [ ] Citation guidance avoids invented DOI/archive metadata.
- [ ] Public release requires recorded approval where applicable.

## 10. Known Deferred Items

- exact maintainer/release approver roster
- formal legal/licensing workflow
- formal trademark/branding process
- derivative project templates
- Zenodo/DOI/archive setup
- final citation metadata
- project-specific maintainer assignments

## 11. Recommended Reviewer Focus

Reviewers should focus on:

- whether the policy set is internally consistent
- whether README links and docs paths are correct
- whether claim boundaries are conservative enough
- whether dataset/public-safe artifact restrictions are explicit enough
- whether maintainer/reviewer/release roles are practical
- whether deferred legal, branding, citation, and roster items are clearly marked

## 12. Merge Readiness Note

This branch is suitable for review as a documentation-only OSS operating foundation package if the README index and policy links are correct.

Merge should not be treated as public scientific validation, dataset release approval, wet-lab validation, clinical readiness, public preprint readiness, or endorsement of derivative projects.
