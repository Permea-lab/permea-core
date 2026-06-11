"""Dataset card YAML validation and Markdown generation for Permea Core."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only without PyYAML installed.
    yaml = None  # type: ignore[assignment]


DEFAULT_DATASET_CARD_DIR = Path("dataset_cards")
DEFAULT_GENERATED_DATASET_CARD_DIR = Path("docs/examples/generated/dataset_cards")

REQUIRED_DATASET_CARD_FIELDS = frozenset(
    {
        "dataset_id",
        "dataset_name",
        "source_ids",
        "benchmark_ids",
        "delivery_axis",
        "biological_scope",
        "expected_data_type",
        "label_type",
        "acquisition_status",
        "license_access_status",
        "redistribution_status",
        "provenance_requirements",
        "split_policy",
        "known_limitations",
        "claim_boundary",
        "next_action",
    }
)

ALLOWED_ACQUISITION_STATUSES = frozenset(
    {
        "source-carded",
        "access-to-verify",
        "acquisition-planned",
        "acquisition-script-planned",
        "no-redistribution-source-card-only",
        "benchmark-mapped",
    }
)

ALLOWED_REDISTRIBUTION_STATUSES = frozenset(
    {
        "not-reviewed",
        "not-confirmed",
        "no-redistribution",
        "metadata-only",
        "redistribution-to-verify",
    }
)

NON_CLAIMS = (
    "no dataset downloaded",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
)


@dataclass(frozen=True, slots=True)
class DatasetCardValidationError:
    """Structured validation error for one dataset card."""

    entry: str
    field: str
    message: str


@dataclass(frozen=True, slots=True)
class DatasetCardValidationResult:
    """Validation outcome for one dataset card YAML file."""

    path: Path
    dataset_id: str
    errors: tuple[DatasetCardValidationError, ...] = field(default_factory=tuple)

    @property
    def passed(self) -> bool:
        """Return True when the dataset card has no validation errors."""
        return not self.errors


@dataclass(frozen=True, slots=True)
class DatasetCardGenerationResult:
    """Structured result for one generated dataset card file."""

    input_path: Path
    output_path: Path
    dataset_id: str
    passed: bool
    message: str


@dataclass(frozen=True, slots=True)
class DatasetCardBatchResult:
    """Structured result for generating multiple dataset card files."""

    input_dir: Path
    output_dir: Path
    generated: tuple[DatasetCardGenerationResult, ...]
    passed: bool
    message: str


def load_dataset_card_yaml(path: str | Path) -> Any:
    """Load a local dataset card YAML file."""
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to validate dataset card YAML files. "
            "Install PyYAML or run in the project environment that provides it."
        )

    card_path = Path(path)
    with card_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_dataset_card(card: dict[str, Any]) -> list[DatasetCardValidationError]:
    """Validate one dataset card mapping and return structured errors."""
    name = _entry_name(card)
    errors: list[DatasetCardValidationError] = []

    missing = sorted(REQUIRED_DATASET_CARD_FIELDS.difference(card))
    for field_name in missing:
        errors.append(
            DatasetCardValidationError(
                entry=name,
                field=field_name,
                message="Required field is missing.",
            )
        )

    _validate_enum(
        errors=errors,
        entry=name,
        field="acquisition_status",
        value=card.get("acquisition_status"),
        allowed=ALLOWED_ACQUISITION_STATUSES,
    )
    _validate_enum(
        errors=errors,
        entry=name,
        field="redistribution_status",
        value=card.get("redistribution_status"),
        allowed=ALLOWED_REDISTRIBUTION_STATUSES,
    )

    for field_name in (
        "source_ids",
        "benchmark_ids",
        "provenance_requirements",
        "known_limitations",
    ):
        value = card.get(field_name)
        if value is not None and not isinstance(value, list):
            errors.append(
                DatasetCardValidationError(
                    entry=name,
                    field=field_name,
                    message=f"{field_name} must be a list.",
                )
            )

    if card.get("split_policy") is not None and not isinstance(
        card.get("split_policy"), dict
    ):
        errors.append(
            DatasetCardValidationError(
                entry=name,
                field="split_policy",
                message="split_policy must be a mapping.",
            )
        )

    return errors


def validate_dataset_card_file(path: str | Path) -> DatasetCardValidationResult:
    """Validate one dataset card YAML file."""
    card_path = Path(path)
    try:
        payload = load_dataset_card_yaml(card_path)
    except Exception as exc:  # noqa: BLE001 - CLI should report load failures clearly.
        return DatasetCardValidationResult(
            path=card_path,
            dataset_id="<invalid>",
            errors=(
                DatasetCardValidationError(
                    entry="<file>",
                    field="<load>",
                    message=str(exc),
                ),
            ),
        )

    if not isinstance(payload, dict):
        return DatasetCardValidationResult(
            path=card_path,
            dataset_id="<invalid>",
            errors=(
                DatasetCardValidationError(
                    entry="<file>",
                    field="<payload>",
                    message="Dataset card YAML must contain one mapping.",
                ),
            ),
        )

    return DatasetCardValidationResult(
        path=card_path,
        dataset_id=_entry_name(payload),
        errors=tuple(validate_dataset_card(payload)),
    )


def render_dataset_card(card: dict[str, Any]) -> str:
    """Render one validated dataset card as deterministic Markdown."""
    dataset_id = _required_string(card, "dataset_id")
    dataset_name = _required_string(card, "dataset_name")

    sections = [
        f"# Dataset Card: {dataset_name}",
        "",
        "> Generated from Permea dataset-card metadata. This public-safe example records metadata only: no dataset downloaded, no redistribution rights confirmed, and no wet-lab validation by Permea.",
        "",
        "## Dataset ID",
        "",
        dataset_id,
        "",
        "## Source IDs",
        "",
        _render_list(card.get("source_ids")),
        "",
        "## Benchmark IDs",
        "",
        _render_list(card.get("benchmark_ids")),
        "",
        "## Delivery Axis",
        "",
        _required_string(card, "delivery_axis"),
        "",
        "## Biological Scope",
        "",
        _required_string(card, "biological_scope"),
        "",
        "## Expected Data Type",
        "",
        _required_string(card, "expected_data_type"),
        "",
        "## Label Type",
        "",
        _required_string(card, "label_type"),
        "",
        "## Acquisition Status",
        "",
        _required_string(card, "acquisition_status"),
        "",
        "## License / Access Status",
        "",
        _required_string(card, "license_access_status"),
        "",
        "## Redistribution Status",
        "",
        _required_string(card, "redistribution_status"),
        "",
        "## Provenance Requirements",
        "",
        _render_list(card.get("provenance_requirements")),
        "",
        "## Split Policy",
        "",
        _render_mapping(card.get("split_policy")),
        "",
        "## Known Limitations",
        "",
        _render_list(card.get("known_limitations")),
        "",
        "## Explicit Non-Claims",
        "",
        _render_list(list(NON_CLAIMS)),
        "",
        "## Claim Boundary",
        "",
        _required_string(card, "claim_boundary"),
        "",
        "## Next Action",
        "",
        _required_string(card, "next_action"),
        "",
    ]
    return "\n".join(sections)


def generate_dataset_card_file(
    input_path: str | Path,
    output_path: str | Path,
) -> DatasetCardGenerationResult:
    """Validate one dataset card YAML file and write its Markdown card."""
    card_path = Path(input_path)
    output = Path(output_path)

    validation = validate_dataset_card_file(card_path)
    if not validation.passed:
        return DatasetCardGenerationResult(
            input_path=card_path,
            output_path=output,
            dataset_id=validation.dataset_id,
            passed=False,
            message=_format_validation_failure(validation.errors),
        )

    payload = load_dataset_card_yaml(card_path)
    if not isinstance(payload, dict):
        return DatasetCardGenerationResult(
            input_path=card_path,
            output_path=output,
            dataset_id="<invalid>",
            passed=False,
            message="Dataset card YAML must contain one mapping.",
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_dataset_card(payload), encoding="utf-8")
    return DatasetCardGenerationResult(
        input_path=card_path,
        output_path=output,
        dataset_id=_required_string(payload, "dataset_id"),
        passed=True,
        message="Generated dataset card.",
    )


def generate_dataset_cards(
    input_dir: str | Path,
    output_dir: str | Path,
) -> DatasetCardBatchResult:
    """Generate Markdown cards for every YAML card in an input directory."""
    source_dir = Path(input_dir)
    destination = Path(output_dir)
    results: list[DatasetCardGenerationResult] = []

    for card_path in sorted(source_dir.glob("*.yaml")):
        payload = load_dataset_card_yaml(card_path)
        dataset_id = (
            payload.get("dataset_id")
            if isinstance(payload, dict) and isinstance(payload.get("dataset_id"), str)
            else card_path.stem
        )
        results.append(
            generate_dataset_card_file(card_path, destination / f"{dataset_id}.md")
        )

    failed = [result for result in results if not result.passed]
    if failed:
        return DatasetCardBatchResult(
            input_dir=source_dir,
            output_dir=destination,
            generated=tuple(results),
            passed=False,
            message="; ".join(result.message for result in failed),
        )

    destination.mkdir(parents=True, exist_ok=True)
    _write_index(destination, results)
    return DatasetCardBatchResult(
        input_dir=source_dir,
        output_dir=destination,
        generated=tuple(results),
        passed=True,
        message=f"Generated {len(results)} dataset card(s).",
    )


def _write_index(
    output_dir: Path,
    results: list[DatasetCardGenerationResult],
) -> None:
    lines = [
        "# Generated Dataset Cards",
        "",
        "These public-safe examples are generated from dataset-card metadata.",
        "",
        "They record metadata only: no dataset downloaded, no redistribution rights confirmed, and no wet-lab validation by Permea.",
        "",
    ]
    for result in results:
        lines.append(f"- [{result.dataset_id}]({result.dataset_id}.md)")
    lines.append("")
    output_dir.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")


def _entry_name(card: dict[str, Any]) -> str:
    value = card.get("dataset_id")
    if isinstance(value, str) and value:
        return value
    return "<dataset_card>"


def _required_string(card: dict[str, Any], field: str) -> str:
    value = card[field]
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string.")
    return value


def _validate_enum(
    *,
    errors: list[DatasetCardValidationError],
    entry: str,
    field: str,
    value: Any,
    allowed: frozenset[str],
) -> None:
    if value in allowed:
        return
    errors.append(
        DatasetCardValidationError(
            entry=entry,
            field=field,
            message=f"{field} must be one of: " + ", ".join(sorted(allowed)),
        )
    )


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


def _format_validation_failure(
    errors: tuple[DatasetCardValidationError, ...],
) -> str:
    details = "; ".join(
        f"{error.entry}.{error.field}: {error.message}" for error in errors
    )
    return f"Dataset card validation failed: {details}"
