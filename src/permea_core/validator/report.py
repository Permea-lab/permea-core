"""Deterministic report rendering for public artifact checks."""

from __future__ import annotations

from typing import Any


def render_check_report(report: dict[str, Any]) -> str:
    """Render a stable text summary for the validator CLI."""
    lines = [
        f"{report['status']} Permea artifact check",
        "",
        "Checked artifact families:",
    ]
    lines.extend(f"- {family}" for family in report["checked_families"])
    lines.extend(["", "Checked files:"])
    lines.extend(f"- {path}" for path in report["checked_files"])
    lines.extend(["", "Failed checks:"])
    if report["failed_checks"]:
        lines.extend(f"- {item}" for item in report["failed_checks"])
    else:
        lines.append("- none")
    lines.extend(["", "Warnings:"])
    if report["warnings"]:
        lines.extend(f"- {item}" for item in report["warnings"])
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            f"Non-claim boundary status: {report['non_claim_boundary_status']}",
            "",
        ]
    )
    return "\n".join(lines)
