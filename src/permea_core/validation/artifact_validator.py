"""Lightweight public artifact validator for Permea Core examples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

try:  # pragma: no cover - import guard mirrors existing YAML-using modules
    import yaml
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("PyYAML is required for current Permea YAML artifacts") from exc


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
FAIL = "FAIL"
WARNING = "WARNING"

BUILT_IN_ARTIFACTS: tuple[str, ...] = (
    "docs/examples/generated/dataset_cards/b3pred_dataset3.md",
    "docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md",
    "docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json",
    "docs/examples/generated/run_manifests/example_artifact_generation.md",
    "docs/examples/generated/output_packages/bbb_b3pred_dataset3",
)

NON_CLAIM_ALIASES: dict[str, tuple[str, ...]] = {
    "no dataset downloaded": ("no dataset downloaded", "no_dataset_download"),
    "no acquisition executed": ("no acquisition executed",),
    "no redistribution rights confirmed": (
        "no redistribution rights confirmed",
        "no redistribution-rights confirmation",
        "no_redistribution_rights_confirmation",
    ),
    "no wet-lab validation by Permea": (
        "no wet-lab validation by permea",
        "no_wet_lab_validation_by_permea",
    ),
    "no clinical efficacy claim": (
        "no clinical efficacy claim",
        "no clinical-effectiveness claim",
    ),
    "no model performance claim": ("no model performance claim",),
    "no SOTA claim": ("no sota claim", "no state-of-the-art claim"),
    "no solved-delivery claim": ("no solved-delivery claim",),
}

REQUIRED_NON_CLAIMS_BY_TYPE: dict[str, tuple[str, ...]] = {
    "dataset_card": (
        "no dataset downloaded",
        "no redistribution rights confirmed",
        "no wet-lab validation by Permea",
    ),
    "benchmark_card": (),
    "evidence_card": (
        "no dataset downloaded",
        "no redistribution rights confirmed",
        "no wet-lab validation by Permea",
    ),
    "run_manifest": (
        "no dataset downloaded",
        "no acquisition executed",
        "no redistribution rights confirmed",
        "no wet-lab validation by Permea",
        "no model performance claim",
    ),
    "output_package": (
        "no dataset downloaded",
        "no redistribution rights confirmed",
        "no wet-lab validation by Permea",
    ),
}

REQUIRED_FIELDS_BY_TYPE: dict[str, tuple[str, ...]] = {
    "dataset_card": (
        "Dataset ID",
        "Source IDs",
        "Benchmark IDs",
        "Acquisition Status",
        "Redistribution Status",
        "Claim Boundary",
    ),
    "benchmark_card": (
        "Benchmark ID",
        "Task Name",
        "Dataset Card",
        "Output Artifacts",
        "Limitations",
        "Claim Boundary",
    ),
    "run_manifest": (
        "Run ID",
        "Run Type",
        "Commands",
        "Generated Artifacts",
        "Explicit Non-Claims",
        "Claim Boundary",
    ),
}

SPEC_SCHEMA_BY_TYPE: dict[str, tuple[str, str]] = {
    "dataset_card": ("docs/specs/SPEC_DATASET_CARD.md", "schemas/dataset_card.schema.json"),
    "benchmark_card": ("docs/specs/SPEC_BENCHMARK_CARD.md", "schemas/benchmark_card.schema.json"),
    "evidence_card": ("docs/specs/SPEC_EVIDENCE_CARD.md", "schemas/evidence_card.schema.json"),
    "run_manifest": ("docs/specs/SPEC_RUN_MANIFEST.md", "schemas/run_manifest.schema.json"),
    "output_package": ("docs/specs/SPEC_OUTPUT_PACKAGE.md", "schemas/output_package.schema.json"),
}

UNSUPPORTED_POSITIVE_CLAIMS: tuple[str, ...] = (
    "wet-lab " + "validated",
    "clinical " + "efficacy",
    "universal " + "prediction",
    "alphafold-level " + "maturity",
    "solved " + "delivery",
    "model performance has been " + "measured",
    "state-of-the-" + "art",
    "sota",
)


def validate_builtin_artifacts(root_path: str | Path = ".") -> dict[str, Any]:
    """Validate deterministic built-in public artifacts."""
    root = Path(root_path).resolve()
    results = [validate_artifact(root / artifact, root) for artifact in BUILT_IN_ARTIFACTS]
    return summarize_results(results)


def validate_artifact(artifact_path: str | Path, root_path: str | Path = ".") -> dict[str, Any]:
    """Validate one artifact path and return a deterministic result dictionary."""
    root = Path(root_path).resolve()
    path = Path(artifact_path)
    if not path.is_absolute():
        path = (root / path).resolve()
    artifact_type = infer_artifact_type(path)
    result = _empty_result(root, path, artifact_type)

    if not path.exists():
        _fail(result, "path_exists", f"artifact path does not exist: {_display_path(root, path)}")
        return _finalize(result)

    _pass(result, "path_exists")
    _check_public_relative_path(result)
    _check_artifact_type(result)
    _check_spec_schema_presence(result, root)

    if artifact_type == "dataset_card":
        _validate_markdown_artifact(result, path, REQUIRED_FIELDS_BY_TYPE["dataset_card"])
    elif artifact_type == "benchmark_card":
        _validate_markdown_artifact(result, path, REQUIRED_FIELDS_BY_TYPE["benchmark_card"])
        _check_benchmark_output_names(result, path)
    elif artifact_type == "evidence_card":
        _validate_evidence_card_json(result, path)
    elif artifact_type == "run_manifest":
        _validate_markdown_artifact(result, path, REQUIRED_FIELDS_BY_TYPE["run_manifest"])
        _check_markdown_list_paths(result, path, "Generated Artifacts")
    elif artifact_type == "output_package":
        _validate_output_package(result, path)
    else:
        _fail(result, "artifact_type_recognition", "unsupported artifact type")

    _check_non_claims(result, _artifact_text(path))
    _check_claim_boundary(result, _artifact_text(path))
    return _finalize(result)


def summarize_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize validator results with deterministic counts."""
    pass_count = sum(1 for item in results if item["status"] == PASS)
    warning_count = sum(1 for item in results if item["status"] == WARNING)
    fail_count = sum(1 for item in results if item["status"] == FAIL)
    status = FAIL if fail_count else WARNING if warning_count else PASS
    return {
        "status": status,
        "artifacts_checked": len(results),
        "pass_count": pass_count,
        "warning_count": warning_count,
        "fail_count": fail_count,
        "results": results,
        "issue_summary": [
            f"{item['artifact_path']}: {issue}"
            for item in results
            for issue in item["issues"]
        ],
    }


