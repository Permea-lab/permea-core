# Contributing to Permea Core

## Welcome

Permea Core is building the open execution layer for delivery engineering. Contributions should help make delivery evidence benchmarkable, reproducible, and reusable.

The project is benchmark-first and evidence-bounded. Good contributions make tasks, data, labels, metrics, outputs, provenance, and limitations easier to inspect.

## What Kinds of Contributions Are Useful

Useful contributions include:

- dataset cards
- benchmark tasks
- evidence cards
- run manifests
- feature descriptors
- baseline models or baseline configurations
- reproduction reports
- documentation improvements
- source attribution improvements
- claim-boundary review

See [docs/CONTRIBUTION_OBJECTS.md](docs/CONTRIBUTION_OBJECTS.md) for the contribution object model.

## Before Contributing

Before opening an issue or PR:

- confirm the contribution can be discussed publicly
- identify the source or citation when relevant
- define the task, label, metric, or artifact boundary
- document limitations and uncertainty
- avoid uploading private or restricted row-level data
- avoid uploading secrets, credentials, tokens, or private keys
- use conservative scientific language

If release status is unclear, open a minimal issue describing the question without exposing restricted material.

## Public / Private Safety Rules

Do not include:

- private or proprietary data without rights to share it
- private sequences or sensitive candidate rankings
- restricted row-level datasets or row-level predictions without release approval
- credentials, tokens, passwords, private keys, or environment values
- private workflow notes or internal execution context
- private resource or program references

Public contributions should focus on source attribution, reproducibility, benchmark structure, and claim boundaries.

## Claim Boundaries

Permea Core does not claim solved delivery, wet-lab validation, clinical or therapeutic effect, universal delivery prediction, state-of-the-art status, or maturity comparable to AlphaFold.

Benchmark claims must remain scoped to:

- dataset
- label policy
- split policy
- metric set
- model or baseline
- evidence level
- provenance state
- release boundary

Use "AlphaFold-for-Delivery" only as an ambition and infrastructure direction, not achieved status.

## Contribution Workflow

1. Open an issue using the relevant template.
2. Maintainers triage the issue for scope, data posture, and claim boundaries.
3. Draft the contribution object or implementation.
4. Reproducibility, citation, and claim-boundary review happens before acceptance.
5. Open a pull request with a narrow scope.
6. Maintainers review and merge when the contribution is public-safe and useful.

## How to Propose a Dataset Card

Use the dataset card issue template.

Include the dataset name, task family, source or citation, sequence type, label definition, positive and negative criteria, assay context, limitations, suggested metrics, and public/private data status.

Do not upload row-level data unless public release rights are clear.

## How to Propose a Benchmark Task

Use the benchmark task issue template.

Include the task name, task family, dataset card link or source reference, input schema, label schema, split policy, baseline models, metrics, output artifacts, and non-claims.

Benchmark tasks should be reproducible and bounded. A useful task definition is clear about what the benchmark does and does not support.

## How to Submit an Evidence Card

Use the evidence card issue template.

Include the source paper or database, molecule or sequence reference, barrier or task, assay type, cargo context, organism or cell context, reported outcome, evidence strength, limitations, citation, extraction method, and human review status.

Do not strengthen the original source claim. Evidence cards should preserve context and uncertainty.

## How to Submit a Reproduction Report

Use the reproduction report issue template.

Include the benchmark or task, repository commit, environment, command run, output artifacts, observed metrics, expected metrics if known, deviations, logs or excerpts, and reviewer notes.

Reproduction reports may confirm a result, surface drift, or identify missing instructions.

## Good First Issues

Good first issues should map to a real contribution object. Examples:

- draft a dataset card for a public source
- summarize a benchmark task boundary
- add a feature descriptor explanation
- create an evidence card from a source
- reproduce a documented benchmark run
- improve a guide or docs map

## Pull Request Expectations

Pull requests should:

- stay scoped to one contribution object or document family
- list changed files
- describe claim-boundary impact
- describe any data or artifact release impact
- include reproduction notes when relevant
- avoid unrelated formatting churn
- avoid adding data unless release status is clear

## Code and Documentation Style Expectations

Documentation should be direct, source-aware, and conservative about claims.

Code or configuration contributions should preserve reproducibility through clear inputs, outputs, versions, and provenance. Prefer simple, reviewable baselines before complex model additions.

## Contact

Questions about contribution scope can be sent to a.kim@permea.us.
