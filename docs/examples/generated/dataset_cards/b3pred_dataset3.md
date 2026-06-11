# Dataset Card: B3Pred Dataset 3 dataset-card proposal

> Generated from Permea dataset-card metadata. This public-safe example records metadata only: no dataset downloaded, no redistribution rights confirmed, and no wet-lab validation by Permea.

## Dataset ID

b3pred_dataset3

## Source IDs

- b3pred_dataset3
- b3pdb
- brainpeps

## Benchmark IDs

- bbb_b3pred_dataset3

## Delivery Axis

blood-brain barrier

## Biological Scope

benchmark-oriented BBB peptide classification surface

## Expected Data Type

peptide sequences and source-defined benchmark labels

## Label Type

binary source-defined benchmark label; label policy requires source review

## Acquisition Status

benchmark-mapped

## License / Access Status

source attribution and redistribution require review

## Redistribution Status

not-confirmed

## Provenance Requirements

- source dataset name and citation lineage
- source construction notes
- peptide sequence and source-defined label
- access date or source version if available
- transformations and split policy notes

## Split Policy

- method: stratified_kfold
- leakage_checks:
  - exact_sequence_duplicate_check
  - source_group_review

## Known Limitations

- source access and license posture require review
- labels are source-defined benchmark labels
- dataset card does not imply row-level data is present in this repository

## Explicit Non-Claims

- no dataset downloaded
- no redistribution rights confirmed
- no wet-lab validation by Permea

## Claim Boundary

dataset-card metadata proposal only; no dataset downloaded, no redistribution rights confirmed, and no wet-lab validation by Permea

## Next Action

trace source citation and construction policy before dataset-card review
