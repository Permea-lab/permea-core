# P-CORE-045 Dataset Registry Layer v0

## Purpose

Group P-CORE-045 creates the first dataset operating layer for Permea Core. The layer makes dataset status, card requirements, provenance requirements, linked evidence, linked benchmarks, validation commands, and claim boundaries reviewable without adding raw biological datasets.

## Files Added Or Changed

- `docs/datasets/README.md`
- `docs/datasets/dataset-registry.md`
- `docs/datasets/dataset-lifecycle.md`
- `docs/datasets/dataset-card-template.md`
- `docs/datasets/dataset-provenance.md`
- `docs/datasets/dataset-governance.md`
- `schemas/dataset-card.schema.json`
- `schemas/dataset_card.schema.json`
- `scripts/permea_datasets.py`
- `tests/test_dataset_registry_layer.py`
- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`

## Dataset Layer Design

The dataset layer defines a registry, lifecycle, card template, provenance standard, governance path, schema, and CLI. Current registry entries are public review surfaces only:

- `b3pred_dataset3`: draft card surface linked to current validation and example evidence
- `cppsite2_placeholder`: proposed placeholder surface linked to specification evidence

No active reference dataset is claimed by this layer.

## Provenance Design

The provenance layer requires source reference, acquisition method, processing steps, transformation summary, generated artifacts, checksums where applicable, license or usage constraints, reproducibility path, and known limitations. Provenance completeness is treated as review support, not biological outcome evidence.

## CLI Behavior

`python3 scripts/permea_datasets.py` prints a deterministic summary with:

- registered dataset count
- active reference dataset count
- proposed, draft, documented, and validated counts
- registry entry status
- provenance reminder
- claim-boundary reminder
- dataset docs and schema paths

The command requires no network access and no non-public assets.

## Tests Run

- `git diff --check`
- `python3 scripts/permea_datasets.py`
- `python3 scripts/permea_benchmarks.py`
- `python3 scripts/permea_evidence.py`
- `python3 scripts/permea_check.py`
- `python3 scripts/permea_specs.py`
- `python3 scripts/permea_validate.py`
- `python3 scripts/permea_evaluate.py`
- `python3 scripts/permea_reproduce.py`
- `python3 scripts/validate_permea_artifacts.py`
- `python3 -m pytest`

## Public-Safety Boundary Result

Touched public files were scanned for prohibited public-safety terms. Result: PASS.

## Claim-Discipline Result

Touched public files were scanned for prohibited unsupported scientific claims. Hits are limited to explicit non-claim, future-validation, or out-of-scope language. Result: PASS.

Explicit non-claims:

- no dataset acquisition completion claim unless separately validated
- no redistribution-rights confirmation unless separately documented
- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
- no clinical evidence claim
- no expression improvement claim

## Limitations

This layer does not add raw biological datasets, confirm dataset acquisition, confirm redistribution rights, create active reference datasets, establish independent reproduction, establish external validation, or create biological outcome evidence.

## Next Recommended Task

Add a dataset-card validator extension only after a future dataset card requires stricter schema enforcement beyond the current public fixture validation.
