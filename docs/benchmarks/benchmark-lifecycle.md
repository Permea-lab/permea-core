# Benchmark Lifecycle

The benchmark lifecycle defines how a benchmark moves from idea to active reference benchmark and, later, to deprecation or archive.

Lifecycle status is about public review maturity. It does not imply biological efficacy, experimental validation, therapeutic outcome, clinical evidence, or solved delivery.

Benchmark execution status is tracked separately for benchmark run artifacts. See [Benchmark execution model](benchmark-execution-model.md) and [Benchmark run template](benchmark-run-template.md).

## Statuses

The allowed benchmark card statuses are:

- Proposed
- Draft
- Reproducible Computational Workflow
- Active Reference Benchmark
- Independently Reproduced
- Externally Validated
- Deprecated
- Archived

## Lifecycle Table

| Stage | Entry criteria | Required evidence | Allowed public claims | Prohibited claims | Exit criteria |
| --- | --- | --- | --- | --- | --- |
| Proposed | Benchmark idea, measured property, and intended use are described. | Registry entry or proposal note. | May state that a benchmark surface is proposed. | No result, active benchmark, experimental validation, clinical evidence, or solved-delivery claim. | Benchmark card draft is created. |
| Draft | Benchmark card fields are populated and limitations are explicit. | Draft benchmark card, linked specs, claim boundaries. | May state that a benchmark card is under review. | No active reference benchmark or validated outcome claim. | Reproducible workflow requirements are satisfied. |
| Reproducible Computational Workflow | Public commands reproduce metadata, outputs, or workflow artifacts locally. | Run manifest, output package, validation report, linked evidence record. | May state that computational workflow artifacts reproduce locally. | No independent reproduction, external validation, experimental validation, or clinical evidence claim. | Maintainer review confirms reference readiness. |
| Active Reference Benchmark | Governance review accepts the benchmark as a public reference workflow. | Completed benchmark card, reproducibility evidence, validator output, claim registry link. | May state that the benchmark is an active computational reference benchmark. | No biological efficacy, therapeutic outcome, clinical evidence, or solved-delivery claim. | Independent reproduction record is added or benchmark is revised. |
| Independently Reproduced | Independent reviewer reproduces the computational workflow and records the result. | Dated reproduction report and evidence link. | May state that independent computational reproduction was recorded. | No external validation or experimental validation claim unless separately supported. | External validation record is added or benchmark is revised. |
| Externally Validated | Public external validation record exists for the benchmark workflow. | External validation record, reviewer notes, claim registry update. | May state that an external validation record exists. | No experimental or clinical claim unless separately supported. | Experimental evidence is added or benchmark remains externally validated only. |
| Deprecated | Benchmark is superseded, flawed, stale, or no longer recommended. | Deprecation note with reason and replacement path. | May state that the benchmark is deprecated. | No current benchmark recommendation claim. | Archive or replacement benchmark is approved. |
| Archived | Benchmark is retained for history only. | Archive note, final status, and replacement links if any. | May state that the benchmark is archived. | No active or current recommendation claim. | Reopening requires new proposal review. |

## Evidence Required Before Active Status

Before a benchmark can become an Active Reference Benchmark, it must have:

- a complete benchmark card
- a public dataset/source readiness statement
- a split and metric policy
- expected output artifacts
- reproducibility requirements
- evidence links
- claim boundaries
- limitations
- validation command results
- benchmark run metadata when a run artifact is used to support promotion

## Current Position

Current benchmark surfaces remain Proposed or Draft unless this lifecycle explicitly promotes them with evidence.

Current benchmark execution status is framework-only. No benchmark results are currently registered.
