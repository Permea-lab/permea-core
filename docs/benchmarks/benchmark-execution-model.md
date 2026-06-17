# Benchmark Execution Model

The benchmark execution model defines how Permea Core records a benchmark run after a benchmark has been proposed, documented, and linked to dataset, evidence, validation, and claim-boundary surfaces.

This layer is framework-only. Framework readiness does not imply biological benchmark results, benchmark performance, or biological conclusions.

## Purpose

Benchmark execution exists to make future benchmark runs reviewable. A benchmark run should record what was executed, which benchmark definition and dataset surfaces were used, what artifacts were generated, which validation commands reviewed the artifacts, and which claims remain unsupported.

## Registry Versus Run

| Surface | Purpose | Output |
| --- | --- | --- |
| Benchmark registry | Lists proposed, draft, active, deprecated, and archived benchmark definitions. | Benchmark IDs, lifecycle status, linked evidence, linked claims, and limitations. |
| Benchmark run | Records one execution instance against a benchmark definition. | Run ID, dataset links, protocol, metrics, environment summary, validation outputs, evidence links, and claim boundaries. |

The registry answers whether a benchmark definition exists. A benchmark run answers whether a specific execution artifact has been recorded and validated.

## Required Execution Metadata

Each benchmark run should record:

- benchmark run ID
- benchmark ID
- benchmark name
- run purpose
- status
- dataset links
- benchmark card link
- evaluation protocol
- metrics
- execution environment summary
- reproducibility path
- validation outputs
- evidence links
- claim boundaries
- limitations
- version
- maintainer notes

## Required Dataset Links

Benchmark runs must link to dataset cards, dataset registry entries, or documented dataset provenance records before promotion beyond draft status.

Dataset links should identify source type, provenance status, usage constraints, processing summary, and limitations. Dataset links do not establish biological outcome evidence.

## Required Benchmark Card Links

Every benchmark run should link back to a benchmark card or registry entry that defines:

- measured property
- intended use
- dataset requirements
- evaluation protocol
- metrics
- reproducibility requirements
- claim boundaries
- limitations

## Required Evidence Links

Benchmark runs should link to evidence records, generated artifacts, reports, and validation outputs that support the run's current status. Evidence links should be specific enough for a reviewer to reproduce or inspect the run artifact.

## Required Validation Outputs

Validation outputs should include local command results or generated validation artifacts. Current public validation surfaces include:

- `python3 scripts/permea_check.py`
- `python3 scripts/permea_specs.py`
- `python3 scripts/permea_validate.py`
- `python3 scripts/permea_evaluate.py`
- `python3 scripts/permea_reproduce.py`
- `python3 scripts/validate_permea_artifacts.py`

## Reproducibility Requirements

A benchmark run should include a reproducibility path with:

- command sequence
- input artifact references
- output artifact paths
- environment summary
- versioned benchmark and dataset links
- validation command outputs
- limitations and unsupported claims

## Claim Boundaries

Benchmark execution artifacts are computational review surfaces. A run artifact may describe execution metadata, generated files, validation status, and limitations.

Benchmark execution artifacts must not imply:

- wet-lab validation by Permea
- biological efficacy claim
- therapeutic outcome claim
- BBB success claim
- solved-delivery claim
- SOTA performance claim
- experimental validation claim
- clinical evidence claim
- expression improvement claim

## Limitations

This model does not create biological benchmark results. It does not make benchmark performance claims. It defines the minimum public structure for future benchmark run artifacts.

## No-Result State

Current public benchmark execution status is:

Benchmark Execution Framework Ready

No benchmark results are currently registered.

No biological conclusions should be drawn from framework readiness alone.
