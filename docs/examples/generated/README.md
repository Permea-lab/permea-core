# Permea Core Generated Public Evidence Surface

## Overview

This generated README is the reviewer-facing navigation surface for Permea Core public artifacts. It links the demo packet, artifact index, evidence matrix, benchmark dry-run report, generated artifact families, evidence layer, reproducibility commands, validation commands, explicit non-claims, limitations, and next evidence steps.

- Surface ID: `permea_core_public_evidence_surface`
- Surface type: `public-evidence-surface`
- Generated at: `example-generated`
- Status: `PASS`

## One-command demo

`python3 scripts/generate_demo_packet.py`

- [Public demo packet](DEMO_PACKET.md)
- [Public evaluation packet](EVALUATION_PACKET.md)
- [Benchmark dry-run report](dry_runs/example_benchmark_dry_run.md)
- [Reproducibility report](REPRODUCIBILITY_REPORT.md)

## Core generated surfaces

- Generated evidence surface: [README.md](README.md) - Reviewer-facing navigation for generated public artifacts. (present)
- Public demo packet: [DEMO_PACKET.md](DEMO_PACKET.md) - One generated entry point for inspecting the artifact system. (present)
- Public artifact index: [ARTIFACT_INDEX.md](ARTIFACT_INDEX.md) - Generated inventory of registry inputs and artifact families. (present)
- Public evidence matrix: [EVIDENCE_MATRIX.md](EVIDENCE_MATRIX.md) - Generated mapping from implemented capabilities to evidence and commands. (present)
- Benchmark dry-run report: [dry_runs/example_benchmark_dry_run.md](dry_runs/example_benchmark_dry_run.md) - Generated dry-run output for local metadata and example artifacts. (present)
- Reproducibility report: [REPRODUCIBILITY_REPORT.md](REPRODUCIBILITY_REPORT.md) - Generated report for reproduction commands, validation checks, lineage, and non-claims. (present)
- Evaluation packet: [EVALUATION_PACKET.md](EVALUATION_PACKET.md) - Generated template/reference evaluation packet for artifact-system extension. (present)
- Public artifact specifications: [../../../docs/specs/README.md](../../../docs/specs/README.md) - Public standards for artifact families and their schemas. (present)
- Public evidence layer: [../../../docs/evidence/README.md](../../../docs/evidence/README.md) - Public index mapping claims, artifacts, reports, validation, and limitations. (present)
- Artifact validator command: [../../../scripts/permea_check.py](../../../scripts/permea_check.py) - Local checker for public artifact structure, non-claims, claim boundaries, and evidence linkage. (present)
- External examples: [../../../examples/README.md](../../../examples/README.md) - Copyable public-safe reference packages for using the artifact standard. (present)

## Artifact families

- Benchmark cards: [benchmark_cards/](benchmark_cards/) - Generated benchmark task examples. (present)
- Dataset cards: [dataset_cards/](dataset_cards/) - Generated dataset metadata examples. (present)
- Acquisition manifests: [acquisition_manifests/](acquisition_manifests/) - Generated acquisition-plan metadata examples without executing acquisition. (present)
- Evidence cards: [evidence_cards/](evidence_cards/) - Generated structured evidence-card examples. (present)
- Output packages: [output_packages/](output_packages/) - Generated benchmark output package examples. (present)
- Run manifests: [run_manifests/](run_manifests/) - Generated reproducibility record examples. (present)

## Reproducibility commands

- reproduce public bundle: `python3 scripts/permea_reproduce.py`
- validate public bundle: `python3 scripts/permea_validate.py`
- check artifact standards: `python3 scripts/permea_check.py`
- check synthetic example: `python3 scripts/permea_check.py examples/synthetic_reference_example`
- inspect artifact specs: `python3 scripts/permea_specs.py`
- generate evaluation packet: `python3 scripts/permea_evaluate.py`
- generate evidence surface: `python3 scripts/generate_evidence_surface.py`
- generate demo packet: `python3 scripts/generate_demo_packet.py`
- generate artifact index: `python3 scripts/generate_artifact_index.py`
- generate evidence matrix: `python3 scripts/generate_evidence_matrix.py`
- run benchmark dry-run: `python3 scripts/run_permea_dry_run.py`
- generate all artifacts: `python3 scripts/generate_permea_artifacts.py`

## Validation commands

- validate public bundle: `python3 scripts/permea_validate.py`
- check artifact standards: `python3 scripts/permea_check.py`
- validate all artifacts: `python3 scripts/validate_permea_artifacts.py`
- validate source registry: `python3 scripts/validate_source_registry.py`
- validate benchmark registry: `python3 scripts/validate_benchmark_registry.py`
- validate dataset cards: `python3 scripts/validate_dataset_cards.py`
- validate acquisition manifests: `python3 scripts/validate_acquisition_manifests.py`
- validate run manifests: `python3 scripts/validate_run_manifests.py`

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

- This surface is generated from public repository metadata and generated examples only.
- It is a navigation surface for deterministic local artifacts, not an acquisition run.
- It does not load source datasets, scrape websites, call external services, run ML, or score candidates.
- It does not confirm access, license, redistribution, biological performance, or clinical utility.

## Next Evidence Steps

- Keep generated entry points refreshed through unified generation.
- Keep validation coverage aligned with every generated public evidence surface.
- Attach future public claims to generated artifacts, commands, limitations, and explicit non-claims.
