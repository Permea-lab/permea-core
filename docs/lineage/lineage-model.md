# Lineage Model

## Purpose

The lineage model defines how Permea Core records relationships among claims, evidence assets, datasets, benchmarks, benchmark runs, research packages, review packets, external evidence packages, specifications, and validation artifacts.

This model is infrastructure for provenance tracking. It does not create new scientific evidence or make biological claims.

## Artifact Classes

| Artifact class | Parent relationships | Child relationships | Provenance expectations |
| --- | --- | --- | --- |
| Evidence | Source records, external evidence packages, validation artifacts | Claims, benchmarks, research packages, review packets | source reference, evidence ID, review status, limitations |
| Benchmarks | Evidence, datasets, specifications, claim boundaries | benchmark runs, research packages, review packets | benchmark ID, lifecycle status, metrics, dataset links, validation path |
| Benchmark Runs | benchmarks, datasets, specifications | evidence records, research packages, review packets | run ID, execution metadata, reproducibility path, validation outputs |
| Datasets | source references, external evidence packages, processing artifacts | benchmarks, benchmark runs, research packages | dataset ID, provenance record, license or usage constraints, processing summary |
| Research Packages | evidence, datasets, benchmarks, benchmark runs, specifications, claims | review packets, future package versions | package ID, assembly path, reproducibility checks, validation checks |
| Review Packets | research packages, evidence maps, claim registry, validation outputs | reviewer notes, superseding packets | packet ID, reading path, command path, unsupported claims summary |
| External Evidence Packages | public evidence repositories, reproducibility outputs | evidence records, datasets, benchmarks, research packages | repository, package version, linked Core layer, boundary notes |
| Claims | evidence records, specifications, validation artifacts | research packages, review packets, future claim revisions | claim category, evidence status, limitations, unsupported boundary |
| Specifications | schema files, artifact templates, governance docs | datasets, benchmarks, benchmark runs, evidence records | schema path, version, required fields, validation route |
| Validation Artifacts | commands, generated reports, schema checks | evidence records, claims, review packets | command, output path, status, timestamp when available |

## Relationship Direction

Lineage records should list both parents and children when known:

- Parents explain what an artifact depends on.
- Children explain what later artifacts reference or summarize it.
- Related evidence, claims, specifications, and validation artifacts provide cross-cutting audit links.

For example, a future benchmark run may have parent artifacts such as a benchmark card, dataset card, and specification schema. Its child artifacts may include evidence records, research package sections, and public review packet summaries.

## Lineage Completeness Expectations

Each lineage record should identify:

- artifact type and artifact ID
- known parent artifacts
- known child artifacts
- related claims
- related specifications
- validation artifacts
- provenance notes
- lineage status
- limitations or incomplete links

Incomplete lineage is acceptable when it is explicit. Missing parent links, missing validation outputs, unresolved dataset provenance, or unreviewed external package references should be marked as draft or documented rather than reviewed.

## Claim-Boundary Implications

Lineage can show that an artifact is connected to evidence, a dataset, a benchmark, or a review packet. It cannot by itself establish biological validity, efficacy, benchmark performance, or experimental confirmation.

Lineage presence does not imply biological validity, efficacy, or experimental confirmation.

Public claims should remain bounded by the weakest linked artifact. If a dataset is proposed, a benchmark is draft, or validation is missing, downstream research packages and review packets should keep that limitation visible.

## Limitations

- Current lineage is framework-only until specific lineage records are added.
- Current lineage does not independently validate external evidence packages.
- Current lineage does not convert computational evidence into biological or clinical evidence.
- Current lineage does not replace artifact-specific validators, schemas, or governance review.
