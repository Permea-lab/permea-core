# P-CORE-047 Public Review Packet Layer Review Packet

This packet makes one public Permea artifact system reviewable from GitHub.
It is intended for human review and structured assisted review.

It should be read together with the linked source files, tests, report, and validation command output.

## Packet Metadata

| Field | Value |
| --- | --- |
| Packet ID | `p-core-047-public-review-packet-layer` |
| Artifact path | [docs/review/public-review-packet.md](../public-review-packet.md) |
| Artifact type | guided public review packet operating layer |

## Purpose

Help a reviewer inspect the public review packet layer through its guided packet, review command, template, assembly guide, governance, checklist, schema, report, tests, claim boundaries, and limitations.

## Related Evidence And Report Links

| Review surface | Link |
| --- | --- |
| `scripts/permea_review.py` | [scripts/permea_review.py](../../../scripts/permea_review.py) |
| `docs/review/public-review-packet.md` | [docs/review/public-review-packet.md](../public-review-packet.md) |
| `docs/review/public-review-packet-template.md` | [docs/review/public-review-packet-template.md](../public-review-packet-template.md) |
| `docs/review/public-review-packet-assembly.md` | [docs/review/public-review-packet-assembly.md](../public-review-packet-assembly.md) |
| `docs/review/public-review-packet-governance.md` | [docs/review/public-review-packet-governance.md](../public-review-packet-governance.md) |
| `docs/review/public-review-checklist.md` | [docs/review/public-review-checklist.md](../public-review-checklist.md) |
| `schemas/public-review-packet.schema.json` | [schemas/public-review-packet.schema.json](../../../schemas/public-review-packet.schema.json) |
| `docs/reports/p-core-047-public-review-packet-layer-v0.md` | [docs/reports/p-core-047-public-review-packet-layer-v0.md](../../reports/p-core-047-public-review-packet-layer-v0.md) |
| `tests/test_public_review_packet_layer.py` | [tests/test_public_review_packet_layer.py](../../../tests/test_public_review_packet_layer.py) |
| `README.md` | [README.md](../../../README.md) |
| `OPEN_THIS_FIRST.md` | [OPEN_THIS_FIRST.md](../../../OPEN_THIS_FIRST.md) |
| `REVIEW_HUB.md` | [REVIEW_HUB.md](../../../REVIEW_HUB.md) |

## Validation Commands

```bash
python3 scripts/permea_review.py
```

```bash
python3 scripts/permea_review_packet.py
```

```bash
python3 scripts/validate_permea_artifacts.py
```

```bash
python3 -m pytest tests/test_public_review_packet_layer.py tests/test_evidence_review_packet_system.py
```


## Raw Readability Notes

- The public review packet layer packet points to the committed guide, template, assembly, governance, checklist, and schema files.
- This markdown packet is intentionally written as physical newline-separated text.
- This JSON packet is intentionally written with indent=2, sort_keys=True, and a trailing newline.
- Use commit-SHA raw URLs for external review when branch raw views may be stale or transformed.

## Claim Boundary Notes

- This packet reviews public orientation, reviewer workflow, and validation guidance only.
- It does not create scientific evidence, benchmark results, or biological validation.
- It does not claim wet-lab validation, clinical efficacy, model performance, or solved delivery.
- A passing packet means the listed public review layer is easier to inspect; it does not prove biological outcomes.

## Reviewer Checklist

- [ ] Open the public review packet, template, assembly guide, governance document, checklist, schema, and report.
- [ ] Run the public review command and listed validation commands from the repository root.
- [ ] Confirm the guided reading path, registry commands, validation commands, unsupported claims, and limitations are explicit.
- [ ] Confirm the packet can be reviewed without hidden chat context.
- [ ] Record any missing guide, stale command, unclear boundary, or validation failure before approval.

## Limitations

- The packet covers review workflow and public orientation, not scientific correctness.
- The public review packet layer organizes current public infrastructure and does not establish external validation.
- The packet is curated for the existing P-CORE-047 layer and should be refreshed when that layer changes materially.

## Next Review Step

Regenerate this packet:

```bash
python3 scripts/permea_review_packet.py
```

Then inspect this packet together with the linked report, generated artifacts, and command output.
