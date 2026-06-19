from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT_PUBLIC_HEAD = "6a3d60ce06f7a7f53179a406d4297edf22c71382"
STALE_PUBLIC_HEADS = (
    "ff67926773c86cecfec43d3af3f5fecb454464fa",
    "db1fd4bb1e5d6b216a34b65db198786df5bda59e",
    "5ab200290fe77829f6f5483da983efc34e04b1a0",
    "a5595eb3be23e6a19c7f9166591e9a499718b793",
)
REVIEW_NAVIGATION_FILES = (
    "README.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "docs/architecture/README.md",
    "docs/artifacts/README.md",
    "docs/reports/README.md",
    "docs/reports/p-core-051-long-run-supervisor-pilot-v0.md",
    "docs/reports/p-core-052-autonomous-queue-pilot-v0.md",
    "docs/reports/p-core-053-artifact-consistency-system-v0.md",
    "docs/reports/p-core-054-evidence-review-packet-system-v0.md",
    "docs/reports/p-core-061-autonomous-review-merge-loop-pilot-v0.md",
)
REQUIRED_NAVIGATION_TARGETS = (
    "docs/architecture/README.md",
    "docs/artifacts/README.md",
    "docs/reports/README.md",
    "docs/lineage/README.md",
    "docs/reports/p-core-051-long-run-supervisor-pilot-v0.md",
    "docs/reports/p-core-052-autonomous-queue-pilot-v0.md",
    "docs/reports/p-core-053-artifact-consistency-system-v0.md",
    "docs/reports/p-core-054-evidence-review-packet-system-v0.md",
    "docs/review/review-loop-operating-standard.md",
    "docs/reports/p-core-061-autonomous-review-merge-loop-pilot-v0.md",
    "scripts/permea_artifacts.py",
    "scripts/permea_review_packet.py",
    "scripts/permea_lineage.py",
    "scripts/permea_review.py",
)
PROHIBITED_PUBLIC_SAFETY_TERMS = (
    "AI " + "Champion",
    "H" + "100",
    "K-" + "EXAONE",
    "KO" + "RA",
    "competition " + "references",
    "private " + "infrastructure",
    "sponsor" + "ship",
    "cloud " + "credits",
    "private " + "repositories",
    "local-only " + "workflows",
    "Chat" + "GPT",
    "Co" + "dex",
    "prompt " + "workflow",
    "private " + "handoff",
)
PROHIBITED_AFFIRMATIVE_CLAIMS = (
    "wet-lab " + "validation",
    "biological " + "efficacy",
    "therapeutic " + "outcomes",
    "BBB " + "success",
    "solved " + "delivery",
    "SOTA " + "performance",
    "clinical " + "efficacy",
    "clinical " + "evidence",
    "expression " + "improvement",
)
BOUNDARY_MARKERS = (
    "no ",
    "not ",
    "does not ",
    "do not ",
    "without ",
    "prohibited ",
    "out of scope",
    "not yet demonstrated",
    "future ",
    "non-claim",
)


def test_review_breadcrumbs_reference_current_public_head() -> None:
    open_first = (ROOT / "OPEN_THIS_FIRST.md").read_text(encoding="utf-8")
    review_hub = (ROOT / "REVIEW_HUB.md").read_text(encoding="utf-8")
    combined = f"{open_first}\n{review_hub}"

    assert CURRENT_PUBLIC_HEAD in open_first
    assert CURRENT_PUBLIC_HEAD in review_hub
    for stale_head in STALE_PUBLIC_HEADS:
        assert stale_head not in combined
    assert ("Review the " + "signal integration branch") not in combined
    assert ("Review the " + "signal integration PR") not in combined
    assert ("Review the P-CORE-051 " + "long-run supervisor pilot PR") not in combined
    assert ("Review the P-CORE-051 " + "long-run supervisor pilot branch") not in combined
    assert ("Review the P-CORE-052 " + "autonomous queue pilot PR") not in combined
    assert ("Review the P-CORE-052 " + "autonomous queue pilot branch") not in combined


