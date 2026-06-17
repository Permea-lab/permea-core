from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOUCHED_PUBLIC_FILES = (
    "OPEN_THIS_FIRST.md",
    "QUICKSTART.md",
    "README.md",
    "REVIEW_HUB.md",
    "docs/claims/claim-registry.md",
    "docs/evidence/EVIDENCE-042-quickstart-experience-layer.md",
    "docs/evidence/README.md",
    "docs/evidence/evidence-index.md",
    "docs/reports/p-core-042-quickstart-experience-layer-v0.md",
    "scripts/permea_demo.py",
)
PROHIBITED_PUBLIC_SAFETY_TERMS = (
    "AI Champion",
    "H100",
    "KORA",
    "private infrastructure",
    "sponsorship",
    "cloud credits",
    "private handoffs",
    "local-only notes",
    "ChatGPT",
    "Codex",
    "prompt workflow",
)
PROHIBITED_AFFIRMATIVE_CLAIMS = (
    "wet-lab validation",
    "clinical efficacy",
    "model performance superiority",
    "SOTA",
    "solved delivery",
    "BBB performance",
    "expression improvement",
    "biological outcome validation",
)
NEGATION_MARKERS = (
    "no ",
    "not ",
    "does not ",
    "without ",
    "unsupported ",
    "must not ",
    "must not claim",
    "does not claim",
    "not currently claim",
)


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
    assert "Evaluation, evidence, and claim boundaries:" in completed.stdout
    assert "docs/examples/generated/EVALUATION_PACKET.md" in completed.stdout
    assert "docs/examples/generated/EVIDENCE_MATRIX.md" in completed.stdout
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


def test_quickstart_demo_output_is_deterministic() -> None:
    command = [sys.executable, str(ROOT / "scripts" / "permea_demo.py")]
    first = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout
    second = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout

    assert first == second


def test_touched_public_files_avoid_prohibited_public_safety_terms() -> None:
    combined = _combined_touched_text()

    for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
        assert term.lower() not in combined.lower()


def test_touched_public_files_do_not_make_prohibited_claims() -> None:
    combined = _combined_touched_text()
    lowered = combined.lower()

    for phrase in PROHIBITED_AFFIRMATIVE_CLAIMS:
        start = 0
        phrase_lower = phrase.lower()
        while True:
            index = lowered.find(phrase_lower, start)
            if index == -1:
                break
            context = lowered[max(0, index - 256) : index + len(phrase_lower) + 128]
            assert any(marker in context for marker in NEGATION_MARKERS), context
            start = index + len(phrase_lower)


def _combined_touched_text() -> str:
    return "\n".join(
        (ROOT / path).read_text(encoding="utf-8") for path in TOUCHED_PUBLIC_FILES
    )
