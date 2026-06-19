"""Completeness checks for public review bundle text."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PASS = "PASS"
FAIL = "FAIL"

DEFAULT_SAMPLE_BUNDLE = """\
Group P-CORE-062

PR URL: https://github.com/Permea-lab/permea-core/pull/999
Branch: p-core-062-review-bundle-completeness-check
Head SHA: 0123456789abcdef0123456789abcdef01234567

Changed files:
- scripts/check_review_bundle_completeness.py
- src/permea_core/review_packets/bundle_completeness.py

Validation results:
- git diff --check: PASS
- python3 -m pytest: PASS

Local human-review paths:
- /Users/albertkim/02_PROJECTS/18_PERMEA/repos/permea-core/scripts/check_review_bundle_completeness.py

Remote GitHub review URLs:
- https://github.com/Permea-lab/permea-core/blob/p-core-062-review-bundle-completeness-check/scripts/check_review_bundle_completeness.py

Scope audit result: PASS, bounded reviewability checker only.
Boundary audit result: PASS, no private references.
Claim-discipline audit result: PASS, no unsupported claims.
Review packet decision: not needed for this checker.
Final human/model-assisted review gate recommendation: recommended before merge.
Stop reason: PR opened and left unmerged for review.
"""


@dataclass(frozen=True)
class RequiredField:
    name: str
    patterns: tuple[str, ...]


REQUIRED_FIELDS: tuple[RequiredField, ...] = (
    RequiredField("PR URL", (r"https://github\.com/[^/\s]+/[^/\s]+/pull/\d+",)),
    RequiredField("branch name", (r"\bbranch\s*:\s*\S+",)),
    RequiredField("head SHA", (r"\bhead sha\s*:\s*[0-9a-f]{7,40}\b",)),
    RequiredField("changed files", (r"changed files\s*:",)),
    RequiredField("validation commands and results", (r"validation results\s*:", r"\bpass\b")),
    RequiredField("local human-review paths", (r"local human-review paths\s*:", r"/Users/")),
    RequiredField("remote GitHub review URLs", (r"remote github review urls\s*:", r"https://github\.com/.*/blob/")),
    RequiredField("scope audit result", (r"scope audit result\s*:",)),
    RequiredField("boundary audit result", (r"boundary audit result\s*:",)),
    RequiredField("claim-discipline audit result", (r"claim-discipline audit result\s*:",)),
    RequiredField("review packet decision", (r"review packet decision\s*:",)),
    RequiredField("stop reason", (r"stop reason\s*:",)),
    RequiredField(
        "final human/model-assisted review gate status or recommendation",
        (r"final human/model-assisted review gate (status|recommendation)\s*:",),
    ),
)


def check_review_bundle_completeness(text: str) -> dict[str, Any]:
    """Check whether review bundle text includes required public handoff fields."""
    checks = [_check_required_field(text, field) for field in REQUIRED_FIELDS]
    status = PASS if all(check["status"] == PASS for check in checks) else FAIL
    missing = [check["name"] for check in checks if check["status"] == FAIL]
    return {
        "status": status,
        "required_field_count": len(REQUIRED_FIELDS),
        "missing_fields": missing,
        "checks": checks,
        "limitations": [
            "text presence check only",
            "does not verify factual correctness",
            "does not approve merge readiness",
            "does not create scientific evidence or benchmark results",
        ],
    }


def check_review_bundle_file(path: Path) -> dict[str, Any]:
    """Read and check a review bundle file."""
    return check_review_bundle_completeness(path.read_text(encoding="utf-8"))


def render_bundle_completeness_summary(result: dict[str, Any]) -> str:
    """Render deterministic human-readable output."""
    lines = [
        "Permea Core review bundle completeness check",
        "",
        f"Status: {result['status']}",
        f"Required fields checked: {result['required_field_count']}",
        "",
        "Checks:",
    ]
    lines.extend(f"- {check['status']} {check['name']}" for check in result["checks"])
    lines.extend(["", "Missing fields:"])
    if result["missing_fields"]:
        lines.extend(f"- {field}" for field in result["missing_fields"])
    else:
        lines.append("- none")
    lines.extend(["", "Limitations:"])
    lines.extend(f"- {item}" for item in result["limitations"])
    return "\n".join(lines) + "\n"


def _check_required_field(text: str, field: RequiredField) -> dict[str, str]:
    lowered = text.lower()
    passed = all(re.search(pattern, lowered, flags=re.MULTILINE | re.IGNORECASE) for pattern in field.patterns)
    return {"name": field.name, "status": PASS if passed else FAIL}
