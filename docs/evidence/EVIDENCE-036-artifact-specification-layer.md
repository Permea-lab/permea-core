# Evidence: Artifact Specification Layer

## Evidence ID

EVIDENCE-036

## Status

Implemented, Public-Safe

## Source Task / Group

Group P-CORE-036

## Related Decision Records

- [DEC-004: Specification layer for Permea standard](../decisions/DEC-004-specification-layer-for-permea-standard.md)
- [DEC-005: No production or clinical claims without evidence](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)

## Primary Report

- [P-CORE-036 artifact specification layer report](../reports/p-core-036-artifact-specification-layer.md)

## Primary Public Artifacts

- [Public artifact specifications](../specs/README.md)
- [Dataset card schema](../../schemas/dataset_card.schema.json)
- [Benchmark card schema](../../schemas/benchmark_card.schema.json)
- [Evidence card schema](../../schemas/evidence_card.schema.json)
- [Run manifest schema](../../schemas/run_manifest.schema.json)
- [Output package schema](../../schemas/output_package.schema.json)

## Method / Construction

The specification layer defines public artifact standards and lightweight JSON schemas for current Permea artifact families. It is inspected through a deterministic registry command.

## Validation Surface

```bash
python3 scripts/permea_specs.py
```

## Supported Claims

- Permea Core has public artifact specifications for current artifact families.
- Permea Core has lightweight schemas for current artifact families.

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

The specification layer defines structure and expectations. It is not a validator bundle and does not prove source access, biological behavior, or model quality.

## Reproducibility Instructions

```bash
python3 scripts/permea_specs.py
```

## Next Evidence Step

Add a separate evidence record when artifact-spec validator work is merged.
