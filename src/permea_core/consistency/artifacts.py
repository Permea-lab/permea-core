"""Discover and validate public artifact navigation surfaces."""

from __future__ import annotations

from dataclasses import dataclass
import json
import re
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

PASS = "PASS"
FAIL = "FAIL"

PUBLIC_MARKDOWN_ROOTS = (
    "docs/architecture",
    "docs/artifacts",
    "docs/benchmarks",
    "docs/datasets",
    "docs/evidence",
    "docs/integrations",
    "docs/lineage",
    "docs/reports",
    "docs/research",
    "docs/review",
    "docs/specs",
)
PUBLIC_MARKDOWN_FILES = (
    "README.md",
    "QUICKSTART.md",
    "OPEN_THIS_FIRST.md",
    "REVIEW_HUB.md",
    "REPRODUCIBILITY.md",
    "EVALUATION.md",
)
IMPORTANT_REVIEW_SURFACES = (
    "README.md",
    "QUICKSTART.md",
    "docs/review/README.md",
    "docs/evidence/README.md",
    "docs/evidence/evidence-map.md",
    "docs/benchmarks/README.md",
    "docs/datasets/README.md",
    "docs/research/README.md",
    "docs/integrations/README.md",
    "docs/lineage/README.md",
    "docs/architecture/README.md",
    "docs/artifacts/README.md",
    "docs/reports/README.md",
    "docs/claims/claim-registry.md",
    "docs/specs/README.md",
    "docs/examples/generated/ARTIFACT_INDEX.md",
    "docs/examples/generated/EVALUATION_PACKET.md",
    "docs/examples/generated/REPRODUCIBILITY_REPORT.md",
)
LOCAL_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_LINK_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
)


@dataclass(frozen=True)
class Artifact:
    """A public markdown artifact included in consistency checks."""

    path: str
    category: str


@dataclass(frozen=True)
class Issue:
    """A consistency issue found in a public artifact surface."""

    code: str
    path: str
    message: str


def discover_artifacts(root: Path) -> list[Artifact]:
    """Return deterministic public markdown inventory."""
    artifacts: list[Artifact] = []
    for file_path in PUBLIC_MARKDOWN_FILES:
        path = root / file_path
        if path.exists():
            artifacts.append(Artifact(file_path, "root"))

    for directory in PUBLIC_MARKDOWN_ROOTS:
        base = root / directory
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            artifacts.append(Artifact(_relative(path, root), directory))

    return sorted(set(artifacts), key=lambda artifact: artifact.path)


def validate_artifact_consistency(root: Path) -> dict[str, object]:
    """Validate local links, review reachability, and report index coverage."""
    artifacts = discover_artifacts(root)
    artifact_paths = {artifact.path for artifact in artifacts}
    issues: list[Issue] = []

    issues.extend(_missing_local_link_issues(root, artifacts))
    issues.extend(_missing_review_reachability_issues(root))
    issues.extend(_missing_report_index_issues(root))

    result = {
        "status": PASS if not issues else FAIL,
        "artifact_count": len(artifacts),
        "issue_count": len(issues),
        "artifacts": [artifact.__dict__ for artifact in artifacts],
        "checked_surface_count": len(artifact_paths),
        "required_review_surfaces": list(IMPORTANT_REVIEW_SURFACES),
        "issues": [issue.__dict__ for issue in issues],
        "non_claims": [
            "documentation consistency only",
            "no biological result claim",
            "no wet-lab validation claim",
            "no clinical efficacy claim",
            "no solved-delivery claim",
        ],
    }
    return result


def render_summary(result: dict[str, object]) -> str:
    """Render a human-readable consistency summary."""
    lines = [
        "Permea Core artifact consistency",
        "",
        f"Artifact Consistency System Ready",
        "",
        f"Status: {result['status']}",
        f"Public markdown artifacts discovered: {result['artifact_count']}",
        f"Consistency issues: {result['issue_count']}",
        "",
        "Checks:",
        "- public markdown artifact inventory discovery",
        "- local markdown link target existence",
        "- important review surface reachability from OPEN_THIS_FIRST.md or REVIEW_HUB.md",
        "- docs/reports/README.md coverage for public report files",
        "",
        "Claim-boundary reminder:",
        "- artifact consistency checks review documentation and reproducibility surfaces",
        "- no scientific, biological, wet-lab, clinical, performance, or solved-delivery claim is made by this layer",
        "",
        "Next recommended commands:",
        "- python3 scripts/permea_validate.py",
        "- python3 scripts/validate_permea_artifacts.py",
        "- python3 -m pytest",
    ]

    issues = result["issues"]
    if issues:
        lines.extend(["", "Issues:"])
        for issue in issues:  # type: ignore[assignment]
            lines.append(f"- {issue['code']} {issue['path']}: {issue['message']}")
    else:
        lines.extend(["", "Issues:", "- none"])

    return "\n".join(lines) + "\n"


def render_json(result: dict[str, object]) -> str:
    """Render deterministic JSON for automation and tests."""
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def _missing_local_link_issues(root: Path, artifacts: Iterable[Artifact]) -> list[Issue]:
    issues: list[Issue] = []
    for artifact in artifacts:
        source = root / artifact.path
        text = source.read_text(encoding="utf-8")
        for raw_target in LOCAL_LINK_RE.findall(text):
            target = _clean_link_target(raw_target)
            if _ignore_link_target(target):
                continue
            target_path = _resolve_link(root, source, target)
            if not target_path.exists():
                issues.append(
                    Issue(
                        "MISSING_LINK",
                        artifact.path,
                        f"{raw_target} -> {_relative(target_path, root)}",
                    )
                )
    return issues


def _missing_review_reachability_issues(root: Path) -> list[Issue]:
    open_first = _read_optional(root / "OPEN_THIS_FIRST.md")
    review_hub = _read_optional(root / "REVIEW_HUB.md")
    combined = f"{open_first}\n{review_hub}"
    issues: list[Issue] = []
    for surface in IMPORTANT_REVIEW_SURFACES:
        if not (root / surface).exists():
            issues.append(Issue("MISSING_SURFACE", surface, "required review surface does not exist"))
            continue
        if surface not in combined:
            issues.append(
                Issue(
                    "UNREACHABLE_SURFACE",
                    surface,
                    "not linked from OPEN_THIS_FIRST.md or REVIEW_HUB.md",
                )
            )
    return issues


def _missing_report_index_issues(root: Path) -> list[Issue]:
    reports_dir = root / "docs/reports"
    reports_index = reports_dir / "README.md"
    if not reports_index.exists():
        return [Issue("MISSING_REPORT_INDEX", "docs/reports/README.md", "reports index is missing")]

    index_text = reports_index.read_text(encoding="utf-8")
    issues: list[Issue] = []
    for report_path in sorted(reports_dir.glob("*.md")):
        if report_path.name == "README.md":
            continue
        if report_path.name not in index_text:
            issues.append(
                Issue(
                    "MISSING_REPORT_INDEX_ENTRY",
                    _relative(report_path, root),
                    "not linked from docs/reports/README.md",
                )
            )
    return issues


def _clean_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith("#"):
        target = target.split(" ", 1)[0]
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    return unquote(target)


def _ignore_link_target(target: str) -> bool:
    if not target:
        return True
    lowered = target.lower()
    return lowered.startswith(IGNORED_LINK_PREFIXES)


def _resolve_link(root: Path, source: Path, target: str) -> Path:
    if target.startswith("/"):
        return (root / target.lstrip("/")).resolve()
    return (source.parent / target).resolve()


def _read_optional(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _relative(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()
