"""Deterministic public evaluation bundle metadata and packet generation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
FAIL = "FAIL"
GENERATED_AT = "example-generated"
DEFAULT_EVALUATION_OUTPUT_DIR = Path("docs/examples/generated")
EVALUATION_PACKET_MD = "EVALUATION_PACKET.md"
EVALUATION_PACKET_JSON = "EVALUATION_PACKET.json"

REFERENCE_INPUT_FAMILIES: tuple[tuple[str, str, str], ...] = (
    ("dataset cards", "dataset_cards/", "Dataset metadata templates and example inputs."),
    ("benchmark cards", "benchmark_cards/", "Benchmark-card pattern inputs for task definitions."),
    ("evidence cards", "evidence_cards/", "Evidence-card pattern inputs for structured evidence records."),
    ("acquisition manifests", "acquisition_manifests/", "Acquisition-plan metadata examples without execution."),
    ("run manifests", "run_manifests/", "Reproducibility record inputs."),
    ("output packages", "output_packages/", "Output-package pattern inputs for reviewer-facing results."),
)

GENERATED_SURFACES: tuple[tuple[str, str], ...] = (
    ("evaluation packet", "docs/examples/generated/EVALUATION_PACKET.md"),
    ("evaluation packet JSON", "docs/examples/generated/EVALUATION_PACKET.json"),
    ("generated evidence surface", "docs/examples/generated/README.md"),
    ("demo packet", "docs/examples/generated/DEMO_PACKET.md"),
    ("artifact index", "docs/examples/generated/ARTIFACT_INDEX.md"),
    ("evidence matrix", "docs/examples/generated/EVIDENCE_MATRIX.md"),
    ("reproducibility report", "docs/examples/generated/REPRODUCIBILITY_REPORT.md"),
    ("benchmark dry-run report", "docs/examples/generated/dry_runs/example_benchmark_dry_run.md"),
)

ARTIFACT_LINEAGE: tuple[tuple[str, str], ...] = (
    ("README", "README.md"),
    ("Quickstart", "QUICKSTART.md"),
    ("Reproducibility guide", "REPRODUCIBILITY.md"),
    ("Evaluation guide", "EVALUATION.md"),
    ("Generated evidence surface", "docs/examples/generated/README.md"),
    ("Evaluation packet", "docs/examples/generated/EVALUATION_PACKET.md"),
    ("Demo packet", "docs/examples/generated/DEMO_PACKET.md"),
    ("Artifact index", "docs/examples/generated/ARTIFACT_INDEX.md"),
    ("Evidence matrix", "docs/examples/generated/EVIDENCE_MATRIX.md"),
    ("Reproducibility report", "docs/examples/generated/REPRODUCIBILITY_REPORT.md"),
    ("Dry-run report", "docs/examples/generated/dry_runs/example_benchmark_dry_run.md"),
    ("Benchmark cards", "docs/examples/generated/benchmark_cards"),
    ("Dataset cards", "docs/examples/generated/dataset_cards"),
    ("Acquisition manifests", "docs/examples/generated/acquisition_manifests"),
    ("Evidence cards", "docs/examples/generated/evidence_cards"),
    ("Output packages", "docs/examples/generated/output_packages"),
    ("Run manifests", "docs/examples/generated/run_manifests"),
)

VALIDATION_HANDOFF: tuple[tuple[str, str], ...] = (
    ("evaluation packet generation", "python3 scripts/permea_evaluate.py"),
    ("public reproducibility validation", "python3 scripts/permea_validate.py"),
    ("unified artifact validation", "python3 scripts/validate_permea_artifacts.py"),
)

REPRODUCIBILITY_HANDOFF: tuple[tuple[str, str], ...] = (
    ("public reproduction", "python3 scripts/permea_reproduce.py"),
    ("unified artifact generation", "python3 scripts/generate_permea_artifacts.py"),
)

NON_CLAIMS: tuple[str, ...] = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no clinical efficacy claim",
    "no model performance claim",
    "no SOTA claim",
    "no solved-delivery claim",
)

LIMITATIONS: tuple[str, ...] = (
    "This evaluation bundle is a reusable template and reference workflow.",
    "It references current public example inputs and generated artifact families only.",
    "It does not load datasets, execute acquisition, call external services, run ML, or score candidates.",
    "It does not establish access rights, redistribution status, biological performance, or clinical utility.",
)

NEXT_EVIDENCE_STEPS: tuple[str, ...] = (
    "Use the packet to inspect how dataset-card, benchmark-card, and evidence-card inputs connect to generated surfaces.",
    "Adapt the pattern by adding bounded input metadata, generator coverage, validation coverage, and tests together.",
    "Run reproduction and validation commands before proposing a public evaluation package change.",
)

REQUIRED_PACKET_SECTIONS: tuple[str, ...] = (
    "## Overview",
    "## Evaluation bundle summary",
    "## Reference input families",
    "## Generated surfaces",
    "## Artifact lineage",
    "## Validation handoff",
    "## Reproducibility handoff",
    "## Explicit Non-Claims",
    "## Limitations",
    "## Next Evidence Steps",
)


def collect_evaluation_bundle(root_path: str | Path = ".") -> dict[str, Any]:
    """Collect deterministic public evaluation bundle metadata."""
    root = Path(root_path).resolve()
    bundle = {
        "bundle_name": "permea_core_public_evaluation_bundle",
        "generated_at": GENERATED_AT,
        "status": PASS,
        "overview": (
            "This public evaluation bundle is a template/reference workflow for "
            "plugging dataset-card, benchmark-card, and evidence-card style inputs "
            "into the Permea Core artifact system and generating a reviewer-facing "
            "evaluation packet."
        ),
        "reference_inputs": _existing_items(root, REFERENCE_INPUT_FAMILIES),
        "generated_surfaces": _existing_path_items(root, GENERATED_SURFACES),
        "artifact_lineage": [
            {
                "order": index + 1,
                "label": label,
                "path": path,
                "exists": (root / path).exists(),
            }
            for index, (label, path) in enumerate(ARTIFACT_LINEAGE)
        ],
        "validation_handoff": [
            {"label": label, "command": command}
            for label, command in VALIDATION_HANDOFF
        ],
        "reproducibility_handoff": [
            {"label": label, "command": command}
            for label, command in REPRODUCIBILITY_HANDOFF
        ],
        "non_claims": list(NON_CLAIMS),
        "limitations": list(LIMITATIONS),
        "next_evidence_steps": list(NEXT_EVIDENCE_STEPS),
    }
    _assert_public_relative(bundle)
    return bundle


def render_evaluation_packet(bundle: dict[str, Any]) -> str:
    """Render the evaluation packet as public-safe Markdown."""
    lines = [
        "# Permea Core Public Evaluation Packet",
        "",
        "## Overview",
        "",
        bundle["overview"],
        "",
        "## Evaluation bundle summary",
        "",
        f"- Bundle name: `{bundle['bundle_name']}`",
        f"- Generated at: `{bundle['generated_at']}`",
        f"- Status: `{bundle['status']}`",
        "- Evaluation guide: [../../EVALUATION.md](../../EVALUATION.md)",
        "",
        "## Reference input families",
        "",
    ]
    lines.extend(_render_described_items(bundle["reference_inputs"]))
    lines.extend(["", "## Generated surfaces", ""])
    lines.extend(_render_path_items(bundle["generated_surfaces"]))
    lines.extend(["", "## Artifact lineage", ""])
    lines.extend(
        f"{item['order']}. {item['label']}: [{item['path']}]({_packet_link(item['path'])})"
        f" ({'present' if item['exists'] else 'missing'})"
        for item in bundle["artifact_lineage"]
    )
    lines.extend(["", "## Validation handoff", ""])
    lines.extend(
        f"- {item['label']}: `{item['command']}`"
        for item in bundle["validation_handoff"]
    )
    lines.extend(["", "## Reproducibility handoff", ""])
    lines.extend(
        f"- {item['label']}: `{item['command']}`"
        for item in bundle["reproducibility_handoff"]
    )
    lines.extend(["", "## Explicit Non-Claims", ""])
    lines.extend(f"- {claim}" for claim in bundle["non_claims"])
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {limitation}" for limitation in bundle["limitations"])
    lines.extend(["", "## Next Evidence Steps", ""])
    lines.extend(f"- {step}" for step in bundle["next_evidence_steps"])
    lines.append("")
    return "\n".join(lines)


def write_evaluation_packet(
    output_dir: str | Path = DEFAULT_EVALUATION_OUTPUT_DIR,
    root_path: str | Path | None = None,
) -> dict[str, Any]:
    """Write deterministic evaluation packet Markdown and JSON outputs."""
    root = Path(root_path).resolve() if root_path is not None else ROOT
    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination
    destination.mkdir(parents=True, exist_ok=True)

    markdown_path = destination / EVALUATION_PACKET_MD
    json_path = destination / EVALUATION_PACKET_JSON
    bundle = collect_evaluation_bundle(root)
    bundle_with_outputs = {
        **bundle,
        "output_paths": {
            "markdown": _display_path(root, markdown_path),
            "json": _display_path(root, json_path),
        },
    }
    markdown_path.write_text(render_evaluation_packet(bundle_with_outputs), encoding="utf-8")
    json_path.write_text(
        json.dumps(bundle_with_outputs, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return bundle_with_outputs


def validate_evaluation_bundle(root_path: str | Path = ".") -> dict[str, Any]:
    """Validate evaluation packet files, sections, lineage, and non-claims."""
    root = Path(root_path).resolve()
    bundle = collect_evaluation_bundle(root)
    checks: list[dict[str, str]] = []
    for item in [*bundle["generated_surfaces"], *bundle["artifact_lineage"]]:
        checks.append(
            {
                "name": f"path present: {item['path']}",
                "status": PASS if (root / item["path"]).exists() else FAIL,
            }
        )

    packet_path = root / "docs/examples/generated/EVALUATION_PACKET.md"
    text = packet_path.read_text(encoding="utf-8") if packet_path.exists() else ""
    for section in REQUIRED_PACKET_SECTIONS:
        checks.append(
            {
                "name": f"packet section: {section}",
                "status": PASS if section in text else FAIL,
            }
        )
    for claim in NON_CLAIMS:
        checks.append(
            {
                "name": f"non-claim: {claim}",
                "status": PASS if claim in text else FAIL,
            }
        )
    for _label, path, _description in REFERENCE_INPUT_FAMILIES:
        checks.append(
            {
                "name": f"reference input family: {path}",
                "status": PASS if path in text else FAIL,
            }
        )

    status = PASS if all(check["status"] == PASS for check in checks) else FAIL
    return {"status": status, "checks": checks}


def _existing_items(
    root: Path,
    items: tuple[tuple[str, str, str], ...],
) -> list[dict[str, Any]]:
    return [
        {
            "label": label,
            "path": path,
            "description": description,
            "exists": (root / path).exists() or (root / "docs/examples/generated" / path).exists(),
        }
        for label, path, description in items
    ]


def _existing_path_items(root: Path, items: tuple[tuple[str, str], ...]) -> list[dict[str, Any]]:
    return [
        {"label": label, "path": path, "exists": (root / path).exists()}
        for label, path in items
    ]


def _render_described_items(items: list[dict[str, Any]]) -> list[str]:
    return [
        f"- {item['label']}: [{item['path']}]({_packet_link(item['path'])}) - "
        f"{item['description']} ({'present' if item['exists'] else 'missing'})"
        for item in items
    ]


def _render_path_items(items: list[dict[str, Any]]) -> list[str]:
    return [
        f"- {item['label']}: [{item['path']}]({_packet_link(item['path'])})"
        f" ({'present' if item['exists'] else 'missing'})"
        for item in items
    ]


def _packet_link(path: str) -> str:
    family_paths = {
        "dataset_cards/",
        "benchmark_cards/",
        "evidence_cards/",
        "acquisition_manifests/",
        "run_manifests/",
        "output_packages/",
    }
    if path in family_paths:
        return path
    if path.startswith("docs/examples/generated/"):
        return path.removeprefix("docs/examples/generated/")
    return f"../../{path}"


def _assert_public_relative(value: Any) -> None:
    if isinstance(value, dict):
        for nested in value.values():
            _assert_public_relative(nested)
    elif isinstance(value, list):
        for nested in value:
            _assert_public_relative(nested)
    elif isinstance(value, str):
        if str(ROOT) in value or value.startswith("/"):
            raise ValueError(f"non-public or absolute path in evaluation bundle: {value}")


def _display_path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.name
