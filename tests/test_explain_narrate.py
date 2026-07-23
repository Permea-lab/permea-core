"""Tests for the permea_explain NARRATE layer: source, guardrails, and narrate end-to-end.

No network: a FakeProvider supplies the narration text so the guardrails and assembly are
exercised deterministically.
"""
from __future__ import annotations

import json
import re

import pytest

from permea_core.diagnose import diagnose
from permea_core.eval.run import EvalRun, MetricRow
from permea_explain import GuardrailViolation, guardrails, narrate, prompt, source
from permea_explain.extract import extract
from permea_explain.providers.base import Provider, ProviderResponse
from permea_explain.violations import NUMERIC_UNTRACED

GOOD_IDENTITY = {"alignment": "global", "denominator": "shorter_sequence", "gap_treatment": "free"}


def _run(delta_point=-0.05, ci_lo=-0.08, ci_hi=-0.02, ci_excludes_zero=True):
    row = MetricRow(
        model="rf",
        metric="pr_auc",
        A_mean=0.6,
        A_std=0.01,
        B_mean=0.6 + delta_point,
        B_std=0.01,
        delta_point=delta_point,
        delta_boot_median=delta_point,
        ci_lo=ci_lo,
        ci_hi=ci_hi,
        ci_excludes_zero=ci_excludes_zero,
    )
    return EvalRun(
        representation="physchem",
        threshold_label="NA",
        seeds=(0, 1, 2, 3, 4),
        k=5,
        n_boot=2000,
        resample_unit="cluster",
        headline_condition="B",
        identity_definition=GOOD_IDENTITY,
        n=2959,
        pos=269,
        neg=2690,
        n_clusters=1000,
        data_sha256="a" * 64,
        rows=(row,),
    )


def _report_file(tmp_path):
    diag = diagnose(_run())  # fires exactly PERMEA-W101 (critical)
    report = diag.to_dict()
    path = tmp_path / "diagnostic_report.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return path, report


class FakeProvider(Provider):
    """Returns a fixed narration text; no network. Keeps the provider identity 'configured'."""

    name = "configured"

    def __init__(self, text: str):
        self._text = text

    @property
    def model_id(self) -> str:
        return "fake-model"

    def complete(self, system, user, *, max_tokens, temperature=None, stop=None):
        return ProviderResponse(text=self._text, provider="configured", model_id="fake-model")


# A faithful narration: every number is a typed field of the W101 report.
FAITHFUL = (
    "이 실행에서 식별성이 통제된 조건 B 가 헤드라인으로 보고되었습니다. "
    "경고 PERMEA-W101 이 발화되었습니다: rf/pr_auc 의 B-A 델타는 -0.05 이고, "
    "신뢰구간은 -0.08 에서 -0.02 로 0 을 제외하며, 크기가 임계값 0.02 이상입니다. "
    "총 1 개의 심각(critical) 경고가 있고, 클러스터 수는 1000 개입니다."
)


def test_load_report_and_collect_numbers(tmp_path):
    path, report = _report_file(tmp_path)
    loaded, sha = source.load_report(path)
    assert loaded == report
    assert re.fullmatch(r"[a-f0-9]{64}", sha)
    nums = source.collect_numbers(report)
    for expected in (-0.05, -0.08, -0.02, 0.02, 2959.0, 269.0, 2690.0, 1000.0, 1.0, 0.0):
        assert expected in nums


def test_render_checked_passes_faithful(tmp_path):
    _, report = _report_file(tmp_path)
    assert guardrails.render_checked(FAITHFUL, report) == FAITHFUL


def test_precision_aware_matches_4f_forms(tmp_path):
    """The .4f evidence_str forms (-0.0500) must trace to the raw -0.05 typed fields."""
    _, report = _report_file(tmp_path)
    text = "델타는 -0.0500 이고 신뢰구간은 -0.0800 에서 -0.0200 이며 임계값 0.02 이상입니다."
    assert guardrails.render_checked(text, report) == text


