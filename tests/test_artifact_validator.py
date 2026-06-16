from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.validation.artifact_validator import (  # noqa: E402
    FAIL,
    PASS,
    render_summary,
    summarize_results,
    validate_artifact,
    validate_builtin_artifacts,
)


def test_builtin_artifact_validator_passes() -> None:
    summary = validate_builtin_artifacts(ROOT)

    assert summary["status"] == PASS
    assert summary["artifacts_checked"] == 8
    assert summary["pass_count"] == 8
    assert summary["fail_count"] == 0


def test_result_model_contains_required_keys() -> None:
    result = validate_artifact(
        ROOT / "docs/examples/generated/dataset_cards/b3pred_dataset3.md",
        ROOT,
    )

    assert result["status"] == PASS
    for key in (
        "artifact_path",
        "artifact_type",
        "status",
        "checks",
        "issues",
        "warnings",
        "non_claims_seen",
        "evidence_links_seen",
    ):
        assert key in result
    assert result["artifact_path"] == "docs/examples/generated/dataset_cards/b3pred_dataset3.md"
    assert result["artifact_type"] == "dataset_card"
    assert any(check["name"] == "schema_presence:spec" for check in result["checks"])
    assert any(check["name"] == "schema_presence:schema" for check in result["checks"])


def test_missing_required_field_fails(tmp_path: Path) -> None:
    artifact = tmp_path / "docs/examples/generated/dataset_cards/bad.md"
    artifact.parent.mkdir(parents=True)
    artifact.write_text(
        "\n".join(
            [
                "# Dataset Card: Bad",
                "",
                "## Source IDs",
                "",
                "- example",
                "",
                "## Benchmark IDs",
                "",
                "- example",
                "",
                "## Acquisition Status",
                "",
                "not-started",
                "",
                "## Redistribution Status",
                "",
                "not-confirmed",
                "",
                "## Claim Boundary",
                "",
                "metadata only; no dataset downloaded, no redistribution rights confirmed, and no wet-lab validation by Permea",
            ]
        ),
        encoding="utf-8",
    )

    result = validate_artifact(artifact, tmp_path)

    assert result["status"] == FAIL
    assert any("missing required section: Dataset ID" in issue for issue in result["issues"])


def test_unsupported_claim_fails(tmp_path: Path) -> None:
    artifact = tmp_path / "docs/examples/generated/benchmark_cards/bad.md"
    artifact.parent.mkdir(parents=True)
    artifact.write_text(
        "\n".join(
            [
                "# Benchmark Card: bad",
                "",
                "## Benchmark ID",
                "",
                "bad",
                "",
                "## Task Name",
                "",
                "bad_task",
                "",
                "## Dataset Card",
                "",
                "dataset_cards/bad.md",
                "",
                "## Output Artifacts",
                "",
                "- metrics.json",
                "- ranking.csv",
                "- manifest.yaml",
                "- evidence_cards.json",
                "",
                "## Limitations",
                "",
                "- none",
                "",
                "## Claim Boundary",
                "",
                "This benchmark establishes " + "clinical " + "efficacy.",
            ]
        ),
        encoding="utf-8",
    )

    result = validate_artifact(artifact, tmp_path)

    assert result["status"] == FAIL
    assert any("unsupported claim phrase" in issue for issue in result["issues"])


def test_missing_non_claim_fails(tmp_path: Path) -> None:
    artifact = tmp_path / "docs/examples/generated/dataset_cards/bad.md"
    artifact.parent.mkdir(parents=True)
    artifact.write_text(
        "\n".join(
            [
                "# Dataset Card: Bad",
                "",
                "## Dataset ID",
                "",
                "bad",
                "",
                "## Source IDs",
                "",
                "- example",
                "",
                "## Benchmark IDs",
                "",
                "- example",
                "",
                "## Acquisition Status",
                "",
                "not-started",
                "",
                "## Redistribution Status",
                "",
                "not-confirmed",
                "",
                "## Claim Boundary",
                "",
                "metadata only; no dataset downloaded and no redistribution rights confirmed",
            ]
        ),
        encoding="utf-8",
    )

    result = validate_artifact(artifact, tmp_path)

    assert result["status"] == FAIL
    assert any("missing explicit non-claim" in issue for issue in result["issues"])


def test_cli_summary_behavior() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "permea_check.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "Permea artifact validator" in completed.stdout
    assert "Artifacts checked: 8" in completed.stdout
    assert "Pass count: 8" in completed.stdout
    assert "Next recommended command:" in completed.stdout


def test_render_summary_includes_issue_summary() -> None:
    summary = summarize_results(
        [
            {
                "artifact_path": "example.md",
                "artifact_type": "dataset_card",
                "status": FAIL,
                "checks": [],
                "issues": ["missing field"],
                "warnings": [],
                "non_claims_seen": [],
                "evidence_links_seen": [],
            }
        ]
    )

    rendered = render_summary(summary)

    assert "Status: FAIL" in rendered
    assert "- example.md: missing field" in rendered
