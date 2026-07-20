"""Tests for the permea_explain EXTRACT postcondition (permea_explain.extract).

No network and no model: the candidate documents are built by hand so the three gates are
exercised deterministically. The honesty core is Gate 2 -- a span must be findable in the
source, case-preserved, with zero fuzz -- so most of this file is about what must FAIL.
"""
from __future__ import annotations

import copy
import hashlib
import json
import unicodedata

import pytest

from permea_explain import ExtractionViolation, StaleSourceError, write_checked
from permea_explain import extract as extract_mod
from permea_explain.providers.base import Provider, ProviderResponse

# Two deliberate whitespace features, both load-bearing for the offset tests:
#   * "Methods.  We" -- a DOUBLE space, so normalized indices run 1 behind raw indices for
#     everything after it. This is what makes "offset is in raw coordinates" falsifiable.
#   * "we\n    report" -- a newline plus indent, a 5-character run collapsing to one space,
#     so a line-wrapped span only matches under normalization N.
METHODS_TEXT = (
    "Methods.  We assembled a binary classification benchmark of blood-brain barrier "
    "penetration.\n"
    "Positive examples are peptides with experimentally observed blood-brain barrier "
    "penetration, measured by in situ perfusion.\n"
    "Negative examples were drawn at random from UniProt and were not tested; we\n"
    "    report a validated fraction of 0.0 for the negative set.\n"
    "Sequences in the negative set are random protein fragments, non-BBB-related.\n"
    "The final benchmark contains 269 positives and 2690 negatives.\n"
    "We estimate a label noise rate of 0.05 from duplicate review.\n"
)
SOURCE_SHA = hashlib.sha256(METHODS_TEXT.encode("utf-8")).hexdigest()

DISCLAIMER = (
    "This is a machine-generated candidate extraction of one dataset's label construction, "
    "read from its frozen methods text. It is NON-AUTHORITATIVE and asserts nothing beyond "
    "what its cited evidence spans support. A null value means 'not stated in the methods "
    "text', not 'false'."
)


def _leaf(value, span=None, offset=None, confidence=0.9):
    """A per-field-provenance leaf. Offset defaults to the span's first occurrence."""
    if value is None:
        return {"value": None, "evidence_span": None, "offset": None, "confidence": confidence}
    if offset is None:
        offset = METHODS_TEXT.index(span)
    return {"value": value, "evidence_span": span, "offset": offset, "confidence": confidence}


def _doc():
    """A candidate that passes all three gates. Ten non-null leaves, two honest abstentions."""
    return {
        "schema": "permea.extract/1.1",
        "authoritative": False,
        "status": "candidate",
        "source_text_sha256": SOURCE_SHA,
        "dataset_card": {"ref": "dataset_cards/bbb_peptides.json"},
        "model": {"provider": "exaone", "model_id": "fake-exaone-model"},
        "extracted": {
            "task_type": _leaf("binary_classification", "binary classification benchmark"),
            "positive_class": {
                "definition": _leaf(
                    "experimentally observed blood-brain barrier penetration",
                    "experimentally observed blood-brain barrier penetration",
                ),
                "evidence_type": _leaf("experimental_direct", "measured by in situ perfusion"),
                "assays": _leaf(["in_situ_perfusion"], "in situ perfusion"),
                "provenance_ref": _leaf(None),  # honest abstention
            },
            "negative_class": {
                "construction": _leaf(
                    "presumed_random",
                    "Negative examples were drawn at random from UniProt",
                ),
                "validated_fraction": _leaf(0.0, "validated fraction of 0.0"),
                "source_pool": _leaf(
                    "random protein fragments, non-BBB-related",
                    "random protein fragments, non-BBB-related",
                ),
                "matched_on": _leaf(None),  # honest abstention
                "known_confounds": _leaf(
                    ["source_pool_shift"], "drawn at random from UniProt"
                ),
            },
            "class_balance": _leaf(
                {"positive": 269, "negative": 2690}, "269 positives and 2690 negatives"
            ),
            "label_noise_estimate": _leaf(0.05, "label noise rate of 0.05"),
        },
        "disclaimer": DISCLAIMER,
    }


@pytest.fixture
def doc():
    return _doc()


def _construction(d):
    return d["extracted"]["negative_class"]["construction"]


