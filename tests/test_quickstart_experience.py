from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
#: Files that necessarily contain prohibited terms because they are themselves term guards.
#: Term lists are written as fragments joined at import, so a guard definition does not match
#: itself when scanned.
#:
#: Excluded by exact relative path, never by glob or filename pattern. ``_scanned_paths``
#: verifies every entry exists AND actually defines a prohibited-terms list, so this cannot be
#: quietly pointed at ordinary source to bury a real leak.
GUARD_FILES = (
    "tests/test_quickstart_experience.py",
    "tests/test_artifact_consistency_system.py",
    "tests/test_evidence_review_packet_system.py",
    "tests/test_review_bundle_completeness_check.py",
    "tests/test_review_navigation_consistency.py",
    "tests/test_review_packet_coverage_check.py",
)
GUARD_MARKER = "PROHIBITED_PUBLIC" + "_SAFETY_TERMS"
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
    # --- deployment identity -----------------------------------------------------------
    # Matched as SUBSTRINGS, case-insensitively, deliberately: a whole-word match would miss
    # exactly the forms that leak, e.g. a vendor hostname inside a URL.
    #
    # Written as fragments joined at import so this list does not match itself; GUARD_FILES is
    # what actually keeps this file out of its own scan.
    "Friend" + "li",
    "fl" + "p_",
    "Dedicated " + "Endpoint",
    "Mega" + "zoneCloud",  # prophylactic: no current hit, prohibited before one can appear
    "EXA" + "ONE",
    # --- competition framing -----------------------------------------------------------
    # Bare "demo" is unusable as a term: scripts/permea_demo.py, "quickstart demo", and
    # several test names use it legitimately, so it would fire constantly on things that are
    # fine. Scoped to the phrases that actually carry the framing.
    "demo surface",
    "demo-visible",
    "for a demo",
    "domestic LLM",  # prophylactic: no current hit
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


def _scanned_paths() -> list[Path]:
    """Every file the broad prohibited-term scan reads, minus this guard file itself.

    Wider than ``TOUCHED_PUBLIC_FILES``, which covers top-level docs only. A term that never
    reaches a doc but sits in shipped package source is still public the moment the repo is.
    """
    paths = [ROOT / path for path in TOUCHED_PUBLIC_FILES]
    paths.append(ROOT / ".env.example")
    paths.extend(sorted((ROOT / "permea_explain").rglob("*.py")))
    paths.extend(sorted((ROOT / "tests").rglob("*.py")))

    excluded = set()
    for relative in GUARD_FILES:
        path = ROOT / relative
        # An exclusion that names a missing file, or a file that is not a term guard, is a
        # hole rather than an exemption. Both are load-bearing: without the marker check,
        # adding a path here would be enough to hide any leak from this scan.
        assert path.is_file(), f"excluded guard file does not exist: {relative}"
        assert GUARD_MARKER in path.read_text(encoding="utf-8"), (
            f"excluded file is not a term guard (no {GUARD_MARKER}): {relative}"
        )
        excluded.add(path.resolve())

    kept = [path for path in paths if path.resolve() not in excluded]
    # A silently-empty scan would report "no leaks" for the same reason a correct one does.
    assert kept, "prohibited-term scan matched no files at all"
    return kept


def test_public_sources_avoid_prohibited_terms() -> None:
    violations: list[str] = []

    for path in _scanned_paths():
        relative = path.relative_to(ROOT)
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            lowered = line.lower()
            for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
                if term.lower() in lowered:
                    violations.append(f"{relative}:{lineno}: {term!r} -- {line.strip()}")

    assert not violations, "prohibited terms found:\n" + "\n".join(violations)
