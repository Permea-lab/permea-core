# P-CORE-038 Artifact Validator Layer

## Objective

Create the first public artifact validator layer for Permea Core so researchers and developers can check public example artifacts against the public artifact standards.

## Why this layer exists

The previous artifact specification layer defined public standards. This validator layer makes those standards executable enough for local inspection, review, and extension without requiring dataset acquisition, external services, or model execution.

## What changed

- Added a lightweight public artifact validator module.
- Added `scripts/permea_check.py`.
- Added validator documentation at `docs/specs/VALIDATION.md`.
- Added tests for validator behavior, report structure, boundary checks, and documentation links.
- Linked validation guidance from public entry points.

## Public artifacts added

- `docs/specs/VALIDATION.md`
- `docs/reports/p-core-038-artifact-validator-layer.md`
- `scripts/permea_check.py`
- `src/permea_core/validator/`
- `tests/test_artifact_validator.py`

## Technical design

The validator uses the existing public specification registry and schema files as its source of required field concepts. It checks current public examples in their existing formats: Markdown for cards and manifests, JSON for evidence cards, and YAML-like metadata for output-package manifests.

## Validator checks implemented

- artifact file exists
- artifact family is known
- required top-level schema concepts are present through current public example aliases
- claim-boundary language is present
- explicit non-claim language is present where appropriate
- forbidden public/private boundary terms are absent
- obvious credential-like terms are absent
- report status is deterministic

## CLI design

The CLI supports:

```bash
python3 scripts/permea_check.py --all
python3 scripts/permea_check.py --family dataset_card
python3 scripts/permea_check.py --family benchmark_card
python3 scripts/permea_check.py --family evidence_card
python3 scripts/permea_check.py --family run_manifest
python3 scripts/permea_check.py --family output_package
python3 scripts/permea_check.py --file docs/examples/generated/dataset_cards/b3pred_dataset3.md
```

## Validation report format

The report is deterministic text with:

- status
- checked artifact families
- checked files
- failed checks
- warnings
- non-claim boundary status

## How this supports researchers and developers

Researchers and developers can run one local command before proposing new artifact examples. The validator makes missing structural concepts and boundary issues visible early.

## How this supports future papers/reports/proposals

Future public reports and proposals can reference a repeatable artifact-checking layer instead of relying only on prose review. The validator keeps claims tied to artifact structure and explicit limitations.

## Validation commands

```bash
python3 scripts/permea_check.py --all
python3 scripts/permea_specs.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/generate_permea_artifacts.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest tests/test_artifact_validator.py
```

## Claim boundaries

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- This is a lightweight public validator, not a full JSON Schema validation layer.
- It validates current public example artifacts, not private or row-level data.
- It does not prove source rights, biological transport, mechanism, safety, therapeutic effect, or model quality.

## Next evidence steps

- Add stricter schema checks when the public examples converge on fully structured representations.
- Extend validator coverage as new public artifact families are accepted.
- Keep validator behavior aligned with public specs, generated examples, and tests.
