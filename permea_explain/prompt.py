"""prompt.py -- the one shared prompt contract for narrating a Diagnosis.

Zero computation: it serializes the report (stable key order) into the user message and
carries the absolute rules in ``SYSTEM_PROMPT``. The engine produces every number; the model
only restates what the Diagnosis already says, in Korean. The rules mirror the guardrails so
the model is told the exact contract it will be checked against (defence in depth).

Non-numeric context: the static ``title``/``description`` of each fired code is pulled from
the ``permea_core`` warning registry (a one-way import) so the model can explain what a code
means. The numeric allowed-set is taken strictly from the report's typed fields, never from
registry prose -- and only ACTIVE codes fire, whose descriptions carry no numeric literals.
That last clause was an unchecked assertion and was false in practice (W001/W002 carried
"permea-eval/1.0", W101 "Paper 1 P1", W501 a hardcoded "95%"), so faithful narrations copied
numbers no report field could back and the provenance guard withheld them. The literals are
gone and ``tests/test_explain_registry_numerals.py`` now enforces the invariant against the
guardrail's own extractor.
"""
from __future__ import annotations

import json

from permea_core.contracts.warnings import REGISTRY

PROMPT_TEMPLATE_VERSION = "permea-explain-narrate-prompt/0.1"

SYSTEM_PROMPT = """\
당신은 Permea 평가-진단(Diagnosis) 리포트의 해설자입니다. 결정론적 엔진이 이미
Diagnosis 를 계산했습니다. 당신의 유일한 임무는 그 Diagnosis 를 한국어 산문으로
설명하는 것입니다. 당신은 어떤 것도 계산하지 않습니다.

절대 규칙 — 모두 지키십시오. 자동 guardrail 이 위반을 거부합니다.

1. 엔진이 모든 숫자를 소유합니다. 숫자를 만들거나, 추정하거나, 반올림하거나,
   재계산하지 마십시오. 출력의 모든 숫자는 Diagnosis JSON 의 타입이 있는 숫자 필드
   값과 문자 그대로 일치해야 합니다. 리포맷 금지 — 0.0432 를 "4.32%" 나 "4%" 로
   바꾸지 말고 그대로 쓰십시오. JSON 의 숫자 필드에 없는 숫자는 출력에 나올 수
   없습니다. 신뢰수준(예: "95% 신뢰구간"의 95)처럼 숫자 필드가 아니라 설명 문자열
   안에만 있는 값은 숫자로 다시 쓰지 마십시오. 아래의 레지스트리 설명(경고 코드의
   의미)도 숫자의 출처가 아닙니다. 그 안에 숫자·버전·논문 참조가 보이더라도 출력에
   옮기지 마십시오.

2. fired 목록에 있는 경고만 서술하십시오. fired 에 없는 경고 코드(PERMEA-W###)를
   지어내지 마십시오.

3. 각 코드의 severity 를 있는 그대로 존중하십시오. WARN 을 확정·조작으로 격상하지
   마십시오.

4. 근거 없는 생물학·인과 주장을 하지 마십시오. Diagnosis 필드가 직접 뒷받침하지
   않는 주장은 하지 마십시오. 이 리포트는 평가 방법의 타당성에 관한 것이지, 특정
   펩타이드의 뇌 투과 여부에 관한 것이 아닙니다.

5. Diagnosis 에 없는 해결책·권고를 지어내지 마십시오.

6. 이 해설은 비권위적(non-authoritative)입니다. Diagnosis 와 이 해설이 다르면
   항상 Diagnosis 가 옳습니다.

출력은 한국어 산문으로만 작성하십시오."""


def _registry_context(report: dict) -> str:
    """Static title/description for each fired code, as read-only context (no numbers)."""
    lines: list[str] = []
    for f in report.get("fired", []):
        spec = REGISTRY.get(f.get("code"))
        if spec is None:
            continue
        lines.append(f"- {spec.code} ({spec.title}): {spec.description}")
    return "\n".join(lines) if lines else "(발화된 경고 없음)"


def build_messages(report: dict, output_language: str = "korean") -> tuple[str, str]:
    """Return ``(system, user)``. The report is serialized with stable key order; nothing computed."""
    report_json = json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False)
    lang = output_language or "korean"
    user = (
        f"다음 Diagnosis 를 {lang} 산문으로 해설하십시오. 시스템 지시의 모든 규칙을 "
        "따르고, 아래에 있는 필드만 사용하며, 모든 숫자를 문자 그대로 복사하십시오.\n\n"
        "발화된 각 경고 코드의 의미(정적 레지스트리 설명 — 숫자 출처가 아님):\n"
        f"{_registry_context(report)}\n\n"
        f"Diagnosis JSON (권위 있는 숫자의 유일한 출처):\n{report_json}"
    )
    return SYSTEM_PROMPT, user
