# Architecture Index

This index points reviewers to the current Permea Core architecture surfaces. It is navigation only; it does not introduce new architecture or scientific claims.

## Start Here

- [Architecture design](../DD-ARCHITECTURE.md)
- [Specification](../SPEC.md)
- [OSS operating docs map](../OSS_OPERATING_DOCS_MAP.md)
- [Decision records](../decisions/README.md)
- [Benchmark-first ADR](../adr/ADR-0002-benchmark-first.md)
- [Lineage model](../lineage/lineage-model.md)
- [Artifact consistency](../artifacts/README.md)
- [Reports index](../reports/README.md)
- [Public review packet](../review/README.md)
- [Evidence map](../evidence/evidence-map.md)

## Layer Entry Points

- [Evidence](../evidence/README.md)
- [Benchmarks](../benchmarks/README.md)
- [Benchmark execution](../benchmarks/benchmark-execution-model.md)
- [Datasets](../datasets/README.md)
- [Research packages](../research/README.md)
- [Signal integration](../integrations/README.md)
- [Lineage](../lineage/README.md)
- [Claims](../claims/claim-registry.md)

## Local Review Commands

```bash
python3 scripts/permea_review.py
python3 scripts/permea_artifacts.py
python3 scripts/permea_lineage.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
```

## Review Path

README -> QUICKSTART -> REVIEW PACKET -> ARCHITECTURE -> EVIDENCE -> LINEAGE -> CLAIMS -> VALIDATION

## Boundary

Architecture docs describe repository structure, artifact surfaces, review paths, and reproducibility expectations. They do not claim biological results, wet-lab validation, clinical efficacy, or solved delivery.
