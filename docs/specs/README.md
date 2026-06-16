# Permea Core Public Artifact Specifications

## Overview

This directory defines the first public artifact specification layer for Permea Core. It gives researchers and developers stable, lightweight standards for creating, inspecting, implementing, validating, and extending public artifact families.

## Specification Index

| Artifact family | Specification | Schema |
| --- | --- | --- |
| Dataset cards | [SPEC_DATASET_CARD.md](SPEC_DATASET_CARD.md) | [dataset_card.schema.json](../../schemas/dataset_card.schema.json) |
| Benchmark cards | [SPEC_BENCHMARK_CARD.md](SPEC_BENCHMARK_CARD.md) | [benchmark_card.schema.json](../../schemas/benchmark_card.schema.json) |
| Evidence cards | [SPEC_EVIDENCE_CARD.md](SPEC_EVIDENCE_CARD.md) | [evidence_card.schema.json](../../schemas/evidence_card.schema.json) |
| Run manifests | [SPEC_RUN_MANIFEST.md](SPEC_RUN_MANIFEST.md) | [run_manifest.schema.json](../../schemas/run_manifest.schema.json) |
| Output packages | [SPEC_OUTPUT_PACKAGE.md](SPEC_OUTPUT_PACKAGE.md) | [output_package.schema.json](../../schemas/output_package.schema.json) |

## Registry Command

```bash
python3 scripts/permea_specs.py
```

The command prints the available public specs, schema paths, governed artifact families, and explicit non-claims.

## Validator Command

```bash
python3 scripts/permea_check.py
```

The validator checks current public example artifacts against lightweight Permea standard expectations for required fields, artifact type recognition, repo-relative paths, non-claims, claim-boundary wording, and evidence linkage.

Copyable validator-compatible packages are available in [External Examples](../../examples/README.md).

## Evidence Reference

- [EVIDENCE-036: Artifact Specification Layer](../evidence/EVIDENCE-036-artifact-specification-layer.md)
- [EVIDENCE-038: Artifact Validator Bundle](../evidence/EVIDENCE-038-artifact-validator-bundle.md)
- [EVIDENCE-040: External Example Packages](../evidence/EVIDENCE-040-external-example-packages.md)

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Extension Policy

New artifact specs should define required fields, recommended fields, field definitions, example structure, validation expectations, claim boundaries, limitations, and extension points before they become reviewer-facing standards.
