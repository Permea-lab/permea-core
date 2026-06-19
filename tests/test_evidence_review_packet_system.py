from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.review_packets import (  # noqa: E402
    PACKET_OUTPUTS,
    generate_review_packets,
)

PACKET_ID = "p-core-053-artifact-consistency-system"
PACKET_MD = ROOT / PACKET_OUTPUTS[PACKET_ID]["markdown"]
PACKET_JSON = ROOT / PACKET_OUTPUTS[PACKET_ID]["json"]
TOUCHED_PUBLIC_FILES = (
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/README.md",
    "docs/reports/p-core-054-evidence-review-packet-system-v0.md",
    "docs/review/review-packet-system.md",
    "docs/review/packets/README.md",
    "docs/review/packets/p-core-053-artifact-consistency-system.md",
    "scripts/permea_review_packet.py",
    "src/permea_core/review_packets/__init__.py",
    "src/permea_core/review_packets/packets.py",
    "tests/test_evidence_review_packet_system.py",
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
    "biological " + "results",
    "model " + "performance",
    "solved " + "delivery",
    "in-vivo",
    "in vivo",
)
BOUNDARY_MARKERS = (
    "no ",
    "not ",
    "does not ",
    "do not ",
    "without ",
    "limitations",
    "boundary",
)


def test_review_packet_cli_executes_and_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts/permea_review_packet.py")]
    first = subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True).stdout
    first_markdown = PACKET_MD.read_text(encoding="utf-8")
    first_json = PACKET_JSON.read_text(encoding="utf-8")

    second = subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True).stdout
    second_markdown = PACKET_MD.read_text(encoding="utf-8")
    second_json = PACKET_JSON.read_text(encoding="utf-8")

    assert first == second
    assert first_markdown == second_markdown
    assert first_json == second_json
    assert "Evidence Review Packet System Ready" in first
    assert "Review packets generated: 1" in first


def test_review_packet_generation_result_structure() -> None:
    result = generate_review_packets(ROOT)

    assert result["status"] == "PASS"
    assert result["packet_count"] == 1
    assert result["packets"][0]["packet_id"] == PACKET_ID
    assert PACKET_MD.exists()
    assert PACKET_JSON.exists()


def test_review_packet_json_contains_required_fields() -> None:
    payload = json.loads(PACKET_JSON.read_text(encoding="utf-8"))

    for field in (
        "packet_id",
        "title",
        "artifact_path",
        "artifact_type",
        "purpose",
        "related_evidence_report_links",
        "validation_commands",
        "claim_boundary_notes",
        "reviewer_checklist",
        "limitations",
    ):
        assert field in payload

    assert payload["packet_id"] == PACKET_ID
    assert payload["artifact_path"] == "docs/artifacts/README.md"


def test_review_packet_links_existing_artifacts() -> None:
    payload = json.loads(PACKET_JSON.read_text(encoding="utf-8"))

    for path in payload["related_evidence_report_links"]:
        assert (ROOT / path).exists(), path

    assert "scripts/permea_artifacts.py" in payload["related_evidence_report_links"]
    assert "src/permea_core/consistency/artifacts.py" in payload["related_evidence_report_links"]
    assert "docs/reports/p-core-053-artifact-consistency-system-v0.md" in payload["related_evidence_report_links"]


def test_review_packet_markdown_contains_review_sections() -> None:
    text = PACKET_MD.read_text(encoding="utf-8")

    for heading in (
        "## Packet Metadata",
        "## Related Evidence And Report Links",
        "## Validation Commands",
        "## Claim Boundary Notes",
        "## Reviewer Checklist",
        "## Limitations",
    ):
        assert heading in text

    assert "| Field | Value |" in text
    assert "| Review surface | Link |" in text
    assert "```bash\npython3 scripts/permea_artifacts.py\n```" in text
    assert "```bash\npython3 scripts/permea_review_packet.py\n```" in text
    assert "python3 scripts/permea_artifacts.py" in text
    assert "does not create scientific evidence" in text


