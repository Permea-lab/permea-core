# P-CORE-052 Autonomous Queue Pilot

## Purpose

P-CORE-052 tests whether the Permea Core maintenance system can process a small autonomous task queue in one extended run while staying inside bounded review, navigation, documentation, and test scope.

This pilot does not add new scientific evidence, benchmark results, dataset records, or biological claims.

## Selected Queue

1. Refresh `OPEN_THIS_FIRST.md` and `REVIEW_HUB.md` after the P-CORE-051 merge.
2. Add a reports index at `docs/reports/README.md` and link it from public navigation surfaces.
3. Strengthen `docs/architecture/README.md` with existing layer entry points and local review commands.
4. Extend regression tests for freshness, report indexing, architecture navigation, public-safety boundaries, and claim discipline.

## Queue Execution Result

- Queue item 1: Completed.
- Queue item 2: Completed.
- Queue item 3: Completed.
- Queue item 4: Completed.

## Files Added Or Changed

- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/architecture/README.md`
- `docs/reports/README.md`
- `docs/reports/p-core-051-long-run-supervisor-pilot-v0.md`
- `docs/reports/p-core-052-autonomous-queue-pilot-v0.md`
- `tests/test_review_navigation_consistency.py`

## Scope Audit

The queue stayed limited to review navigation, report indexing, architecture index readability, documentation freshness, and regression tests.

No new feature layer, schema family, scientific evidence record, benchmark run, dataset, research package, or external evidence package was added.

## Public-Safety Boundary

Touched public files are designed to avoid non-public project references, non-public operational details, handoff content, and internal process references.

## Claim Discipline

This pilot does not claim biological results, wet-lab validation, clinical efficacy, model performance, or solved delivery. It improves reviewability and consistency of existing public infrastructure only.

## Validation Plan

The intended validation set is:

```bash
git diff --check
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

## Human Judgment Required

Human judgment was still required to choose the queue boundaries: the selected tasks had to be useful enough to test autonomous sequencing without becoming a major feature or architecture expansion.

## Limitations

- The reports index is a navigation surface, not a release history authority.
- The architecture index remains a compact map over existing documents.
- The regression tests cover current navigation expectations and should be updated when future task reports or review paths are added.

## Next Recommended Task

Review the P-CORE-052 pull request. After merge, continue with the next scoped evidence, benchmark-run, dataset, research-package, review-packet, signal-integration, lineage, validation, or review-navigation task.
