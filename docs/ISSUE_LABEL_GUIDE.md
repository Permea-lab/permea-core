# Issue Label Guide

This guide explains how labels are used in Permea Core issues so contributors can
pick work with the right public-data, evidence, and review posture.

## Scope Labels

- `dataset-card`: issue is about drafting or improving a dataset card.
- `benchmark-task`: issue is about a benchmark task definition, split policy, or metrics.
- `evidence-card`: issue is about extracting or curating bounded source evidence.
- `docs`: issue is documentation-only.
- `reproduction`: issue is about rerunning or validating an existing benchmark flow.

## Review Posture Labels

- `claim-boundary`: reviewer should check wording for overclaim risk.
- `citation-needed`: issue is not ready to merge without explicit source attribution.
- `public-safe`: content is expected to stay within public-release boundaries.
- `needs-triage`: maintainers still need to confirm scope, release posture, or next step.

## Difficulty / Onramp Labels

- `good first issue`: narrow, public-safe work item suitable for a first contribution.
- `help wanted`: maintainers want outside help, but the issue may still need domain context.

## How Contributors Should Use Labels

Before starting work:

1. Confirm there is at least one scope label so the contribution object is clear.
2. Check whether a review-posture label signals extra care around claims, citations, or release boundaries.
3. If the issue has no `public-safe` signal and touches data or evidence, ask for clarification before drafting artifacts.

## Recommended Label Combinations

- Dataset drafting: `dataset-card` + `citation-needed` + `public-safe`
- Benchmark definition: `benchmark-task` + `claim-boundary`
- First contribution docs work: `docs` + `good first issue`
- Re-run / validation task: `reproduction` + `help wanted`

## Notes For Maintainers

Prefer small, composable label sets over highly specific one-off labels. A short,
consistent taxonomy makes it easier for contributors to understand whether an issue
is about data structure, evidence extraction, benchmark design, or review posture.
