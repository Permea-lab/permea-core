"""Tests for Gate 4 -- the EXTRACT postcondition's schema-validity gate.

Gates 1-3 answer "is this reading grounded?". None of them answered "is this document the
shape it claims to be", so before this gate a grounded-but-impossible value collected the
verified:true stamp. Every case marked OQ#7 below was verified PASSING beforehand.

The gate validates the STAMPED document, so what is checked is exactly what is returned:
a document that comes out of write_checked is always valid against extract.schema.json.
"""
from __future__ import annotations

import copy
import sys

import pytest

from permea_explain import extract as extract_mod
from permea_explain.extract import ExtractionViolation, collect_violations, write_checked
from permea_explain.violations import SCHEMA_INVALID

from test_explain_extract import METHODS_TEXT, _doc, _leaf

E = lambda d: d["extracted"]  # noqa: E731


def _violates(mutate):
    """Apply a mutation and return only the schema-gate violations."""
    d = _doc()
    mutate(d)
    return d, [v for v in collect_violations(d, METHODS_TEXT) if v.kind == SCHEMA_INVALID]


# ======================================================================================
# OQ#7 -- the cases verified passing before this gate existed
# ======================================================================================
def test_out_of_range_validated_fraction_now_fails():
    """The headline OQ#7 case: 1.7 is grounded by a real span but is not a fraction."""
    d, v = _violates(lambda d: E(d)["negative_class"]["validated_fraction"].update({"value": 1.7}))
    assert v and v[0].pointer == "/extracted/negative_class/validated_fraction"
    with pytest.raises(ExtractionViolation, match="schema violation"):
        write_checked(d, METHODS_TEXT)


def test_short_definition_now_fails():
    d, v = _violates(lambda d: E(d)["positive_class"]["definition"].update({"value": "short"}))
    assert v and v[0].pointer == "/extracted/positive_class/definition"
    with pytest.raises(ExtractionViolation):
        write_checked(d, METHODS_TEXT)


@pytest.mark.parametrize("positive", [-1, 2.5, "269"])
def test_bad_class_balance_now_fails(positive):
    d, v = _violates(lambda d: E(d)["class_balance"]["value"].update({"positive": positive}))
    assert v and v[0].pointer == "/extracted/class_balance"
    with pytest.raises(ExtractionViolation):
        write_checked(d, METHODS_TEXT)


@pytest.mark.parametrize(
    "mutate,pointer",
    [
        (lambda d: E(d)["label_noise_estimate"].update({"value": -0.5}),
         "/extracted/label_noise_estimate"),
        (lambda d: E(d)["positive_class"]["assays"].update({"value": [123]}),
         "/extracted/positive_class/assays"),
        (lambda d: E(d)["negative_class"]["source_pool"].update({"value": 42}),
         "/extracted/negative_class/source_pool"),
        (lambda d: E(d)["task_type"].update({"confidence": 5.0}),
         "/extracted/task_type"),
    ],
)
def test_declared_types_and_ranges_are_enforced(mutate, pointer):
    d, v = _violates(mutate)
    assert v, f"expected a schema violation at {pointer}"
    assert v[0].pointer == pointer


def test_abstention_carrying_a_fabricated_span_now_fails():
    """abstention_coherence was declared in the schema and enforced nowhere.

    A null value used to be able to carry an invented span and offset -- fabricated
    provenance attached to "not stated", which is worse than an out-of-range number.
    """
    d, v = _violates(
        lambda d: E(d)["positive_class"]["provenance_ref"].update(
            {"evidence_span": "totally invented", "offset": 99999}
        )
    )
    assert v and v[0].pointer == "/extracted/positive_class/provenance_ref"
    with pytest.raises(ExtractionViolation):
        write_checked(d, METHODS_TEXT)


# ======================================================================================
# the non-authority posture -- const:false was unenforced before this gate
# ======================================================================================
@pytest.mark.parametrize(
    "key,value", [("authoritative", True), ("status", "final"), ("schema", "permea.extract/9.9")]
)
def test_a_document_cannot_claim_authority(key, value):
    """The most serious pre-gate hole: an extract asserting authority got the verified stamp."""
    d, v = _violates(lambda d: d.update({key: value}))
    assert v, f"{key}={value!r} must not validate"
    with pytest.raises(ExtractionViolation):
        write_checked(d, METHODS_TEXT)


