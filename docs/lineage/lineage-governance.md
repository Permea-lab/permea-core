# Lineage Governance

## Purpose

Lineage governance explains how Permea Core should create, review, update, and retire provenance records across public operating layers.

The goal is traceability. A lineage record should make artifact relationships auditable without copying datasets, notebooks, experiment code, or package implementation details into Core.

## Creating Lineage Records

A lineage record may be created when a public artifact depends on or summarizes another public artifact. Suitable artifacts include:

- evidence records
- benchmark cards
- benchmark run records
- dataset cards
- research packages
- public review packets
- external evidence package records
- claim registry entries
- specifications
- validation outputs

Each record should start from the [lineage record template](lineage-record-template.md) and should satisfy the required fields in `schemas/lineage-record.schema.json`.

## Required Metadata

Each lineage record must include:

- lineage record ID
- artifact type
- artifact ID
- parent artifacts
- child artifacts
- related claims
- lineage status
- provenance notes
- version

Additional recommended metadata includes related evidence, benchmarks, datasets, research packages, review packets, external evidence packages, specifications, validation artifacts, limitations, and maintainer notes.

## Review Expectations

Lineage updates should be reviewed for:

- valid artifact identifiers
- correct parent and child relationships
- explicit provenance notes
- matching claim boundaries
- validation artifact links where applicable
- stale or superseded references
- absence of raw dataset, notebook, or implementation-copy content

Reviewers should prefer explicit incomplete lineage over implied completeness.

## Broken Lineage

Broken lineage exists when a referenced artifact is missing, superseded, renamed, or no longer supports the stated relationship.

Broken lineage should be handled by:

- marking the record as draft or documented until corrected
- adding provenance notes that identify the broken relationship
- updating child records that depend on the broken relationship
- avoiding downstream claim strengthening until the break is resolved

## Deprecated Lineage

Deprecated or superseded lineage should not be deleted if it remains useful for audit history. Instead:

- mark the record as superseded or archived
- link the replacement record when available
- document why the old relationship changed
- preserve claim-boundary limitations from the original record

## External Evidence Packages

External evidence packages participate through metadata links, not copied contents. Permea Core may reference repository names, package IDs, public paths, evidence categories, reproducibility commands, validation paths, and claim boundaries.

Permea Core should not copy raw datasets, notebooks, bulky experiment code, or paper-specific implementation material from adjacent evidence packages.

## Claim Boundary Enforcement

Lineage records must not upgrade claims beyond the supported evidence status. A relationship among artifacts remains computational-only, framework-only, proposed, not yet demonstrated, out of scope, or requiring future validation unless independent review changes the relevant source records.

Prohibited claim language must be avoided except in explicit non-claim or boundary sections.
