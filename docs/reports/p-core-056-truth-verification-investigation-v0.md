# P-CORE-056 Truth Verification Investigation v0

## Purpose

This report records a direct GitHub truth verification investigation for PR #68, the P-CORE-054 Evidence Review Packet System.

The investigation compares generated review packet files through both mutable branch raw URLs and immutable commit-SHA raw URLs. It exists to avoid relying only on local generated files when reviewer feedback depends on what GitHub raw views actually serve.

PR #68 was not merged during this investigation.

## Identity And PR State

| Check | Result |
| --- | --- |
| GitHub login | `Permea-lab-admin` |
| Git author | `Albert Kim <a.kim@permea.us>` |
| PR | `https://github.com/Permea-lab/permea-core/pull/68` |
| PR state | `OPEN` |
| PR branch | `p-core-054-evidence-review-packet-system` |
| PR base | `main` |

## SHA Evidence

| SHA type | Value |
| --- | --- |
| PR head SHA | `3aacbc1f829ae2b4ce627fa56b8370fce0f246e7` |
| Latest commit SHA | `3aacbc1f829ae2b4ce627fa56b8370fce0f246e7` |
| Local branch HEAD SHA | `3aacbc1f829ae2b4ce627fa56b8370fce0f246e7` |
| Remote branch SHA | `3aacbc1f829ae2b4ce627fa56b8370fce0f246e7` |
| Local and remote match | yes |

## Raw URL Evidence

### Branch Raw URLs

| File | URL | HTTP | Bytes | Lines | Ends with newline | Literal `\n` count |
| --- | --- | --- | ---: | ---: | --- | ---: |
| Markdown packet | `https://raw.githubusercontent.com/Permea-lab/permea-core/p-core-054-evidence-review-packet-system/docs/review/packets/p-core-053-artifact-consistency-system.md` | 200 | 3384 | 81 | true | 0 |
| JSON packet | `https://raw.githubusercontent.com/Permea-lab/permea-core/p-core-054-evidence-review-packet-system/docs/review/packets/p-core-053-artifact-consistency-system.json` | 200 | 2249 | 41 | true | 0 |

### Commit-SHA Raw URLs

| File | URL | HTTP | Bytes | Lines | Ends with newline | Literal `\n` count |
| --- | --- | --- | ---: | ---: | --- | ---: |
| Markdown packet | `https://raw.githubusercontent.com/Permea-lab/permea-core/3aacbc1f829ae2b4ce627fa56b8370fce0f246e7/docs/review/packets/p-core-053-artifact-consistency-system.md` | 200 | 3384 | 81 | true | 0 |
| JSON packet | `https://raw.githubusercontent.com/Permea-lab/permea-core/3aacbc1f829ae2b4ce627fa56b8370fce0f246e7/docs/review/packets/p-core-053-artifact-consistency-system.json` | 200 | 2249 | 41 | true | 0 |

## First 10 Raw Lines

### Markdown Packet

```text
# P-CORE-053 Artifact Consistency System Review Packet

This packet makes one public Permea artifact system reviewable from GitHub.
It is intended for human review and structured assisted review.

It should be read together with the linked source files, tests, report, and validation command output.

## Packet Metadata

| Field | Value |
```

### JSON Packet

```json
{
  "artifact_path": "docs/artifacts/README.md",
  "artifact_type": "artifact consistency reviewability layer",
  "claim_boundary_notes": [
    "This packet reviews documentation and reproducibility surfaces only.",
    "It does not create scientific evidence, benchmark results, or biological validation.",
    "It does not claim wet-lab validation, clinical efficacy, model performance, or solved delivery.",
    "A passing packet means the listed artifact system is easier to inspect; it does not prove biological outcomes."
  ],
  "limitations": [
```

## Diagnosis

The branch raw URLs and commit-SHA raw URLs return the same byte counts, line counts, newline counts, first lines, and trailing-newline status.

The investigation found no evidence of:

- local-only generation
- unpushed commits
- wrong branch
- local/remote mismatch
- literal escaped newline sequences in the packet files
- renderer compression in the current PR head
- delayed branch propagation at the time of the curl checks

The most likely explanation for the disagreement is that the external review checked a stale, cached, transformed, or different snapshot than the current PR head. The immutable commit-SHA URLs are the recommended review targets because they remove branch-mutation ambiguity.

## Verification Process Update

P-CORE-055 added a committed raw URL verifier:

```bash
python3 scripts/verify_review_packet_raw_urls.py
```

That verifier uses `curl` against GitHub raw URLs and reports HTTP status, byte count, physical line count, trailing-newline status, literal `\n` sequence count, first 20 raw lines, and remote branch HEAD.

## Validation

Validation for this investigation should include:

```bash
git diff --check
python3 scripts/permea_review_packet.py
python3 scripts/permea_artifacts.py
python3 scripts/verify_review_packet_raw_urls.py
python3 -m pytest
```

## Recommendation

PR #68 is suitable for external re-review using the commit-SHA raw URLs listed above.

Do not rely on a copied, transformed, cached, or branch-stale rendering when judging raw readability. Use either direct `curl` output or the committed verifier command before merge.

This report does not create new scientific evidence, benchmark results, biological validation, clinical efficacy evidence, model performance evidence, or solved-delivery evidence.
