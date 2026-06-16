# DEC-004: Specification Layer for Permea Standard

## Context

Permea Core needs public artifact standards that are independent of a single generated example. External researchers and developers need to inspect, implement, validate, and extend the artifact families.

## Decision

Permea Core will maintain a public specification layer for dataset cards, benchmark cards, evidence cards, run manifests, and output packages.

## Rationale

Specifications make the Permea standard inspectable and reusable. They reduce ambiguity about required fields, recommended fields, validation expectations, limitations, and extension points.

## Alternatives Considered

- Keep artifact expectations only in generator code.
- Define standards only through examples.
- Delay specifications until after more artifact families exist.

These alternatives were rejected because they make external adoption and review harder.

## Consequences

- Artifact families should remain aligned with public specs and schemas.
- Future validators should use the specification layer as their source of structure.
- Specs should stay general enough for external extension.

## Related Reports

- [P-CORE-036 artifact specification layer](../reports/p-core-036-artifact-specification-layer.md)

## Related Evidence

- [Public artifact specifications](../specs/README.md)
- [Artifact schemas](../../schemas/)
- [Specification registry command](../../scripts/permea_specs.py)

## Claim Boundary

The specification layer defines structure and expectations. It does not prove source access, redistribution rights, biological behavior, clinical effectiveness, or model performance.
