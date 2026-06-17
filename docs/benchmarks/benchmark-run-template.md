# Benchmark Run Template

Use this template when recording a future Permea benchmark execution artifact.

## Benchmark Run ID

`benchmark_run_id`

## Benchmark ID

`benchmark_id`

## Benchmark Name

Human-readable benchmark name.

## Run Purpose

Why this benchmark run exists and what review question it supports.

## Dataset Links

- dataset registry entry:
- dataset card:
- provenance record:

## Benchmark Card Link

Link to the benchmark card or benchmark registry entry that defines the measured property, intended use, protocol, metrics, limitations, and claim boundaries.

## Evaluation Protocol

Describe the protocol used for the execution, including splits, input artifacts, metric calculations, and expected outputs.

## Metrics

List metrics to be generated or reviewed. Metrics must be tied to the benchmark card and must not imply benchmark performance claims unless supported by validated run evidence.

## Execution Environment Summary

Record environment, command sequence, code version, artifact versions, and relevant configuration summary.

## Reproducibility Path

Commands and artifacts needed to reproduce the run.

## Validation Outputs

- `python3 scripts/permea_check.py`:
- `python3 scripts/permea_specs.py`:
- `python3 scripts/permea_validate.py`:
- `python3 scripts/permea_evaluate.py`:
- `python3 scripts/permea_reproduce.py`:
- `python3 scripts/validate_permea_artifacts.py`:

## Evidence Links

Link evidence records, generated artifacts, validation reports, and review notes that support current status.

## Claim Boundaries

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

List what this run does not establish and which future validation would be required before expanding claims.

## Status

One of:

- planned
- draft
- executed
- validated
- superseded
- archived

## Version

Benchmark run artifact version.

## Maintainer Notes

Reviewer notes, known issues, supersession path, or future validation requirements.
