from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.evidence.matrix import (
    CAPABILITY_ROWS,
    EXPLICIT_NON_CLAIMS,
    PASS,
    collect_evidence_matrix,
    render_evidence_matrix,
    write_evidence_matrix,
)


REQUIRED_JSON_KEYS = (
    "matrix_id",
    "matrix_type",
    "generated_at",
    "overview",
    "implemented_capabilities",
    "artifact_evidence",
    "command_evidence",
    "validation_evidence",
    "explicit_non_claims",
    "limitations",
    "next_evidence_steps",
)

REQUIRED_MARKDOWN_SECTIONS = (
    "## Overview",
    "## Implemented Capabilities",
    "## Artifact Evidence",
    "## Command Evidence",
    "## Validation Evidence",
    "## Explicit Non-Claims",
    "## Limitations",
    "## Next Evidence Steps",
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


def test_evidence_matrix_generation_returns_pass() -> None:
    matrix = collect_evidence_matrix(ROOT)

    assert matrix["status"] == PASS
    assert matrix["matrix_id"] == "permea_core_public_evidence_matrix"


def test_generated_markdown_includes_required_sections() -> None:
    rendered = render_evidence_matrix(collect_evidence_matrix(ROOT))

    for section in REQUIRED_MARKDOWN_SECTIONS:
        assert section in rendered


def test_generated_json_includes_required_keys(tmp_path: Path) -> None:
    result = write_evidence_matrix(tmp_path, ROOT)
    payload = json.loads((tmp_path / "EVIDENCE_MATRIX.json").read_text(encoding="utf-8"))

    for key in REQUIRED_JSON_KEYS:
        assert key in payload
    assert payload["status"] == PASS
    assert payload["output_paths"] == result["output_paths"]


def test_generated_matrix_includes_required_capabilities() -> None:
    matrix = collect_evidence_matrix(ROOT)
    capabilities = {row["capability"] for row in matrix["implemented_capabilities"]}

    assert capabilities == {capability for capability, _boundary, _paths, _next in CAPABILITY_ROWS}
    assert all(row["artifact_status"] == PASS for row in matrix["implemented_capabilities"])


def test_generated_markdown_includes_explicit_non_claims() -> None:
    rendered = render_evidence_matrix(collect_evidence_matrix(ROOT))

    for claim in EXPLICIT_NON_CLAIMS:
        assert f"- {claim}" in rendered


def test_paths_are_relative_public_safe(tmp_path: Path) -> None:
    result = write_evidence_matrix(tmp_path, ROOT)
    rendered = render_evidence_matrix(result)

    assert str(ROOT) not in rendered
    for item in result["artifact_evidence"]:
        assert not item["path"].startswith("/")
    for row in result["implemented_capabilities"]:
        assert all(not path.startswith("/") for path in row["artifact_paths"])


def test_cli_exits_zero_and_writes_outputs() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_evidence_matrix.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "PASS evidence matrix generation" in completed.stdout
    assert (ROOT / "docs" / "examples" / "generated" / "EVIDENCE_MATRIX.md").exists()
    assert (ROOT / "docs" / "examples" / "generated" / "EVIDENCE_MATRIX.json").exists()


def test_unsupported_claim_phrases_are_absent() -> None:
    rendered = render_evidence_matrix(collect_evidence_matrix(ROOT))
    payload = json.dumps(collect_evidence_matrix(ROOT), sort_keys=True)
    combined = f"{rendered}\n{payload}"

    for parts in UNSUPPORTED_CLAIM_PHRASE_PARTS:
        phrase = "".join(parts) if parts == ("SO", "TA") else " ".join(parts)
        assert phrase not in combined
