# Dataset Registry Layer

The dataset registry layer is the public operating surface for Permea Core dataset cards, provenance records, lifecycle status, and review expectations.

It answers what dataset framework exists, what a dataset card requires, what provenance must be recorded, which benchmark or evidence assets a dataset can support, and what remains proposed, external, computational-only, or not yet validated.

## Review Path

Start with the deterministic CLI:

```bash
python3 scripts/permea_datasets.py
```

Then review:

- [Dataset registry](dataset-registry.md)
- [Dataset lifecycle](dataset-lifecycle.md)
- [Dataset card template](dataset-card-template.md)
- [Dataset provenance](dataset-provenance.md)
- [Dataset governance](dataset-governance.md)
- [Dataset card schema](../../schemas/dataset-card.schema.json)

## Status

Dataset Framework Ready

This layer does not add raw biological datasets. Current entries are documentation and review surfaces for future dataset accumulation.

## Claim Boundaries

Permea dataset records may support computational review, provenance inspection, and reproducibility planning. They do not establish biological effect, experimental validation, therapeutic outcome, clinical evidence, or solved delivery.

Explicit non-claims:

- no dataset acquisition completion claim unless separately validated
- no redistribution-rights confirmation unless separately documented
- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
- no clinical evidence claim
- no expression improvement claim
