from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.review_packets.bundle_completeness import (  # noqa: E402
    DEFAULT_SAMPLE_BUNDLE,
    FAIL,
    PASS,
    check_review_bundle_completeness,
    check_review_bundle_file,
    render_bundle_completeness_summary,
)

FIXTURE_PATH = ROOT / "docs/review/examples/final-review-bundle-complete-example.md"
REPORT_PATH = ROOT / "docs/reports/p-core-063-review-bundle-fixture-example-v0.md"
THIS_TEST_PATH = ROOT / "tests/test_review_bundle_completeness_check.py"
READABILITY_FILES = (FIXTURE_PATH, REPORT_PATH, THIS_TEST_PATH)
MIN_PHYSICAL_LINES = {
    FIXTURE_PATH: 80,
    REPORT_PATH: 80,
    THIS_TEST_PATH: 240,
}
MAX_LINE_LENGTH = 240
LINE_FEED = chr(10)
BAD_CODEPOINTS = {
    0x2028,
    0x2029,
    0x200B,
    0x200C,
    0x200D,
    0x2060,
    0xFEFF,
    0x061C,
    *range(0x202A, 0x202F),
}
TOUCHED_PUBLIC_FILES = (
    "scripts/check_review_bundle_completeness.py",
    "src/permea_core/review_packets/bundle_completeness.py",
    "tests/test_review_bundle_completeness_check.py",
    "docs/reports/p-core-062-review-bundle-completeness-check-v0.md",
    "docs/review/examples/README.md",
    "docs/review/examples/final-review-bundle-complete-example.md",
    "docs/reports/p-core-063-review-bundle-fixture-example-v0.md",
)
PROHIBITED_PUBLIC_SAFETY_TERMS = (
    "AI " + "Champion",
    "H" + "100",
    "K-" + "EXAONE",
    "KO" + "RA",
    "private " + "doctrine",
    "private " + "infrastructure",
)
PROHIBITED_AFFIRMATIVE_CLAIMS = (
    "wet-lab",
    "clinical",
    "biological " + "result",
    "model " + "performance",
    "benchmark " + "result",
    "scientific " + "evidence",
    "solved-" + "delivery",
    "in-vivo",
    "in vivo",
)
BOUNDARY_MARKERS = (
    "no ",
    "not ",
    "does not ",
    "without ",
    "limitations",
    "boundary",
    "claim",
)


def test_complete_bundle_passes() -> None:
    result = check_review_bundle_completeness(DEFAULT_SAMPLE_BUNDLE)

    assert result["status"] == PASS
    assert result["missing_fields"] == []
    assert all(check["status"] == PASS for check in result["checks"])


def test_complete_fixture_file_passes() -> None:
    result = check_review_bundle_file(FIXTURE_PATH)

    assert result["status"] == PASS
    assert result["missing_fields"] == []
    assert all(check["status"] == PASS for check in result["checks"])


def test_fixture_missing_required_section_fails() -> None:
    fixture_text = FIXTURE_PATH.read_text(encoding="utf-8")
    text = fixture_text.replace("Remote GitHub review URLs:", "Remote review links:")
    result = check_review_bundle_completeness(text)

    assert result["status"] == FAIL
    assert "remote GitHub review URLs" in result["missing_fields"]


def test_missing_local_paths_fails() -> None:
    result = check_review_bundle_completeness(_without_section("Local human-review paths"))

    assert result["status"] == FAIL
    assert "local human-review paths" in result["missing_fields"]


def test_missing_remote_urls_fails() -> None:
    result = check_review_bundle_completeness(_without_section("Remote GitHub review URLs"))

    assert result["status"] == FAIL
    assert "remote GitHub review URLs" in result["missing_fields"]


def test_missing_validation_results_fails() -> None:
    result = check_review_bundle_completeness(_without_section("Validation results"))

    assert result["status"] == FAIL
    assert "validation commands and results" in result["missing_fields"]


def test_missing_audit_results_fails() -> None:
    text = DEFAULT_SAMPLE_BUNDLE.replace("Scope audit result:", "Scope review:")
    text = text.replace("Boundary audit result:", "Boundary review:")
    text = text.replace("Claim-discipline audit result:", "Claim review:")
    result = check_review_bundle_completeness(text)

    assert result["status"] == FAIL
    assert "scope audit result" in result["missing_fields"]
    assert "boundary audit result" in result["missing_fields"]
    assert "claim-discipline audit result" in result["missing_fields"]


