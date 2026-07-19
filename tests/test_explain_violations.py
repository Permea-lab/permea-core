"""Tests for structured violation attribution across both verification layers.

The refactor that introduced ``Violation`` was behavior-preserving: the exception messages
``write_checked`` and ``render_checked`` raise are byte-identical to what they raised when
the collectors returned ``list[str]``. The first test in this file pins that literally, so a
future edit to a message is a deliberate act rather than a silent break of anything reading
those strings.

The rest pins the two distinctions the type exists to preserve: mirror drift is not an
invalid value, and a forbidden phrase has no field to blame.
"""
from __future__ import annotations

import copy

import pytest

from permea_explain import extract as extract_mod
from permea_explain import guardrails
from permea_explain.extract import collect_violations, write_checked
from permea_explain.violations import (
    ENUM_INVALID,
    ENUM_MIRROR_DRIFT,
    FORBIDDEN_PHRASE,
    KINDS,
    LEAF_MISSING,
    LEAF_MISSING_VALUE,
    NUMERIC_UNTRACED,
    OFFSET_INVALID,
    SCHEMA_INVALID,
    SPAN_EMPTY,
    SPAN_MISSING_ON_NONNULL,
    SPAN_NOT_FOUND,
    SPAN_OFFSET_MISMATCH,
    UNFIRED_CODE,
    Violation,
    join_messages,
)

from test_explain_extract import METHODS_TEXT, _doc

CONSTRUCTION = "/extracted/negative_class/construction"
DEFINITION = "/extracted/positive_class/definition"
SOURCE_POOL = "/extracted/negative_class/source_pool"


def _grounding_only_doc():
    """Fails Gate 2 and Gate 3 only. Both are states the SCHEMA considers valid -- a span
    that is absent from the source and a forbidden phrase in a well-formed string are not
    schema violations -- so Gate 4 stays silent and the message is the pre-Gate-4 text."""
    d = _doc()
    d["extracted"]["positive_class"]["definition"]["evidence_span"] = "absent span"
    d["extracted"]["negative_class"]["source_pool"]["value"] = "we recommend random fragments"
    return d


def _multi_violation_doc():
    """Fails all four gates. The enum fault is ALSO a schema fault, so Gate 4 co-reports."""
    d = _grounding_only_doc()
    d["extracted"]["negative_class"]["construction"]["value"] = "Presumed_Random"
    return d


# ======================================================================================
# behaviour preservation -- the original three gates' text is byte-identical
# ======================================================================================
# Captured from the pre-refactor implementation and pasted verbatim. Not regenerated from
# the code under test: a regenerated expectation would agree with any change.
#
# Gate 4 (#0020) is additive and does not touch this text. It DOES add a fourth violation
# whenever a fault is both a gate fault and a schema fault -- see the enum case below -- so
# this pin deliberately uses a document whose faults are grounding faults only.
PRE_REFACTOR_MESSAGE = (
    "extraction failed 2 postcondition check(s): "
    "/extracted/positive_class/definition: evidence_span does not appear verbatim in "
    "methods_text: 'absent span'; "
    "forbidden phrase present: 'we recommend'"
)


def test_raised_message_is_byte_identical_to_pre_refactor():
    with pytest.raises(extract_mod.ExtractionViolation) as exc:
        write_checked(_grounding_only_doc(), METHODS_TEXT)
    head = str(exc.value).split("\n--- offending document ---")[0]
    assert head == PRE_REFACTOR_MESSAGE


def test_gate_order_in_the_message_is_enum_span_phrase_schema():
    v = collect_violations(_multi_violation_doc(), METHODS_TEXT)
    assert [x.kind for x in v] == [
        ENUM_INVALID,
        SPAN_NOT_FOUND,
        FORBIDDEN_PHRASE,
        SCHEMA_INVALID,
    ]


def test_grounding_faults_alone_do_not_wake_the_schema_gate():
    v = collect_violations(_grounding_only_doc(), METHODS_TEXT)
    assert [x.kind for x in v] == [SPAN_NOT_FOUND, FORBIDDEN_PHRASE]


def test_joined_messages_are_what_gets_raised():
    """The structured list and the raised string cannot drift: one is rendered from the other."""
    doc = _multi_violation_doc()
    with pytest.raises(extract_mod.ExtractionViolation) as exc:
        write_checked(doc, METHODS_TEXT)
    assert join_messages(collect_violations(doc, METHODS_TEXT)) in str(exc.value)


def test_narrate_message_is_unchanged_and_rendered_from_violations(tmp_path):
    from test_explain_narrate import _report_file

    _, report = _report_file(tmp_path)
    text = "PERMEA-W301 이 발화되었고 정확도는 0.87 입니다."
    with pytest.raises(guardrails.GuardrailViolation) as exc:
        guardrails.render_checked(text, report)
    v = guardrails.collect_violations(text, report)
    assert str(exc.value) == (
        f"narration failed {len(v)} guardrail check(s): "
        + join_messages(v)
        + f"\n--- offending output ---\n{text}"
    )


# ======================================================================================
# attribution -- every kind carries the right pointer
# ======================================================================================
def test_collect_violations_does_not_raise_on_a_clean_document():
    assert collect_violations(_doc(), METHODS_TEXT) == []


def test_every_emitted_kind_is_in_the_closed_set():
    seen = set()
    for doc in (_multi_violation_doc(), _shape_broken_doc()):
        seen |= {v.kind for v in collect_violations(doc, METHODS_TEXT)}
    assert seen  # non-empty, or this asserts nothing
    assert seen <= KINDS


