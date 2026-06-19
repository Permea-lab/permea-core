# Evidence Review Packet System

The evidence review packet system turns selected public Permea artifact systems into reviewer-friendly packets.

Each packet gives a reviewer one place to inspect:

- artifact path
- artifact type
- purpose
- related evidence and report links
- validation commands
- claim boundary notes
- reviewer checklist
- limitations

Review packets support reproducibility and human review by connecting concrete files, generated outputs, tests, commands, summaries, and known limitations. They are designed to prevent treating file creation alone as approval.

## How To Run

```bash
python3 scripts/permea_review_packet.py
```

Generated packets are written under [packets](packets/README.md).

## Post-Push Raw URL Verification

Before merging a review-packet PR, verify the committed GitHub raw files, not only local generated files:

```bash
python3 scripts/verify_review_packet_raw_urls.py
```

This command uses `curl` against `raw.githubusercontent.com` and reports HTTP status, byte count, physical line count, trailing-newline status, literal `\n` sequence count, the first 20 raw lines, and the remote branch HEAD.

Use this check when reviewer feedback depends on raw GitHub readability.

## Current Packets

- [P-CORE-030 Evidence Surface Layer Review Packet](packets/p-core-030-evidence-surface-layer.md)
- [P-CORE-032 Reproducibility Bundle Review Packet](packets/p-core-032-reproducibility-bundle.md)
- [P-CORE-034 Evaluation Bundle Review Packet](packets/p-core-034-evaluation-bundle.md)
- [P-CORE-047 Public Review Packet Layer Review Packet](packets/p-core-047-public-review-packet-layer.md)
- [P-CORE-053 Artifact Consistency System Review Packet](packets/p-core-053-artifact-consistency-system.md)

## Future Use

Future public artifact systems should add a review packet when they become reviewer-facing. A useful packet should list the files to inspect, commands to run, claim boundaries to check, and limitations that remain after validation passes.

## What It Does Not Prove

The evidence review packet system does not create scientific evidence, benchmark results, wet-lab validation, clinical efficacy evidence, model performance evidence, or solved-delivery evidence.

It only improves reviewability of public artifact systems.
