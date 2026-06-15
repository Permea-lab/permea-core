# Output Package Specification

## Overview

An output package is a public bundle of reviewer-facing benchmark or artifact outputs.

## Purpose

Output packages group manifests, metrics-like metadata, rankings when present, benchmark-card summaries, evidence-card references, limitations, and claim boundaries.

## Required fields

- `package_id`
- `manifest_path`
- `metrics_path`
- `benchmark_card_path`
- `limitations`
- `claim_boundary`

## Recommended fields

- `ranking_path`
- `evidence_card_paths`
- `run_manifest_path`
- `review_status`
- `generation_command`

## Field definitions

- `package_id`: stable identifier for the output package.
- `manifest_path`: relative path to package manifest metadata.
- `metrics_path`: relative path to aggregate metrics or metrics-like metadata.
- `benchmark_card_path`: relative path to benchmark-card summary.
- `limitations`: output, task, metric, release, or review limits.
- `claim_boundary`: explicit statement of what the package can support.

## Example structure

```yaml
package_id: example_output_package
manifest_path: docs/examples/generated/output_packages/example/manifest.yaml
metrics_path: docs/examples/generated/output_packages/example/metrics.json
benchmark_card_path: docs/examples/generated/output_packages/example/benchmark_card.md
limitations:
  - example_metadata_only
claim_boundary: Reviewer-facing output package only; no biological-performance claim.
```

## Validation expectations

Validation should confirm required fields, relative paths, expected package files, limitations, and claim boundaries. Validation should not infer performance quality from package presence.

## Claim boundaries

Output packages support review, comparison, and reproducibility packaging. They do not establish biological performance, therapeutic effect, model quality, or best-performance status.

## Limitations

Output packages depend on benchmark-card quality, run-manifest quality, metric definitions, and release posture.

## Extension points

External contributors may add visual summaries, evidence-card links, run-manifest links, reviewer notes, and generation commands while preserving the required fields.

