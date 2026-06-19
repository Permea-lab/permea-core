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

The repository currently supports local artifact generation, artifact validation, a first-user quickstart demo, public review packet guidance, evidence review packet generation, benchmark registry and execution governance, dataset registry governance, research package governance, signal integration for adjacent public evidence packages, evidence lineage and provenance governance, reproducibility, evaluation packet generation, dry-run reporting, generated evidence navigation, public evidence records, evidence navigation docs, public artifact specification inspection, copyable external examples, decision records, and project memory.

The repository does not currently prove biological transport, mechanism, safety, therapeutic effect, clinical effectiveness, generalization, model performance, data acquisition completion, or redistribution rights.

## Current Branch / Commit

Use live Git state as the source of truth:

```bash
git status --short --branch
git log -1 --oneline
```

At this update point, the reviewed public baseline was `main` at `6a3d60ce06f7a7f53179a406d4297edf22c71382`.

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
| Benchmark Registry Layer | Implemented | Benchmark registry, lifecycle, card template, governance, schema, and CLI review. |
| Benchmark Execution Layer | Implemented | Benchmark execution model, run template, schema, deterministic CLI review, validation path, and claim boundaries. |
| Dataset Registry Layer | Implemented | Dataset registry, lifecycle, card template, provenance, governance, schema, and CLI review. |
| Research Package Layer | Implemented | Research package registry, lifecycle, template, assembly, governance, schema, and CLI review. |
| Signal Integration Layer | Implemented | External evidence package integration docs, template, governance, schema, deterministic CLI review, and repository-boundary guidance. |
| Evidence Lineage Layer | Implemented | Lineage model, governance, review guide, record template, schema, deterministic CLI review, provenance reminders, and claim boundaries. |
| Public Review Packet Layer | Implemented | Guided public packet, checklist, assembly, governance, schema, and CLI review. |
| Evidence Review Packet System | Implemented | Generated reviewer packets for selected public artifact systems with concrete files, validation commands, claim boundaries, and limitations. |
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
- Architecture index exists at [docs/architecture/README.md](docs/architecture/README.md).
- Artifact consistency docs exist at [docs/artifacts/README.md](docs/artifacts/README.md).
- Artifact consistency command exists at [scripts/permea_artifacts.py](scripts/permea_artifacts.py).
- Evidence review packet system docs exist at [docs/review/review-packet-system.md](docs/review/review-packet-system.md).
- Evidence review packet generator exists at [scripts/permea_review_packet.py](scripts/permea_review_packet.py).
- Review loop operating standard exists at [docs/review/review-loop-operating-standard.md](docs/review/review-loop-operating-standard.md).
- P-CORE-030 evidence surface layer review packet exists at [docs/review/packets/p-core-030-evidence-surface-layer.md](docs/review/packets/p-core-030-evidence-surface-layer.md).
- P-CORE-032 reproducibility bundle review packet exists at [docs/review/packets/p-core-032-reproducibility-bundle.md](docs/review/packets/p-core-032-reproducibility-bundle.md).
- P-CORE-034 evaluation bundle review packet exists at [docs/review/packets/p-core-034-evaluation-bundle.md](docs/review/packets/p-core-034-evaluation-bundle.md).
- P-CORE-047 public review packet layer review packet exists at [docs/review/packets/p-core-047-public-review-packet-layer.md](docs/review/packets/p-core-047-public-review-packet-layer.md).
- P-CORE-053 artifact consistency review packet exists at [docs/review/packets/p-core-053-artifact-consistency-system.md](docs/review/packets/p-core-053-artifact-consistency-system.md).
- Reports index exists at [docs/reports/README.md](docs/reports/README.md).
- Benchmark registry exists at [docs/benchmarks/benchmark-registry.md](docs/benchmarks/benchmark-registry.md).
- Benchmark lifecycle exists at [docs/benchmarks/benchmark-lifecycle.md](docs/benchmarks/benchmark-lifecycle.md).
- Benchmark card template exists at [docs/benchmarks/benchmark-card-template.md](docs/benchmarks/benchmark-card-template.md).
- Benchmark execution model exists at [docs/benchmarks/benchmark-execution-model.md](docs/benchmarks/benchmark-execution-model.md).
- Benchmark run template exists at [docs/benchmarks/benchmark-run-template.md](docs/benchmarks/benchmark-run-template.md).
- Benchmark governance exists at [docs/benchmarks/benchmark-governance.md](docs/benchmarks/benchmark-governance.md).
- Benchmark review command exists at [scripts/permea_benchmarks.py](scripts/permea_benchmarks.py).
- Benchmark execution review command exists at [scripts/permea_benchmark_run.py](scripts/permea_benchmark_run.py).
- Dataset registry exists at [docs/datasets/dataset-registry.md](docs/datasets/dataset-registry.md).
- Dataset lifecycle exists at [docs/datasets/dataset-lifecycle.md](docs/datasets/dataset-lifecycle.md).
- Dataset card template exists at [docs/datasets/dataset-card-template.md](docs/datasets/dataset-card-template.md).
- Dataset provenance exists at [docs/datasets/dataset-provenance.md](docs/datasets/dataset-provenance.md).
- Dataset governance exists at [docs/datasets/dataset-governance.md](docs/datasets/dataset-governance.md).
- Dataset review command exists at [scripts/permea_datasets.py](scripts/permea_datasets.py).
- Research package registry exists at [docs/research/research-package-registry.md](docs/research/research-package-registry.md).
- Research package lifecycle exists at [docs/research/research-package-lifecycle.md](docs/research/research-package-lifecycle.md).
- Research package template exists at [docs/research/research-package-template.md](docs/research/research-package-template.md).
- Research package assembly exists at [docs/research/research-package-assembly.md](docs/research/research-package-assembly.md).
- Research package governance exists at [docs/research/research-package-governance.md](docs/research/research-package-governance.md).
- Research package review command exists at [scripts/permea_research.py](scripts/permea_research.py).
- Signal integration docs exist at [docs/integrations/README.md](docs/integrations/README.md).
- Permea Signal ML integration exists at [docs/integrations/permea-signal-ml.md](docs/integrations/permea-signal-ml.md).
- External evidence package template exists at [docs/integrations/external-evidence-package-template.md](docs/integrations/external-evidence-package-template.md).
- External evidence package governance exists at [docs/integrations/external-evidence-package-governance.md](docs/integrations/external-evidence-package-governance.md).
- Signal integration review command exists at [scripts/permea_signal.py](scripts/permea_signal.py).
- Evidence lineage docs exist at [docs/lineage/README.md](docs/lineage/README.md).
- Lineage model exists at [docs/lineage/lineage-model.md](docs/lineage/lineage-model.md).
- Lineage governance exists at [docs/lineage/lineage-governance.md](docs/lineage/lineage-governance.md).
- Lineage review guide exists at [docs/lineage/lineage-review-guide.md](docs/lineage/lineage-review-guide.md).
- Lineage record template exists at [docs/lineage/lineage-record-template.md](docs/lineage/lineage-record-template.md).
- Evidence lineage review command exists at [scripts/permea_lineage.py](scripts/permea_lineage.py).
- Public review packet exists at [docs/review/public-review-packet.md](docs/review/public-review-packet.md).
- Public review packet assembly exists at [docs/review/public-review-packet-assembly.md](docs/review/public-review-packet-assembly.md).
- Public review checklist exists at [docs/review/public-review-checklist.md](docs/review/public-review-checklist.md).
- Public review packet command exists at [scripts/permea_review.py](scripts/permea_review.py).
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
- [Review packet layer](docs/review/README.md)
- [Architecture index](docs/architecture/README.md)
- [Artifact consistency](docs/artifacts/README.md)
- [Evidence review packet system](docs/review/review-packet-system.md)
- [Review loop operating standard](docs/review/review-loop-operating-standard.md)
- [P-CORE-030 evidence surface layer review packet](docs/review/packets/p-core-030-evidence-surface-layer.md)
- [P-CORE-032 reproducibility bundle review packet](docs/review/packets/p-core-032-reproducibility-bundle.md)
- [P-CORE-034 evaluation bundle review packet](docs/review/packets/p-core-034-evaluation-bundle.md)
- [P-CORE-047 public review packet layer review packet](docs/review/packets/p-core-047-public-review-packet-layer.md)
- [P-CORE-053 artifact consistency review packet](docs/review/packets/p-core-053-artifact-consistency-system.md)
- [Reports index](docs/reports/README.md)
- [Benchmark registry](docs/benchmarks/benchmark-registry.md)
- [Benchmark layer](docs/benchmarks/README.md)
- [Benchmark lifecycle](docs/benchmarks/benchmark-lifecycle.md)
- [Benchmark execution model](docs/benchmarks/benchmark-execution-model.md)
- [Benchmark governance](docs/benchmarks/benchmark-governance.md)
- [Dataset registry](docs/datasets/dataset-registry.md)
- [Dataset layer](docs/datasets/README.md)
- [Dataset lifecycle](docs/datasets/dataset-lifecycle.md)
- [Dataset provenance](docs/datasets/dataset-provenance.md)
- [Research package registry](docs/research/research-package-registry.md)
- [Research package layer](docs/research/README.md)
- [Research package lifecycle](docs/research/research-package-lifecycle.md)
- [Research package assembly](docs/research/research-package-assembly.md)
- [Signal integration](docs/integrations/README.md)
- [Permea Signal ML integration](docs/integrations/permea-signal-ml.md)
- [Evidence lineage](docs/lineage/README.md)
- [Lineage model](docs/lineage/lineage-model.md)
- [Lineage review guide](docs/lineage/lineage-review-guide.md)
- [Public review packet](docs/review/public-review-packet.md)
- [Public review checklist](docs/review/public-review-checklist.md)
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

