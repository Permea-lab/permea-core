# Benchmark Card Template

Use this template when proposing or updating a Permea benchmark card.

## Benchmark ID

`permea_<domain>_<short_name>_<version>`

## Name

Human-readable benchmark name.

## Purpose

Explain why the benchmark exists and what review question it supports.

## Measured Property

Define the bounded computational property or task. Avoid language that implies biological outcome validation.

## Intended Use

State how researchers and reviewers should use the benchmark. Keep use limited to computational review unless stronger evidence exists.

## Dataset Requirements

- dataset card path
- source context
- label policy
- redistribution posture
- leakage controls
- known limitations

## Evaluation Protocol

- task type
- split policy
- baseline policy
- execution command if available
- expected generated artifacts

## Metrics

- primary metric
- secondary metrics
- metric rationale
- metric limitations

## Reproducibility Requirements

- run manifest
- output package
- validator command
- expected deterministic artifacts
- dependency assumptions

## Evidence Links

- evidence record
- report
- generated artifact
- validation output
- claim registry link

## Claim Boundaries

State what the benchmark can support and what it cannot support.

Required non-claims:

- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
- no clinical evidence claim
- no expression improvement claim

## Limitations

- source limitations
- label limitations
- split limitations
- metric limitations
- release limitations
- evidence maturity limitations

## Status

Must be one of the statuses in [Benchmark lifecycle](benchmark-lifecycle.md).

## Version

Use semantic or date-based versioning for benchmark card updates.

## Maintainer Notes

Record reviewer notes, change rationale, open questions, and next evidence needed.
