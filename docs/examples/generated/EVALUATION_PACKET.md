# Permea Core Public Evaluation Packet

## Overview

This public evaluation bundle is a template/reference workflow for plugging dataset-card, benchmark-card, and evidence-card style inputs into the Permea Core artifact system and generating a reviewer-facing evaluation packet.

## Evaluation bundle summary

- Bundle name: `permea_core_public_evaluation_bundle`
- Generated at: `example-generated`
- Status: `PASS`
- Evaluation guide: [../../EVALUATION.md](../../EVALUATION.md)

## Reference input families

- dataset cards: [dataset_cards/](dataset_cards/) - Dataset metadata templates and example inputs. (present)
- benchmark cards: [benchmark_cards/](benchmark_cards/) - Benchmark-card pattern inputs for task definitions. (present)
- evidence cards: [evidence_cards/](evidence_cards/) - Evidence-card pattern inputs for structured evidence records. (present)
- acquisition manifests: [acquisition_manifests/](acquisition_manifests/) - Acquisition-plan metadata examples without execution. (present)
- run manifests: [run_manifests/](run_manifests/) - Reproducibility record inputs. (present)
- output packages: [output_packages/](output_packages/) - Output-package pattern inputs for reviewer-facing results. (present)

## Generated surfaces

- evaluation packet: [docs/examples/generated/EVALUATION_PACKET.md](EVALUATION_PACKET.md) (present)
- evaluation packet JSON: [docs/examples/generated/EVALUATION_PACKET.json](EVALUATION_PACKET.json) (present)
- generated evidence surface: [docs/examples/generated/README.md](README.md) (present)
- demo packet: [docs/examples/generated/DEMO_PACKET.md](DEMO_PACKET.md) (present)
- artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](ARTIFACT_INDEX.md) (present)
- evidence matrix: [docs/examples/generated/EVIDENCE_MATRIX.md](EVIDENCE_MATRIX.md) (present)
- reproducibility report: [docs/examples/generated/REPRODUCIBILITY_REPORT.md](REPRODUCIBILITY_REPORT.md) (present)
- benchmark dry-run report: [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](dry_runs/example_benchmark_dry_run.md) (present)

## Artifact lineage

1. README: [README.md](../../README.md) (present)
2. Quickstart: [QUICKSTART.md](../../QUICKSTART.md) (present)
3. Reproducibility guide: [REPRODUCIBILITY.md](../../REPRODUCIBILITY.md) (present)
4. Evaluation guide: [EVALUATION.md](../../EVALUATION.md) (present)
5. Generated evidence surface: [docs/examples/generated/README.md](README.md) (present)
6. Evaluation packet: [docs/examples/generated/EVALUATION_PACKET.md](EVALUATION_PACKET.md) (present)
7. Demo packet: [docs/examples/generated/DEMO_PACKET.md](DEMO_PACKET.md) (present)
8. Artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](ARTIFACT_INDEX.md) (present)
9. Evidence matrix: [docs/examples/generated/EVIDENCE_MATRIX.md](EVIDENCE_MATRIX.md) (present)
10. Reproducibility report: [docs/examples/generated/REPRODUCIBILITY_REPORT.md](REPRODUCIBILITY_REPORT.md) (present)
11. Dry-run report: [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](dry_runs/example_benchmark_dry_run.md) (present)
12. Benchmark cards: [docs/examples/generated/benchmark_cards](benchmark_cards) (present)
13. Dataset cards: [docs/examples/generated/dataset_cards](dataset_cards) (present)
14. Acquisition manifests: [docs/examples/generated/acquisition_manifests](acquisition_manifests) (present)
15. Evidence cards: [docs/examples/generated/evidence_cards](evidence_cards) (present)
16. Output packages: [docs/examples/generated/output_packages](output_packages) (present)
17. Run manifests: [docs/examples/generated/run_manifests](run_manifests) (present)

## Validation handoff

- evaluation packet generation: `python3 scripts/permea_evaluate.py`
- public reproducibility validation: `python3 scripts/permea_validate.py`
- unified artifact validation: `python3 scripts/validate_permea_artifacts.py`

## Reproducibility handoff

- public reproduction: `python3 scripts/permea_reproduce.py`
- unified artifact generation: `python3 scripts/generate_permea_artifacts.py`

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

- This evaluation bundle is a reusable template and reference workflow.
- It references current public example inputs and generated artifact families only.
- It does not load datasets, execute acquisition, call external services, run ML, or score candidates.
- It does not establish access rights, redistribution status, biological performance, or clinical utility.

## Next Evidence Steps

- Use the packet to inspect how dataset-card, benchmark-card, and evidence-card inputs connect to generated surfaces.
- Adapt the pattern by adding bounded input metadata, generator coverage, validation coverage, and tests together.
- Run reproduction and validation commands before proposing a public evaluation package change.
