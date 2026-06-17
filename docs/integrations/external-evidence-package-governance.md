# External Evidence Package Governance

External evidence package governance defines how public evidence packages connect to Permea Core without moving package-specific code, datasets, notebooks, generated outputs, or paper-support sprawl into Core.

## Proposing A Package

An external evidence package proposal should include:

- evidence package ID
- package name
- public repository
- purpose
- evidence type
- linked datasets
- linked benchmarks
- linked research packages
- linked claims
- reproducibility path
- validation path
- claim boundaries
- limitations
- status
- version

New packages start as `proposed` unless the package has enough public metadata to be documented.

## Linking To Permea Core

Packages should link to Core through:

- evidence navigation
- dataset registry concepts
- benchmark registry concepts
- benchmark execution metadata
- research package references
- public review packet path
- claim registry entries
- validation and reproducibility commands

The integration should be specific enough for a reviewer to understand what the package supports and what remains unsupported.

## Required Metadata

Required metadata is defined by [external-evidence-package.schema.json](../../schemas/external-evidence-package.schema.json). Package records must include repository, purpose, evidence type, linked datasets, linked benchmarks, linked research packages, linked claims, reproducibility path, validation path, claim boundaries, limitations, status, and version.

## What Must Remain Outside Permea Core

The following should remain in the external evidence package or its release process:

- raw datasets
- prepared or row-level derived datasets
- notebooks
- bulky experiment code
- package-specific generated outputs
- package-specific figures
- package-specific manuscript drafts
- package-specific release review records

Core should retain integration metadata, schemas, governance, review paths, and claim boundaries.

## Claim Boundary Enforcement

Every package link must preserve explicit claim boundaries. External evidence package records must not imply:

- wet-lab validation by Permea
- biological efficacy claim
- therapeutic outcome claim
- BBB success claim
- solved-delivery claim
- SOTA performance claim
- experimental validation claim
- clinical evidence claim
- expression improvement claim

If a package cannot support a claim with evidence and validation, narrow the claim or remove it.

## Future Package Versions

Future package versions should update:

- package version
- linked dataset status
- linked benchmark status
- reproducibility path
- validation path
- evidence links
- claim boundaries
- limitations
- supersession notes

Version changes should be reviewed for public-safety boundaries, claim discipline, and repository-boundary discipline.

## Stale Or Superseded Packages

Mark a package as `superseded` when a newer package version replaces it. Mark a package as `archived` when retained for history only.

Superseded or archived packages should not be presented as current evidence without clear status language.
