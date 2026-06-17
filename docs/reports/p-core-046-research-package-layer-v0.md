# P-CORE-046 Research Package Layer v0

## Purpose

Group P-CORE-046 creates the first research-package operating layer for Permea Core. The layer makes package status, evidence linkage, benchmark linkage, dataset linkage, specification linkage, claim boundaries, reproducibility path, validation path, and review limitations inspectable without writing a new paper or claiming new scientific results.

## Files Added Or Changed

- `docs/research/README.md`
- `docs/research/research-package-registry.md`
- `docs/research/research-package-lifecycle.md`
- `docs/research/research-package-template.md`
- `docs/research/research-package-governance.md`
- `docs/research/research-package-assembly.md`
- `schemas/research-package.schema.json`
- `scripts/permea_research.py`
- `tests/test_research_package_layer.py`
- `README.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`

## Research Package Layer Design

The research package layer defines a registry, lifecycle, template, assembly guide, governance path, schema, and CLI. Current registry entries are proposed public review surfaces only:

- `permea_core_public_artifact_package_v0`: proposed package surface for organizing current evidence, benchmark, dataset, specification, and claim-boundary assets

No active public-review research package, paper submission, publication, external review record, or new scientific result is claimed by this layer.

## Assembly Design

The assembly guide defines how a package should link evidence assets, benchmark cards, dataset cards, specification records, validation outputs, claim registry entries, and reproducibility outputs. Missing or future-facing items must be marked proposed, not yet demonstrated, out of scope, or requiring future validation.

## CLI Behavior

`python3 scripts/permea_research.py` prints a deterministic summary with:

- registered research package count
- active/public-review package count
- proposed, draft, submitted, and published counts
- registry entry status
- reproducibility reminder
- claim-boundary reminder
- research docs and schema paths

The command requires no network access and no non-public assets.

## Tests Run

- `git diff --check`
- `python3 scripts/permea_research.py`
- `python3 scripts/permea_datasets.py`
- `python3 scripts/permea_benchmarks.py`
- `python3 scripts/permea_evidence.py`
- `python3 scripts/permea_check.py`
- `python3 scripts/permea_specs.py`
- `python3 scripts/permea_validate.py`
- `python3 scripts/permea_evaluate.py`
- `python3 scripts/permea_reproduce.py`
- `python3 scripts/validate_permea_artifacts.py`
- `python3 -m pytest`

## Public-Safety Boundary Result

Touched public files were scanned for prohibited public-safety terms. Result: PASS.

## Claim-Discipline Result

Touched public files were scanned for prohibited unsupported scientific claims. Hits are limited to explicit non-claim, future-validation, or out-of-scope language. Result: PASS.

Explicit non-claims:

- no paper claim unless separately reviewed and approved
- no new scientific result claim from this layer
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

This layer does not write a paper, submit a paper, publish a paper, create new scientific evidence, create external review evidence, or create biological outcome evidence.

## Next Recommended Task

Add a concrete research package card only after its evidence links, benchmark links, dataset links, specification links, claim boundaries, validation path, and reproducibility path are complete for the stated package scope.
