# Acquisition Manifest: cppsite2_placeholder_acquisition_plan

> Generated from Permea acquisition-manifest metadata. This public-safe example records planning metadata only: no dataset downloaded, no acquisition executed, no redistribution rights confirmed, and no wet-lab validation by Permea.

## Manifest ID

cppsite2_placeholder_acquisition_plan

## Dataset ID

cppsite2_placeholder

## Source IDs

- cppsite2

## Benchmark IDs

- cpp_cppsite2_placeholder

## Acquisition Mode

manual-source-card

## Acquisition Status

source-carded

## Redistribution Status

not-reviewed

## Expected Local Outputs

- ignored local field inventory if access is later confirmed
- ignored local provenance notes if acquisition is later approved
- generated dataset card metadata only in this repository

## Provenance Requirements

- source record identifier
- peptide sequence and modification state
- cargo or assay context where available
- source publication or PMID/DOI
- access date and source version if later reviewed

## Review Requirements

- license_review_required: True
- manual_review_required: True

## Failure Modes

- source access path changes or is unavailable
- license/access terms remain unclear
- positive-only source membership creates negative sampling risk
- cargo or assay context is incomplete

## Fallback Strategy

- keep source card and dataset card as metadata-only planning artifacts
- require negative sampling proposal before benchmark use
- defer acquisition until access and redistribution posture are reviewed

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea

## Claim Boundary

acquisition manifest metadata only; no dataset downloaded, no acquisition executed, no redistribution rights confirmed, and no wet-lab validation by Permea

## Next Action

verify access path, license/access terms, field schema, and negative sampling policy before any acquisition script is proposed
