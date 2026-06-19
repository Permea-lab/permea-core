"""Consistency checks for generated review packet coverage."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .packets import PACKET_OUTPUTS, default_packets

PASS = "PASS"
FAIL = "FAIL"


def check_review_packet_coverage(root: Path) -> dict[str, Any]:
    """Check packet definitions, generated files, links, and index coverage."""
    packets = default_packets()
    packet_ids = [packet.packet_id for packet in packets]
    output_ids = list(PACKET_OUTPUTS)
    checks: list[dict[str, str]] = []

    _append_check(
        checks,
        "packet definitions match output map",
        packet_ids == output_ids,
    )

    packet_index = _read_text(root / "docs/review/packets/README.md")
    system_doc = _read_text(root / "docs/review/review-packet-system.md")
    raw_target_paths = _raw_target_paths()

    for packet in packets:
        outputs = PACKET_OUTPUTS[packet.packet_id]
        markdown = outputs["markdown"]
        json_path = outputs["json"]
        _append_check(checks, f"{packet.packet_id} markdown output exists", (root / markdown).exists())
        _append_check(checks, f"{packet.packet_id} json output exists", (root / json_path).exists())
        _append_check(checks, f"{packet.packet_id} artifact path exists", (root / packet.artifact_path).exists())
        _append_check(checks, f"{packet.packet_id} listed in packet index", Path(markdown).name in packet_index)
        _append_check(checks, f"{packet.packet_id} listed in system docs", Path(markdown).name in system_doc)
        _append_check(checks, f"{packet.packet_id} raw markdown target covered", markdown in raw_target_paths)
        _append_check(checks, f"{packet.packet_id} raw json target covered", json_path in raw_target_paths)
        for linked_path in packet.related_evidence_report_links:
            _append_check(
                checks,
                f"{packet.packet_id} linked path exists: {linked_path}",
                (root / linked_path).exists(),
            )

    status = PASS if all(check["status"] == PASS for check in checks) else FAIL
    return {
        "status": status,
        "packet_count": len(packets),
        "packet_ids": packet_ids,
        "checks": checks,
        "non_claims": [
            "review packet coverage check only",
            "no scientific evidence claim",
            "no benchmark result claim",
            "no biological validation claim",
            "no solved-delivery claim",
        ],
    }


def render_coverage_summary(result: dict[str, Any]) -> str:
    """Render a deterministic human-readable coverage summary."""
    lines = [
        "Permea Core review packet coverage check",
        "",
        f"Status: {result['status']}",
        f"Review packets checked: {result['packet_count']}",
        "",
        "Packet IDs:",
    ]
    lines.extend(f"- {packet_id}" for packet_id in result["packet_ids"])
    lines.extend(["", "Checks:"])
    for check in result["checks"]:
        lines.append(f"- {check['status']} {check['name']}")
    lines.extend(
        [
            "",
            "Claim-boundary reminder:",
        ]
    )
    lines.extend(f"- {claim}" for claim in result["non_claims"])
    return "\n".join(lines) + "\n"


def _append_check(checks: list[dict[str, str]], name: str, passed: bool) -> None:
    checks.append({"name": name, "status": PASS if passed else FAIL})


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _raw_target_paths() -> set[str]:
    return {
        outputs[key]
        for outputs in PACKET_OUTPUTS.values()
        for key in ("markdown", "json")
    }
