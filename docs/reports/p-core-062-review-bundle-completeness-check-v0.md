# P-CORE-062 Review Bundle Completeness Check v0

## Summary

P-CORE-062 adds a lightweight deterministic checker for final public review bundle completeness.

The checker encodes part of the P-CORE-061 Review Loop Operating Standard so future low-intervention review loops can detect missing review information before a human or structured assisted final review gate.

## What The Checker Verifies

The checker verifies that review bundle text includes:

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

## What The Checker Does Not Verify

- It does not verify factual correctness of the reported values.
- It does not inspect pull request state on GitHub.
- It does not approve a merge.
- It does not replace human review of scope, wording, or claim boundaries.

## Files Added Or Changed

- `src/permea_core/review_packets/bundle_completeness.py`
- `scripts/check_review_bundle_completeness.py`
- `tests/test_review_bundle_completeness_check.py`
- `docs/reports/p-core-062-review-bundle-completeness-check-v0.md`
- `docs/review/review-loop-operating-standard.md`
- `docs/review/README.md`
- `docs/reports/README.md`
- `REVIEW_HUB.md`

## Human Review Paths

Open these local files from the repository root:

```bash
open src/permea_core/review_packets/bundle_completeness.py
open scripts/check_review_bundle_completeness.py
open tests/test_review_bundle_completeness_check.py
open docs/reports/p-core-062-review-bundle-completeness-check-v0.md
open docs/review/review-loop-operating-standard.md
```

## Validation Commands

```bash
git diff --check
python3 scripts/check_review_bundle_completeness.py
python3 scripts/check_review_bundle_completeness.py --json
python3 scripts/permea_review.py
python3 scripts/permea_artifacts.py
python3 scripts/validate_permea_artifacts.py
python3 scripts/check_review_packet_coverage.py
python3 -m pytest
```

## Review Packet Decision

No generated evidence review packet is added for P-CORE-062.

This checker validates review-bundle handoff text. It does not introduce a new generated artifact system with packet outputs.

## Claim Boundaries

This checker reviews the presence of public review bundle fields only.

It does not create scientific evidence, benchmark results, biological validation, wet-lab validation, in-vivo validation, clinical efficacy evidence, model performance evidence, or solved-delivery evidence.

## Limitations

- The checker validates text presence, not factual correctness.
- The checker does not call GitHub or inspect pull request state.
- The checker should be extended only when the Review Loop Operating Standard changes.
