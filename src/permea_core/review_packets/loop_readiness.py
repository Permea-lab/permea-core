"""Readiness checks for the public review loop."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .bundle_completeness import (
    PASS,
    check_review_bundle_file,
)

FAIL = "FAIL"

FIXTURE_PATH = Path("docs/review/examples/final-review-bundle-complete-example.md")
CHECKER_PATH = Path("scripts/check_review_bundle_completeness.py")
REVIEW_README_PATH = Path("docs/review/README.md")
REVIEW_STANDARD_PATH = Path("docs/review/review-loop-operating-standard.md")
REVIEW_EXAMPLES_INDEX_PATH = Path("docs/review/examples/README.md")
REVIEW_HUB_PATH = Path("REVIEW_HUB.md")
REPORTS_INDEX_PATH = Path("docs/reports/README.md")

REQUIRED_FIELD_LABELS = (
    "PR URL",
    "Branch",
    "Head SHA",
    "Changed files",
    "Validation results",
    "Local human-review paths",
    "Remote GitHub review URLs",
    "Scope audit result",
    "Boundary audit result",
    "Claim-discipline audit result",
    "Review packet decision",
    "Stop reason",
)


def check_review_loop_readiness(root: Path) -> dict[str, Any]:
    """Check that the current public review loop is wired for local review."""
    repo_root = root.resolve()
    checks = [
        _check_fixture_exists(repo_root),
        _check_fixture_passes_completeness(repo_root),
        _check_public_navigation_reaches_fixture(repo_root),
        _check_docs_reference_fixture_and_checker(repo_root),
        _check_fixture_field_shape(repo_root),
    ]
    status = PASS if all(check["status"] == PASS for check in checks) else FAIL
    return {
        "status": status,
        "checks": checks,
        "limitations": [
            "local review-loop readiness only",
            "does not verify factual correctness",
            "does not approve merge readiness",
            "does not create scientific evidence or benchmark results",
        ],
    }


def render_review_loop_readiness_summary(result: dict[str, Any]) -> str:
    """Render deterministic human-readable output."""
    lines = [
        "Permea Core review loop readiness check",
        "",
        f"Status: {result['status']}",
        "",
        "Checks:",
    ]
    for check in result["checks"]:
        lines.append(f"- {check['status']} {check['name']}")
        if check["status"] != PASS:
            lines.extend(f"  - {detail}" for detail in check["details"])
    lines.extend(["", "Limitations:"])
    lines.extend(f"- {item}" for item in result["limitations"])
    return "\n".join(lines) + "\n"


def _check_fixture_exists(root: Path) -> dict[str, Any]:
    path = root / FIXTURE_PATH
    return _result(
        "canonical fixture exists",
        path.exists() and path.is_file(),
        [str(FIXTURE_PATH)],
    )


def _check_fixture_passes_completeness(root: Path) -> dict[str, Any]:
    path = root / FIXTURE_PATH
    if not path.exists():
        return _result("canonical fixture passes completeness checker", False, [str(FIXTURE_PATH)])
    result = check_review_bundle_file(path)
    details = [f"missing fields: {', '.join(result['missing_fields'])}"] if result["missing_fields"] else []
    return _result("canonical fixture passes completeness checker", result["status"] == PASS, details)


def _check_public_navigation_reaches_fixture(root: Path) -> dict[str, Any]:
    review_readme = _read(root, REVIEW_README_PATH)
    examples_index = _read(root, REVIEW_EXAMPLES_INDEX_PATH)
    review_hub = _read(root, REVIEW_HUB_PATH)
    details = [
        "docs/review/README.md links docs/review/examples/README.md",
        "docs/review/examples/README.md links final-review-bundle-complete-example.md",
        "REVIEW_HUB.md links docs/review/examples/README.md",
    ]
    passed = (
        "examples/README.md" in review_readme
        and "final-review-bundle-complete-example.md" in examples_index
        and "docs/review/examples/README.md" in review_hub
    )
    return _result("public review navigation reaches fixture", passed, details)


def _check_docs_reference_fixture_and_checker(root: Path) -> dict[str, Any]:
    docs = {
        str(REVIEW_README_PATH): _read(root, REVIEW_README_PATH),
        str(REVIEW_STANDARD_PATH): _read(root, REVIEW_STANDARD_PATH),
        str(REPORTS_INDEX_PATH): _read(root, REPORTS_INDEX_PATH),
    }
    missing: list[str] = []
    for label, text in docs.items():
        if "check_review_bundle_completeness.py" not in text:
            missing.append(f"{label} lacks completeness checker reference")
    if "final-review-bundle-complete-example.md" not in docs[str(REVIEW_README_PATH)]:
        missing.append("docs/review/README.md lacks canonical fixture reference")
    if "examples/final-review-bundle-complete-example.md" not in docs[str(REVIEW_STANDARD_PATH)]:
        missing.append("docs/review/review-loop-operating-standard.md lacks canonical fixture reference")
    if "check_review_loop_readiness.py" not in docs[str(REPORTS_INDEX_PATH)]:
        missing.append("docs/reports/README.md lacks readiness checker reference")
    return _result("review-loop docs reference fixture and checkers", not missing, missing)


def _check_fixture_field_shape(root: Path) -> dict[str, Any]:
    text = _read(root, FIXTURE_PATH)
    missing = [label for label in REQUIRED_FIELD_LABELS if label not in text]
    return _result("canonical fixture includes required review-bundle fields", not missing, missing)


def _read(root: Path, path: Path) -> str:
    resolved = root / path
    if not resolved.exists():
        return ""
    return resolved.read_text(encoding="utf-8")


def _result(name: str, passed: bool, details: list[str]) -> dict[str, Any]:
    return {
        "name": name,
        "status": PASS if passed else FAIL,
        "details": details,
    }
