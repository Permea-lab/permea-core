# Open This First

This file is the first continuation breadcrumb for Permea Core. It summarizes the current public state so a reviewer, contributor, or new session can continue without reading historical chat logs.

## Current Status

Permea Core is a public, benchmark-first infrastructure repository for sequence-first biological delivery engineering. The current repository state emphasizes reproducible artifact generation, public evidence indexing, evaluation and reproducibility bundles, artifact specifications, artifact validation, decision records, project memory, and bounded claim language.

Current public baseline when this breadcrumb was refreshed:

- Branch used for this update: `p-core-038-artifact-validator-bundle`
- Public baseline reviewed: `main` at `2749f987b5cc7ceca60b2c9545e091a3f1d71286`
- Refresh command: `git status --short --branch && git log -1 --oneline`

## Current Public Truth

Permea Core currently provides:

- public artifact specifications for dataset cards, benchmark cards, evidence cards, run manifests, and output packages
- a lightweight public artifact validator command for current public example artifacts
- deterministic generated example artifact surfaces under `docs/examples/generated/`
- local commands for reproduction, validation, evaluation packet generation, dry-run generation, and specification registry inspection
- public evidence records under `docs/evidence/`
- public claim registry at `docs/claims/claim-registry.md`
- decision records for major program choices under `docs/decisions/`
- public claim-boundary and paper-alignment policies
- lightweight schemas under `schemas/`

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

See [Evidence Layer](docs/evidence/README.md), [Evidence Index](docs/evidence/evidence-index.md), and [Decision Records](docs/decisions/README.md) for the current review surfaces.

## Last Completed Major Work

The last completed major public documentation layer is the evidence layer:

- [P-DOC-007 evidence layer bootstrap report](docs/reports/p-doc-007-evidence-layer-bootstrap-v0.md)
- [Evidence layer](docs/evidence/README.md)

## Current Branch / Commit

Use live Git state as the source of truth:

```bash
git status --short --branch
git log -1 --oneline
```

At this update, the reviewed public baseline was `2749f987b5cc7ceca60b2c9545e091a3f1d71286`.

## Primary Reports

- [P-CORE-036 artifact specification layer report](docs/reports/p-core-036-artifact-specification-layer.md)
- [P-DOC-001 project operating-system adoption report](docs/reports/p-doc-001-project-operating-system-adoption-v0.md)
- [P-DOC-004 decision and documentation backfill report](docs/reports/p-doc-004-decision-and-documentation-backfill-v0.md)
- [P-DOC-007 evidence layer bootstrap report](docs/reports/p-doc-007-evidence-layer-bootstrap-v0.md)
- [P-CORE-038 artifact validator bundle report](docs/reports/p-core-038-artifact-validator-bundle-v0.md)
- [Generated reproducibility report](docs/examples/generated/REPRODUCIBILITY_REPORT.md)
- [Generated evaluation packet](docs/examples/generated/EVALUATION_PACKET.md)
- [Generated evidence matrix](docs/examples/generated/EVIDENCE_MATRIX.md)
- [Generated demo packet](docs/examples/generated/DEMO_PACKET.md)

## Primary Evidence

- [Generated evidence surface](docs/examples/generated/README.md)
- [Evidence layer](docs/evidence/README.md)
- [Evidence index](docs/evidence/evidence-index.md)
- [Claim registry](docs/claims/claim-registry.md)
- [Artifact validator evidence](docs/evidence/EVIDENCE-038-artifact-validator-bundle.md)
- [Artifact index](docs/examples/generated/ARTIFACT_INDEX.md)
- [Benchmark dry-run report](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)
- [Source registry](sources/registry.yaml)
- [Benchmark registry](benchmarks/registry.yaml)
- [Artifact schemas](schemas/)
- [Public artifact specifications](docs/specs/README.md)
- [Decision records](docs/decisions/README.md)

## Current Research Direction

Current work should continue strengthening Permea Core as public infrastructure:

- keep artifact standards inspectable and easy to extend
- keep artifact validation aligned with public specifications and evidence-linkage expectations
- keep generation and validation deterministic
- keep evidence records connected to claims, artifacts, reports, validation, and limitations
- keep paper and report language aligned with the claim boundary
- keep decision records current when strategy or technical direction changes
- add validators and contribution workflows only when they preserve public-safe evidence boundaries

## Recommended Next Task

Recommended next task after this artifact validator bundle:

- Review and merge the artifact validator bundle branch if clean.
- Then continue with the next scoped validation or documentation task, prioritizing validator coverage only when public artifact families require it.

## How To Continue

1. Start with this file.
2. Read [REVIEW_HUB.md](REVIEW_HUB.md).
3. Check current Git state with `git status --short --branch` and `git log -1 --oneline`.
4. Review [Claim Registry](docs/claims/claim-registry.md) and [Claim Boundary](docs/CLAIM_BOUNDARY.md) before changing public claims.
5. Run the current local validation commands before committing:

```bash
python3 scripts/permea_specs.py
python3 scripts/permea_check.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
git diff --check
```

6. At task completion, update the relevant memory surface for the kind of work completed. Strategic or technical decisions must create or update a [Decision Record](docs/decisions/README.md).
