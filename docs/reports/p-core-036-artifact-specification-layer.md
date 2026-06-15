# P-CORE-036 Artifact Specification Layer

## Objective

Create the first public artifact specification layer for Permea Core.

## Why this layer exists

Permea Core now has reproducible and evaluable public artifact bundles. The next layer is a public standard that researchers and developers can inspect, implement, validate, and extend without relying on one generated example.

## What changed

- Added a public artifact specification index.
- Added five public specification documents.
- Added five lightweight JSON schemas.
- Added a deterministic specification registry module and CLI.
- Added focused tests for specification presence, schema structure, registry output, documentation links, and explicit non-claims.

## Public artifacts added

- `docs/specs/README.md`
- `docs/specs/SPEC_DATASET_CARD.md`
- `docs/specs/SPEC_BENCHMARK_CARD.md`
- `docs/specs/SPEC_EVIDENCE_CARD.md`
- `docs/specs/SPEC_RUN_MANIFEST.md`
- `docs/specs/SPEC_OUTPUT_PACKAGE.md`
- `schemas/dataset_card.schema.json`
- `schemas/benchmark_card.schema.json`
- `schemas/evidence_card.schema.json`
- `schemas/run_manifest.schema.json`
- `schemas/output_package.schema.json`
- `scripts/permea_specs.py`

## Technical design

The layer is intentionally lightweight. Specification documents define public-facing expectations. JSON schemas define minimum required structure. The registry module exposes deterministic metadata for scripts and tests.

## Specification registry design

`src/permea_core/specs/registry.py` contains a static registry of artifact families, spec paths, schema paths, and purposes. `scripts/permea_specs.py` prints the registry without writing generated output.

## Schema design decisions

Schemas require stable identifiers, core structural fields, limitations, and claim boundaries. `additionalProperties` is set to `true` so external researchers and developers can extend artifacts without waiting for a schema revision.

## How this supports researchers and developers

Researchers can inspect the minimum public structure for dataset cards, benchmark cards, evidence cards, run manifests, and output packages. Developers can build generators, validators, and contribution workflows against stable path and field expectations.

## How this supports future papers/reports/proposals

Future public reports can reference artifact standards rather than describing each artifact from scratch. Papers and proposals can point to public schemas, specification docs, and deterministic registry output as reusable infrastructure.

## Validation commands

```bash
python3 scripts/permea_specs.py
python3 -m pytest tests/test_artifact_specs.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
```

## Claim boundaries

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- This layer defines public artifact standards only.
- It does not add a validator bundle.
- It does not download datasets, execute acquisition, call external services, run ML, score candidates, or measure performance.
- It does not confirm source access, license status, redistribution status, biological behavior, or clinical utility.

## Next evidence steps

- Add a dedicated artifact-spec validator bundle in a later group.
- Connect schema checks to future contribution workflows.
- Keep new artifact families aligned with public specifications, schemas, and claim boundaries.

