# P-CORE-030 Evidence Surface Layer Review Packet

This packet makes one public Permea artifact system reviewable from GitHub.
It is intended for human review and structured assisted review.

It should be read together with the linked source files, tests, report, and validation command output.

## Packet Metadata

| Field | Value |
| --- | --- |
| Packet ID | `p-core-030-evidence-surface-layer` |
| Artifact path | [docs/examples/generated/README.md](../../examples/generated/README.md) |
| Artifact type | generated public evidence navigation surface |

## Purpose

Help a reviewer inspect the generated evidence surface through its navigation README, evidence record, source module, generation command, validation commands, linked artifact families, boundaries, and limitations.

## Related Evidence And Report Links

| Review surface | Link |
| --- | --- |
| `scripts/generate_evidence_surface.py` | [scripts/generate_evidence_surface.py](../../../scripts/generate_evidence_surface.py) |
| `scripts/permea_evidence.py` | [scripts/permea_evidence.py](../../../scripts/permea_evidence.py) |
| `scripts/permea_validate.py` | [scripts/permea_validate.py](../../../scripts/permea_validate.py) |
| `scripts/validate_permea_artifacts.py` | [scripts/validate_permea_artifacts.py](../../../scripts/validate_permea_artifacts.py) |
| `src/permea_core/surface/evidence_surface.py` | [src/permea_core/surface/evidence_surface.py](../../../src/permea_core/surface/evidence_surface.py) |
| `docs/examples/generated/README.md` | [docs/examples/generated/README.md](../../examples/generated/README.md) |
| `docs/examples/generated/ARTIFACT_INDEX.md` | [docs/examples/generated/ARTIFACT_INDEX.md](../../examples/generated/ARTIFACT_INDEX.md) |
| `docs/examples/generated/EVIDENCE_MATRIX.md` | [docs/examples/generated/EVIDENCE_MATRIX.md](../../examples/generated/EVIDENCE_MATRIX.md) |
| `docs/evidence/EVIDENCE-030-evidence-surface-layer.md` | [docs/evidence/EVIDENCE-030-evidence-surface-layer.md](../../evidence/EVIDENCE-030-evidence-surface-layer.md) |
| `docs/evidence/evidence-index.md` | [docs/evidence/evidence-index.md](../../evidence/evidence-index.md) |
| `docs/evidence/evidence-map.md` | [docs/evidence/evidence-map.md](../../evidence/evidence-map.md) |
| `docs/evidence/claim-to-evidence-matrix.md` | [docs/evidence/claim-to-evidence-matrix.md](../../evidence/claim-to-evidence-matrix.md) |
| `tests/test_evidence_surface.py` | [tests/test_evidence_surface.py](../../../tests/test_evidence_surface.py) |
| `tests/test_evidence_navigation.py` | [tests/test_evidence_navigation.py](../../../tests/test_evidence_navigation.py) |

## Validation Commands

```bash
python3 scripts/generate_evidence_surface.py
```

```bash
python3 scripts/permea_evidence.py
```

```bash
python3 scripts/validate_permea_artifacts.py
```

```bash
python3 -m pytest tests/test_evidence_surface.py tests/test_evidence_navigation.py
```


## Raw Readability Notes

- The evidence surface packet points to generated navigation Markdown and evidence-layer docs.
- This markdown packet is intentionally written as physical newline-separated text.
- This JSON packet is intentionally written with indent=2, sort_keys=True, and a trailing newline.
- Use commit-SHA raw URLs for external review when branch raw views may be stale or transformed.

## Claim Boundary Notes

- This packet reviews navigation, artifact-family links, and validation surfaces only.
- It does not download datasets, execute acquisition, call external services, run ML, or score candidates.
- It does not create scientific evidence, benchmark results, or biological validation.
- It does not claim wet-lab validation, clinical efficacy, model performance, or solved delivery.
- A passing packet means the listed evidence surface is easier to inspect; it does not prove biological outcomes.

## Reviewer Checklist

- [ ] Open the generated evidence surface and confirm it links current public artifact families and review commands.
- [ ] Run the listed generation, evidence summary, validation, and focused test commands from the repository root.
- [ ] Confirm the evidence record, evidence index, evidence map, and matrix remain aligned with the generated surface.
- [ ] Confirm limitations and non-claims remain explicit in the generated surface and evidence docs.
- [ ] Record any missing artifact family, stale link, unclear boundary, or validation failure before approval.

## Limitations

- The packet covers generated evidence navigation, not source-data acquisition or external validation.
- The packet checks reviewability and local generation coverage, not scientific correctness.
- The generated evidence surface organizes current public artifacts and should not be treated as experimental evidence.

## Next Review Step

Regenerate this packet:

```bash
python3 scripts/permea_review_packet.py
```

Then inspect this packet together with the linked report, generated artifacts, and command output.
