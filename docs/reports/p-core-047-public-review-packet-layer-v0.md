# P-CORE-047 Public Review Packet Layer v0

## Purpose

Group P-CORE-047 creates the first public review packet operating layer for Permea Core. The layer gives reviewers one guided packet for orientation, first command, evidence, benchmarks, datasets, research packages, claims, validation, unsupported claims, limitations, and fastest credible review path.

## Files Added Or Changed

- `docs/review/README.md`
- `docs/review/public-review-packet.md`
- `docs/review/public-review-packet-template.md`
- `docs/review/public-review-packet-assembly.md`
- `docs/review/public-review-packet-governance.md`
- `docs/review/public-review-checklist.md`
- `schemas/public-review-packet.schema.json`
- `scripts/permea_review.py`
- `tests/test_public_review_packet_layer.py`
- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`

## Public Review Packet Layer Design

The public review packet layer defines a guided review packet, packet template, assembly guide, governance document, checklist, schema, CLI, and review report. The packet path is:

README -> QUICKSTART -> REVIEW PACKET -> EVIDENCE -> BENCHMARKS -> DATASETS -> RESEARCH -> CLAIMS -> VALIDATION

The layer organizes current public infrastructure only. It does not create new scientific evidence or paper claims.

## Assembly Design

The assembly guide explains how to assemble a packet from README, QUICKSTART, evidence assets, benchmark registry, dataset registry, research package registry, claim registry, validation outputs, and reproducibility outputs.

## CLI Behavior

`python3 scripts/permea_review.py` prints a deterministic summary with:

- public review packet readiness
- recommended reading path
- first command to run
- available registry CLIs
- validation reminder
- claim-boundary reminder
- public review docs and schema paths

The command requires no network access and no non-public assets.

## Tests Run

- `git diff --check`
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

Touched public files were scanned for prohibited public-safety terms. Result: PASS.

## Claim-Discipline Result

Touched public files were scanned for prohibited unsupported scientific claims. Hits are limited to explicit non-claim, future-validation, or out-of-scope language. Result: PASS.

Explicit non-claims:

- no new scientific result claim from this layer
- no paper claim from this layer
- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
- no clinical evidence claim
- no expression improvement claim

## Limitations

This layer does not create new scientific evidence, write a paper, submit a paper, publish a paper, establish external validation, or create biological outcome evidence.

## Next Recommended Task

Add a versioned public review packet metadata fixture only after the packet schema is needed by downstream automation.
