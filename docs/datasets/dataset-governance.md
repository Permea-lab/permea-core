# Dataset Governance

Dataset governance defines how Permea Core dataset records are proposed, reviewed, promoted, deprecated, and linked to evidence and benchmarks.

## Proposal

A dataset may be proposed when it has a clear intended use, source type, expected provenance needs, and claim boundary. Proposed entries must remain clearly marked as proposed or not yet demonstrated.

## External Dataset Documentation

External datasets can be documented when the source reference, usage constraints, intended use, limitations, and validation path are recorded. Documentation does not imply acquisition completion, redistribution rights, active reference status, or biological outcome evidence.

## Reproducible Derived Datasets

A derived dataset can move toward reproducible status only when acquisition method, processing steps, transformation summary, generated artifacts, checksums where applicable, and local reproduction path are recorded.

## Linking Evidence And Benchmarks

Dataset entries should link to:

- evidence records that support the current status
- benchmark entries that reference or depend on the dataset
- specifications and schemas used by the dataset card
- validation commands that can be run locally
- claim boundaries that define what is and is not supported

## Claim Constraints

Dataset cards may claim only the status supported by provenance and evidence. Active status is a computational reference status. It does not establish biological efficacy, therapeutic outcome, expression improvement, experimental validation, clinical evidence, or solved delivery.

## Deprecation

Deprecate a dataset when source constraints, provenance concerns, benchmark drift, or evidence updates make it unsuitable for new reference work. Deprecated entries should retain their history, limitations, replacement path if one exists, and linked evidence.

## Change Review

Dataset changes should be reviewed when they alter source references, processing, labels, usage constraints, linked benchmarks, linked evidence, lifecycle status, or claim boundaries.

Required review checks:

- schema validity
- provenance completeness
- linked evidence and benchmark consistency
- claim-boundary scan
- public-safety scan
- local validation command output
