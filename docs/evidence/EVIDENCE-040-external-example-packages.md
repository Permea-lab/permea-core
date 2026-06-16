# Evidence: External Example Packages

## Evidence ID

EVIDENCE-040

## Status

Implemented, Public-Safe

## Source Task / Group

Group P-CORE-040

## Related Decision Records

- [DEC-002: Evidence bundle before claims](../decisions/DEC-002-evidence-bundle-before-claims.md)
- [DEC-004: Specification layer for Permea standard](../decisions/DEC-004-specification-layer-for-permea-standard.md)
- [DEC-005: No production or clinical claims without evidence](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)

## Primary Report

- [P-CORE-040 external example packages report](../reports/p-core-040-external-example-packages-v0.md)

## Primary Public Artifacts

- [External examples index](../../examples/README.md)
- [Synthetic reference example](../../examples/synthetic_reference_example/README.md)
- [BBB peptide reference example](../../examples/bbb_peptide_reference_example/README.md)
- [Expression engineering reference example](../../examples/expression_engineering_reference_example/README.md)
- [Artifact validator](../../scripts/permea_check.py)

## Method / Construction

The example packages are deterministic, public-safe fixture packages. Each package includes JSON artifact files, a README, and deterministic validation result files. The artifact validator checks each package for required files, JSON parsing, non-claims, claim-boundary wording, and package-level validation status.

## Validation Surface

```bash
python3 scripts/permea_check.py examples/synthetic_reference_example
python3 scripts/permea_check.py examples/bbb_peptide_reference_example
python3 scripts/permea_check.py examples/expression_engineering_reference_example
python3 -m pytest tests/test_external_examples.py
```

## Supported Claims

- Permea Core provides copyable public reference packages for the current artifact standard.
- The reference packages can be checked with the public artifact validator.
- The examples demonstrate artifact structure, validation handoff, evaluation handoff, reproducibility handoff, claim boundaries, and extension pattern.

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

- Examples are reference fixtures only.
- Examples do not demonstrate biological performance, source rights, model performance, expression improvement, BBB crossing, or experimental outcomes.
- Future examples may need stricter schema coverage if the public specifications become stricter.

## Reproducibility Instructions

```bash
python3 scripts/permea_check.py
python3 scripts/permea_validate.py
```

## Next Evidence Step

Add external example packages only when they remain public-safe, deterministic, validator-compatible, and claim-bounded.
