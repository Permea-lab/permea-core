# Review Hub

This hub is the reviewer-facing map for the current Permea Core public repository state. It points to doctrine, decisions, evidence, reports, risks, and continuation workflow needed to resume work safely.

## Project Identity

Permea Core is the public execution and specification layer for benchmark-first, sequence-first biological delivery engineering.

Primary public repository role:

- define reusable public artifact standards
- generate deterministic public artifact examples
- validate local metadata and generated surfaces
- record major strategic and technical decisions
- keep computational evidence separate from biological, clinical, or performance claims

## Current Public Truth

The repository currently supports local artifact generation, validation, reproducibility, evaluation packet generation, dry-run reporting, generated evidence navigation, public artifact specification inspection, decision records, and project memory.

The repository does not currently prove biological transport, mechanism, safety, therapeutic effect, clinical effectiveness, generalization, model performance, data acquisition completion, or redistribution rights.

## Current Branch / Commit

Use live Git state as the source of truth:

```bash
git status --short --branch
git log -1 --oneline
```

At this update point, the reviewed public baseline was `main` at `d1806acf83d327855d69a0b1be999f8adcb8a40e`.

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

## Current State Summary

- Public evidence surface exists at [docs/examples/generated/README.md](docs/examples/generated/README.md).
- Reproducibility and evaluation bundles exist at [REPRODUCIBILITY.md](REPRODUCIBILITY.md) and [EVALUATION.md](EVALUATION.md).
- Public artifact specifications exist at [docs/specs/README.md](docs/specs/README.md).
- Decision records exist at [docs/decisions/README.md](docs/decisions/README.md).
- Artifact schemas exist under [schemas/](schemas/).
- Current artifact-system commands are listed in [QUICKSTART.md](QUICKSTART.md).
- Claim boundary and paper-alignment policy are public and should govern public wording.

## Research Status

Current research posture is infrastructure-first. Permea Core defines and validates artifact structures for computational delivery evidence, but does not publish wet-lab findings or model-performance claims from this repository.

Paper-related status:

- [Paper Alignment Policy](docs/paper-alignment/PAPER_ALIGNMENT_POLICY.md) exists.
- No public preprint-readiness claim should be made from this repository unless a future release gate records that approval.

## Evidence Index

- [Generated evidence surface](docs/examples/generated/README.md)
- [Artifact index](docs/examples/generated/ARTIFACT_INDEX.md)
- [Evidence matrix](docs/examples/generated/EVIDENCE_MATRIX.md)
- [Demo packet](docs/examples/generated/DEMO_PACKET.md)
- [Evaluation packet](docs/examples/generated/EVALUATION_PACKET.md)
- [Reproducibility report](docs/examples/generated/REPRODUCIBILITY_REPORT.md)
- [Benchmark dry-run report](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)
- [Source registry](sources/registry.yaml)
- [Benchmark registry](benchmarks/registry.yaml)
- [Artifact schemas](schemas/)

## Decision Index

- [DEC-001: Reproducibility-first program structure](docs/decisions/DEC-001-reproducibility-first-program-structure.md)
- [DEC-002: Evidence bundle before claims](docs/decisions/DEC-002-evidence-bundle-before-claims.md)
- [DEC-003: Evaluation bundle as user transfer layer](docs/decisions/DEC-003-evaluation-bundle-as-user-transfer-layer.md)
- [DEC-004: Specification layer for Permea standard](docs/decisions/DEC-004-specification-layer-for-permea-standard.md)
- [DEC-005: No production or clinical claims without evidence](docs/decisions/DEC-005-no-production-or-clinical-claims-without-evidence.md)
- [DEC-006: Project memory layer required for continuation](docs/decisions/DEC-006-project-memory-layer-required-for-continuation.md)

## Report Index

- [P-CORE-036 artifact specification layer](docs/reports/p-core-036-artifact-specification-layer.md)
- [P-DOC-001 project operating-system adoption v0](docs/reports/p-doc-001-project-operating-system-adoption-v0.md)
- [P-DOC-004 decision and documentation backfill v0](docs/reports/p-doc-004-decision-and-documentation-backfill-v0.md)

Generated report-like surfaces:

- [Reproducibility report](docs/examples/generated/REPRODUCIBILITY_REPORT.md)
- [Evaluation packet](docs/examples/generated/EVALUATION_PACKET.md)
- [Evidence matrix](docs/examples/generated/EVIDENCE_MATRIX.md)

## ADR Index

- [ADR-0001: Open-source-first](docs/adr/ADR-0001-open-source-first.md)
- [ADR-0002: Benchmark-first](docs/adr/ADR-0002-benchmark-first.md)
- [ADR-001: Project breadcrumb and review hub standard](docs/adr/ADR-001-project-breadcrumb-and-review-hub-standard.md)

## Claim Boundary Summary

Allowed public framing:

- open technical foundation
- benchmark-first infrastructure
- deterministic artifact generation and validation
- public artifact standards
- computational evidence surfaces
- candidate prioritization before experimental follow-up

Current non-claims:

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical-effectiveness claim
- no model performance claim
- no state-of-the-art claim
- no solved-delivery claim

Use [Claim Boundary](docs/CLAIM_BOUNDARY.md) and [Claim Registry](docs/scientific-governance/CLAIM_REGISTRY.md) before changing public claims.

## Current Risks

- Generated files can become stale if generators are changed without regeneration.
- Public docs can drift from claim-boundary and paper-alignment policy.
- Artifact specifications can become too narrow if future work overfits them to one example.
- New evidence surfaces can become hard to review if they are not linked from the hub and breadcrumb.
- Decision records can become stale if strategic or technical choices change without updating the Decision Layer.

## Current Open Questions

- When should artifact schemas move from structure-only checks to a dedicated validator bundle?
- Which contribution workflows should require schema validation before review?
- Which generated surfaces should become release-gated artifacts?
- How should future paper or report drafts cite generated evidence without expanding claims?
- Which decisions should later be promoted into ADRs because they affect repository architecture?

## Recommended Next Tasks

1. Review and merge the decision and documentation backfill branch if validation and scans remain clean.
2. Backfill only remaining decision-critical documentation gaps.
3. Add a dedicated artifact-spec validator bundle in a separate scoped task.
4. Keep generated evidence surfaces, reports, and decision records refreshed as new artifact families are added.
5. Keep the claim boundary and paper-alignment policy synchronized with any new public report.

## How To Resume With A Review Assistant

Start with:

- [OPEN_THIS_FIRST.md](OPEN_THIS_FIRST.md)
- [REVIEW_HUB.md](REVIEW_HUB.md)
- [Claim Boundary](docs/CLAIM_BOUNDARY.md)
- [Decision Records](docs/decisions/README.md)
- [Generated evidence surface](docs/examples/generated/README.md)

Ask the session to inspect live Git state before giving implementation guidance.

## How To Resume With A Coding Agent

Start from the repository root and run:

```bash
git status --short --branch
git log -1 --oneline
python3 scripts/permea_specs.py
python3 scripts/permea_validate.py
```

Before completing a task, the coding agent should update the relevant memory surface for the work completed. If the task makes or changes a strategic or technical decision, it must create or update a [Decision Record](docs/decisions/README.md).
