# P-CORE-061 Autonomous Review-Merge Loop Pilot v0

## Summary

P-CORE-061 records a low-intervention review loop pilot for Permea Core.

The pilot first runs a merge gate for the already reviewed P-CORE-060B review packet coverage check, then opens one additional bounded public pull request that improves review-loop handoff standards.

## Public Scope

The follow-on pull request adds a Review Loop Operating Standard for future public review bundles.

The standard defines what a merge gate or newly opened pull request should report so a reviewer can inspect concrete files, validation commands, local paths, remote URLs, limitations, and claim boundaries without relying on hidden conversation context.

## Files Added Or Changed

- `docs/review/review-loop-operating-standard.md`
- `docs/reports/p-core-061-autonomous-review-merge-loop-pilot-v0.md`
- `docs/review/README.md`
- `docs/reports/README.md`
- `REVIEW_HUB.md`
- `tests/test_review_navigation_consistency.py`

## Human Review Paths

Open these local files from the repository root:

```bash
open docs/review/review-loop-operating-standard.md
open docs/reports/p-core-061-autonomous-review-merge-loop-pilot-v0.md
open docs/review/README.md
open docs/reports/README.md
open REVIEW_HUB.md
open tests/test_review_navigation_consistency.py
```

## Validation Commands

```bash
git diff --check
python3 scripts/permea_review.py
python3 scripts/permea_artifacts.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest tests/test_review_navigation_consistency.py
python3 -m pytest
```

## Review Packet Decision

No generated evidence review packet is added for P-CORE-061.

This task documents review-loop handoff behavior rather than a new artifact system with generated outputs. Future work can add packet coverage if the review-loop standard becomes a generated artifact surface.

## Claim Boundaries

This report describes repository review workflow and public handoff expectations only.

It does not create scientific evidence, benchmark results, biological validation, wet-lab validation, in-vivo validation, clinical efficacy evidence, model performance evidence, or solved-delivery evidence.

## Limitations

- The standard improves review handoff consistency; it does not automate human judgment.
- The pilot is limited to one merge gate plus one follow-on pull request.
- The follow-on pull request remains open for separate review.
