# DEC-002: Evidence Bundle Before Claims

## Context

Permea Core contains public artifacts, generated surfaces, registries, and reports. Without an evidence-first rule, public language could move faster than the artifacts that support it.

## Decision

Permea Core will package evidence surfaces before expanding claims. Claims should point to generated artifacts, validation commands, reports, or explicit non-claims.

## Rationale

Evidence-first work makes review easier and reduces repeated debate about whether a claim is supported. It keeps public wording tied to concrete repository artifacts.

## Alternatives Considered

- Let the README or narrative docs lead claims and backfill evidence later.
- Use roadmap intent as evidence of completed capability.
- Treat generated examples as proof of scientific performance.

These alternatives were rejected because they can overstate the repository's current evidence posture.

## Consequences

- Public claims should identify their support surface.
- New evidence surfaces should include limitations and non-claims.
- Unsupported claims should be narrowed or removed.

## Related Reports

- [P-DOC-001 project operating-system adoption v0](../reports/p-doc-001-project-operating-system-adoption-v0.md)
- [P-CORE-036 artifact specification layer](../reports/p-core-036-artifact-specification-layer.md)

## Related Evidence

- [Evidence matrix](../examples/generated/EVIDENCE_MATRIX.md)
- [Demo packet](../examples/generated/DEMO_PACKET.md)
- [Artifact index](../examples/generated/ARTIFACT_INDEX.md)

## Claim Boundary

This decision supports evidence-backed public language. It does not convert generated metadata, dry-run reports, or example artifacts into biological, clinical, or model-performance claims.
