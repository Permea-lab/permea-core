# P-CORE-050 Evidence Lineage Layer v0

## Purpose

P-CORE-050 adds the first lineage and provenance framework for Permea Core. It defines how claims, evidence, datasets, benchmarks, benchmark runs, research packages, review packets, external evidence packages, specifications, and validation artifacts should be linked for review.

This task does not create new scientific evidence, biological findings, or benchmark results.

## Files Added Or Changed

- `docs/lineage/README.md`
- `docs/lineage/lineage-model.md`
- `docs/lineage/lineage-governance.md`
- `docs/lineage/lineage-review-guide.md`
- `docs/lineage/lineage-record-template.md`
- `schemas/lineage-record.schema.json`
- `scripts/permea_lineage.py`
- `tests/test_evidence_lineage_layer.py`
- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/reports/p-core-050-evidence-lineage-layer-v0.md`

## Lineage Design

The lineage layer defines relationship expectations for:

- Evidence
- Benchmarks
- Benchmark Runs
- Datasets
- Research Packages
- Review Packets
- External Evidence Packages
- Claims
- Specifications
- Validation Artifacts

The model requires parent artifacts, child artifacts, related claims, lineage status, provenance notes, and version metadata. It also supports optional links to evidence, benchmarks, datasets, research packages, review packets, external evidence packages, specifications, and validation artifacts.

## Provenance Model

Lineage records should expose where an artifact came from, what it depends on, what depends on it, which claims it touches, which validation artifacts exist, and what remains incomplete.

Incomplete lineage should remain visible and should be marked draft, documented, proposed, not yet demonstrated, out of scope, or requiring future validation as appropriate.

## CLI Behavior

`python3 scripts/permea_lineage.py` prints:

- lineage framework readiness
- count of lineage-capable artifact classes
- lineage status categories
- lineage documentation and schema paths
- provenance reminders
- claim-boundary reminders
- validation reminders

The command is deterministic, local, and does not require network access or private files.

## Tests Run

Validation expected for this layer:

- `git diff --check`
- `python3 scripts/permea_lineage.py`
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

Touched public files are designed to avoid prohibited public-safety terms and private workflow references.

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

Lineage presence is framework-only unless supported by reviewed evidence and validation artifacts.

## Limitations

- No individual lineage records are activated by this task.
- No external evidence package is independently validated by this task.
- No dataset, notebook, experiment code, or paper implementation detail is copied from the adjacent public evidence repo.
- The lineage schema provides metadata structure, not scientific validation.

## Next Recommended Task

Create the first example lineage records for existing public evidence, benchmark, dataset, research, review, and signal integration surfaces once a small registry format is selected.
