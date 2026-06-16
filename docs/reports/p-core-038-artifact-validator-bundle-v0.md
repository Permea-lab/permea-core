# P-CORE-038 Artifact Validator Bundle Report

## Purpose

This report records the first public artifact validator bundle for Permea Core. The goal is to let researchers and developers check public artifact examples against Permea specification, claim-boundary, non-claim, repo-relative path, and evidence-linkage expectations.

## Scope

This bundle adds a lightweight local validator for current public example artifacts:

- dataset cards
- benchmark cards
- evidence cards
- run manifests
- output packages

It does not add acquisition, dataset loading, model execution, model scoring, or scientific performance validation.

## Files Changed

- `scripts/permea_check.py`
- `src/permea_core/validation/artifact_validator.py`
- `src/permea_core/validation/__init__.py`
- `src/permea_core/validation/artifacts.py`
- `tests/test_artifact_validator.py`
- `docs/evidence/EVIDENCE-038-artifact-validator-bundle.md`
- `docs/reports/p-core-038-artifact-validator-bundle-v0.md`
- public documentation, breadcrumb, evidence, claim, specification, and generated-surface navigation files

## Technical Design

The validator uses a deterministic result dictionary for each artifact. It infers artifact type from repo-relative paths, checks existence and required sections or fields, scans for required non-claims, checks claim-boundary wording, and records evidence-linkage paths or references where applicable.

The implementation avoids new dependencies. It uses standard JSON parsing and the existing YAML dependency already used by current repository validators.

## Validator Contract

Each artifact result includes:

- `artifact_path`
- `artifact_type`
- `status`
- `checks`
- `issues`
- `warnings`
- `non_claims_seen`
- `evidence_links_seen`

Statuses are:

- `PASS`
- `FAIL`
- `WARNING`

## Supported Artifact Families

- Dataset Card
- Benchmark Card
- Evidence Card
- Run Manifest
- Output Package

## Checks Implemented

- Schema presence through public specification and artifact-family recognition
- Required field or section presence
- File/path existence for public-safe repo-relative artifacts
- Artifact type recognition
- Non-claim presence
- Claim-boundary check
- Evidence-linkage check where applicable
- Human-readable issue messages

## Results

The built-in public example artifacts pass the validator:

```bash
python3 scripts/permea_check.py
```

Expected summary:

- Status: `PASS`
- Artifacts checked: `5`
- Fail count: `0`

## Validation

Required validation for this bundle:

```bash
git diff --check
python3 scripts/permea_check.py
python3 scripts/permea_specs.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest tests/test_artifact_validator.py tests/test_artifact_specs.py tests/test_evaluation_bundle.py tests/test_reproducibility_bundle.py tests/test_evidence_surface.py tests/test_demo_packet.py tests/test_artifact_index.py tests/test_evidence_matrix.py tests/test_permea_dry_run.py tests/test_generate_permea_artifacts.py tests/test_validate_permea_artifacts.py
```

## Scan Results

The public/private scan, claim-boundary scan, and secret scan should be run before merging. Expected result is no restricted local paths, no restricted infrastructure details, no credentials, and no unsupported scientific claims.

## Claim Boundaries

This validator supports local structural review of public examples. It does not support any unsupported public claim listed below.

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

- The validator is lightweight and intentionally not a full JSON Schema enforcement layer.
- It validates current public examples and artifact-family expectations.
- It does not validate scientific truth, biological outcomes, clinical utility, or source-access rights.
- Future artifacts may require expanded checks and stricter schemas.

## Next Recommended Goal

Review and merge the artifact validator bundle if validation and scans remain clean. Then extend validator coverage only when new public artifact families or stricter artifact specifications require it.