def test_fabricated_number_hard_fails(tmp_path):
    _, report = _report_file(tmp_path)
    text = FAITHFUL + " 모델 정확도는 0.87 입니다."  # 0.87 is in no report field
    with pytest.raises(GuardrailViolation, match="0.87"):
        guardrails.render_checked(text, report)


def test_percent_reformat_hard_fails(tmp_path):
    _, report = _report_file(tmp_path)
    text = "델타는 5% 감소했습니다."  # 5 traces to nothing; reformatting 0.05 -> 5%
    with pytest.raises(GuardrailViolation):
        guardrails.render_checked(text, report)


def test_forbidden_phrase_hard_fails(tmp_path):
    _, report = _report_file(tmp_path)
    text = "경고 PERMEA-W101 이 발화되었으며, 이는 데이터가 조작이다 라는 뜻입니다."
    with pytest.raises(GuardrailViolation, match="forbidden phrase"):
        guardrails.render_checked(text, report)


def test_unfired_code_hard_fails(tmp_path):
    _, report = _report_file(tmp_path)
    text = "경고 PERMEA-W301 이 발화되었습니다."  # W301 did not fire
    with pytest.raises(GuardrailViolation, match="PERMEA-W301"):
        guardrails.render_checked(text, report)


def test_narrate_end_to_end_writes_only_on_pass(tmp_path):
    path, report = _report_file(tmp_path)
    _, source_sha = source.load_report(path)
    out = tmp_path / "interpretation.json"
    result = narrate(path, provider=FakeProvider(FAITHFUL), out_path=out)

    assert result["schema"] == "permea.interpretation/1.0"
    assert result["authoritative"] is False
    assert result["source_report_sha256"] == source_sha
    assert result["model"]["provider"] == "configured"
    assert result["model"]["model_id"] == "fake-model"
    assert re.fullmatch(r"[a-f0-9]{64}", result["model"]["prompt_sha256"])
    assert result["narrative"]["summary"] == FAITHFUL
    assert result["narrative"]["language"] == "ko"
    assert result["numeric_provenance"]["verified"] is True
    assert result["numeric_provenance"]["all_numbers_traced"] is True
    assert result["numeric_provenance"]["numbers_in_narrative"]  # non-empty
    assert len(result["disclaimer"]) >= 40

    # File written, and it round-trips.
    on_disk = json.loads(out.read_text(encoding="utf-8"))
    assert on_disk == result


def test_narrate_fabricated_writes_nothing(tmp_path):
    path, _ = _report_file(tmp_path)
    out = tmp_path / "interpretation.json"
    bad = FAITHFUL + " 그리고 정확도는 0.99 입니다."
    with pytest.raises(GuardrailViolation):
        narrate(path, provider=FakeProvider(bad), out_path=out)
    assert not out.exists()  # postcondition: nothing written on failure


# --------------------------------------------------------------------------------------
# Regression: the confidence level is a real report number (live false positive, 2026-07-18)
# --------------------------------------------------------------------------------------
# A real live narration said "95% 신뢰구간" and was rejected: the CI in the report IS a
# 95% bootstrap CI, but the level itself was not carried as a field, so "95" traced to
# nothing. The fix was to emit the level from the engine, not to soften the guardrail --
# these tests pin both halves of that.

def test_stating_the_confidence_level_passes_korean(tmp_path):
    _, report = _report_file(tmp_path)
    text = FAITHFUL + " 95% 신뢰구간은 -0.08 에서 -0.02 입니다."
    assert guardrails.render_checked(text, report) == text


def test_stating_the_confidence_level_passes_english(tmp_path):
    _, report = _report_file(tmp_path)
    text = "The 95% confidence interval runs from -0.08 to -0.02 and excludes 0."
    assert guardrails.render_checked(text, report, output_language="english") == text


def test_confidence_level_traces_to_the_report_field(tmp_path):
    """'95' is traceable because the engine emits it, not because it is exempted."""
    _, report = _report_file(tmp_path)
    assert report["context"]["ci_level_pct"] == 95.0
    assert 95.0 in source.collect_numbers(report)


