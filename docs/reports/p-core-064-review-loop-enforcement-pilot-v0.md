# P-CORE-064 Review Loop Enforcement Pilot v0

## Purpose

P-CORE-064 makes the P-CORE-061, P-CORE-062, and P-CORE-063 review loop
standard operational before final review. P-CORE-061 defined the review bundle
standard, P-CORE-062 added the completeness checker, and P-CORE-063 added a
copyable complete fixture. This pilot adds a small local readiness gate that
confirms those pieces remain wired together.

## Added Enforcement

This task adds:

- `scripts/check_review_loop_readiness.py`
- `src/permea_core/review_packets/loop_readiness.py`
- focused tests in `tests/test_review_loop_readiness_check.py`

The readiness checker verifies:

- the canonical final review bundle fixture exists at
  `docs/review/examples/final-review-bundle-complete-example.md`
- the canonical fixture passes
  `python3 scripts/check_review_bundle_completeness.py docs/review/examples/final-review-bundle-complete-example.md`
- public review navigation can reach the fixture
- review-loop docs reference both the canonical fixture and
  `scripts/check_review_bundle_completeness.py`
- the fixture keeps the required final review bundle field shape

## Intended Use

Future bounded review-loop tasks should run:

```bash
python3 scripts/check_review_loop_readiness.py
python3 scripts/check_review_loop_readiness.py --json
python3 scripts/check_review_bundle_completeness.py docs/review/examples/final-review-bundle-complete-example.md
```

The readiness check should run before final review so missing fixture links,
missing checker references, or malformed fixture fields are caught locally.

## Boundaries

The readiness checker is local and review-focused. It does not:

- create a broad orchestration framework
- automate merge decisions
- approve factual correctness
- approve merge readiness
- does not create scientific evidence
- does not create benchmark results
- does not create biological validation
- does not create wet-lab validation
- does not create in-vivo validation
- does not create clinical evidence
- does not create model performance evidence
- does not create solved-delivery evidence

## Relationship to P-CORE-061 / P-CORE-062 / P-CORE-063

- P-CORE-061 defines the expected review bundle standard.
- P-CORE-062 checks review bundle field presence.
- P-CORE-063 provides the canonical complete fixture.
- P-CORE-064 checks that the fixture, checker, and public navigation remain
  reachable before final review.

## Limitations

- The checker is a structural readiness check only.
- It checks known public navigation files, not every Markdown link in the
  repository.
- It verifies field labels and checker output, not the factual correctness of a
  future task's live final review bundle.

## Next Recommended Task

Recommended next task: add a small PR-template or release-gate note that lists
`python3 scripts/check_review_loop_readiness.py` beside the existing final
review bundle completeness command, without changing merge automation.
