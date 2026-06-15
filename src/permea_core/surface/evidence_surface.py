"""Deterministic public-safe generated evidence surface navigation."""

from __future__ import annotations

from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
DEFAULT_EVIDENCE_SURFACE_PATH = Path("docs/examples/generated/README.md")
SURFACE_ID = "permea_core_public_evidence_surface"
SURFACE_TYPE = "public-evidence-surface"
GENERATED_AT = "example-generated"

PRIMARY_ENTRY_POINTS: tuple[tuple[str, str, str], ...] = (
    (
        "Generated evidence surface",
        "README.md",
        "Reviewer-facing navigation for generated public artifacts.",
    ),
    (
        "Public demo packet",
        "DEMO_PACKET.md",
        "One generated entry point for inspecting the artifact system.",
    ),
    (
        "Public artifact index",
        "ARTIFACT_INDEX.md",
        "Generated inventory of registry inputs and artifact families.",
    ),
    (
        "Public evidence matrix",
        "EVIDENCE_MATRIX.md",
        "Generated mapping from implemented capabilities to evidence and commands.",
    ),
    (
        "Benchmark dry-run report",
        "dry_runs/example_benchmark_dry_run.md",
        "Generated dry-run output for local metadata and example artifacts.",
    ),
    (
        "Reproducibility report",
        "REPRODUCIBILITY_REPORT.md",
        "Generated report for reproduction commands, validation checks, lineage, and non-claims.",
    ),
)

ARTIFACT_FAMILIES: tuple[tuple[str, str, str], ...] = (
    ("Benchmark cards", "benchmark_cards/", "Generated benchmark task examples."),
    ("Dataset cards", "dataset_cards/", "Generated dataset metadata examples."),
    (
        "Acquisition manifests",
        "acquisition_manifests/",
        "Generated acquisition-plan metadata examples without executing acquisition.",
    ),
    ("Evidence cards", "evidence_cards/", "Generated structured evidence-card examples."),
    ("Output packages", "output_packages/", "Generated benchmark output package examples."),
    ("Run manifests", "run_manifests/", "Generated reproducibility record examples."),
)

REPRODUCIBILITY_COMMANDS: tuple[tuple[str, str], ...] = (
    ("reproduce public bundle", "python3 scripts/permea_reproduce.py"),
    ("validate public bundle", "python3 scripts/permea_validate.py"),
    ("generate evidence surface", "python3 scripts/generate_evidence_surface.py"),
    ("generate demo packet", "python3 scripts/generate_demo_packet.py"),
    ("generate artifact index", "python3 scripts/generate_artifact_index.py"),
    ("generate evidence matrix", "python3 scripts/generate_evidence_matrix.py"),
    ("run benchmark dry-run", "python3 scripts/run_permea_dry_run.py"),
    ("generate all artifacts", "python3 scripts/generate_permea_artifacts.py"),
)

VALIDATION_COMMANDS: tuple[tuple[str, str], ...] = (
    ("validate public bundle", "python3 scripts/permea_validate.py"),
    ("validate all artifacts", "python3 scripts/validate_permea_artifacts.py"),
    ("validate source registry", "python3 scripts/validate_source_registry.py"),
    ("validate benchmark registry", "python3 scripts/validate_benchmark_registry.py"),
    ("validate dataset cards", "python3 scripts/validate_dataset_cards.py"),
    ("validate acquisition manifests", "python3 scripts/validate_acquisition_manifests.py"),
    ("validate run manifests", "python3 scripts/validate_run_manifests.py"),
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
    "This surface is generated from public repository metadata and generated examples only.",
    "It is a navigation surface for deterministic local artifacts, not an acquisition run.",
    "It does not load source datasets, scrape websites, call external services, run ML, or score candidates.",
    "It does not confirm access, license, redistribution, biological performance, or clinical utility.",
)

NEXT_EVIDENCE_STEPS: tuple[str, ...] = (
    "Keep generated entry points refreshed through unified generation.",
    "Keep validation coverage aligned with every generated public evidence surface.",
    "Attach future public claims to generated artifacts, commands, limitations, and explicit non-claims.",
)


