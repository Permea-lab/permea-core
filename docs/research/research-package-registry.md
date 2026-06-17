# Research Package Registry

The research package registry is the public operating index for Permea Core research package surfaces.

It records package purpose, package type, lifecycle status, linked evidence, linked benchmarks, linked datasets, linked specifications, linked claims, reproducibility status, validation status, and limitations. It does not create new scientific results or paper claims.

## Registry Status

Research Package Framework Ready

No active public-review research package is claimed by this registry. Proposed entries are included only as public review surfaces and are not paper claims.

## Registry Fields

| Field | Meaning |
| --- | --- |
| Research package ID | Stable registry identifier. |
| Title | Human-readable package title. |
| Purpose | Why the package exists. |
| Package type | Paper support package, technical report package, external review packet, reproducible artifact package, or proposed package. |
| Status | Lifecycle status from [Research package lifecycle](research-package-lifecycle.md). |
| Linked evidence | Evidence records, generated artifacts, reports, or review surfaces. |
| Linked benchmarks | Benchmark registry entries or benchmark cards referenced by the package. |
| Linked datasets | Dataset registry entries or dataset cards referenced by the package. |
| Linked specifications | Public specs or schemas required to review the package. |
| Linked claims | Claim registry entries or explicit claim-boundary categories. |
| Reproducibility status | Current reproduction command, report, or status. |
| Validation status | Current local validation command or status. |
| Limitations | What the package does not establish. |

## Current Registry

| Research package ID | Title | Purpose | Package type | Status | Linked evidence | Linked benchmarks | Linked datasets | Linked specifications | Linked claims | Reproducibility status | Validation status | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `permea_core_public_artifact_package_v0` | Permea Core public artifact package v0 | Proposed package surface for organizing current evidence, benchmark, dataset, specification, and claim-boundary assets. | Reproducible public artifact package | Proposed | [Evidence map](../evidence/evidence-map.md), [Evidence matrix](../examples/generated/EVIDENCE_MATRIX.md), [Reproducibility report](../examples/generated/REPRODUCIBILITY_REPORT.md) | [Benchmark registry](../benchmarks/benchmark-registry.md) | [Dataset registry](../datasets/dataset-registry.md) | [Specs README](../specs/README.md), [Research package schema](../../schemas/research-package.schema.json) | [Claim registry](../claims/claim-registry.md) | Proposed; current public reproduction command exists but this package is not promoted. | `python3 scripts/permea_research.py`; full validation required before promotion. | Proposed package only; not a submitted paper, not a published paper, not an external validation record, and not a new scientific result claim. |

## Active Package Requirements

A research package cannot be promoted toward public review until it has:

- completed package metadata using [Research package template](research-package-template.md)
- linked evidence, benchmark, dataset, specification, and claim registry entries
- reproducibility path and validation path
- figures and tables inventory where applicable
- explicit limitations and claim boundaries
- local validation command output
- review record for unsupported and future-facing claims

## Where Future Research Packages Accumulate

- Registry entries: this file
- Package metadata: future package cards or public YAML fixtures
- Assembly requirements: [Research package assembly](research-package-assembly.md)
- Lifecycle requirements: [Research package lifecycle](research-package-lifecycle.md)
- Governance: [Research package governance](research-package-governance.md)
- Schema: [research-package.schema.json](../../schemas/research-package.schema.json)
- Evidence: `docs/evidence/`
- Benchmarks: `docs/benchmarks/`
- Datasets: `docs/datasets/`
- Claims: `docs/claims/`

## Explicit Non-Claims

- no submitted paper claim
- no published paper claim
- no new scientific result claim from this layer
- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
- no clinical evidence claim
- no expression improvement claim
