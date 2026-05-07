# Security Policy

## Scope

This policy covers security and sensitive-disclosure handling for Permea Core.

Relevant issues include:

- software vulnerabilities
- accidental secret or credential exposure
- private data exposure
- restricted dataset exposure
- license or provenance leaks
- accidental publication of row-level biological datasets
- accidental publication of row-level predictions, rankings, split manifests, group assignments, or sequence-pair leakage artifacts where release permission is unresolved

## Reporting Vulnerabilities or Sensitive Exposure

Do not disclose sensitive issues publicly if the report includes:

- secrets, credentials, API keys, tokens, or private keys
- private or confidential data
- partner-controlled data
- restricted row-level datasets
- unlicensed biological datasets
- nonpublic source terms or license details
- exploitable vulnerability details

Until a dedicated security contact is published, contact a repository maintainer directly through an appropriate private channel. If a public issue is necessary, keep it minimal and do not include sensitive details.

## Dataset and Artifact Safety

Permea is an open scientific OSS project, but public-by-default does not mean every data artifact is safe to publish.

Special care is required for:

- row-level datasets
- source-derived biological records
- row-level labels
- row-level predictions
- rankings
- split manifests
- group assignments
- leakage-audit tables
- partner or collaborator data
- artifacts with unresolved source/license terms

Do not upload these materials unless release permission, attribution, and source terms are documented.

## Claim and Release Safety

Security review includes release-boundary safety. A public artifact can create risk if it exposes restricted data or supports unsupported claims.

Permea may use "AlphaFold for Delivery" as an ambition or positioning phrase only. It must not claim AlphaFold-level performance, adoption, or standardization.

Permea must not claim:

- completed wet-lab validation unless documented
- clinical efficacy
- therapeutic efficacy
- universal delivery prediction
- dataset redistribution permission without source/license approval

Benchmark claims must remain scoped to dataset, split, metric, and evidence level.

## Response Expectations

Maintainers will aim to:

- acknowledge sensitive reports when feasible
- assess whether private handling is required
- remove exposed secrets or restricted artifacts when appropriate
- document public-safe remediation where possible
- avoid making legal, licensing, clinical, or biological validation conclusions without appropriate review

Response timelines are currently best-effort while the project is in an early open scientific stage.
