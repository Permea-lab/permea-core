# DEC-003: Evaluation Bundle as User Transfer Layer

## Context

Researchers and developers need a way to understand how Permea artifact families fit together without copying an internal workflow or assuming a completed scientific result.

## Decision

Permea Core will use the evaluation bundle as a user transfer layer: a template/reference packet that shows how input families, generated surfaces, validation path, reproducibility path, limitations, and non-claims connect.

## Rationale

The evaluation bundle makes the artifact pattern easier to adapt. It helps external users understand how dataset cards, benchmark cards, evidence cards, manifests, and output packages relate without implying that Permea has run acquisition or measured performance.

## Alternatives Considered

- Provide only individual artifact specs.
- Provide only generated examples without a reviewer-facing packet.
- Present the evaluation packet as a completed scientific evaluation.

These alternatives were rejected because they either make transfer harder or risk overstating what the bundle proves.

## Consequences

- Evaluation docs should remain clear that the bundle is a template/reference workflow.
- New user-facing artifact patterns should link back to validation and reproducibility paths.
- The evaluation bundle should not become a performance or validation claim.

## Related Reports

- [P-DOC-001 project operating-system adoption v0](../reports/p-doc-001-project-operating-system-adoption-v0.md)

## Related Evidence

- [Evaluation packet](../examples/generated/EVALUATION_PACKET.md)
- [Generated evidence surface](../examples/generated/README.md)
- [Reproducibility report](../examples/generated/REPRODUCIBILITY_REPORT.md)

## Claim Boundary

The evaluation bundle transfers an artifact pattern. It does not prove dataset availability, acquisition completion, biological transport, clinical effectiveness, model performance, or generalization.
