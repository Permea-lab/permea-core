# ADR-0002: Benchmark-First

## Status

Accepted

## Context

Permea Core is being formed before the repository has broad implementation coverage or established result history. At this stage, the main risk is not limited feature scope. The main risk is building code and claims on top of unstable task definitions, weak provenance, and non-comparable outputs.

## Decision

Permea Core will be benchmark-first. Benchmark definitions, evaluation rules, provenance requirements, and reproducible workflows take priority over broader repository expansion.

## Alternatives Considered

### Model-First

Prioritize sophisticated models before benchmark and provenance infrastructure.

Not chosen because it makes comparison, audit, and repository consistency harder.

### Product-Surface-First

Prioritize broader interfaces or platform features before benchmark contracts are stable.

Not chosen because it expands surface area without strengthening the public technical foundation.

## Tradeoffs

- visible repository breadth grows more slowly
- benchmark and provenance work requires more up-front discipline
- some contributors may prefer feature work before interface stability exists

## Rationale

Permea Core should first establish exact benchmark surfaces and reproducible workflows. That is the most credible path for an open toolkit and benchmarks program in sequence-first delivery and mRNA expression engineering.
