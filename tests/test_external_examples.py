from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permea_core.validation.artifact_validator import PASS, validate_artifact  # noqa: E402


EXAMPLES = (
    "synthetic_reference_example",
    "bbb_peptide_reference_example",
    "expression_engineering_reference_example",
)

REQUIRED_FILES = (
    "README.md",
    "dataset_card.json",
    "benchmark_card.json",
    "evidence_card.json",
    "run_manifest.json",
    "output_package.json",
    "validation_result.md",
    "validation_result.json",
)

REQUIRED_README_SECTIONS = (
    "## Overview",
    "## What this example demonstrates",
    "## Files included",
    "## How to validate this example",
    "## How to adapt this example",
    "## Claim boundaries",
    "## Explicit non-claims",
    "## Limitations",
    "## Next steps",
)

REQUIRED_NON_CLAIMS = (
    "no dataset downloaded",
    "no acquisition executed",
    "no redistribution rights confirmed",
    "no wet-lab validation by Permea",
    "no clinical efficacy claim",
    "no model performance claim",
    "no SOTA claim",
    "no solved-delivery claim",
)


def test_all_example_directories_exist() -> None:
    for example in EXAMPLES:
        assert (ROOT / "examples" / example).is_dir()


def test_each_example_has_required_files() -> None:
    for example in EXAMPLES:
        directory = ROOT / "examples" / example
        for filename in REQUIRED_FILES:
            assert (directory / filename).exists()


def test_each_example_readme_has_required_sections() -> None:
    for example in EXAMPLES:
        text = (ROOT / "examples" / example / "README.md").read_text(encoding="utf-8")
        for section in REQUIRED_README_SECTIONS:
            assert section in text


def test_each_example_json_file_parses() -> None:
    for example in EXAMPLES:
        directory = ROOT / "examples" / example
        for filename in REQUIRED_FILES:
            if filename.endswith(".json"):
                payload = json.loads((directory / filename).read_text(encoding="utf-8"))
                assert isinstance(payload, dict)


def test_each_validation_result_json_passes() -> None:
    for example in EXAMPLES:
        payload = json.loads(
            (ROOT / "examples" / example / "validation_result.json").read_text(
                encoding="utf-8"
            )
        )
        assert payload["status"] == PASS
        assert payload["artifacts_checked"] == 5
        assert payload["failures"] == []


def test_validator_passes_each_example_directory() -> None:
    for example in EXAMPLES:
        result = validate_artifact(ROOT / "examples" / example, ROOT)
        assert result["status"] == PASS


def test_required_non_claims_are_present() -> None:
    for example in EXAMPLES:
        combined = "\n".join(
            (ROOT / "examples" / example / filename).read_text(encoding="utf-8")
            for filename in REQUIRED_FILES
        )
        for claim in REQUIRED_NON_CLAIMS:
            assert claim in combined


def test_root_examples_readme_links_all_examples() -> None:
    text = (ROOT / "examples" / "README.md").read_text(encoding="utf-8")
    for example in EXAMPLES:
        assert f"{example}/README.md" in text


def test_cli_validates_each_example_directory() -> None:
    for example in EXAMPLES:
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "permea_check.py"),
                f"examples/{example}",
            ],
            cwd=ROOT,
            check=False,
            text=True,
            capture_output=True,
        )
        assert completed.returncode == 0
        assert "Status: PASS" in completed.stdout
        assert "Artifacts checked: 1" in completed.stdout