# ======================================================================================
# precondition -- source text authentication, BEFORE any gate
# ======================================================================================
def test_wrong_methods_text_raises_stale_source(doc):
    with pytest.raises(StaleSourceError, match="source_text_sha256"):
        write_checked(doc, METHODS_TEXT + " tampered")


def test_stale_source_preempts_the_gates(doc):
    """A doc with a fabricated enum AND a stale hash reports the hash, not the enum: spans
    checked against the wrong string are meaningless, so the gates must not run at all."""
    _construction(doc)["value"] = "synthetic_decoys"
    with pytest.raises(StaleSourceError):
        write_checked(doc, "an entirely different methods text")


# ======================================================================================
# GATE 1 -- enum-validity
# ======================================================================================
def test_gate1_valid_enums_pass(doc):
    extract_mod.check_enum_validity(doc)  # does not raise


@pytest.mark.parametrize(
    "value",
    [
        "validated_experimental",
        "matched_control",
        "decoy_generated",
        "presumed_random",
        "assumed_unlabeled",
    ],
)
def test_gate1_accepts_every_construction_value_in_the_schema(doc, value):
    """All five label_schema construction values, decoy_generated included, are accepted.
    Guards against the enum being narrowed or hand-copied incompletely into Python."""
    _construction(doc)["value"] = value
    extract_mod.check_enum_validity(doc)


def test_gate1_fabricated_scalar_value_fails(doc):
    _construction(doc)["value"] = "synthetic_decoys"
    with pytest.raises(ExtractionViolation, match="synthetic_decoys"):
        extract_mod.check_enum_validity(doc)


def test_gate1_case_variant_fails(doc):
    """Exact string equality: no casefold, no trim, no nearest-match."""
    _construction(doc)["value"] = "Presumed_Random"
    with pytest.raises(ExtractionViolation, match="Presumed_Random"):
        extract_mod.check_enum_validity(doc)


def test_gate1_bad_array_element_fails(doc):
    doc["extracted"]["negative_class"]["known_confounds"]["value"] = [
        "source_pool_shift",
        "vibes_shift",
    ]
    with pytest.raises(ExtractionViolation, match="vibes_shift"):
        extract_mod.check_enum_validity(doc)


def test_gate1_non_unique_array_fails(doc):
    doc["extracted"]["negative_class"]["known_confounds"]["value"] = [
        "source_pool_shift",
        "source_pool_shift",
    ]
    with pytest.raises(ExtractionViolation, match="unique"):
        extract_mod.check_enum_validity(doc)


def test_gate1_null_value_passes(doc):
    _construction(doc).update({"value": None, "evidence_span": None, "offset": None})
    extract_mod.check_enum_validity(doc)


def test_gate1_empty_array_passes(doc):
    """[] means 'stated as none', which is a real reading and distinct from null."""
    doc["extracted"]["negative_class"]["matched_on"] = _leaf([], "were not tested")
    extract_mod.check_enum_validity(doc)


def test_gate1_mirror_drift_fires(doc, monkeypatch):
    """If extract.schema.json stops mirroring a label_schema enum value, say so at gate
    time rather than letting the divergence surface during reconciliation."""
    real = extract_mod._load_schema
    label = copy.deepcopy(real("label_schema.schema.json"))
    mirror = copy.deepcopy(real("extract.schema.json"))
    values = mirror["$defs"]["prov_construction"]["properties"]["value"]["enum"]
    mirror["$defs"]["prov_construction"]["properties"]["value"]["enum"] = [
        v for v in values if v != "decoy_generated"
    ]
    monkeypatch.setattr(
        extract_mod, "_load_schema", lambda name: label if "label_schema" in name else mirror
    )
    with pytest.raises(ExtractionViolation, match="mirror drift"):
        extract_mod.check_enum_validity(doc)


