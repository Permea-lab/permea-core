"""Deterministic public-safe benchmark dry-run orchestration."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
FAIL = "FAIL"
DEFAULT_DRY_RUN_OUTPUT_DIR = Path("docs/examples/generated/dry_runs")
DEFAULT_DRY_RUN_JSON = "example_benchmark_dry_run.json"
DEFAULT_DRY_RUN_MARKDOWN = "example_benchmark_dry_run.md"
DEFAULT_DRY_RUN_README = "README.md"
DRY_RUN_ID = "example_benchmark_dry_run"
DRY_RUN_TYPE = "benchmark-dry-run-example"
GENERATED_AT = "example-generated"

INPUT_ARTIFACTS: tuple[tuple[str, str], ...] = (
    ("benchmark registry", "benchmarks/registry.yaml"),
    ("benchmark metadata", "benchmarks/bbb_b3pred_dataset3.yaml"),
    ("dataset card metadata", "dataset_cards/b3pred_dataset3.yaml"),
    ("acquisition manifest metadata", "acquisition_manifests/b3pred_dataset3.yaml"),
    ("run manifest metadata", "run_manifests/example_artifact_generation.yaml"),
)

LOCAL_COMMANDS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("benchmark registry validation", ("scripts/validate_benchmark_registry.py",)),
    ("dataset card validation", ("scripts/validate_dataset_cards.py",)),
    ("acquisition manifest validation", ("scripts/validate_acquisition_manifests.py",)),
    ("run manifest validation", ("scripts/validate_run_manifests.py",)),
    ("benchmark card generation", ("scripts/generate_benchmark_card.py",)),
    ("evidence card generation", ("scripts/generate_evidence_cards.py",)),
    ("output package generation", ("scripts/generate_output_package.py",)),
    ("run manifest generation", ("scripts/generate_run_manifests.py",)),
    ("artifact index generation", ("scripts/generate_artifact_index.py",)),
)

GENERATED_ARTIFACTS: tuple[tuple[str, str], ...] = (
    (
        "benchmark card",
        "docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md",
    ),
    (
        "evidence cards",
        "docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json",
    ),
    (
        "output package manifest",
        "docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml",
    ),
    (
        "output package metrics metadata",
        "docs/examples/generated/output_packages/bbb_b3pred_dataset3/metrics.json",
    ),
    (
        "output package ranking metadata",
        "docs/examples/generated/output_packages/bbb_b3pred_dataset3/ranking.csv",
    ),
    (
        "generated run manifest",
        "docs/examples/generated/run_manifests/example_artifact_generation.md",
    ),
    ("artifact index", "docs/examples/generated/ARTIFACT_INDEX.md"),
)

NON_CLAIMS: tuple[str, ...] = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no model performance claim",
)

LIMITATIONS: tuple[str, ...] = (
    "This dry-run is generated from local metadata and example artifacts only.",
    "It does not load source datasets or inspect row-level biological data.",
    "It does not evaluate baselines, train models, score candidates, or measure performance.",
    "It does not confirm access, license, redistribution, or acquisition readiness.",
)


def run_benchmark_dry_run(root_path: str | Path = ".") -> dict[str, Any]:
    """Run local dry-run generation and validation commands."""
    root = Path(root_path).resolve()
    command_results = [_run_local_command(root, name, command) for name, command in LOCAL_COMMANDS]
    status = PASS if all(step["status"] == PASS for step in command_results) else FAIL
    validation_steps = [
        step
        for step in command_results
        if "validation" in step["name"] or step["name"] == "artifact index generation"
    ]

    return {
        "dry_run_id": DRY_RUN_ID,
        "dry_run_type": DRY_RUN_TYPE,
        "generated_at": GENERATED_AT,
        "input_artifacts": [
            {"label": label, "path": path} for label, path in INPUT_ARTIFACTS
        ],
        "generated_artifacts": [
            {"label": label, "path": path} for label, path in GENERATED_ARTIFACTS
        ],
        "validation_steps": validation_steps,
        "commands_executed": command_results,
        "status": status,
        "non_claims": list(NON_CLAIMS),
        "limitations": list(LIMITATIONS),
        "next_action": "Review generated dry-run artifacts and run unified validation.",
    }


def render_dry_run_report(result: dict[str, Any]) -> str:
    """Render a public-safe Markdown dry-run report."""
    lines = [
        "# Benchmark Dry-Run: example_benchmark_dry_run",
        "",
        "## Overview",
        "",
        (
            "This deterministic dry-run is generated from metadata and local "
            "example artifacts. It demonstrates how Permea Core artifact layers "
            "fit together without dataset download, acquisition execution, API "
            "calls, ML runs, or performance measurement."
        ),
        "",
        "## Dry-Run Metadata",
        "",
        f"- Dry-run ID: `{result['dry_run_id']}`",
        f"- Dry-run type: `{result['dry_run_type']}`",
        f"- Generated at: `{result['generated_at']}`",
        f"- Status: `{result['status']}`",
        "",
        "## Input Artifacts",
        "",
    ]
    lines.extend(_render_path_items(result["input_artifacts"]))
    lines.extend(["", "## Commands Executed", ""])
    lines.extend(
        f"- {step['status']} `{step['command']}`"
        for step in result["commands_executed"]
    )
    lines.extend(["", "## Generated Artifacts", ""])
    lines.extend(_render_path_items(result["generated_artifacts"]))
    lines.extend(["", "## Related Evidence Surfaces", ""])
    lines.extend(
        [
            "- generated evidence surface: [../README.md](../README.md)",
            "- public demo packet: [../DEMO_PACKET.md](../DEMO_PACKET.md)",
            "- public artifact index: [../ARTIFACT_INDEX.md](../ARTIFACT_INDEX.md)",
            "- public evidence matrix: [../EVIDENCE_MATRIX.md](../EVIDENCE_MATRIX.md)",
            "- public reproducibility report: [../REPRODUCIBILITY_REPORT.md](../REPRODUCIBILITY_REPORT.md)",
        ]
    )
    lines.extend(["", "## Validation Steps", ""])
    lines.extend(
        f"- {step['status']} `{step['command']}`"
        for step in result["validation_steps"]
    )
    lines.extend(["", "## Explicit Non-Claims", ""])
    lines.extend(f"- {claim}" for claim in result["non_claims"])
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {limitation}" for limitation in result["limitations"])
    lines.extend(
        [
            "",
            "## Next Action",
            "",
            result["next_action"],
            "",
        ]
    )
    return "\n".join(lines)


def write_dry_run_outputs(
    output_dir: str | Path = DEFAULT_DRY_RUN_OUTPUT_DIR,
    root_path: str | Path | None = None,
) -> dict[str, Any]:
    """Run the benchmark dry-run and write JSON, Markdown, and README outputs."""
    root = Path(root_path).resolve() if root_path is not None else ROOT
    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination

    result = run_benchmark_dry_run(root)
    destination.mkdir(parents=True, exist_ok=True)

    json_path = destination / DEFAULT_DRY_RUN_JSON
    markdown_path = destination / DEFAULT_DRY_RUN_MARKDOWN
    readme_path = destination / DEFAULT_DRY_RUN_README

    output_paths = {
        "json": _display_path(root, json_path),
        "markdown": _display_path(root, markdown_path),
        "readme": _display_path(root, readme_path),
    }
    result_with_outputs = {**result, "output_paths": output_paths}

    json_path.write_text(
        json.dumps(result_with_outputs, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_dry_run_report(result), encoding="utf-8")
    readme_path.write_text(_render_readme(output_paths), encoding="utf-8")

    return result_with_outputs


def _run_local_command(
    root: Path,
    name: str,
    command: tuple[str, ...],
) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, *command],
        cwd=root,
        check=False,
        text=True,
        capture_output=True,
    )
    return {
        "name": name,
        "command": _format_public_command(command),
        "status": PASS if completed.returncode == 0 else FAIL,
        "return_code": completed.returncode,
    }


def _render_path_items(items: list[dict[str, str]]) -> list[str]:
    return [f"- {item['label']}: [{item['path']}]({item['path']})" for item in items]


def _render_readme(output_paths: dict[str, str]) -> str:
    return "\n".join(
        [
            "# Generated Benchmark Dry-Run Reports",
            "",
            "These public-safe reports are generated from local Permea Core metadata.",
            "",
            "- No dataset downloaded.",
            "- No acquisition executed.",
            "- No redistribution rights confirmed.",
            "- No wet-lab validation by Permea.",
            "- No model performance claim.",
            "",
            "## Reports",
            "",
            f"- [Markdown report]({Path(output_paths['markdown']).name})",
            f"- [JSON report]({Path(output_paths['json']).name})",
            "",
        ]
    )


def _format_public_command(command: tuple[str, ...]) -> str:
    return " ".join(("python3", *command))


def _display_path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.name
