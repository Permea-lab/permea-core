"""Tests for extract() candidate generation -- generate, verify, DEMOTE.

Strictly offline. The provider is a stub that returns a canned response; no test here reaches
a live deployment, and a test that did would fail for reasons having nothing to do with this
repo.

The contract under test has exactly two outcomes: a document that has ALREADY passed
write_checked, or an exception. Most of this file is about which failures are demoted (the
model's reading could not be grounded, so the honest answer is "unknown") and which are
raised (abstaining would conceal something).
"""
from __future__ import annotations

import json

import pytest

from permea_explain import extract as extract_mod
from permea_explain.extract import ExtractionFormatError, ExtractionViolation, extract
from permea_explain.providers.base import Provider, ProviderResponse

from test_explain_extract import METHODS_TEXT

CARD = {"ref": "dataset_cards/bbb_peptides.json"}
CONSTRUCTION = "/extracted/negative_class/construction"
DEFINITION = "/extracted/positive_class/definition"


class StubProvider(Provider):
    """Returns canned responses in order; records what it was asked. No network."""

    name = "exaone"

    def __init__(self, *responses):
        self._responses = list(responses)
        self.calls = 0
        self.system = self.user = None

    @property
    def model_id(self) -> str:
        return "fake-exaone-model"

    def complete(self, system, user, *, max_tokens, temperature=None, stop=None):
        self.system, self.user, self.temperature = system, user, temperature
        self.calls += 1
        text = self._responses[min(self.calls - 1, len(self._responses) - 1)]
        return ProviderResponse(text=text, provider="exaone", model_id="fake-exaone-model")


def _leaf(value=None, span=None, confidence=0.9):
    return {"value": value, "evidence_span": span, "confidence": confidence}


def _subtree(**overrides):
    """A fully grounded reading of METHODS_TEXT. Override 'a.b' or 'a' to break one leaf."""
    tree = {
        "task_type": _leaf("binary_classification", "binary classification benchmark"),
        "positive_class": {
            "definition": _leaf(
                "experimentally observed blood-brain barrier penetration",
                "experimentally observed blood-brain barrier penetration",
            ),
            "evidence_type": _leaf("experimental_direct", "measured by in situ perfusion"),
            "assays": _leaf(["in_situ_perfusion"], "in situ perfusion"),
            "provenance_ref": _leaf(),
        },
        "negative_class": {
            "construction": _leaf(
                "presumed_random", "Negative examples were drawn at random from UniProt"
            ),
            "validated_fraction": _leaf(0.0, "validated fraction of 0.0"),
            "source_pool": _leaf(
                "random protein fragments, non-BBB-related",
                "random protein fragments, non-BBB-related",
            ),
            "matched_on": _leaf(),
            "known_confounds": _leaf(["source_pool_shift"], "drawn at random from UniProt"),
        },
        "class_balance": _leaf(
            {"positive": 269, "negative": 2690}, "269 positives and 2690 negatives"
        ),
        "label_noise_estimate": _leaf(0.05, "label noise rate of 0.05"),
    }
    for key, value in overrides.items():
        if "." in key:
            group, leaf = key.split(".")
            tree[group][leaf] = value
        else:
            tree[key] = value
    return tree


def _response(**overrides):
    return json.dumps(_subtree(**overrides), ensure_ascii=False)


def _run(response, **kwargs):
    provider = StubProvider(response)
    return extract(CARD, METHODS_TEXT, provider=provider, **kwargs), provider


def _demoted(doc):
    return {r["pointer"]: r for r in doc["extraction_provenance"]["demoted"]}


# ======================================================================================
# the happy path, and the fact that abstention is also a happy path
# ======================================================================================
def test_a_fully_grounded_reading_is_stamped_with_nothing_demoted():
    doc, _ = _run(_response())
    assert doc["extraction_provenance"]["verified"] is True
    assert doc["extraction_provenance"]["demoted"] == []
    assert doc["extraction_provenance"]["spans_checked"] == 10
    assert doc["extracted"]["negative_class"]["construction"]["value"] == "presumed_random"


