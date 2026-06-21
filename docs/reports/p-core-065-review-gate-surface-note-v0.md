# P-CORE-065 Review Gate Surface Note v0

## Purpose

P-CORE-065 makes the P-CORE-064 review loop readiness checker visible in the
human-facing pull request review surface. P-CORE-064 added the local readiness
checker; this task places that command beside the existing final review bundle
completeness command where contributors and reviewers already prepare a pull
request.

## Updated Gate Surface

The selected gate surface is:

- `.github/PULL_REQUEST_TEMPLATE.md`

The template now includes a narrow review gate checklist with:

```bash
python3 scripts/check_review_bundle_completeness.py
python3 scripts/check_review_loop_readiness.py
```

The checklist is intentionally small. It surfaces the two local review-loop
commands without creating merge automation, release orchestration, or a broader
process framework.

## Relationship to P-CORE-064

P-CORE-064 introduced `python3 scripts/check_review_loop_readiness.py` to check
that the canonical final review bundle fixture, completeness checker, and public
review navigation remain wired together. P-CORE-065 exposes that checker at the
pull request review gate so future contributors know to run it beside the
completeness checker before final review.

## Reviewer Use

For bounded review-loop tasks, reviewers should confirm the PR template checklist
records both commands:

```bash
python3 scripts/check_review_bundle_completeness.py
python3 scripts/check_review_loop_readiness.py
```

Those commands should be run before final review alongside the task-specific
validation commands listed in the PR body or final review bundle.

## Boundaries

This task does not:

- build merge automation
- implement autonomous merge logic
- create a broad release orchestration framework
- modify scientific, model, data, or wet-lab content
- create biological, clinical, benchmark-result, model-performance, or
  solved-delivery claims

## Limitations

- The PR template is a human-facing checklist, not an enforcement mechanism.
- The checklist improves review-surface visibility only; command results still
  need to be run and recorded in the final review bundle.
- The readiness checker remains structural. It does not approve factual
  correctness, claim discipline, or merge readiness by itself.

## Next Recommended Task

Keep using the PR review gate checklist and add future gate-surface notes only
when a recurring human review step needs explicit reviewer visibility.
