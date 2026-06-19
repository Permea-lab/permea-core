# P-CORE-032 Reproducibility Bundle Review Packet

This packet makes one public Permea artifact system reviewable from GitHub.
It is intended for human review and structured assisted review.

It should be read together with the linked source files, tests, report, and validation command output.

## Packet Metadata

| Field | Value |
| --- | --- |
| Packet ID | `p-core-032-reproducibility-bundle` |
| Artifact path | [docs/examples/generated/REPRODUCIBILITY_REPORT.md](../../examples/generated/REPRODUCIBILITY_REPORT.md) |
| Artifact type | public reproducibility report and local regeneration surface |

## Purpose

Help a reviewer inspect the reproducibility bundle through its public report, generator, validation commands, evidence record, tests, lineage, claim boundaries, and limitations.

## Related Evidence And Report Links

| Review surface | Link |
| --- | --- |
| `scripts/permea_reproduce.py` | [scripts/permea_reproduce.py](../../../scripts/permea_reproduce.py) |
| `scripts/permea_validate.py` | [scripts/permea_validate.py](../../../scripts/permea_validate.py) |
| `scripts/generate_permea_artifacts.py` | [scripts/generate_permea_artifacts.py](../../../scripts/generate_permea_artifacts.py) |
| `scripts/validate_permea_artifacts.py` | [scripts/validate_permea_artifacts.py](../../../scripts/validate_permea_artifacts.py) |
| `src/permea_core/reproducibility/bundle.py` | [src/permea_core/reproducibility/bundle.py](../../../src/permea_core/reproducibility/bundle.py) |
| `docs/examples/generated/REPRODUCIBILITY_REPORT.md` | [docs/examples/generated/REPRODUCIBILITY_REPORT.md](../../examples/generated/REPRODUCIBILITY_REPORT.md) |
| `docs/examples/generated/REPRODUCIBILITY_REPORT.json` | [docs/examples/generated/REPRODUCIBILITY_REPORT.json](../../examples/generated/REPRODUCIBILITY_REPORT.json) |
| `docs/evidence/EVIDENCE-032-reproducibility-bundle.md` | [docs/evidence/EVIDENCE-032-reproducibility-bundle.md](../../evidence/EVIDENCE-032-reproducibility-bundle.md) |
| `REPRODUCIBILITY.md` | [REPRODUCIBILITY.md](../../../REPRODUCIBILITY.md) |
| `tests/test_reproducibility_bundle.py` | [tests/test_reproducibility_bundle.py](../../../tests/test_reproducibility_bundle.py) |

## Validation Commands

```bash
python3 scripts/permea_reproduce.py
```

```bash
python3 scripts/permea_validate.py
```

```bash
python3 scripts/validate_permea_artifacts.py
```

```bash
python3 -m pytest tests/test_reproducibility_bundle.py
```


## Raw Readability Notes

- The reproducibility packet points to generated Markdown and JSON report outputs.
- This markdown packet is intentionally written as physical newline-separated text.
- This JSON packet is intentionally written with indent=2, sort_keys=True, and a trailing newline.
- Use commit-SHA raw URLs for external review when branch raw views may be stale or transformed.

## Claim Boundary Notes

- This packet reviews deterministic local reproduction and validation surfaces only.
- It does not download datasets, execute acquisition, call external services, run ML, or score candidates.
- It does not create scientific evidence, benchmark results, or biological validation.
- It does not claim wet-lab validation, clinical efficacy, model performance, or solved delivery.
- A passing packet means the listed reproducibility surface is easier to inspect; it does not prove biological outcomes.

## Reviewer Checklist

- [ ] Open the reproducibility report Markdown and JSON outputs and confirm they are generated from public repository files.
- [ ] Run the listed reproduction and validation commands from the repository root.
- [ ] Confirm generated artifact lineage points to existing public files and directories.
- [ ] Confirm limitations and non-claims remain explicit in the report and evidence record.
- [ ] Record any missing generated surface, stale command, unclear boundary, or validation failure before approval.

## Limitations

- The packet covers local deterministic metadata artifacts, not dataset acquisition or external service execution.
- The packet checks reviewability and reproducibility command coverage, not scientific correctness.
- Generated examples are infrastructure surfaces and should not be treated as experimental evidence.

## Next Review Step

Regenerate this packet:

```bash
python3 scripts/permea_review_packet.py
```

Then inspect this packet together with the linked report, generated artifacts, and command output.
