# Permea Benchmark Layer

The benchmark layer defines how Permea Core benchmark surfaces are proposed, reviewed, executed, validated, promoted, deprecated, and archived.

This layer does not create biological benchmark results. It provides registry, lifecycle, execution, schema, governance, and CLI surfaces for future benchmark accumulation.

## Start Here

- [Benchmark registry](benchmark-registry.md)
- [Benchmark lifecycle](benchmark-lifecycle.md)
- [Benchmark card template](benchmark-card-template.md)
- [Benchmark execution model](benchmark-execution-model.md)
- [Benchmark run template](benchmark-run-template.md)
- [Benchmark governance](benchmark-governance.md)
- [Existing benchmark registry background](BENCHMARK_REGISTRY.md)

## Review Command

```bash
python3 scripts/permea_benchmarks.py
```

The command prints registered benchmark counts, active benchmark counts, lifecycle counts, claim-boundary reminders, and benchmark documentation paths.

Review the benchmark execution framework:

```bash
python3 scripts/permea_benchmark_run.py
```

The command prints benchmark execution framework status, registered benchmark counts, executable benchmark counts, benchmark run artifact status, documentation paths, claim-boundary reminders, and validation reminders.

## What A Permea Benchmark Measures

A Permea benchmark measures a bounded computational task definition under explicit dataset, split, metric, artifact, and claim-boundary constraints.

Permea benchmarks may support public review of computational workflows. They do not establish biological effect, experimental validation, therapeutic outcome, clinical evidence, or solved delivery.

## What A Permea Benchmark Run Records

A Permea benchmark run records one execution instance against a benchmark definition. It should include dataset links, benchmark card link, evaluation protocol, metrics, environment summary, reproducibility path, validation outputs, evidence links, claim boundaries, limitations, status, and version.

Current benchmark execution status is framework-only. No benchmark results are currently registered. No biological conclusions should be drawn from framework readiness alone.

## Current Public Position

The benchmark framework is ready for public review. Current benchmark surfaces are not active reference benchmarks unless they meet lifecycle entry criteria and evidence requirements.

The benchmark execution framework is ready for public review. Current benchmark run surfaces are not registered benchmark results unless a future run artifact satisfies the benchmark run schema, validation expectations, evidence links, and governance review.

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
