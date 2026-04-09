# Biocore ML Summary

## Framing

This note captures the initial machine learning framing for Permea Core. It is not a literature review and does not claim comprehensive coverage. Its role is to define the problem surface that the repository intends to make operational.

## Core Observation

Many biological ML efforts concentrate on sequence modeling alone, while practical delivery and expression outcomes depend on additional context, assay design, and experimental constraints. That makes purely sequence-level comparison insufficient for engineering use.

## Repository Implication

Permea Core should treat the problem as a coupled system:

- sequence as the primary design object
- delivery context as a first-class conditioning variable
- expression or downstream outcome as the evaluation target

## Working Research Direction

The technical challenge is to build benchmarks and workflows that preserve this coupling without collapsing into vague task definitions. The repository should therefore prioritize:

- explicit task statements
- clear data lineage
- comparable baselines
- result formats that are easy to audit

## Status

This document is an initial orientation note. Specific papers, datasets, and benchmark mappings will be added only when they are incorporated into a concrete technical plan.
