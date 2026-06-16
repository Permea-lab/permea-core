# DEC-001: Reproducibility-First Program Structure

## Context

Permea Core needs to be useful to researchers and developers before it can support stronger scientific claims. A public reviewer must be able to clone the repository, run local commands, regenerate current public artifacts, and inspect what is intentionally not claimed.

## Decision

Permea Core will keep reproducibility as a first-order program structure. Public artifact generation, validation, and reports should be runnable locally before claims are expanded.

## Rationale

Reproducible infrastructure gives reviewers a stable way to inspect the repository. It also prevents future work from relying on hidden state, one-off files, or unstated assumptions.

## Alternatives Considered

- Start with narrative-only documentation.
- Start with model or performance surfaces before reproducibility scaffolding.
- Treat reproducibility as a later cleanup step after more artifacts exist.

These alternatives were rejected because they make review, extension, and claim discipline weaker.

## Consequences

- New artifact surfaces should be connected to generation and validation commands.
- Reports should name the commands used to reproduce the public state.
- Reproducibility gaps should remain visible rather than being hidden behind broader wording.

## Related Reports

- [P-DOC-001 project operating-system adoption v0](../reports/p-doc-001-project-operating-system-adoption-v0.md)
- [P-CORE-036 artifact specification layer](../reports/p-core-036-artifact-specification-layer.md)
- [Generated reproducibility report](../examples/generated/REPRODUCIBILITY_REPORT.md)

## Related Evidence

- [Generated evidence surface](../examples/generated/README.md)
- [Artifact index](../examples/generated/ARTIFACT_INDEX.md)
- [Benchmark dry-run report](../examples/generated/dry_runs/example_benchmark_dry_run.md)

## Claim Boundary

This decision supports reproducible public infrastructure. It does not claim dataset download, acquisition execution, biological validation, clinical effectiveness, model performance, or broad delivery prediction.
