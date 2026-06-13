"""Run manifest YAML validation and deterministic Markdown generation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only without PyYAML installed.
    yaml = None  # type: ignore[assignment]


DEFAULT_RUN_MANIFEST_DIR = Path("run_manifests")
DEFAULT_GENERATED_RUN_MANIFEST_DIR = Path("docs/examples/generated/run_manifests")

REQUIRED_RUN_MANIFEST_FIELDS = frozenset(
    {
        "run_id",
        "run_type",
        "generated_at",
        "artifact_status",
        "benchmark_ids",
        "dataset_ids",
        "source_ids",
        "acquisition_manifest_ids",
        "commands",
        "generated_artifacts",
        "validation_steps",
        "provenance_summary",
        "claim_boundary",
        "limitations",
        "non_claims",
        "next_action",
    }
)

ALLOWED_RUN_TYPES = frozenset(
    {
        "artifact-generation-example",
        "validation-example",
        "benchmark-dry-run-example",
    }
)

ALLOWED_ARTIFACT_STATUSES = frozenset(
    {
        "example-metadata-artifact",
        "generated-local-artifact",
        "validation-only-artifact",
    }
)

REQUIRED_NON_CLAIMS = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no model performance claim",
)

LIST_FIELDS = (
    "benchmark_ids",
    "dataset_ids",
    "source_ids",
    "acquisition_manifest_ids",
    "commands",
    "generated_artifacts",
    "validation_steps",
    "limitations",
    "non_claims",
)


@dataclass(frozen=True, slots=True)
class RunManifestValidationResult:
    """Validation outcome for one run manifest YAML file."""

    path: Path
    run_id: str
    errors: tuple[str, ...] = field(default_factory=tuple)

    @property
    def passed(self) -> bool:
        """Return True when the run manifest has no validation errors."""
        return not self.errors


@dataclass(frozen=True, slots=True)
class RunManifestGenerationResult:
    """Structured result for one generated run manifest Markdown file."""

    input_path: Path
    output_path: Path
    run_id: str
    passed: bool
    message: str


@dataclass(frozen=True, slots=True)
class RunManifestBatchResult:
    """Structured result for validating or generating multiple run manifests."""

    input_dir: Path
    output_dir: Path | None
    results: tuple[RunManifestValidationResult | RunManifestGenerationResult, ...]
    passed: bool
    message: str


def load_run_manifest_yaml(path: str | Path) -> Any:
    """Load a local run manifest YAML file."""
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to validate run manifest YAML files. "
            "Install PyYAML or run in the project environment that provides it."
        )

    manifest_path = Path(path)
    with manifest_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_run_manifest(manifest: dict[str, Any]) -> list[str]:
    """Validate one run manifest mapping and return validation messages."""
    name = _entry_name(manifest)
    errors: list[str] = []

    missing = sorted(REQUIRED_RUN_MANIFEST_FIELDS.difference(manifest))
    for field_name in missing:
        errors.append(f"{name}.{field_name}: Required field is missing.")

    _validate_enum(
        errors=errors,
        entry=name,
        field="run_type",
        value=manifest.get("run_type"),
        allowed=ALLOWED_RUN_TYPES,
    )
    _validate_enum(
        errors=errors,
        entry=name,
        field="artifact_status",
        value=manifest.get("artifact_status"),
        allowed=ALLOWED_ARTIFACT_STATUSES,
    )

    for field_name in LIST_FIELDS:
        value = manifest.get(field_name)
        if value is not None and not isinstance(value, list):
            errors.append(f"{name}.{field_name}: {field_name} must be a list.")

    non_claims = manifest.get("non_claims")
    if isinstance(non_claims, list):
        missing_non_claims = [
            claim for claim in REQUIRED_NON_CLAIMS if claim not in non_claims
        ]
        for claim in missing_non_claims:
            errors.append(f"{name}.non_claims: Missing required non-claim: {claim}.")

    for field_name in (
        "run_id",
        "generated_at",
        "provenance_summary",
        "claim_boundary",
        "next_action",
    ):
        value = manifest.get(field_name)
        if value is not None and not isinstance(value, str):
            errors.append(f"{name}.{field_name}: {field_name} must be a string.")

    return errors


def validate_run_manifest_file(path: str | Path) -> RunManifestValidationResult:
    """Validate one run manifest YAML file."""
    manifest_path = Path(path)
    try:
        payload = load_run_manifest_yaml(manifest_path)
    except Exception as exc:  # noqa: BLE001 - CLI should report load failures clearly.
        return RunManifestValidationResult(
            path=manifest_path,
            run_id="<invalid>",
            errors=(f"<file>.<load>: {exc}",),
        )

    if not isinstance(payload, dict):
        return RunManifestValidationResult(
            path=manifest_path,
            run_id="<invalid>",
            errors=("<file>.<payload>: Run manifest YAML must contain one mapping.",),
        )

    return RunManifestValidationResult(
        path=manifest_path,
        run_id=_entry_name(payload),
        errors=tuple(validate_run_manifest(payload)),
    )


def validate_run_manifest_dir(input_dir: str | Path) -> RunManifestBatchResult:
    """Validate every run manifest YAML file in a directory."""
    source_dir = Path(input_dir)
    results = tuple(
        validate_run_manifest_file(manifest_path)
        for manifest_path in sorted(source_dir.glob("*.yaml"))
    )

    failed = [result for result in results if not result.passed]
    if failed:
        details = "; ".join(error for result in failed for error in result.errors)
        return RunManifestBatchResult(
            input_dir=source_dir,
            output_dir=None,
            results=results,
            passed=False,
            message=details,
        )

    return RunManifestBatchResult(
        input_dir=source_dir,
        output_dir=None,
        results=results,
        passed=True,
        message=f"Validated {len(results)} run manifest(s).",
    )


def render_run_manifest(manifest: dict[str, Any]) -> str:
    """Render one validated run manifest as deterministic Markdown."""
    run_id = _required_string(manifest, "run_id")

    sections = [
        f"# Run Manifest: {run_id}",
        "",
        "> Generated from Permea run-manifest metadata. This public-safe example records metadata only: no dataset downloaded, no acquisition executed, no redistribution rights confirmed, no wet-lab validation by Permea, and no model performance claim.",
        "",
        "## Run ID",
        "",
        run_id,
        "",
        "## Run Type",
        "",
        _required_string(manifest, "run_type"),
        "",
        "## Generated At",
        "",
        _required_string(manifest, "generated_at"),
        "",
        "## Artifact Status",
        "",
        _required_string(manifest, "artifact_status"),
        "",
        "## Benchmark IDs",
        "",
        _render_list(manifest.get("benchmark_ids")),
        "",
        "## Dataset IDs",
        "",
        _render_list(manifest.get("dataset_ids")),
        "",
        "## Source IDs",
        "",
        _render_list(manifest.get("source_ids")),
        "",
        "## Acquisition Manifest IDs",
        "",
        _render_list(manifest.get("acquisition_manifest_ids")),
        "",
        "## Commands",
        "",
        _render_list(manifest.get("commands")),
        "",
        "## Generated Artifacts",
        "",
        _render_list(manifest.get("generated_artifacts")),
        "",
        "## Validation Steps",
        "",
        _render_list(manifest.get("validation_steps")),
        "",
        "## Provenance Summary",
        "",
        _required_string(manifest, "provenance_summary"),
        "",
        "## Explicit Non-Claims",
        "",
        _render_list(manifest.get("non_claims")),
        "",
        "## Claim Boundary",
        "",
        _required_string(manifest, "claim_boundary"),
        "",
        "## Limitations",
        "",
        _render_list(manifest.get("limitations")),
        "",
        "## Next Action",
        "",
        _required_string(manifest, "next_action"),
        "",
    ]
    return "\n".join(sections)


def generate_run_manifest_file(
    input_path: str | Path,
    output_path: str | Path,
) -> RunManifestGenerationResult:
    """Validate one run manifest YAML file and write its Markdown rendering."""
    manifest_path = Path(input_path)
    output = Path(output_path)

    validation = validate_run_manifest_file(manifest_path)
    if not validation.passed:
        return RunManifestGenerationResult(
            input_path=manifest_path,
            output_path=output,
            run_id=validation.run_id,
            passed=False,
            message="Run manifest validation failed: " + "; ".join(validation.errors),
        )

    payload = load_run_manifest_yaml(manifest_path)
    if not isinstance(payload, dict):
        return RunManifestGenerationResult(
            input_path=manifest_path,
            output_path=output,
            run_id="<invalid>",
            passed=False,
            message="Run manifest YAML must contain one mapping.",
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_run_manifest(payload), encoding="utf-8")
    return RunManifestGenerationResult(
        input_path=manifest_path,
        output_path=output,
        run_id=_required_string(payload, "run_id"),
        passed=True,
        message="Generated run manifest.",
    )


def generate_run_manifests(
    input_dir: str | Path,
    output_dir: str | Path,
) -> RunManifestBatchResult:
    """Generate Markdown run manifests for every YAML manifest in a directory."""
    source_dir = Path(input_dir)
    destination = Path(output_dir)
    results: list[RunManifestGenerationResult] = []

    for manifest_path in sorted(source_dir.glob("*.yaml")):
        payload = load_run_manifest_yaml(manifest_path)
        run_id = (
            payload.get("run_id")
            if isinstance(payload, dict) and isinstance(payload.get("run_id"), str)
            else manifest_path.stem
        )
        results.append(
            generate_run_manifest_file(manifest_path, destination / f"{run_id}.md")
        )

    failed = [result for result in results if not result.passed]
    if failed:
        return RunManifestBatchResult(
            input_dir=source_dir,
            output_dir=destination,
            results=tuple(results),
            passed=False,
            message="; ".join(result.message for result in failed),
        )

    destination.mkdir(parents=True, exist_ok=True)
    _write_index(destination, results)
    return RunManifestBatchResult(
        input_dir=source_dir,
        output_dir=destination,
        results=tuple(results),
        passed=True,
        message=f"Generated {len(results)} run manifest(s).",
    )


def _write_index(
    output_dir: Path,
    results: list[RunManifestGenerationResult],
) -> None:
    lines = [
        "# Generated Run Manifests",
        "",
        "These public-safe examples are generated from run-manifest metadata.",
        "",
        "They record metadata only: no dataset downloaded, no acquisition executed, no redistribution rights confirmed, no wet-lab validation by Permea, and no model performance claim.",
        "",
    ]
    for result in results:
        lines.append(f"- [{result.run_id}]({result.run_id}.md)")
    lines.append("")
    output_dir.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")


def _entry_name(manifest: dict[str, Any]) -> str:
    value = manifest.get("run_id")
    if isinstance(value, str) and value:
        return value
    return "<run_manifest>"


def _required_string(manifest: dict[str, Any], field: str) -> str:
    value = manifest[field]
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string.")
    return value


def _validate_enum(
    *,
    errors: list[str],
    entry: str,
    field: str,
    value: Any,
    allowed: frozenset[str],
) -> None:
    if value in allowed:
        return
    errors.append(f"{entry}.{field}: {field} must be one of: " + ", ".join(sorted(allowed)))


def _render_list(value: Any) -> str:
    if not isinstance(value, list) or not value:
        return "- not specified"
    return "\n".join(f"- {item}" for item in value)
