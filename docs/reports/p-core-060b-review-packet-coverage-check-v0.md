# P-CORE-060B Review Packet Coverage Check v0

## Summary

P-CORE-060B adds a small consistency checker for the existing generated review packet set.

The checker verifies that packet definitions, output paths, generated packet files, reviewed artifact paths, packet index entries, system documentation entries, and raw URL target coverage stay aligned.

## Why This Is A Separate PR

This PR adds a validation surface for the current packet set. It does not add new packet coverage and does not change generated packet Markdown or JSON files.

This keeps the work independent from packet-expansion PRs.

## Files Added Or Changed

- `src/permea_core/review_packets/coverage.py`
- `scripts/check_review_packet_coverage.py`
- `tests/test_review_packet_coverage_check.py`
- `docs/reports/p-core-060b-review-packet-coverage-check-v0.md`
- `docs/reports/README.md`

## Human Review Paths

Open these local files from the repository root:

```bash
open scripts/check_review_packet_coverage.py
open src/permea_core/review_packets/coverage.py
open tests/test_review_packet_coverage_check.py
open docs/reports/p-core-060b-review-packet-coverage-check-v0.md
```

## Validation Commands

```bash
git diff --check
python3 scripts/check_review_packet_coverage.py
python3 scripts/check_review_packet_coverage.py --json
python3 scripts/permea_review_packet.py
python3 scripts/permea_artifacts.py
python3 -m pytest tests/test_review_packet_coverage_check.py
python3 -m pytest
```

## Claim Boundaries

This checker reviews consistency of public review packet coverage only.

It does not create scientific evidence, benchmark results, biological validation, wet-lab validation, clinical efficacy evidence, model performance evidence, or solved-delivery evidence.

## Limitations

- The checker validates current packet coverage structure, not scientific correctness.
- It verifies local files and declared links; it does not replace human review of packet quality.
- It should be extended only when new packet coverage expectations become concrete and public.
