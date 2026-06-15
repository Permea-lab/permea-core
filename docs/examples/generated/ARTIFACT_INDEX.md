# Permea Core Public Artifact Index

## Overview

This generated index lists the current public registry inputs, generated example artifacts, and local generation and validation commands available in Permea Core.

## Unified Commands

- `python3 scripts/generate_evidence_surface.py`
- `python3 scripts/permea_evaluate.py`
- `python3 scripts/permea_reproduce.py`
- `python3 scripts/permea_validate.py`
- `python3 scripts/generate_demo_packet.py`
- `python3 scripts/generate_artifact_index.py`
- `python3 scripts/generate_evidence_matrix.py`
- `python3 scripts/run_permea_dry_run.py`
- `python3 scripts/generate_permea_artifacts.py`
- `python3 scripts/validate_permea_artifacts.py`

## Core Generated Surfaces

- Generated evidence surface: [docs/examples/generated/README.md](docs/examples/generated/README.md)
- Public demo packet: [docs/examples/generated/DEMO_PACKET.md](docs/examples/generated/DEMO_PACKET.md)
- Public artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md)
- Public evidence matrix: [docs/examples/generated/EVIDENCE_MATRIX.md](docs/examples/generated/EVIDENCE_MATRIX.md)
- Public evaluation packet: [docs/examples/generated/EVALUATION_PACKET.md](docs/examples/generated/EVALUATION_PACKET.md)
- Public reproducibility report: [docs/examples/generated/REPRODUCIBILITY_REPORT.md](docs/examples/generated/REPRODUCIBILITY_REPORT.md)
- Benchmark dry-run report: [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)

## Registry Inputs

- Source registry: [sources/registry.yaml](sources/registry.yaml)
- Benchmark registry: [benchmarks/registry.yaml](benchmarks/registry.yaml)
- Dataset card inputs: [dataset_cards](dataset_cards)
- Acquisition manifest inputs: [acquisition_manifests](acquisition_manifests)
- Run manifest inputs: [run_manifests](run_manifests)

## Generated Benchmark Cards

- [docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md](docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md)
- [docs/examples/generated/benchmark_cards/cpp_cppsite2_placeholder.md](docs/examples/generated/benchmark_cards/cpp_cppsite2_placeholder.md)

## Generated Dataset Cards

- [docs/examples/generated/dataset_cards/README.md](docs/examples/generated/dataset_cards/README.md)
- [docs/examples/generated/dataset_cards/b3pred_dataset3.md](docs/examples/generated/dataset_cards/b3pred_dataset3.md)
- [docs/examples/generated/dataset_cards/cppsite2_placeholder.md](docs/examples/generated/dataset_cards/cppsite2_placeholder.md)

## Generated Acquisition Manifests

- [docs/examples/generated/acquisition_manifests/README.md](docs/examples/generated/acquisition_manifests/README.md)
- [docs/examples/generated/acquisition_manifests/b3pred_dataset3.md](docs/examples/generated/acquisition_manifests/b3pred_dataset3.md)
- [docs/examples/generated/acquisition_manifests/cppsite2_placeholder.md](docs/examples/generated/acquisition_manifests/cppsite2_placeholder.md)

## Generated Evidence Cards

- [docs/examples/generated/evidence_cards/README.md](docs/examples/generated/evidence_cards/README.md)
- [docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json](docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json)
- [docs/examples/generated/evidence_cards/cpp_cppsite2_placeholder.evidence_cards.json](docs/examples/generated/evidence_cards/cpp_cppsite2_placeholder.evidence_cards.json)

## Generated Output Packages

- [docs/examples/generated/output_packages/README.md](docs/examples/generated/output_packages/README.md)
- [docs/examples/generated/output_packages/bbb_b3pred_dataset3/benchmark_card.md](docs/examples/generated/output_packages/bbb_b3pred_dataset3/benchmark_card.md)
- [docs/examples/generated/output_packages/bbb_b3pred_dataset3/evidence_cards.json](docs/examples/generated/output_packages/bbb_b3pred_dataset3/evidence_cards.json)
- [docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml](docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml)
- [docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json](docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json)
- [docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv](docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv)

## Generated Run Manifests

- [docs/examples/generated/run_manifests/README.md](docs/examples/generated/run_manifests/README.md)
- [docs/examples/generated/run_manifests/example_artifact_generation.md](docs/examples/generated/run_manifests/example_artifact_generation.md)

## Validation Boundary

The listed artifacts are deterministic local examples and metadata records. Validation checks repository schemas, required fields, path references, and generated-file presence.

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no model performance claim

## Next Steps

- Keep generated artifacts refreshed through the unified generator.
- Keep validation command coverage aligned with new artifact families.
- Add new public artifact families only after their schema and boundary checks exist.