def test_review_navigation_targets_are_linked() -> None:
    combined = _combined_review_text()

    for target in REQUIRED_NAVIGATION_TARGETS:
        assert target in combined
    assert "P-CORE-051 long-run supervisor pilot" in combined
    assert "P-CORE-052 autonomous queue pilot" in combined
    assert "P-CORE-053 artifact consistency system" in combined
    assert "P-CORE-054 evidence review packet system" in combined
    assert "Architecture index" in combined
    assert "Artifact consistency" in combined
    assert "Reports index" in combined


def test_architecture_index_links_existing_surfaces() -> None:
    architecture_index = (ROOT / "docs/architecture/README.md").read_text(
        encoding="utf-8"
    )

    for target in (
        "../DD-ARCHITECTURE.md",
        "../SPEC.md",
        "../OSS_OPERATING_DOCS_MAP.md",
        "../decisions/README.md",
        "../adr/ADR-0002-benchmark-first.md",
        "../lineage/lineage-model.md",
        "../artifacts/README.md",
        "../reports/README.md",
        "../review/README.md",
        "../evidence/evidence-map.md",
    ):
        assert target in architecture_index
        assert (ROOT / "docs/architecture" / target).resolve().exists()

    for target in (
        "../evidence/README.md",
        "../benchmarks/README.md",
        "../datasets/README.md",
        "../research/README.md",
        "../integrations/README.md",
        "../claims/claim-registry.md",
    ):
        assert target in architecture_index
        assert (ROOT / "docs/architecture" / target).resolve().exists()

    assert (
        "README -> QUICKSTART -> REVIEW PACKET -> ARCHITECTURE -> EVIDENCE -> LINEAGE -> CLAIMS -> VALIDATION"
        in architecture_index
    )
    assert "python3 scripts/permea_review.py" in architecture_index
    assert "python3 scripts/permea_artifacts.py" in architecture_index
    assert "python3 scripts/validate_permea_artifacts.py" in architecture_index


def test_reports_index_links_current_reports_and_generated_surfaces() -> None:
    reports_index = (ROOT / "docs/reports/README.md").read_text(encoding="utf-8")

    for target in (
        "p-core-050-evidence-lineage-layer-v0.md",
        "p-core-051-long-run-supervisor-pilot-v0.md",
        "p-core-052-autonomous-queue-pilot-v0.md",
        "p-core-053-artifact-consistency-system-v0.md",
        "p-core-061-autonomous-review-merge-loop-pilot-v0.md",
        "../examples/generated/REPRODUCIBILITY_REPORT.md",
        "../examples/generated/EVALUATION_PACKET.md",
        "../examples/generated/ARTIFACT_INDEX.md",
    ):
        assert target in reports_index
        assert (ROOT / "docs/reports" / target).resolve().exists()

    assert (
        "OPEN_THIS_FIRST -> REVIEW_HUB -> REPORTS INDEX -> ARCHITECTURE -> EVIDENCE -> LINEAGE -> CLAIMS -> VALIDATION"
        in reports_index
    )


def test_review_hub_resume_commands_include_current_review_tools() -> None:
    review_hub = (ROOT / "REVIEW_HUB.md").read_text(encoding="utf-8")

    for command in (
        "python3 scripts/permea_lineage.py",
        "python3 scripts/permea_review.py",
        "python3 scripts/permea_artifacts.py",
        "python3 scripts/permea_reproduce.py",
        "python3 scripts/permea_validate.py",
        "python3 scripts/validate_permea_artifacts.py",
        "python3 -m pytest",
    ):
        assert command in review_hub


def test_public_safe_boundary_scan_for_review_navigation_files() -> None:
    lowered = _combined_review_text().lower()

    for term in PROHIBITED_PUBLIC_SAFETY_TERMS:
        assert term.lower() not in lowered


def test_prohibited_claim_scan_for_review_navigation_files() -> None:
    lowered = _combined_review_text().lower()

    for phrase in PROHIBITED_AFFIRMATIVE_CLAIMS:
        phrase_lower = phrase.lower()
        for match in re.finditer(re.escape(phrase_lower), lowered):
            context = lowered[max(0, match.start() - 256) : match.end() + 160]
            assert any(marker in context for marker in BOUNDARY_MARKERS), context


def _combined_review_text() -> str:
    return "\n".join(
        (ROOT / path).read_text(encoding="utf-8")
        for path in (*REVIEW_NAVIGATION_FILES, "tests/test_review_navigation_consistency.py")
    )
