# Evidence: Quickstart Experience Layer

EVIDENCE-042

## Status

Implemented, Public-Safe

## Source Task

Group P-CORE-042

## Summary

Permea Core now has a deterministic first-user quickstart command:

```bash
python3 scripts/permea_demo.py
```

The command discovers public example packages, runs local artifact validation, links evidence and claim-boundary surfaces, prints explicit non-claims, and recommends the next validation commands.

## Primary Artifacts

- [Quickstart](../../QUICKSTART.md)
- [Quickstart demo script](../../scripts/permea_demo.py)
- [Quickstart experience tests](../../tests/test_quickstart_experience.py)
- [Quickstart experience report](../reports/p-core-042-quickstart-experience-layer-v0.md)
- [Evidence index](evidence-index.md)
- [Claim registry](../claims/claim-registry.md)

## Validation Surface

```bash
python3 scripts/permea_demo.py
python3 -m pytest tests/test_quickstart_experience.py
```

## Supported Public Claims

- Permea Core provides a one-command first-user path for example discovery and artifact validation.
- The quickstart links users to evidence and claim-boundary surfaces.
- The quickstart prints next commands for broader local validation.

## Unsupported Public Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- The quickstart validates public example package structure and claim-boundary hygiene.
- The quickstart does not create biological results.
- The quickstart does not confirm source access or redistribution rights.

## Next Evidence Step

Keep the quickstart synchronized with future example package, artifact validator, and evidence index changes.
