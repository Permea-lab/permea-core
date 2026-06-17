# Permea Signal ML Integration

`permea-signal-ml` is an adjacent public evidence package connected to Permea Core.

This integration document explains the relationship between the package and Core. It does not copy raw datasets, notebooks, experiment code, or paper-specific working material into Core.

## Purpose Of `permea-signal-ml`

`permea-signal-ml` is a public computational evidence package for a bounded sequence-first delivery benchmark workflow. It packages dataset workflow documentation, sequence-derived feature workflows, baseline modeling surfaces, aggregate evaluation outputs, reproducibility-oriented materials, and review-support documentation in its own repository.

Read it as an evidence package connected to Permea Core, not as the whole Permea Core operating layer.

## Relationship To `permea-core`

`permea-core` defines the public operating system:

- evidence navigation
- dataset registry concepts
- benchmark registry concepts
- benchmark execution model
- research package concepts
- public review packet concepts
- claim registry and claim boundaries
- validation and reproducibility conventions

`permea-signal-ml` applies those ideas to one adjacent public computational evidence package. It should remain outside Core when the material is package-specific, experimental-code-oriented, row-level, bulky, or paper-support-specific.

## Linked Evidence Categories

The signal package may link to these Permea Core evidence categories:

- computational evidence surfaces
- reproducibility workflow evidence
- benchmark-support evidence
- dataset provenance and limitation evidence
- validation and review-support evidence

These links support reviewability. They do not establish biological outcomes.

## Linked Dataset Registry Concepts

The signal package relates to Core dataset concepts through:

- dataset source documentation
- provenance status
- usage constraints
- processing summaries
- known limitations
- release posture for row-level or derived artifacts

Core should record dataset concepts and boundaries. Package-specific raw data, prepared data, notebooks, and row-level derived artifacts belong in the evidence package or its release process, not in Core.

## Linked Benchmark Registry Concepts

The signal package relates to Core benchmark concepts through:

- benchmark surface documentation
- measured property description
- evaluation protocol
- metric reporting conventions
- benchmark card links
- benchmark execution metadata
- limitations and unsupported claims

Core should define benchmark and benchmark-run standards. Package-specific benchmark implementation code and generated outputs belong in the evidence package.

## Linked Research Package Concepts

The signal package may support a future research package by providing:

- evidence package reference
- reproducibility path
- validation path
- aggregate artifact references
- limitations
- claim-boundary statements

Core should package references and review paths. Paper drafts, supplement drafts, figure-generation code, and package-specific review artifacts should remain in the evidence package unless a future Core task explicitly creates a public reference packet.

## Linked Public Review Packet Concepts

The signal package can be reviewed through the public Core path:

README -> QUICKSTART -> REVIEW PACKET -> EVIDENCE -> BENCHMARKS -> DATASETS -> RESEARCH -> SIGNAL INTEGRATION -> CLAIMS -> VALIDATION

The integration path helps reviewers understand where package evidence fits and where claims stop.

## What Belongs In `permea-core`

- public integration metadata
- external evidence package template
- external evidence governance
- schema for external evidence package metadata
- links to public evidence package repositories
- claim-boundary and validation guidance
- review path and registry references

## What Belongs In `permea-signal-ml`

- package-specific code
- package-specific configs
- package-specific generated outputs
- package-specific figures
- package-specific notebooks
- package-specific paper-support materials
- package-specific release review for row-level or derived artifacts

## Claim Boundaries

This integration is computational-only and review-oriented. It does not claim:

- wet-lab validation by Permea
- biological efficacy claim
- therapeutic outcome claim
- BBB success claim
- solved-delivery claim
- SOTA performance claim
- experimental validation claim
- clinical evidence claim
- expression improvement claim

## Limitations

This integration does not validate the external package independently. It does not import package artifacts into Core. It does not register new scientific results. It records the public relationship and review path.

## Future Validation Path

Future package versions should add or update:

- evidence package metadata
- linked dataset cards or dataset registry concepts
- linked benchmark cards or benchmark run records
- reproducibility commands
- validation outputs
- claim registry links
- limitations
- supersession status when older package versions are replaced
