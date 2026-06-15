from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.evaluation.bundle import (
    ARTIFACT_LINEAGE,
    NON_CLAIMS,
    PASS,
    REFERENCE_INPUT_FAMILIES,
    REQUIRED_PACKET_SECTIONS,
    collect_evaluation_bundle,
    render_evaluation_packet,
    validate_evaluation_bundle,
    write_evaluation_packet,
)
from permea_core.generation import artifacts as generation_artifacts
from permea_core.validation import artifacts as validation_artifacts


REQUIRED_JSON_KEYS = (
    "bundle_name",
    "status",
    "reference_inputs",
    "generated_surfaces",
    "artifact_lineage",
    "validation_handoff",
    "reproducibility_handoff",
    "non_claims",
    "limitations",
    "next_evidence_steps",
)

REQUIRED_REFERENCE_INPUT_FAMILIES = (
    "dataset_cards/",
    "benchmark_cards/",
    "evidence_cards/",
    "acquisition_manifests/",
    "run_manifests/",
    "output_packages/",
)

REQUIRED_GUIDE_SECTIONS = (
    "## Overview",
    "## Who this is for",
    "## Evaluation contract",
    "## Reference input families",
    "## One-command evaluation packet generation",
    "## Generated outputs",
    "## How to inspect the evaluation packet",
    "## How to adapt the pattern for new dataset cards",
    "## How to adapt the pattern for new benchmark cards",
    "## How to adapt the pattern for new evidence cards",
    "## Validation and reproducibility commands",
    "## Explicit Non-Claims",
    "## Limitations",
    "## Next Evidence Steps",
)

UNSUPPORTED_POSITIVE_CLAIM_PARTS = (
    ("data has already been", "downloaded"),
    ("acquisition has been", "executed"),
    ("redistribution rights have been", "confirmed"),
    ("model performance has been", "measured"),
    ("wet-lab", "validated"),
    ("clinical", "efficacy shown"),
    ("delivery", "solved"),
    ("AlphaFold-level", "maturity"),
)


def test_evaluation_bundle_generation_returns_pass() -> None:
    bundle = collect_evaluation_bundle(ROOT)

    assert bundle["status"] == PASS
    assert bundle["bundle_name"] == "permea_core_public_evaluation_bundle"


def test_evaluation_packet_markdown_includes_required_sections() -> None:
    rendered = render_evaluation_packet(collect_evaluation_bundle(ROOT))

    for section in REQUIRED_PACKET_SECTIONS:
        assert section in rendered


def test_evaluation_guide_includes_required_sections() -> None:
    guide = (ROOT / "EVALUATION.md").read_text(encoding="utf-8")

    for section in REQUIRED_GUIDE_SECTIONS:
        assert section in guide


def test_evaluation_packet_json_includes_required_keys(tmp_path: Path) -> None:
    result = write_evaluation_packet(tmp_path, ROOT)
    payload = json.loads((tmp_path / "EVALUATION_PACKET.json").read_text())

    for key in REQUIRED_JSON_KEYS:
        assert key in payload
    assert payload["status"] == PASS
    assert payload["output_paths"] == result["output_paths"]


def test_reference_input_families_are_present() -> None:
    bundle = collect_evaluation_bundle(ROOT)
    rendered = render_evaluation_packet(bundle)

    assert [path for _label, path, _description in REFERENCE_INPUT_FAMILIES] == list(
        REQUIRED_REFERENCE_INPUT_FAMILIES
    )
    for path in REQUIRED_REFERENCE_INPUT_FAMILIES:
        assert path in rendered


def test_artifact_lineage_matches_required_order() -> None:
    bundle = collect_evaluation_bundle(ROOT)

    assert [item["path"] for item in bundle["artifact_lineage"]] == [
        path for _label, path in ARTIFACT_LINEAGE
    ]


def test_evaluation_packet_includes_explicit_non_claims() -> None:
    rendered = render_evaluation_packet(collect_evaluation_bundle(ROOT))

    for claim in NON_CLAIMS:
        assert f"- {claim}" in rendered


def test_paths_are_relative_public_safe(tmp_path: Path) -> None:
    result = write_evaluation_packet(tmp_path, ROOT)
    rendered = render_evaluation_packet(result)

    assert str(ROOT) not in rendered
    for key in ("reference_inputs", "generated_surfaces", "artifact_lineage"):
        for item in result[key]:
            assert not item["path"].startswith("/")


def test_evaluation_bundle_validation_passes() -> None:
    write_evaluation_packet(root_path=ROOT)
    result = validate_evaluation_bundle(ROOT)

    assert result["status"] == PASS
    assert all(check["status"] == PASS for check in result["checks"])


def test_evaluate_cli_exits_zero() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "permea_evaluate.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS evaluation packet generation" in completed.stdout


def test_unified_generation_and_validation_include_evaluation_bundle() -> None:
    generation_names = [name for name, _command in generation_artifacts.GENERATION_STEPS]
    validation_names = [name for name, _command in validation_artifacts.VALIDATION_STEPS]

    assert "evaluation packet generation" in generation_names
    assert "evaluation packet generation" in validation_names
    assert "evaluation bundle validation" in validation_names


def test_unsupported_positive_claim_phrases_are_absent() -> None:
    bundle = collect_evaluation_bundle(ROOT)
    combined = f"{render_evaluation_packet(bundle)}\n{json.dumps(bundle, sort_keys=True)}"

    for parts in UNSUPPORTED_POSITIVE_CLAIM_PARTS:
        assert " ".join(parts) not in combined