def render_summary(summary: dict[str, Any]) -> str:
    """Render validator summary text for CLI output."""
    lines = [
        "Permea artifact validator",
        f"Status: {summary['status']}",
        f"Artifacts checked: {summary['artifacts_checked']}",
        f"Pass count: {summary['pass_count']}",
        f"Warning count: {summary['warning_count']}",
        f"Fail count: {summary['fail_count']}",
        "Issue summary:",
    ]
    if summary["issue_summary"]:
        lines.extend(f"- {issue}" for issue in summary["issue_summary"])
    else:
        lines.append("- none")
    lines.extend(
        [
            "Next recommended command:",
            "python3 scripts/permea_validate.py",
            "",
        ]
    )
    return "\n".join(lines)


def infer_artifact_type(path: Path) -> str:
    """Infer a supported artifact type from a path."""
    parts = path.parts
    name = path.name
    if path.is_dir() and "output_packages" in parts:
        return "output_package"
    if "dataset_cards" in parts and path.suffix == ".md":
        return "dataset_card"
    if "benchmark_cards" in parts and path.suffix == ".md":
        return "benchmark_card"
    if "evidence_cards" in parts and path.suffix == ".json":
        return "evidence_card"
    if "run_manifests" in parts and path.suffix == ".md":
        return "run_manifest"
    if name == "manifest.yaml":
        return "output_package"
    return "unknown"


