# P-CORE-044 Benchmark Registry Layer Report

## Purpose

This report records the first benchmark operating layer for Permea Core. The layer defines registry, lifecycle, card-template, governance, schema, CLI, and review surfaces for future benchmark accumulation.

This task does not create biological benchmark results.

## Files Added Or Changed

- `docs/benchmarks/README.md`
- `docs/benchmarks/benchmark-registry.md`
- `docs/benchmarks/benchmark-lifecycle.md`
- `docs/benchmarks/benchmark-card-template.md`
- `docs/benchmarks/benchmark-governance.md`
- `schemas/benchmark-card.schema.json`
- `schemas/benchmark_card.schema.json`
- `scripts/permea_benchmarks.py`
- `tests/test_benchmark_registry_layer.py`
- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`

## Benchmark Layer Design

The layer separates benchmark maturity from scientific outcome claims:

- Proposed and Draft entries can exist without active benchmark status.
- Active Reference Benchmark status requires reproducible computational workflow evidence, validation, claim boundaries, and governance review.
- Independent, external, experimental, and clinical evidence are separate maturity levels and are not claimed by current benchmark surfaces.

## CLI Behavior

`python3 scripts/permea_benchmarks.py` prints:

- registered benchmark count
- active benchmark count
- proposed, draft, and validated counts
- registry entries
- claim-boundary reminders
- benchmark documentation paths
- `Benchmark Framework Ready`

## Tests Run

```bash
git diff --check
python3 scripts/permea_benchmarks.py
python3 scripts/permea_evidence.py
python3 scripts/permea_check.py
python3 scripts/permea_specs.py
python3 scripts/permea_validate.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/validate_permea_artifacts.py
python3 -m pytest
```

## Public-Safety Boundary Result

Touched public files should not introduce non-public project, funding, non-public repository, continuation-tool, or non-public handoff references. Public benchmark docs and CLI are intended to be standalone.

## Claim-Discipline Result

The benchmark registry layer explicitly preserves non-claims:

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

- Current benchmark entries are not active reference benchmarks.
- The layer defines benchmark operations, not biological results.
- Future benchmark promotion requires lifecycle evidence, validator support, and claim-registry links.

## Next Recommended Task

Add a benchmark-card validator that checks future benchmark card files against the lifecycle status vocabulary, schema, evidence links, and claim-boundary requirements.
