# Public-Safe Artifact Policy

## 1. Purpose

This document defines Permea Core's initial public-safe artifact policy.

The policy separates artifacts that are generally safe to publish from artifacts that require source, license, confidentiality, or claim-boundary review before release.

Public-safe does not mean claim-free. Even aggregate artifacts require conservative interpretation.

## 2. Artifact Classes

### Safe to Publish

Artifacts that usually do not expose restricted data and support public project understanding.

Examples:

- source code without secrets
- schemas
- benchmark contract docs
- run manifest templates
- reproducibility instructions
- public governance docs
- aggregate non-sensitive summaries

### Likely Safe After Review

Artifacts that may be safe after maintainer/manual review.

Examples:

- aggregate metrics
- aggregate figures
- non-row-level tables
- public-safe artifact manifests
- summary reports
- benchmark summaries
- source-to-claim reviews

### Hold Until Source/License Decision

Artifacts that may depend on third-party, derived, or source-controlled data.

Examples:

- processed feature tables
- dataset manifests with row-level identifiers
- derived row-level outputs
- source-derived metadata
- partner-generated summaries

### Do Not Publish Without Explicit Permission

Artifacts that should not be released unless release permission and required review are documented.

Examples:

- restricted row-level datasets
- unlicensed biological datasets
- raw upstream dataset mirrors
- confidential partner data
- private data
- secrets or credentials

## 3. Public-Safe Examples

Generally public-safe candidates include:

- code
- schemas
- benchmark contracts
- run manifest templates
- result artifact schema definitions
- aggregate metrics
- aggregate figures
- non-row-level summaries
- reproducibility instructions
- claim-boundary checklists
- release review checklists

These still require review for unsupported scientific or public-readiness claims.

## 4. Hold / Block Examples

Hold or block public release for:

- row-level peptide datasets
- row-level labels
- row-level feature tables
- row-level predictions
- ranking tables
- split manifests
- group assignments
- sequence-pair leakage CSVs
- raw upstream dataset mirrors
- private or partner-controlled records
- artifacts with unresolved source/license terms

These artifacts may be used internally only when allowed by source terms and project policy.

## 5. Release Review Checklist

Before publishing an artifact, check:

- Does it contain row-level records?
- Does it reveal labels, predictions, rankings, split assignments, or grouped row identity?
- Does it derive from a third-party dataset?
- Are source, license, and attribution documented?
- Is redistribution permission explicit?
- Is the artifact aggregate or row-level?
- Does the artifact support only scoped benchmark claims?
- Are secrets, credentials, private data, and confidential content absent?
- Is maintainer/manual approval needed?
- Are README, paper, website, and release notes aligned?

If uncertain, hold the artifact.

## 6. Public Artifact Manifest Requirements

Each public artifact package should include a manifest with:

- artifact path
- artifact type
- source dataset reference, if relevant
- row-level or aggregate status
- release class
- license or source status
- claim supported
- evidence level
- reviewer or maintainer decision
- known limitations

The manifest should make it clear what is released and what remains withheld.

## 7. Repo-Specific Release Boundary

### Permea Core

`permea-core` should usually publish:

- operating docs
- benchmark contracts
- schemas
- templates
- governance policies
- reproducibility guides
- public-safe examples

It should not publish paper-specific restricted datasets or private local orchestration context.

### Permea Signal ML

`permea-signal-ml` may contain paper-specific artifacts, but public release must respect:

- source/license status
- row-level artifact restrictions
- manuscript claim boundaries
- supplement/export review
- dataset redistribution decisions

Row-level artifacts should remain blocked until explicit permission is documented.

### Future Benchmark / Dataset Repos

Future repos should declare their release boundary before accepting data:

- what can be public
- what is aggregate-only
- what is internal-only
- what requires partner/manual/legal review
- what must never be committed

## Claim-Boundary Reminder

Permea may use "AlphaFold for Delivery" as ambition or positioning only.

Permea must not claim AlphaFold-level performance, adoption, or standardization; completed wet-lab validation unless documented; clinical efficacy; universal delivery prediction; production-grade drug delivery platform status; or dataset redistribution permission without source/license approval.

Benchmark claims must remain scoped to dataset, split, metric, model, artifact, and evidence level.
