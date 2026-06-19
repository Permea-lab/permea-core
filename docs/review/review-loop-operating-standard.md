# Review Loop Operating Standard

This standard defines the public review bundle expected when a low-intervention Permea Core maintenance loop reviews, merges, or opens a pull request.

It is a reviewability standard only. It does not create scientific evidence, benchmark results, biological validation, clinical evidence, model performance evidence, or solved-delivery evidence.

## Purpose

The loop should reduce repeated reviewer setup work while keeping every public change independently inspectable.

Each completed loop step should leave enough concrete material for a human reviewer or structured assisted review to inspect the actual repository files, commands, limitations, and claim boundaries without relying on hidden conversation context.

## Required Review Bundle

Each merge gate or newly opened pull request should report:

- pull request URL
- branch name
- head SHA before merge or current branch SHA for an open pull request
- merge method and final main SHA when a merge occurs
- changed files
- validation commands and results
- local human-review paths as absolute filesystem paths
- remote GitHub review URLs
- scope audit result
- boundary audit result
- claim-discipline audit result
- whether a review packet was created, updated, or not needed
- exact stop reason when the loop stops

## Merge Gate Standard

Before merging a reviewed pull request, the loop must verify:

- expected GitHub identity
- expected git author
- clean target repository state
- clean adjacent reference repositories
- pull request state is open
- merge state is clean
- base branch is `main`
- head SHA is recorded before merge
- changed files match the approved scope
- validation commands pass
- public wording remains inside claim boundaries

If those checks pass, the pull request may be squash-merged when the task explicitly allows merge.

If any check fails, the loop should stop with a concrete blocker and leave the pull request unmerged.

## New Pull Request Standard

When the loop opens a follow-on pull request, the task should be:

- small enough to review as one unit
- independent from the merge gate just completed
- limited to existing public Permea Core surfaces
- documented with local and remote review paths
- validated before push
- left open unless the task explicitly authorizes merge

The pull request description should make review possible from repository files and URLs, not from hidden chat state.

## Local Completeness Check

Use the deterministic completeness checker before sending a final review bundle for review:

```bash
python3 scripts/check_review_bundle_completeness.py
python3 scripts/check_review_bundle_completeness.py --json
```

The checker verifies field presence only. It does not approve content, factual correctness, or merge readiness.

## Boundaries

The loop must not introduce:

- non-public doctrine or infrastructure details
- unrelated feature work
- broad orchestration frameworks
- new scientific claims
- biological-result claims
- wet-lab or in-vivo validation claims
- clinical claims
- model-performance claims
- benchmark-result claims
- solved-delivery claims

## Limitations

- This standard describes review handoff behavior, not scientific correctness.
- Passing validation means the reviewed public surfaces are easier to inspect; it does not prove biological outcomes.
- Human judgment is still required for final approval of non-trivial content, scope boundaries, and claim discipline.
