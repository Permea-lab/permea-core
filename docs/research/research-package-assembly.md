# Research Package Assembly

Research package assembly describes how Permea Core turns evidence assets, benchmark cards, dataset cards, specification records, validation outputs, reproducibility outputs, and claim registry entries into a reviewable package.

This guide does not create a paper, paper submission, publication, or new scientific result. It defines the assembly path for future packages.

## Reviewer Path

README -> QUICKSTART -> EVIDENCE -> BENCHMARKS -> DATASETS -> RESEARCH PACKAGE -> CLAIMS -> VALIDATION

Recommended commands:

```bash
python3 scripts/permea_demo.py
python3 scripts/permea_evidence.py
python3 scripts/permea_benchmarks.py
python3 scripts/permea_datasets.py
python3 scripts/permea_research.py
python3 scripts/permea_validate.py
```

## Assembly Inputs

| Input | Required review |
| --- | --- |
| Evidence assets | Link evidence IDs, evidence map entries, generated evidence matrix rows, reports, and limitations. |
| Benchmark cards | Link benchmark IDs, lifecycle status, measured property, metrics, validation status, and benchmark limitations. |
| Dataset cards | Link dataset IDs, provenance status, source references, usage constraints, validation status, and dataset limitations. |
| Specification records | Link specs, schemas, validators, and artifact requirements. |
| Validation outputs | Link commands, pass/fail state, validator scope, and known gaps. |
| Claim registry entries | Link supported claims, unsupported claims, and evidence boundaries. |
| Reproducibility outputs | Link reproduction commands, generated reports, run manifests, and reproducibility limitations. |

## Assembly Steps

1. Define package purpose, audience, package type, status, and version.
2. Link evidence records and generated evidence surfaces.
3. Link benchmark registry entries and benchmark cards.
4. Link dataset registry entries, dataset cards, and provenance records.
5. Link specifications, schemas, and validator commands.
6. Link claim registry entries and explicit unsupported-claim boundaries.
7. Record reproducibility path and validation path.
8. Record figures and tables inventory when applicable.
9. Record limitations and review status.
10. Run local validation commands before promotion.

## Promotion Rule

Package promotion requires current evidence links, benchmark links, dataset links, specification links, claim boundaries, validation output, reproducibility output, and limitations. Missing or future-facing items must be marked proposed, not yet demonstrated, out of scope, or requiring future validation.
