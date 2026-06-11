"""Acquisition manifest YAML validation and Markdown generation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only without PyYAML installed.
    yaml = None  # type: ignore[assignment]


DEFAULT_ACQUISITION_MANIFEST_DIR = Path("acquisition_manifests")
DEFAULT_GENERATED_ACQUISITION_MANIFEST_DIR = Path(
    "docs/examples/generated/acquisition_manifests"
)

REQUIRED_ACQUISITION_MANIFEST_FIELDS = frozenset(
    {
        "manifest_id",
        "dataset_id",
        "source_ids",
        "benchmark_ids",
        "acquisition_mode",
        "acquisition_status",
        "redistribution_status",
        "expected_local_outputs",
        "provenance_requirements",
        "license_review_required",
        "manual_review_required",
        "failure_modes",
        "fallback_strategy",
        "claim_boundary",
        "next_action",
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

ALLOWED_ACQUISITION_STATUSES = frozenset(
    {
        "source-carded",
        "access-to-verify",
        "license-to-verify",
        "acquisition-planned",
        "acquisition-script-planned",
        "no-redistribution-source-card-only",
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
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
)


@dataclass(frozen=True, slots=True)
class AcquisitionManifestValidationError:
    """Structured validation error for one acquisition manifest."""

    entry: str
    field: str
    message: str


@dataclass(frozen=True, slots=True)
class AcquisitionManifestValidationResult:
    """Validation outcome for one acquisition manifest YAML file."""

    path: Path
    manifest_id: str
    errors: tuple[AcquisitionManifestValidationError, ...] = field(default_factory=tuple)

    @property
    def passed(self) -> bool:
        """Return True when the acquisition manifest has no validation errors."""
        return not self.errors


@dataclass(frozen=True, slots=True)
class AcquisitionManifestGenerationResult:
    """Structured result for one generated acquisition manifest file."""

    input_path: Path
    output_path: Path
    manifest_id: str
    passed: bool
    message: str


@dataclass(frozen=True, slots=True)
class AcquisitionManifestBatchResult:
    """Structured result for generating multiple acquisition manifest files."""

    input_dir: Path
    output_dir: Path
    generated: tuple[AcquisitionManifestGenerationResult, ...]
    passed: bool
    message: str


def load_acquisition_manifest_yaml(path: str | Path) -> Any:
    """Load a local acquisition manifest YAML file."""
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to validate acquisition manifest YAML files. "
            "Install PyYAML or run in the project environment that provides it."
        )

    manifest_path = Path(path)
    with manifest_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_acquisition_manifest(
    manifest: dict[str, Any],
) -> list[AcquisitionManifestValidationError]:
    """Validate one acquisition manifest mapping and return structured errors."""
    name = _entry_name(manifest)
    errors: list[AcquisitionManifestValidationError] = []

    missing = sorted(REQUIRED_ACQUISITION_MANIFEST_FIELDS.difference(manifest))
    for field_name in missing:
        errors.append(
            AcquisitionManifestValidationError(
                entry=name,
                field=field_name,
                message="Required field is missing.",
            )
        )

    _validate_enum(
        errors=errors,
        entry=name,
        field="acquisition_mode",
        value=manifest.get("acquisition_mode"),
        allowed=ALLOWED_ACQUISITION_MODES,
    )
    _validate_enum(
        errors=errors,
        entry=name,
        field="acquisition_status",
        value=manifest.get("acquisition_status"),
        allowed=ALLOWED_ACQUISITION_STATUSES,
    )
    _validate_enum(
        errors=errors,
        entry=name,
        field="redistribution_status",
        value=manifest.get("redistribution_status"),
        allowed=ALLOWED_REDISTRIBUTION_STATUSES,
    )

    for field_name in (
        "source_ids",
        "benchmark_ids",
        "expected_local_outputs",
        "provenance_requirements",
        "failure_modes",
        "fallback_strategy",
    ):
        value = manifest.get(field_name)
        if value is not None and not isinstance(value, list):
            errors.append(
                AcquisitionManifestValidationError(
                    entry=name,
                    field=field_name,
                    message=f"{field_name} must be a list.",
                )
            )

    for field_name in ("license_review_required", "manual_review_required"):
        value = manifest.get(field_name)
        if value is not None and not isinstance(value, bool):
            errors.append(
                AcquisitionManifestValidationError(
                    entry=name,
                    field=field_name,
                    message=f"{field_name} must be a boolean.",
                )
            )

    return errors


def validate_acquisition_manifest_file(
    path: str | Path,
) -> AcquisitionManifestValidationResult:
    """Validate one acquisition manifest YAML file."""
    manifest_path = Path(path)
    try:
        payload = load_acquisition_manifest_yaml(manifest_path)
    except Exception as exc:  # noqa: BLE001 - CLI should report load failures clearly.
        return AcquisitionManifestValidationResult(
            path=manifest_path,
            manifest_id="<invalid>",
            errors=(
                AcquisitionManifestValidationError(
                    entry="<file>",
                    field="<load>",
                    message=str(exc),
                ),
            ),
        )

    if not isinstance(payload, dict):
        return AcquisitionManifestValidationResult(
            path=manifest_path,
            manifest_id="<invalid>",
            errors=(
                AcquisitionManifestValidationError(
                    entry="<file>",
                    field="<payload>",
                    message="Acquisition manifest YAML must contain one mapping.",
                ),
            ),
        )

    return AcquisitionManifestValidationResult(
        path=manifest_path,
        manifest_id=_entry_name(payload),
        errors=tuple(validate_acquisition_manifest(payload)),
    )


def render_acquisition_manifest(manifest: dict[str, Any]) -> str:
    """Render one validated acquisition manifest as deterministic Markdown."""
    manifest_id = _required_string(manifest, "manifest_id")
    dataset_id = _required_string(manifest, "dataset_id")

    sections = [
        f"# Acquisition Manifest: {manifest_id}",
        "",
        "> Generated from Permea acquisition-manifest metadata. This public-safe example records planning metadata only: no dataset downloaded, no acquisition executed, no redistribution rights confirmed, and no wet-lab validation by Permea.",
        "",
        "## Manifest ID",
        "",
        manifest_id,
        "",
        "## Dataset ID",
        "",
        dataset_id,
        "",
        "## Source IDs",
        "",
        _render_list(manifest.get("source_ids")),
        "",
        "## Benchmark IDs",
        "",
        _render_list(manifest.get("benchmark_ids")),
        "",
        "## Acquisition Mode",
        "",
        _required_string(manifest, "acquisition_mode"),
        "",
        "## Acquisition Status",
        "",
        _required_string(manifest, "acquisition_status"),
        "",
        "## Redistribution Status",
        "",
        _required_string(manifest, "redistribution_status"),
        "",
        "## Expected Local Outputs",
        "",
        _render_list(manifest.get("expected_local_outputs")),
        "",
        "## Provenance Requirements",
        "",
        _render_list(manifest.get("provenance_requirements")),
        "",
        "## Review Requirements",
        "",
        f"- license_review_required: {manifest.get('license_review_required')}",
        f"- manual_review_required: {manifest.get('manual_review_required')}",
        "",
        "## Failure Modes",
        "",
        _render_list(manifest.get("failure_modes")),
        "",
        "## Fallback Strategy",
        "",
        _render_list(manifest.get("fallback_strategy")),
        "",
        "## Explicit Non-Claims",
        "",
        _render_list(list(NON_CLAIMS)),
        "",
        "## Claim Boundary",
        "",
        _required_string(manifest, "claim_boundary"),
        "",
        "## Next Action",
        "",
        _required_string(manifest, "next_action"),
        "",
    ]
    return "\n".join(sections)


def generate_acquisition_manifest_file(
    input_path: str | Path,
    output_path: str | Path,
) -> AcquisitionManifestGenerationResult:
    """Validate one acquisition manifest YAML file and write its Markdown."""
    manifest_path = Path(input_path)
    output = Path(output_path)

    validation = validate_acquisition_manifest_file(manifest_path)
    if not validation.passed:
        return AcquisitionManifestGenerationResult(
            input_path=manifest_path,
            output_path=output,
            manifest_id=validation.manifest_id,
            passed=False,
            message=_format_validation_failure(validation.errors),
        )

    payload = load_acquisition_manifest_yaml(manifest_path)
    if not isinstance(payload, dict):
        return AcquisitionManifestGenerationResult(
            input_path=manifest_path,
            output_path=output,
            manifest_id="<invalid>",
            passed=False,
            message="Acquisition manifest YAML must contain one mapping.",
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_acquisition_manifest(payload), encoding="utf-8")
    return AcquisitionManifestGenerationResult(
        input_path=manifest_path,
        output_path=output,
        manifest_id=_required_string(payload, "manifest_id"),
        passed=True,
        message="Generated acquisition manifest.",
    )


def generate_acquisition_manifests(
    input_dir: str | Path,
    output_dir: str | Path,
) -> AcquisitionManifestBatchResult:
    """Generate Markdown manifests for every YAML manifest in an input directory."""
    source_dir = Path(input_dir)
    destination = Path(output_dir)
    results: list[AcquisitionManifestGenerationResult] = []

    for manifest_path in sorted(source_dir.glob("*.yaml")):
        payload = load_acquisition_manifest_yaml(manifest_path)
        dataset_id = (
            payload.get("dataset_id")
            if isinstance(payload, dict) and isinstance(payload.get("dataset_id"), str)
            else manifest_path.stem
        )
        results.append(
            generate_acquisition_manifest_file(
                manifest_path,
                destination / f"{dataset_id}.md",
            )
        )

    failed = [result for result in results if not result.passed]
    if failed:
        return AcquisitionManifestBatchResult(
            input_dir=source_dir,
            output_dir=destination,
            generated=tuple(results),
            passed=False,
            message="; ".join(result.message for result in failed),
        )

    destination.mkdir(parents=True, exist_ok=True)
    _write_index(destination, results)
    return AcquisitionManifestBatchResult(
        input_dir=source_dir,
        output_dir=destination,
        generated=tuple(results),
        passed=True,
        message=f"Generated {len(results)} acquisition manifest(s).",
    )


def _write_index(
    output_dir: Path,
    results: list[AcquisitionManifestGenerationResult],
) -> None:
    lines = [
        "# Generated Acquisition Manifests",
        "",
        "These public-safe examples are generated from acquisition-manifest metadata.",
        "",
        "They record planning metadata only: no dataset downloaded, no acquisition executed, no redistribution rights confirmed, and no wet-lab validation by Permea.",
        "",
    ]
    for result in results:
        dataset_id = result.output_path.stem
        lines.append(f"- [{dataset_id}]({dataset_id}.md)")
    lines.append("")
    output_dir.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")


def _entry_name(manifest: dict[str, Any]) -> str:
    value = manifest.get("manifest_id")
    if isinstance(value, str) and value:
        return value
    return "<acquisition_manifest>"


def _required_string(manifest: dict[str, Any], field: str) -> str:
    value = manifest[field]
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string.")
    return value


def _validate_enum(
    *,
    errors: list[AcquisitionManifestValidationError],
    entry: str,
    field: str,
    value: Any,
    allowed: frozenset[str],
) -> None:
    if value in allowed:
        return
    errors.append(
        AcquisitionManifestValidationError(
            entry=entry,
            field=field,
            message=f"{field} must be one of: " + ", ".join(sorted(allowed)),
        )
    )


def _render_list(value: Any) -> str:
    if not isinstance(value, list) or not value:
        return "- not specified"
    return "\n".join(f"- {item}" for item in value)


def _format_validation_failure(
    errors: tuple[AcquisitionManifestValidationError, ...],
) -> str:
    details = "; ".join(
        f"{error.entry}.{error.field}: {error.message}" for error in errors
    )
    return f"Acquisition manifest validation failed: {details}"