def test_the_returned_document_has_already_passed_the_postcondition():
    """The contract: no unverified return value, ever."""
    from jsonschema import Draft202012Validator

    doc, _ = _run(_response())
    Draft202012Validator(extract_mod._load_schema("extract.schema.json")).validate(doc)
    assert extract_mod.collect_violations(doc, METHODS_TEXT) == []


def test_an_all_abstention_reading_is_a_SUCCESS():
    """Nine nulls is a correct report that the text states little -- not a degraded answer."""
    empty = {
        "task_type": _leaf(),
        "positive_class": {k: _leaf() for k in
                           ("definition", "evidence_type", "assays", "provenance_ref")},
        "negative_class": {k: _leaf() for k in
                           ("construction", "validated_fraction", "source_pool",
                            "matched_on", "known_confounds")},
        "class_balance": _leaf(),
        "label_noise_estimate": _leaf(),
    }
    doc, _ = _run(json.dumps(empty))
    assert doc["extraction_provenance"]["verified"] is True
    assert doc["extraction_provenance"]["spans_checked"] == 0
    assert doc["extraction_provenance"]["demoted"] == []  # abstained, NOT demoted
    assert doc["extracted"]["task_type"]["value"] is None


def test_an_abstention_never_carries_the_models_span():
    """A null value fabricates no provenance, whatever the model attached to it."""
    doc, _ = _run(_response(task_type=_leaf(None, "a span attached to a null")))
    assert doc["extracted"]["task_type"] == {
        "value": None, "evidence_span": None, "offset": None, "confidence": 0.9,
    }
    assert "a span attached to a null" not in json.dumps(doc, ensure_ascii=False)


def test_empty_list_is_preserved_as_distinct_from_null():
    doc, _ = _run(_response(**{"negative_class.matched_on":
                               _leaf([], "drawn at random from UniProt")}))
    assert doc["extracted"]["negative_class"]["matched_on"]["value"] == []


# ======================================================================================
# demotion -- the honest recovery
# ======================================================================================
def test_an_ungroundable_span_is_demoted_not_accepted():
    fabricated = "a sentence that appears nowhere in the methods text"
    doc, _ = _run(_response(**{"negative_class.construction":
                               _leaf("presumed_random", fabricated)}))

    leaf = doc["extracted"]["negative_class"]["construction"]
    assert leaf == {"value": None, "evidence_span": None, "offset": None, "confidence": None}
    record = _demoted(doc)[CONSTRUCTION]
    assert record["kinds"] == ["span_not_found"]
    assert record["failure_class"] == ["span_absent"]
    assert fabricated not in json.dumps(doc, ensure_ascii=False)
    assert doc["extraction_provenance"]["verified"] is True  # still a valid artifact


def test_a_mis_cased_enum_is_demoted_with_case_variant_and_never_quoted():
    doc, _ = _run(_response(**{"negative_class.construction":
                               _leaf("Presumed_Random",
                                     "Negative examples were drawn at random from UniProt")}))
    record = _demoted(doc)[CONSTRUCTION]
    assert record["failure_class"] == ["case_variant"]
    assert "Presumed_Random" not in json.dumps(doc, ensure_ascii=False)
    assert len(record["rejected_value_sha256"]) == 64
    assert record["rejected_confidence"] == 0.9


def test_an_invented_enum_is_demoted_as_not_a_member():
    doc, _ = _run(_response(**{"negative_class.construction":
                               _leaf("synthetic_decoys",
                                     "Negative examples were drawn at random from UniProt")}))
    assert _demoted(doc)[CONSTRUCTION]["failure_class"] == ["not_a_member"]


def test_an_out_of_range_value_is_demoted():
    doc, _ = _run(_response(**{"negative_class.validated_fraction":
                               _leaf(1.7, "validated fraction of 0.0")}))
    record = _demoted(doc)["/extracted/negative_class/validated_fraction"]
    assert record["failure_class"] == ["out_of_range"]


def test_several_fields_demote_in_one_pass():
    doc, _ = _run(_response(
        **{"negative_class.construction": _leaf("synthetic_decoys", "absent quote one"),
           "positive_class.evidence_type": _leaf("experimental_direct", "absent quote two")}))
    assert set(_demoted(doc)) == {CONSTRUCTION, "/extracted/positive_class/evidence_type"}
    assert doc["extraction_provenance"]["verified"] is True


