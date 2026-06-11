"""Deterministic example evidence card generation for benchmark metadata."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .registry import load_registry_yaml, validate_registry_file


DEFAULT_EVIDENCE_CARD_INPUTS = (
    Path("benchmarks/bbb_b3pred_dataset3.yaml"),
    Path("benchmarks/cpp_cppsite2_placeholder.yaml"),
)
DEFAULT_EVIDENCE_CARD_DIR = Path("docs/examples/generated/evidence_cards")
EXAMPLE_GENERATED_AT = "example-generated"
EXAMPLE_ARTIFACT_STATUS = "example metadata artifact"
EXAMPLE_NON_CLAIMS = {
    "no_model_execution": True,
    "no_dataset_download": True,
    "no_wet_lab_validation_by_permea": True,
    "no_redistribution_rights_confirmation": True,
}
EXAMPLE_GENERATION_NOTE = (
    "Example metadata artifact only; no model execution, no dataset download, "
    "no wet-lab validation by Permea, and no redistribution-rights confirmation."
)


@dataclass(frozen=True, slots=True)
class EvidenceCardGenerationResult:
    """Structured result for one generated evidence card file."""

    input_path: Path
    output_path: Path
    benchmark_id: str
    passed: bool
    message: str


@dataclass(frozen=True, slots=True)
class EvidenceCardBatchResult:
    """Structured result for generating multiple evidence card files."""

    output_dir: Path
    generated: tuple[EvidenceCardGenerationResult, ...]
    passed: bool
    message: str


def generate_evidence_card(
    entry: dict[str, Any],
    evidence_type: str = "metadata",
) -> dict[str, Any]:
    """Generate one deterministic public-safe evidence card."""
    benchmark_id = _required_string(entry, "benchmark_id")
    task_name = _required_string(entry, "task_name")
    dataset_card = _required_string(entry, "dataset_card")
    benchmark_task_spec = _required_string(entry, "benchmark_task_spec")

    return {
        "evidence_card_id": f"ec_{benchmark_id}_{evidence_type}_example",
        "artifact_status": EXAMPLE_ARTIFACT_STATUS,
        "artifact_type": "example_metadata_artifact",
        "generated_at": EXAMPLE_GENERATED_AT,
        "benchmark_id": benchmark_id,
        "task_name": task_name,
        "evidence_type": evidence_type,
        "source_reference": {
            "source_kind": "benchmark_metadata",
            "dataset_card": dataset_card,
            "benchmark_task_spec": benchmark_task_spec,
            "source_access_status": "not_accessed_in_this_example",
        },
        "provenance_status": "metadata_only_no_source_retrieval",
        "delivery_context": _required_string(entry, "delivery_context"),
        "molecule_sequence_cargo": {
            "molecule_type": "not_specified_in_example_metadata",
            "sequence_or_identifier": "not_included",
            "cargo_context": "not_specified_in_example_metadata",
        },
        "assay_or_evidence_type": f"example_{evidence_type}_only",
        "extracted_claim": {
            "text": (
                "This example records benchmark metadata and claim boundaries only."
            ),
            "source_context_preserved": True,
        },
        "support_level": "example_only",
        "review_status": "draft_example",
        "related_objects": {
            "dataset_card": dataset_card,
            "benchmark_task": benchmark_task_spec,
            "benchmark_id": benchmark_id,
        },
        "limitations": entry.get("limitations", []),
        "claim_boundary": _required_string(entry, "claim_boundary"),
        "non_claims": dict(EXAMPLE_NON_CLAIMS),
        "generation_note": EXAMPLE_GENERATION_NOTE,
    }


def generate_evidence_cards(entry: dict[str, Any]) -> list[dict[str, Any]]:
    """Generate deterministic public-safe evidence cards for one benchmark."""
    return [generate_evidence_card(entry)]


def generate_evidence_cards_file(
    input_path: str | Path,
    output_path: str | Path,
) -> EvidenceCardGenerationResult:
    """Validate one benchmark YAML file and write example evidence cards."""
    benchmark_path = Path(input_path)
    evidence_path = Path(output_path)

    validation = validate_registry_file(benchmark_path)
    if not validation.passed:
        return EvidenceCardGenerationResult(
            input_path=benchmark_path,
            output_path=evidence_path,
            benchmark_id="<invalid>",
            passed=False,
            message=_format_validation_failure(validation.errors),
        )

    entry = load_registry_yaml(benchmark_path)
    if not isinstance(entry, dict):
        return EvidenceCardGenerationResult(
            input_path=benchmark_path,
            output_path=evidence_path,
            benchmark_id="<invalid>",
            passed=False,
            message="Benchmark YAML must contain one mapping entry.",
        )

    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    evidence_path.write_text(
        json.dumps(generate_evidence_cards(entry), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    return EvidenceCardGenerationResult(
        input_path=benchmark_path,
        output_path=evidence_path,
        benchmark_id=_required_string(entry, "benchmark_id"),
        passed=True,
        message="Generated evidence cards.",
    )


def generate_evidence_cards_for_inputs(
    input_paths: tuple[Path, ...],
    output_dir: str | Path,
) -> EvidenceCardBatchResult:
    """Generate evidence card files for multiple benchmark YAML files."""
    destination = Path(output_dir)
    results: list[EvidenceCardGenerationResult] = []

    for input_path in input_paths:
        entry = load_registry_yaml(input_path)
        benchmark_id = (
            entry.get("benchmark_id")
            if isinstance(entry, dict) and isinstance(entry.get("benchmark_id"), str)
            else input_path.stem
        )
        output_path = destination / f"{benchmark_id}.evidence_cards.json"
        result = generate_evidence_cards_file(input_path, output_path)
        results.append(result)

    failed = [result for result in results if not result.passed]
    if failed:
        message = "; ".join(result.message for result in failed)
        return EvidenceCardBatchResult(
            output_dir=destination,
            generated=tuple(results),
            passed=False,
            message=message,
        )

    return EvidenceCardBatchResult(
        output_dir=destination,
        generated=tuple(results),
        passed=True,
        message=f"Generated {len(results)} evidence card file(s).",
    )


def _required_string(entry: dict[str, Any], field: str) -> str:
    value = entry[field]
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string.")
    return value


def _format_validation_failure(errors: tuple[Any, ...]) -> str:
    details = "; ".join(
        f"{error.entry}.{error.field}: {error.message}" for error in errors
    )
    return f"Benchmark metadata validation failed: {details}"
