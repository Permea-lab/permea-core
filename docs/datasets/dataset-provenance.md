# Dataset Provenance

Dataset provenance records explain where a dataset surface came from, how it can be reviewed, how it can be reproduced, and what limits apply.

## Required Provenance Standards

| Standard | Requirement |
| --- | --- |
| Source reference | Record citation, registry link, accession, source URL, release identifier, or source owner reference where applicable. |
| Acquisition method | Record whether acquisition is proposed, documented, scripted, manually reviewed, externally supplied, or out of scope. |
| Processing steps | Record filtering, normalization, cleaning, label mapping, deduplication, aggregation, or other transformation steps. |
| Transformation summary | Summarize how source material becomes the dataset-card or derived artifact surface. |
| Generated artifacts | List generated cards, manifests, packages, matrices, or reports that depend on the dataset. |
| Checksums where applicable | Record hashes for stable public artifacts when the artifact is fixed and reviewable. |
| License / usage constraints | Record license, redistribution, citation, access, review, and reuse constraints. |
| Reproducibility path | Record the command, script, manifest, or review path that reproduces the documented surface. |
| Known limitations | Record incomplete source context, missing labels, acquisition gaps, redistribution limits, benchmark limits, or evidence gaps. |

## Provenance Status Values

- Proposed: provenance requirements are identified but incomplete.
- Partial: source and limitation records exist, but acquisition, processing, or usage constraints remain incomplete.
- Documented: source, use constraints, and limitations are documented for review.
- Reproducible: processing path or generated artifacts can be reproduced locally.
- Independently Reproduced: an independent reviewer reproduced the documented computational surface.
- Externally Validated: an external source or reviewer validated a bounded provenance scope.
- Deprecated: provenance remains for traceability, but new use is discouraged.
- Archived: provenance is retained for historical review only.

## Boundary Rule

Provenance completeness supports reviewability. It does not by itself establish biological effect, therapeutic outcome, expression improvement, experimental validation, clinical evidence, or solved delivery.
