# Evidence: Evidence Surface Layer

## Evidence ID

EVIDENCE-030

## Status

Implemented, Public-Safe

## Source Task / Group

Group P-CORE-030

## Related Decision Records

- [DEC-002: Evidence bundle before claims](../decisions/DEC-002-evidence-bundle-before-claims.md)
- [DEC-006: Project memory layer required for continuation](../decisions/DEC-006-project-memory-layer-required-for-continuation.md)

## Primary Report

- [Generated evidence surface](../examples/generated/README.md)

## Primary Public Artifacts

- [Demo packet](../examples/generated/DEMO_PACKET.md)
- [Artifact index](../examples/generated/ARTIFACT_INDEX.md)
- [Evidence matrix](../examples/generated/EVIDENCE_MATRIX.md)
- [Benchmark dry-run report](../examples/generated/dry_runs/example_benchmark_dry_run.md)

## Method / Construction

The evidence surface is generated from public repository metadata and public generated artifact paths. It creates a navigation layer for reviewer-facing artifact inspection.

## Validation Surface

```bash
python3 scripts/generate_evidence_surface.py
python3 scripts/validate_permea_artifacts.py
```

## Supported Claims

- Permea Core has an implemented public navigation surface for generated artifact review.
- The surface links current public artifact families, commands, limitations, and explicit non-claims.

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

This surface organizes public artifacts and commands. It does not create new scientific evidence or validate biological behavior.

## Reproducibility Instructions

```bash
python3 scripts/generate_evidence_surface.py
python3 scripts/permea_validate.py
```

## Next Evidence Step

Keep evidence records synchronized with generated surface changes.
