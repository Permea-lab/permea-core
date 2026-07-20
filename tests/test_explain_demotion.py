"""Tests for the permea.extract/1.1 demotion record (OQ#4).

Without this record an artifact cannot tell an extractor that abstained nine times from one
that guessed nine times and was demoted nine times -- the documents are identical and the
instruments are opposite. The record makes the difference visible.

The rule the whole design turns on, and the one most of this file guards: everything in a
document stamped verified:true is grounded or null. The record therefore stores a COMPUTED
classification and digests, never the reading the gate rejected.
"""
from __future__ import annotations

import json

import pytest

from permea_explain import extract as extract_mod
from permea_explain.extract import ExtractionViolation, collect_violations, write_checked
from permea_explain.violations import (
    DEMOTABLE_KINDS,
    ENUM_INVALID,
    ENUM_MIRROR_DRIFT,
    FORBIDDEN_PHRASE,
    KINDS,
    LEAF_MISSING,
    LEAF_MISSING_VALUE,
    SCHEMA_INVALID,
    SPAN_NOT_FOUND,
    Demotion,
)

from test_explain_extract import METHODS_TEXT, _doc, _leaf

CONSTRUCTION = "/extracted/negative_class/construction"
DEFINITION = "/extracted/positive_class/definition"
FRACTION = "/extracted/negative_class/validated_fraction"


def _leaf_parent(doc, pointer):
    parent, keys = doc["extracted"], pointer[len("/extracted/") :].split("/")
    for k in keys[:-1]:
        parent = parent[k]
    return parent, keys[-1]


def _demote(doc, pointer, mutate):
    """Break a leaf, capture what the recovery path would discard, reset it to abstention."""
    parent, key = _leaf_parent(doc, pointer)
    mutate(parent[key])
    leaf = parent[key]
    demotion = Demotion(
        pointer,
        tuple(v for v in collect_violations(doc, METHODS_TEXT) if v.pointer == pointer),
        leaf["value"],
        leaf["evidence_span"],
        leaf["confidence"],
    )
    # The canonical demoted abstention: confidence is reset too. A 0.9 left attached to a null
    # would read as "90% sure it is not stated", which is not what the model claimed.
    parent[key] = _leaf(None, confidence=None)
    return demotion


def _stamp_with(doc, *demotions):
    return write_checked(doc, METHODS_TEXT, demotions=list(demotions))


def _record(doc, pointer, mutate):
    d = doc
    out = _stamp_with(d, _demote(d, pointer, mutate))
    return out, out["extraction_provenance"]["demoted"][0]


# ======================================================================================
# the receipt exists, and [] is a positive assertion
# ======================================================================================
def test_a_clean_extract_asserts_nothing_was_demoted():
    stamped = write_checked(_doc(), METHODS_TEXT)
    assert stamped["extraction_provenance"]["demoted"] == []


def test_demoted_is_required_by_gate_4():
    """An absent list would be ambiguous between 'nothing demoted' and 'not tracked'."""
    schema = extract_mod._load_schema("extract.schema.json")
    assert "demoted" in schema["properties"]["extraction_provenance"]["required"]

    from jsonschema import Draft202012Validator

    stamped = write_checked(_doc(), METHODS_TEXT)
    del stamped["extraction_provenance"]["demoted"]
    assert not Draft202012Validator(schema).is_valid(stamped)


def test_the_version_bumped_to_1_1():
    schema = extract_mod._load_schema("extract.schema.json")
    assert schema["properties"]["schema"]["const"] == "permea.extract/1.1"
    assert "/permea-eval/1.1/" in schema["$id"]