# ======================================================================================
# GATE 2 -- span-groundedness (the honesty-critical gate)
# ======================================================================================
def test_gate2_exact_match_passes(doc):
    extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_line_wrapped_span_passes_via_normalization(doc):
    """The source wraps 'we\\n    report'; a span with single spaces still matches under N."""
    raw = METHODS_TEXT.index("we\n")
    doc["extracted"]["label_noise_estimate"] = _leaf(
        0.05, "we report a validated fraction of 0.0", offset=raw
    )
    extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_offset_is_raw_not_normalized(doc):
    """The reported offset is in RAW methods_text coordinates. Everything after the double
    space in 'Methods.  We' sits one character earlier in normalized coordinates, so the
    normalized index is a concrete wrong answer -- and it must fail."""
    raw = METHODS_TEXT.index("we\n")
    normalized = raw - 1  # only the "Methods.  " double space precedes this point

    doc["extracted"]["label_noise_estimate"] = _leaf(
        0.05, "we report a validated fraction of 0.0", offset=normalized
    )
    with pytest.raises(ExtractionViolation, match=f"stated {normalized}"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)

    doc["extracted"]["label_noise_estimate"]["offset"] = raw
    extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_changed_case_fails(doc):
    """Matching is CASE-PRESERVED. A recased quote is not a quote."""
    _construction(doc)["evidence_span"] = "negative examples were drawn at random from uniprot"
    with pytest.raises(ExtractionViolation, match="does not appear verbatim"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_changed_punctuation_fails(doc):
    """N normalizes whitespace and nothing else -- not punctuation, not quotes, not dashes."""
    doc["extracted"]["negative_class"]["source_pool"]["evidence_span"] = (
        "random protein fragments non-BBB-related"  # comma dropped
    )
    with pytest.raises(ExtractionViolation, match="does not appear verbatim"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_dash_variant_fails(doc):
    """An en-dash is not a hyphen. No character folding of any kind."""
    doc["extracted"]["negative_class"]["source_pool"]["evidence_span"] = (
        "random protein fragments, non–BBB–related"
    )
    with pytest.raises(ExtractionViolation, match="does not appear verbatim"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_fuzzy_but_not_verbatim_fails(doc):
    """A near-miss paraphrase is exactly what this gate exists to reject. No threshold, ever."""
    _construction(doc)["evidence_span"] = (
        "Negative examples were drawn randomly from UniProt"  # 'at random' -> 'randomly'
    )
    with pytest.raises(ExtractionViolation, match="does not appear verbatim"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_correct_span_at_wrong_offset_fails_and_reports_both(doc):
    actual = METHODS_TEXT.index("validated fraction of 0.0")
    doc["extracted"]["negative_class"]["validated_fraction"]["offset"] = actual + 7
    with pytest.raises(ExtractionViolation) as exc:
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)
    message = str(exc.value)
    assert f"stated {actual + 7}" in message
    assert f"actual [{actual}]" in message


def test_gate2_recurring_span_at_a_valid_occurrence_passes(doc):
    """A span may legitimately recur. The extractor must point at a real occurrence -- not
    necessarily the first. (Gate 2 checks location, never entailment.)"""
    first = METHODS_TEXT.index("the negative set")
    second = METHODS_TEXT.index("the negative set", first + 1)
    assert first != second

    doc["extracted"]["negative_class"]["source_pool"] = _leaf(
        "the negative set", "the negative set", offset=second
    )
    extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_recurring_span_at_a_fabricated_offset_fails(doc):
    first = METHODS_TEXT.index("the negative set")
    doc["extracted"]["negative_class"]["source_pool"] = _leaf(
        "the negative set", "the negative set", offset=first + 3
    )
    with pytest.raises(ExtractionViolation, match="not at the stated offset"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_whitespace_only_span_fails(doc):
    """Empty after N. The schema's minLength:1 catches ''; this catches '   '."""
    doc["extracted"]["negative_class"]["source_pool"]["evidence_span"] = "   "
    doc["extracted"]["negative_class"]["source_pool"]["offset"] = 0
    with pytest.raises(ExtractionViolation, match="empty after whitespace normalization"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_abstained_field_needs_no_span_and_passes(doc):
    """Honest silence is free. A gate that punishes abstention manufactures fabrication."""
    doc["extracted"]["negative_class"]["source_pool"] = _leaf(None)
    doc["extracted"]["class_balance"] = _leaf(None)
    extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_non_null_value_without_a_span_fails(doc):
    doc["extracted"]["negative_class"]["source_pool"]["evidence_span"] = None
    with pytest.raises(ExtractionViolation, match="requires a string evidence_span"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)


def test_gate2_span_absent_from_source_fails(doc):
    _construction(doc)["evidence_span"] = "negatives were validated by mass spectrometry"
    with pytest.raises(ExtractionViolation, match="does not appear verbatim"):
        extract_mod.check_span_groundedness(doc, METHODS_TEXT)


# ======================================================================================
# GATE 3 -- forbidden-phrase (reused from NARRATE unchanged)
# ======================================================================================
def test_gate3_clean_text_passes(doc):
    extract_mod.check_forbidden_phrase(doc)


def test_gate3_forbidden_english_term_fails(doc):
    doc["extracted"]["negative_class"]["source_pool"]["value"] = (
        "random fragments; we recommend treating them as true negatives"
    )
    with pytest.raises(ExtractionViolation, match="forbidden phrase"):
        extract_mod.check_forbidden_phrase(doc, "english")


def test_gate3_forbidden_korean_term_fails_when_korean(doc):
    doc["extracted"]["positive_class"]["definition"]["value"] = "이 펩타이드는 통과할 것"
    with pytest.raises(ExtractionViolation, match="forbidden phrase"):
        extract_mod.check_forbidden_phrase(doc, "korean")


def test_gate3_korean_term_not_scanned_in_english_mode(doc):
    doc["extracted"]["positive_class"]["definition"]["value"] = "이 펩타이드는 통과할 것"
    extract_mod.check_forbidden_phrase(doc, "english")


def test_gate3_forbidden_phrase_inside_an_evidence_span_passes(doc):
    """A span QUOTES the source. If the methods text itself says 'we recommend', quoting it
    faithfully must not fail -- otherwise the gate would push the extractor to paraphrase its
    quotes, which would destroy Gate 2. Gate 3 constrains what the extractor SAYS, never what
    the source SAID."""
    quoting = _doc()
    quoting["extracted"]["negative_class"]["source_pool"]["evidence_span"] = (
        "we recommend treating them as negatives"
    )
    extract_mod.check_forbidden_phrase(quoting)  # passes: spans are excluded from Gate 3


# ======================================================================================
# write_checked -- aggregation and the proof-carrying stamps
# ======================================================================================
def test_write_checked_stamps_only_after_all_gates_pass(doc):
    result = write_checked(doc, METHODS_TEXT)
    provenance = result["extraction_provenance"]
    assert provenance["verified"] is True
    assert provenance["all_spans_verbatim"] is True
    assert provenance["all_span_enums_valid"] is True
    assert provenance["verifier_version"] == extract_mod.VERIFIER_VERSION
    # Ten non-null leaves; the two abstentions are excluded -- spans_checked counts what was
    # verified, not what was visited.
    assert provenance["spans_checked"] == 10


def test_write_checked_does_not_mutate_the_input(doc):
    before = copy.deepcopy(doc)
    write_checked(doc, METHODS_TEXT)
    assert doc == before
    assert "extraction_provenance" not in doc


def test_failed_gate_never_produces_stamps(doc):
    """The stamps are const:true in the schema; a doc that failed must be unconstructible
    through the sanctioned path."""
    _construction(doc)["value"] = "synthetic_decoys"
    with pytest.raises(ExtractionViolation):
        write_checked(doc, METHODS_TEXT)
    assert "extraction_provenance" not in doc


def test_incoming_stamps_do_not_survive_a_failed_gate(doc):
    """A candidate that arrives already asserting verified:true still has to earn it."""
    doc["extraction_provenance"] = {
        "verified": True,
        "all_spans_verbatim": True,
        "all_span_enums_valid": True,
    }
    _construction(doc)["evidence_span"] = "a sentence that is not in the methods text"
    with pytest.raises(ExtractionViolation):
        write_checked(doc, METHODS_TEXT)


def test_write_checked_aggregates_every_violation(doc):
    """All four gates run and all violations are reported -- never short-circuited.

    The count is 4, not 3: an out-of-enum value is ALSO schema-invalid, so Gate 4 reports it
    too. The overlap is deliberate -- suppressing it would mean re-deriving in Python which
    constraints the other gates already cover, which is the schema-forking Gate 4 avoids.
    """
    _construction(doc)["value"] = "synthetic_decoys"  # gate 1
    doc["extracted"]["negative_class"]["validated_fraction"]["evidence_span"] = (
        "not a sentence from the source"  # gate 2
    )
    doc["extracted"]["positive_class"]["definition"]["value"] = (
        "a definition that says you should trust it"  # gate 3
    )
    with pytest.raises(ExtractionViolation) as exc:
        write_checked(doc, METHODS_TEXT)
    message = str(exc.value)
    assert "synthetic_decoys" in message
    assert "does not appear verbatim" in message
    assert "forbidden phrase" in message
    assert "schema violation" in message
    assert "failed 4 postcondition check(s)" in message
    assert "--- offending document ---" in message


# ======================================================================================
# normalization N -- it must equal whole-string NFC, or offsets silently drift
# ======================================================================================
def _reference_normalize(text):
    """Whole-string NFC, then the same whitespace collapse. The definition N must match."""
    normalized = unicodedata.normalize("NFC", text)
    out, i = [], 0
    while i < len(normalized):
        if extract_mod._is_space(normalized[i]):
            while i < len(normalized) and extract_mod._is_space(normalized[i]):
                i += 1
            out.append(" ")
        else:
            out.append(normalized[i])
            i += 1
    return "".join(out)


@pytest.mark.parametrize(
    "text",
    [
        "plain ascii text",
        "café samples",  # decomposed
        "café samples",  # precomposed
        "ö̧ reordering",  # marks needing canonical reordering
        "각 jamo",  # Hangul L+V+T -> 각
        "각 precomposed",
        "펩타이드는 통과",
        "nbsp and​zwsp",
        "trailing   spaces\n\n  and newlines",
    ],
)
def test_normalization_matches_whole_string_nfc(text):
    normalized, index_map = extract_mod._normalize_with_map(text)
    assert normalized == _reference_normalize(text)
    assert len(normalized) == len(index_map)
    assert all(0 <= raw < len(text) for raw in index_map)
    assert all(index_map[j] <= index_map[j + 1] for j in range(len(index_map) - 1))


def test_hangul_jamo_span_matches_precomposed_source():
    """Conjoining jamo have combining class 0, so a naive 'starter + non-starters' cluster
    rule splits L+V+T and breaks NFC. This is the regression guard for that."""
    source = "샘플 각 negatives were pooled"
    span = "각"  # jamo spelling of 각
    normalized_text, index_map = extract_mod._normalize_with_map(source)
    hits = extract_mod._find_all(normalized_text, extract_mod._normalize_span(span))
    assert hits, "decomposed jamo span must match the precomposed source under N"
    assert index_map[hits[0]] == source.index("각")


def test_decomposed_span_matches_precomposed_source_offset_is_raw():
    source = "the café samples were pooled"
    span = "café samples"  # decomposed e + combining acute
    normalized_text, index_map = extract_mod._normalize_with_map(source)
    hits = extract_mod._find_all(normalized_text, extract_mod._normalize_span(span))
    assert hits
    assert index_map[hits[0]] == source.index("caf")


_ALL_NULL = json.dumps({
    "task_type": {"value": None, "evidence_span": None, "confidence": None},
    "positive_class": {k: {"value": None, "evidence_span": None, "confidence": None}
                       for k in ("definition", "evidence_type", "assays", "provenance_ref")},
    "negative_class": {k: {"value": None, "evidence_span": None, "confidence": None}
                       for k in ("construction", "validated_fraction", "source_pool",
                                 "matched_on", "known_confounds")},
    "class_balance": {"value": None, "evidence_span": None, "confidence": None},
    "label_noise_estimate": {"value": None, "evidence_span": None, "confidence": None},
})


class _StubProvider(Provider):
    """Offline. Behavioural coverage of extract() lives in test_explain_generate.py."""

    name = "exaone"

    def __init__(self, text):
        self._text = text

    @property
    def model_id(self) -> str:
        return "fake-exaone-model"

    def complete(self, system, user, *, max_tokens, temperature=None, stop=None):
        return ProviderResponse(text=self._text, provider="exaone", model_id="fake-exaone-model")


def test_candidate_generation_is_wired_to_the_postcondition():
    """extract() is implemented (#0023); its behaviour lives in test_explain_generate.py.

    What is pinned here is the relationship this module exists for: generation is not a
    separate path around the gate, it ends in write_checked.
    """
    calls = []
    real = extract_mod.write_checked
    monkey = pytest.MonkeyPatch()
    monkey.setattr(
        extract_mod,
        "write_checked",
        lambda *a, **kw: calls.append(1) or real(*a, **kw),
    )
    try:
        doc = extract_mod.extract(
            {"ref": "card.json"}, METHODS_TEXT, provider=_StubProvider(_ALL_NULL)
        )
    finally:
        monkey.undo()

    assert calls, "extract() must not return without going through write_checked"
    # And what it returned is what the gate stamped, not something assembled beside it.
    assert doc["extraction_provenance"]["verified"] is True
    assert extract_mod.collect_violations(doc, METHODS_TEXT) == []
