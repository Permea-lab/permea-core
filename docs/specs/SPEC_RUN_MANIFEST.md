# Run Manifest Specification

## Overview

A run manifest is a public provenance record for a deterministic artifact-generation or benchmark-style run.

## Purpose

Run manifests record what command was run, which inputs were referenced, which artifacts were produced, and which boundaries apply.

## Required fields

- `run_id`
- `run_type`
- `repository_commit`
- `command`
- `inputs`
- `artifact_paths`
- `limitations`
- `claim_boundary`

## Recommended fields

- `generated_at`
- `environment_summary`
- `configuration_ref`
- `validation_commands`
- `review_status`

## Field definitions

- `run_id`: stable identifier for the run.
- `run_type`: artifact generation, dry-run, evaluation packet, benchmark run, or another bounded type.
- `repository_commit`: public repository revision used for the run.
- `command`: command used to reproduce the run.
- `inputs`: relative paths or public references used as inputs.
- `artifact_paths`: relative paths to generated outputs.
- `limitations`: run, input, environment, or interpretation limits.
- `claim_boundary`: explicit statement of what the run manifest can support.

## Example structure

```yaml
run_id: example_run_manifest
run_type: artifact_generation
repository_commit: 0000000000000000000000000000000000000000
command: python3 scripts/generate_permea_artifacts.py
inputs:
  - dataset_cards/example.yaml
artifact_paths:
  - docs/examples/generated/README.md
limitations:
  - metadata_only_run
claim_boundary: Reproducibility record only; no biological-performance claim.
```

## Validation expectations

Validation should confirm required fields, relative paths, command presence, artifact references, limitations, and claim boundaries. Validation should not execute external services or expose private host details.

## Claim boundaries

Run manifests support provenance, reproducibility, and audit. They do not prove biological behavior, therapeutic effect, model quality, or data access rights.

## Limitations

A run manifest records the public run context but cannot replace dataset review, source review, model evaluation, or external validation.

## Extension points

External contributors may add environment references, configuration identifiers, validation commands, and review status while preserving the required fields.

