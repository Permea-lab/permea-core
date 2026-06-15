"""Deterministic public-safe evidence matrix generation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
DEFAULT_EVIDENCE_MATRIX_OUTPUT_DIR = Path("docs/examples/generated")
DEFAULT_EVIDENCE_MATRIX_JSON = "EVIDENCE_MATRIX.json"
DEFAULT_EVIDENCE_MATRIX_MARKDOWN = "EVIDENCE_MATRIX.md"
MATRIX_ID = "permea_core_public_evidence_matrix"
MATRIX_TYPE = "public-evidence-matrix"
GENERATED_AT = "example-generated"

COMMANDS: tuple[tuple[str, str], ...] = (
    ("source registry validation", "python3 scripts/validate_source_registry.py"),
    ("dataset card generation", "python3 scripts/generate_dataset_cards.py"),
    ("acquisition manifest generation", "python3 scripts/generate_acquisition_manifests.py"),
    ("benchmark registry validation", "python3 scripts/validate_benchmark_registry.py"),
    ("benchmark card generation", "python3 scripts/generate_benchmark_card.py"),
    ("evidence card generation", "python3 scripts/generate_evidence_cards.py"),
    ("output package generation", "python3 scripts/generate_output_package.py"),
    ("run manifest generation", "python3 scripts/generate_run_manifests.py"),
    ("artifact index generation", "python3 scripts/generate_artifact_index.py"),
    ("demo packet generation", "python3 scripts/generate_demo_packet.py"),
    ("benchmark dry-run orchestration", "python3 scripts/run_permea_dry_run.py"),
    ("unified generation", "python3 scripts/generate_permea_artifacts.py"),
    ("unified validation", "python3 scripts/validate_permea_artifacts.py"),
)

CAPABILITY_ROWS: tuple[tuple[str, str, tuple[str, ...], str], ...] = (
    (
        "source registry validation",
        "Validates public source registry structure and entries.",
        ("sources/registry.yaml",),
        "Keep source records aligned with dataset and benchmark metadata.",
    ),
    (
        "dataset card generation",
        "Generates public dataset-card examples from local metadata.",
        ("docs/examples/generated/dataset_cards/b3pred_dataset3.md",),
        "Add richer review status and source limitations as cards mature.",
    ),
    (
        "acquisition manifest generation",
        "Generates public acquisition-plan metadata without executing acquisition.",
        ("docs/examples/generated/acquisition_manifests/b3pred_dataset3.md",),
        "Add acquisition readiness checks only after access and release policy are reviewed.",
    ),
    (
        "benchmark registry validation",
        "Validates benchmark task registry metadata.",
        ("benchmarks/registry.yaml",),
        "Keep task definitions tied to explicit labels, metrics, splits, and limitations.",
    ),
    (
        "benchmark card generation",
        "Generates benchmark-card examples for reviewable task definitions.",
        ("docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md",),
        "Expand cards as benchmark contracts stabilize.",
    ),
    (
        "evidence card generation",
        "Generates structured public evidence-card examples.",
        ("docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json",),
        "Add evidence review status and uncertainty fields as source coverage grows.",
    ),
    (
        "output package generation",
        "Generates deterministic output-package examples for benchmark review.",
        ("docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml",),
        "Connect future benchmark outputs to the same package shape.",
    ),
    (
        "run manifest generation",
        "Generates reproducibility records for local artifact generation.",
        ("docs/examples/generated/run_manifests/example_artifact_generation.md",),
        "Keep manifest fields aligned with generated artifacts and command coverage.",
    ),
    (
        "artifact index generation",
        "Generates a public index of current registry inputs and generated artifacts.",
        ("docs/examples/generated/ARTIFACT_INDEX.md",),
        "Add new artifact families only after generator and validation coverage exist.",
    ),
    (
        "demo packet generation",
        "Generates a public entry point for inspecting current artifact-system outputs.",
        ("docs/examples/generated/DEMO_PACKET.md", "docs/examples/generated/DEMO_PACKET.json"),
        "Keep the packet refreshed as new generated entry points are added.",
    ),
    (
        "benchmark dry-run orchestration",
        "Runs local metadata checks and example generators for a deterministic dry-run report.",
        (
            "docs/examples/generated/dry_runs/example_benchmark_dry_run.md",
            "docs/examples/generated/dry_runs/example_benchmark_dry_run.json",
        ),
        "Add broader dry-run coverage only after public-safe task contracts are stable.",
    ),
    (
        "unified generation",
        "Runs current deterministic artifact generators through one local command.",
        ("scripts/generate_permea_artifacts.py",),
        "Integrate the evidence matrix into unified generation in a later bounded run.",
    ),
    (
        "unified validation",
        "Runs current local validation and generation checks through one command.",
        ("scripts/validate_permea_artifacts.py",),
        "Integrate evidence-matrix presence checks in a later bounded run.",
    ),
)

ARTIFACT_EVIDENCE: tuple[tuple[str, str], ...] = (
    ("public demo packet", "docs/examples/generated/DEMO_PACKET.md"),
    ("public demo packet JSON", "docs/examples/generated/DEMO_PACKET.json"),
    ("public artifact index", "docs/examples/generated/ARTIFACT_INDEX.md"),
    ("public evaluation packet", "docs/examples/generated/EVALUATION_PACKET.md"),
    ("public reproducibility report", "docs/examples/generated/REPRODUCIBILITY_REPORT.md"),
    ("benchmark dry-run report", "docs/examples/generated/dry_runs/example_benchmark_dry_run.md"),
    ("benchmark dry-run JSON", "docs/examples/generated/dry_runs/example_benchmark_dry_run.json"),
    ("benchmark card example", "docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md"),
    ("dataset card example", "docs/examples/generated/dataset_cards/b3pred_dataset3.md"),
    ("acquisition manifest example", "docs/examples/generated/acquisition_manifests/b3pred_dataset3.md"),
    ("evidence card example", "docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json"),
    ("output package manifest", "docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml"),
    ("output package metrics metadata", "docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json"),
    ("output package ranking metadata", "docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv"),
    ("run manifest example", "docs/examples/generated/run_manifests/example_artifact_generation.md"),
)

EXPLICIT_NON_CLAIMS: tuple[str, ...] = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no clinical-effectiveness claim",
    "no model performance claim",
    "no state-of-the-art claim",
    "no solved-delivery claim",
)

LIMITATIONS: tuple[str, ...] = (
    "This matrix is generated from repository metadata, generated examples, and local commands only.",
    "It maps implemented artifact infrastructure, not biological or therapeutic performance.",
    "It does not load datasets, run acquisition, call external services, run ML, or score candidates.",
    "It records evidence boundaries for current public artifacts and does not expand scientific claims.",
)


def collect_evidence_matrix(root_path: str | Path = ".") -> dict[str, Any]:
    """Collect deterministic public evidence matrix metadata."""
    root = Path(root_path).resolve()
    implemented_capabilities = [
        {
            "capability": capability,
            "current_evidence_boundary": boundary,
            "artifact_paths": list(paths),
            "command": _command_for(capability),
            "next_evidence_step": next_step,
            "artifact_status": _artifact_status(root, paths),
        }
        for capability, boundary, paths, next_step in CAPABILITY_ROWS
    ]
    matrix = {
        "matrix_id": MATRIX_ID,
        "matrix_type": MATRIX_TYPE,
        "generated_at": GENERATED_AT,
        "status": PASS,
        "overview": (
            "This public evidence matrix maps current Permea Core artifact "
            "capabilities to generated artifacts, reproducible local commands, "
            "validation evidence, explicit non-claims, limitations, and next "
            "evidence steps."
        ),
        "implemented_capabilities": implemented_capabilities,
        "artifact_evidence": _existing_path_items(root, ARTIFACT_EVIDENCE),
        "command_evidence": [
            {"label": label, "command": command} for label, command in COMMANDS
        ],
        "validation_evidence": [
            {"label": "artifact validation", "command": "python3 scripts/validate_permea_artifacts.py"},
            {"label": "unified generation", "command": "python3 scripts/generate_permea_artifacts.py"},
            {"label": "demo packet generation", "command": "python3 scripts/generate_demo_packet.py"},
            {"label": "benchmark dry-run", "command": "python3 scripts/run_permea_dry_run.py"},
        ],
        "explicit_non_claims": list(EXPLICIT_NON_CLAIMS),
        "limitations": list(LIMITATIONS),
        "next_evidence_steps": [
            "Integrate this matrix into unified generation in a later bounded run.",
            "Add validation coverage for matrix file presence in a later bounded run.",
            "Keep new public claims tied to generated artifacts, commands, limitations, and non-claims.",
        ],
    }
    _assert_public_relative_matrix(matrix)
    return matrix


def render_evidence_matrix(matrix: dict[str, Any]) -> str:
    """Render an evidence matrix as public-safe Markdown."""
    lines = [
        "# Permea Core Public Evidence Matrix",
        "",
        "## Overview",
        "",
        matrix["overview"],
        "",
        f"- Matrix ID: `{matrix['matrix_id']}`",
        f"- Matrix type: `{matrix['matrix_type']}`",
        f"- Generated at: `{matrix['generated_at']}`",
        f"- Status: `{matrix['status']}`",
        "",
        "## Implemented Capabilities",
        "",
        "| Capability | Current evidence boundary | Artifact evidence | Command | Next evidence step |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in matrix["implemented_capabilities"]:
        artifact_links = "<br>".join(f"[{path}]({path})" for path in row["artifact_paths"])
        next_step = row["next_evidence_step"]
        if row["capability"] == "unified generation":
            next_step = "Keep public evidence-surface generators included as new generated surfaces are added."
        elif row["capability"] == "unified validation":
            next_step = "Keep public evidence-surface presence covered by local validation."
        lines.append(
            "| "
            f"{row['capability']} | "
            f"{row['current_evidence_boundary']} | "
            f"{artifact_links} | "
            f"`{row['command']}` | "
            f"{next_step} |"
        )

    lines.extend(["", "## Artifact Evidence", ""])
    lines.extend(_render_path_items(matrix["artifact_evidence"]))
    lines.extend(["", "## Related Evidence Surfaces", ""])
    lines.extend(
        [
            "- generated evidence surface: [README.md](README.md)",
            "- public demo packet: [DEMO_PACKET.md](DEMO_PACKET.md)",
            "- public artifact index: [ARTIFACT_INDEX.md](ARTIFACT_INDEX.md)",
            "- public evaluation packet: [EVALUATION_PACKET.md](EVALUATION_PACKET.md)",
            "- public reproducibility report: [REPRODUCIBILITY_REPORT.md](REPRODUCIBILITY_REPORT.md)",
            "- benchmark dry-run report: [dry_runs/example_benchmark_dry_run.md](dry_runs/example_benchmark_dry_run.md)",
        ]
    )
    lines.extend(["", "## Command Evidence", ""])
    lines.extend(
        f"- {item['label']}: `{item['command']}`"
        for item in matrix["command_evidence"]
    )
    lines.extend(["", "## Validation Evidence", ""])
    lines.extend(
        f"- {item['label']}: `{item['command']}`"
        for item in matrix["validation_evidence"]
    )
    lines.extend(["", "## Explicit Non-Claims", ""])
    lines.extend(f"- {claim}" for claim in matrix["explicit_non_claims"])
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {limitation}" for limitation in matrix["limitations"])
    lines.extend(["", "## Next Evidence Steps", ""])
    lines.extend(
        [
            "- Keep this matrix connected to the generated evidence surface, demo packet, artifact index, and dry-run report.",
            "- Keep unified generation and validation coverage aligned with new generated evidence surfaces.",
            "- Keep new public claims tied to generated artifacts, commands, limitations, and non-claims.",
        ]
    )
    lines.append("")
    return "\n".join(lines)


def write_evidence_matrix(
    output_dir: str | Path = DEFAULT_EVIDENCE_MATRIX_OUTPUT_DIR,
    root_path: str | Path | None = None,
) -> dict[str, Any]:
    """Write deterministic evidence matrix Markdown and JSON outputs."""
    root = Path(root_path).resolve() if root_path is not None else ROOT
    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination
    destination.mkdir(parents=True, exist_ok=True)

    matrix = collect_evidence_matrix(root)
    markdown_path = destination / DEFAULT_EVIDENCE_MATRIX_MARKDOWN
    json_path = destination / DEFAULT_EVIDENCE_MATRIX_JSON
    output_paths = {
        "markdown": _display_path(root, markdown_path),
        "json": _display_path(root, json_path),
    }
    matrix_with_outputs = {**matrix, "output_paths": output_paths}

    markdown_path.write_text(render_evidence_matrix(matrix_with_outputs), encoding="utf-8")
    json_path.write_text(
        json.dumps(matrix_with_outputs, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    return matrix_with_outputs


def _command_for(capability: str) -> str:
    return dict(COMMANDS)[capability]


def _artifact_status(root: Path, paths: tuple[str, ...]) -> str:
    return PASS if all((root / path).exists() for path in paths) else "MISSING"


def _existing_path_items(
    root: Path,
    items: tuple[tuple[str, str], ...],
) -> list[dict[str, Any]]:
    return [
        {"label": label, "path": path, "exists": (root / path).exists()}
        for label, path in items
    ]


def _render_path_items(items: list[dict[str, Any]]) -> list[str]:
    return [
        f"- {item['label']}: [{item['path']}]({item['path']})"
        f" ({'present' if item.get('exists') else 'missing'})"
        for item in items
    ]


def _assert_public_relative_matrix(value: Any) -> None:
    if isinstance(value, dict):
        for nested in value.values():
            _assert_public_relative_matrix(nested)
    elif isinstance(value, list):
        for nested in value:
            _assert_public_relative_matrix(nested)
    elif isinstance(value, str):
        if str(ROOT) in value or value.startswith("/"):
            raise ValueError(f"non-public or absolute path in evidence matrix: {value}")


def _display_path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.name