def _empty_result(root: Path, path: Path, artifact_type: str) -> dict[str, Any]:
    return {
        "artifact_path": _display_path(root, path),
        "artifact_type": artifact_type,
        "status": PASS,
        "checks": [],
        "issues": [],
        "warnings": [],
        "non_claims_seen": [],
        "evidence_links_seen": [],
    }


def _validate_markdown_artifact(
    result: dict[str, Any],
    path: Path,
    required_sections: tuple[str, ...],
) -> None:
    sections = _markdown_sections(path.read_text(encoding="utf-8"))
    for section in required_sections:
        if section in sections:
            _pass(result, f"required_field:{section}")
        else:
            _fail(result, f"required_field:{section}", f"missing required section: {section}")


def _validate_evidence_card_json(result: dict[str, Any], path: Path) -> None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        _fail(result, "json_parse", f"invalid JSON: {exc}")
        return
    _pass(result, "json_parse")
    records = payload if isinstance(payload, list) else [payload]
    if not records or not all(isinstance(record, dict) for record in records):
        _fail(result, "required_fields", "evidence card JSON must contain object records")
        return

    required = (
        "evidence_card_id",
        "artifact_type",
        "claim_boundary",
        "limitations",
        "non_claims",
        "related_objects",
        "source_reference",
    )
    for index, record in enumerate(records):
        for field in required:
            if field in record:
                _pass(result, f"required_field:{field}")
            else:
                _fail(result, f"required_field:{field}", f"record {index} missing field: {field}")
        links = record.get("related_objects", {})
        if isinstance(links, dict):
            result["evidence_links_seen"].extend(
                str(value) for value in links.values() if isinstance(value, str)
            )
    if result["evidence_links_seen"]:
        _pass(result, "evidence_linkage")
    else:
        _fail(result, "evidence_linkage", "no evidence linkage paths found")


def _validate_output_package(result: dict[str, Any], path: Path) -> None:
    package_dir = path if path.is_dir() else path.parent
    required_files = (
        "manifest.yaml",
        "metrics.json",
        "ranking.csv",
        "benchmark_card.md",
        "evidence_cards.json",
    )
    for name in required_files:
        candidate = package_dir / name
        if candidate.exists():
            _pass(result, f"path_exists:{name}")
            result["evidence_links_seen"].append(name)
        else:
            _fail(result, f"path_exists:{name}", f"output package missing file: {name}")

    manifest = package_dir / "manifest.yaml"
    if not manifest.exists():
        return
    payload = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        _fail(result, "manifest_parse", "output package manifest is not an object")
        return
    _pass(result, "manifest_parse")
    for field in (
        "run_id",
        "artifact_type",
        "benchmark_id",
        "dataset",
        "benchmark_task",
        "metrics_output_path",
        "ranking_output_path",
        "benchmark_card_path",
        "evidence_card_paths",
        "claim_boundary",
        "limitations",
    ):
        if field in payload:
            _pass(result, f"required_field:{field}")
        else:
            _fail(result, f"required_field:{field}", f"output manifest missing field: {field}")


def _check_markdown_list_paths(result: dict[str, Any], path: Path, section: str) -> None:
    root = ROOT
    sections = _markdown_sections(path.read_text(encoding="utf-8"))
    values = sections.get(section, [])
    paths = [line[2:] for line in values if line.startswith("- ")]
    if not paths:
        _fail(result, "evidence_linkage", f"section has no paths: {section}")
        return
    for value in paths:
        candidate = root / value
        if candidate.exists():
            result["evidence_links_seen"].append(value)
        else:
            _fail(result, "path_exists", f"linked artifact path missing: {value}")
    if result["evidence_links_seen"]:
        _pass(result, "evidence_linkage")


def _check_benchmark_output_names(result: dict[str, Any], path: Path) -> None:
    sections = _markdown_sections(path.read_text(encoding="utf-8"))
    outputs = "\n".join(sections.get("Output Artifacts", []))
    for name in ("metrics.json", "ranking.csv", "manifest.yaml", "evidence_cards.json"):
        if name in outputs:
            _pass(result, f"evidence_linkage:{name}")
            result["evidence_links_seen"].append(name)
        else:
            _fail(result, f"evidence_linkage:{name}", f"missing output artifact reference: {name}")


