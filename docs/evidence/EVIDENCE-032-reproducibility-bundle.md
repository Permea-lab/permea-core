# Evidence: Reproducibility Bundle

## Evidence ID

EVIDENCE-032

## Status

Implemented, Public-Safe

## Source Task / Group

Group P-CORE-032

## Related Decision Records

- [DEC-001: Reproducibility-first program structure](../decisions/DEC-001-reproducibility-first-program-structure.md)
- [DEC-002: Evidence bundle before claims](../decisions/DEC-002-evidence-bundle-before-claims.md)

## Primary Report

- [Reproducibility report](../examples/generated/REPRODUCIBILITY_REPORT.md)

## Primary Public Artifacts

- [Reproducibility report JSON](../examples/generated/REPRODUCIBILITY_REPORT.json)
- [Generated evidence surface](../examples/generated/README.md)
- [Artifact index](../examples/generated/ARTIFACT_INDEX.md)

## Method / Construction

The reproducibility bundle uses local deterministic commands to regenerate public artifact surfaces and validate their expected structure.

## Validation Surface

```bash
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
```

## Supported Claims

- Permea Core has a local public reproduction path for current generated artifact surfaces.
- Public generated artifacts can be validated locally through repository commands.

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

The bundle covers public metadata and generated examples. It does not load source datasets, call external services, run models, or measure performance.

## Reproducibility Instructions

```bash
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
```

## Next Evidence Step

Add new evidence records when additional reproducible artifact families are merged.
