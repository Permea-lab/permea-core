# P-CORE-049 Signal Integration Layer v0

## Purpose

P-CORE-049 adds the first public signal integration layer for Permea Core. The layer documents how Core links to the adjacent public `permea-signal-ml` evidence package while preserving repository boundaries and claim discipline.

## Files Added Or Changed

- `docs/integrations/README.md`
- `docs/integrations/permea-signal-ml.md`
- `docs/integrations/external-evidence-package-template.md`
- `docs/integrations/external-evidence-package-governance.md`
- `schemas/external-evidence-package.schema.json`
- `scripts/permea_signal.py`
- `tests/test_signal_integration_layer.py`
- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/reports/p-core-049-signal-integration-layer-v0.md`

## Signal Integration Design

The integration layer records `permea-signal-ml` as an adjacent public evidence package connected to Core evidence, dataset, benchmark, benchmark execution, research package, public review packet, claim registry, validation, and reproducibility layers.

The integration does not import raw datasets, notebooks, bulky experiment code, package-specific generated outputs, or package-specific paper-support material into Core.

## External Evidence Package Design

External evidence packages are documented through:

- integration docs
- external evidence package template
- external evidence package governance
- external evidence package schema
- deterministic signal integration CLI

The schema requires package ID, package name, repository, purpose, evidence type, linked datasets, linked benchmarks, linked research packages, linked claims, reproducibility path, validation path, claim boundaries, limitations, status, and version.

## CLI Behavior

`python3 scripts/permea_signal.py` prints deterministic signal integration status, registered external evidence package count, `permea-signal-ml` package status, linked Core layers, integration doc paths, repository-boundary reminders, claim-boundary reminders, validation reminders, and `Status: PASS`.

## Tests Run

- `git diff --check`
- `python3 scripts/permea_signal.py`
- `python3 scripts/permea_benchmark_run.py`
- `python3 scripts/permea_review.py`
- `python3 scripts/permea_research.py`
- `python3 scripts/permea_datasets.py`
- `python3 scripts/permea_benchmarks.py`
- `python3 scripts/permea_evidence.py`
- `python3 scripts/permea_check.py`
- `python3 scripts/permea_specs.py`
- `python3 scripts/permea_validate.py`
- `python3 scripts/permea_evaluate.py`
- `python3 scripts/permea_reproduce.py`
- `python3 scripts/validate_permea_artifacts.py`
- `python3 -m pytest`

## Public-Safety Boundary Result

Touched public files are intended to avoid non-public project references, non-public infrastructure references, non-public repository references, and workflow-instruction references.

## Claim-Discipline Result

This layer does not claim:

- wet-lab validation by Permea
- biological efficacy claim
- therapeutic outcome claim
- BBB success claim
- solved-delivery claim
- SOTA performance claim
- experimental validation claim
- clinical evidence claim
- expression improvement claim

Unsupported or future-facing items are framed as computational-only, framework-only, not yet demonstrated, out of scope, or requiring future validation.

## Limitations

This task does not validate the adjacent evidence package independently, copy package assets into Core, create new scientific evidence, or make new scientific claims. It creates a public integration and review layer.

## Next Recommended Task

Add a formal external evidence package registry only after future packages need the same integration metadata, schema validation, and lifecycle review path.