def test_a_wrong_confidence_level_still_fails(tmp_path):
    """The guardrail stayed literal: only the level actually used is sayable."""
    _, report = _report_file(tmp_path)
    with pytest.raises(GuardrailViolation, match="99"):
        guardrails.render_checked("99% 신뢰구간은 -0.08 에서 -0.02 입니다.", report)


def test_guardrail_strictness_is_unchanged(tmp_path):
    """The new field widened the traceable set by exactly one value, not by a category."""
    _, report = _report_file(tmp_path)
    for fabricated in ("88", "95.5", "0.95"):
        with pytest.raises(GuardrailViolation, match=re.escape(fabricated)):
            guardrails.render_checked(f"신뢰도는 {fabricated} 입니다.", report)


def test_narrate_end_to_end_accepts_the_confidence_level(tmp_path):
    """The exact live case, through the full NARRATE path: it now writes."""
    path, _ = _report_file(tmp_path)
    out = tmp_path / "interpretation.json"
    text = FAITHFUL + " 95% 신뢰구간은 0 을 제외합니다."
    result = narrate(path, provider=FakeProvider(text), out_path=out)
    assert out.exists()
    assert "95" in result["numeric_provenance"]["numbers_in_narrative"]
    assert result["numeric_provenance"]["all_numbers_traced"] is True


# --------------------------------------------------------------------------------------
# Regression: thousands separators (live false positive, 2026-07-18)
# --------------------------------------------------------------------------------------
# A real live narration wrote the sample counts as "2,959" and "2,690" -- the correct
# values, Korean-convention group-formatted. The tokenizer split at the comma and read "2",
# "959", "2", "690", none of which trace. The fix normalizes grouping commas before
# tokenizing; it does not make the parser permissive, so every test below that asserts a
# FAILURE is guarding that boundary.

def test_thousands_separated_counts_trace(tmp_path):
    _, report = _report_file(tmp_path)
    text = "총 표본은 2,959개이며, 음성 2,690개와 클러스터 1,000개를 포함합니다."
    assert guardrails.render_checked(text, report) == text


def test_thousands_separated_and_plain_forms_are_the_same_number(tmp_path):
    _, report = _report_file(tmp_path)
    for grouped, plain in (("2,959", "2959"), ("2,690", "2690"), ("1,000", "1000")):
        assert guardrails.render_checked(f"표본은 {grouped} 입니다.", report)
        assert guardrails.render_checked(f"표본은 {plain} 입니다.", report)


def test_fabricated_number_still_fails_when_group_formatted(tmp_path):
    """Normalization must not become a way to smuggle a number past the check."""
    _, report = _report_file(tmp_path)
    with pytest.raises(GuardrailViolation, match="3141"):
        guardrails.render_checked("표본은 3,141개입니다.", report)


def test_decimal_forms_are_untouched(tmp_path):
    """'.' is the decimal point and ',' only ever groups -- the two never swap roles."""
    _, report = _report_file(tmp_path)
    text = "델타는 -0.0500 이고 임계값은 0.02 이며 95% 신뢰수준입니다."
    assert guardrails.render_checked(text, report) == text
    assert guardrails.numbers_in_narrative(text) == ["-0.0500", "0.02", "95"]


def test_malformed_comma_numbers_are_not_normalized(tmp_path):
    """Only real 3-digit groupings are joined; malformed ones fail exactly as before."""
    _, report = _report_file(tmp_path)
    # "2,95" -> short group; "1,2345" -> over-long group; "1,234,56" -> short trailing group.
    for malformed in ("2,95", "1,2345", "1,234,56"):
        assert "," in malformed
        with pytest.raises(GuardrailViolation):
            guardrails.render_checked(f"표본은 {malformed} 입니다.", report)
    # And none of them were silently joined into a spurious single number.
    assert guardrails.numbers_in_narrative("2,95 1,2345 1,234,56") == [
        "2", "95", "1", "2345", "1", "234", "56",
    ]


