# Open This First

This file is the first continuation breadcrumb for Permea Core. It summarizes the current public state so a reviewer, contributor, or new session can continue without reading historical chat logs.

## Current Status

Permea Core is a public, benchmark-first infrastructure repository for sequence-first biological delivery engineering. The current repository state emphasizes reproducible artifact generation, public review packet guidance, public evidence navigation, evidence lineage and provenance governance, benchmark registry and execution governance, dataset and research package registry governance, signal integration for adjacent public evidence packages, public evidence indexing, evaluation and reproducibility bundles, artifact specifications, artifact validation, external examples, decision records, project memory, and bounded claim language.

Current public baseline when this breadcrumb was refreshed:

- Branch used for this update: `p-core-051-long-run-supervisor-pilot`
- Public baseline reviewed: `main` at `5ab200290fe77829f6f5483da983efc34e04b1a0`
- Refresh command: `git status --short --branch && git log -1 --oneline`

## Current Public Truth

Permea Core currently provides:

- public artifact specifications for dataset cards, benchmark cards, evidence cards, run manifests, and output packages
- a lightweight public artifact validator command for current public example artifacts
- copyable public-safe external example packages under `examples/`
- deterministic generated example artifact surfaces under `docs/examples/generated/`
- local commands for reproduction, validation, evaluation packet generation, dry-run generation, and specification registry inspection
- public evidence records under `docs/evidence/`
- evidence navigation docs at `docs/evidence/evidence-map.md`, `docs/evidence/claim-to-evidence-matrix.md`, `docs/evidence/evidence-maturity-model.md`, and `docs/evidence/evidence-timeline.md`
- an evidence review command at `python3 scripts/permea_evidence.py`
- architecture navigation at `docs/architecture/README.md`
- public claim registry at `docs/claims/claim-registry.md`
- decision records for major program choices under `docs/decisions/`
- public claim-boundary and paper-alignment policies
- lightweight schemas under `schemas/`
- a first-user quickstart demo at `python3 scripts/permea_demo.py`
- a benchmark registry layer at `docs/benchmarks/`
- a benchmark review command at `python3 scripts/permea_benchmarks.py`
- a benchmark execution layer at `docs/benchmarks/benchmark-execution-model.md`
- a benchmark execution review command at `python3 scripts/permea_benchmark_run.py`
- a dataset registry layer at `docs/datasets/`
- a dataset review command at `python3 scripts/permea_datasets.py`
- a research package layer at `docs/research/`
- a research package review command at `python3 scripts/permea_research.py`
- a signal integration layer at `docs/integrations/`
- a signal integration review command at `python3 scripts/permea_signal.py`
- an evidence lineage layer at `docs/lineage/`
- an evidence lineage review command at `python3 scripts/permea_lineage.py`
- a public review packet layer at `docs/review/`
- a public review packet command at `python3 scripts/permea_review.py`

Permea Core does not currently claim dataset download, acquisition execution, redistribution-rights confirmation, wet-lab validation by Permea, clinical effectiveness, model performance, state-of-the-art status, or solved delivery.

## Permea Layer Model

Permea's current public program model is:

- Doctrine Layer: Established
- Decision Layer: Developing
- Evidence Layer: Strong
- Reproducibility Layer: Strong
- Evaluation Layer: Strong
- Specification Layer: Strong
- Memory Layer: Established
- Example Layer: Developing
- Quickstart Experience Layer: Implemented
- Evidence Navigation Layer: Implemented
- Benchmark Registry Layer: Implemented
- Benchmark Execution Layer: Implemented
- Dataset Registry Layer: Implemented
- Research Package Layer: Implemented
- Signal Integration Layer: Implemented
- Evidence Lineage Layer: Implemented
- Public Review Packet Layer: Implemented

See [Evidence Layer](docs/evidence/README.md), [Evidence Index](docs/evidence/evidence-index.md), and [Decision Records](docs/decisions/README.md) for the current review surfaces.

## Last Completed Major Work

The latest completed major public infrastructure layer is the evidence lineage layer:

