#!/usr/bin/env python3
"""Verify GitHub raw readability for generated review packet files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.review_packets import PACKET_OUTPUTS  # noqa: E402

DEFAULT_BRANCH = None
RAW_TARGETS = tuple(
    (f"{packet_id} markdown", outputs["markdown"], 70)
    for packet_id, outputs in PACKET_OUTPUTS.items()
) + tuple(
    (f"{packet_id} json", outputs["json"], 35)
    for packet_id, outputs in PACKET_OUTPUTS.items()
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--branch",
        default=DEFAULT_BRANCH,
        help="GitHub branch or ref to verify; defaults to the current git branch",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="print deterministic JSON instead of a human-readable summary",
    )
    args = parser.parse_args()

    branch = args.branch or _current_branch()
    result = verify_raw_urls(branch)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_summary(result))
    return 0 if result["status"] == "PASS" else 1


def verify_raw_urls(branch: str) -> dict[str, object]:
    """Fetch configured GitHub raw URLs with curl and report line evidence."""
    branch_head = _remote_branch_head(branch)
    checks = []
    for label, path, minimum_lines in RAW_TARGETS:
        url = f"https://raw.githubusercontent.com/Permea-lab/permea-core/{branch}/{path}"
        raw = _curl_raw(url)
        metrics = analyze_bytes(raw["body"])
        passed = (
            raw["http_status"] == 200
            and metrics["line_count"] >= minimum_lines
            and metrics["ends_with_newline"]
            and metrics["literal_backslash_n_count"] == 0
        )
        checks.append(
            {
                "label": label,
                "path": path,
                "url": url,
                "http_status": raw["http_status"],
                "byte_count": metrics["byte_count"],
                "line_count": metrics["line_count"],
                "newline_count": metrics["newline_count"],
                "ends_with_newline": metrics["ends_with_newline"],
                "literal_backslash_n_count": metrics["literal_backslash_n_count"],
                "first_20_lines": metrics["first_20_lines"],
                "minimum_lines": minimum_lines,
                "status": "PASS" if passed else "FAIL",
            }
        )

    return {
        "status": "PASS" if all(check["status"] == "PASS" for check in checks) else "FAIL",
        "branch": branch,
        "remote_branch_head": branch_head,
        "checks": checks,
    }


def analyze_bytes(data: bytes) -> dict[str, object]:
    """Return physical line-readability metrics for raw file bytes."""
    text = data.decode("utf-8", errors="replace")
    return {
        "byte_count": len(data),
        "line_count": len(data.splitlines()),
        "newline_count": data.count(b"\n"),
        "ends_with_newline": data.endswith(b"\n"),
        "literal_backslash_n_count": data.count(b"\\n"),
        "first_20_lines": text.splitlines()[:20],
    }


def render_summary(result: dict[str, object]) -> str:
    """Render a concise human-readable raw verification report."""
    lines = [
        "Permea Core review packet raw URL verification",
        "",
        f"Status: {result['status']}",
        f"Branch: {result['branch']}",
        f"Remote branch HEAD: {result['remote_branch_head']}",
    ]
    for check in result["checks"]:  # type: ignore[assignment]
        lines.extend(
            [
                "",
                f"{check['label']}: {check['status']}",
                f"- url: {check['url']}",
                f"- http_status: {check['http_status']}",
                f"- byte_count: {check['byte_count']}",
                f"- line_count: {check['line_count']}",
                f"- newline_count: {check['newline_count']}",
                f"- ends_with_newline: {check['ends_with_newline']}",
                f"- literal_backslash_n_count: {check['literal_backslash_n_count']}",
                "- first_20_lines:",
            ]
        )
        lines.extend(f"  {line}" for line in check["first_20_lines"])
    return "\n".join(lines) + "\n"


def _curl_raw(url: str) -> dict[str, object]:
    with tempfile.NamedTemporaryFile() as tmp:
        completed = subprocess.run(
            ["curl", "-L", "-sS", "-w", "%{http_code}", "-o", tmp.name, url],
            check=True,
            text=True,
            capture_output=True,
        )
        body = Path(tmp.name).read_bytes()
    return {"http_status": int(completed.stdout), "body": body}


def _remote_branch_head(branch: str) -> str:
    completed = subprocess.run(
        ["git", "ls-remote", "origin", f"refs/heads/{branch}"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    if not completed.stdout.strip():
        return "missing"
    return completed.stdout.split()[0]


def _current_branch() -> str:
    completed = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return completed.stdout.strip()


if __name__ == "__main__":
    raise SystemExit(main())
