# Evidence: Evaluation Bundle

## Evidence ID

EVIDENCE-034

## Status

Implemented, Public-Safe

## Source Task / Group

Group P-CORE-034

## Related Decision Records

- [DEC-003: Evaluation bundle as user transfer layer](../decisions/DEC-003-evaluation-bundle-as-user-transfer-layer.md)
- [DEC-005: No production or clinical claims without evidence](../decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)

## Primary Report

- [Evaluation packet](../examples/generated/EVALUATION_PACKET.md)

## Primary Public Artifacts

- [Evaluation packet JSON](../examples/generated/EVALUATION_PACKET.json)
- [Generated evidence surface](../examples/generated/README.md)
- [Artifact index](../examples/generated/ARTIFACT_INDEX.md)

## Method / Construction

The evaluation bundle creates a template/reference packet that maps public input families, generated surfaces, validation paths, reproducibility paths, limitations, and non-claims.

## Validation Surface

```bash
python3 scripts/permea_evaluate.py
python3 scripts/permea_validate.py
```

## Supported Claims

- Permea Core has an implemented template/reference evaluation packet for artifact-system extension.
- The evaluation packet links current input families and public generated surfaces.

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

The evaluation bundle is not an experimental result. It transfers an artifact pattern and does not prove biological behavior or model quality.

## Reproducibility Instructions

```bash
python3 scripts/permea_evaluate.py
python3 scripts/permea_validate.py
```

## Next Evidence Step

Keep the evaluation bundle linked to future public input-family examples and claim-boundary updates.
