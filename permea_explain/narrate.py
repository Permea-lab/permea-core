"""narrate.py -- NARRATE entrypoint: a frozen Diagnosis JSON -> a verified interpretation.

Read-only over the report. Every number in the narration is verified to trace to the report
BEFORE anything is written: verification is a precondition of writing, not a flag on the
output. If any guardrail fails, ``render_checked`` raises and no interpretation is produced.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from . import guardrails, prompt, source
from .providers import get_provider

SCHEMA_ID = "permea.interpretation/1.0"
_TEMPERATURE = 0.2
_MAX_TOKENS = 700

_DISCLAIMER = (
    "이 문서는 Permea 진단 리포트에 대한 기계 생성 해설입니다. 평가 기록의 일부가 아니며, "
    "어떤 권위도 갖지 않고, 스스로 어떤 숫자도 만들지 않습니다. 모든 숫자 값은 원본 "
    "리포트로 추적됩니다. 이 해설과 진단 리포트가 다르면 진단 리포트가 옳습니다."
)


def narrate(report_path, *, provider=None, output_language: str = "korean", out_path=None) -> dict:
    """Narrate a frozen Diagnosis report into a verified, non-authoritative interpretation.

    Returns the interpretation dict. If ``out_path`` is given, the file is written only after
    every guardrail has passed. On any violation a ``GuardrailViolation`` propagates and no
    file is written.
    """
    report, source_sha = source.load_report(report_path)
    system, user = prompt.build_messages(report, output_language=output_language)
    provider = provider or get_provider()
    resp = provider.complete(system, user, max_tokens=_MAX_TOKENS, temperature=_TEMPERATURE)

    # Postcondition on the model output: raises on any violation, so nothing below runs.
    guardrails.render_checked(resp.text, report, output_language=output_language)

    interpretation = _assemble(resp, report, source_sha, temperature=_TEMPERATURE)
    if out_path is not None:
        Path(out_path).write_text(
            json.dumps(interpretation, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    return interpretation


def _assemble(resp, report: dict, source_sha: str, *, temperature: float) -> dict:
    prompt_sha = hashlib.sha256(prompt.SYSTEM_PROMPT.encode("utf-8")).hexdigest()
    return {
        "schema": SCHEMA_ID,
        "authoritative": False,
        "source_report_sha256": source_sha,
        "model": {
            "provider": resp.provider,
            "model_id": resp.model_id,
            "temperature": temperature,
            "prompt_sha256": prompt_sha,
        },
        "narrative": {
            "summary": resp.text,
            "audience": "non_specialist",
            "language": "ko",
        },
        "numeric_provenance": {
            "verified": True,
            "numbers_in_narrative": guardrails.numbers_in_narrative(resp.text),
            "all_numbers_traced": True,
            "verifier_version": guardrails.VERIFIER_VERSION,
        },
        "disclaimer": _DISCLAIMER,
    }
