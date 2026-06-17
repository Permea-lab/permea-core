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

The repository currently supports local artifact generation, artifact validation, a first-user quickstart demo, reproducibility, evaluation packet generation, dry-run reporting, generated evidence navigation, public evidence records, evidence navigation docs, public artifact specification inspection, copyable external examples, decision records, and project memory.

The repository does not currently prove biological transport, mechanism, safety, therapeutic effect, clinical effectiveness, generalization, model performance, data acquisition completion, or redistribution rights.

## Current Branch / Commit

Use live Git state as the source of truth:

```bash
git status --short --branch
git log -1 --oneline
```

At this update point, the reviewed public baseline was `main` at `019eae46adfbe0fea1aca39104a004eb74ce0cc2`.

## Permea Layer Model

| Layer | Status | Role |
| --- | --- | --- |
| Doctrine Layer | Established | Public principles, claim boundaries, governance, and research posture. |
| Decision Layer | Developing | Durable records for strategic and technical choices. |
| Evidence Layer | Strong | Generated evidence surfaces, artifact indexes, matrices, and dry-run reports. |
| Reproducibility Layer | Strong | Local commands and reports that regenerate and validate current public artifacts. |
| Evaluation Layer | Strong | Template/reference packet for transferring the artifact pattern to users. |
| Specification Layer | Strong | Public standards and schemas for artifact families. |
| Standard Enforcement Layer | Developing | Lightweight public artifact checks for current example files. |
| Example Layer | Developing | Copyable public-safe reference packages for external users. |
| Quickstart Experience Layer | Implemented | One-command first-user path for discovery, validation, evidence links, and non-claims. |
| Evidence Navigation Layer | Implemented | Evidence map, claim matrix, maturity model, timeline, and CLI for review. |
| Memory Layer | Established | Breadcrumb, review hub, ADR, runbook, and reports for continuation. |

## Current State Summary

- Public evidence surface exists at [docs/examples/generated/README.md](docs/examples/generated/README.md).
- Public evidence layer exists at [docs/evidence/README.md](docs/evidence/README.md).
- Public claim registry exists at [docs/claims/claim-registry.md](docs/claims/claim-registry.md).
- Reproducibility and evaluation bundles exist at [REPRODUCIBILITY.md](REPRODUCIBILITY.md) and [EVALUATION.md](EVALUATION.md).
- Public artifact specifications exist at [docs/specs/README.md](docs/specs/README.md).
- Public artifact validator exists at [scripts/permea_check.py](scripts/permea_check.py).
- Quickstart demo exists at [scripts/permea_demo.py](scripts/permea_demo.py).
- Evidence review command exists at [scripts/permea_evidence.py](scripts/permea_evidence.py).
- Evidence map exists at [docs/evidence/evidence-map.md](docs/evidence/evidence-map.md).
- Claim-to-evidence matrix exists at [docs/evidence/claim-to-evidence-matrix.md](docs/evidence/claim-to-evidence-matrix.md).
- Evidence maturity model exists at [docs/evidence/evidence-maturity-model.md](docs/evidence/evidence-maturity-model.md).
- Evidence timeline exists at [docs/evidence/evidence-timeline.md](docs/evidence/evidence-timeline.md).
- External example packages exist at [examples/README.md](examples/README.md).
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
- [Evidence layer](docs/evidence/README.md)
- [Evidence index](docs/evidence/evidence-index.md)
- [Evidence map](docs/evidence/evidence-map.md)
- [Claim-to-evidence matrix](docs/evidence/claim-to-evidence-matrix.md)
- [Evidence maturity model](docs/evidence/evidence-maturity-model.md)
- [Evidence timeline](docs/evidence/evidence-timeline.md)
- [EVIDENCE-030: Evidence Surface Layer](docs/evidence/EVIDENCE-030-evidence-surface-layer.md)
- [EVIDENCE-032: Reproducibility Bundle](docs/evidence/EVIDENCE-032-reproducibility-bundle.md)
- [EVIDENCE-034: Evaluation Bundle](docs/evidence/EVIDENCE-034-evaluation-bundle.md)
- [EVIDENCE-036: Artifact Specification Layer](docs/evidence/EVIDENCE-036-artifact-specification-layer.md)
- [EVIDENCE-038: Artifact Validator Bundle](docs/evidence/EVIDENCE-038-artifact-validator-bundle.md)
- [EVIDENCE-040: External Example Packages](docs/evidence/EVIDENCE-040-external-example-packages.md)
- [EVIDENCE-042: Quickstart Experience Layer](docs/evidence/EVIDENCE-042-quickstart-experience-layer.md)
- [EVIDENCE-043: Evidence Navigation Layer](docs/evidence/evidence-map.md)
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
- [P-DOC-007 evidence layer bootstrap v0](docs/reports/p-doc-007-evidence-layer-bootstrap-v0.md)
- [P-CORE-038 artifact validator bundle v0](docs/reports/p-core-038-artifact-validator-bundle-v0.md)
- [P-CORE-040 external example packages v0](docs/reports/p-core-040-external-example-packages-v0.md)
- [P-CORE-042 quickstart experience layer v0](docs/reports/p-core-042-quickstart-experience-layer-v0.md)
- [P-CORE-043 evidence navigation map](docs/evidence/evidence-map.md)

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
- deterministic quickstart demo for example discovery and validator execution
- deterministic evidence review command for inventory, claim boundaries, maturity, and validation status
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