def test_review_packet_markdown_is_physical_multiline_text() -> None:
    raw = PACKET_MD.read_bytes()
    text = raw.decode("utf-8")
    lines = text.splitlines()

    assert raw.endswith(b"\n")
    assert raw.count(b"\n") >= 70
    assert b"\\n" not in raw
    assert len(lines) >= 70
    assert lines[0] == "# P-CORE-053 Artifact Consistency System Review Packet"
    assert "## Packet Metadata" in lines
    assert "## Validation Commands" in lines
    assert "## Reviewer Checklist" in lines
    assert "## Limitations" in lines


def test_generated_packet_files_have_no_hidden_unicode_or_bad_line_endings() -> None:
    bidi_markers = {
        "\u061c",
        "\u200e",
        "\u200f",
        "\u202a",
        "\u202b",
        "\u202c",
        "\u202d",
        "\u202e",
        "\u2066",
        "\u2067",
        "\u2068",
        "\u2069",
    }
    zero_width = {"\u200b", "\u200c", "\u200d", "\ufeff"}

    for packet_path, minimum_lines in ((PACKET_MD, 40), (PACKET_JSON, 10)):
        raw = packet_path.read_bytes()
        text = raw.decode("utf-8")

        assert raw.count(b"\n") >= minimum_lines
        assert raw.endswith(b"\n")
        assert b"\r" not in raw
        assert b"\r\n" not in raw
        assert b"\\n" not in raw
        assert "\u2028".encode("utf-8") not in raw
        assert "\u2029".encode("utf-8") not in raw

        suspicious = []
        for index, char in enumerate(text):
            category = unicodedata.category(char)
            bidi = unicodedata.bidirectional(char)
            if char in {"\n", "\t"}:
                continue
            if (
                category.startswith("C")
                or char in bidi_markers
                or char in zero_width
                or bidi in {"RLO", "LRO", "RLE", "LRE", "PDF", "RLI", "LRI", "FSI", "PDI"}
            ):
                suspicious.append((index, f"U+{ord(char):04X}", category, bidi))

        assert suspicious == []


def test_review_packet_json_is_pretty_printed_with_stable_key_order() -> None:
    raw_bytes = PACKET_JSON.read_bytes()
    raw = raw_bytes.decode("utf-8")
    payload = json.loads(raw)

    assert raw_bytes.endswith(b"\n")
    assert raw_bytes.count(b"\n") >= 35
    assert b"\\n" not in raw_bytes
    assert raw.startswith('{\n  "artifact_path":')
    assert '\n  "validation_commands": [\n' in raw
    assert raw == json.dumps(payload, indent=2, sort_keys=True) + "\n"


def test_review_packet_surface_integration() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    open_first = (ROOT / "OPEN_THIS_FIRST.md").read_text(encoding="utf-8")
    review_hub = (ROOT / "REVIEW_HUB.md").read_text(encoding="utf-8")
    reports = (ROOT / "docs/reports/README.md").read_text(encoding="utf-8")

    assert "python3 scripts/permea_review_packet.py" in readme
    assert "docs/review/review-packet-system.md" in open_first
    assert "docs/review/packets/p-core-053-artifact-consistency-system.md" in review_hub
    assert "p-core-054-evidence-review-packet-system-v0.md" in reports


def test_public_safe_boundary_scan_for_review_packet_files() -> None:
    lowered = _combined_touched_text().lower()

    for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
        assert term.lower() not in lowered


def test_prohibited_claim_scan_for_review_packet_files() -> None:
    lowered = _combined_touched_text().lower()

    for phrase in PROHIBITED_AFFIRMATIVE_CLAIMS:
        phrase_lower = phrase.lower()
        for match in re.finditer(re.escape(phrase_lower), lowered):
            context = lowered[max(0, match.start() - 256) : match.end() + 160]
            assert any(marker in context for marker in BOUNDARY_MARKERS), context


def _combined_touched_text() -> str:
    return "\n".join((ROOT / path).read_text(encoding="utf-8") for path in TOUCHED_PUBLIC_FILES)
