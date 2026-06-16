# Open This First

This file is the first continuation breadcrumb for Permea Core. It summarizes the current public state so a reviewer, contributor, or new assistant session can continue without reading historical chat logs.

## Current Status

Permea Core is a public, benchmark-first infrastructure repository for sequence-first biological delivery engineering. The current repository state emphasizes reproducible artifact generation, public evidence navigation, evaluation and reproducibility bundles, artifact specifications, and bounded claim language.

Current public baseline when this breadcrumb was created:

- Branch used for this adoption: `p-doc-001-project-operating-system-adoption`
- Public baseline reviewed: `main` at `f799e29 Add artifact specification layer (#47)`
- Refresh command: `git status --short --branch && git log -1 --oneline`

## Current Public Truth

Permea Core currently provides:

- public artifact specifications for dataset cards, benchmark cards, evidence cards, run manifests, and output packages
- deterministic generated example artifact surfaces under `docs/examples/generated/`
- local commands for reproduction, validation, evaluation packet generation, dry-run generation, and specification registry inspection
- public claim-boundary and paper-alignment policies
- lightweight schemas under `schemas/`

Permea Core does not currently claim dataset download, acquisition execution, redistribution-rights confirmation, wet-lab validation by Permea, clinical effectiveness, model performance, state-of-the-art status, or solved delivery.

## Last Completed Major Work

The last completed major public infrastructure layer is the artifact specification layer:

- [Artifact specification report](docs/reports/p-core-036-artifact-specification-layer.md)
- [Public artifact specifications](docs/specs/README.md)
- [Specification registry command](scripts/permea_specs.py)

## Current Branch / Commit

Use live Git state as the source of truth:

```bash
git status --short --branch
git log -1 --oneline
```

At adoption time, the reviewed public baseline was `f799e29 Add artifact specification layer (#47)`.

## Primary Reports

- [P-CORE-036 artifact specification layer report](docs/reports/p-core-036-artifact-specification-layer.md)
- [Generated reproducibility report](docs/examples/generated/REPRODUCIBILITY_REPORT.md)
- [Generated evaluation packet](docs/examples/generated/EVALUATION_PACKET.md)
- [Generated evidence matrix](docs/examples/generated/EVIDENCE_MATRIX.md)
- [Generated demo packet](docs/examples/generated/DEMO_PACKET.md)

## Primary Evidence

- [Generated evidence surface](docs/examples/generated/README.md)
- [Artifact index](docs/examples/generated/ARTIFACT_INDEX.md)
- [Benchmark dry-run report](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)
- [Source registry](sources/registry.yaml)
- [Benchmark registry](benchmarks/registry.yaml)
- [Artifact schemas](schemas/)
- [Public artifact specifications](docs/specs/README.md)

## Current Research Direction

Current work should continue strengthening Permea Core as public infrastructure:

- keep artifact standards inspectable and easy to extend
- keep generation and validation deterministic
- keep evidence surfaces navigable from repository entry points
- keep paper and report language aligned with the claim boundary
- add validators and contribution workflows only when they preserve public-safe evidence boundaries

## Recommended Next Task

Recommended next task after this adoption:

- Review and merge the project operating-system adoption branch if clean.
- Then continue with the next scoped infrastructure task, prioritizing validation coverage for artifact specifications.

## How To Continue

1. Start with this file.
2. Read [REVIEW_HUB.md](REVIEW_HUB.md).
3. Check current Git state with `git status --short --branch` and `git log -1 --oneline`.
4. Review [Claim Boundary](docs/CLAIM_BOUNDARY.md) before changing public claims.
5. Run the current local validation commands before committing:

```bash
python3 scripts/permea_specs.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
git diff --check
```

6. At task completion, update this file and [REVIEW_HUB.md](REVIEW_HUB.md), unless the task explicitly exempts breadcrumb updates.
