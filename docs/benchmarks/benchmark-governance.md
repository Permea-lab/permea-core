# Benchmark Governance

Benchmark governance defines how Permea Core benchmark surfaces are proposed, reviewed, promoted, changed, deprecated, and archived.

Benchmark run governance defines how future execution artifacts link back to benchmark definitions, dataset surfaces, evidence records, validation outputs, reproducibility paths, limitations, and claim boundaries.

## Proposing A Benchmark

A benchmark proposal should include:

- benchmark ID
- name
- measured property
- intended use
- dataset requirements
- evaluation protocol
- metrics
- evidence links if available
- claim boundaries
- limitations
- proposed lifecycle status

New proposals start as Proposed unless a complete benchmark card and required evidence already exist.

## Becoming Active

A benchmark may become an Active Reference Benchmark only after:

- benchmark card review is complete
- reproducible computational workflow evidence is linked
- validation commands pass
- claim registry links are present
- limitations are explicit
- unsupported claims are documented
- reviewer approval is recorded

Active status is a computational reference status. It does not establish biological efficacy, therapeutic outcome, experimental validation, clinical evidence, or solved delivery.

## Linking Evidence

Each benchmark should link to:

- evidence records under `docs/evidence/`
- public reports under `docs/reports/`
- relevant generated artifacts under `docs/examples/generated/`
- validation commands
- claim registry entries

If a claim cannot be linked to evidence, narrow the claim or remove it.

## Reviewing Benchmark Runs

Benchmark run changes should review:

- benchmark run schema compatibility
- benchmark registry and benchmark card links
- dataset links and provenance status
- evaluation protocol and metrics
- execution environment summary
- reproducibility path
- validation outputs
- evidence links
- claim boundaries
- limitations

Framework readiness does not imply biological benchmark results. No benchmark result should be treated as registered until the run artifact, validation outputs, evidence links, and governance review are complete.

## Constraining Claims

Benchmark language should prefer:

- computational benchmark surface
- reproducible workflow
- public artifact review
- candidate prioritization before wet-lab work
- evidence maturity
- claim boundary

Benchmark language should not imply experimental, clinical, therapeutic, or solved-delivery outcomes.

## Deprecating Benchmarks

Deprecate a benchmark when:

- source context is no longer appropriate
- labels or metrics are no longer fit for purpose
- leakage or split concerns invalidate the workflow
- a better benchmark supersedes it
- claim boundaries cannot be maintained

Deprecation records should include reason, replacement path if any, date, and reviewer notes.

## Archiving Benchmarks

Archived benchmarks are retained for history. They should not be recommended as current references.

## Reviewing Benchmark Changes

Benchmark changes should review:

- lifecycle status
- schema compatibility
- evidence links
- benchmark run links where applicable
- validation commands
- claim boundaries
- limitations
- downstream docs and README links
- public-safety boundaries