def collect_evidence_surface(root_path: str | Path = ".") -> dict[str, Any]:
    """Collect deterministic public evidence surface metadata."""
    root = Path(root_path).resolve()
    surface = {
        "surface_id": SURFACE_ID,
        "surface_type": SURFACE_TYPE,
        "generated_at": GENERATED_AT,
        "status": PASS,
        "overview": (
            "This generated README is the reviewer-facing navigation surface for "
            "Permea Core public artifacts. It links the demo packet, artifact "
            "index, evidence matrix, benchmark dry-run report, generated artifact "
            "families, reproducibility commands, validation commands, explicit "
            "non-claims, limitations, and next evidence steps."
        ),
        "primary_entry_points": _existing_link_items(root, PRIMARY_ENTRY_POINTS),
        "artifact_families": _existing_link_items(root, ARTIFACT_FAMILIES),
        "reproducibility_commands": [
            {"label": label, "command": command}
            for label, command in REPRODUCIBILITY_COMMANDS
        ],
        "validation_commands": [
            {"label": label, "command": command}
            for label, command in VALIDATION_COMMANDS
        ],
        "explicit_non_claims": list(EXPLICIT_NON_CLAIMS),
        "limitations": list(LIMITATIONS),
        "next_evidence_steps": list(NEXT_EVIDENCE_STEPS),
    }
    _assert_public_relative_surface(surface)
    return surface


def render_evidence_surface(surface: dict[str, Any]) -> str:
    """Render the evidence surface as public-safe Markdown."""
    lines = [
        "# Permea Core Generated Public Evidence Surface",
        "",
        "## Overview",
        "",
        surface["overview"],
        "",
        f"- Surface ID: `{surface['surface_id']}`",
        f"- Surface type: `{surface['surface_type']}`",
        f"- Generated at: `{surface['generated_at']}`",
        f"- Status: `{surface['status']}`",
        "",
        "## One-command demo",
        "",
        "`python3 scripts/generate_demo_packet.py`",
        "",
        "- [Public demo packet](DEMO_PACKET.md)",
        "- [Benchmark dry-run report](dry_runs/example_benchmark_dry_run.md)",
        "- [Reproducibility report](REPRODUCIBILITY_REPORT.md)",
        "",
        "## Core generated surfaces",
        "",
    ]
    lines.extend(_render_link_items(surface["primary_entry_points"]))
    lines.extend(["", "## Artifact families", ""])
    lines.extend(_render_link_items(surface["artifact_families"]))
    lines.extend(["", "## Reproducibility commands", ""])
    lines.extend(
        f"- {item['label']}: `{item['command']}`"
        for item in surface["reproducibility_commands"]
    )
    lines.extend(["", "## Validation commands", ""])
    lines.extend(
        f"- {item['label']}: `{item['command']}`"
        for item in surface["validation_commands"]
    )
    lines.extend(["", "## Explicit Non-Claims", ""])
    lines.extend(f"- {claim}" for claim in surface["explicit_non_claims"])
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {limitation}" for limitation in surface["limitations"])
    lines.extend(["", "## Next Evidence Steps", ""])
    lines.extend(f"- {step}" for step in surface["next_evidence_steps"])
    lines.append("")
    return "\n".join(lines)


def write_evidence_surface(
    output_path: str | Path = DEFAULT_EVIDENCE_SURFACE_PATH,
    root_path: str | Path | None = None,
) -> dict[str, Any]:
    """Write the deterministic generated evidence surface README."""
    root = Path(root_path).resolve() if root_path is not None else ROOT
    output = Path(output_path)
    if not output.is_absolute():
        output = root / output
    output.parent.mkdir(parents=True, exist_ok=True)

    surface = collect_evidence_surface(root)
    output.write_text(render_evidence_surface(surface), encoding="utf-8")

    return {**surface, "output_path": _display_path(root, output)}


def _existing_link_items(
    root: Path,
    items: tuple[tuple[str, str, str], ...],
) -> list[dict[str, Any]]:
    return [
        {
            "label": label,
            "path": path,
            "description": description,
            "exists": (root / "docs/examples/generated" / path).exists(),
        }
        for label, path, description in items
    ]


def _render_link_items(items: list[dict[str, Any]]) -> list[str]:
    return [
        f"- {item['label']}: [{item['path']}]({item['path']}) - "
        f"{item['description']} ({'present' if item.get('exists') else 'missing'})"
        for item in items
    ]


def _assert_public_relative_surface(value: Any) -> None:
    if isinstance(value, dict):
        for nested in value.values():
            _assert_public_relative_surface(nested)
    elif isinstance(value, list):
        for nested in value:
            _assert_public_relative_surface(nested)
    elif isinstance(value, str):
        if str(ROOT) in value or value.startswith("/"):
            raise ValueError(f"non-public or absolute path in evidence surface: {value}")


def _display_path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.name
