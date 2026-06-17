# P-CORE-048 Benchmark Execution Layer v0

## Purpose

P-CORE-048 adds the first benchmark execution layer for Permea Core. The layer explains how future benchmark runs should be recorded, validated, linked to evidence, and reviewed without implying biological benchmark results.

## Files Added Or Changed

- `docs/benchmarks/benchmark-execution-model.md`
- `docs/benchmarks/benchmark-run-template.md`
- `docs/benchmarks/README.md`
- `docs/benchmarks/benchmark-registry.md`
- `docs/benchmarks/benchmark-lifecycle.md`
- `docs/benchmarks/benchmark-governance.md`
- `schemas/benchmark-run.schema.json`
- `scripts/permea_benchmark_run.py`
- `tests/test_benchmark_execution_layer.py`
- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/reports/p-core-048-benchmark-execution-layer-v0.md`

## Benchmark Execution Design

The execution layer distinguishes benchmark definitions from benchmark runs:

- benchmark registry entries define the benchmark surface and lifecycle status
- benchmark runs record a specific execution artifact, inputs, protocol, metrics, environment summary, reproducibility path, validation outputs, evidence links, limitations, and claim boundaries

The current repository state is framework-only. No benchmark results are currently registered.

## Benchmark Run Metadata Design

The benchmark run schema requires:

- benchmark run ID
- benchmark ID
- name
- purpose
- status
- dataset links
- benchmark card link
- evaluation protocol
- metrics
- reproducibility path
- validation outputs
- evidence links
- claim boundaries
- limitations
- version

Allowed run statuses are `planned`, `draft`, `executed`, `validated`, `superseded`, and `archived`.

## CLI Behavior

`python3 scripts/permea_benchmark_run.py` prints deterministic framework status, registered benchmark counts, executable benchmark counts, benchmark run count, artifact status, benchmark execution doc paths, claim-boundary reminders, and validation reminders.

The CLI explicitly states:

- `Benchmark Execution Framework Ready`
- `No benchmark results are currently registered.`
- `No biological conclusions should be drawn from framework readiness alone.`

## Tests Run

- `git diff --check`
- `python3 scripts/permea_benchmark_run.py`
- `python3 scripts/permea_review.py`
- `python3 scripts/permea_research.py`
- `python3 scripts/permea_datasets.py`
- `python3 scripts/permea_benchmarks.py`
- `python3 scripts/permea_evidence.py`
- `python3 scripts/permea_check.py`
- `python3 scripts/permea_specs.py`
- `python3 scripts/permea_validate.py`
- `python3 scripts/permea_evaluate.py`
- `python3 scripts/permea_reproduce.py`
- `python3 scripts/validate_permea_artifacts.py`
- `python3 -m pytest`

## Public-Safety Boundary Result

Touched public files are intended to avoid non-public project references, non-public infrastructure references, non-public repository references, and workflow-instruction references.

## Claim-Discipline Result

This layer does not claim:

- wet-lab validation by Permea
- biological efficacy claim
- therapeutic outcome claim
- BBB success claim
- solved-delivery claim
- SOTA performance claim
- experimental validation claim
- clinical evidence claim
- expression improvement claim

Unsupported or future-facing items are framed as framework-only, not yet demonstrated, out of scope, or requiring future validation.

## Limitations

This task does not create benchmark results, biological evidence, benchmark performance claims, or active executable benchmarks. It creates the execution model and review surface for future benchmark run artifacts.

## Next Recommended Task

Add a benchmark run fixture only after a future task defines the run artifact, generated outputs, validation expectations, and claim-boundary review path.
