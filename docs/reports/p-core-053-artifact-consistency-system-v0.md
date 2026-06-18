# P-CORE-053 Artifact Consistency System v0

## Purpose

P-CORE-053 adds a public, bounded artifact consistency system for Permea Core. The system checks whether public documentation, reports, evidence navigation, architecture indexes, review surfaces, and generated validation outputs remain internally linked and discoverable.

This task strengthens Permea Core as benchmark-first, reproducible infrastructure. It does not create new scientific evidence, benchmark results, dataset records, or biological claims.

## Files Added Or Changed

- `src/permea_core/consistency/__init__.py`
- `src/permea_core/consistency/artifacts.py`
- `scripts/permea_artifacts.py`
- `docs/artifacts/README.md`
- `docs/reports/p-core-053-artifact-consistency-system-v0.md`
- `tests/test_artifact_consistency_system.py`
- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/architecture/README.md`
- `docs/reports/README.md`
- `tests/test_review_navigation_consistency.py`

## Implementation Plan Completed

1. Add deterministic public artifact inventory discovery.
2. Add local markdown link-target checks for public review surfaces.
3. Add review-surface reachability checks from `OPEN_THIS_FIRST.md` and `REVIEW_HUB.md`.
4. Add reports-index coverage checks for `docs/reports/*.md`.
5. Add a CLI at `python3 scripts/permea_artifacts.py`.
6. Add regression tests and public review documentation.

## CLI Behavior

`python3 scripts/permea_artifacts.py` prints:

- public markdown artifact count
- consistency issue count
- checks performed
- claim-boundary reminder
- next recommended validation commands
- any missing-link, missing-surface, unreachable-surface, or missing-report-index issues

`python3 scripts/permea_artifacts.py --json` prints deterministic JSON for automation and regression tests.

## Public-Safety Boundary

The artifact consistency system is local, deterministic, and public. It does not require network access, private files, or adjacent repository changes.

## Claim Discipline

This layer does not claim:

- biological results
- wet-lab validation
- clinical efficacy
- model performance
- solved delivery

It only checks documentation, report, evidence, architecture, review, and generated artifact navigation consistency.

## Validation Plan

The intended validation set is:

```bash
git diff --check
python3 scripts/permea_artifacts.py
python3 scripts/permea_lineage.py
python3 scripts/permea_signal.py
python3 scripts/permea_benchmark_run.py
python3 scripts/permea_review.py
python3 scripts/permea_research.py
python3 scripts/permea_datasets.py
python3 scripts/permea_benchmarks.py
python3 scripts/permea_evidence.py
python3 scripts/permea_check.py
python3 scripts/permea_specs.py
python3 scripts/permea_validate.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest
```

## Limitations

- The checker focuses on practical local markdown links and selected review surfaces.
- It does not validate remote URLs.
- It does not prove scientific validity or artifact correctness beyond navigation and discoverability.
- Future report families or review surfaces should update the inventory rules and tests when needed.

## Next Recommended Task

Review the P-CORE-053 pull request. After merge, continue with the next scoped artifact consistency, evidence, benchmark-run, dataset, research-package, review-packet, signal-integration, lineage, or validation task.
