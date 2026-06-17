# Public Review Packet

This packet gives reviewers a single guided path through Permea Core.

## Guided Review Path

README -> QUICKSTART -> REVIEW PACKET -> EVIDENCE -> BENCHMARKS -> DATASETS -> RESEARCH -> CLAIMS -> VALIDATION

## Reviewer Objective

Understand what Permea Core currently provides, what can be reproduced locally, what evidence and registry infrastructure exists, what public claims are supported, what claims are not supported, and what remains proposed or requiring future validation.

## Expected Review Time

15 to 30 minutes for a first technical orientation. A deeper review should follow the linked evidence, benchmark, dataset, research package, claim, and validation surfaces.

## First Command To Run

```bash
python3 scripts/permea_review.py
```

Then run:

```bash
python3 scripts/permea_demo.py
python3 scripts/permea_evidence.py
python3 scripts/permea_benchmarks.py
python3 scripts/permea_datasets.py
python3 scripts/permea_research.py
python3 scripts/permea_validate.py
```

## Evidence Review Path

- [Evidence map](../evidence/evidence-map.md)
- [Claim-to-evidence matrix](../evidence/claim-to-evidence-matrix.md)
- [Evidence maturity model](../evidence/evidence-maturity-model.md)
- [Evidence timeline](../evidence/evidence-timeline.md)
- [Generated evidence matrix](../examples/generated/EVIDENCE_MATRIX.md)

## Benchmark Review Path

- [Benchmark registry](../benchmarks/benchmark-registry.md)
- [Benchmark lifecycle](../benchmarks/benchmark-lifecycle.md)
- [Benchmark card template](../benchmarks/benchmark-card-template.md)
- `python3 scripts/permea_benchmarks.py`

## Dataset Review Path

- [Dataset registry](../datasets/dataset-registry.md)
- [Dataset lifecycle](../datasets/dataset-lifecycle.md)
- [Dataset provenance](../datasets/dataset-provenance.md)
- `python3 scripts/permea_datasets.py`

## Research Package Review Path

- [Research package registry](../research/research-package-registry.md)
- [Research package lifecycle](../research/research-package-lifecycle.md)
- [Research package assembly](../research/research-package-assembly.md)
- `python3 scripts/permea_research.py`

## Claim Boundary Review Path

- [Claim registry](../claims/claim-registry.md)
- [Claim boundary](../CLAIM_BOUNDARY.md)
- [Claim-to-evidence matrix](../evidence/claim-to-evidence-matrix.md)

## Validation Review Path

- `python3 scripts/permea_check.py`
- `python3 scripts/permea_specs.py`
- `python3 scripts/permea_validate.py`
- `python3 scripts/permea_evaluate.py`
- `python3 scripts/permea_reproduce.py`
- `python3 scripts/validate_permea_artifacts.py`

## What Is Supported

- public artifact specifications and schemas
- deterministic local artifact generation and validation commands
- first-user quickstart demo
- evidence navigation surfaces
- benchmark registry infrastructure
- dataset registry and provenance infrastructure
- research package assembly infrastructure
- explicit public claim-boundary review

## What Is Not Yet Demonstrated

- active biological benchmark results are not demonstrated by this packet
- active reference datasets are not demonstrated by this packet
- public-review research package promotion is not demonstrated by this packet
- external validation is not demonstrated by this packet
- experimental validation is not demonstrated by this packet
- clinical evidence is not demonstrated by this packet

## Limitations

This packet is a review guide for existing public infrastructure. It does not create new scientific evidence, write a paper, submit a paper, publish a paper, establish wet-lab validation by Permea, establish biological efficacy, establish therapeutic outcomes, establish BBB success, establish SOTA performance, establish expression improvement, or establish solved delivery.