def test_missing_stop_reason_fails() -> None:
    result = check_review_bundle_completeness(_without_section("Stop reason"))

    assert result["status"] == FAIL
    assert "stop reason" in result["missing_fields"]


def test_json_output_is_deterministic() -> None:
    first = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_review_bundle_completeness.py"), "--json"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    second = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_review_bundle_completeness.py"), "--json"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )

    assert first.stdout == second.stdout
    assert json.loads(first.stdout)["status"] == PASS


def test_fixture_json_output_is_deterministic() -> None:
    command = [
        sys.executable,
        str(ROOT / "scripts/check_review_bundle_completeness.py"),
        str(FIXTURE_PATH.relative_to(ROOT)),
        "--json",
    ]
    first = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    second = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )

    assert first.stdout == second.stdout
    assert json.loads(first.stdout)["status"] == PASS


def test_cli_text_output_passes() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_review_bundle_completeness.py")],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )

    assert "Status: PASS" in completed.stdout
    assert "Missing fields:" in completed.stdout
    assert "- none" in completed.stdout


def test_summary_is_deterministic() -> None:
    result = check_review_bundle_completeness(DEFAULT_SAMPLE_BUNDLE)

    assert render_bundle_completeness_summary(result) == render_bundle_completeness_summary(result)


def test_review_navigation_includes_bundle_examples() -> None:
    review_readme = (ROOT / "docs/review/README.md").read_text(encoding="utf-8")
    review_standard = (ROOT / "docs/review/review-loop-operating-standard.md").read_text(
        encoding="utf-8"
    )
    review_hub = (ROOT / "REVIEW_HUB.md").read_text(encoding="utf-8")
    reports_index = (ROOT / "docs/reports/README.md").read_text(encoding="utf-8")

    assert "examples/README.md" in review_readme
    assert "examples/final-review-bundle-complete-example.md" in review_standard
    assert "docs/review/examples/README.md" in review_hub
    assert "p-core-063-review-bundle-fixture-example-v0.md" in reports_index


def test_review_bundle_fixture_files_are_physically_readable() -> None:
    for path, minimum in MIN_PHYSICAL_LINES.items():
        lines = path.read_text(encoding="utf-8").splitlines()

        assert len(lines) >= minimum, path
        assert max(len(line) for line in lines) <= MAX_LINE_LENGTH, path


def test_review_bundle_fixture_files_use_lf_only() -> None:
    for path in READABILITY_FILES:
        content = path.read_bytes()

        assert bytes([13]) not in content, path
        assert content.count(bytes([10])) >= MIN_PHYSICAL_LINES[path], path


def test_review_bundle_fixture_files_have_no_hidden_unicode() -> None:
    for path in READABILITY_FILES:
        text = path.read_text(encoding="utf-8")
        hidden = [hex(ord(char)) for char in text if ord(char) in BAD_CODEPOINTS]

        assert hidden == [], path


def test_review_bundle_fixture_files_have_no_literal_escaped_newlines() -> None:
    for path in (FIXTURE_PATH, REPORT_PATH):
        assert bytes([92, 110]) not in path.read_bytes(), path


def test_review_bundle_test_file_is_not_compressed() -> None:
    source = THIS_TEST_PATH.read_text(encoding="utf-8")

    assert "def test_complete_fixture_file_passes" in source
    assert source.count(f"{LINE_FEED}def test_") >= 15


def test_public_safe_boundary_scan_for_bundle_check_files() -> None:
    lowered = _combined_touched_text().lower()

    for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
        assert term.lower() not in lowered


def test_prohibited_claim_scan_for_bundle_check_files() -> None:
    lowered = _combined_touched_text().lower()

    for phrase in PROHIBITED_AFFIRMATIVE_CLAIMS:
        phrase_lower = phrase.lower()
        for match in re.finditer(re.escape(phrase_lower), lowered):
            context = lowered[max(0, match.start() - 256) : match.end() + 160]
            assert any(marker in context for marker in BOUNDARY_MARKERS), context


def _without_section(section: str) -> str:
    lines = DEFAULT_SAMPLE_BUNDLE.splitlines()
    return LINE_FEED.join(line for line in lines if not line.lower().startswith(section.lower())) + LINE_FEED


def _combined_touched_text() -> str:
    return LINE_FEED.join((ROOT / path).read_text(encoding="utf-8") for path in TOUCHED_PUBLIC_FILES)