Use [Public Claim Registry](docs/claims/claim-registry.md), [Claim Boundary](docs/CLAIM_BOUNDARY.md), and [Scientific Claim Registry](docs/scientific-governance/CLAIM_REGISTRY.md) before changing public claims.

## Current Technical Surface

- Artifact generation: Implemented through local scripts and generated example outputs.
- Reproducibility bundle: Implemented and Public-Safe.
- Evaluation bundle: Implemented and Public-Safe.
- Artifact specifications: Implemented and Public-Safe.
- Evidence layer: Implemented and Public-Safe.
- Artifact validator bundle: Implemented for current public example artifact families.
- External examples: Implemented for three public-safe reference packages.
- Quickstart demo: Implemented for first-user discovery, validation, evidence links, and next commands.
- Evidence navigation: Implemented for evidence inventory, claim-to-evidence mapping, maturity levels, timeline, and CLI review.

## Validation Status

Current evidence-layer validation uses:

```bash
python3 scripts/permea_check.py
python3 scripts/permea_demo.py
python3 scripts/permea_evidence.py
python3 scripts/permea_check.py examples/synthetic_reference_example
python3 scripts/permea_specs.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
```

## Current Risks

- Generated files can become stale if generators are changed without regeneration.
- Public docs can drift from claim-boundary and paper-alignment policy.
- Artifact specifications can become too narrow if future work overfits them to one example.
- New evidence surfaces can become hard to review if they are not linked from the hub and breadcrumb.
- Decision records can become stale if strategic or technical choices change without updating the Decision Layer.
- Evidence records can become stale if reports, generated artifacts, or validation surfaces change without an evidence-layer refresh.
- Validator checks can drift if public artifact specs are changed without matching tests.
- External examples can become misleading if they are not kept template-oriented and explicit about non-claims.

## Current Open Questions

- When should artifact schemas move from lightweight checks to stricter schema enforcement?
- Which contribution workflows should require schema validation before review?
- Which future example packages should be added only after the current examples are reviewed by external users?
- Which generated surfaces should become release-gated artifacts?
- How should future paper or report drafts cite generated evidence without expanding claims?
- Which decisions should later be promoted into ADRs because they affect repository architecture?

## Recommended Next Tasks

1. Review the evidence navigation branch if validation and scans remain clean.
2. Extend example packages only when public-safe fixture values and validator coverage are ready.
3. Extend validator coverage only when new public artifact families or stricter schemas require it.
4. Add evidence records for future merged artifact or validation layers.
5. Keep generated evidence surfaces, reports, decision records, and evidence records refreshed as new artifact families are added.
6. Keep the claim boundary and paper-alignment policy synchronized with any new public report.

## How To Resume With A Review Assistant

Start with:

- [OPEN_THIS_FIRST.md](OPEN_THIS_FIRST.md)
- [REVIEW_HUB.md](REVIEW_HUB.md)
- [Claim Boundary](docs/CLAIM_BOUNDARY.md)
- [Claim Registry](docs/claims/claim-registry.md)
- [Evidence Layer](docs/evidence/README.md)
- [Evidence map](docs/evidence/evidence-map.md)
- [Claim-to-evidence matrix](docs/evidence/claim-to-evidence-matrix.md)
- [Decision Records](docs/decisions/README.md)
- [Generated evidence surface](docs/examples/generated/README.md)

Ask the session to inspect live Git state before giving implementation guidance.

## How To Resume With A Coding Agent

Start from the repository root and run:

```bash
git status --short --branch
git log -1 --oneline
python3 scripts/permea_demo.py
python3 scripts/permea_evidence.py
python3 scripts/permea_specs.py
python3 scripts/permea_check.py
python3 scripts/permea_check.py examples/synthetic_reference_example
python3 scripts/permea_validate.py
```

Before completing a task, the coding agent should update the relevant memory surface for the work completed. If the task makes or changes a strategic or technical decision, it must create or update a [Decision Record](docs/decisions/README.md).
