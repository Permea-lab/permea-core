"""Deterministic public reproducibility bundle metadata and reports."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
FAIL = "FAIL"
GENERATED_AT = "example-generated"
REPORT_MD = Path("docs/examples/generated/REPRODUCIBILITY_REPORT.md")
REPORT_JSON = Path("docs/examples/generated/REPRODUCIBILITY_REPORT.json")

COMMANDS: tuple[tuple[str, str, str], ...] = (
    ("reproduce public artifacts", "python3 scripts/permea_reproduce.py", "Regenerates public artifact surfaces and the reproducibility report."),
    ("validate public artifacts", "python3 scripts/permea_validate.py", "Runs unified validation and reproducibility bundle checks."),
    ("generate evaluation packet", "python3 scripts/permea_evaluate.py", "Writes the public template/reference evaluation packet."),
    ("generate all artifacts", "python3 scripts/generate_permea_artifacts.py", "Runs deterministic local artifact generators."),
    ("validate all artifacts", "python3 scripts/validate_permea_artifacts.py", "Runs local validation and generated-artifact checks."),
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

GENERATED_ARTIFACTS: tuple[tuple[str, str], ...] = (
    ("Generated evidence surface", "docs/examples/generated/README.md"),
    ("Evaluation packet", "docs/examples/generated/EVALUATION_PACKET.md"),
    ("Evaluation packet JSON", "docs/examples/generated/EVALUATION_PACKET.json"),
    ("Demo packet", "docs/examples/generated/DEMO_PACKET.md"),
    ("Artifact index", "docs/examples/generated/ARTIFACT_INDEX.md"),
    ("Evidence matrix", "docs/examples/generated/EVIDENCE_MATRIX.md"),
    ("Reproducibility report Markdown", "docs/examples/generated/REPRODUCIBILITY_REPORT.md"),
    ("Reproducibility report JSON", "docs/examples/generated/REPRODUCIBILITY_REPORT.json"),
    ("Dry-run report", "docs/examples/generated/dry_runs/example_benchmark_dry_run.md"),
)

VALIDATION_CHECKS: tuple[tuple[str, str], ...] = (
    ("unified artifact validation", "python3 scripts/validate_permea_artifacts.py"),
    ("reproducibility bundle validation", "python3 scripts/permea_validate.py"),
    ("focused reproducibility tests", "python3 -m pytest tests/test_reproducibility_bundle.py"),
)

NON_CLAIMS: tuple[str, ...] = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no clinical-effectiveness claim",
    "no model performance claim",
    "no state-of-the-art claim",
    "no solved-delivery claim",
)

LIMITATIONS: tuple[str, ...] = (
    "This bundle regenerates deterministic public metadata artifacts from repository files only.",
    "It does not download datasets, execute acquisition, call external services, run ML, or score candidates.",
    "It validates artifact presence, structure, links, and stated boundaries; it does not validate biological performance.",
    "Researchers and developers should treat generated examples as infrastructure surfaces, not experimental evidence.",
)

REQUIRED_REPORT_SECTIONS: tuple[str, ...] = (
    "## Run summary",
    "## Generated surfaces",
    "## Validation summary",
    "## Artifact lineage",
    "## Reproducibility status",
    "## Explicit Non-Claims",
    "## Limitations",
    "## Next Evidence Steps",
)


def collect_reproducibility_report(root_path: str | Path = ".") -> dict[str, Any]:
    """Collect deterministic public reproducibility bundle metadata."""
    root = Path(root_path).resolve()
    report = {
        "run_name": "permea_core_public_reproducibility_bundle",
        "generated_at": GENERATED_AT,
        "status": PASS,
        "commands": [
            {"label": label, "command": command, "description": description}
            for label, command, description in COMMANDS
        ],
        "generated_artifacts": _path_items(root, GENERATED_ARTIFACTS),
        "validation_checks": [
            {"label": label, "command": command} for label, command in VALIDATION_CHECKS
        ],
        "artifact_lineage": [
            {
                "order": index + 1,
                "label": label,
                "path": path,
                "exists": (root / path).exists(),
            }
            for index, (label, path) in enumerate(ARTIFACT_LINEAGE)
        ],
        "non_claims": list(NON_CLAIMS),
        "limitations": list(LIMITATIONS),
        "next_evidence_steps": [
            "Run the reproduction command after cloning or changing generator code.",
            "Run the validation command before proposing changes to generated artifact surfaces.",
            "Extend the artifact system by adding generator, validation, tests, and bounded claim language together.",
        ],
    }
    _assert_public_relative(report)
    return report


def render_reproducibility_report(report: dict[str, Any]) -> str:
    """Render the reproducibility report as public-safe Markdown."""
    lines = [
        "# Permea Core Public Reproducibility Report",
        "",
        "## Run summary",
        "",
        f"- Run name: `{report['run_name']}`",
        f"- Generated at: `{report['generated_at']}`",
        f"- Status: `{report['status']}`",
        "",
        "## Generated surfaces",
        "",
    ]
    lines.extend(_render_path_items(report["generated_artifacts"]))
    lines.extend(["", "## Validation summary", ""])
    lines.extend(
        f"- {item['label']}: `{item['command']}`"
        for item in report["validation_checks"]
    )
    lines.extend(["", "## Artifact lineage", ""])
    lines.extend(
        f"{item['order']}. {item['label']}: [{item['path']}]({item['path']})"
        f" ({'present' if item['exists'] else 'missing'})"
        for item in report["artifact_lineage"]
    )
    lines.extend(
        [
            "",
            "## Reproducibility status",
            "",
            "The bundle is reproducible when the listed artifacts are present and the reproduction and validation commands exit successfully.",
            "",
            "## Explicit Non-Claims",
            "",
        ]
    )
    lines.extend(f"- {claim}" for claim in report["non_claims"])
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {limitation}" for limitation in report["limitations"])
    lines.extend(["", "## Next Evidence Steps", ""])
    lines.extend(f"- {step}" for step in report["next_evidence_steps"])
    lines.append("")
    return "\n".join(lines)


def write_reproducibility_report(
    output_dir: str | Path = "docs/examples/generated",
    root_path: str | Path | None = None,
) -> dict[str, Any]:
    """Write deterministic reproducibility report Markdown and JSON."""
    root = Path(root_path).resolve() if root_path is not None else ROOT
    destination = Path(output_dir)
    if not destination.is_absolute():
        destination = root / destination
    destination.mkdir(parents=True, exist_ok=True)

    markdown_path = destination / REPORT_MD.name
    json_path = destination / REPORT_JSON.name
    report = collect_reproducibility_report(root)
    report_with_outputs = {
        **report,
        "output_paths": {
            "markdown": _display_path(root, markdown_path),
            "json": _display_path(root, json_path),
        },
    }
    markdown_path.write_text(render_reproducibility_report(report_with_outputs), encoding="utf-8")
    json_path.write_text(
        json.dumps(report_with_outputs, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return report_with_outputs


def validate_reproducibility_bundle(root_path: str | Path = ".") -> dict[str, Any]:
    """Validate reproducibility bundle artifacts, sections, links, and boundaries."""
    root = Path(root_path).resolve()
    report = collect_reproducibility_report(root)
    checks: list[dict[str, Any]] = []
    for item in [*report["generated_artifacts"], *report["artifact_lineage"]]:
        checks.append(
            {
                "name": f"path present: {item['path']}",
                "status": PASS if (root / item["path"]).exists() else FAIL,
            }
        )

    report_path = root / REPORT_MD
    text = report_path.read_text(encoding="utf-8") if report_path.exists() else ""
    for section in REQUIRED_REPORT_SECTIONS:
        checks.append(
            {
                "name": f"report section: {section}",
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

    status = PASS if all(check["status"] == PASS for check in checks) else FAIL
    return {"status": status, "checks": checks}


def _path_items(root: Path, items: tuple[tuple[str, str], ...]) -> list[dict[str, Any]]:
    return [
        {"label": label, "path": path, "exists": (root / path).exists()}
        for label, path in items
    ]


def _render_path_items(items: list[dict[str, Any]]) -> list[str]:
    return [
        f"- {item['label']}: [{item['path']}]({item['path']})"
        f" ({'present' if item['exists'] else 'missing'})"
        for item in items
    ]


def _assert_public_relative(value: Any) -> None:
    if isinstance(value, dict):
        for nested in value.values():
            _assert_public_relative(nested)
    elif isinstance(value, list):
        for nested in value:
            _assert_public_relative(nested)
    elif isinstance(value, str):
        if str(ROOT) in value or value.startswith("/"):
            raise ValueError(f"non-public or absolute path in reproducibility bundle: {value}")


def _display_path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.name
