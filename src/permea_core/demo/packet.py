"""Deterministic public-safe demo packet generation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
DEFAULT_DEMO_PACKET_OUTPUT_DIR = Path("docs/examples/generated")
DEFAULT_DEMO_PACKET_JSON = "DEMO_PACKET.json"
DEFAULT_DEMO_PACKET_MARKDOWN = "DEMO_PACKET.md"
PACKET_ID = "permea_core_public_demo_packet"
PACKET_TYPE = "public-demo-packet"
GENERATED_AT = "example-generated"

AVAILABLE_COMMANDS: tuple[tuple[str, str], ...] = (
    ("one-command demo packet", "python3 scripts/generate_demo_packet.py"),
    ("benchmark dry-run", "python3 scripts/run_permea_dry_run.py"),
    ("unified artifact generation", "python3 scripts/generate_permea_artifacts.py"),
    ("unified artifact validation", "python3 scripts/validate_permea_artifacts.py"),
)

INPUT_ARTIFACTS: tuple[tuple[str, str], ...] = (
    ("source registry", "sources/registry.yaml"),
    ("benchmark registry", "benchmarks/registry.yaml"),
    ("benchmark task metadata", "benchmarks/bbb_b3pred_dataset3.yaml"),
    ("dataset card metadata", "dataset_cards/b3pred_dataset3.yaml"),
    ("acquisition manifest metadata", "acquisition_manifests/b3pred_dataset3.yaml"),
    ("run manifest metadata", "run_manifests/example_artifact_generation.yaml"),
)

GENERATED_ARTIFACTS: tuple[tuple[str, str], ...] = (
    ("artifact index", "docs/examples/generated/ARTIFACT_INDEX.md"),
    ("benchmark dry-run Markdown", "docs/examples/generated/dry_runs/example_benchmark_dry_run.md"),
    ("benchmark dry-run JSON", "docs/examples/generated/dry_runs/example_benchmark_dry_run.json"),
    ("benchmark card", "docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md"),
    ("dataset card", "docs/examples/generated/dataset_cards/b3pred_dataset3.md"),
    ("acquisition manifest", "docs/examples/generated/acquisition_manifests/b3pred_dataset3.md"),
    ("evidence cards", "docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json"),
    ("output package manifest", "docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml"),
    ("output package metrics metadata", "docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json"),
    ("output package ranking metadata", "docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv"),
    ("run manifest", "docs/examples/generated/run_manifests/example_artifact_generation.md"),
)

ARTIFACT_FAMILIES: tuple[tuple[str, str], ...] = (
    ("Artifact index", "docs/examples/generated/ARTIFACT_INDEX.md"),
    ("Benchmark dry-run reports", "docs/examples/generated/dry_runs/README.md"),
    ("Benchmark cards", "docs/examples/generated/benchmark_cards"),
    ("Dataset cards", "docs/examples/generated/dataset_cards"),
    ("Acquisition manifests", "docs/examples/generated/acquisition_manifests"),
    ("Evidence cards", "docs/examples/generated/evidence_cards"),
    ("Output packages", "docs/examples/generated/output_packages"),
    ("Run manifests", "docs/examples/generated/run_manifests"),
)

NON_CLAIMS: tuple[str, ...] = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no model performance claim",
)

LIMITATIONS: tuple[str, ...] = (
    "This packet is generated from repository metadata and generated examples only.",
    "It is a public artifact-system demonstration, not a data acquisition run.",
    "It does not load source datasets, inspect row-level biological data, run ML, or score candidates.",
    "It does not confirm access, license, redistribution, acquisition readiness, or biological performance.",
)


def collect_demo_packet(root_path: str | Path = ".") -> dict[str, Any]:
    """Collect deterministic public demo packet metadata."""
    root = Path(root_path).resolve()
    packet = {
        "packet_id": PACKET_ID,
        "packet_type": PACKET_TYPE,
        "generated_at": GENERATED_AT,
        "status": PASS,
        "overview": (
            "This public demo packet is a generated entry point for the current "
            "Permea Core artifact system. It points reviewers to local commands, "
            "input metadata, generated examples, dry-run outputs, validation, and "
            "explicit non-claims."
        ),
        "available_commands": [
            {"label": label, "command": command}
            for label, command in AVAILABLE_COMMANDS
        ],
        "input_artifacts": _existing_path_items(root, INPUT_ARTIFACTS),
        "generated_artifacts": _existing_path_items(root, GENERATED_ARTIFACTS),
        "artifact_families": _existing_path_items(root, ARTIFACT_FAMILIES),
        "dry_run_summary": {
            "command": "python3 scripts/run_permea_dry_run.py",
            "summary": (
                "Runs local metadata checks and example artifact generators, then "
                "writes deterministic dry-run Markdown and JSON reports."
            ),
            "paths": [
                "docs/examples/generated/dry_runs/example_benchmark_dry_run.md",
                "docs/examples/generated/dry_runs/example_benchmark_dry_run.json",
            ],
        },
        "unified_generation_summary": {
            "command": "python3 scripts/generate_permea_artifacts.py",
            "summary": "Regenerates the current deterministic public example artifacts.",
        },
        "unified_validation_summary": {
            "command": "python3 scripts/validate_permea_artifacts.py",
            "summary": (
                "Validates current registry inputs and generated artifact examples "
                "with local deterministic checks."
            ),
        },
        "artifact_index_path": "docs/examples/generated/ARTIFACT_INDEX.md",
        "dry_run_report_paths": [
            "docs/examples/generated/dry_runs/example_benchmark_dry_run.md",
            "docs/examples/generated/dry_runs/example_benchmark_dry_run.json",
        ],
        "non_claims": list(NON_CLAIMS),
        "limitations": list(LIMITATIONS),
        "next_action": (
            "Review this packet, then run the dry-run, unified generation, and "
            "unified validation commands before opening or reviewing a public PR."
        ),
    }
    _assert_public_relative_packet(packet)
    return packet


def render_demo_packet(packet: dict[str, Any]) -> str:
    """Render a demo packet as public-safe Markdown."""
    lines = [
        "# Permea Core Public Demo Packet",
        "",
        "## Overview",
        "",
        packet["overview"],
        "",
        f"- Packet ID: `{packet['packet_id']}`",
        f"- Packet type: `{packet['packet_type']}`",
        f"- Generated at: `{packet['generated_at']}`",
        f"- Status: `{packet['status']}`",
        "",
        "## One-command demo",
        "",
        "`python3 scripts/generate_demo_packet.py`",
        "",
        "This command writes:",
        "",
        "- `docs/examples/generated/DEMO_PACKET.md`",
        "- `docs/examples/generated/DEMO_PACKET.json`",
        "",
        "## Regenerate artifacts",
        "",
        f"`{packet['unified_generation_summary']['command']}`",
        "",
        packet["unified_generation_summary"]["summary"],
        "",
        "## Validate artifacts",
        "",
        f"`{packet['unified_validation_summary']['command']}`",
        "",
        packet["unified_validation_summary"]["summary"],
        "",
        "## Artifact families",
        "",
    ]
    lines.extend(_render_path_items(packet["artifact_families"]))
    lines.extend(["", "## Input Artifacts", ""])
    lines.extend(_render_path_items(packet["input_artifacts"]))
    lines.extend(["", "## Generated Artifacts", ""])
    lines.extend(_render_path_items(packet["generated_artifacts"]))
    lines.extend(
        [
            "",
            "## Dry-run output",
            "",
            f"`{packet['dry_run_summary']['command']}`",
            "",
            packet["dry_run_summary"]["summary"],
            "",
        ]
    )
    lines.extend(f"- [{path}]({path})" for path in packet["dry_run_report_paths"])
    lines.extend(
        [
            "",
            "## Public artifact index",
            "",
            f"- [{packet['artifact_index_path']}]({packet['artifact_index_path']})",
            "",
            "## Available Commands",
            "",
        ]
    )
    lines.extend(
        f"- {item['label']}: `{item['command']}`"
        for item in packet["available_commands"]
    )
    lines.extend(["", "## Explicit Non-Claims", ""])
    lines.extend(f"- {claim}" for claim in packet["non_claims"])
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {limitation}" for limitation in packet["limitations"])
    lines.extend(["", "## Next Steps", "", packet["next_action"], ""])
    return "\n".join(lines)


def write_demo_packet(
    output_dir: str | Path = DEFAULT_DEMO_PACKET_OUTPUT_DIR,
    root_path: str | Path | None = None,
) -> dict[str, Any]:
    """Write deterministic demo packet Markdown and JSON outputs."""
    root = Path(root_path).resolve() if root_path is not None else ROOT
    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination
    destination.mkdir(parents=True, exist_ok=True)

    packet = collect_demo_packet(root)
    markdown_path = destination / DEFAULT_DEMO_PACKET_MARKDOWN
    json_path = destination / DEFAULT_DEMO_PACKET_JSON
    output_paths = {
        "markdown": _display_path(root, markdown_path),
        "json": _display_path(root, json_path),
    }
    packet_with_outputs = {**packet, "output_paths": output_paths}

    markdown_path.write_text(render_demo_packet(packet_with_outputs), encoding="utf-8")
    json_path.write_text(
        json.dumps(packet_with_outputs, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    return packet_with_outputs


def _existing_path_items(
    root: Path,
    items: tuple[tuple[str, str], ...],
) -> list[dict[str, str]]:
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


def _assert_public_relative_packet(value: Any) -> None:
    if isinstance(value, dict):
        for nested in value.values():
            _assert_public_relative_packet(nested)
    elif isinstance(value, list):
        for nested in value:
            _assert_public_relative_packet(nested)
    elif isinstance(value, str):
        if str(ROOT) in value or value.startswith("/"):
            raise ValueError(f"non-public or absolute path in demo packet: {value}")


def _display_path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.name
