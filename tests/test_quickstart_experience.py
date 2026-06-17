from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_quickstart_demo_command_passes() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "permea_demo.py")],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert completed.returncode == 0
    assert "Permea Core quickstart demo" in completed.stdout
    assert "Example package discovery:" in completed.stdout
    assert "Validator execution:" in completed.stdout
    assert "Evidence and claim boundaries:" in completed.stdout
    assert "Status: PASS" in completed.stdout


def test_quickstart_demo_discovers_all_public_examples() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "permea_demo.py")],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )

    for example in (
        "examples/bbb_peptide_reference_example",
        "examples/expression_engineering_reference_example",
        "examples/synthetic_reference_example",
    ):
        assert example in completed.stdout


def test_quickstart_docs_point_to_demo_and_boundaries() -> None:
    quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    for text in (quickstart, readme):
        assert "python3 scripts/permea_demo.py" in text
        assert "docs/evidence/evidence-index.md" in text
        assert "docs/claims/claim-registry.md" in text

    for non_claim in (
        "no wet-lab validation by Permea",
        "no clinical efficacy claim",
        "no model performance claim",
        "no solved-delivery claim",
    ):
        assert non_claim in quickstart
