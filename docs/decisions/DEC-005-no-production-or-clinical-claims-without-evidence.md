# DEC-005: No Production or Clinical Claims Without Evidence

## Context

Permea Core works near scientific and biomedical domains where wording can easily imply stronger evidence than the repository currently supports.

## Decision

Permea Core will not make production, clinical, broad delivery, wet-lab, model-performance, or best-performance claims without specific supporting evidence and review.

## Rationale

Clear claim boundaries protect reviewers, contributors, collaborators, and future papers. They make the repository easier to trust because limitations are visible and durable.

## Alternatives Considered

- Use aspirational language as if it were current capability.
- Treat computational artifacts as biological validation.
- Treat generated examples as measured model performance.

These alternatives were rejected because they would weaken scientific discipline and public trust.

## Consequences

- Public docs should keep non-claims visible.
- Future stronger claims must identify evidence, artifacts, review status, and limitations.
- Report, README, and paper language should remain aligned.

## Related Reports

- [P-DOC-001 project operating-system adoption v0](../reports/p-doc-001-project-operating-system-adoption-v0.md)

## Related Evidence

- [Claim Boundary](../CLAIM_BOUNDARY.md)
- [Claim Registry](../scientific-governance/CLAIM_REGISTRY.md)
- [Paper Alignment Policy](../paper-alignment/PAPER_ALIGNMENT_POLICY.md)

## Claim Boundary

Current public non-claims remain: no dataset downloaded, no acquisition executed, no redistribution rights confirmed, no wet-lab validation by Permea, no clinical-effectiveness claim, no model performance claim, no state-of-the-art claim, and no solved-delivery claim.