- [Benchmark registry](docs/benchmarks/benchmark-registry.md)
- [Benchmark lifecycle](docs/benchmarks/benchmark-lifecycle.md)
- [Benchmark card template](docs/benchmarks/benchmark-card-template.md)
- [Benchmark execution model](docs/benchmarks/benchmark-execution-model.md)
- [Benchmark run template](docs/benchmarks/benchmark-run-template.md)
- [Benchmark governance](docs/benchmarks/benchmark-governance.md)
- [Dataset registry](docs/datasets/dataset-registry.md)
- [Dataset lifecycle](docs/datasets/dataset-lifecycle.md)
- [Dataset card template](docs/datasets/dataset-card-template.md)
- [Dataset provenance](docs/datasets/dataset-provenance.md)
- [Dataset governance](docs/datasets/dataset-governance.md)
- [Research package registry](docs/research/research-package-registry.md)
- [Research package lifecycle](docs/research/research-package-lifecycle.md)
- [Research package template](docs/research/research-package-template.md)
- [Research package assembly](docs/research/research-package-assembly.md)
- [Research package governance](docs/research/research-package-governance.md)
- [Signal integration](docs/integrations/README.md)
- [Permea Signal ML integration](docs/integrations/permea-signal-ml.md)
- [External evidence package template](docs/integrations/external-evidence-package-template.md)
- [External evidence package governance](docs/integrations/external-evidence-package-governance.md)
- [Evidence lineage](docs/lineage/README.md)
- [Lineage model](docs/lineage/lineage-model.md)
- [Lineage governance](docs/lineage/lineage-governance.md)
- [Lineage review guide](docs/lineage/lineage-review-guide.md)
- [Lineage record template](docs/lineage/lineage-record-template.md)
- [Public review packet](docs/review/public-review-packet.md)
- [Public review packet assembly](docs/review/public-review-packet-assembly.md)
- [Public review checklist](docs/review/public-review-checklist.md)

## Current Branch / Commit

Use live Git state as the source of truth:

```bash
git status --short --branch
git log -1 --oneline
```

At this update, the reviewed public baseline was `5ab200290fe77829f6f5483da983efc34e04b1a0`.

## Primary Reports

- [P-CORE-036 artifact specification layer report](docs/reports/p-core-036-artifact-specification-layer.md)
- [P-DOC-001 project operating-system adoption report](docs/reports/p-doc-001-project-operating-system-adoption-v0.md)
- [P-DOC-004 decision and documentation backfill report](docs/reports/p-doc-004-decision-and-documentation-backfill-v0.md)
- [P-DOC-007 evidence layer bootstrap report](docs/reports/p-doc-007-evidence-layer-bootstrap-v0.md)
- [P-CORE-038 artifact validator bundle report](docs/reports/p-core-038-artifact-validator-bundle-v0.md)
- [P-CORE-040 external example packages report](docs/reports/p-core-040-external-example-packages-v0.md)
- [P-CORE-042 quickstart experience layer report](docs/reports/p-core-042-quickstart-experience-layer-v0.md)
- [P-CORE-044 benchmark registry layer report](docs/reports/p-core-044-benchmark-registry-layer-v0.md)
- [P-CORE-045 dataset registry layer report](docs/reports/p-core-045-dataset-registry-layer-v0.md)
- [P-CORE-046 research package layer report](docs/reports/p-core-046-research-package-layer-v0.md)
- [P-CORE-047 public review packet layer report](docs/reports/p-core-047-public-review-packet-layer-v0.md)
- [P-CORE-048 benchmark execution layer report](docs/reports/p-core-048-benchmark-execution-layer-v0.md)
- [P-CORE-049 signal integration layer report](docs/reports/p-core-049-signal-integration-layer-v0.md)
- [P-CORE-050 evidence lineage layer report](docs/reports/p-core-050-evidence-lineage-layer-v0.md)
- [P-CORE-051 long-run supervisor pilot report](docs/reports/p-core-051-long-run-supervisor-pilot-v0.md)
- [Generated reproducibility report](docs/examples/generated/REPRODUCIBILITY_REPORT.md)
- [Generated evaluation packet](docs/examples/generated/EVALUATION_PACKET.md)
- [Generated evidence matrix](docs/examples/generated/EVIDENCE_MATRIX.md)
- [Generated demo packet](docs/examples/generated/DEMO_PACKET.md)

