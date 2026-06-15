# Permea Core Evaluation Bundle

## Overview

The public evaluation bundle is a template/reference workflow for connecting Permea Core input families to reviewer-facing generated artifacts. It shows how dataset-card, benchmark-card, and evidence-card style inputs can be linked to generated surfaces without asserting dataset access, acquisition execution, or measured performance.

## Who this is for

- Researchers who want to inspect the artifact pattern before adding new public inputs.
- Developers who want to extend generators, validation, and tests together.
- Reviewers who want to trace an evaluation packet back to bounded input families and generated surfaces.

## Evaluation contract

The contract is local, deterministic, and metadata-only. The bundle references public repository inputs, generates a packet, links existing artifact families, and hands off to validation and reproducibility commands.

## Reference input families

- `dataset_cards/`
- `benchmark_cards/`
- `evidence_cards/`
- `acquisition_manifests/`
- `run_manifests/`
- `output_packages/`

The public artifact standards are indexed at [docs/specs/README.md](docs/specs/README.md). The evaluation pattern should stay aligned with the dataset card, benchmark card, evidence card, run manifest, and output package specifications.

The validator handoff is documented at [docs/specs/VALIDATION.md](docs/specs/VALIDATION.md).

## One-command evaluation packet generation

```bash
python3 scripts/permea_evaluate.py
```

## Generated outputs

- `docs/examples/generated/EVALUATION_PACKET.md`
- `docs/examples/generated/EVALUATION_PACKET.json`

## How to inspect the evaluation packet

Start with [docs/examples/generated/EVALUATION_PACKET.md](docs/examples/generated/EVALUATION_PACKET.md), then follow its lineage links to the generated evidence surface, demo packet, artifact index, evidence matrix, reproducibility report, dry-run report, and artifact families.

## How to adapt the pattern for new dataset cards

Add or update dataset-card metadata, keep source and limitation fields explicit, add generator and validation coverage, and keep the generated packet linked to the relevant dataset-card family.

## How to adapt the pattern for new benchmark cards

Add benchmark task metadata with bounded labels, split policy, metrics, and limitations. Regenerate benchmark cards, update validation where needed, and keep benchmark claims tied to generated artifacts.

## How to adapt the pattern for new evidence cards

Add evidence-card records only when source, uncertainty, review status, and claim boundary are clear. Regenerate the evidence-card family and rerun validation before publishing changes.

## Validation and reproducibility commands

```bash
python3 scripts/permea_evaluate.py
python3 scripts/permea_check.py --all
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/generate_permea_artifacts.py
python3 scripts/validate_permea_artifacts.py
```

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- This bundle is a public template/reference workflow, not an experimental result.
- It links existing metadata and generated surfaces; it does not load source datasets.
- It does not execute acquisition, call external services, run ML, score candidates, or measure performance.
- It does not establish biological delivery, mechanism, safety, therapeutic effect, or generalization.

## Next Evidence Steps

- Use the evaluation packet as the reviewer-facing entry point for the template pattern.
- Add new input families only with matching generator, validation, tests, and non-claim coverage.
- Run reproduction and validation commands before proposing public evaluation changes.
