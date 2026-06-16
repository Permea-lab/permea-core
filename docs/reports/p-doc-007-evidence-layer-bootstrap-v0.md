# P-DOC-007 Evidence Layer Bootstrap v0

## Purpose

Create the first public Evidence Layer for Permea Core so supported claims, unsupported claims, validation surfaces, reports, generated artifacts, and decision records are connected in one reviewable evidence system.

## Scope

This task is a documentation and evidence bootstrap only. It creates public evidence records and a public claim registry. It does not add validator functionality, change generated artifact semantics, execute acquisition, download datasets, run models, or expand claims.

## Files Changed

- `docs/evidence/README.md`
- `docs/evidence/evidence-index.md`
- `docs/evidence/EVIDENCE-030-evidence-surface-layer.md`
- `docs/evidence/EVIDENCE-032-reproducibility-bundle.md`
- `docs/evidence/EVIDENCE-034-evaluation-bundle.md`
- `docs/evidence/EVIDENCE-036-artifact-specification-layer.md`
- `docs/claims/claim-registry.md`
- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`
- `docs/decisions/README.md`
- `docs/runbooks/project-documentation-operating-standard.md`
- `docs/specs/README.md`
- `docs/examples/generated/README.md`
- `README.md`

## Method

The bootstrap maps four merged public layers to evidence records:

- Evidence Surface Layer
- Reproducibility Bundle
- Evaluation Bundle
- Artifact Specification Layer

Each evidence record links source task/group, related decisions, primary report, public artifacts, method, validation surface, supported claims, unsupported claims, limitations, reproducibility instructions, and next evidence step.

## Results

- Added `docs/evidence/`.
- Added a public evidence index.
- Added four public evidence records.
- Added `docs/claims/claim-registry.md`.
- Refreshed repository breadcrumbs and review hub.
- Linked evidence references from decision, spec, generated evidence surface, and root README surfaces.

## Validation

Recommended validation:

```bash
git diff --check
python3 scripts/permea_specs.py
python3 scripts/permea_evaluate.py
python3 scripts/permea_reproduce.py
python3 scripts/permea_validate.py
python3 scripts/validate_permea_artifacts.py
```

## Scan Results

Expected scan posture:

- Public/private scan: no restricted paths, non-public process details, restricted infrastructure details, or blocked continuation references.
- Claim-boundary scan: explicit non-claims are allowed; unsupported positive scientific claims are not allowed.
- Secret scan: no API keys, passwords, secrets, or tokens.

## Claim Boundaries

Required non-claims remain:

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no clinical efficacy claim
- no model performance claim
- no SOTA claim
- no solved-delivery claim

## Limitations

- This layer indexes existing merged public evidence surfaces.
- It does not create new scientific evidence.
- It does not add schema validation or artifact validators.
- It does not prove biological behavior, model quality, source access, redistribution rights, or clinical utility.

## Next Recommended Goal

Merge this evidence-layer bootstrap after review if validation and scans remain clean, then add evidence records for future merged artifact or validation layers.
