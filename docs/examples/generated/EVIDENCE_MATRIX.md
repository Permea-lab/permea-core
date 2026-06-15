# Permea Core Public Evidence Matrix

## Overview

This public evidence matrix maps current Permea Core artifact capabilities to generated artifacts, reproducible local commands, validation evidence, explicit non-claims, limitations, and next evidence steps.

- Matrix ID: `permea_core_public_evidence_matrix`
- Matrix type: `public-evidence-matrix`
- Generated at: `example-generated`
- Status: `PASS`

## Implemented Capabilities

| Capability | Current evidence boundary | Artifact evidence | Command | Next evidence step |
| --- | --- | --- | --- | --- |
| source registry validation | Validates public source registry structure and entries. | [sources/registry.yaml](sources/registry.yaml) | `python3 scripts/validate_source_registry.py` | Keep source records aligned with dataset and benchmark metadata. |
| dataset card generation | Generates public dataset-card examples from local metadata. | [docs/examples/generated/dataset_cards/b3pred_dataset3.md](docs/examples/generated/dataset_cards/b3pred_dataset3.md) | `python3 scripts/generate_dataset_cards.py` | Add richer review status and source limitations as cards mature. |
| acquisition manifest generation | Generates public acquisition-plan metadata without executing acquisition. | [docs/examples/generated/acquisition_manifests/b3pred_dataset3.md](docs/examples/generated/acquisition_manifests/b3pred_dataset3.md) | `python3 scripts/generate_acquisition_manifests.py` | Add acquisition readiness checks only after access and release policy are reviewed. |
| benchmark registry validation | Validates benchmark task registry metadata. | [benchmarks/registry.yaml](benchmarks/registry.yaml) | `python3 scripts/validate_benchmark_registry.py` | Keep task definitions tied to explicit labels, metrics, splits, and limitations. |
| benchmark card generation | Generates benchmark-card examples for reviewable task definitions. | [docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md](docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md) | `python3 scripts/generate_benchmark_card.py` | Expand cards as benchmark contracts stabilize. |
| evidence card generation | Generates structured public evidence-card examples. | [docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json](docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json) | `python3 scripts/generate_evidence_cards.py` | Add evidence review status and uncertainty fields as source coverage grows. |
| output package generation | Generates deterministic output-package examples for benchmark review. | [docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml](docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml) | `python3 scripts/generate_output_package.py` | Connect future benchmark outputs to the same package shape. |
| run manifest generation | Generates reproducibility records for local artifact generation. | [docs/examples/generated/run_manifests/example_artifact_generation.md](docs/examples/generated/run_manifests/example_artifact_generation.md) | `python3 scripts/generate_run_manifests.py` | Keep manifest fields aligned with generated artifacts and command coverage. |
| artifact index generation | Generates a public index of current registry inputs and generated artifacts. | [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md) | `python3 scripts/generate_artifact_index.py` | Add new artifact families only after generator and validation coverage exist. |
| demo packet generation | Generates a public entry point for inspecting current artifact-system outputs. | [docs/examples/generated/DEMO_PACKET.md](docs/examples/generated/DEMO_PACKET.md)<br>[docs/examples/generated/DEMO_PACKET.json](docs/examples/generated/DEMO_PACKET.json) | `python3 scripts/generate_demo_packet.py` | Keep the packet refreshed as new generated entry points are added. |
| benchmark dry-run orchestration | Runs local metadata checks and example generators for a deterministic dry-run report. | [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)<br>[docs/examples/generated/dry_runs/example_benchmark_dry_run.json](docs/examples/generated/dry_runs/example_benchmark_dry_run.json) | `python3 scripts/run_permea_dry_run.py` | Add broader dry-run coverage only after public-safe task contracts are stable. |
| unified generation | Runs current deterministic artifact generators through one local command. | [scripts/generate_permea_artifacts.py](scripts/generate_permea_artifacts.py) | `python3 scripts/generate_permea_artifacts.py` | Keep public evidence-surface generators included as new generated surfaces are added. |
| unified validation | Runs current local validation and generation checks through one command. | [scripts/validate_permea_artifacts.py](scripts/validate_permea_artifacts.py) | `python3 scripts/validate_permea_artifacts.py` | Keep public evidence-surface presence covered by local validation. |

