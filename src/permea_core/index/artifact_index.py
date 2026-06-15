"""Generate a deterministic public index of Permea Core artifacts."""

from __future__ import annotations

from pathlib import Path
from typing import Any


DEFAULT_ARTIFACT_INDEX_PATH = Path("docs/examples/generated/ARTIFACT_INDEX.md")

REGISTRY_INPUTS: tuple[tuple[str, str], ...] = (
    ("Source registry", "sources/registry.yaml"),
    ("Benchmark registry", "benchmarks/registry.yaml"),
    ("Dataset card inputs", "dataset_cards"),
    ("Acquisition manifest inputs", "acquisition_manifests"),
    ("Run manifest inputs", "run_manifests"),
)

ARTIFACT_FAMILIES: tuple[tuple[str, str, str], ...] = (
    (
        "Generated Benchmark Cards",
        "benchmark_cards",
        "docs/examples/generated/benchmark_cards",
    ),
    (
        "Generated Dataset Cards",
        "dataset_cards",
        "docs/examples/generated/dataset_cards",
    ),
    (
        "Generated Acquisition Manifests",
        "acquisition_manifests",
        "docs/examples/generated/acquisition_manifests",
    ),
    (
        "Generated Evidence Cards",
        "evidence_cards",
        "docs/examples/generated/evidence_cards",
    ),
    (
        "Generated Output Packages",
        "output_packages",
        "docs/examples/generated/output_packages",
    ),
    (
        "Generated Run Manifests",
        "run_manifests",
        "docs/examples/generated/run_manifests",
    ),
)

UNIFIED_COMMANDS: tuple[str, ...] = (
    "python3 scripts/generate_evidence_surface.py",
    "python3 scripts/permea_evaluate.py",
    "python3 scripts/permea_reproduce.py",
    "python3 scripts/permea_validate.py",
    "python3 scripts/generate_demo_packet.py",
    "python3 scripts/generate_artifact_index.py",
    "python3 scripts/generate_evidence_matrix.py",
    "python3 scripts/run_permea_dry_run.py",
    "python3 scripts/generate_permea_artifacts.py",
    "python3 scripts/validate_permea_artifacts.py",
)

CORE_SURFACES: tuple[tuple[str, str], ...] = (
    ("Generated evidence surface", "docs/examples/generated/README.md"),
    ("Public demo packet", "docs/examples/generated/DEMO_PACKET.md"),
    ("Public artifact index", "docs/examples/generated/ARTIFACT_INDEX.md"),
    ("Public evidence matrix", "docs/examples/generated/EVIDENCE_MATRIX.md"),
    ("Public evaluation packet", "docs/examples/generated/EVALUATION_PACKET.md"),
    ("Public reproducibility report", "docs/examples/generated/REPRODUCIBILITY_REPORT.md"),
    ("Benchmark dry-run report", "docs/examples/generated/dry_runs/example_benchmark_dry_run.md"),
)

NON_CLAIMS: tuple[str, ...] = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no model performance claim",
)


def collect_artifact_paths(root_path: str | Path = ".") -> dict[str, Any]:
    """Collect public registry and generated artifact paths under a repo root."""
    root = Path(root_path).resolve()
    registry_inputs = [
        {"label": label, "path": _relative_path(root, root / path)}
        for label, path in REGISTRY_INPUTS
        if (root / path).exists()
    ]
    artifact_families = {
        key: {
            "title": title,
            "root": _relative_path(root, root / directory),
            "paths": _collect_files(root, root / directory),
        }
        for title, key, directory in ARTIFACT_FAMILIES
    }
    return {
        "registry_inputs": registry_inputs,
        "artifact_families": artifact_families,
        "commands": list(UNIFIED_COMMANDS),
        "core_surfaces": [
            {"label": label, "path": path}
            for label, path in CORE_SURFACES
            if (root / path).exists()
        ],
        "non_claims": list(NON_CLAIMS),
    }


def render_artifact_index(index: dict[str, Any]) -> str:
    """Render a deterministic Markdown artifact index."""
    lines = [
        "# Permea Core Public Artifact Index",
        "",
        "## Overview",
        "",
        (
            "This generated index lists the current public registry inputs, "
            "generated example artifacts, and local generation and validation "
            "commands available in Permea Core."
        ),
        "",
        "## Unified Commands",
        "",
    ]
    lines.extend(f"- `{command}`" for command in index["commands"])
    lines.extend(["", "## Core Generated Surfaces", ""])
    lines.extend(
        f"- {item['label']}: [{item['path']}]({item['path']})"
        for item in index["core_surfaces"]
    )
    lines.extend(["", "## Registry Inputs", ""])
    lines.extend(
        f"- {item['label']}: [{item['path']}]({item['path']})"
        for item in index["registry_inputs"]
    )

    for title, key, _directory in ARTIFACT_FAMILIES:
        family = index["artifact_families"][key]
        lines.extend(["", f"## {title}", ""])
        if not family["paths"]:
            lines.append("- No generated files found.")
            continue
        lines.extend(f"- [{path}]({path})" for path in family["paths"])

    lines.extend(
        [
            "",
            "## Validation Boundary",
            "",
            (
                "The listed artifacts are deterministic local examples and "
                "metadata records. Validation checks repository schemas, "
                "required fields, path references, and generated-file presence."
            ),
            "",
            "## Explicit Non-Claims",
            "",
        ]
    )
    lines.extend(f"- {claim}" for claim in index["non_claims"])
    lines.extend(
        [
            "",
            "## Next Steps",
            "",
            "- Keep generated artifacts refreshed through the unified generator.",
            "- Keep validation command coverage aligned with new artifact families.",
            "- Add new public artifact families only after their schema and boundary checks exist.",
            "",
        ]
    )
    return "\n".join(lines)


def generate_artifact_index(
    output_path: str | Path = DEFAULT_ARTIFACT_INDEX_PATH,
    root_path: str | Path | None = None,
) -> dict[str, Any]:
    """Generate the public artifact index and return a structured result."""
    output = Path(output_path)
    root = Path(root_path).resolve() if root_path is not None else Path.cwd().resolve()
    if not output.is_absolute():
        output = root / output

    index = collect_artifact_paths(root)
    rendered = render_artifact_index(index)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")

    relative_output = _display_path(root, output)
    file_count = sum(
        len(family["paths"]) for family in index["artifact_families"].values()
    )
    return {
        "passed": True,
        "output_path": relative_output,
        "artifact_family_count": len(index["artifact_families"]),
        "generated_file_count": file_count,
    }


def _collect_files(root: Path, directory: Path) -> list[str]:
    if not directory.exists():
        return []
    return [
        _relative_path(root, path)
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    ]


def _relative_path(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def _display_path(root: Path, path: Path) -> str:
    try:
        return _relative_path(root, path)
    except ValueError:
        return path.name
