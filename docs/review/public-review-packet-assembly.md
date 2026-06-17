# Public Review Packet Assembly

Public review packet assembly explains how to build a guided packet from the current public Permea Core surfaces.

This guide does not create new scientific evidence, write a paper, or claim biological outcomes.

## Assembly Inputs

| Input | Required review |
| --- | --- |
| README | Confirm first-user orientation and links to review packet, quickstart, evidence, benchmarks, datasets, research, claims, and validation. |
| QUICKSTART | Confirm the first successful command and expected local validation path. |
| Evidence assets | Link evidence map, claim matrix, maturity model, timeline, generated evidence matrix, and limitations. |
| Benchmark registry | Link benchmark registry, lifecycle, card template, governance, and CLI. |
| Dataset registry | Link dataset registry, lifecycle, provenance, governance, and CLI. |
| Research package registry | Link research package registry, lifecycle, assembly guide, governance, and CLI. |
| Claim registry | Link supported claims, unsupported claims, and explicit claim boundaries. |
| Validation outputs | Link validation commands and expected pass/fail surfaces. |
| Reproducibility outputs | Link reproduction commands, generated reports, run manifests, and limitations. |

## Assembly Steps

1. Define packet purpose, intended reviewer, review objective, version, and maintainer notes.
2. Set the required reading path: README -> QUICKSTART -> REVIEW PACKET -> EVIDENCE -> BENCHMARKS -> DATASETS -> RESEARCH -> CLAIMS -> VALIDATION.
3. Set the first command: `python3 scripts/permea_review.py`.
4. Link evidence assets and evidence limitations.
5. Link benchmark, dataset, and research package registries.
6. Link claim registry entries and unsupported claim boundaries.
7. Link validation and reproducibility commands.
8. Record what is supported.
9. Record what is not yet demonstrated.
10. Run public-safety and claim-discipline scans before promotion.

## Promotion Rule

Packet promotion requires current links, deterministic commands, validation status, unsupported-claim boundaries, and limitations. Missing or future-facing items must be marked proposed, not yet demonstrated, out of scope, or requiring future validation.
