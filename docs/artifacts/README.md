# Artifact Consistency System

The artifact consistency system checks whether public Permea Core review surfaces remain linked, discoverable, and locally reproducible.

It is a documentation and artifact-navigation quality layer. It does not create scientific evidence, benchmark results, dataset records, biological validation, clinical claims, or solved-delivery claims.

## What It Checks

`python3 scripts/permea_artifacts.py` checks:

- public markdown artifact inventory discovery
- local markdown link target existence
- important review surface reachability from `OPEN_THIS_FIRST.md` or `REVIEW_HUB.md`
- `docs/reports/README.md` coverage for public report files

## How To Run

```bash
python3 scripts/permea_artifacts.py
```

For automation-oriented output:

```bash
python3 scripts/permea_artifacts.py --json
```

## Review Path

README -> QUICKSTART -> REVIEW PACKET -> ARTIFACT CONSISTENCY -> REPORTS INDEX -> ARCHITECTURE -> EVIDENCE -> LINEAGE -> CLAIMS -> VALIDATION

## What It Does Not Claim

The artifact consistency system does not claim:

- biological results
- wet-lab validation
- clinical efficacy
- model performance
- solved delivery

It only checks public documentation, report, evidence, architecture, and generated artifact navigation consistency.

## Related Surfaces

- [Open This First](../../OPEN_THIS_FIRST.md)
- [Review Hub](../../REVIEW_HUB.md)
- [Reports index](../reports/README.md)
- [Architecture index](../architecture/README.md)
- [Evidence layer](../evidence/README.md)
- [Lineage layer](../lineage/README.md)