def _check_public_relative_path(result: dict[str, Any]) -> None:
    path = result["artifact_path"]
    if path.startswith("/") or ".." in Path(path).parts:
        _fail(result, "public_relative_path", f"path is not repo-relative public path: {path}")
    else:
        _pass(result, "public_relative_path")


def _check_artifact_type(result: dict[str, Any]) -> None:
    if result["artifact_type"] == "unknown":
        _fail(result, "artifact_type_recognition", "artifact type could not be inferred")
    else:
        _pass(result, "artifact_type_recognition")


def _check_spec_schema_presence(result: dict[str, Any], root: Path) -> None:
    paths = SPEC_SCHEMA_BY_TYPE.get(result["artifact_type"])
    if paths is None:
        return
    spec_path, schema_path = paths
    if (root / spec_path).exists():
        _pass(result, "schema_presence:spec")
        result["evidence_links_seen"].append(spec_path)
    else:
        _fail(result, "schema_presence:spec", f"missing public spec: {spec_path}")
    if (root / schema_path).exists():
        _pass(result, "schema_presence:schema")
        result["evidence_links_seen"].append(schema_path)
    else:
        _fail(result, "schema_presence:schema", f"missing public schema: {schema_path}")


def _check_non_claims(result: dict[str, Any], text: str) -> None:
    expected = REQUIRED_NON_CLAIMS_BY_TYPE.get(result["artifact_type"], ())
    lowered = text.lower()
    seen = [
        canonical
        for canonical, aliases in NON_CLAIM_ALIASES.items()
        if any(alias.lower() in lowered for alias in aliases)
    ]
    result["non_claims_seen"] = seen
    for claim in expected:
        if claim in seen:
            _pass(result, f"non_claim:{claim}")
        else:
            _fail(result, f"non_claim:{claim}", f"missing explicit non-claim: {claim}")


def _check_claim_boundary(result: dict[str, Any], text: str) -> None:
    lowered = text.lower()
    if "claim boundary" in lowered or "claim_boundary" in lowered:
        _pass(result, "claim_boundary_present")
    else:
        _fail(result, "claim_boundary_present", "missing claim-boundary wording")

    for phrase in UNSUPPORTED_POSITIVE_CLAIMS:
        for index in _find_all(lowered, phrase):
            context = lowered[max(0, index - 16) : index + len(phrase) + 24]
            if _is_boundary_context(context):
                continue
            _fail(
                result,
                "claim_boundary_check",
                f"unsupported claim phrase outside boundary context: {phrase}",
            )


def _artifact_text(path: Path) -> str:
    if path.is_dir():
        chunks = []
        for child in sorted(path.iterdir()):
            if child.is_file() and child.suffix in {".md", ".json", ".yaml", ".csv"}:
                chunks.append(child.read_text(encoding="utf-8"))
        return "\n".join(chunks)
    return path.read_text(encoding="utf-8")


def _markdown_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return sections


def _find_all(text: str, phrase: str) -> list[int]:
    starts: list[int] = []
    start = 0
    while True:
        index = text.find(phrase, start)
        if index == -1:
            return starts
        starts.append(index)
        start = index + len(phrase)


def _is_boundary_context(context: str) -> bool:
    return any(
        marker in context
        for marker in (
            "no ",
            "not ",
            "does not",
            "do not",
            "unsupported",
            "non-claim",
            "non_claim",
            "without",
            "claim-boundary",
        )
    )


def _pass(result: dict[str, Any], name: str) -> None:
    result["checks"].append({"name": name, "status": PASS})


def _fail(result: dict[str, Any], name: str, issue: str) -> None:
    result["checks"].append({"name": name, "status": FAIL})
    if issue not in result["issues"]:
        result["issues"].append(issue)


def _finalize(result: dict[str, Any]) -> dict[str, Any]:
    result["non_claims_seen"] = sorted(set(result["non_claims_seen"]))
    result["evidence_links_seen"] = sorted(set(result["evidence_links_seen"]))
    result["status"] = FAIL if result["issues"] else WARNING if result["warnings"] else PASS
    return result


def _display_path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()
