# Acquisition Manifest: b3pred_dataset3_acquisition_plan

> Generated from Permea acquisition-manifest metadata. This public-safe example records planning metadata only: no dataset downloaded, no acquisition executed, no redistribution rights confirmed, and no wet-lab validation by Permea.

## Manifest ID

b3pred_dataset3_acquisition_plan

## Dataset ID

b3pred_dataset3

## Source IDs

- b3pred_dataset3
- b3pdb
- brainpeps

## Benchmark IDs

- bbb_b3pred_dataset3

## Acquisition Mode

no-redistribution-source-card-only

## Acquisition Status

no-redistribution-source-card-only

## Redistribution Status

not-confirmed

## Expected Local Outputs

- ignored local source review notes if access is later confirmed
- ignored local provenance ledger if acquisition is later approved
- generated dataset card metadata only in this repository

## Provenance Requirements

- source dataset name and citation lineage
- source construction notes
- source-defined label policy
- access date or source version if later reviewed
- transformation and split policy notes

## Review Requirements

- license_review_required: True
- manual_review_required: True

## Failure Modes

- source access cannot be confirmed
- license terms do not allow redistribution
- source construction policy remains ambiguous
- provenance fields are insufficient for benchmark use

## Fallback Strategy

- keep dataset in source-card-only mode
- retain benchmark mapping as metadata only
- defer dataset card promotion until source and license review pass

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea

## Claim Boundary

acquisition manifest metadata only; no dataset downloaded, no acquisition executed, no redistribution rights confirmed, and no wet-lab validation by Permea

## Next Action

review source citation lineage, access posture, and license terms before any acquisition script is proposed
