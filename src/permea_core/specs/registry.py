"""Deterministic registry for Permea Core public artifact specifications."""

from __future__ import annotations

from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PASS = "PASS"
SPEC_INDEX_PATH = "docs/specs/README.md"

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

SPEC_ROWS: tuple[dict[str, str], ...] = (
    {
        "artifact": "Dataset Card",
        "family": "dataset_cards/",
        "spec_path": "docs/specs/SPEC_DATASET_CARD.md",
        "schema_path": "schemas/dataset_card.schema.json",
        "purpose": "Minimum public structure for dataset source, labels, readiness, limitations, and provenance.",
    },
    {
        "artifact": "Benchmark Card",
        "family": "benchmark_cards/",
        "spec_path": "docs/specs/SPEC_BENCHMARK_CARD.md",
        "schema_path": "schemas/benchmark_card.schema.json",
        "purpose": "Minimum public structure for benchmark task intent, metrics, split policy, outputs, and boundaries.",
    },
    {
        "artifact": "Evidence Card",
        "family": "evidence_cards/",
        "spec_path": "docs/specs/SPEC_EVIDENCE_CARD.md",
        "schema_path": "schemas/evidence_card.schema.json",
        "purpose": "Minimum public structure for source-backed evidence records, uncertainty, and review status.",
    },
    {
        "artifact": "Run Manifest",
        "family": "run_manifests/",
        "spec_path": "docs/specs/SPEC_RUN_MANIFEST.md",
        "schema_path": "schemas/run_manifest.schema.json",
        "purpose": "Minimum public structure for reproducible run provenance and generated output paths.",
    },
    {
        "artifact": "Output Package",
        "family": "output_packages/",
        "spec_path": "docs/specs/SPEC_OUTPUT_PACKAGE.md",
        "schema_path": "schemas/output_package.schema.json",
        "purpose": "Minimum public structure for reviewer-facing benchmark output bundles.",
    },
)


def collect_spec_registry(root_path: str | Path = ".") -> dict[str, Any]:
    """Collect public artifact specification registry metadata."""
    root = Path(root_path).resolve()
    specs = [
        {
            **row,
            "spec_exists": (root / row["spec_path"]).exists(),
            "schema_exists": (root / row["schema_path"]).exists(),
        }
        for row in SPEC_ROWS
    ]
    registry = {
        "status": PASS,
        "spec_index_path": SPEC_INDEX_PATH,
        "specifications": specs,
        "non_claims": list(NON_CLAIMS),
    }
    _assert_public_relative(registry)
    return registry


def render_spec_registry(registry: dict[str, Any]) -> str:
    """Render a deterministic text report for the spec registry CLI."""
    lines = [
        f"{registry['status']} Permea artifact specification registry",
        "",
        f"Spec index: {registry['spec_index_path']}",
        "",
        "Specifications:",
    ]
    for item in registry["specifications"]:
        lines.extend(
            [
                f"- {item['artifact']}",
                f"  family: {item['family']}",
                f"  markdown: {item['spec_path']} ({'present' if item['spec_exists'] else 'missing'})",
                f"  schema: {item['schema_path']} ({'present' if item['schema_exists'] else 'missing'})",
                f"  purpose: {item['purpose']}",
            ]
        )
    lines.extend(["", "Explicit Non-Claims:"])
    lines.extend(f"- {claim}" for claim in registry["non_claims"])
    lines.append("")
    return "\n".join(lines)


def _assert_public_relative(value: Any) -> None:
    if isinstance(value, dict):
        for nested in value.values():
            _assert_public_relative(nested)
    elif isinstance(value, list):
        for nested in value:
            _assert_public_relative(nested)
    elif isinstance(value, str):
        if str(ROOT) in value or value.startswith("/"):
            raise ValueError(f"non-public or absolute path in spec registry: {value}")