- [Reports index](docs/reports/README.md)
- [P-CORE-036 artifact specification layer](docs/reports/p-core-036-artifact-specification-layer.md)
- [P-DOC-001 project operating-system adoption v0](docs/reports/p-doc-001-project-operating-system-adoption-v0.md)
- [P-DOC-004 decision and documentation backfill v0](docs/reports/p-doc-004-decision-and-documentation-backfill-v0.md)
- [P-DOC-007 evidence layer bootstrap v0](docs/reports/p-doc-007-evidence-layer-bootstrap-v0.md)
- [P-CORE-038 artifact validator bundle v0](docs/reports/p-core-038-artifact-validator-bundle-v0.md)
- [P-CORE-040 external example packages v0](docs/reports/p-core-040-external-example-packages-v0.md)
- [P-CORE-042 quickstart experience layer v0](docs/reports/p-core-042-quickstart-experience-layer-v0.md)
- [P-CORE-043 evidence navigation map](docs/evidence/evidence-map.md)
- [P-CORE-044 benchmark registry layer v0](docs/reports/p-core-044-benchmark-registry-layer-v0.md)
- [P-CORE-045 dataset registry layer v0](docs/reports/p-core-045-dataset-registry-layer-v0.md)
- [P-CORE-046 research package layer v0](docs/reports/p-core-046-research-package-layer-v0.md)
- [P-CORE-047 public review packet layer v0](docs/reports/p-core-047-public-review-packet-layer-v0.md)
- [P-CORE-048 benchmark execution layer v0](docs/reports/p-core-048-benchmark-execution-layer-v0.md)
- [P-CORE-049 signal integration layer v0](docs/reports/p-core-049-signal-integration-layer-v0.md)
- [P-CORE-050 evidence lineage layer v0](docs/reports/p-core-050-evidence-lineage-layer-v0.md)
- [P-CORE-051 long-run supervisor pilot v0](docs/reports/p-core-051-long-run-supervisor-pilot-v0.md)
- [P-CORE-052 autonomous queue pilot v0](docs/reports/p-core-052-autonomous-queue-pilot-v0.md)
- [P-CORE-053 artifact consistency system v0](docs/reports/p-core-053-artifact-consistency-system-v0.md)
- [P-CORE-054 evidence review packet system v0](docs/reports/p-core-054-evidence-review-packet-system-v0.md)
- [P-CORE-059 review packet expansion v0](docs/reports/p-core-059-review-packet-expansion-v0.md)
- [P-CORE-061 autonomous review-merge loop pilot v0](docs/reports/p-core-061-autonomous-review-merge-loop-pilot-v0.md)

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
- deterministic benchmark review command for registry counts, lifecycle status, docs, and claim boundaries
- deterministic benchmark execution command for framework status, benchmark run artifact status, validation reminders, docs, and claim boundaries
- deterministic dataset review command for registry counts, provenance status, docs, and claim boundaries
- deterministic research package review command for package counts, reproducibility status, docs, and claim boundaries
- deterministic signal integration command for external evidence package status, linked Core layers, repository-boundary reminders, validation reminders, docs, and claim boundaries
- deterministic evidence lineage command for lineage-capable artifact classes, status categories, provenance reminders, docs, and claim boundaries
- deterministic public review packet command for reviewer path, registry commands, validation commands, and claim boundaries
- deterministic evidence review packet command for selected public artifact systems, concrete review files, validation commands, claim boundaries, and limitations
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
- Benchmark registry layer: Implemented for benchmark registry, lifecycle, card template, governance, schema, and CLI review.
- Benchmark execution layer: Implemented for execution model, run template, run schema, CLI review, validation path, and claim boundaries.
- Dataset registry layer: Implemented for dataset registry, lifecycle, card template, provenance, governance, schema, and CLI review.
- Research package layer: Implemented for research package registry, lifecycle, template, assembly, governance, schema, and CLI review.
- Signal integration layer: Implemented for external evidence package docs, template, governance, schema, deterministic CLI review, and repository-boundary guidance.
- Evidence lineage layer: Implemented for lineage model, governance, review guide, record template, schema, deterministic CLI review, provenance reminders, and claim boundaries.
- Public review packet layer: Implemented for guided packet, checklist, assembly, governance, schema, and CLI review.
- Architecture navigation: Implemented as a compact index over existing architecture, specification, decision, ADR, and lineage surfaces.
- Report navigation: Implemented as a compact index over public implementation, evidence, review, and maintenance reports.
- Artifact consistency system: Implemented for public markdown inventory, local link existence, review-surface reachability, reports-index coverage, deterministic CLI review, and regression tests.
- Evidence review packet system: Implemented for generated review packets, concrete artifact links, validation commands, claim-boundary notes, reviewer checklists, limitations, deterministic CLI generation, and regression tests.

