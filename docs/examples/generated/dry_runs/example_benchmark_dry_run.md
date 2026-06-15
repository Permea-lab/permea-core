# Benchmark Dry-Run: example_benchmark_dry_run

## Overview

This deterministic dry-run is generated from metadata and local example artifacts. It demonstrates how Permea Core artifact layers fit together without dataset download, acquisition execution, API calls, ML runs, or performance measurement.

## Dry-Run Metadata

- Dry-run ID: `example_benchmark_dry_run`
- Dry-run type: `benchmark-dry-run-example`
- Generated at: `example-generated`
- Status: `PASS`

## Input Artifacts

- benchmark registry: [benchmarks/registry.yaml](benchmarks/registry.yaml)
- benchmark metadata: [benchmarks/bbb_b3pred_dataset3.yaml](benchmarks/bbb_b3pred_dataset3.yaml)
- dataset card metadata: [dataset_cards/b3pred_dataset3.yaml](dataset_cards/b3pred_dataset3.yaml)
- acquisition manifest metadata: [acquisition_manifests/b3pred_dataset3.yaml](acquisition_manifests/b3pred_dataset3.yaml)
- run manifest metadata: [run_manifests/example_artifact_generation.yaml](run_manifests/example_artifact_generation.yaml)

## Commands Executed

- PASS `python3 scripts/validate_benchmark_registry.py`
- PASS `python3 scripts/validate_dataset_cards.py`
- PASS `python3 scripts/validate_acquisition_manifests.py`
- PASS `python3 scripts/validate_run_manifests.py`
- PASS `python3 scripts/generate_benchmark_card.py`
- PASS `python3 scripts/generate_evidence_cards.py`
- PASS `python3 scripts/generate_output_package.py`
- PASS `python3 scripts/generate_run_manifests.py`
- PASS `python3 scripts/generate_artifact_index.py`

## Generated Artifacts

- benchmark card: [docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md](docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md)
- evidence cards: [docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json](docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json)
- output package manifest: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml](docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml)
- output package metrics metadata: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json](docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json)
- output package ranking metadata: [docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv](docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv)
- generated run manifest: [docs/examples/generated/run_manifests/example_artifact_generation.md](docs/examples/generated/run_manifests/example_artifact_generation.md)
- artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md)

## Related Evidence Surfaces

- generated evidence surface: [../README.md](../README.md)
- public demo packet: [../DEMO_PACKET.md](../DEMO_PACKET.md)
- public artifact index: [../ARTIFACT_INDEX.md](../ARTIFACT_INDEX.md)
- public evidence matrix: [../EVIDENCE_MATRIX.md](../EVIDENCE_MATRIX.md)

## Validation Steps

- PASS `python3 scripts/validate_benchmark_registry.py`
- PASS `python3 scripts/validate_dataset_cards.py`
- PASS `python3 scripts/validate_acquisition_manifests.py`
- PASS `python3 scripts/validate_run_manifests.py`
- PASS `python3 scripts/generate_artifact_index.py`

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no model performance claim

## Limitations

- This dry-run is generated from local metadata and example artifacts only.
- It does not load source datasets or inspect row-level biological data.
- It does not evaluate baselines, train models, score candidates, or measure performance.
- It does not confirm access, license, redistribution, or acquisition readiness.

## Next Action

Review generated dry-run artifacts and run unified validation.
