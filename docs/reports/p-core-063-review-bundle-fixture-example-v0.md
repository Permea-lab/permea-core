# P-CORE-063 Review Bundle Fixture Example

## Summary

P-CORE-063 adds a canonical complete example final review bundle for future Permea Core review loops.

The fixture lives at:

- [docs/review/examples/final-review-bundle-complete-example.md](../review/examples/final-review-bundle-complete-example.md)

## Why It Exists

P-CORE-061 defined the Review Loop Operating Standard. P-CORE-062 added a
deterministic checker for required review-bundle fields.

P-CORE-063 makes the expected final bundle concrete, so future loops can copy a
public-safe fixture instead of reconstructing the format from hidden
conversation context.

## How It Reduces User Intervention

Future loops can start from the fixture, fill in the live PR details, run the
completeness checker, and produce a final review bundle that already includes
the required local paths, remote URLs, validation results, audits, review packet
decision, and stop reason.

That reduces repeated reviewer setup work and makes missing handoff fields visible before final review.

## What It Checks

The fixture is validated by:

```bash
python3 scripts/check_review_bundle_completeness.py docs/review/examples/final-review-bundle-complete-example.md
```

The checker confirms required field presence for:

- PR URL
- branch name
- head SHA
- changed files
- validation commands and results
- local human-review paths
- remote GitHub review URLs
- scope audit result
- boundary audit result
- claim-discipline audit result
- review packet decision
- stop reason
- final human/model-assisted review gate status or recommendation

## What It Does Not Check

The fixture and checker do not verify factual correctness, live GitHub state,
merge readiness, scientific evidence, benchmark results, biological validation,
wet-lab validation, in-vivo validation, clinical evidence, model performance
evidence, or solved-delivery evidence.

## Future Loop Use

Future Permea Core loops should:

1. Copy the fixture shape.
2. Replace fictional values with live PR data.
3. Add exact validation command results.
4. Add local absolute review paths and remote GitHub review URLs.
5. Record scope, boundary, and claim-discipline audit results.
6. Run the completeness checker before final review.
7. Leave the pull request unmerged unless the task explicitly authorizes merge.

## Validation

- `git diff --check`: PASS
- `python3 scripts/check_review_bundle_completeness.py`: PASS
- `python3 scripts/check_review_bundle_completeness.py --json`: PASS
- `python3 scripts/check_review_bundle_completeness.py docs/review/examples/final-review-bundle-complete-example.md`:
  PASS
- `python3 scripts/permea_review.py`: PASS
- `python3 scripts/permea_artifacts.py`: PASS
- `python3 scripts/validate_permea_artifacts.py`: PASS
- `python3 scripts/check_review_packet_coverage.py`: PASS
- `python3 -m pytest`: PASS

## Boundary

This report documents a reviewability fixture only. It does not create new
evidence, benchmark results, biological validation, clinical evidence, model
performance evidence, or solved-delivery evidence.
