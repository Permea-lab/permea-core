# P-CORE-034 Evaluation Bundle Review Packet

This packet makes one public Permea artifact system reviewable from GitHub.
It is intended for human review and structured assisted review.

It should be read together with the linked source files, tests, report, and validation command output.

## Packet Metadata

| Field | Value |
| --- | --- |
| Packet ID | `p-core-034-evaluation-bundle` |
| Artifact path | [docs/examples/generated/EVALUATION_PACKET.md](../../examples/generated/EVALUATION_PACKET.md) |
| Artifact type | public evaluation template and reference packet surface |

## Purpose

Help a reviewer inspect the evaluation bundle through its generated packet, template inputs, source module, validation handoff, reproducibility handoff, evidence record, tests, boundaries, and limitations.

## Related Evidence And Report Links

| Review surface | Link |
| --- | --- |
| `scripts/permea_evaluate.py` | [scripts/permea_evaluate.py](../../../scripts/permea_evaluate.py) |
| `scripts/permea_reproduce.py` | [scripts/permea_reproduce.py](../../../scripts/permea_reproduce.py) |
| `scripts/permea_validate.py` | [scripts/permea_validate.py](../../../scripts/permea_validate.py) |
| `src/permea_core/evaluation/bundle.py` | [src/permea_core/evaluation/bundle.py](../../../src/permea_core/evaluation/bundle.py) |
| `docs/examples/generated/EVALUATION_PACKET.md` | [docs/examples/generated/EVALUATION_PACKET.md](../../examples/generated/EVALUATION_PACKET.md) |
| `docs/examples/generated/EVALUATION_PACKET.json` | [docs/examples/generated/EVALUATION_PACKET.json](../../examples/generated/EVALUATION_PACKET.json) |
| `docs/evidence/EVIDENCE-034-evaluation-bundle.md` | [docs/evidence/EVIDENCE-034-evaluation-bundle.md](../../evidence/EVIDENCE-034-evaluation-bundle.md) |
| `EVALUATION.md` | [EVALUATION.md](../../../EVALUATION.md) |
| `tests/test_evaluation_bundle.py` | [tests/test_evaluation_bundle.py](../../../tests/test_evaluation_bundle.py) |

## Validation Commands

```bash
python3 scripts/permea_evaluate.py
```

```bash
python3 scripts/permea_reproduce.py --report-only
```

```bash
python3 scripts/permea_validate.py
```

```bash
python3 -m pytest tests/test_evaluation_bundle.py
```


## Raw Readability Notes

- The evaluation packet points to generated Markdown and JSON packet outputs.
- This markdown packet is intentionally written as physical newline-separated text.
- This JSON packet is intentionally written with indent=2, sort_keys=True, and a trailing newline.
- Use commit-SHA raw URLs for external review when branch raw views may be stale or transformed.

## Claim Boundary Notes

- This packet reviews a template/reference evaluation workflow only.
- It does not load datasets, execute acquisition, call external services, run ML, or score candidates.
- It does not create scientific evidence, benchmark results, or biological validation.
- It does not claim wet-lab validation, clinical efficacy, model performance, or solved delivery.
- A passing packet means the listed evaluation surface is easier to inspect; it does not prove biological outcomes.

## Reviewer Checklist

- [ ] Open the evaluation packet Markdown and JSON outputs and confirm the input-family links are public and existing.
- [ ] Run the listed evaluation, reproduction, validation, and focused test commands from the repository root.
- [ ] Confirm validation and reproducibility handoffs are visible in the generated evaluation packet.
- [ ] Confirm limitations and non-claims remain explicit in the packet and evidence record.
- [ ] Record any missing input family, stale command, unclear boundary, or validation failure before approval.

## Limitations

- The packet covers a reusable template/reference workflow, not a completed external evaluation result.
- The packet checks reviewability and local generation coverage, not scientific correctness.
- The evaluation bundle does not establish access rights, redistribution status, biological performance, or clinical utility.

## Next Review Step

Regenerate this packet:

```bash
python3 scripts/permea_review_packet.py
```

Then inspect this packet together with the linked report, generated artifacts, and command output.
