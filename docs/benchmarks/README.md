# Permea Benchmark Layer

The benchmark layer defines how Permea Core benchmark surfaces are proposed, reviewed, validated, promoted, deprecated, and archived.

This layer does not create biological benchmark results. It provides registry, lifecycle, schema, governance, and CLI surfaces for future benchmark accumulation.

## Start Here

- [Benchmark registry](benchmark-registry.md)
- [Benchmark lifecycle](benchmark-lifecycle.md)
- [Benchmark card template](benchmark-card-template.md)
- [Benchmark governance](benchmark-governance.md)
- [Existing benchmark registry background](BENCHMARK_REGISTRY.md)

## Review Command

```bash
python3 scripts/permea_benchmarks.py
```

The command prints registered benchmark counts, active benchmark counts, lifecycle counts, claim-boundary reminders, and benchmark documentation paths.

## What A Permea Benchmark Measures

A Permea benchmark measures a bounded computational task definition under explicit dataset, split, metric, artifact, and claim-boundary constraints.

Permea benchmarks may support public review of computational workflows. They do not establish biological effect, experimental validation, therapeutic outcome, clinical evidence, or solved delivery.

## Current Public Position

The benchmark framework is ready for public review. Current benchmark surfaces are not active reference benchmarks unless they meet lifecycle entry criteria and evidence requirements.

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
