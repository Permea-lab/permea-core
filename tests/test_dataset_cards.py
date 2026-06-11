from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.datasets.cards import (
    generate_dataset_card_file,
    render_dataset_card,
    validate_dataset_card,
    validate_dataset_card_file,
)


def test_current_dataset_cards_pass() -> None:
    card_paths = sorted((ROOT / "dataset_cards").glob("*.yaml"))

    assert len(card_paths) == 2
    for card_path in card_paths:
        result = validate_dataset_card_file(card_path)
        assert result.passed, card_path


def test_missing_required_field_fails(tmp_path: Path) -> None:
    payload = _valid_card()
    del payload["claim_boundary"]
    card_path = tmp_path / "missing_required.yaml"
    card_path.write_text(yaml.safe_dump(payload), encoding="utf-8")

    result = validate_dataset_card_file(card_path)

    assert not result.passed
    assert any(error.field == "claim_boundary" for error in result.errors)


def test_invalid_acquisition_status_fails() -> None:
    card = _valid_card()
    card["acquisition_status"] = "downloaded"

    errors = validate_dataset_card(card)

    assert any(error.field == "acquisition_status" for error in errors)


def test_invalid_redistribution_status_fails() -> None:
    card = _valid_card()
    card["redistribution_status"] = "confirmed"

    errors = validate_dataset_card(card)

    assert any(error.field == "redistribution_status" for error in errors)


def test_rendered_markdown_includes_required_sections() -> None:
    text = render_dataset_card(_valid_card())

    for section in (
        "## Dataset ID",
        "## Source IDs",
        "## Benchmark IDs",
        "## Acquisition Status",
        "## Redistribution Status",
        "## Explicit Non-Claims",
        "## Claim Boundary",
    ):
        assert section in text


def test_rendered_markdown_includes_explicit_non_claims() -> None:
    text = render_dataset_card(_valid_card())

    assert "no dataset downloaded" in text
    assert "no redistribution rights confirmed" in text
    assert "no wet-lab validation by Permea" in text


def test_generate_dataset_card_file_writes_markdown(tmp_path: Path) -> None:
    output_path = tmp_path / "b3pred_dataset3.md"

    result = generate_dataset_card_file(
        ROOT / "dataset_cards" / "b3pred_dataset3.yaml",
        output_path,
    )

    assert result.passed
    assert "# Dataset Card:" in output_path.read_text(encoding="utf-8")


def test_cli_validates_and_generates_dataset_cards() -> None:
    validate = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_dataset_cards.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    generate = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_dataset_cards.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert validate.returncode == 0
    assert "PASS dataset card validation: 2 card(s)" in validate.stdout
    assert generate.returncode == 0
    assert "PASS dataset card generation: Generated 2 dataset card(s)." in generate.stdout


def _valid_card() -> dict[str, object]:
    return yaml.safe_load((ROOT / "dataset_cards" / "b3pred_dataset3.yaml").read_text())
