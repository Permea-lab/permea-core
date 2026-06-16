# Permea Core Quickstart

## Overview

Permea Core is a public infrastructure layer for deterministic artifact generation, validation, and review. This quickstart shows how to reproduce the current public artifact surfaces locally.

## Who this is for

- Researchers who want to inspect generated evidence artifacts before extending them.
- Developers who want to run the local artifact system and verify expected outputs.
- Reviewers who want one path from repository entry points to generated reports and non-claims.

## Install / local setup assumptions

- Python 3 is available as `python3`.
- The repository has been cloned locally.
- Commands are run from the repository root.
- No dataset download, external service call, acquisition execution, or ML run is required.

## One-command reproduction

```bash
python3 scripts/permea_reproduce.py
```

This regenerates the public artifact surfaces and writes the reproducibility report.

## One-command validation

```bash
python3 scripts/permea_validate.py
```

This runs unified artifact validation and reproducibility bundle checks.

## One-command artifact standard check

```bash
python3 scripts/permea_check.py
```

This checks built-in public dataset-card, benchmark-card, evidence-card, run-manifest, and output-package examples for required fields, repo-relative paths, non-claims, claim-boundary wording, and evidence linkage.

You can also validate a copyable example package:

```bash
python3 scripts/permea_check.py examples/synthetic_reference_example
```

## One-command evaluation packet generation

```bash
python3 scripts/permea_evaluate.py
```

This writes a public template/reference evaluation packet that links current input families, generated surfaces, validation handoff, reproducibility handoff, explicit non-claims, and next evidence steps.

## Where generated outputs appear

- [Generated evidence surface](docs/examples/generated/README.md)
- [Demo packet](docs/examples/generated/DEMO_PACKET.md)
- [Artifact index](docs/examples/generated/ARTIFACT_INDEX.md)
- [Evidence matrix](docs/examples/generated/EVIDENCE_MATRIX.md)
- [Evaluation packet](docs/examples/generated/EVALUATION_PACKET.md)
- [Reproducibility report](docs/examples/generated/REPRODUCIBILITY_REPORT.md)
- [Dry-run report](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)
- [External examples](examples/README.md)

## How to inspect the evidence surface

Start with [docs/examples/generated/README.md](docs/examples/generated/README.md), then follow the links to the evaluation packet, demo packet, artifact index, evidence matrix, reproducibility report, dry-run report, and generated artifact families.

## How to extend the artifact system

Start with the [public artifact specifications](docs/specs/README.md), then add generator logic, validation logic, generated examples, tests, and claim-boundary language together. New artifact families should be linked from the generated evidence surface and covered by validation before they become public reviewer-facing surfaces.

Inspect the specification registry with:

```bash
python3 scripts/permea_specs.py
```

Check current public examples against the artifact standards with:

```bash
python3 scripts/permea_check.py
```

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical-effectiveness claim
- no model performance claim
- no state-of-the-art claim
- no solved-delivery claim

## Troubleshooting

- If reproduction fails, run `python3 scripts/generate_permea_artifacts.py` to identify the failing generator step.
- If validation fails, run `python3 scripts/validate_permea_artifacts.py` to identify the failing validation step.
- If an artifact standard check fails, run `python3 scripts/permea_check.py path/to/artifact` to inspect a single public artifact path.
- If generated files look stale, rerun `python3 scripts/permea_reproduce.py` from the repository root.

## Next steps

Read [REPRODUCIBILITY.md](REPRODUCIBILITY.md) and [EVALUATION.md](EVALUATION.md), then inspect the generated [evaluation packet](docs/examples/generated/EVALUATION_PACKET.md) and [reproducibility report](docs/examples/generated/REPRODUCIBILITY_REPORT.md).
