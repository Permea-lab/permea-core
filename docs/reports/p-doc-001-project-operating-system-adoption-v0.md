# P-DOC-001 Project Operating System Adoption v0

## Objective

Adopt a public project operating-system layer for Permea Core so reviewers, contributors, and future sessions can understand and continue the repository without historical chat logs.

## Why This Layer Exists

Permea Core has grown from a documentation and specification repository into a public artifact infrastructure layer with generated surfaces, schemas, validation commands, reproducibility flows, evaluation packets, and technical reports.

The operating layer makes that state navigable.

## What Changed

- Added `OPEN_THIS_FIRST.md`.
- Added `REVIEW_HUB.md`.
- Added a documentation operating-standard runbook.
- Added an ADR for the breadcrumb and review hub standard.
- Added this public adoption report.

## Public Artifacts Added

- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/runbooks/project-documentation-operating-standard.md`
- `docs/adr/ADR-001-project-breadcrumb-and-review-hub-standard.md`
- `docs/reports/p-doc-001-project-operating-system-adoption-v0.md`

## Technical Design

The layer is intentionally lightweight and Markdown-only. It does not add runtime dependencies or change artifact generation behavior.

The root breadcrumb is optimized for first contact. The review hub is optimized for navigation and continuation. The runbook defines task completion expectations. The ADR records the durable decision.

## Current Public Truth Captured

The backfill is intentionally minimal. It records:

- current public artifact infrastructure
- current generated evidence surfaces
- current artifact specifications and schemas
- current claim boundaries
- current paper-alignment posture
- current primary reports and evidence
- recommended next work

It does not reconstruct full project history.

## Evidence And Report Links

- [OPEN_THIS_FIRST.md](../../OPEN_THIS_FIRST.md)
- [REVIEW_HUB.md](../../REVIEW_HUB.md)
- [Generated evidence surface](../examples/generated/README.md)
- [Artifact index](../examples/generated/ARTIFACT_INDEX.md)
- [Evidence matrix](../examples/generated/EVIDENCE_MATRIX.md)
- [Artifact specification report](p-core-036-artifact-specification-layer.md)
- [Public artifact specifications](../specs/README.md)

## Continuation Workflow

Every new task should start by reading:

1. `OPEN_THIS_FIRST.md`
2. `REVIEW_HUB.md`
3. the relevant public docs and generated surfaces

Every completed task or group should update:

1. `OPEN_THIS_FIRST.md`
2. `REVIEW_HUB.md`

unless the task explicitly exempts breadcrumb updates.

## Validation Commands

Recommended validation for this adoption:

```bash
pwd
git status --short --branch
git log -1 --oneline
python3 scripts/permea_specs.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
git diff --check
```

## Claim Boundaries

This adoption is documentation structure only. It does not add scientific evidence or expand Permea claims.

Current non-claims remain:

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical-effectiveness claim
- no model performance claim
- no state-of-the-art claim
- no solved-delivery claim

## Limitations

- This is the first version of the project operating-system layer.
- It does not validate links automatically.
- It does not replace generated evidence surfaces, reports, or ADRs.
- It does not add new artifact validators.

## Next Evidence Steps

- Keep the breadcrumb and review hub refreshed at task completion.
- Add link-checking or documentation consistency checks in a later task if needed.
- Continue strengthening artifact-spec validation in a separate scoped task.
