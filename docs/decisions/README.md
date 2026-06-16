# Permea Decision Records

This directory records decision-critical Permea history. Reports explain what happened. Evidence surfaces explain what was generated or measured. Decision records explain why Permea chose a direction.

Decision records support paper writing, reviewer response, technical diligence, proposal work, collaborator onboarding, and continuity across future contributors.

## Layer Model

Permea's current public documentation and evidence model uses these layers:

| Layer | Status | Role |
| --- | --- | --- |
| Doctrine Layer | Established | Public principles, claim boundaries, governance, and research posture. |
| Decision Layer | Developing | Durable records for strategic and technical choices. |
| Evidence Layer | Strong | Generated evidence surfaces, artifact indexes, matrices, and dry-run reports. |
| Reproducibility Layer | Strong | Local commands and reports that regenerate and validate current public artifacts. |
| Evaluation Layer | Strong | Template/reference packet for transferring the artifact pattern to users. |
| Specification Layer | Strong | Public standards and schemas for artifact families. |
| Memory Layer | Established | Breadcrumb, review hub, ADR, runbook, and reports for continuation. |

## Decision Index

- [DEC-001: Reproducibility-first program structure](DEC-001-reproducibility-first-program-structure.md)
- [DEC-002: Evidence bundle before claims](DEC-002-evidence-bundle-before-claims.md)
- [DEC-003: Evaluation bundle as user transfer layer](DEC-003-evaluation-bundle-as-user-transfer-layer.md)
- [DEC-004: Specification layer for Permea standard](DEC-004-specification-layer-for-permea-standard.md)
- [DEC-005: No production or clinical claims without evidence](DEC-005-no-production-or-clinical-claims-without-evidence.md)
- [DEC-006: Project memory layer required for continuation](DEC-006-project-memory-layer-required-for-continuation.md)

## Update Rule

If a task makes or changes a strategic or technical decision, it must create or update a decision record.

Every major task should update at least one relevant project memory surface:

- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/reports/`
- `docs/evidence/`
- `docs/decisions/`
- `docs/adr/`

The chosen surface should match the kind of work completed.
