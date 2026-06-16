# P-DOC-004 Decision and Documentation Backfill v0

## Objective

Create the first public Decision Layer for Permea Core and backfill only the decision-critical history needed to understand current direction.

## Why This Layer Exists

Reports explain what happened. Evidence surfaces explain what was generated or validated. Decision records explain why Permea chose a direction.

The Decision Layer helps future paper writing, reviewer response, technical diligence, proposal work, collaborator onboarding, and continuation across future contributors.

## What Changed

- Added `docs/decisions/`.
- Added a decision-record index.
- Added six initial decision records for major Permea choices.
- Updated `OPEN_THIS_FIRST.md` with the layer model and decision links.
- Updated `REVIEW_HUB.md` with the layer model, decision index, and updated continuation rule.
- Updated the documentation operating-standard runbook with decision-record completion rules.

## Public Artifacts Added

- `docs/decisions/README.md`
- `docs/decisions/DEC-001-reproducibility-first-program-structure.md`
- `docs/decisions/DEC-002-evidence-bundle-before-claims.md`
- `docs/decisions/DEC-003-evaluation-bundle-as-user-transfer-layer.md`
- `docs/decisions/DEC-004-specification-layer-for-permea-standard.md`
- `docs/decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md`
- `docs/decisions/DEC-006-project-memory-layer-required-for-continuation.md`

## Permea Layer Model

| Layer | Status | Role |
| --- | --- | --- |
| Doctrine Layer | Established | Public principles, claim boundaries, governance, and research posture. |
| Decision Layer | Developing | Durable records for strategic and technical choices. |
| Evidence Layer | Strong | Generated evidence surfaces, artifact indexes, matrices, and dry-run reports. |
| Reproducibility Layer | Strong | Local commands and reports that regenerate and validate current public artifacts. |
| Evaluation Layer | Strong | Template/reference packet for transferring the artifact pattern to users. |
| Specification Layer | Strong | Public standards and schemas for artifact families. |
| Memory Layer | Established | Breadcrumb, review hub, ADR, runbook, and reports for continuation. |

## Decision-Critical Backfill

This backfill focuses on:

- why Permea exists as an evidence-centric research program
- why evidence bundles come before claims
- why reproducibility and evaluation bundles matter
- why artifact specifications define a reusable Permea standard
- why claim boundaries and public-safe separation matter
- why a project memory layer is required for continuation

It does not reconstruct the entire project history.

## Future Rule

Every major Permea task must update at least one of:

- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/reports/`
- `docs/evidence/`
- `docs/decisions/`
- `docs/adr/`

If a task makes or changes a strategic or technical decision, it must create or update a decision record.

## Related Reports

- [P-DOC-001 project operating-system adoption v0](p-doc-001-project-operating-system-adoption-v0.md)
- [P-CORE-036 artifact specification layer](p-core-036-artifact-specification-layer.md)

## Related Evidence

- [Generated evidence surface](../examples/generated/README.md)
- [Evidence matrix](../examples/generated/EVIDENCE_MATRIX.md)
- [Artifact index](../examples/generated/ARTIFACT_INDEX.md)
- [Evaluation packet](../examples/generated/EVALUATION_PACKET.md)
- [Reproducibility report](../examples/generated/REPRODUCIBILITY_REPORT.md)
- [Public artifact specifications](../specs/README.md)

## Validation Commands

Recommended validation for this backfill:

```bash
pwd
git status --short --branch
git log -1 --oneline
python3 scripts/permea_specs.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
git diff --check
```

## Claim Boundary

This backfill adds decision documentation only. It does not add scientific evidence or expand Permea claims.

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

- The Decision Layer is developing and intentionally minimal.
- The backfill covers major current choices, not full project history.
- The records are public technical rationale, not legal, clinical, or release approval.
- `docs/evidence/` is referenced as a future memory surface but is not created in this task.

## Next Evidence Steps

- Merge the decision-layer branch after review if validation and scans remain clean.
- Add only decision-critical backfill in later tasks.
- Add or update decision records whenever strategic or technical choices change.
- Continue artifact-spec validation work in a separate scoped group.
