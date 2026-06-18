# P-CORE-051 Long-Run Supervisor Pilot

## Purpose

P-CORE-051 tested whether the existing Permea Core development system can handle a bounded multi-step maintenance unit without expanding into risky feature work.

The pilot focused on review navigation, stale-state prevention, architecture indexing, and validation coverage.

## Role Flow

- Supervisor: selected a bounded improvement bundle from existing gaps.
- Worker: refreshed review navigation, added an architecture index, added a task report, and added a focused consistency test.
- Scope Auditor: checked that changes stayed limited to review navigation, architecture indexing, reporting, and tests.
- Boundary Auditor: scanned touched public files for prohibited private or internal references.
- Claim Auditor: scanned touched public files for unsupported biological or performance claims.
- Harness Auditor: ran deterministic review commands, validators, and tests.
- Reporter: recorded this report and linked it from the review surfaces.

## Files Added Or Changed

- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/architecture/README.md`
- `docs/reports/p-core-051-long-run-supervisor-pilot-v0.md`
- `tests/test_review_navigation_consistency.py`

## Bounded Bundle

The work addressed three existing gaps:

1. Review breadcrumbs still referenced an older public baseline and an older recommended next task.
2. The requested `docs/architecture/` review surface did not have a lightweight navigation index.
3. No focused test guarded review navigation against stale baseline drift.

## Architecture Navigation

The new architecture index links existing architecture, specification, operating-docs, decision, ADR, and lineage surfaces. It does not create a new architecture layer or new technical claims.

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

## Public-Safety Boundary

The touched public files are intended to remain free of non-public project references, non-public operational details, handoff content, and internal process references.

## Claim Discipline

This pilot does not add scientific evidence, benchmark results, dataset records, research-package claims, or biological outcome claims. It only improves reviewability and consistency of existing public infrastructure.

## Limitations

- The architecture index is intentionally lightweight.
- It does not replace deeper architecture design documents.
- It does not validate future architecture changes automatically beyond the specific navigation checks added in this task.

## Next Recommended Task

Continue with the next scoped evidence, benchmark-run, dataset, research-package, review-packet, signal-integration, lineage, validation, or review-navigation task.
