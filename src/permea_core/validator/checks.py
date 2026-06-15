"""Lightweight public artifact checks for Permea Core example artifacts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from permea_core.specs.registry import NON_CLAIMS

PASS = "PASS"
FAIL = "FAIL"

FORBIDDEN_BOUNDARY_PATTERNS: tuple[str, ...] = (
    "AI " + "Champion",
    "H" + "100",
    "K-" + "EXAONE",
    "Chat" + "GPT",
    "Co" + "dex",
    "pro" + "mpt",
    "local" + "-only",
    "assigned " + "GPU",
    "competi" + "tion",
    "sponsor" + "ship",
    "cloud " + "credits",
    "API " + "key",
    "pass" + "word",
    "sec" + "ret",
    "tok" + "en",
    "KO" + "RA",
)

CREDENTIAL_PATTERNS: tuple[str, ...] = (
    "API" + "_KEY",
    "SEC" + "RET",
    "TOK" + "EN",
    "PASS" + "WORD",
    "PRIVATE " + "KEY",
    "BEGIN " + "RSA",
    "s" + "k-",
    "g" + "hp_",
    "xo" + "xb-",
    "A" + "KIA",
    "AI" + "za",
)

FAMILY_CHECKS: dict[str, dict[str, Any]] = {
    "dataset_card": {
        "files": (
            "docs/examples/generated/dataset_cards/b3pred_dataset3.md",
            "docs/examples/generated/dataset_cards/cppsite2_placeholder.md",
        ),
        "schema_path": "schemas/dataset_card.schema.json",
        "required_aliases": {
            "dataset_id": ("## Dataset ID",),
            "dataset_name": ("# Dataset Card:",),
            "source": ("## Source IDs",),
            "label_schema": ("## Label Type",),
            "limitations": ("## Known Limitations",),
            "claim_boundary": ("## Claim Boundary",),
        },
    },
    "benchmark_card": {
        "files": (
            "docs/examples/generated/benchmark_cards/bbb_b3pred_dataset3.md",
            "docs/examples/generated/benchmark_cards/cpp_cppsite2_placeholder.md",
        ),
        "schema_path": "schemas/benchmark_card.schema.json",
        "required_aliases": {
            "benchmark_id": ("## Benchmark ID",),
            "task_type": ("## Task Name",),
            "dataset_card_refs": ("## Dataset Card",),
            "split_policy": ("## Split Policy",),
            "metric_set": ("## Metrics",),
            "output_artifacts": ("## Output Artifacts",),
            "limitations": ("## Limitations",),
            "claim_boundary": ("## Claim Boundary",),
        },
    },
    "evidence_card": {
        "files": (
            "docs/examples/generated/evidence_cards/bbb_b3pred_dataset3.evidence_cards.json",
            "docs/examples/generated/evidence_cards/cpp_cppsite2_placeholder.evidence_cards.json",
        ),
        "schema_path": "schemas/evidence_card.schema.json",
        "required_aliases": {
            "evidence_id": ("evidence_id", "evidence_card_id"),
            "source": ("source", "source_reference"),
            "evidence_type": ("evidence_type",),
            "extracted_claim": ("extracted_claim",),
            "limitations": ("limitations",),
            "review_status": ("review_status",),
            "claim_boundary": ("claim_boundary",),
        },
    },
    "run_manifest": {
        "files": ("docs/examples/generated/run_manifests/example_artifact_generation.md",),
        "schema_path": "schemas/run_manifest.schema.json",
        "required_aliases": {
            "run_id": ("## Run ID",),
            "run_type": ("## Run Type",),
            "repository_commit": ("## Provenance Summary", "## Generated At"),
            "command": ("## Commands",),
            "inputs": ("## Benchmark IDs", "## Dataset IDs",),
            "artifact_paths": ("## Generated Artifacts",),
            "limitations": ("## Limitations",),
            "claim_boundary": ("## Claim Boundary",),
        },
    },
    "output_package": {
        "files": ("docs/examples/generated/output_packages/bbb_b3pred_dataset3/manifest.yaml",),
        "schema_path": "schemas/output_package.schema.json",
        "required_aliases": {
            "package_id": ("package_id", "run_id"),
            "manifest_path": ("manifest_path", "run_id"),
            "metrics_path": ("metrics_path", "metrics_output_path"),
            "benchmark_card_path": ("benchmark_card_path",),
            "limitations": ("limitations",),
            "claim_boundary": ("claim_boundary",),
        },
    },
}


def check_artifacts(
    root_path: str | Path = ".",
    *,
    family: str | None = None,
    file_path: str | Path | None = None,
) -> dict[str, Any]:
    """Check public example artifacts against lightweight spec expectations."""
    root = Path(root_path).resolve()
    selected = _select_families(family, file_path)
    failed: list[str] = []
    warnings: list[str] = []
    checked_files: list[str] = []

    for family_name in selected:
        config = FAMILY_CHECKS[family_name]
        paths = _selected_files_for_family(config, file_path)
        schema_required = _load_schema_required(root / config["schema_path"], failed)
        for rel_path in paths:
            checked_files.append(rel_path)
            artifact_path = root / rel_path
            if not artifact_path.exists():
                failed.append(f"{family_name}: missing file {rel_path}")
                continue
            text = artifact_path.read_text(encoding="utf-8")
            _check_required_fields(family_name, rel_path, text, schema_required, config, failed)
            _check_claim_boundary(family_name, rel_path, text, failed, warnings)
            _check_forbidden_terms(family_name, rel_path, text, failed)
            _check_credential_terms(family_name, rel_path, text, failed)

    report = {
        "status": PASS if not failed else FAIL,
        "checked_families": selected,
        "checked_files": checked_files,
        "failed_checks": failed,
        "warnings": warnings,
        "non_claim_boundary_status": PASS if not failed else FAIL,
    }
    _assert_public_relative(report)
    return report


def _select_families(family: str | None, file_path: str | Path | None) -> list[str]:
    if family is not None:
        if family not in FAMILY_CHECKS:
            raise ValueError(f"unknown artifact family: {family}")
        return [family]
    if file_path is not None:
        rel = str(file_path)
        matches = [
            name
            for name, config in FAMILY_CHECKS.items()
            if rel in config["files"] or any(rel.endswith(path) for path in config["files"])
        ]
        if not matches:
            raise ValueError(f"could not infer artifact family for file: {rel}")
        return [matches[0]]
    return list(FAMILY_CHECKS)


def _selected_files_for_family(config: dict[str, Any], file_path: str | Path | None) -> list[str]:
    if file_path is None:
        return list(config["files"])
    rel = str(file_path)
    for known in config["files"]:
        if rel == known or rel.endswith(known):
            return [known]
    return [rel]


def _load_schema_required(schema_path: Path, failed: list[str]) -> list[str]:
    if not schema_path.exists():
        failed.append(f"missing schema {schema_path.as_posix()}")
        return []
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    return list(schema.get("required", []))


def _check_required_fields(
    family: str,
    rel_path: str,
    text: str,
    schema_required: list[str],
    config: dict[str, Any],
    failed: list[str],
) -> None:
    aliases = config["required_aliases"]
    for field in schema_required:
        field_aliases = aliases.get(field, (field,))
        if not any(alias in text for alias in field_aliases):
            failed.append(f"{family}: {rel_path} missing required field concept {field}")


def _check_claim_boundary(
    family: str,
    rel_path: str,
    text: str,
    failed: list[str],
    warnings: list[str],
) -> None:
    lowered = text.lower()
    if "claim_boundary" not in lowered and "claim boundary" not in lowered:
        failed.append(f"{family}: {rel_path} missing claim-boundary language")
    if not any(claim.lower() in lowered for claim in NON_CLAIMS):
        warnings.append(f"{family}: {rel_path} has claim boundary but no registry non-claim phrase")


def _check_forbidden_terms(family: str, rel_path: str, text: str, failed: list[str]) -> None:
    for pattern in FORBIDDEN_BOUNDARY_PATTERNS:
        if re.search(re.escape(pattern), text, flags=re.IGNORECASE):
            failed.append(f"{family}: {rel_path} contains forbidden boundary term {pattern}")


def _check_credential_terms(family: str, rel_path: str, text: str, failed: list[str]) -> None:
    for pattern in CREDENTIAL_PATTERNS:
        if pattern in text:
            failed.append(f"{family}: {rel_path} contains credential-like term {pattern}")


def _assert_public_relative(value: Any) -> None:
    if isinstance(value, dict):
        for nested in value.values():
            _assert_public_relative(nested)
    elif isinstance(value, list):
        for nested in value:
            _assert_public_relative(nested)
    elif isinstance(value, str):
        if value.startswith("/"):
            raise ValueError(f"absolute path in validator report: {value}")
