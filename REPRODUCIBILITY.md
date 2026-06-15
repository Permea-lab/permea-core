# Permea Core Reproducibility

## Purpose

This guide defines the public reproducibility contract for Permea Core artifact surfaces. It explains how to regenerate artifacts, validate them, inspect their lineage, and keep claims bounded.

## Reproducibility contract

The current public contract is local and deterministic: repository metadata is used to generate public example artifacts, index them, validate expected files and sections, and record explicit non-claims. The contract does not include dataset acquisition, row-level data loading, external service access, model execution, or performance measurement.

## Command map

- Reproduce public surfaces: `python3 scripts/permea_reproduce.py`
- Validate public surfaces: `python3 scripts/permea_validate.py`
- Inspect artifact specs: `python3 scripts/permea_specs.py`
- Generate all artifacts: `python3 scripts/generate_permea_artifacts.py`
- Validate all artifacts: `python3 scripts/validate_permea_artifacts.py`
- Generate evaluation packet: `python3 scripts/permea_evaluate.py`
- Run dry-run report generation: `python3 scripts/run_permea_dry_run.py`

## Generated artifact lineage

1. [README.md](README.md)
2. [QUICKSTART.md](QUICKSTART.md)
3. [REPRODUCIBILITY.md](REPRODUCIBILITY.md)
4. [EVALUATION.md](EVALUATION.md)
5. [Public artifact specifications](docs/specs/README.md)
6. [Generated evidence surface](docs/examples/generated/README.md)
7. [Evaluation packet](docs/examples/generated/EVALUATION_PACKET.md)
8. [Demo packet](docs/examples/generated/DEMO_PACKET.md)
9. [Artifact index](docs/examples/generated/ARTIFACT_INDEX.md)
10. [Evidence matrix](docs/examples/generated/EVIDENCE_MATRIX.md)
11. [Reproducibility report](docs/examples/generated/REPRODUCIBILITY_REPORT.md)
12. [Dry-run report](docs/examples/generated/dry_runs/example_benchmark_dry_run.md)
13. Generated artifact families under `docs/examples/generated/`

## Validation map

- Registry checks validate public metadata inputs.
- Generator checks regenerate public example artifacts.
- Reproducibility checks verify report sections, lineage paths, and explicit non-claims.
- Tests verify required sections, relative paths, command behavior, and unsupported claim hygiene.

## Expected outputs

- `docs/examples/generated/README.md`
- `docs/examples/generated/DEMO_PACKET.md`
- `docs/examples/generated/ARTIFACT_INDEX.md`
- `docs/examples/generated/EVIDENCE_MATRIX.md`
- `docs/examples/generated/EVALUATION_PACKET.md`
- `docs/examples/generated/EVALUATION_PACKET.json`
- `docs/examples/generated/REPRODUCIBILITY_REPORT.md`
- `docs/examples/generated/REPRODUCIBILITY_REPORT.json`
- `docs/examples/generated/dry_runs/example_benchmark_dry_run.md`

## Expected non-claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical-effectiveness claim
- no model performance claim
- no state-of-the-art claim
- no solved-delivery claim

## Known limitations

- Generated artifacts are examples from repository metadata.
- Validation checks local artifact structure and presence, not biological behavior.
- The bundle does not establish access rights, acquisition readiness, transport, mechanism, safety, therapeutic effect, or generalization.

## Extension points for researchers/developers

- Add dataset-card inputs with bounded source and claim metadata.
- Add benchmark-task metadata with explicit labels, splits, metrics, and limitations.
- Add artifact generators with matching validation and tests.
- Add evidence cards only when uncertainty, source, and review status are clear.

## What this bundle does not prove

This bundle does not prove biological delivery, clinical utility, broad prediction, model quality, redistribution rights, or data acquisition readiness. It proves that the public artifact infrastructure can be regenerated, validated, inspected, and extended locally.
