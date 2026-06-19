from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_review_packet_raw_urls.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("verify_review_packet_raw_urls", SCRIPT)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_raw_url_verifier_uses_curl_and_expected_urls() -> None:
    text = SCRIPT.read_text(encoding="utf-8")

    assert '"curl"' in text
    assert "raw.githubusercontent.com/Permea-lab/permea-core" in text
    assert "rev-parse" in text
    assert "--abbrev-ref" in text
    assert "PACKET_OUTPUTS" in text

    module = _load_module()
    target_paths = [target[1] for target in module.RAW_TARGETS]
    assert "docs/review/packets/p-core-053-artifact-consistency-system.md" in target_paths
    assert "docs/review/packets/p-core-053-artifact-consistency-system.json" in target_paths
    assert "docs/review/packets/p-core-032-reproducibility-bundle.md" in target_paths
    assert "docs/review/packets/p-core-032-reproducibility-bundle.json" in target_paths
    assert "docs/review/packets/p-core-034-evaluation-bundle.md" in target_paths
    assert "docs/review/packets/p-core-034-evaluation-bundle.json" in target_paths
    assert "docs/review/packets/p-core-030-evidence-surface-layer.md" in target_paths
    assert "docs/review/packets/p-core-030-evidence-surface-layer.json" in target_paths


def test_raw_byte_analysis_detects_physical_lines() -> None:
    module = _load_module()
    sample = b"# Title\n\n```bash\npython3 scripts/permea_review_packet.py\n```\n"

    metrics = module.analyze_bytes(sample)

    assert metrics["byte_count"] == len(sample)
    assert metrics["line_count"] == 5
    assert metrics["newline_count"] == 5
    assert metrics["ends_with_newline"] is True
    assert metrics["literal_backslash_n_count"] == 0
    assert metrics["first_20_lines"][0] == "# Title"


def test_raw_byte_analysis_detects_literal_backslash_n_compression() -> None:
    module = _load_module()
    sample = b"# Title\\n\\ncompressed"

    metrics = module.analyze_bytes(sample)

    assert metrics["line_count"] == 1
    assert metrics["literal_backslash_n_count"] == 2
    assert metrics["ends_with_newline"] is False
