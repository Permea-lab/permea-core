# P-CORE-040 External Example Packages Report

## Purpose

This report records the first public external example packages for Permea Core. The examples show how outside researchers and developers can inspect, copy, validate, and adapt Permea-style artifact packages.

## Scope

This task adds public-safe reference examples only. The examples demonstrate artifact structure, validation flow, evaluation handoff, reproducibility handoff, claim boundaries, and extension pattern.

## Files Changed

- `examples/README.md`
- `examples/synthetic_reference_example/`
- `examples/bbb_peptide_reference_example/`
- `examples/expression_engineering_reference_example/`
- `tests/test_external_examples.py`
- validator integration in `src/permea_core/validation/artifact_validator.py`
- documentation, evidence, claim registry, report, and breadcrumb updates

## Technical Design

Each example package contains:

- `README.md`
- `dataset_card.json`
- `benchmark_card.json`
- `evidence_card.json`
- `run_manifest.json`
- `output_package.json`
- `validation_result.md`
- `validation_result.json`

The validator treats each example directory as an `example_package` and checks required files, JSON parsing, validation result status, non-claims, claim-boundary wording, and package links.

## Example Package Contract

Example packages must be deterministic, public-safe, repo-relative, copyable, validator-compatible, and explicit about unsupported claims.

## Examples Added

- `examples/synthetic_reference_example`
- `examples/bbb_peptide_reference_example`
- `examples/expression_engineering_reference_example`

## Validator Integration

The default validator command includes the three example packages:

```bash
python3 scripts/permea_check.py
```

Each package can also be checked directly:

```bash
python3 scripts/permea_check.py examples/synthetic_reference_example
python3 scripts/permea_check.py examples/bbb_peptide_reference_example
python3 scripts/permea_check.py examples/expression_engineering_reference_example
```

## Results

All three examples return `PASS` with the artifact validator.

## Validation

Required validation for this task:

```bash
git diff --check
python3 scripts/permea_check.py
python3 scripts/permea_check.py examples/synthetic_reference_example
python3 scripts/permea_check.py examples/bbb_peptide_reference_example
python3 scripts/permea_check.py examples/expression_engineering_reference_example
python3 scripts/permea_specs.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest tests/test_external_examples.py tests/test_artifact_validator.py tests/test_artifact_specs.py tests/test_evaluation_bundle.py tests/test_reproducibility_bundle.py tests/test_evidence_surface.py tests/test_demo_packet.py tests/test_artifact_index.py tests/test_evidence_matrix.py tests/test_permea_dry_run.py tests/test_generate_permea_artifacts.py tests/test_validate_permea_artifacts.py
```

## Scan Results

The public/private scan, claim-boundary scan, and secret scan should pass before merge. Expected result is no restricted paths, no restricted infrastructure details, no credentials, and no unsupported scientific claims.

## Claim Boundaries

The examples demonstrate structure and validator compatibility only. They do not demonstrate biological performance, wet-lab validation by Permea, clinical efficacy, dataset acquisition, source rights, model performance, BBB crossing performance, expression improvement, or solved delivery.

Required non-claims remain:

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- Examples are reference fixtures only.
- Examples do not include row-level source data or real acquisition.
- Validator compatibility is structural and claim-boundary oriented.
- Future examples may require stricter schema alignment.

## Next Recommended Goal

Review and merge the external example packages if validation and scans remain clean. Then add future example packages only when they are public-safe, deterministic, validator-compatible, and clearly claim-bounded.
