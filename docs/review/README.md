# Public Review Packet Layer

The public review packet layer is the guided entry point for reviewing Permea Core without repository archaeology.

It answers what to read first, what to run first, what evidence exists, what benchmark, dataset, and research-package infrastructure exists, what claims are supported, what claims are not supported, and what remains proposed, computational-only, or requiring future validation.

## Review Path

Start with the deterministic CLI:

```bash
python3 scripts/permea_review.py
```

Then follow the packet:

- [Public review packet](public-review-packet.md)
- [Review loop operating standard](review-loop-operating-standard.md)
- [Review bundle examples](examples/README.md)
- [Evidence review packet system](review-packet-system.md)
- [Generated review packets](packets/README.md)
- [P-CORE-030 Evidence Surface Layer Review Packet](packets/p-core-030-evidence-surface-layer.md)
- [P-CORE-032 Reproducibility Bundle Review Packet](packets/p-core-032-reproducibility-bundle.md)
- [P-CORE-034 Evaluation Bundle Review Packet](packets/p-core-034-evaluation-bundle.md)
- [P-CORE-047 Public Review Packet Layer Review Packet](packets/p-core-047-public-review-packet-layer.md)
- [P-CORE-053 Artifact Consistency System Review Packet](packets/p-core-053-artifact-consistency-system.md)
- [Public review packet template](public-review-packet-template.md)
- [Public review packet assembly](public-review-packet-assembly.md)
- [Public review packet governance](public-review-packet-governance.md)
- [Public review checklist](public-review-checklist.md)
- [Public review packet schema](../../schemas/public-review-packet.schema.json)

## Status

Public Review Packet Ready

This layer does not create new scientific evidence, write a paper, submit a paper, publish a paper, or claim biological outcomes.

The evidence review packet system adds concrete reviewer packets for selected public artifact systems. Generate them with:

```bash
python3 scripts/permea_review_packet.py
```

Review bundle completeness can be checked with:

```bash
python3 scripts/check_review_bundle_completeness.py
python3 scripts/check_review_bundle_completeness.py docs/review/examples/final-review-bundle-complete-example.md
```

## Claim Boundaries

Public review packets organize current computational evidence, validation commands, reproducibility surfaces, and explicit claim boundaries. They do not establish biological effect, experimental validation, therapeutic outcome, clinical evidence, expression improvement, or solved delivery.

Explicit non-claims:

- no new scientific result claim from this layer
- no paper claim from this layer
- no wet-lab validation by Permea
- no biological efficacy claim
- no therapeutic outcome claim
- no BBB success claim
- no solved-delivery claim
- no SOTA performance claim
- no experimental validation claim
- no clinical evidence claim
- no expression improvement claim