# ======================================================================================
# the three states are distinguishable
# ======================================================================================
def test_stated_abstained_and_demoted_are_all_distinguishable():
    d = _doc()
    d["extracted"]["negative_class"]["matched_on"] = _leaf(None)  # (b) honest abstention
    demotion = _demote(d, CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    out = _stamp_with(d, demotion)

    demoted = {r["pointer"] for r in out["extraction_provenance"]["demoted"]}
    E = out["extracted"]

    # (a) stated and verified
    assert E["class_balance"]["value"] is not None
    assert "/extracted/class_balance" not in demoted
    # (b) honest abstention -- null, and NOT in the record
    assert E["negative_class"]["matched_on"]["value"] is None
    assert "/extracted/negative_class/matched_on" not in demoted
    # (c) demoted -- null, and IN the record
    assert E["negative_class"]["construction"]["value"] is None
    assert CONSTRUCTION in demoted


# ======================================================================================
# OQ#1 as decided: classification only, ZERO model content
# ======================================================================================
@pytest.mark.parametrize(
    "raw,expected",
    [
        ("Presumed_Random", "case_variant"),      # a REAL member, mis-cased
        ("PRESUMED_RANDOM", "case_variant"),
        (" presumed_random ", "whitespace_variant"),
        ("synthetic_decoys", "not_a_member"),     # invented
        (42, "not_a_member"),                     # the constraint IS the enum
        (["presumed_random"], "wrong_type"),      # container shape: array for a scalar field
    ],
)
def test_failure_class_is_computed_from_the_rejected_enum(raw, expected):
    _, record = _record(_doc(), CONSTRUCTION, lambda l: l.__setitem__("value", raw))
    assert record["failure_class"] == [expected]


def test_the_rejected_value_never_appears_in_the_artifact():
    """The decided position: no relaxation of 'no unverified model content in a verified doc'."""
    out, record = _record(_doc(), CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    assert "synthetic_decoys" not in json.dumps(out, ensure_ascii=False)
    assert "rejected_value" not in record  # no plaintext field exists at all
    assert record["rejected_value_sha256"]  # the digest does
    schema = extract_mod._load_schema("extract.schema.json")
    assert "rejected_value" not in schema["$defs"]["demotion_record"]["properties"]


def test_a_fabricated_span_is_hashed_never_reproduced():
    """The sharp case: a rejected span is text that LOOKS like a source quote and is not."""
    fabricated = "a quote that was never in the source"
    out, record = _record(_doc(), DEFINITION, lambda l: l.__setitem__("evidence_span", fabricated))
    assert fabricated not in json.dumps(out, ensure_ascii=False)
    assert record["failure_class"] == ["span_absent"]
    assert record["rejected_span_length"] == len(fabricated)
    assert len(record["rejected_span_sha256"]) == 64


def test_digests_are_stable_and_discriminating():
    _, a = _record(_doc(), CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    _, b = _record(_doc(), CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    _, c = _record(_doc(), CONSTRUCTION, lambda l: l.__setitem__("value", "other_invention"))
    assert a["rejected_value_sha256"] == b["rejected_value_sha256"]  # reproducible across runs
    assert a["rejected_value_sha256"] != c["rejected_value_sha256"]  # distinguishes readings


def test_rejected_confidence_is_kept():
    """A bare number, inert -- and the best signal for 'was the model confidently wrong?'."""
    _, record = _record(_doc(), CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    assert record["rejected_confidence"] == 0.9


@pytest.mark.parametrize(
    "pointer,mutate,expected",
    [
        (FRACTION, lambda l: l.__setitem__("value", 1.7), "out_of_range"),
        (DEFINITION, lambda l: l.__setitem__("value", "short"), "out_of_range"),
        ("/extracted/negative_class/source_pool", lambda l: l.__setitem__("value", 42), "wrong_type"),
    ],
)
def test_schema_faults_classify_past_the_anyof_wrapper(pointer, mutate, expected):
    """Every leaf permits abstention, so its value sits behind anyOf and the top-level message
    says only 'not valid under any of the given schemas'. The class comes from the sub-error."""
    _, record = _record(_doc(), pointer, mutate)
    assert record["failure_class"] == [expected]


def test_a_precise_enum_class_is_not_drowned_by_the_schema_echo():
    """Gates overlap: one bad enum arrives as ENUM_INVALID and SCHEMA_INVALID. The schema echo
    can only say not_a_member, which must not bury the finer case_variant reading."""
    _, record = _record(_doc(), CONSTRUCTION, lambda l: l.__setitem__("value", "Presumed_Random"))
    assert record["kinds"] == [ENUM_INVALID, SCHEMA_INVALID]  # both fired
    assert record["failure_class"] == ["case_variant"]  # but the specific one won


# ======================================================================================
# structural enforcement -- what Gate 4 makes unrecordable
# ======================================================================================
def test_non_demotable_kinds_are_structurally_unrecordable():
    """enum_mirror_drift, leaf_missing, leaf_missing_value and forbidden_phrase must never
    appear in a record: demoting them would bury a schema bug, or invent an answer the model
    never gave, or blank a field on no evidence."""
    schema = extract_mod._load_schema("extract.schema.json")
    allowed = set(schema["$defs"]["demotion_record"]["properties"]["kinds"]["items"]["enum"])
    assert allowed == DEMOTABLE_KINDS
    for forbidden in (ENUM_MIRROR_DRIFT, LEAF_MISSING, LEAF_MISSING_VALUE, FORBIDDEN_PHRASE):
        assert forbidden in KINDS and forbidden not in allowed


def test_recording_a_non_demotable_kind_raises_at_the_source():
    """Gate 4 would catch it too, but failing here names the caller that tried."""
    d = _doc()
    parent, key = _leaf_parent(d, CONSTRUCTION)
    parent[key] = _leaf(None, confidence=None)
    drift = Demotion(
        CONSTRUCTION,
        (extract_mod.Violation(CONSTRUCTION, ENUM_MIRROR_DRIFT, "drift"),),
        None, None, None,
    )
    with pytest.raises(ExtractionViolation, match="not demotable"):
        _stamp_with(d, drift)


def test_a_record_with_a_non_demotable_kind_fails_gate_4():
    from jsonschema import Draft202012Validator

    schema = extract_mod._load_schema("extract.schema.json")
    stamped = write_checked(_doc(), METHODS_TEXT)
    stamped["extraction_provenance"]["demoted"] = [
        {"pointer": CONSTRUCTION, "kinds": [ENUM_MIRROR_DRIFT], "failure_class": ["not_a_member"]}
    ]
    assert not Draft202012Validator(schema).is_valid(stamped)


def test_a_record_with_an_invented_pointer_fails_gate_4():
    from jsonschema import Draft202012Validator

    schema = extract_mod._load_schema("extract.schema.json")
    stamped = write_checked(_doc(), METHODS_TEXT)
    stamped["extraction_provenance"]["demoted"] = [
        {"pointer": "/extracted/not_a_field", "kinds": [ENUM_INVALID],
         "failure_class": ["not_a_member"]}
    ]
    assert not Draft202012Validator(schema).is_valid(stamped)


def test_every_recorded_pointer_is_one_of_the_twelve_leaves():
    schema = extract_mod._load_schema("extract.schema.json")
    assert schema["$defs"]["demotion_record"]["properties"]["pointer"]["enum"] == list(
        extract_mod._PROV_LEAVES
    )


# ======================================================================================
# the two runtime rules JSON Schema cannot express
# ======================================================================================
def test_two_records_for_one_pointer_raise():
    """A field that failed several ways carries ONE record with several kinds."""
    d = _doc()
    demotion = _demote(d, CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    with pytest.raises(ExtractionViolation, match="more than one record"):
        _stamp_with(d, demotion, demotion)


def test_a_demoted_pointer_whose_leaf_is_not_null_raises():
    """A demotion IS an abstention; the receipt and the reading must not disagree."""
    d = _doc()  # construction left intact, i.e. it still carries a value
    bogus = Demotion(CONSTRUCTION, (), None, None, None)
    with pytest.raises(ExtractionViolation, match="value is not null"):
        _stamp_with(d, bogus)


def test_both_runtime_rules_are_documented_in_the_schema():
    rules = extract_mod._load_schema("extract.schema.json")["$runtime_rules"]
    assert "demotion_one_record_per_pointer" in rules
    assert "demotion_pointer_resolves_to_abstention" in rules


# ======================================================================================
# unforgeability -- the reason the record lives in extraction_provenance
# ======================================================================================
def test_a_model_supplied_demoted_list_is_discarded():
    """A model that could write 'I was not demoted' could lie about it."""
    d = _doc()
    demotion = _demote(d, CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    d["extraction_provenance"] = {  # forged: claims a clean run
        "verified": True,
        "all_spans_verbatim": True,
        "all_span_enums_valid": True,
        "spans_checked": 9999,
        "verifier_version": "forged",
        "demoted": [],
    }
    out = _stamp_with(d, demotion)
    assert len(out["extraction_provenance"]["demoted"]) == 1
    assert out["extraction_provenance"]["verifier_version"] == extract_mod.VERIFIER_VERSION
    assert out["extraction_provenance"]["spans_checked"] != 9999


def test_a_forged_extra_record_cannot_survive():
    d = _doc()
    d["extraction_provenance"] = {"demoted": [{"pointer": DEFINITION, "kinds": [ENUM_INVALID],
                                               "failure_class": ["not_a_member"]}]}
    assert write_checked(d, METHODS_TEXT)["extraction_provenance"]["demoted"] == []


def test_input_document_is_not_mutated_by_demotion_recording():
    d = _doc()
    demotion = _demote(d, CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    before = json.dumps(d, sort_keys=True)
    _stamp_with(d, demotion)
    assert json.dumps(d, sort_keys=True) == before


# ======================================================================================
# a demoted field is still an ordinary abstention
# ======================================================================================
def test_a_demoted_leaf_is_the_canonical_abstention():
    """abstention_coherence is untouched: there is exactly one notion of 'abstained', and the
    record annotates why one arose rather than creating a second kind."""
    d = _doc()
    demotion = _demote(d, CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    out = _stamp_with(d, demotion)
    leaf = out["extracted"]["negative_class"]["construction"]
    assert leaf == {"value": None, "evidence_span": None, "offset": None, "confidence": None}


def test_a_demoted_document_still_passes_all_four_gates():
    d = _doc()
    demotion = _demote(d, CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    assert collect_violations(d, METHODS_TEXT, demotions=[demotion]) == []
    out = _stamp_with(d, demotion)
    assert out["extraction_provenance"]["verified"] is True
    assert out["extraction_provenance"]["spans_checked"] == 9  # one fewer grounded leaf


def test_the_stamped_document_validates_under_1_1():
    from jsonschema import Draft202012Validator

    d = _doc()
    demotion = _demote(d, CONSTRUCTION, lambda l: l.__setitem__("value", "synthetic_decoys"))
    out = _stamp_with(d, demotion)
    Draft202012Validator(extract_mod._load_schema("extract.schema.json")).validate(out)
