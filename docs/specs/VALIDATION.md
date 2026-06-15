# Permea Artifact Validation

## Overview

This document describes the first public artifact validator layer for Permea Core. The validator checks current public example artifacts against lightweight public specification expectations without adding a full schema-validation dependency.

## Purpose

The validator gives researchers and developers a local way to check whether public artifact examples include the required structural concepts, claim-boundary language, and public-safety hygiene expected by the public Permea artifact standards.

## Supported artifact families

- `dataset_card`
- `benchmark_card`
- `evidence_card`
- `run_manifest`
- `output_package`

## CLI usage

```bash
python3 scripts/permea_check.py --all
python3 scripts/permea_check.py --family dataset_card
python3 scripts/permea_check.py --family benchmark_card
python3 scripts/permea_check.py --family evidence_card
python3 scripts/permea_check.py --family run_manifest
python3 scripts/permea_check.py --family output_package
```

Checking one known public example file is also supported:

```bash
python3 scripts/permea_check.py --file docs/examples/generated/dataset_cards/b3pred_dataset3.md
```

## Validation checks

The validator checks that:

- artifact files exist
- artifact families are known
- required schema concepts are present in the current public example format
- claim-boundary language is present
- explicit non-claim language is present where appropriate
- forbidden public/private boundary terms are absent
- obvious credential-like terms are absent
- report status is deterministic

## Report format

The CLI prints:

- `PASS` or `FAIL`
- checked artifact families
- checked files
- failed checks
- warnings
- non-claim boundary status

## Expected PASS/FAIL behavior

`PASS` means required structural and boundary checks succeeded. `FAIL` means at least one required file, required field concept, claim-boundary check, public/private boundary check, or credential hygiene check failed.

Warnings are deterministic and identify non-blocking review notes. For example, an artifact can have claim-boundary language without using one exact registry non-claim phrase.

## How researchers/developers should use this

Run the validator before proposing new or changed public artifact examples. Add generator, documentation, and test updates together when a new artifact family or required concept is introduced.

## Claim-boundary validation

The validator checks for public-safe claim-boundary language and required explicit non-claims:

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- This is a lightweight validator, not a complete JSON Schema validator.
- Current public examples use Markdown, JSON, and YAML-like files, so required field checks use public spec concepts and aliases.
- The validator checks artifact structure and boundary hygiene; it does not evaluate biological behavior, benchmark quality, source rights, or model performance.

## Next evidence steps

- Expand validator coverage as public artifact families stabilize.
- Add stricter schema validation only when it can be done without brittle coupling or heavy dependencies.
- Keep validation docs, registry metadata, generated examples, and tests aligned.