## Artifact Evidence

- public demo packet: [docs/examples/generated/DEMO_PACKET.md](docs/examples/generated/DEMO_PACKET.md) (present)
- public demo packet JSON: [docs/examples/generated/DEMO_PACKET.json](docs/examples/generated/DEMO_PACKET.json) (present)
- public artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md) (present)
- public reproducibility report: [docs/examples/generated/REPRODUCIBILITY_REPORT.md](docs/examples/generated/REPRODUCIBILITY_REPORT.md) (present)
- benchmark dry-run report: [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](docs/examples/generated/dry_runs/example_benchmark_dry_run.md) (present)
- benchmark dry-run JSON: [docs/examples/generated/dry_runs/example_benchmark_dry_run.json](docs/examples/generated/dry_runs/example_benchmark_dry_run.json) (present)
- benchmark card example: [docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md](docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md) (present)
- dataset card example: [docs/examples/generated/dataset_cards/b3pred_dataset3.md](docs/examples/generated/dataset_cards/b3pred_dataset3.md) (present)
- acquisition manifest example: [docs/examples/generated/acquisition_manifests/b3pred_dataset3.md](docs/examples/generated/acquisition_manifests/b3pred_dataset3.md) (present)
- evidence card example: [docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json](docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json) (present)
- output package manifest: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml](docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml) (present)
- output package metrics metadata: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json](docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json) (present)
- output package ranking metadata: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv](docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv) (present)
- run manifest example: [docs/examples/generated/run_manifests/example_artifact_generation.md](docs/examples/generated/run_manifests/example_artifact_generation.md) (present)

## Related Evidence Surfaces

- generated evidence surface: [README.md](README.md)
- public demo packet: [DEMO_PACKET.md](DEMO_PACKET.md)
- public artifact index: [ARTIFACT_INDEX.md](ARTIFACT_INDEX.md)
- public reproducibility report: [REPRODUCIBILITY_REPORT.md](REPRODUCIBILITY_REPORT.md)
- benchmark dry-run report: [dry_runs/example_benchmark_dry_run.md](dry_runs/example_benchmark_dry_run.md)

## Command Evidence

- source registry validation: `python3 scripts/validate_source_registry.py`
- dataset card generation: `python3 scripts/generate_dataset_cards.py`
- acquisition manifest generation: `python3 scripts/generate_acquisition_manifests.py`
- benchmark registry validation: `python3 scripts/validate_benchmark_registry.py`
- benchmark card generation: `python3 scripts/generate_benchmark_card.py`
- evidence card generation: `python3 scripts/generate_evidence_cards.py`
- output package generation: `python3 scripts/generate_output_package.py`
- run manifest generation: `python3 scripts/generate_run_manifests.py`
- artifact index generation: `python3 scripts/generate_artifact_index.py`
- demo packet generation: `python3 scripts/generate_demo_packet.py`
- benchmark dry-run orchestration: `python3 scripts/run_permea_dry_run.py`
- unified generation: `python3 scripts/generate_permea_artifacts.py`
- unified validation: `python3 scripts/validate_permea_artifacts.py`

## Validation Evidence

- artifact validation: `python3 scripts/validate_permea_artifacts.py`
- unified generation: `python3 scripts/generate_permea_artifacts.py`
- demo packet generation: `python3 scripts/generate_demo_packet.py`
- benchmark dry-run: `python3 scripts/run_permea_dry_run.py`

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical-effectiveness claim
- no model performance claim
- no state-of-the-art claim
- no solved-delivery claim

## Limitations

- This matrix is generated from repository metadata, generated examples, and local commands only.
- It maps implemented artifact infrastructure, not biological or therapeutic performance.
- It does not load datasets, run acquisition, call external services, run ML, or score candidates.
- It records evidence boundaries for current public artifacts and does not expand scientific claims.

## Next Evidence Steps

- Keep this matrix connected to the generated evidence surface, demo packet, artifact index, and dry-run report.
- Keep unified generation and validation coverage aligned with new generated evidence surfaces.
- Keep new public claims tied to generated artifacts, commands, limitations, and non-claims.
