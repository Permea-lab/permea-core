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

from permea_core.review_packets import PACKET_OUTPUTS  # noqa: E402
from permea_core.review_packets.coverage import (  # noqa: E402
    PASS,
    check_review_packet_coverage,
    render_coverage_summary,
)

TOUCHED_PUBLIC_FILES = (
    "scripts/check_review_packet_coverage.py",
    "src/permea_core/review_packets/coverage.py",
    "tests/test_review_packet_coverage_check.py",
    "docs/reports/p-core-060b-review-packet-coverage-check-v0.md",
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
    "wet-lab " + "validation",
    "clinical " + "efficacy",
    "biological " + "result",
    "model " + "performance",
    "benchmark " + "result",
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


def test_review_packet_coverage_check_passes() -> None:
    result = check_review_packet_coverage(ROOT)

    assert result["status"] == PASS
    assert result["packet_count"] == len(PACKET_OUTPUTS)
    assert result["packet_ids"] == list(PACKET_OUTPUTS)
    assert all(check["status"] == PASS for check in result["checks"])


def test_review_packet_coverage_summary_is_deterministic() -> None:
    first = render_coverage_summary(check_review_packet_coverage(ROOT))
    second = render_coverage_summary(check_review_packet_coverage(ROOT))

    assert first == second
    assert "Permea Core review packet coverage check" in first
    assert "Status: PASS" in first
    assert "Review packets checked:" in first
    assert "Claim-boundary reminder:" in first


def test_review_packet_coverage_cli_text_and_json() -> None:
    text_completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_review_packet_coverage.py")],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    json_completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_review_packet_coverage.py"), "--json"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )

    payload = json.loads(json_completed.stdout)
    assert "Status: PASS" in text_completed.stdout
    assert payload["status"] == PASS
    assert payload["packet_count"] == len(PACKET_OUTPUTS)


def test_review_packet_coverage_required_checks_exist() -> None:
    result = check_review_packet_coverage(ROOT)
    check_names = [check["name"] for check in result["checks"]]

    assert "packet definitions match output map" in check_names
    for packet_id, outputs in PACKET_OUTPUTS.items():
        assert f"{packet_id} markdown output exists" in check_names
        assert f"{packet_id} json output exists" in check_names
        assert f"{packet_id} raw markdown target covered" in check_names
        assert f"{packet_id} raw json target covered" in check_names
        assert Path(outputs["markdown"]).name in (ROOT / "docs/review/packets/README.md").read_text(encoding="utf-8")


def test_public_safe_boundary_scan_for_coverage_check_files() -> None:
    lowered = _combined_touched_text().lower()

    for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
        assert term.lower() not in lowered


def test_prohibited_claim_scan_for_coverage_check_files() -> None:
    lowered = _combined_touched_text().lower()

    for phrase in PROHIBITED_AFFIRMATIVE_CLAIMS:
        phrase_lower = phrase.lower()
        for match in re.finditer(re.escape(phrase_lower), lowered):
            context = lowered[max(0, match.start() - 256) : match.end() + 160]
            assert any(marker in context for marker in BOUNDARY_MARKERS), context


def _combined_touched_text() -> str:
    return "\n".join((ROOT / path).read_text(encoding="utf-8") for path in TOUCHED_PUBLIC_FILES)
