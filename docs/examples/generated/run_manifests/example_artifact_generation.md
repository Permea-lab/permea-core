# Run Manifest: example_artifact_generation

> Generated from Permea run-manifest metadata. This public-safe example records metadata only: no dataset downloaded, no acquisition executed, no redistribution rights confirmed, no wet-lab validation by Permea, and no model performance claim.

## Run ID

example_artifact_generation

## Run Type

artifact-generation-example

## Generated At

example-generated

## Artifact Status

example-metadata-artifact

## Benchmark IDs

- bbb_b3pred_dataset3
- cpp_cppsite2_placeholder

## Dataset IDs

- b3pred_dataset3
- cppsite2_placeholder

## Source IDs

- b3pred_dataset3
- cppsite2

## Acquisition Manifest IDs

- b3pred_dataset3_acquisition_plan
- cppsite2_placeholder_acquisition_plan

## Commands

- python3 scripts/generate_permea_artifacts.py
- python3 scripts/validate_permea_artifacts.py

## Generated Artifacts

- docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md
- docs/examples/generated/benchmark_cards/cpp_cppsite2_placeholder.md
- docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml
- docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json
- docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv
- docs/examples/generated/output_packages/bbb_b3pred_dataset3/benchmark_card.md
- docs/examples/generated/output_packages/bbb_b3pred_dataset3/evidence_cards.json
- docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json
- docs/examples/generated/evidence_cards/cpp_cppsite2_placeholder.evidence_cards.json
- docs/examples/generated/dataset_cards/b3pred_dataset3.md
- docs/examples/generated/dataset_cards/cppsite2_placeholder.md
- docs/examples/generated/acquisition_manifests/b3pred_dataset3.md
- docs/examples/generated/acquisition_manifests/cppsite2_placeholder.md

## Validation Steps

- python3 scripts/validate_run_manifests.py
- python3 scripts/validate_permea_artifacts.py
- python3 -m pytest tests/test_run_manifests.py

## Provenance Summary

Example metadata record for deterministic local artifact generation and validation. It records commands and artifact paths only.

## Explicit Non-Claims

- no dataset downloaded
- no acquisition executed
- no redistribution rights confirmed
- no wet-lab validation by Permea
- no model performance claim

## Claim Boundary

Metadata-only run manifest for deterministic artifact examples; no dataset acquisition, no model execution, no wet-lab validation by Permea, and no model performance claim.

## Limitations

- Example metadata only.
- Commands record local artifact generation and validation surfaces.
- Artifact paths point to public-safe generated examples.

## Next Action

Review run manifest metadata before any real benchmark execution record.