def test_demotion_leaves_the_grounded_fields_alone():
    doc, _ = _run(_response(**{"negative_class.construction":
                               _leaf("synthetic_decoys", "an absent quote")}))
    assert doc["extracted"]["class_balance"]["value"] == {"positive": 269, "negative": 2690}
    assert doc["extraction_provenance"]["spans_checked"] == 9


# ======================================================================================
# offsets are computed here, never taken from the model
# ======================================================================================
def test_offsets_are_computed_and_raw():
    doc, _ = _run(_response())
    span = "binary classification benchmark"
    assert doc["extracted"]["task_type"]["offset"] == METHODS_TEXT.index(span)
    assert METHODS_TEXT[doc["extracted"]["task_type"]["offset"]:].startswith(span)


def test_a_model_supplied_offset_is_ignored():
    """Counting characters is what a model is worst at, and a wrong offset is a Gate 2 fault --
    trusting it would manufacture failures out of correct readings."""
    subtree = _subtree()
    subtree["task_type"]["offset"] = 99999  # the model volunteering an offset
    with pytest.raises(ExtractionFormatError, match="exactly value/evidence_span/confidence"):
        _run(json.dumps(subtree))


def test_a_line_wrapped_span_is_located_through_normalization():
    """The span crosses a newline + indent in the source; Gate 2's normalized stage finds it,
    and the offset recorded is the RAW one."""
    wrapped = "we report a validated fraction of 0.0"
    doc, _ = _run(_response(**{"negative_class.validated_fraction": _leaf(0.0, wrapped)}))
    assert _demoted(doc) == {}  # located, not demoted
    offset = doc["extracted"]["negative_class"]["validated_fraction"]["offset"]
    assert METHODS_TEXT[offset:].startswith("we\n")  # raw coordinates, not normalized


# ======================================================================================
# format failures are retried; content failures never are
# ======================================================================================
def test_malformed_json_is_retried_then_fails_hard():
    provider = StubProvider("not json at all", "still not json")
    with pytest.raises(ExtractionFormatError, match="not valid JSON"):
        extract(CARD, METHODS_TEXT, provider=provider, max_format_retries=1)
    assert provider.calls == 2  # the original plus one retry


def test_a_retry_that_succeeds_is_used():
    provider = StubProvider("{ broken", _response())
    doc = extract(CARD, METHODS_TEXT, provider=provider, max_format_retries=1)
    assert provider.calls == 2
    assert doc["extraction_provenance"]["verified"] is True


def test_zero_retries_is_honoured():
    provider = StubProvider("not json", _response())
    with pytest.raises(ExtractionFormatError):
        extract(CARD, METHODS_TEXT, provider=provider, max_format_retries=0)
    assert provider.calls == 1


def test_a_fenced_response_is_unwrapped():
    provider = StubProvider(f"```json\n{_response()}\n```")
    assert extract(CARD, METHODS_TEXT, provider=provider)["extraction_provenance"]["verified"]


@pytest.mark.parametrize(
    "bad,match",
    [
        ('{"task_type": {}}', "wrong keys"),
        ('["a list"]', "must be a JSON object"),
        (json.dumps({**_subtree(), "extra_field": {}}), "wrong keys"),
    ],
)
def test_shape_failures_are_loud(bad, match):
    with pytest.raises(ExtractionFormatError, match=match):
        _run(bad, max_format_retries=0)


def test_a_gate_violation_is_never_retried():
    """Re-prompting with 'that span was not found, try again' would optimise the model for
    passing the gate rather than for reading correctly."""
    provider = StubProvider(_response(**{"negative_class.construction":
                                         _leaf("synthetic_decoys", "an absent quote")}))
    extract(CARD, METHODS_TEXT, provider=provider, max_format_retries=3)
    assert provider.calls == 1  # demoted, not re-asked