def test_adjacent_numbers_are_never_merged(tmp_path):
    """A comma between two distinct numbers must not glue them into a third."""
    assert guardrails.numbers_in_narrative("0.05,100") == ["0.05", "100"]
    _, report = _report_file(tmp_path)
    # 100 is in no report field, so this still fails -- 05100 was never manufactured.
    with pytest.raises(GuardrailViolation, match="100"):
        guardrails.render_checked("값은 0.05,100 입니다.", report)


def test_grouped_negative_and_multi_group_numbers(tmp_path):
    assert guardrails.numbers_in_narrative("-2,959") == ["-2959"]
    assert guardrails.numbers_in_narrative("1,234,567") == ["1234567"]
    assert guardrails.numbers_in_narrative("1,234.56") == ["1234.56"]


def test_narrate_end_to_end_accepts_grouped_counts(tmp_path):
    """The live shape, through the full NARRATE path: both fixes hold together.

    Reconstructed to match the reported failure (grouped counts alongside the "95%" the
    previous fix made traceable) -- the verbatim narration from that run was not captured.
    """
    path, _ = _report_file(tmp_path)
    out = tmp_path / "interpretation.json"
    text = (
        "이 실행에서 식별성이 통제된 조건 B 가 헤드라인으로 보고되었습니다. "
        "경고 PERMEA-W101 이 발화되었습니다: rf/pr_auc 의 B-A 델타는 -0.05 이고, "
        "95% 신뢰수준에서 신뢰구간은 -0.08 에서 -0.02 로 0 을 제외합니다. "
        "총 표본 2,959개 중 양성은 269개, 음성은 2,690개이며 클러스터는 1,000개입니다."
    )
    result = narrate(path, provider=FakeProvider(text), out_path=out)
    assert out.exists()
    nums = result["numeric_provenance"]["numbers_in_narrative"]
    assert "2959" in nums and "2690" in nums and "1000" in nums and "95" in nums
    assert result["numeric_provenance"]["all_numbers_traced"] is True


# --------------------------------------------------------------------------------------
# Symmetric identifier blanking (#0030)
# --------------------------------------------------------------------------------------
# The identifier strip once required a run to START on a letter/underscore, so a sha256 that
# began with hex digits ("41dba61b...8004d") left its leading "41" behind as a bare number and
# false-failed a narration that faithfully quoted the hash. Blanking now removes any
# [A-Za-z0-9_] run carrying a letter/underscore WHOLE -- leading digits included -- while a
# pure-digit run still reaches the number gate.
#
# KNOWN LIMITATION, stated plainly: after this change a FABRICATED identifier-shaped token (a
# hallucinated hash, a made-up column name with digits) no longer trips the provenance gate
# via its leading digits. That detection was ACCIDENTAL, never a guarantee -- the number gate
# exists to catch bare fabricated NUMBERS, not fabricated identifiers, and hash fidelity is out
# of scope for it. The tests below pin the intended behavior, not that lost side effect.

# The demo fixture (permea_ui.fixtures, _SEED = 20260721) emits this exact digit-first sha256;
# see tests/test_ui_drylab.py for the end-to-end regression over that fixture.
_DIGIT_FIRST_SHA256 = "41dba61bf87bd33674c49388075707f5a0dade7060a2da6298bd7f91b1b8004d"


def test_digit_first_identifier_leaves_no_bare_number():
    """A digit-first hash is blanked whole; trailing-digit ids already were -- now symmetric."""
    assert guardrails.numbers_in_narrative(f"데이터 해시는 {_DIGIT_FIRST_SHA256} 입니다.") == []
    # "42abc" (leading digits) now matches "abc42" (trailing): both blank whole, neither leaks.
    assert guardrails.numbers_in_narrative("식별자 42abc 와 abc42 를 봅니다.") == []


def test_faithful_hash_quote_passes_provenance(tmp_path):
    """(a) Quoting the report's data_sha256 no longer trips the number-provenance gate."""
    _, report = _report_file(tmp_path)
    report["context"]["data_sha256"] = _DIGIT_FIRST_SHA256  # digit-first, as the demo fixture emits
    text = f"이 해설은 데이터 해시 {_DIGIT_FIRST_SHA256} 를 참조합니다. 조건 B 가 헤드라인입니다."
    assert guardrails.render_checked(text, report) == text


