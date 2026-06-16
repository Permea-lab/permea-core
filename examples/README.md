# Permea Core External Examples

## Overview

These examples are public-safe reference packages that show how to structure Permea-style artifacts for inspection, validation, evaluation handoff, and reproducibility handoff.

## Available examples

- [Synthetic reference example](synthetic_reference_example/README.md)
- [BBB peptide reference example](bbb_peptide_reference_example/README.md)
- [Expression engineering reference example](expression_engineering_reference_example/README.md)

## How examples relate to Permea specs

Each example includes dataset-card, benchmark-card, evidence-card, run-manifest, and output-package JSON files aligned with the public artifact families in [docs/specs/README.md](../docs/specs/README.md).

## How examples relate to validation

Validate all built-in public examples:

```bash
python3 scripts/permea_check.py
```

Validate a single example package:

```bash
python3 scripts/permea_check.py examples/synthetic_reference_example
```

## How examples relate to evaluation and reproducibility

Examples are copyable input patterns. They can be inspected before using the evaluation and reproducibility flows:

```bash
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
```

## How to copy/adapt an example

Copy an example directory, rename IDs, keep paths repo-relative, preserve explicit non-claims, and rerun `python3 scripts/permea_check.py path/to/example`.

## Explicit non-claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- Examples are reference fixtures only.
- Examples do not demonstrate biological performance, source rights, model performance, or experimental outcomes.
- Examples do not include non-public filesystem paths, private datasets, acquisition execution, or row-level source data.

## Next recommended commands

```bash
python3 scripts/permea_check.py
python3 scripts/permea_validate.py
```
