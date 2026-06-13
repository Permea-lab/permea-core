"""Unified local generation for deterministic Permea Core example artifacts."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
FAIL = "FAIL"

GENERATION_STEPS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("benchmark card generation", ("scripts/generate_benchmark_card.py",)),
    ("output package generation", ("scripts/generate_output_package.py",)),
    ("evidence card generation", ("scripts/generate_evidence_cards.py",)),
    ("dataset card generation", ("scripts/generate_dataset_cards.py",)),
    ("acquisition manifest generation", ("scripts/generate_acquisition_manifests.py",)),
    ("run manifest generation", ("scripts/generate_run_manifests.py",)),
    ("artifact index generation", ("scripts/generate_artifact_index.py",)),
    ("benchmark dry-run generation", ("scripts/run_permea_dry_run.py",)),
)


def run_generation_step(name: str, command: list[str]) -> dict[str, Any]:
    """Run one local generation command and return a structured step result."""
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    status = PASS if completed.returncode == 0 else FAIL
    return {
        "name": name,
        "command": command,
        "status": status,
        "return_code": completed.returncode,
        "stdout_summary": _summarize_stream(completed.stdout),
        "stderr_summary": _summarize_stream(completed.stderr),
    }


def generate_permea_artifacts() -> dict[str, Any]:
    """Generate current deterministic Permea Core example artifacts."""
    steps = [
        run_generation_step(name, [sys.executable, *command])
        for name, command in GENERATION_STEPS
    ]
    status = PASS if all(step["status"] == PASS for step in steps) else FAIL
    return {
        "status": status,
        "steps": steps,
    }


def format_generation_report(result: dict[str, Any]) -> str:
    """Format a unified generation result as a readable PASS/FAIL report."""
    lines = [
        f"{result['status']} Permea artifact generation",
        "",
        "Steps:",
    ]
    for step in result["steps"]:
        lines.append(
            f"- {step['status']} {step['name']} "
            f"(exit {step['return_code']}): {_format_command(step['command'])}"
        )
        if step["stdout_summary"]:
            lines.append(f"  stdout: {step['stdout_summary']}")
        if step["stderr_summary"]:
            lines.append(f"  stderr: {step['stderr_summary']}")

    return "\n".join(lines)


def _format_command(command: list[str]) -> str:
    return " ".join(command)


def _summarize_stream(text: str, max_lines: int = 8) -> str:
    lines = [line for line in text.strip().splitlines() if line.strip()]
    if not lines:
        return ""
    if len(lines) <= max_lines:
        return " | ".join(lines)
    omitted = len(lines) - max_lines
    return " | ".join([*lines[:max_lines], f"... {omitted} more line(s)"])
