# Evidence: Artifact Validator Bundle

## Evidence ID

EVIDENCE-038

## Status

Implemented, Public-Safe

## Source Task / Group

Group P-CORE-038

## Related Decision Records

- [DEC-004: Specification layer for Permea standard](../decisions/DEC-004-specification-layer-for-permea-standard.md)
- [DEC-005: No production or clinical claims without evidence](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)

## Primary Report

- [P-CORE-038 artifact validator bundle report](../reports/p-core-038-artifact-validator-bundle-v0.md)

## Primary Public Artifacts

- [Artifact validator CLI](../../scripts/permea_check.py)
- [Artifact validator module](../../src/permea_core/validation/artifact_validator.py)
- [Public artifact specifications](../specs/README.md)
- [Generated public artifact examples](../examples/generated/README.md)

## Method / Construction

The validator performs lightweight structural checks over built-in public example artifacts. It inspects dataset cards, benchmark cards, evidence cards, run manifests, and output packages for required fields, artifact type recognition, repo-relative paths, explicit non-claims, claim-boundary wording, and evidence-linkage expectations.

## Validation Surface

```bash
python3 scripts/permea_check.py
python3 -m pytest tests/test_artifact_validator.py
```

## Supported Claims

- Permea Core provides a local artifact validator command for current public example artifacts.
- The validator can report PASS/FAIL-style results for required fields, non-claims, claim boundaries, repo-relative paths, and evidence-linkage expectations.
- The validator is integrated into the unified artifact validation command.

## Claims Not Supported

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- The validator is structural and public-example oriented.
- It does not execute acquisition, load datasets, call external services, run models, or score candidates.
- It does not establish biological delivery, mechanism, safety, therapeutic effect, clinical utility, or broad generalization.
- Future stricter schema enforcement should be added only when the public artifact specs stabilize further.

## Reproducibility Instructions

```bash
python3 scripts/permea_check.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
```

## Next Evidence Step

Extend validator coverage when new artifact families are added or when current lightweight specs move to stricter schema enforcement.
