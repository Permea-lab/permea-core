"""Source registry YAML validation for Permea Core."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only without PyYAML installed.
    yaml = None  # type: ignore[assignment]


REQUIRED_SOURCE_FIELDS = frozenset(
    {
        "source_id",
        "source_name",
        "delivery_axis",
        "biological_scope",
        "likely_data_type",
        "acquisition_mode",
        "license_access_status",
        "redistribution_risk",
        "provenance_strength",
        "benchmark_mapping",
        "priority",
        "current_status",
        "next_action",
        "limitations",
        "claim_boundary",
    }
)

ALLOWED_PRIORITIES = frozenset({"high", "medium", "low"})

ALLOWED_CURRENT_STATUSES = frozenset(
    {
        "candidate",
        "source-carded",
        "access-to-verify",
        "license-to-verify",
        "acquisition-planned",
        "benchmark-mapped",
    }
)

ALLOWED_ACQUISITION_MODES = frozenset(
    {
        "manual-source-card",
        "public-download-to-verify",
        "api-metadata-to-verify",
        "literature-metadata",
        "no-redistribution-source-card-only",
    }
)


@dataclass(frozen=True, slots=True)
class SourceRegistryValidationError:
    """Structured validation error for a source registry entry."""

    entry: str
    field: str
    message: str


@dataclass(frozen=True, slots=True)
class SourceRegistryValidationResult:
    """Validation outcome for a source registry YAML file."""

    path: Path
    entries_checked: int
    errors: tuple[SourceRegistryValidationError, ...] = field(default_factory=tuple)

    @property
    def passed(self) -> bool:
        """Return True when the registry has no validation errors."""
        return not self.errors


def load_source_registry_yaml(path: str | Path) -> Any:
    """Load a local source registry YAML file."""
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to validate source registry YAML files. "
            "Install PyYAML or run in the project environment that provides it."
        )

    registry_path = Path(path)
    with registry_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_source_entry(entry: dict[str, Any]) -> list[SourceRegistryValidationError]:
    """Validate one source registry entry and return structured errors."""
    name = _entry_name(entry, 0)
    return _validate_entry(entry, name)


def validate_source_registry(data: dict[str, Any]) -> list[SourceRegistryValidationError]:
    """Validate a source registry payload and return structured errors."""
    entries = _extract_entries(data)
    errors: list[SourceRegistryValidationError] = []

    if not entries:
        errors.append(
            SourceRegistryValidationError(
                entry="<registry>",
                field="sources",
                message="Registry must contain at least one source entry.",
            )
        )
        return errors

    for index, entry in enumerate(entries):
        errors.extend(_validate_entry(entry, _entry_name(entry, index)))

    return errors


def validate_source_registry_file(path: str | Path) -> SourceRegistryValidationResult:
    """Validate a source registry YAML file and return structured errors."""
    registry_path = Path(path)
    try:
        payload = load_source_registry_yaml(registry_path)
    except Exception as exc:  # noqa: BLE001 - CLI should report load failures clearly.
        return SourceRegistryValidationResult(
            path=registry_path,
            entries_checked=0,
            errors=(
                SourceRegistryValidationError(
                    entry="<file>",
                    field="<load>",
                    message=str(exc),
                ),
            ),
        )

    entries = _extract_entries(payload)
    errors = validate_source_registry(payload if isinstance(payload, dict) else {})
    return SourceRegistryValidationResult(
        path=registry_path,
        entries_checked=len(entries) if not errors or entries else 0,
        errors=tuple(errors),
    )


def _extract_entries(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict) and isinstance(payload.get("sources"), list):
        return [entry for entry in payload["sources"] if isinstance(entry, dict)]
    if isinstance(payload, dict) and "source_id" in payload:
        return [payload]
    return []


def _entry_name(entry: dict[str, Any], index: int) -> str:
    value = entry.get("source_id")
    if isinstance(value, str) and value:
        return value
    return f"entry[{index}]"


def _validate_entry(
    entry: dict[str, Any],
    name: str,
) -> list[SourceRegistryValidationError]:
    errors: list[SourceRegistryValidationError] = []

    missing = sorted(REQUIRED_SOURCE_FIELDS.difference(entry))
    for field_name in missing:
        errors.append(
            SourceRegistryValidationError(
                entry=name,
                field=field_name,
                message="Required field is missing.",
            )
        )

    _validate_enum(
        errors=errors,
        entry=name,
        field="priority",
        value=entry.get("priority"),
        allowed=ALLOWED_PRIORITIES,
    )
    _validate_enum(
        errors=errors,
        entry=name,
        field="current_status",
        value=entry.get("current_status"),
        allowed=ALLOWED_CURRENT_STATUSES,
    )
    _validate_enum(
        errors=errors,
        entry=name,
        field="acquisition_mode",
        value=entry.get("acquisition_mode"),
        allowed=ALLOWED_ACQUISITION_MODES,
    )

    for field_name in ("benchmark_mapping", "limitations"):
        value = entry.get(field_name)
        if value is not None and not isinstance(value, list):
            errors.append(
                SourceRegistryValidationError(
                    entry=name,
                    field=field_name,
                    message=f"{field_name} must be a list.",
                )
            )

    return errors


def _validate_enum(
    *,
    errors: list[SourceRegistryValidationError],
    entry: str,
    field: str,
    value: Any,
    allowed: frozenset[str],
) -> None:
    if value in allowed:
        return

    errors.append(
        SourceRegistryValidationError(
            entry=entry,
            field=field,
            message=f"{field} must be one of: " + ", ".join(sorted(allowed)),
        )
    )
