# Permea Core Public Reproducibility Report

## Run summary

- Run name: `permea_core_public_reproducibility_bundle`
- Generated at: `example-generated`
- Status: `PASS`

## Generated surfaces

- Generated evidence surface: [docs/examples/generated/README.md](docs/examples/generated/README.md) (present)
- Demo packet: [docs/examples/generated/DEMO_PACKET.md](docs/examples/generated/DEMO_PACKET.md) (present)
- Artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md) (present)
- Evidence matrix: [docs/examples/generated/EVIDENCE_MATRIX.md](docs/examples/generated/EVIDENCE_MATRIX.md) (present)
- Reproducibility report Markdown: [docs/examples/generated/REPRODUCIBILITY_REPORT.md](docs/examples/generated/REPRODUCIBILITY_REPORT.md) (present)
- Reproducibility report JSON: [docs/examples/generated/REPRODUCIBILITY_REPORT.json](docs/examples/generated/REPRODUCIBILITY_REPORT.json) (present)
- Dry-run report: [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](docs/examples/generated/dry_runs/example_benchmark_dry_run.md) (present)

## Validation summary

- unified artifact validation: `python3 scripts/validate_permea_artifacts.py`
- reproducibility bundle validation: `python3 scripts/permea_validate.py`
- focused reproducibility tests: `python3 -m pytest tests/test_reproducibility_bundle.py`

## Artifact lineage

1. README: [README.md](README.md) (present)
2. Quickstart: [QUICKSTART.md](QUICKSTART.md) (present)
3. Reproducibility guide: [REPRODUCIBILITY.md](REPRODUCIBILITY.md) (present)
4. Generated evidence surface: [docs/examples/generated/README.md](docs/examples/generated/README.md) (present)
5. Demo packet: [docs/examples/generated/DEMO_PACKET.md](docs/examples/generated/DEMO_PACKET.md) (present)
6. Artifact index: [docs/examples/generated/ARTIFACT_INDEX.md](docs/examples/generated/ARTIFACT_INDEX.md) (present)
7. Evidence matrix: [docs/examples/generated/EVIDENCE_MATRIX.md](docs/examples/generated/EVIDENCE_MATRIX.md) (present)
8. Reproducibility report: [docs/examples/generated/REPRODUCIBILITY_REPORT.md](docs/examples/generated/REPRODUCIBILITY_REPORT.md) (present)
9. Dry-run report: [docs/examples/generated/dry_runs/example_benchmark_dry_run.md](docs/examples/generated/dry_runs/example_benchmark_dry_run.md) (present)
10. Benchmark cards: [docs/examples/generated/benchmark_cards](docs/examples/generated/benchmark_cards) (present)
11. Dataset cards: [docs/examples/generated/dataset_cards](docs/examples/generated/dataset_cards) (present)
12. Acquisition manifests: [docs/examples/generated/acquisition_manifests](docs/examples/generated/acquisition_manifests) (present)
13. Evidence cards: [docs/examples/generated/evidence_cards](docs/examples/generated/evidence_cards) (present)
14. Output packages: [docs/examples/generated/output_packages](docs/examples/generated/output_packages) (present)
15. Run manifests: [docs/examples/generated/run_manifests](docs/examples/generated/run_manifests) (present)

## Reproducibility status

The bundle is reproducible when the listed artifacts are present and the reproduction and validation commands exit successfully.

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

- This bundle regenerates deterministic public metadata artifacts from repository files only.
- It does not download datasets, execute acquisition, call external services, run ML, or score candidates.
- It validates artifact presence, structure, links, and stated boundaries; it does not validate biological performance.
- Researchers and developers should treat generated examples as infrastructure surfaces, not experimental evidence.

## Next Evidence Steps

- Run the reproduction command after cloning or changing generator code.
- Run the validation command before proposing changes to generated artifact surfaces.
- Extend the artifact system by adding generator, validation, tests, and bounded claim language together.
