# Evidence Ladder

## Purpose

This document defines an initial Permea evidence ladder for claim discipline and validation discipline. It is meant to clarify what kinds of statements are justified at each stage of work.

## Why an evidence ladder is needed

Permea should not only publish artifacts. It should also make explicit what those artifacts do and do not support. Without an evidence ladder, computational outputs can be misread as biological confirmation, and ambition can outrun the available evidence.

## Level 0 — Conceptual framing

Level 0 is for thesis, taxonomy, architecture, repository design, and problem framing only. It can clarify why a benchmark matters or how a field should be structured, but it does not support empirical claims.

## Level 1 — Computational signal

Level 1 is for early model outputs, exploratory scoring, and initial computational signal. It can support narrow statements that a non-random signal may be present in the current computational setting. It does not establish biological truth.

## Level 2 — Reproducible benchmark evidence

Level 2 is for regenerated current-contract artifacts such as configs, manifests, metrics, predictions, and comparison tables. It can support bounded claims that a workflow may help candidate prioritization before wet-lab work, provided the claim remains tied to the benchmark surface that was actually regenerated.

## Level 3 — Literature-grounded biological plausibility

Level 3 applies when computational findings are interpreted alongside known mechanisms, prior papers, or established biological context. It can support stronger plausibility arguments, but it still does not constitute direct experimental confirmation of the present candidates or workflow.

## Level 4 — In vitro validation

Level 4 requires actual assay behavior or comparable experimental readouts. At this level, claims can begin to refer to observed biological performance in the tested setting, while still respecting assay limits and context.

## Level 5 — Stronger biological validation

Level 5 is reserved for stronger experimental evidence beyond early in vitro support. It should not be implied prematurely, and it should be used only when the biological validation surface is materially stronger than benchmark outputs or limited assay observations.

## Claim discipline rules

- computational evidence is not experimental validation
- benchmark evidence is not universal delivery proof
- biological claims must not outrun the evidence tier that supports them
- Permea should prefer narrower claims than ambition

## Why this ladder matters for Permea

Permea is trying to build benchmark-first, reproducible, open evidence surfaces. That only works if claim boundaries remain explicit. This ladder gives the project a reusable standard for writing docs, interpreting outputs, and keeping future public artifacts aligned with the actual strength of evidence.
