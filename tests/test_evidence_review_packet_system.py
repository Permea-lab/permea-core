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

PACKET_IDS = tuple(PACKET_OUTPUTS)
PACKET_ID = "p-core-053-artifact-consistency-system"
PACKET_MD = ROOT / PACKET_OUTPUTS[PACKET_ID]["markdown"]
PACKET_JSON = ROOT / PACKET_OUTPUTS[PACKET_ID]["json"]
TOUCHED_PUBLIC_FILES = (
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/reports/README.md",
    "docs/reports/p-core-054-evidence-review-packet-system-v0.md",
    "docs/reports/p-core-059-review-packet-expansion-v0.md",
    "docs/review/README.md",
    "docs/review/review-packet-system.md",
    "docs/review/packets/README.md",
    "scripts/permea_review_packet.py",
    "scripts/verify_review_packet_raw_urls.py",
    "src/permea_core/review_packets/__init__.py",
    "src/permea_core/review_packets/packets.py",
    "tests/test_evidence_review_packet_system.py",
    "tests/test_review_packet_raw_url_verification.py",
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
    assert f"Review packets generated: {len(PACKET_IDS)}" in first
    for packet_id in PACKET_IDS:
        assert packet_id in first


def test_review_packet_generation_result_structure() -> None:
    result = generate_review_packets(ROOT)

    assert result["status"] == "PASS"
    assert result["packet_count"] == len(PACKET_IDS)
    assert [packet["packet_id"] for packet in result["packets"]] == list(PACKET_IDS)
    for packet_id in PACKET_IDS:
        assert (ROOT / PACKET_OUTPUTS[packet_id]["markdown"]).exists()
        assert (ROOT / PACKET_OUTPUTS[packet_id]["json"]).exists()


def test_review_packet_json_contains_required_fields() -> None:
    for packet_id in PACKET_IDS:
        payload = _packet_payload(packet_id)

        for field in (
            "packet_id",
            "title",
            "artifact_path",
            "artifact_type",
            "purpose",
            "related_evidence_report_links",
            "validation_commands",
            "raw_readability_notes",
            "claim_boundary_notes",
            "reviewer_checklist",
            "limitations",
        ):
            assert field in payload

        assert payload["packet_id"] == packet_id
        assert (ROOT / payload["artifact_path"]).exists(), payload["artifact_path"]
        for field in (
            "related_evidence_report_links",
            "validation_commands",
            "raw_readability_notes",
            "claim_boundary_notes",
            "reviewer_checklist",
            "limitations",
        ):
            assert payload[field], f"{packet_id} missing {field}"


def test_review_packet_links_existing_artifacts() -> None:
    for packet_id in PACKET_IDS:
        payload = _packet_payload(packet_id)

        for path in payload["related_evidence_report_links"]:
            assert (ROOT / path).exists(), f"{packet_id}: {path}"

    assert "scripts/permea_artifacts.py" in _packet_payload(PACKET_ID)["related_evidence_report_links"]
    assert "src/permea_core/consistency/artifacts.py" in _packet_payload(PACKET_ID)["related_evidence_report_links"]
    assert "docs/reports/p-core-053-artifact-consistency-system-v0.md" in _packet_payload(PACKET_ID)["related_evidence_report_links"]
    assert "scripts/permea_reproduce.py" in _packet_payload("p-core-032-reproducibility-bundle")["related_evidence_report_links"]
    assert "scripts/permea_evaluate.py" in _packet_payload("p-core-034-evaluation-bundle")["related_evidence_report_links"]
    assert "scripts/permea_evidence.py" in _packet_payload("p-core-030-evidence-surface-layer")["related_evidence_report_links"]


def test_review_packet_markdown_contains_review_sections() -> None:
    for packet_id in PACKET_IDS:
        text = _packet_markdown(packet_id)

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
        assert "```bash\npython3 scripts/permea_review_packet.py\n```" in text
        assert "does not create scientific evidence" in text

    assert "```bash\npython3 scripts/permea_artifacts.py\n```" in _packet_markdown(PACKET_ID)
    assert "```bash\npython3 scripts/permea_reproduce.py\n```" in _packet_markdown("p-core-032-reproducibility-bundle")
    assert "```bash\npython3 scripts/permea_evaluate.py\n```" in _packet_markdown("p-core-034-evaluation-bundle")
    assert "```bash\npython3 scripts/permea_evidence.py\n```" in _packet_markdown("p-core-030-evidence-surface-layer")


def test_review_packet_markdown_is_physical_multiline_text() -> None:
    for packet_id in PACKET_IDS:
        raw = _packet_markdown_path(packet_id).read_bytes()
        text = raw.decode("utf-8")
        lines = text.splitlines()
        payload = _packet_payload(packet_id)

        assert raw.endswith(b"\n")
        assert raw.count(b"\n") >= 70
        assert b"\\n" not in raw
        assert len(lines) >= 70
        assert lines[0] == f"# {payload['title']}"
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
    packet_paths = []
    for packet_id in PACKET_IDS:
        packet_paths.append((_packet_markdown_path(packet_id), 40))
        packet_paths.append((_packet_json_path(packet_id), 10))

    for packet_path, minimum_lines in packet_paths:
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
    for packet_id in PACKET_IDS:
        raw_bytes = _packet_json_path(packet_id).read_bytes()
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
    assert "docs/review/packets/p-core-032-reproducibility-bundle.md" in review_hub
    assert "docs/review/packets/p-core-034-evaluation-bundle.md" in review_hub
    assert "docs/review/packets/p-core-030-evidence-surface-layer.md" in review_hub
    assert "p-core-054-evidence-review-packet-system-v0.md" in reports
    assert "p-core-059-review-packet-expansion-v0.md" in reports


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
    paths = [ROOT / path for path in TOUCHED_PUBLIC_FILES]
    for packet_id in PACKET_IDS:
        paths.append(_packet_markdown_path(packet_id))
        paths.append(_packet_json_path(packet_id))
    return "\n".join(path.read_text(encoding="utf-8") for path in paths)


def _packet_markdown_path(packet_id: str) -> Path:
    return ROOT / PACKET_OUTPUTS[packet_id]["markdown"]


def _packet_json_path(packet_id: str) -> Path:
    return ROOT / PACKET_OUTPUTS[packet_id]["json"]


def _packet_markdown(packet_id: str) -> str:
    return _packet_markdown_path(packet_id).read_text(encoding="utf-8")


def _packet_payload(packet_id: str) -> dict[str, object]:
    return json.loads(_packet_json_path(packet_id).read_text(encoding="utf-8"))
