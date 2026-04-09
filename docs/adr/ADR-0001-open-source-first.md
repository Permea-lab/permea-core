# ADR-0001: Open-Source-First

## Status

Accepted

## Context

Permea Core is intended to serve as a public technical foundation for sequence-first delivery and mRNA expression engineering. The repository centers on benchmark definitions, reproducible workflows, and technical contracts that need outside review to be credible.

If these core surfaces are opaque, the repository becomes difficult to audit, compare, or extend.

## Decision

Permea Core will be open-source-first. Specifications, benchmark definitions, architecture documents, reference workflow logic, and provenance expectations should be public by default unless legal, ethical, biosafety, or confidentiality constraints require restriction.

## Tradeoffs and Constraints

- public development increases the documentation burden
- some data or methods may require restricted handling
- external legibility can slow rapid internal iteration
- open visibility does not remove the need for review discipline

## Rationale

Permea Core is an open toolkit and benchmarks program before it is anything else. Open-source-first is therefore a structural decision, not a presentation choice.
