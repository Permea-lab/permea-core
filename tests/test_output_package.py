from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.benchmarks.output_package import (
    OUTPUT_PACKAGE_FILES,
    generate_evidence_cards,
    generate_metrics,
    generate_output_package,
    generate_ranking,
)


UNSUPPORTED_CLAIM_PHRASES = (
    "wet-lab " + "validated",
    "clinical " + "efficacy",
    "universal " + "predictor",
    "solved " + "delivery",
    "state-of-the-art",
)


def test_generate_output_package_writes_required_files(tmp_path: Path) -> None:
    output_dir = tmp_path / "package"

    result = generate_output_package(
        ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml",
        output_dir,
    )

    assert result.passed
    assert {path.name for path in result.files_written} == set(OUTPUT_PACKAGE_FILES)
    for filename in OUTPUT_PACKAGE_FILES:
        assert (output_dir / filename).exists()


def test_manifest_includes_benchmark_id_and_task_name(tmp_path: Path) -> None:
    output_dir = tmp_path / "package"
    generate_output_package(ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml", output_dir)

    manifest = yaml.safe_load((output_dir / "manifest.yaml").read_text())

    assert manifest["benchmark_id"] == "bbb_b3pred_dataset3"
    assert manifest["task_name"] == "bbb_peptide_prioritization_v1"
    assert manifest["generated_at"] == "example-generated"
    assert manifest["example_boundaries"]["no_model_execution"] is True


def test_metrics_ranking_and_evidence_cards_are_deterministic() -> None:
    entry = yaml.safe_load((ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml").read_text())

    assert generate_metrics(entry) == generate_metrics(entry)
    assert generate_ranking(entry) == generate_ranking(entry)
    assert generate_evidence_cards(entry) == generate_evidence_cards(entry)
    assert generate_metrics(entry)["metric_values"]["pr_auc"] is None
    assert generate_ranking(entry)[0]["candidate_id"].endswith("example_candidate_001")


def test_benchmark_card_in_output_package_includes_required_headings(tmp_path: Path) -> None:
    output_dir = tmp_path / "package"
    generate_output_package(ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml", output_dir)

    card = (output_dir / "benchmark_card.md").read_text(encoding="utf-8")

    assert "# Benchmark Card: bbb_b3pred_dataset3" in card
    assert "## Benchmark ID" in card
    assert "## Task Name" in card
    assert "## Claim Boundary" in card


def test_cli_generates_default_output_package() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_output_package.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS output package generation" in completed.stdout
    assert (
        ROOT
        / "docs"
        / "examples"
        / "generated"
        / "output_packages"
        / "bbb_b3pred_dataset3"
        / "manifest.yaml"
    ).exists()


def test_generated_output_package_avoids_unsupported_claim_phrases(tmp_path: Path) -> None:
    output_dir = tmp_path / "package"
    generate_output_package(ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml", output_dir)

    combined = "\n".join(
        (output_dir / filename).read_text(encoding="utf-8")
        for filename in OUTPUT_PACKAGE_FILES
    ).lower()

    for phrase in UNSUPPORTED_CLAIM_PHRASES:
        assert phrase not in combined


def test_ranking_csv_rows_are_stable(tmp_path: Path) -> None:
    output_dir = tmp_path / "package"
    generate_output_package(ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml", output_dir)

    with (output_dir / "ranking.csv").open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    assert rows[0]["rank"] == "1"
    assert rows[1]["rank"] == "2"


def test_metrics_json_is_public_safe_example_metadata(tmp_path: Path) -> None:
    output_dir = tmp_path / "package"
    generate_output_package(ROOT / "benchmarks" / "bbb_b3pred_dataset3.yaml", output_dir)

    metrics = json.loads((output_dir / "metrics.json").read_text(encoding="utf-8"))

    assert metrics["artifact_type"] == "example_metadata_artifact"
    assert "no model execution" in metrics["generation_note"]
