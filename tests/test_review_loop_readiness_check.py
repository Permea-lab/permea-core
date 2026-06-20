from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.review_packets.bundle_completeness import FAIL, PASS  # noqa: E402
from permea_core.review_packets.loop_readiness import (  # noqa: E402
    CHECKER_PATH,
    FIXTURE_PATH,
    REPORTS_INDEX_PATH,
    REVIEW_EXAMPLES_INDEX_PATH,
    REVIEW_HUB_PATH,
    REVIEW_README_PATH,
    REVIEW_STANDARD_PATH,
    check_review_loop_readiness,
    render_review_loop_readiness_summary,
)


def test_review_loop_readiness_passes_current_repo() -> None:
    result = check_review_loop_readiness(ROOT)

    assert result["status"] == PASS
    assert all(check["status"] == PASS for check in result["checks"])


def test_review_loop_readiness_json_output_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts/check_review_loop_readiness.py"), "--json"]
    first = subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True)
    second = subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True)

    assert first.stdout == second.stdout
    assert json.loads(first.stdout)["status"] == PASS


def test_review_loop_readiness_text_output_passes() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_review_loop_readiness.py")],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )

    assert "Permea Core review loop readiness check" in completed.stdout
    assert "Status: PASS" in completed.stdout


def test_review_loop_readiness_fails_when_fixture_is_malformed(tmp_path: Path) -> None:
    repo = _copy_readiness_surface(tmp_path)
    fixture = repo / FIXTURE_PATH
    fixture.write_text(
        fixture.read_text(encoding="utf-8").replace(
            "Remote GitHub review URLs:",
            "Remote review links:",
        ),
        encoding="utf-8",
    )

    result = check_review_loop_readiness(repo)

    assert result["status"] == FAIL
    failed = {check["name"] for check in result["checks"] if check["status"] == FAIL}
    assert "canonical fixture passes completeness checker" in failed


def test_review_loop_readiness_fails_when_navigation_cannot_reach_fixture(tmp_path: Path) -> None:
    repo = _copy_readiness_surface(tmp_path)
    examples_index = repo / REVIEW_EXAMPLES_INDEX_PATH
    examples_index.write_text(
        examples_index.read_text(encoding="utf-8").replace(
            "final-review-bundle-complete-example.md",
            "missing-review-bundle-example.md",
        ),
        encoding="utf-8",
    )

    result = check_review_loop_readiness(repo)

    assert result["status"] == FAIL
    failed = {check["name"] for check in result["checks"] if check["status"] == FAIL}
    assert "public review navigation reaches fixture" in failed


def test_readiness_docs_reference_fixture_and_checkers() -> None:
    review_readme = (ROOT / REVIEW_README_PATH).read_text(encoding="utf-8")
    review_standard = (ROOT / REVIEW_STANDARD_PATH).read_text(encoding="utf-8")
    reports_index = (ROOT / REPORTS_INDEX_PATH).read_text(encoding="utf-8")

    assert "final-review-bundle-complete-example.md" in review_readme
    assert "examples/final-review-bundle-complete-example.md" in review_standard
    assert "check_review_bundle_completeness.py" in review_readme
    assert "check_review_bundle_completeness.py" in review_standard
    assert "check_review_loop_readiness.py" in reports_index


def test_summary_is_deterministic() -> None:
    result = check_review_loop_readiness(ROOT)

    assert render_review_loop_readiness_summary(result) == render_review_loop_readiness_summary(result)


def _copy_readiness_surface(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    for relative in (
        FIXTURE_PATH,
        CHECKER_PATH,
        REVIEW_README_PATH,
        REVIEW_STANDARD_PATH,
        REVIEW_EXAMPLES_INDEX_PATH,
        REVIEW_HUB_PATH,
        REPORTS_INDEX_PATH,
    ):
        source = ROOT / relative
        target = repo / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    return repo
