from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.demo.packet import (
    NON_CLAIMS,
    PASS,
    collect_demo_packet,
    render_demo_packet,
    write_demo_packet,
)


REQUIRED_JSON_KEYS = (
    "packet_id",
    "packet_type",
    "generated_at",
    "overview",
    "available_commands",
    "input_artifacts",
    "generated_artifacts",
    "dry_run_summary",
    "unified_generation_summary",
    "unified_validation_summary",
    "artifact_index_path",
    "dry_run_report_paths",
    "non_claims",
    "limitations",
    "next_action",
)

REQUIRED_MARKDOWN_SECTIONS = (
    "## Overview",
    "## One-command demo",
    "## Regenerate artifacts",
    "## Validate artifacts",
    "## Artifact families",
    "## Dry-run output",
    "## Public artifact index",
    "## Explicit Non-Claims",
    "## Limitations",
    "## Next Steps",
)

UNSUPPORTED_CLAIM_PHRASE_PARTS = (
    ("wet-lab", "validated"),
    ("clinical", "efficacy"),
    ("universal", "predictor"),
    ("solved", "delivery"),
    ("bioRxiv", "ready"),
    ("SO", "TA"),
    ("data has been", "downloaded"),
    ("redistribution rights have been", "confirmed"),
    ("acquisition has been", "executed"),
    ("model performance has been", "measured"),
)


def test_demo_packet_generation_returns_pass() -> None:
    packet = collect_demo_packet(ROOT)

    assert packet["status"] == PASS
    assert packet["packet_id"] == "permea_core_public_demo_packet"


def test_generated_markdown_includes_required_sections() -> None:
    rendered = render_demo_packet(collect_demo_packet(ROOT))

    for section in REQUIRED_MARKDOWN_SECTIONS:
        assert section in rendered


def test_generated_json_includes_required_keys(tmp_path: Path) -> None:
    result = write_demo_packet(tmp_path, ROOT)
    payload = json.loads((tmp_path / "DEMO_PACKET.json").read_text(encoding="utf-8"))

    for key in REQUIRED_JSON_KEYS:
        assert key in payload
    assert payload["status"] == PASS
    assert payload["output_paths"] == result["output_paths"]


def test_generated_markdown_includes_explicit_non_claims() -> None:
    rendered = render_demo_packet(collect_demo_packet(ROOT))

    for claim in NON_CLAIMS:
        assert f"- {claim}" in rendered


def test_paths_are_relative_public_safe(tmp_path: Path) -> None:
    result = write_demo_packet(tmp_path, ROOT)
    rendered = render_demo_packet(result)

    assert str(ROOT) not in rendered
    for key in ("input_artifacts", "generated_artifacts", "artifact_families"):
        for item in result[key]:
            assert not item["path"].startswith("/")
    assert not result["artifact_index_path"].startswith("/")
    assert all(not path.startswith("/") for path in result["dry_run_report_paths"])


def test_cli_exits_zero_and_writes_outputs() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_demo_packet.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS demo packet generation" in completed.stdout
    assert (ROOT / "docs" / "examples" / "generated" / "DEMO_PACKET.md").exists()
    assert (ROOT / "docs" / "examples" / "generated" / "DEMO_PACKET.json").exists()


def test_unsupported_claim_phrases_are_absent() -> None:
    rendered = render_demo_packet(collect_demo_packet(ROOT))
    payload = json.dumps(collect_demo_packet(ROOT), sort_keys=True)
    combined = f"{rendered}\n{payload}"

    for parts in UNSUPPORTED_CLAIM_PHRASE_PARTS:
        phrase = "".join(parts) if parts == ("SO", "TA") else " ".join(parts)
        assert phrase not in combined
