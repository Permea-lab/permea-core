# Lineage Review Guide

## Reviewer Path

README -> REVIEW PACKET -> RESEARCH -> DATASETS -> BENCHMARKS -> EVIDENCE -> CLAIMS -> LINEAGE

Recommended entry points:

1. [README](../../README.md)
2. [Public review packet](../review/public-review-packet.md)
3. [Research package registry](../research/research-package-registry.md)
4. [Dataset registry](../datasets/dataset-registry.md)
5. [Benchmark registry](../benchmarks/benchmark-registry.md)
6. [Evidence map](../evidence/evidence-map.md)
7. [Claim registry](../claims/claim-registry.md)
8. [Lineage model](lineage-model.md)

## First Command

```bash
python3 scripts/permea_lineage.py
```

## What To Inspect

Reviewers should inspect:

- whether each artifact lists its parent artifacts
- whether downstream child artifacts are visible
- whether related claims are evidence-bounded
- whether linked datasets include provenance status
- whether linked benchmarks include lifecycle status
- whether linked benchmark runs include validation outputs
- whether research packages and review packets preserve upstream limitations
- whether external evidence packages are referenced without copied implementation content

## Lineage Completeness Checks

Ask:

- Does the artifact identify where its evidence originated?
- Are parent and child artifacts listed with stable IDs?
- Are related specifications and validation artifacts linked?
- Are incomplete links marked as draft, documented, proposed, or not yet demonstrated?
- Are deprecated or superseded links preserved for audit history?

## Provenance Checks

Ask:

- Is source attribution present?
- Is the reproducibility path clear?
- Is the validation path clear?
- Are external evidence packages documented as adjacent packages rather than copied into Core?
- Are known limitations visible to downstream reviewers?

## Unsupported Claim Checks

Ask:

- Does the lineage record avoid unsupported biological or clinical claims?
- Are future-facing items explicitly marked framework-only, computational-only, proposed, not yet demonstrated, out of scope, or requiring future validation?
- Does a downstream review packet preserve limitations from upstream evidence, dataset, benchmark, or research package records?

## Limitations Review

Current lineage is a framework and review path. It does not independently validate evidence, complete dataset provenance, activate benchmarks, create benchmark results, or support biological outcome claims.