def _shape_broken_doc():
    d = _doc()
    del d["extracted"]["class_balance"]  # LEAF_MISSING
    d["extracted"]["label_noise_estimate"].pop("value")  # LEAF_MISSING_VALUE
    d["extracted"]["positive_class"]["definition"]["evidence_span"] = "   "  # SPAN_EMPTY
    d["extracted"]["negative_class"]["validated_fraction"]["offset"] = "3"  # OFFSET_INVALID
    d["extracted"]["positive_class"]["assays"]["evidence_span"] = None  # SPAN_MISSING_ON_NONNULL
    return d


@pytest.mark.parametrize(
    "kind,pointer",
    [
        (LEAF_MISSING, "/extracted/class_balance"),
        (LEAF_MISSING_VALUE, "/extracted/label_noise_estimate"),
        (SPAN_EMPTY, DEFINITION),
        (OFFSET_INVALID, "/extracted/negative_class/validated_fraction"),
        (SPAN_MISSING_ON_NONNULL, "/extracted/positive_class/assays"),
    ],
)
def test_shape_violations_carry_their_field_pointer(kind, pointer):
    v = collect_violations(_shape_broken_doc(), METHODS_TEXT)
    assert (pointer, kind) in [(x.pointer, x.kind) for x in v]


def test_span_offset_mismatch_carries_its_pointer():
    d = _doc()
    d["extracted"]["label_noise_estimate"]["offset"] = 3
    v = collect_violations(d, METHODS_TEXT)
    assert [(x.pointer, x.kind) for x in v] == [
        ("/extracted/label_noise_estimate", SPAN_OFFSET_MISMATCH)
    ]


def test_array_element_violation_points_at_the_field_not_the_element():
    """The field is the unit a demoter can act on; the index stays in the message."""
    d = _doc()
    d["extracted"]["negative_class"]["known_confounds"]["value"] = ["not_a_confound"]
    v = [x for x in collect_violations(d, METHODS_TEXT) if x.kind == ENUM_INVALID]
    assert len(v) == 1
    assert v[0].pointer == "/extracted/negative_class/known_confounds"  # no "/0" suffix
    assert "/known_confounds/0:" in v[0].message  # index preserved in the text


# ======================================================================================
# OQ#2 -- mirror drift is its own kind, never enum_invalid
# ======================================================================================
def test_mirror_drift_is_its_own_kind(monkeypatch):
    """A demoter keying on pointer alone would bury a schema divergence as an abstention."""
    real = extract_mod._load_schema

    def fake(name):
        s = copy.deepcopy(real(name))
        if name == "extract.schema.json":
            enum = s["$defs"]["prov_construction"]["properties"]["value"]["enum"]
            enum.remove("decoy_generated")  # mirror now omits a permitted value
        return s

    monkeypatch.setattr(extract_mod, "_load_schema", fake)

    v = collect_violations(_doc(), METHODS_TEXT)
    drift = [x for x in v if x.kind == ENUM_MIRROR_DRIFT]
    assert len(drift) == 1
    assert drift[0].pointer == CONSTRUCTION
    assert "enum mirror drift" in drift[0].message
    # The document's own value is fine -- no value-level violation was raised.
    assert not [x for x in v if x.kind == ENUM_INVALID]


def test_mirror_drift_and_enum_invalid_are_distinguishable_on_the_same_field(monkeypatch):
    """Same pointer, two different faults. Only the kind tells them apart."""
    real = extract_mod._load_schema

    def fake(name):
        s = copy.deepcopy(real(name))
        if name == "extract.schema.json":
            s["$defs"]["prov_construction"]["properties"]["value"]["enum"].remove(
                "decoy_generated"
            )
        return s

    monkeypatch.setattr(extract_mod, "_load_schema", fake)
    d = _doc()
    d["extracted"]["negative_class"]["construction"]["value"] = "Presumed_Random"

    kinds = {x.kind for x in collect_violations(d, METHODS_TEXT) if x.pointer == CONSTRUCTION}
    # SCHEMA_INVALID rides along because a bad enum is also a schema fault; the point is that
    # drift is still separable from the value fault, which pointer alone cannot do.
    assert kinds == {ENUM_MIRROR_DRIFT, ENUM_INVALID, SCHEMA_INVALID}


# ======================================================================================
# OQ#3 -- a forbidden phrase has no field to blame, and says so
# ======================================================================================
def test_forbidden_phrase_has_no_pointer():
    d = _doc()
    d["extracted"]["negative_class"]["source_pool"]["value"] = "we recommend random fragments"
    v = [x for x in collect_violations(d, METHODS_TEXT) if x.kind == FORBIDDEN_PHRASE]
    assert len(v) == 1
    assert v[0].pointer is None  # not SOURCE_POOL -- the scan genuinely cannot attribute it


def test_narrate_violations_are_all_unattributed():
    """A narration is prose; there is no field to point at, and none is invented."""
    report = {"fired": [], "context": {"n": 7}}
    v = guardrails.collect_violations("PERMEA-W301 이 발화, 정확도 0.87, 이는 조작이다.", report)
    assert {x.kind for x in v} == {NUMERIC_UNTRACED, FORBIDDEN_PHRASE, UNFIRED_CODE}
    assert all(x.pointer is None for x in v)
    assert {x.kind for x in v} <= KINDS


# ======================================================================================
# the type itself
# ======================================================================================
def test_violation_is_a_plain_named_tuple():
    v = Violation("/a/b", ENUM_INVALID, "msg")
    assert (v.pointer, v.kind, v.message) == ("/a/b", ENUM_INVALID, "msg")
    assert tuple(v) == ("/a/b", ENUM_INVALID, "msg")


def test_stale_source_still_preempts_collection():
    """The precondition raises; it is not reported as a recoverable violation."""
    with pytest.raises(extract_mod.StaleSourceError):
        collect_violations(_doc(), METHODS_TEXT + " tampered")