## Validation Status

Current evidence-layer validation uses:

```bash
python3 scripts/permea_check.py
python3 scripts/permea_demo.py
python3 scripts/permea_artifacts.py
python3 scripts/permea_review_packet.py
python3 scripts/permea_evidence.py
python3 scripts/permea_benchmarks.py
python3 scripts/permea_benchmark_run.py
python3 scripts/permea_datasets.py
python3 scripts/permea_research.py
python3 scripts/permea_signal.py
python3 scripts/permea_lineage.py
python3 scripts/permea_review.py
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

1. Review the P-CORE-059 review packet expansion branch if validation and scans remain clean.
2. Add external evidence package records only when repository boundaries, schema metadata, reproducibility, validation, and claim-boundary requirements are met.
3. Add benchmark run artifacts only when schema, evidence, validation, reproducibility, and claim-boundary requirements are met.
4. Promote additional review packets only when evidence, benchmark, dataset, research, signal integration, claim, validation, and reproducibility links are current.
5. Promote research packages only when lifecycle evidence, dataset, benchmark, reproducibility, validation, and claim-boundary requirements are met.
6. Promote dataset entries only when lifecycle provenance and evidence requirements are met.
7. Keep generated evidence surfaces, reports, decision records, and evidence records refreshed as new artifact families are added.
8. Keep the claim boundary and paper-alignment policy synchronized with any new public report.

## How To Resume With A Review Assistant

Start with:

- [OPEN_THIS_FIRST.md](OPEN_THIS_FIRST.md)
- [REVIEW_HUB.md](REVIEW_HUB.md)
- [Claim Boundary](docs/CLAIM_BOUNDARY.md)
- [Claim Registry](docs/claims/claim-registry.md)
- [Evidence Layer](docs/evidence/README.md)
- [Architecture index](docs/architecture/README.md)
- [Artifact consistency](docs/artifacts/README.md)
- [Evidence review packet system](docs/review/review-packet-system.md)
- [P-CORE-030 evidence surface layer review packet](docs/review/packets/p-core-030-evidence-surface-layer.md)
- [P-CORE-032 reproducibility bundle review packet](docs/review/packets/p-core-032-reproducibility-bundle.md)
- [P-CORE-034 evaluation bundle review packet](docs/review/packets/p-core-034-evaluation-bundle.md)
- [P-CORE-047 public review packet layer review packet](docs/review/packets/p-core-047-public-review-packet-layer.md)
- [P-CORE-053 artifact consistency review packet](docs/review/packets/p-core-053-artifact-consistency-system.md)
- [Reports index](docs/reports/README.md)
- [Evidence map](docs/evidence/evidence-map.md)
- [Claim-to-evidence matrix](docs/evidence/claim-to-evidence-matrix.md)
- [Benchmark registry](docs/benchmarks/benchmark-registry.md)
- [Benchmark execution model](docs/benchmarks/benchmark-execution-model.md)
- [Signal integration](docs/integrations/README.md)
- [Evidence lineage](docs/lineage/README.md)
- [Decision Records](docs/decisions/README.md)
- [Generated evidence surface](docs/examples/generated/README.md)

Ask the session to inspect live Git state before giving implementation guidance.

## How To Resume With A Coding Agent

Start from the repository root and run:

```bash
git status --short --branch
git log -1 --oneline
python3 scripts/permea_demo.py
python3 scripts/permea_artifacts.py
python3 scripts/permea_review_packet.py
python3 scripts/permea_evidence.py
python3 scripts/permea_benchmarks.py
python3 scripts/permea_benchmark_run.py
python3 scripts/permea_datasets.py
python3 scripts/permea_research.py
python3 scripts/permea_signal.py
python3 scripts/permea_lineage.py
python3 scripts/permea_review.py
python3 scripts/permea_specs.py
python3 scripts/permea_check.py
python3 scripts/permea_check.py examples/synthetic_reference_example
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest
```

Before completing a task, the coding agent should update the relevant memory surface for the work completed. If the task makes or changes a strategic or technical decision, it must create or update a [Decision Record](docs/decisions/README.md).
