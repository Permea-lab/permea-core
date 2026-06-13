from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.dry_run.orchestrator import (
    NON_CLAIMS,
    PASS,
    render_dry_run_report,
    run_benchmark_dry_run,
    write_dry_run_outputs,
)


REQUIRED_JSON_KEYS = (
    "dry_run_id",
    "dry_run_type",
    "generated_at",
    "input_artifacts",
    "generated_artifacts",
    "validation_steps",
    "commands_executed",
    "status",
    "non_claims",
    "limitations",
    "next_action",
)

REQUIRED_MARKDOWN_SECTIONS = (
    "## Overview",
    "## Dry-Run Metadata",
    "## Input Artifacts",
    "## Commands Executed",
    "## Generated Artifacts",
    "## Validation Steps",
    "## Explicit Non-Claims",
    "## Limitations",
    "## Next Action",
)


def test_dry_run_returns_pass_on_current_repo_state() -> None:
    result = run_benchmark_dry_run(ROOT)

    assert result["status"] == PASS
    assert result["dry_run_id"] == "example_benchmark_dry_run"
    assert all(step["return_code"] == 0 for step in result["commands_executed"])


def test_generated_json_includes_required_keys(tmp_path: Path) -> None:
    result = write_dry_run_outputs(tmp_path, ROOT)
    payload = json.loads((tmp_path / "example_benchmark_dry_run.json").read_text())

    for key in REQUIRED_JSON_KEYS:
        assert key in payload
    assert payload["status"] == PASS
    assert payload["output_paths"] == result["output_paths"]


def test_generated_markdown_includes_required_sections() -> None:
    report = render_dry_run_report(run_benchmark_dry_run(ROOT))

    for section in REQUIRED_MARKDOWN_SECTIONS:
        assert section in report


def test_generated_markdown_includes_explicit_non_claims() -> None:
    report = render_dry_run_report(run_benchmark_dry_run(ROOT))

    for claim in NON_CLAIMS:
        assert f"- {claim}" in report


def test_cli_exits_zero_and_writes_outputs() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_permea_dry_run.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS benchmark dry-run" in completed.stdout
    assert (
        ROOT
        / "docs"
        / "examples"
        / "generated"
        / "dry_runs"
        / "example_benchmark_dry_run.md"
    ).exists()


def test_output_paths_are_relative_public_paths(tmp_path: Path) -> None:
    result = write_dry_run_outputs(tmp_path, ROOT)
    report = render_dry_run_report(result)

    assert str(ROOT) not in report
    for item in result["input_artifacts"]:
        assert not item["path"].startswith("/")
    for item in result["generated_artifacts"]:
        assert not item["path"].startswith("/")
