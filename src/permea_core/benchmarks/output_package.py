"""Deterministic example output package generation for benchmark metadata."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .cards import render_benchmark_card
from .registry import load_registry_yaml, validate_registry_file, yaml


DEFAULT_OUTPUT_PACKAGE_INPUT = Path("benchmarks/bbb_b3pred_dataset3.yaml")
DEFAULT_OUTPUT_PACKAGE_DIR = Path(
    "docs/examples/generated/output_packages/bbb_b3pred_dataset3"
)
OUTPUT_PACKAGE_FILES = (
    "manifest.yaml",
    "metrics.json",
    "ranking.csv",
    "benchmark_card.md",
    "evidence_cards.json",
)
EXAMPLE_GENERATED_AT = "example-generated"
EXAMPLE_NOTE = (
    "Example metadata artifact only; no model execution, no dataset download, "
    "no wet-lab validation by Permea, and no redistribution-rights confirmation."
)


@dataclass(frozen=True, slots=True)
class OutputPackageGenerationResult:
    """Structured result for output package generation."""

    input_path: Path
    output_dir: Path
    benchmark_id: str
    files_written: tuple[Path, ...]
    passed: bool
    message: str


def generate_manifest(entry: dict[str, Any]) -> dict[str, Any]:
    """Generate a deterministic example run manifest from benchmark metadata."""
    benchmark_id = _required_string(entry, "benchmark_id")
    task_name = _required_string(entry, "task_name")
    return {
        "run_id": f"example_{benchmark_id}_output_package",
        "generated_at": EXAMPLE_GENERATED_AT,
        "artifact_type": "example_metadata_artifact",
        "benchmark_id": benchmark_id,
        "task_name": task_name,
        "delivery_context": _required_string(entry, "delivery_context"),
        "maturity_level": _required_string(entry, "maturity_level"),
        "dataset": {
            "dataset_card_path": _required_string(entry, "dataset_card"),
            "dataset_version": "example",
            "label_version": "example",
            "release_posture": "public_example_metadata_only",
        },
        "benchmark_task": {
            "benchmark_task_path": _required_string(entry, "benchmark_task_spec"),
            "task_version": "example",
            "task_type": "example_metadata_only",
        },
        "split_policy": entry.get("split_policy", {}),
        "metrics_output_path": "metrics.json",
        "ranking_output_path": "ranking.csv",
        "benchmark_card_path": "benchmark_card.md",
        "evidence_card_paths": ["evidence_cards.json"],
        "example_boundaries": {
            "no_model_execution": True,
            "no_dataset_download": True,
            "no_wet_lab_validation_by_permea": True,
            "no_redistribution_rights_confirmation": True,
        },
        "limitations": entry.get("limitations", []),
        "claim_boundary": _required_string(entry, "claim_boundary"),
        "generation_note": EXAMPLE_NOTE,
    }


def generate_metrics(entry: dict[str, Any]) -> dict[str, Any]:
    """Generate deterministic placeholder metrics metadata."""
    metrics = entry.get("metrics", {})
    primary = metrics.get("primary", "not_specified") if isinstance(metrics, dict) else "not_specified"
    secondary = metrics.get("secondary", []) if isinstance(metrics, dict) else []
    metric_names = [primary, *secondary]
    return {
        "artifact_type": "example_metadata_artifact",
        "generated_at": EXAMPLE_GENERATED_AT,
        "benchmark_id": _required_string(entry, "benchmark_id"),
        "task_name": _required_string(entry, "task_name"),
        "model_or_baseline": "example_placeholder_no_model_execution",
        "metric_values": {metric_name: None for metric_name in metric_names},
        "limitations": entry.get("limitations", []),
        "claim_boundary": _required_string(entry, "claim_boundary"),
        "generation_note": EXAMPLE_NOTE,
    }


def generate_ranking(entry: dict[str, Any]) -> list[dict[str, Any]]:
    """Generate deterministic placeholder ranking rows."""
    benchmark_id = _required_string(entry, "benchmark_id")
    return [
        {
            "candidate_id": f"{benchmark_id}_example_candidate_001",
            "rank": 1,
            "score": "",
            "review_status": "example_metadata_only",
            "note": "No model execution or dataset download.",
        },
        {
            "candidate_id": f"{benchmark_id}_example_candidate_002",
            "rank": 2,
            "score": "",
            "review_status": "example_metadata_only",
            "note": "No model execution or dataset download.",
        },
    ]


def generate_evidence_cards(entry: dict[str, Any]) -> list[dict[str, Any]]:
    """Generate deterministic example evidence-card metadata."""
    benchmark_id = _required_string(entry, "benchmark_id")
    return [
        {
            "evidence_card_id": f"ec_{benchmark_id}_example_metadata",
            "artifact_type": "example_metadata_artifact",
            "generated_at": EXAMPLE_GENERATED_AT,
            "delivery_context": _required_string(entry, "delivery_context"),
            "assay_or_evidence_type": "example_metadata_only",
            "support_level": "example_only",
            "review_status": "draft_example",
            "related_objects": {
                "dataset_card": _required_string(entry, "dataset_card"),
                "benchmark_task": _required_string(entry, "benchmark_task_spec"),
            },
            "limitations": entry.get("limitations", []),
            "claim_boundary": _required_string(entry, "claim_boundary"),
            "generation_note": EXAMPLE_NOTE,
        }
    ]


def generate_output_package(
    input_path: str | Path,
    output_dir: str | Path,
) -> OutputPackageGenerationResult:
    """Validate benchmark YAML and write a deterministic example output package."""
    benchmark_path = Path(input_path)
    package_dir = Path(output_dir)

    validation = validate_registry_file(benchmark_path)
    if not validation.passed:
        return OutputPackageGenerationResult(
            input_path=benchmark_path,
            output_dir=package_dir,
            benchmark_id="<invalid>",
            files_written=(),
            passed=False,
            message=_format_validation_failure(validation.errors),
        )

    entry = load_registry_yaml(benchmark_path)
    if not isinstance(entry, dict):
        return OutputPackageGenerationResult(
            input_path=benchmark_path,
            output_dir=package_dir,
            benchmark_id="<invalid>",
            files_written=(),
            passed=False,
            message="Benchmark YAML must contain one mapping entry.",
        )

    package_dir.mkdir(parents=True, exist_ok=True)
    written = (
        _write_yaml(package_dir / "manifest.yaml", generate_manifest(entry)),
        _write_json(package_dir / "metrics.json", generate_metrics(entry)),
        _write_ranking_csv(package_dir / "ranking.csv", generate_ranking(entry)),
        _write_text(package_dir / "benchmark_card.md", render_benchmark_card(entry)),
        _write_json(package_dir / "evidence_cards.json", generate_evidence_cards(entry)),
    )

    return OutputPackageGenerationResult(
        input_path=benchmark_path,
        output_dir=package_dir,
        benchmark_id=_required_string(entry, "benchmark_id"),
        files_written=written,
        passed=True,
        message=f"Generated {len(written)} output package artifact(s).",
    )


def _required_string(entry: dict[str, Any], field: str) -> str:
    value = entry[field]
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string.")
    return value


def _write_yaml(path: Path, payload: dict[str, Any]) -> Path:
    if yaml is None:
        raise RuntimeError("PyYAML is required to generate manifest.yaml.")
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    return path


def _write_json(path: Path, payload: Any) -> Path:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _write_ranking_csv(path: Path, rows: list[dict[str, Any]]) -> Path:
    fieldnames = ("candidate_id", "rank", "score", "review_status", "note")
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return path


def _write_text(path: Path, text: str) -> Path:
    path.write_text(text, encoding="utf-8")
    return path


def _format_validation_failure(errors: tuple[Any, ...]) -> str:
    details = "; ".join(
        f"{error.entry}.{error.field}: {error.message}" for error in errors
    )
    return f"Benchmark metadata validation failed: {details}"
