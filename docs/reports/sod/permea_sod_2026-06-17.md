# Permea SOD Operating Handoff - 2026-06-17

## Current Status

Permea Core is a public, benchmark-first infrastructure repository for sequence-first biological delivery engineering.

Current public state:

- artifact specifications exist
- lightweight schemas exist
- artifact validator exists
- external example packages exist
- generated evidence, reproducibility, and evaluation surfaces exist
- public claim boundaries remain explicit

## Main HEAD

Start from public `main` at:

- `ab8393df12a555b3c5cb5ffbd605db11b081b9db`

Confirm live state before work:

```bash
git status --short --branch
git log -1 --oneline
```

## First Task Tomorrow

Group P-CORE-042 - Quickstart Experience Layer.

## Scope

The next task should improve first-time user flow from a fresh checkout:

- where to start
- which commands to run first
- how to validate the repository
- how to inspect examples
- how to understand generated outputs
- how to extend the artifact pattern without expanding claims

The task should not change scientific claims or imply biological validation.

## Validation Expectations

Run at minimum:

```bash
git diff --check
python3 scripts/permea_check.py
python3 scripts/permea_specs.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
```

If the task changes examples, validation, generated surfaces, or quickstart command flow, also run the relevant focused tests and generation commands.

## Public / Private Boundaries

Public docs may reference:

- public repository paths
- public commands
- public generated artifact paths
- public examples
- public reports
- public evidence records
- public specifications and schemas

Public docs must not include sensitive access material, restricted infrastructure details, non-public support details, machine-specific paths, or raw restricted data.

## Claim Boundaries

Required public non-claims remain:

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical-effectiveness claim
- no model performance claim
- no state-of-the-art claim
- no solved-delivery claim

The next task may improve usability wording, but it must not add biological outcome claims.

## How To Continue

1. Read [OPEN_THIS_FIRST.md](../../../OPEN_THIS_FIRST.md).
2. Read [REVIEW_HUB.md](../../../REVIEW_HUB.md).
3. Review [Claim Registry](../../claims/claim-registry.md).
4. Review [External Examples](../../../examples/README.md).
5. Run the validation commands above.
6. Keep the smallest accurate documentation memory surface updated when the task completes.
