# Project Documentation Operating Standard

## Purpose

This runbook defines the public documentation operating standard for Permea Core. It keeps the repository self-describing for reviewers, contributors, and future sessions without relying on historical chat logs.

## Project Documentation Standard

Permea Core should maintain three public documentation layers:

- entry breadcrumbs: `OPEN_THIS_FIRST.md` and `REVIEW_HUB.md`
- decision records: `docs/decisions/`
- architecture decision records: `docs/adr/`
- task and technical reports: `docs/reports/`

Generated evidence surfaces should remain under `docs/examples/generated/` and should be refreshed by generators rather than hand-edited when possible.

## Continuation Workflow

At the start of a task:

1. Read `OPEN_THIS_FIRST.md`.
2. Read `REVIEW_HUB.md`.
3. Check live Git state.
4. Read the claim boundary before editing public wording.
5. Inspect the files directly related to the task.

At the end of a task:

1. Run relevant generation and validation commands.
2. Run `git diff --check`.
3. Review public/private and claim-boundary language.
4. Update the relevant project memory surface for the kind of work completed.
5. Add or update a report under `docs/reports/` when the task changes project direction, evidence posture, or reviewer workflow.
6. Add or update a decision record under `docs/decisions/` when the task makes or changes a strategic or technical decision.

## Public / Private Separation

Public documentation may include:

- repository structure
- public commands
- public reports
- public artifact paths
- public claim boundaries
- public roadmap and next tasks

Public documentation must not include sensitive access material, restricted infrastructure details, non-public support details, machine-specific paths, or raw restricted data.

## Evidence Rules

Evidence references should point to public artifacts, public reports, generated surfaces, schemas, registries, or documented policies.

Do not describe ungenerated artifacts as current evidence. Do not convert roadmap items into completed claims. If evidence is incomplete, say so directly.

## Report Rules

Reports under `docs/reports/` should include:

- objective
- what changed
- evidence or artifact references
- validation commands
- claim boundaries
- limitations
- next evidence steps

Reports should be public-safe and should not include private process details.

## ADR Rules

ADRs should record durable decisions, not routine task notes.

Each ADR should include:

- status
- context
- decision
- rationale
- consequences

If a future task changes the documentation operating model, update or add an ADR.

## Task Completion Rules

Every major completed task or group must update at least one of:

- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/reports/`
- `docs/evidence/`
- `docs/decisions/`
- `docs/adr/`

The selected surface should match the work performed. If a task makes or changes a strategic or technical decision, it must create or update a decision record.

Exception: a task may skip these updates only when it explicitly says documentation memory updates are exempted or when the task is purely mechanical and does not change project state, evidence, reports, decisions, roadmap, or review workflow.

When in doubt, update the smallest accurate memory surface.
