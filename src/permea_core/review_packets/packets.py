"""Generate deterministic reviewer packets for public artifact systems."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path

PASS = "PASS"
PACKET_OUTPUTS = {
    "p-core-053-artifact-consistency-system": {
        "markdown": "docs/review/packets/p-core-053-artifact-consistency-system.md",
        "json": "docs/review/packets/p-core-053-artifact-consistency-system.json",
    }
}


@dataclass(frozen=True)
class ReviewPacket:
    """A deterministic packet that makes one public artifact system reviewable."""

    packet_id: str
    title: str
    artifact_path: str
    artifact_type: str
    purpose: str
    related_evidence_report_links: tuple[str, ...]
    validation_commands: tuple[str, ...]
    raw_readability_notes: tuple[str, ...]
    claim_boundary_notes: tuple[str, ...]
    reviewer_checklist: tuple[str, ...]
    limitations: tuple[str, ...]


def default_packets() -> tuple[ReviewPacket, ...]:
    """Return the current public review packet set."""
    return (
        ReviewPacket(
            packet_id="p-core-053-artifact-consistency-system",
            title="P-CORE-053 Artifact Consistency System Review Packet",
            artifact_path="docs/artifacts/README.md",
            artifact_type="artifact consistency reviewability layer",
            purpose=(
                "Help a reviewer inspect the P-CORE-053 artifact consistency system through "
                "concrete files, generated outputs, validation commands, boundaries, and limitations."
            ),
            related_evidence_report_links=(
                "scripts/permea_artifacts.py",
                "src/permea_core/consistency/artifacts.py",
                "docs/artifacts/README.md",
                "docs/reports/p-core-053-artifact-consistency-system-v0.md",
                "tests/test_artifact_consistency_system.py",
                "tests/test_review_navigation_consistency.py",
                "OPEN_THIS_FIRST.md",
                "REVIEW_HUB.md",
            ),
            validation_commands=(
                "python3 scripts/permea_artifacts.py",
                "python3 scripts/permea_artifacts.py --json",
                "python3 scripts/validate_permea_artifacts.py",
                "python3 -m pytest tests/test_artifact_consistency_system.py tests/test_review_navigation_consistency.py",
            ),
            raw_readability_notes=(
                "This markdown packet is intentionally written as physical newline-separated text.",
                "This JSON packet is intentionally written with indent=2, sort_keys=True, and a trailing newline.",
                "Use commit-SHA raw URLs for external review when branch raw views may be stale or transformed.",
            ),
            claim_boundary_notes=(
                "This packet reviews documentation and reproducibility surfaces only.",
                "It does not create scientific evidence, benchmark results, or biological validation.",
                "It does not claim wet-lab validation, clinical efficacy, model performance, or solved delivery.",
                "A passing packet means the listed artifact system is easier to inspect; it does not prove biological outcomes.",
            ),
            reviewer_checklist=(
                "Open each related file and confirm the artifact system can be understood without prior session context.",
                "Run the listed validation commands from the repository root.",
                "Confirm generated summaries, JSON, and tests point to the same reviewed surfaces.",
                "Confirm limitations and claim boundaries are explicit.",
                "Record any missing file, stale link, unclear boundary, or validation failure before approval.",
            ),
            limitations=(
                "The packet is manually curated for the current artifact system target.",
                "The packet checks reviewability and deterministic local validation, not scientific correctness.",
                "Future packets should be added when new public artifact systems become reviewer-facing.",
            ),
        ),
    )


def generate_review_packets(root: Path) -> dict[str, object]:
    """Write deterministic markdown and JSON packets under docs/review/packets."""
    packets = default_packets()
    written: list[dict[str, str]] = []
    for packet in packets:
        outputs = PACKET_OUTPUTS[packet.packet_id]
        markdown_path = root / outputs["markdown"]
        json_path = root / outputs["json"]
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(
            render_packet_markdown(packet, markdown_path, root),
            encoding="utf-8",
        )
        json_path.write_text(render_packet_json(packet), encoding="utf-8")
        written.append(
            {
                "packet_id": packet.packet_id,
                "markdown": outputs["markdown"],
                "json": outputs["json"],
            }
        )

    return {
        "status": PASS,
        "packet_count": len(packets),
        "packets": written,
        "non_claims": [
            "reviewability only",
            "no biological result claim",
            "no wet-lab validation claim",
            "no clinical efficacy claim",
            "no solved-delivery claim",
        ],
    }


def render_packet_markdown(packet: ReviewPacket, output_path: Path, root: Path) -> str:
    """Render one packet as deterministic markdown with local links."""
    lines = [
        f"# {packet.title}",
        "",
        "This packet makes one public Permea artifact system reviewable from GitHub.",
        "It is intended for human review and structured assisted review.",
        "",
        "It should be read together with the linked source files, tests, report, and validation command output.",
        "",
        "## Packet Metadata",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| Packet ID | `{packet.packet_id}` |",
        f"| Artifact path | {_link(packet.artifact_path, output_path, root)} |",
        f"| Artifact type | {packet.artifact_type} |",
        "",
        "## Purpose",
        "",
        packet.purpose,
        "",
        "## Related Evidence And Report Links",
        "",
        "| Review surface | Link |",
        "| --- | --- |",
    ]
    lines.extend(
        f"| `{path}` | {_link(path, output_path, root)} |"
        for path in packet.related_evidence_report_links
    )

    lines.extend(["", "## Validation Commands", ""])
    for command in packet.validation_commands:
        lines.extend(["```bash", command, "```", ""])

    lines.extend(["", "## Raw Readability Notes", ""])
    lines.extend(f"- {note}" for note in packet.raw_readability_notes)

    lines.extend(["", "## Claim Boundary Notes", ""])
    lines.extend(f"- {note}" for note in packet.claim_boundary_notes)

    lines.extend(["", "## Reviewer Checklist", ""])
    lines.extend(f"- [ ] {item}" for item in packet.reviewer_checklist)

    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {limitation}" for limitation in packet.limitations)

    lines.extend(
        [
            "",
            "## Next Review Step",
            "",
            "Regenerate this packet:",
            "",
            "```bash",
            "python3 scripts/permea_review_packet.py",
            "```",
            "",
            "Then inspect this packet together with the P-CORE-053 report and artifact consistency command output.",
        ]
    )
    return _newline_terminated_text(lines)


def render_packet_json(packet: ReviewPacket) -> str:
    """Render one packet as deterministic JSON."""
    return json.dumps(asdict(packet), indent=2, sort_keys=True) + "\n"


def render_summary(result: dict[str, object]) -> str:
    """Render a human-readable packet generation summary."""
    lines = [
        "Permea Core evidence review packets",
        "",
        "Evidence Review Packet System Ready",
        "",
        f"Status: {result['status']}",
        f"Review packets generated: {result['packet_count']}",
        "",
        "Generated packets:",
    ]
    for packet in result["packets"]:  # type: ignore[assignment]
        lines.append(f"- {packet['packet_id']}: {packet['markdown']} and {packet['json']}")

    lines.extend(
        [
            "",
            "Review purpose:",
            "- make public artifact systems inspectable through concrete files, commands, summaries, boundaries, and limitations",
            "- support human review and structured assisted review without treating file creation as approval",
            "",
            "Claim-boundary reminder:",
            "- review packets are reviewability surfaces only",
            "- no scientific, biological, wet-lab, clinical, performance, or solved-delivery claim is made by this layer",
            "",
            "Next recommended commands:",
            "- python3 scripts/permea_artifacts.py",
            "- python3 scripts/validate_permea_artifacts.py",
            "- python3 -m pytest",
        ]
    )
    return _newline_terminated_text(lines)


def _link(target: str, output_path: Path, root: Path) -> str:
    relative_target = Path(target)
    from_output = Path(
        os.path.relpath(
            (root / relative_target).resolve(),
            output_path.parent.resolve(),
        )
    )
    return f"[{target}]({from_output.as_posix()})"


def _newline_terminated_text(lines: list[str]) -> str:
    """Return physical line-separated text suitable for raw GitHub review."""
    return "\n".join(lines) + "\n"
