# Permea Core Public Demo Packet

## Overview

This public demo packet is a generated entry point for the current Permea Core artifact system. It points reviewers to local commands, input metadata, generated examples, dry-run outputs, validation, and explicit non-claims.

- Packet ID: `permea_core_public_demo_packet`
- Packet type: `public-demo-packet`
- Generated at: `example-generated`
- Status: `PASS`

## One-command demo

`python3 scripts/generate_demo_packet.py`

Start from the generated evidence surface:

- [docs/examples/generated/README.md](README.md)

This command writes:

- `docs/examples/generated/DEMO_PACKET.md`
- `docs/examples/generated/DEMO_PACKET.json`

## Regenerate artifacts

`python3 scripts/generate_permea_artifacts.py`

Regenerates the current deterministic public example artifacts.

## Validate artifacts

`python3 scripts/validate_permea_artifacts.py`

Validates current registry inputs and generated artifact examples with local deterministic checks.

## Artifact families

- Artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md) (present)
- Benchmark dry-run reports: [docs/examples/generated/dry_runs/README.md](docs/examples/generated/dry_runs/README.md) (present)
- Benchmark cards: [docs/examples/generated/benchmark_cards](docs/examples/generated/benchmark_cards) (present)
- Dataset cards: [docs/examples/generated/dataset_cards](docs/examples/generated/dataset_cards) (present)
- Acquisition manifests: [docs/examples/generated/acquisition_manifests](docs/examples/generated/acquisition_manifests) (present)
- Evidence cards: [docs/examples/generated/evidence_cards](docs/examples/generated/evidence_cards) (present)
- Output packages: [docs/examples/generated/output_packages](docs/examples/generated/output_packages) (present)
- Run manifests: [docs/examples/generated/run_manifests](docs/examples/generated/run_manifests) (present)

## Input Artifacts

- source registry: [sources/registry.yaml](sources/registry.yaml) (present)
- benchmark registry: [benchmarks/registry.yaml](benchmarks/registry.yaml) (present)
- benchmark task metadata: [benchmarks/bbb_b3pred_dataset3.yaml](benchmarks/bbb_b3pred_dataset3.yaml) (present)
- dataset card metadata: [dataset_cards/b3pred_dataset3.yaml](dataset_cards/b3pred_dataset3.yaml) (present)
- acquisition manifest metadata: [acquisition_manifests/b3pred_dataset3.yaml](acquisition_manifests/b3pred_dataset3.yaml) (present)
- run manifest metadata: [run_manifests/example_artifact_generation.yaml](run_manifests/example_artifact_generation.yaml) (present)

## Generated Artifacts

- artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md) (present)
- evaluation packet: [docs/examples/generated/EVALUATION_PACKET.md](docs/examples/generated/EVALUATION_PACKET.md) (present)
- reproducibility report: [docs/examples/generated/REPRODUCIBILITY_REPORT.md](docs/examples/generated/REPRODUCIBILITY_REPORT.md) (present)
- benchmark dry-run Markdown: [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](docs/examples/generated/dry_runs/example_benchmark_dry_run.md) (present)
- benchmark dry-run JSON: [docs/examples/generated/dry_runs/example_benchmark_dry_run.json](docs/examples/generated/dry_runs/example_benchmark_dry_run.json) (present)
- benchmark card: [docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md](docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md) (present)
- dataset card: [docs/examples/generated/dataset_cards/b3pred_dataset3.md](docs/examples/generated/dataset_cards/b3pred_dataset3.md) (present)
- acquisition manifest: [docs/examples/generated/acquisition_manifests/b3pred_dataset3.md](docs/examples/generated/acquisition_manifests/b3pred_dataset3.md) (present)
- evidence cards: [docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json](docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json) (present)
- output package manifest: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml](docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml) (present)
- output package metrics metadata: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json](docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json) (present)
- output package ranking metadata: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv](docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv) (present)
- run manifest: [docs/examples/generated/run_manifests/example_artifact_generation.md](docs/examples/generated/run_manifests/example_artifact_generation.md) (present)

## Dry-run output

`python3 scripts/run_permea_dry_run.py`

Runs local metadata checks and example artifact generators, then writes deterministic dry-run Markdown and JSON reports.

- [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)
- [docs/examples/generated/dry_runs/example_benchmark_dry_run.json](docs/examples/generated/dry_runs/example_benchmark_dry_run.json)

## Public artifact index

- [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md)

## Related evidence surfaces

- [Generated evidence surface](README.md)
- [Public artifact index](docs/examples/generated/ARTIFACT_INDEX.md)
- [Public evaluation packet](EVALUATION_PACKET.md)
- [Public evidence matrix](EVIDENCE_MATRIX.md)
- [Public reproducibility report](REPRODUCIBILITY_REPORT.md)
- [Benchmark dry-run report](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)

## Available Commands

- one-command demo packet: `python3 scripts/generate_demo_packet.py`
- benchmark dry-run: `python3 scripts/run_permea_dry_run.py`
- unified artifact generation: `python3 scripts/generate_permea_artifacts.py`
- unified artifact validation: `python3 scripts/validate_permea_artifacts.py`

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no model performance claim

## Limitations

- This packet is generated from repository metadata and generated examples only.
- It is a public artifact-system demonstration, not a data acquisition run.
- It does not load source datasets, inspect row-level biological data, run ML, or score candidates.
- It does not confirm access, license, redistribution, acquisition readiness, or biological performance.

## Next Steps

Review this packet, then run the dry-run, unified generation, and unified validation commands before opening or reviewing a public PR.