def test_envelope_constraints_are_enforced():
    for mutate in (
        lambda d: d.update({"disclaimer": "too short"}),          # minLength 40
        lambda d: d.update({"injected": "x"}),                    # additionalProperties false
        lambda d: d["dataset_card"].update({"ref": ""}),          # minLength 1
        lambda d: d.pop("model"),                                 # required
    ):
        _, v = _violates(mutate)
        assert v


# ======================================================================================
# what must still pass
# ======================================================================================
def test_a_valid_document_still_passes_and_is_stamped():
    stamped = write_checked(_doc(), METHODS_TEXT)
    assert stamped["extraction_provenance"]["verified"] is True
    assert stamped["extraction_provenance"]["spans_checked"] == 10


def test_an_abstention_heavy_document_still_passes():
    """Every field honestly null. The schema permits the null branch everywhere, and a gate
    that punished abstention would manufacture the fabrication it exists to catch."""
    d = _doc()
    E(d)["task_type"] = _leaf(None)
    for f in ("definition", "evidence_type", "assays", "provenance_ref"):
        E(d)["positive_class"][f] = _leaf(None)
    for f in ("construction", "validated_fraction", "source_pool", "matched_on",
              "known_confounds"):
        E(d)["negative_class"][f] = _leaf(None)
    E(d)["class_balance"] = _leaf(None)
    E(d)["label_noise_estimate"] = _leaf(None)

    stamped = write_checked(d, METHODS_TEXT)
    assert stamped["extraction_provenance"]["spans_checked"] == 0
    assert collect_violations(d, METHODS_TEXT) == []


def test_empty_arrays_are_still_distinct_from_null_and_pass():
    d = _doc()
    E(d)["negative_class"]["known_confounds"] = _leaf([], "drawn at random from UniProt")
    assert collect_violations(d, METHODS_TEXT) == []


# ======================================================================================
# the invariant: what is validated is what is returned
# ======================================================================================
def test_the_returned_document_is_schema_valid():
    """The whole point of Gate 4: passing implies schema-valid, for the STAMPED artifact."""
    from jsonschema import Draft202012Validator

    stamped = write_checked(_doc(), METHODS_TEXT)
    schema = extract_mod._load_schema("extract.schema.json")
    Draft202012Validator(schema).validate(stamped)  # raises if not


def test_gate4_validates_the_stamped_doc_not_the_raw_candidate():
    """OQ#5: the raw candidate lacks extraction_provenance and is schema-invalid by
    construction, so validating IT would report a failure that is an artifact of the
    pipeline. The candidate below is valid only once stamped."""
    from jsonschema import Draft202012Validator

    schema = extract_mod._load_schema("extract.schema.json")
    candidate = _doc()
    assert "extraction_provenance" not in candidate
    assert not Draft202012Validator(schema).is_valid(candidate)  # raw: invalid
    assert collect_violations(candidate, METHODS_TEXT) == []      # stamped: no violations


def test_a_forged_provenance_block_is_replaced_not_trusted():
    """A candidate arriving with its own extraction_provenance cannot smuggle it through:
    the stamp is rewritten from what the gates actually measured."""
    d = _doc()
    d["extraction_provenance"] = {
        "verified": True,
        "all_spans_verbatim": True,
        "all_span_enums_valid": True,
        "spans_checked": 9999,
        "verifier_version": "forged",
    }
    stamped = write_checked(d, METHODS_TEXT)
    assert stamped["extraction_provenance"]["spans_checked"] == 10
    assert stamped["extraction_provenance"]["verifier_version"] == extract_mod.VERIFIER_VERSION


def test_input_document_is_never_mutated():
    d = _doc()
    before = copy.deepcopy(d)
    write_checked(d, METHODS_TEXT)
    assert d == before


# ======================================================================================
# optional dependency
# ======================================================================================
def test_missing_jsonschema_raises_the_install_hint(monkeypatch):
    extract_mod._validator.cache_clear()
    monkeypatch.setitem(sys.modules, "jsonschema", None)  # makes `import jsonschema` raise
    try:
        with pytest.raises(RuntimeError, match=r"permea-core\[explain\]"):
            collect_violations(_doc(), METHODS_TEXT)
    finally:
        extract_mod._validator.cache_clear()
