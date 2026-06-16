# ADR-001: Project Breadcrumb and Review Hub Standard

## Status

Accepted

## Context

Permea Core now contains multiple public documentation layers: repository README files, generated evidence surfaces, reproducibility and evaluation guides, artifact specifications, schemas, ADRs, and technical reports.

Reports explain completed work, but they are not enough as the main continuation surface. A reviewer or future contributor needs a short current-state entry point before deciding which report, generated artifact, policy, or command to inspect.

## Decision

Permea Core will maintain two root-level continuation documents:

- `OPEN_THIS_FIRST.md`: a short first-read breadcrumb for current state, public truth, primary evidence, and the recommended next task.
- `REVIEW_HUB.md`: a fuller review map covering evidence, reports, ADRs, risks, open questions, claim boundaries, and continuation instructions.

Every completed task or group must update both files unless the task explicitly exempts breadcrumb updates.

## Why The Breadcrumb Layer Exists

The breadcrumb layer prevents project state from being hidden in historical conversations, stale assumptions, or scattered reports. It gives the next reviewer a current starting point and a small set of commands to verify live state.

## Why Reports Alone Are Insufficient

Reports are scoped to individual tasks. They are useful evidence, but they do not always state what changed after later work, which branch is active, what the current public truth is, or what should happen next.

Without a current breadcrumb, a reviewer can read an accurate old report and still misunderstand present state.

## Why The Review Hub Exists

The review hub is the stable navigation map. It indexes primary evidence, reports, ADRs, risks, open questions, claim boundaries, and resume instructions in one place.

The hub should remain concise enough to scan, but complete enough that a reviewer can choose the right next document without reading the whole repository first.

## Consequences

- Task completion now includes a documentation refresh step.
- Documentation drift becomes easier to detect.
- New public evidence surfaces should be linked from the breadcrumb and hub.
- Reports remain useful as evidence, while the hub remains the current navigation surface.

## Future Requirement

Every completed task or group must refresh:

- `OPEN_THIS_FIRST.md`
- `REVIEW_HUB.md`

If a task intentionally skips these updates, the task instructions or final report should say why.
