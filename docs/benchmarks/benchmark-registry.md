# Benchmark Registry

The benchmark registry is the public operating index for Permea Core benchmark surfaces.

It answers what benchmark framework exists, what a benchmark measures, which benchmark cards are required, what evidence is required before a benchmark becomes active, and what remains proposed, computational-only, or not yet validated.

## Registry Status

Benchmark Framework Ready

No active reference benchmark is claimed by this registry. Proposed and draft entries are included only as public review surfaces.

## Registry Fields

| Field | Meaning |
| --- | --- |
| Benchmark ID | Stable registry identifier. |
| Benchmark name | Human-readable benchmark name. |
| Measured property | Bounded computational property or task surface. |
| Status | Lifecycle status from [Benchmark lifecycle](benchmark-lifecycle.md). |
| Linked evidence | Evidence record, generated artifact, or report supporting current status. |
| Linked claims | Claim category or claim boundary supported by current evidence. |
| Linked specifications | Required public specs or schemas. |
| Validation status | Current local validation command or status. |
| Limitations | What the entry does not establish. |

## Current Registry

| Benchmark ID | Benchmark name | Measured property | Status | Linked evidence | Linked claims | Linked specifications | Validation status | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `bbb_b3pred_dataset3` | BBB peptide prioritization surface | Sequence-derived computational prioritization fixture | Draft | [EVIDENCE-038](../evidence/EVIDENCE-038-artifact-validator-bundle.md), [EVIDENCE-040](../evidence/EVIDENCE-040-external-example-packages.md) | Public artifact structure and local validation only | [Benchmark card template](benchmark-card-template.md), [Benchmark card schema](../../schemas/benchmark-card.schema.json), [Benchmark card spec](../specs/SPEC_BENCHMARK_CARD.md) | `python3 scripts/permea_check.py`; `python3 scripts/permea_benchmarks.py` | Not an active reference benchmark; no biological effect, experimental validation, therapeutic outcome, clinical evidence, or solved-delivery claim. |
| `cpp_cppsite2_placeholder` | CPP membrane penetration placeholder | Proposed computational benchmark surface | Proposed | [EVIDENCE-036](../evidence/EVIDENCE-036-artifact-specification-layer.md) | Proposed benchmark metadata only | [Benchmark card template](benchmark-card-template.md), [Benchmark lifecycle](benchmark-lifecycle.md) | Proposed; not active | Placeholder only; source context, label policy, and evidence requirements remain incomplete. |

## Active Benchmark Requirements

A benchmark cannot be considered active until it has:

- a completed benchmark card using [Benchmark card template](benchmark-card-template.md)
- linked dataset, split, metric, output, limitation, and claim-boundary metadata
- reproducible computational workflow evidence
- validation by local public commands
- linked evidence records
- explicit unsupported-claim boundaries

## Where Future Benchmarks Accumulate

- Registry entries: this file
- Benchmark card metadata: future benchmark card files or public YAML fixtures
- Lifecycle requirements: [Benchmark lifecycle](benchmark-lifecycle.md)
- Governance: [Benchmark governance](benchmark-governance.md)
- Schemas: [benchmark-card.schema.json](../../schemas/benchmark-card.schema.json)
- Evidence: `docs/evidence/`

## Explicit Non-Claims

- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
- no clinical evidence claim
- no expression improvement claim