# ======================================================================================
# what abstention cannot honestly repair -- hard failures
# ======================================================================================
def test_a_forbidden_phrase_is_a_hard_failure_not_a_demotion():
    """It carries no pointer, so no field can be blamed; blanking one would be a guess."""
    provider = StubProvider(_response(**{"positive_class.definition":
                                         _leaf("we recommend treating these as penetrant",
                                               "experimentally observed blood-brain barrier "
                                               "penetration")}))
    with pytest.raises(ExtractionViolation, match="abstention cannot honestly repair"):
        extract(CARD, METHODS_TEXT, provider=provider)


def test_a_hard_failure_writes_nothing():
    provider = StubProvider(_response(**{"positive_class.definition":
                                         _leaf("you should discard this dataset",
                                               "experimentally observed blood-brain barrier "
                                               "penetration")}))
    with pytest.raises(ExtractionViolation):
        extract(CARD, METHODS_TEXT, provider=provider)


def test_mirror_drift_is_a_hard_failure(monkeypatch):
    """Demoting it would bury a schema divergence as an honest abstention."""
    import copy as _copy

    real = extract_mod._load_schema

    def fake(name):
        s = _copy.deepcopy(real(name))
        if name == "extract.schema.json":
            s["$defs"]["prov_construction"]["properties"]["value"]["enum"].remove(
                "decoy_generated"
            )
        return s

    monkeypatch.setattr(extract_mod, "_load_schema", fake)
    extract_mod._validator.cache_clear()
    extract_mod._leaf_validator.cache_clear()
    try:
        with pytest.raises(ExtractionViolation, match="abstention cannot honestly repair"):
            _run(_response())
    finally:
        extract_mod._validator.cache_clear()
        extract_mod._leaf_validator.cache_clear()


# ======================================================================================
# the structural trust boundary -- the model authors the reading, nothing else
# ======================================================================================
def test_the_envelope_comes_from_extract_not_the_model():
    doc, _ = _run(_response())
    assert doc["schema"] == "permea.extract/1.1"
    assert doc["authoritative"] is False
    assert doc["status"] == "candidate"
    assert doc["source_text_sha256"] == extract_mod._sha256(METHODS_TEXT)
    assert doc["dataset_card"] == CARD
    assert len(doc["disclaimer"]) >= 40
    assert doc["model"]["provider"] == "exaone"
    assert doc["model"]["model_id"] == "fake-exaone-model"
    assert doc["model"]["temperature"] == 0.0
    assert len(doc["model"]["prompt_sha256"]) == 64


def test_the_model_cannot_author_envelope_or_provenance_fields():
    """A model that could write `authoritative` could write `true`. The shape check makes
    those keys unreachable rather than merely discouraged."""
    subtree = _subtree()
    subtree["authoritative"] = True
    subtree["extraction_provenance"] = {"verified": True, "demoted": []}
    with pytest.raises(ExtractionFormatError, match="wrong keys"):
        _run(json.dumps(subtree), max_format_retries=0)


def test_a_forged_leaf_key_is_rejected():
    subtree = _subtree()
    subtree["task_type"]["offset"] = 0
    with pytest.raises(ExtractionFormatError):
        _run(json.dumps(subtree), max_format_retries=0)


# ======================================================================================
# the prompt mirrors the gates, with enums read at runtime
# ======================================================================================
def test_the_prompt_carries_runtime_enums_not_hand_copied_ones():
    _, provider = _run(_response())
    label_schema = extract_mod._load_schema("label_schema.schema.json")
    for field in extract_mod._ENUM_FIELDS:
        for member in extract_mod._schema_enum(label_schema, field.label_ptr, "label_schema"):
            assert member in provider.user


def test_the_prompt_reproduces_the_methods_text_verbatim():
    """Every character the model sees must be one the span check can find."""
    _, provider = _run(_response())
    assert METHODS_TEXT in provider.user


def test_the_prompt_states_the_rules_the_gates_enforce():
    _, provider = _run(_response())
    system = provider.system.lower()
    assert "character for character" in system
    assert "null" in system and "abstain" in system
    assert "rejected" in system  # the asymmetry that makes abstention the safe default
    assert provider.temperature == 0.0


def test_the_dataset_card_is_marked_unquotable():
    _, provider = _run(_response())
    assert "NOT quotable" in provider.user


def test_one_call_for_all_twelve_fields():
    _, provider = _run(_response())
    assert provider.calls == 1
