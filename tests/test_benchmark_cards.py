from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.benchmarks.cards import (
    generate_benchmark_card_file,
    render_benchmark_card,
)


REQUIRED_HEADINGS = (
    "# Benchmark Card: bbb_b3pred_dataset3",
    "## Benchmark ID",
    "## Task Name",
    "## Delivery Context",
    "## Maturity Level",
    "## Dataset Card",
    "## Benchmark Task Spec",
    "## Split Policy",
    "## Metrics",
    "## Baseline Models",
    "## Output Artifacts",
    "## Limitations",
    "## Claim Boundary",
)


UNSUPPORTED_CLAIM_PHRASES = (
    "wet-lab " + "validated",
    "clinical " + "efficacy",
    "universal " + "predictor",
    "solved " + "delivery",
    "state-of-the-art",
)


def test_render_benchmark_card_includes_required_headings() -> None:
    entry = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())

    card = render_benchmark_card(entry)

    for heading in REQUIRED_HEADINGS:
        assert heading in card
    assert "Generated from Permea benchmark registry metadata" in card


def test_invalid_benchmark_yaml_fails_before_generation(tmp_path: Path) -> None:
    payload = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())
    del payload["claim_boundary"]
    input_path = tmp_path / "invalid.yaml"
    output_path = tmp_path / "invalid.md"
    input_path.write_text(yaml.safe_dump(payload), encoding="utf-8")

    result = generate_benchmark_card_file(input_path, output_path)

    assert not result.passed
    assert "claim_boundary" in result.message
    assert not output_path.exists()


def test_generate_benchmark_card_file_writes_output(tmp_path: Path) -> None:
    output_path = tmp_path / "bbb_b3pred_dataset3.md"

    result = generate_benchmark_card_file(
        ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml",
        output_path,
    )

    assert result.passed
    text = output_path.read_text(encoding="utf-8")
    assert "bbb_b3pred_dataset3" in text
    assert "bbb_peptide_prioritization_v1" in text


def test_cli_generates_default_benchmark_cards(tmp_path: Path) -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_benchmark_card.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS benchmark card generation" in completed.stdout
    assert (
        ROOT / "docs" / "examples" / "generated" / "benchmark_cards" / "bbb_b3pred_dataset3.md"
    ).exists()


def test_generated_text_avoids_unsupported_claim_phrases() -> None:
    entry = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())
    card = render_benchmark_card(entry).lower()

    for phrase in UNSUPPORTED_CLAIM_PHRASES:
        assert phrase not in card
