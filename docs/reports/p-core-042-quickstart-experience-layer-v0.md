# P-CORE-042 Quickstart Experience Layer Report

## Summary

This report records the first-user quickstart experience layer for Permea Core. The layer gives researchers and developers one deterministic command that discovers example packages, runs validation, shows evidence and claim-boundary links, and prints next recommended commands.

The path is:

README -> QUICKSTART -> `python3 scripts/permea_demo.py` -> validate examples -> inspect generated evaluation/evidence outputs -> review claim boundaries.

## User Path

Run from the repository root:

```bash
python3 scripts/permea_demo.py
```

Expected result:

```text
Status: PASS
```

## Implemented Surfaces

- [Quickstart](../../QUICKSTART.md)
- [README](../../README.md)
- [Quickstart demo script](../../scripts/permea_demo.py)
- [Quickstart experience tests](../../tests/test_quickstart_experience.py)
- [Evidence index](../evidence/evidence-index.md)
- [Claim registry](../claims/claim-registry.md)
- [Open This First](../../OPEN_THIS_FIRST.md)
- [Review Hub](../../REVIEW_HUB.md)
- [Generated evaluation packet](../examples/generated/EVALUATION_PACKET.md)
- [Generated evidence matrix](../examples/generated/EVIDENCE_MATRIX.md)

## What The Demo Shows

- what Permea Core is
- what the example packages demonstrate
- one command to run
- what output to expect
- how example package validation is executed
- where generated evaluation, evidence, and claim boundaries are documented
- what is not claimed
- which commands to run next

## Validation Commands

```bash
git diff --check
python3 scripts/permea_demo.py
python3 scripts/permea_check.py
python3 scripts/permea_specs.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest tests/test_quickstart_experience.py tests/test_external_examples.py tests/test_artifact_validator.py
```

## Supported Public Claim

Permea Core provides a deterministic first-user quickstart command for discovering public example packages, validating them locally, and finding evidence and claim-boundary documentation.

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- The demo validates public example package structure and claim-boundary hygiene.
- The demo does not create new scientific results.
- The demo does not confirm source access, redistribution rights, biological outcomes, or model behavior.

## Next Recommended Task

Review the quickstart path with a new contributor and tighten the demo only where the first-run path is unclear.

## Next Recommended Commands

```bash
python3 scripts/permea_check.py
python3 scripts/permea_validate.py
python3 scripts/permea_specs.py
```
