# Synthetic Reference Example

## Overview

This is a minimal neutral reference package for learning the Permea artifact structure.

## What this example demonstrates

- JSON artifact family layout
- validation result structure
- evaluation and reproducibility handoff commands
- explicit claim boundaries and non-claims

## Files included

- [dataset_card.json](dataset_card.json)
- [benchmark_card.json](benchmark_card.json)
- [evidence_card.json](evidence_card.json)
- [run_manifest.json](run_manifest.json)
- [output_package.json](output_package.json)
- [validation_result.md](validation_result.md)
- [validation_result.json](validation_result.json)

## How to validate this example

```bash
python3 scripts/permea_check.py examples/synthetic_reference_example
```

## How to adapt this example

Copy the directory, rename IDs, keep paths repo-relative, preserve non-claims, and rerun the validator.

## Claim boundaries

This example is synthetic metadata only. It does not use a real biological dataset or measure model output.

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

- Synthetic fixture only.
- No source access, acquisition, model execution, or biological result.

## Next steps

Run `python3 scripts/permea_check.py examples/synthetic_reference_example`, then inspect [../../docs/specs/README.md](../../docs/specs/README.md).
