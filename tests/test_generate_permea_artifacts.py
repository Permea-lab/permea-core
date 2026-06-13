from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.generation import artifacts


REQUIRED_STEP_NAMES = tuple(name for name, _command in artifacts.GENERATION_STEPS)


def test_unified_generation_passes_current_repo_state() -> None:
    result = artifacts.generate_permea_artifacts()

    assert result["status"] == artifacts.PASS
    assert [step["name"] for step in result["steps"]] == list(REQUIRED_STEP_NAMES)
    assert all(step["return_code"] == 0 for step in result["steps"])


def test_report_includes_each_required_step_name() -> None:
    result = {
        "status": artifacts.PASS,
        "steps": [
            {
                "name": name,
                "command": [sys.executable, command[0]],
                "status": artifacts.PASS,
                "return_code": 0,
                "stdout_summary": "ok",
                "stderr_summary": "",
            }
            for name, command in artifacts.GENERATION_STEPS
        ],
    }

    report = artifacts.format_generation_report(result)

    assert "PASS Permea artifact generation" in report
    for name in REQUIRED_STEP_NAMES:
        assert name in report


def test_failed_subprocess_step_is_reported_as_fail(monkeypatch) -> None:
    def fail_run(*_args, **_kwargs):
        return subprocess.CompletedProcess(
            args=["python", "scripts/example.py"],
            returncode=7,
            stdout="partial output\n",
            stderr="example failure\n",
        )

    monkeypatch.setattr(artifacts.subprocess, "run", fail_run)

    step = artifacts.run_generation_step(
        "example failure step",
        [sys.executable, "scripts/example.py"],
    )

    assert step["status"] == artifacts.FAIL
    assert step["return_code"] == 7
    assert "partial output" in step["stdout_summary"]
    assert "example failure" in step["stderr_summary"]


def test_cli_exits_zero_on_current_repo_state() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_permea_artifacts.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS Permea artifact generation" in completed.stdout
    for name in REQUIRED_STEP_NAMES:
        assert name in completed.stdout