## Primary Evidence

- [Generated evidence surface](docs/examples/generated/README.md)
- [Evidence layer](docs/evidence/README.md)
- [Evidence map](docs/evidence/evidence-map.md)
- [Claim-to-evidence matrix](docs/evidence/claim-to-evidence-matrix.md)
- [Evidence maturity model](docs/evidence/evidence-maturity-model.md)
- [Evidence timeline](docs/evidence/evidence-timeline.md)
- [Evidence index](docs/evidence/evidence-index.md)
- [Claim registry](docs/claims/claim-registry.md)
- [Architecture index](docs/architecture/README.md)
- [Artifact validator evidence](docs/evidence/EVIDENCE-038-artifact-validator-bundle.md)
- [External examples](examples/README.md)
- [External examples evidence](docs/evidence/EVIDENCE-040-external-example-packages.md)
- [Quickstart experience evidence](docs/evidence/EVIDENCE-042-quickstart-experience-layer.md)
- [Artifact index](docs/examples/generated/ARTIFACT_INDEX.md)
- [Benchmark dry-run report](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)
- [Source registry](sources/registry.yaml)
- [Benchmark registry](benchmarks/registry.yaml)
- [Artifact schemas](schemas/)
- [Public artifact specifications](docs/specs/README.md)
- [Benchmark registry](docs/benchmarks/benchmark-registry.md)
- [Benchmark lifecycle](docs/benchmarks/benchmark-lifecycle.md)
- [Benchmark execution model](docs/benchmarks/benchmark-execution-model.md)
- [Dataset registry](docs/datasets/dataset-registry.md)
- [Dataset provenance](docs/datasets/dataset-provenance.md)
- [Research package registry](docs/research/research-package-registry.md)
- [Research package assembly](docs/research/research-package-assembly.md)
- [Signal integration](docs/integrations/README.md)
- [Permea Signal ML integration](docs/integrations/permea-signal-ml.md)
- [Public review packet](docs/review/public-review-packet.md)
- [Public review checklist](docs/review/public-review-checklist.md)
- [Decision records](docs/decisions/README.md)

## Current Research Direction

Current work should continue strengthening Permea Core as public infrastructure:

- keep artifact standards inspectable and easy to extend
- keep artifact validation aligned with public specifications and evidence-linkage expectations
- keep examples copyable, validator-compatible, and explicitly claim-bounded
- keep generation and validation deterministic
- keep evidence records connected to claims, artifacts, reports, validation, and limitations
- keep paper and report language aligned with the claim boundary
- keep decision records current when strategy or technical direction changes
- add validators and contribution workflows only when they preserve public-safe evidence boundaries

## Recommended Next Task

Recommended next task after the evidence lineage layer and supervisor pilot:

- Review the P-CORE-051 long-run supervisor pilot PR if validation and scans remain clean.
- Then continue with the next scoped external evidence package, benchmark run, review packet, research package, dataset, evidence, or validation task.

## How To Continue

1. Start with this file.
2. Read [REVIEW_HUB.md](REVIEW_HUB.md).
3. Check current Git state with `git status --short --branch` and `git log -1 --oneline`.
4. Review [Claim Registry](docs/claims/claim-registry.md) and [Claim Boundary](docs/CLAIM_BOUNDARY.md) before changing public claims.
5. Run the current local validation commands before committing:

```bash
python3 scripts/permea_specs.py
python3 scripts/permea_demo.py
python3 scripts/permea_evidence.py
python3 scripts/permea_benchmarks.py
python3 scripts/permea_benchmark_run.py
python3 scripts/permea_datasets.py
python3 scripts/permea_research.py
python3 scripts/permea_signal.py
python3 scripts/permea_lineage.py
python3 scripts/permea_review.py
python3 scripts/permea_check.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest
git diff --check
```

6. At task completion, update the relevant memory surface for the kind of work completed. Strategic or technical decisions must create or update a [Decision Record](docs/decisions/README.md).
