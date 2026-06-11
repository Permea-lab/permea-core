from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.benchmarks.evidence_cards import (
    generate_evidence_card,
    generate_evidence_cards,
    generate_evidence_cards_file,
)


REQUIRED_KEYS = (
    "evidence_card_id",
    "artifact_status",
    "benchmark_id",
    "task_name",
    "evidence_type",
    "source_reference",
    "provenance_status",
    "claim_boundary",
    "limitations",
    "generated_at",
    "non_claims",
)

UNSUPPORTED_CLAIM_PHRASES = (
    "wet-lab " + "validated",
    "clinical " + "efficacy",
    "universal " + "predictor",
    "solved " + "delivery",
    "state-of-the-art",
)


def test_generate_evidence_card_includes_required_keys() -> None:
    entry = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())

    card = generate_evidence_card(entry)

    for key in REQUIRED_KEYS:
        assert key in card
    assert card["benchmark_id"] == "bbb_b3pred_dataset3"
    assert card["task_name"] == "bbb_peptide_prioritization_v1"
    assert card["generated_at"] == "example-generated"
    assert card["artifact_status"] == "example metadata artifact"


def test_evidence_cards_are_deterministic() -> None:
    entry = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())

    assert generate_evidence_cards(entry) == generate_evidence_cards(entry)
    assert generate_evidence_card(entry) == generate_evidence_card(entry)


def test_evidence_cards_contain_explicit_non_claims() -> None:
    entry = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())

    card = generate_evidence_card(entry)

    assert card["non_claims"]["no_model_execution"] is True
    assert card["non_claims"]["no_dataset_download"] is True
    assert card["non_claims"]["no_wet_lab_validation_by_permea"] is True
    assert card["non_claims"]["no_redistribution_rights_confirmation"] is True


def test_invalid_benchmark_yaml_fails_before_generation(tmp_path: Path) -> None:
    payload = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())
    del payload["claim_boundary"]
    input_path = tmp_path / "invalid.yaml"
    output_path = tmp_path / "invalid.evidence_cards.json"
    input_path.write_text(yaml.safe_dump(payload), encoding="utf-8")

    result = generate_evidence_cards_file(input_path, output_path)

    assert not result.passed
    assert "claim_boundary" in result.message
    assert not output_path.exists()


def test_generate_evidence_cards_file_writes_output(tmp_path: Path) -> None:
    output_path = tmp_path / "bbb_b3pred_dataset3.evidence_cards.json"

    result = generate_evidence_cards_file(
        ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml",
        output_path,
    )

    assert result.passed
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload[0]["benchmark_id"] == "bbb_b3pred_dataset3"


def test_cli_generates_default_evidence_cards() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_evidence_cards.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS evidence card generation" in completed.stdout
    assert (
        ROOT
        / "docs"
        / "examples"
        / "generated"
        / "evidence_cards"
        / "bbb_b3pred_dataset3.evidence_cards.json"
    ).exists()


def test_generated_text_avoids_unsupported_claim_phrases() -> None:
    entry = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())
    text = json.dumps(generate_evidence_cards(entry)).lower()

    for phrase in UNSUPPORTED_CLAIM_PHRASES:
        assert phrase not in text
