# BBB Peptide Reference Example

## Overview

This is a public-safe reference fixture aligned with Permea's sequence-first delivery wedge.

## What this example demonstrates

- BBB peptide artifact-package structure
- validation handoff for a Permea-style package
- evaluation and reproducibility handoff commands
- explicit limits around source access, model output, and biological claims

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
python3 scripts/permea_check.py examples/bbb_peptide_reference_example
```

## How to adapt this example

Copy the directory, replace fixture IDs with public-safe project IDs, keep source and rights status explicit, and preserve non-claims until independent evidence exists.

## Claim boundaries

This package is a reference example/template. It does not claim BBB crossing performance, model performance, source acquisition, source rights confirmation, or wet-lab validation by Permea.

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

- Reference metadata only.
- No row-level dataset, acquisition execution, model scoring, or biological result.

## Next steps

Run `python3 scripts/permea_check.py examples/bbb_peptide_reference_example`, then inspect [../../EVALUATION.md](../../EVALUATION.md).
