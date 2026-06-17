# Dataset Registry

The dataset registry is the public operating index for Permea Core dataset surfaces.

It records dataset status, provenance completeness, linked evidence, linked benchmarks, claim boundaries, validation status, and limitations. It does not add raw biological datasets.

## Registry Status

Dataset Framework Ready

No active reference dataset is claimed by this registry. Draft and documented entries are included only as public review surfaces.

## Registry Fields

| Field | Meaning |
| --- | --- |
| Dataset ID | Stable registry identifier. |
| Dataset name | Human-readable dataset name. |
| Source type | External, derived, synthetic fixture, or proposed source category. |
| Intended use | Public use case for review, validation, examples, or future benchmark support. |
| Status | Lifecycle status from [Dataset lifecycle](dataset-lifecycle.md). |
| Linked evidence | Evidence record, generated artifact, or report supporting current status. |
| Linked benchmarks | Benchmark registry entries or benchmark cards that can reference the dataset. |
| Linked claims | Claim category or claim boundary supported by current evidence. |
| Linked specifications | Required public specs or schemas. |
| Provenance status | Current source, acquisition, processing, license, and reproducibility record status. |
| Validation status | Current local validation command or status. |
| Limitations | What the entry does not establish. |

## Current Registry

| Dataset ID | Dataset name | Source type | Intended use | Status | Linked evidence | Linked benchmarks | Linked claims | Linked specifications | Provenance status | Validation status | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `b3pred_dataset3` | B3Pred Dataset 3 public fixture card | Documented external dataset card | Example dataset-card validation and benchmark-card linkage | Draft Card | [EVIDENCE-038](../evidence/EVIDENCE-038-artifact-validator-bundle.md), [EVIDENCE-040](../evidence/EVIDENCE-040-external-example-packages.md) | [`bbb_b3pred_dataset3`](../benchmarks/benchmark-registry.md) | Public artifact structure and local validation only | [Dataset card template](dataset-card-template.md), [Dataset card schema](../../schemas/dataset-card.schema.json), [Dataset card spec](../specs/SPEC_DATASET_CARD.md) | Source reference and limitation metadata documented; acquisition and redistribution remain not yet demonstrated. | `python3 scripts/validate_dataset_cards.py`; `python3 scripts/permea_datasets.py` | Not an active reference dataset; no biological effect, experimental validation, therapeutic outcome, clinical evidence, or solved-delivery claim. |
| `cppsite2_placeholder` | CPPSite 2 placeholder dataset card | Proposed external dataset surface | Proposed future example for source and provenance review | Proposed | [EVIDENCE-036](../evidence/EVIDENCE-036-artifact-specification-layer.md) | [`cpp_cppsite2_placeholder`](../benchmarks/benchmark-registry.md) | Proposed dataset metadata only | [Dataset lifecycle](dataset-lifecycle.md), [Dataset provenance](dataset-provenance.md) | Provenance incomplete; source policy, acquisition method, and license constraints require future validation. | Proposed; not active | Placeholder only; source context, processing policy, label policy, and evidence requirements remain incomplete. |

## Active Dataset Requirements

A dataset cannot be considered active until it has:

- a completed dataset card using [Dataset card template](dataset-card-template.md)
- documented source reference, source type, intended use, and license or usage constraints
- acquisition, processing, transformation, generated-artifact, and reproducibility records
- linked benchmark, evidence, specification, and claim-boundary metadata
- validation by local public commands
- explicit unsupported-claim boundaries

## Where Future Dataset Evidence Accumulates

- Registry entries: this file
- Dataset card metadata: future dataset card files or public YAML fixtures
- Provenance requirements: [Dataset provenance](dataset-provenance.md)
- Lifecycle requirements: [Dataset lifecycle](dataset-lifecycle.md)
- Governance: [Dataset governance](dataset-governance.md)
- Schemas: [dataset-card.schema.json](../../schemas/dataset-card.schema.json)
- Evidence: `docs/evidence/`
- Benchmarks: `docs/benchmarks/`

## Explicit Non-Claims

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
