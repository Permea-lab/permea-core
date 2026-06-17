# Public Review Checklist

Use this checklist when reviewing Permea Core through the public review packet.

## Repository Orientation

- [ ] Read `README.md`.
- [ ] Read `OPEN_THIS_FIRST.md`.
- [ ] Read `REVIEW_HUB.md`.
- [ ] Confirm current branch and commit.

## Quickstart Execution

- [ ] Run `python3 scripts/permea_demo.py`.
- [ ] Confirm example discovery output.
- [ ] Confirm validation output.
- [ ] Confirm next recommended commands.

## Evidence Review

- [ ] Read `docs/evidence/evidence-map.md`.
- [ ] Read `docs/evidence/claim-to-evidence-matrix.md`.
- [ ] Read `docs/evidence/evidence-maturity-model.md`.
- [ ] Run `python3 scripts/permea_evidence.py`.

## Benchmark Review

- [ ] Read `docs/benchmarks/benchmark-registry.md`.
- [ ] Read `docs/benchmarks/benchmark-lifecycle.md`.
- [ ] Run `python3 scripts/permea_benchmarks.py`.

## Dataset Review

- [ ] Read `docs/datasets/dataset-registry.md`.
- [ ] Read `docs/datasets/dataset-provenance.md`.
- [ ] Run `python3 scripts/permea_datasets.py`.

## Research Package Review

- [ ] Read `docs/research/research-package-registry.md`.
- [ ] Read `docs/research/research-package-assembly.md`.
- [ ] Run `python3 scripts/permea_research.py`.

## Claim Registry Review

- [ ] Read `docs/claims/claim-registry.md`.
- [ ] Read `docs/CLAIM_BOUNDARY.md`.
- [ ] Confirm unsupported claims are explicit.

## Validation / Reproducibility Review

- [ ] Run `python3 scripts/permea_check.py`.
- [ ] Run `python3 scripts/permea_specs.py`.
- [ ] Run `python3 scripts/permea_validate.py`.
- [ ] Run `python3 scripts/permea_evaluate.py`.
- [ ] Run `python3 scripts/permea_reproduce.py`.
- [ ] Run `python3 scripts/validate_permea_artifacts.py`.

## Unsupported Claims Review

- [ ] Confirm no wet-lab validation by Permea is claimed.
- [ ] Confirm no biological efficacy claim is made.
- [ ] Confirm no therapeutic outcome claim is made.
- [ ] Confirm no BBB success claim is made.
- [ ] Confirm no solved-delivery claim is made.
- [ ] Confirm no SOTA performance claim is made.
- [ ] Confirm no experimental validation claim is made.
- [ ] Confirm no clinical evidence claim is made.
- [ ] Confirm no expression improvement claim is made.

## Public-Safety Boundary Review

- [ ] Confirm no non-public deployment details are introduced.
- [ ] Confirm no non-public repository references are introduced.
- [ ] Confirm no non-public transfer notes are introduced.
- [ ] Confirm no workflow-instruction references are introduced.

## Final Reviewer Notes

- [ ] Record what was reviewed.
- [ ] Record commands run.
- [ ] Record unresolved questions.
- [ ] Record suggested next evidence, benchmark, dataset, research package, claim, or validation task.
