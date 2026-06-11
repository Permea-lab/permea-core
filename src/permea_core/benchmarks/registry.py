"""Benchmark registry interfaces and YAML validation for Permea Core."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only without PyYAML installed.
    yaml = None  # type: ignore[assignment]


REQUIRED_REGISTRY_FIELDS = frozenset(
    {
        "benchmark_id",
        "task_name",
        "delivery_context",
        "maturity_level",
        "dataset_card",
        "benchmark_task_spec",
        "split_policy",
        "metrics",
        "baseline_models",
        "output_artifacts",
        "limitations",
        "claim_boundary",
    }
)

ALLOWED_MATURITY_LEVELS = frozenset(
    {
        "proposed",
        "dataset-carded",
        "benchmark-candidate",
        "baseline-ready",
        "reproducible",
        "community-reviewed",
    }
)

EXPECTED_OUTPUT_ARTIFACTS = (
    "metrics.json",
    "ranking.csv",
    "manifest.yaml",
    "benchmark_card.md",
    "evidence_cards.json",
)


@dataclass(frozen=True, slots=True)
class BenchmarkDefinition:
    """Describes a benchmark task exposed by the repository."""

    benchmark_id: str
    benchmark_version: str
    title: str
    description: str
    input_schema_ref: str
    output_schema_ref: str
    metric_ids: tuple[str, ...] = field(default_factory=tuple)


class BenchmarkRegistry:
    """In-memory registry for benchmark definitions.

    This stub keeps the benchmark surface explicit while avoiding
    premature infrastructure decisions.
    """

    def __init__(self) -> None:
        self._definitions: dict[tuple[str, str], BenchmarkDefinition] = {}

    def register(self, definition: BenchmarkDefinition) -> None:
        """Register a benchmark definition by id and version."""
        key = (definition.benchmark_id, definition.benchmark_version)
        self._definitions[key] = definition

    def get(self, benchmark_id: str, benchmark_version: str) -> BenchmarkDefinition:
        """Return a benchmark definition or raise if it is missing."""
        key = (benchmark_id, benchmark_version)
        try:
            return self._definitions[key]
        except KeyError as exc:
            raise KeyError(
                f"Unknown benchmark definition: {benchmark_id}@{benchmark_version}"
            ) from exc

    def list_definitions(self) -> list[BenchmarkDefinition]:
        """Return all registered definitions in insertion order."""
        return list(self._definitions.values())


@dataclass(frozen=True, slots=True)
class RegistryValidationError:
    """Structured validation error for a registry entry."""

    entry: str
    field: str
    message: str


@dataclass(frozen=True, slots=True)
class RegistryValidationResult:
    """Validation outcome for a benchmark registry YAML file."""

    path: Path
    entries_checked: int
    errors: tuple[RegistryValidationError, ...] = field(default_factory=tuple)

    @property
    def passed(self) -> bool:
        """Return True when the registry has no validation errors."""
        return not self.errors


def load_registry_yaml(path: str | Path) -> Any:
    """Load a YAML registry file."""
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to validate benchmark registry YAML files. "
            "Install PyYAML or run in the project environment that provides it."
        )

    registry_path = Path(path)
    with registry_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_registry_file(path: str | Path) -> RegistryValidationResult:
    """Validate a registry YAML file and return structured errors."""
    registry_path = Path(path)
    try:
        payload = load_registry_yaml(registry_path)
    except Exception as exc:  # noqa: BLE001 - CLI should report load failures clearly.
        return RegistryValidationResult(
            path=registry_path,
            entries_checked=0,
            errors=(
                RegistryValidationError(
                    entry="<file>",
                    field="<load>",
                    message=str(exc),
                ),
            ),
        )

    entries = _extract_entries(payload)
    errors: list[RegistryValidationError] = []

    if not entries:
        errors.append(
            RegistryValidationError(
                entry="<registry>",
                field="benchmarks",
                message="Registry must contain at least one benchmark entry.",
            )
        )
        return RegistryValidationResult(
            path=registry_path,
            entries_checked=0,
            errors=tuple(errors),
        )

    for index, entry in enumerate(entries):
        errors.extend(_validate_entry(entry, index))

    return RegistryValidationResult(
        path=registry_path,
        entries_checked=len(entries),
        errors=tuple(errors),
    )


def _extract_entries(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict) and isinstance(payload.get("benchmarks"), list):
        return [entry for entry in payload["benchmarks"] if isinstance(entry, dict)]
    if isinstance(payload, dict):
        return [payload]
    return []


def _entry_name(entry: dict[str, Any], index: int) -> str:
    value = entry.get("benchmark_id")
    if isinstance(value, str) and value:
        return value
    return f"entry[{index}]"


def _validate_entry(
    entry: dict[str, Any],
    index: int,
) -> list[RegistryValidationError]:
    name = _entry_name(entry, index)
    errors: list[RegistryValidationError] = []

    missing = sorted(REQUIRED_REGISTRY_FIELDS.difference(entry))
    for field_name in missing:
        errors.append(
            RegistryValidationError(
                entry=name,
                field=field_name,
                message="Required field is missing.",
            )
        )

    maturity_level = entry.get("maturity_level")
    if maturity_level not in ALLOWED_MATURITY_LEVELS:
        errors.append(
            RegistryValidationError(
                entry=name,
                field="maturity_level",
                message=(
                    "maturity_level must be one of: "
                    + ", ".join(sorted(ALLOWED_MATURITY_LEVELS))
                ),
            )
        )

    output_artifacts = entry.get("output_artifacts")
    if output_artifacts is not None:
        if not isinstance(output_artifacts, list):
            errors.append(
                RegistryValidationError(
                    entry=name,
                    field="output_artifacts",
                    message="output_artifacts must be a list.",
                )
            )
        else:
            missing_artifacts = [
                artifact
                for artifact in EXPECTED_OUTPUT_ARTIFACTS
                if artifact not in output_artifacts
            ]
            for artifact in missing_artifacts:
                errors.append(
                    RegistryValidationError(
                        entry=name,
                        field="output_artifacts",
                        message=f"Missing expected output artifact: {artifact}",
                    )
                )

    return errors
