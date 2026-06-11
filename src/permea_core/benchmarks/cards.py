"""Markdown benchmark card generation for Permea benchmark metadata."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .registry import load_registry_yaml, validate_registry_file


DEFAULT_BENCHMARK_CARD_DIR = Path("docs/examples/generated/benchmark_cards")


@dataclass(frozen=True, slots=True)
class BenchmarkCardGenerationResult:
    """Structured result for generated benchmark card files."""

    input_path: Path
    output_path: Path
    benchmark_id: str
    passed: bool
    message: str


@dataclass(frozen=True, slots=True)
class BenchmarkCardBatchResult:
    """Structured result for registry-driven benchmark card generation."""

    registry_path: Path
    output_dir: Path
    generated: tuple[BenchmarkCardGenerationResult, ...]
    passed: bool
    message: str


def render_benchmark_card(entry: dict[str, Any]) -> str:
    """Render one validated benchmark registry entry as Markdown."""
    benchmark_id = _required_string(entry, "benchmark_id")
    task_name = _required_string(entry, "task_name")

    sections = [
        f"# Benchmark Card: {benchmark_id}",
        "",
        "> Generated from Permea benchmark registry metadata. This card is a public-safe benchmark summary, not a record of dataset acquisition, model execution, or validation results.",
        "",
        "## Benchmark ID",
        "",
        benchmark_id,
        "",
        "## Task Name",
        "",
        task_name,
        "",
        "## Delivery Context",
        "",
        _required_string(entry, "delivery_context"),
        "",
        "## Maturity Level",
        "",
        _required_string(entry, "maturity_level"),
        "",
        "## Dataset Card",
        "",
        _required_string(entry, "dataset_card"),
        "",
        "## Benchmark Task Spec",
        "",
        _required_string(entry, "benchmark_task_spec"),
        "",
        "## Split Policy",
        "",
        _render_mapping(entry.get("split_policy")),
        "",
        "## Metrics",
        "",
        _render_mapping(entry.get("metrics")),
        "",
        "## Baseline Models",
        "",
        _render_list(entry.get("baseline_models")),
        "",
        "## Output Artifacts",
        "",
        _render_list(entry.get("output_artifacts")),
        "",
        "## Limitations",
        "",
        _render_list(entry.get("limitations")),
        "",
        "## Claim Boundary",
        "",
        _required_string(entry, "claim_boundary"),
        "",
    ]
    return "\n".join(sections)


def generate_benchmark_card_file(
    input_path: str | Path,
    output_path: str | Path,
) -> BenchmarkCardGenerationResult:
    """Validate one benchmark YAML file and write its Markdown card."""
    benchmark_path = Path(input_path)
    card_path = Path(output_path)

    validation = validate_registry_file(benchmark_path)
    if not validation.passed:
        return BenchmarkCardGenerationResult(
            input_path=benchmark_path,
            output_path=card_path,
            benchmark_id="<invalid>",
            passed=False,
            message=_format_validation_failure(validation.errors),
        )

    entry = load_registry_yaml(benchmark_path)
    if not isinstance(entry, dict):
        return BenchmarkCardGenerationResult(
            input_path=benchmark_path,
            output_path=card_path,
            benchmark_id="<invalid>",
            passed=False,
            message="Benchmark YAML must contain one mapping entry.",
        )

    text = render_benchmark_card(entry)
    card_path.parent.mkdir(parents=True, exist_ok=True)
    card_path.write_text(text, encoding="utf-8")

    return BenchmarkCardGenerationResult(
        input_path=benchmark_path,
        output_path=card_path,
        benchmark_id=_required_string(entry, "benchmark_id"),
        passed=True,
        message="Generated benchmark card.",
    )


def generate_benchmark_cards_from_registry(
    registry_path: str | Path,
    output_dir: str | Path,
) -> BenchmarkCardBatchResult:
    """Validate a registry YAML file and generate one card per registry entry."""
    registry = Path(registry_path)
    destination = Path(output_dir)

    validation = validate_registry_file(registry)
    if not validation.passed:
        return BenchmarkCardBatchResult(
            registry_path=registry,
            output_dir=destination,
            generated=(),
            passed=False,
            message=_format_validation_failure(validation.errors),
        )

    payload = load_registry_yaml(registry)
    entries = payload.get("benchmarks") if isinstance(payload, dict) else None
    if not isinstance(entries, list):
        return BenchmarkCardBatchResult(
            registry_path=registry,
            output_dir=destination,
            generated=(),
            passed=False,
            message="Registry YAML must contain a benchmarks list.",
        )

    results: list[BenchmarkCardGenerationResult] = []
    destination.mkdir(parents=True, exist_ok=True)
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        benchmark_id = _required_string(entry, "benchmark_id")
        output_path = destination / f"{benchmark_id}.md"
        output_path.write_text(render_benchmark_card(entry), encoding="utf-8")
        results.append(
            BenchmarkCardGenerationResult(
                input_path=registry,
                output_path=output_path,
                benchmark_id=benchmark_id,
                passed=True,
                message="Generated benchmark card.",
            )
        )

    return BenchmarkCardBatchResult(
        registry_path=registry,
        output_dir=destination,
        generated=tuple(results),
        passed=True,
        message=f"Generated {len(results)} benchmark card(s).",
    )


def _required_string(entry: dict[str, Any], field: str) -> str:
    value = entry[field]
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string.")
    return value


def _render_mapping(value: Any) -> str:
    if not isinstance(value, dict):
        return "- not specified"
    lines: list[str] = []
    for key, item in value.items():
        if isinstance(item, list):
            lines.append(f"- {key}:")
            lines.extend(f"  - {subitem}" for subitem in item)
        else:
            lines.append(f"- {key}: {item}")
    return "\n".join(lines)


def _render_list(value: Any) -> str:
    if not isinstance(value, list) or not value:
        return "- not specified"
    return "\n".join(f"- {item}" for item in value)


def _format_validation_failure(errors: tuple[Any, ...]) -> str:
    details = "; ".join(
        f"{error.entry}.{error.field}: {error.message}" for error in errors
    )
    return f"Benchmark metadata validation failed: {details}"