def test_fabricated_standalone_number_still_untraced(tmp_path):
    """(b) LOAD-BEARING: a bare fabricated number absent from the report is STILL rejected.

    Proves symmetric blanking did not weaken the gate: only alnum runs CARRYING a letter are
    swallowed; a standalone "0.87" carries none, reaches the gate, and fails as NUMERIC_UNTRACED.
    """
    _, report = _report_file(tmp_path)
    violations = guardrails.collect_violations(FAITHFUL + " 정확도는 0.87 입니다.", report)
    assert [v.kind for v in violations] == [NUMERIC_UNTRACED]
    assert "0.87" in violations[0].message


def test_korean_adjacent_digits_still_reach_the_gate(tmp_path):
    """(c) Hangul is outside [A-Za-z0-9_], so "180개" still yields "180" and is provenance-checked."""
    assert guardrails.numbers_in_narrative("표본은 180개입니다.") == ["180"]
    _, report = _report_file(tmp_path)  # this report has n=2959, not 180
    with pytest.raises(GuardrailViolation, match="180"):
        guardrails.render_checked("표본은 180개입니다.", report)


def test_pure_digit_and_decimal_tokenization_unchanged():
    """(d) Pure-digit, decimal, and thousands-grouped forms tokenize exactly as before."""
    assert guardrails.numbers_in_narrative("총 1000 개, 95%, 임계값 0.02, 델타 -0.4344") == [
        "1000", "95", "0.02", "-0.4344",
    ]
    assert guardrails.numbers_in_narrative("표본은 2,959개") == ["2959"]
    # A warning code still loses its digits (W101 -> gone); the standalone 0.87 survives.
    assert guardrails.numbers_in_narrative("PERMEA-W101 이 발화, 정확도 0.87") == ["0.87"]


# --------------------------------------------------------------------------------------
# A-priori sign convention (#0034)
# --------------------------------------------------------------------------------------
# SYSTEM_PROMPT carries a standing instruction to always write signed fields (deltas, CI
# bounds) WITH their sign -- stated ONCE, before any generation, as defence in depth mirroring
# the guardrail's sign-aware token matching. It is NOT a retry after a violation (the verifier
# must never become a training signal). The instruction itself must carry no numeric literal:
# commit b24737a exists because literals injected into prompt-visible text came back in
# narrations and tripped the number gate, so the added sentence must tokenize to [] under the
# SAME extractor the gate uses at runtime.
_SIGN_CONVENTION = (
    "부호가 있는 숫자 필드(델타, 신뢰구간 경계 등)는 항상 그 부호를 "
    "붙여 그대로 쓰십시오. 방향을 동사로 나타내더라도 부호를 뗀 크기(절댓값)만 적는 "
    "것은 허용되지 않습니다. 음수 필드는 반드시 음의 부호와 함께 기재하십시오."
)


def test_sign_convention_present_in_system_prompt():
    """The convention is a-priori: it lives in the standing prompt, sent before generation.

    Matched whitespace-insensitively because SYSTEM_PROMPT hard-wraps its rules across
    indented lines, so the sentence spans several ``\\n   `` breaks in the source.
    """
    collapse = lambda s: re.sub(r"\s+", " ", s).strip()
    assert collapse(_SIGN_CONVENTION) in collapse(prompt.SYSTEM_PROMPT)


def test_sign_convention_carries_no_numeric_literal():
    """A faithful copy of the instruction must not itself fail the provenance gate (b24737a)."""
    assert guardrails._standalone_number_tokens(_SIGN_CONVENTION) == []


def test_extract_is_available_alongside_narrate():
    """Both task layers share one Provider and one verification discipline (#0023)."""
    import inspect

    params = inspect.signature(extract).parameters
    assert "dataset_card" in params and "methods_text" in params
    assert params["provider"].default is None  # same injection point narrate() uses
