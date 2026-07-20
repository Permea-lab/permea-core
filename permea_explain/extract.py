"""extract.py -- the EXTRACT postcondition: the gate a candidate extraction must pass
BEFORE it may be written to record.

``write_checked`` is to EXTRACT what ``guardrails.render_checked`` is to NARRATE: validation
is a PRECONDITION OF WRITING, not a flag on the output. All three gates run, every violation
is collected (never short-circuited -- a partial diagnosis is a worse receipt), and on any
violation ``ExtractionViolation`` is raised so nothing is persisted.

  precondition : sha256(methods_text) == extract_doc.source_text_sha256. Not a gate --
                 spans checked against the wrong string are meaningless, so a mismatch
                 raises ``StaleSourceError`` before any gate runs.

  (1) enum-validity     : every non-null enum-typed value is a member of its enum, read AT
                          RUNTIME from label_schema.schema.json. ADAPTS NARRATE's
                          ``_fidelity_violations`` (membership in a closed set owned
                          elsewhere); the W-code regex does not carry over, because here the
                          values ARE the output rather than embedded in prose.
  (2) span-groundedness : every non-null field's evidence_span appears VERBATIM in
                          methods_text at its stated offset. REWRITES NARRATE's
                          ``_provenance_violations`` -- its precision-aware numeric tolerance
                          reconciles ``.4f`` against raw floats, and there is no analogous
                          benign reformatting for a quoted span. The tolerance here is zero.
  (3) forbidden-phrase  : REUSES NARRATE's check unchanged, term lists included.
  (4) schema-validity   : the document validates against extract.schema.json IN FULL -- the
                          declared types, ranges, lengths, consts and shapes that gates 1-3
                          never looked at. Validated on the STAMPED document, so what is
                          verified is exactly what is returned.

Gate 2 is the honesty-critical one. Matching is two-stage first-match-wins (exact, then
whitespace-normalized), CASE-PRESERVED, with NO fuzzy matching at any threshold, ever. The
whole value of the gate is that a passing extract's span can be pasted into a search box over
the source and found; a fuzzy match breaks that guarantee silently, and silently is the only
way this system can fail badly.

Abstention (value:null) passes Gate 2 with no span required. This is deliberate and pairs
with the schema's ``abstention_coherence``: a gate that punishes abstention manufactures the
fabrication it is meant to catch.

Gate 4 makes the postcondition's guarantee total: "write_checked passed" now IMPLIES "this
artifact is schema-valid". Before it, a grounded-but-impossible value (validated_fraction
1.7, a 5-character definition) collected the verified:true stamp -- and so did a document
setting ``authoritative: true``, since the const:false posture was declared in the schema and
enforced nowhere.

SCOPE. This module verifies that a span IS IN the source. It does NOT verify that the span
SUPPORTS the value it grounds -- see the scope note at the stamp site in ``_stamp``.

EXTRACT itself (prompting a model to produce the candidate) is a later task; only the
postcondition lives here.
"""
from __future__ import annotations

import copy
import functools
import hashlib
import json
import re
import unicodedata
from importlib.resources import files
from typing import NamedTuple

from . import extract_prompt
from .providers import get_provider

# Gate 3 is reused AS-IS from the NARRATE layer. The private name is imported deliberately:
# re-listing the terms here would fork the review surface, and the whole point is that the
# list grows in one place and both layers inherit the growth.
from .guardrails import _forbidden_violations
from .violations import (
    DEMOTABLE_KINDS,
    ENUM_INVALID,
    ENUM_MIRROR_DRIFT,
    LEAF_MISSING,
    LEAF_MISSING_VALUE,
    OFFSET_INVALID,
    SCHEMA_INVALID,
    SPAN_EMPTY,
    SPAN_MISSING_ON_NONNULL,
    SPAN_NOT_FOUND,
    SPAN_OFFSET_MISMATCH,
    Demotion,
    Violation,
    join_messages,
)

VERIFIER_VERSION = "permea-explain-extract-postcondition/0.1"

# The schemas are the source of truth for every enum, read at runtime rather than hand-copied
# into Python -- a duplicated enum list is a drift bug waiting for the 1.1 task_type widening.
# The two schemas the gates READ live inside this package and ship as package-data, resolved
# through importlib.resources rather than a __file__-relative walk. The walk resolved only
# because an editable install leaves the package sitting in the repo; from a wheel it landed
# in site-packages/ and every gate died on the first extract(). The other 18 schemas stay at
# the repo root, which is a public review surface, not an import path.
_SCHEMAS_DIR = files(__package__) / "schemas"


class ExtractionViolation(AssertionError):
    """Raised when a candidate extraction violates the postcondition. Nothing is written."""


class StaleSourceError(AssertionError):
    """Raised when methods_text does not hash to the document's source_text_sha256."""


# --------------------------------------------------------------------------------------
# field map -- what is checked, and where its authority lives
# --------------------------------------------------------------------------------------
_MISSING = object()


class _EnumField(NamedTuple):
    pointer: str  # into extract_doc
    is_array: bool
    label_ptr: str  # authority: label_schema.schema.json
    extract_ptr: str  # mirror: extract.schema.json


_ENUM_FIELDS = (
    _EnumField(
        "/extracted/task_type",
        False,
        "/properties/task_type/enum",
        "/$defs/prov_task_type/properties/value/enum",
    ),
    _EnumField(
        "/extracted/positive_class/evidence_type",
        False,
        "/$defs/positive_class/properties/evidence_type/enum",
        "/$defs/prov_evidence_type/properties/value/enum",
    ),
    _EnumField(
        "/extracted/negative_class/construction",
        False,
        "/$defs/negative_class/properties/construction/enum",
        "/$defs/prov_construction/properties/value/enum",
    ),
    _EnumField(
        "/extracted/negative_class/matched_on",
        True,
        "/$defs/negative_class/properties/matched_on/items/enum",
        "/$defs/prov_matched_on/properties/value/anyOf/0/items/enum",
    ),
    _EnumField(
        "/extracted/negative_class/known_confounds",
        True,
        "/$defs/negative_class/properties/known_confounds/items/enum",
        "/$defs/prov_known_confounds/properties/value/anyOf/0/items/enum",
    ),
)

# Every per-field-provenance leaf, in document order. Gate 2 walks exactly these.
_PROV_LEAVES = (
    "/extracted/task_type",
    "/extracted/positive_class/definition",
    "/extracted/positive_class/evidence_type",
    "/extracted/positive_class/assays",
    "/extracted/positive_class/provenance_ref",
    "/extracted/negative_class/construction",
    "/extracted/negative_class/validated_fraction",
    "/extracted/negative_class/source_pool",
    "/extracted/negative_class/matched_on",
    "/extracted/negative_class/known_confounds",
    "/extracted/class_balance",
    "/extracted/label_noise_estimate",
)

# Gate 3 reads extractor-AUTHORED prose only. Enum values are Gate 1's business, and
# evidence_span values are EXCLUDED on purpose -- a span quotes the source, so forbidding
# source wording would push the extractor to paraphrase its quotes and destroy Gate 2.
_FREE_TEXT_STRING = (
    "/extracted/positive_class/definition",
    "/extracted/positive_class/provenance_ref",
    "/extracted/negative_class/source_pool",
)
_FREE_TEXT_STRING_LIST = ("/extracted/positive_class/assays",)


def _get(doc, pointer: str):
    """Resolve a JSON pointer, returning ``_MISSING`` rather than raising."""
    cur = doc
    for raw in pointer.lstrip("/").split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(cur, dict):
            if token not in cur:
                return _MISSING
            cur = cur[token]
        elif isinstance(cur, list):
            try:
                cur = cur[int(token)]
            except (ValueError, IndexError):
                return _MISSING
        else:
            return _MISSING
    return cur


@functools.lru_cache(maxsize=None)
def _load_schema(name: str) -> dict:
    path = _SCHEMAS_DIR / name
    if not path.is_file():
        raise RuntimeError(
            f"cannot read {name}: {path} not found. The EXTRACT postcondition reads its "
            "enums from the schemas at runtime and refuses to fall back to hand-copied "
            "values, because a stale copy would silently accept a fabricated enum."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_enum(schema: dict, pointer: str, name: str) -> list:
    found = _get(schema, pointer)
    if not isinstance(found, list):
        raise RuntimeError(f"{name}: expected an enum list at {pointer}, found {found!r}")
    return found


# --------------------------------------------------------------------------------------
# (1) enum-validity -- ADAPTS guardrails._fidelity_violations
# --------------------------------------------------------------------------------------
def _enum_violations(doc: dict) -> list[Violation]:
    label_schema = _load_schema("label_schema.schema.json")
    extract_schema = _load_schema("extract.schema.json")
    bad: list[Violation] = []

    for f in _ENUM_FIELDS:
        allowed = _schema_enum(label_schema, f.label_ptr, "label_schema.schema.json")
        mirrored = [
            v
            for v in _schema_enum(extract_schema, f.extract_ptr, "extract.schema.json")
            if v is not None
        ]
        # Mirror drift caught at gate time rather than at reconciliation time: extract.schema
        # mirrors label_schema, so a value the authority permits but the mirror omits means
        # the two have diverged.
        drifted = [v for v in allowed if v not in mirrored]
        if drifted:
            # Its OWN kind, not ENUM_INVALID. This says the two schemas disagree, which is a
            # schema fault; the value in hand may be read perfectly. A recovery step that
            # keyed on the pointer alone would demote the field and bury the divergence.
            bad.append(
                Violation(
                    f.pointer,
                    ENUM_MIRROR_DRIFT,
                    f"{f.pointer}: enum mirror drift -- label_schema permits {drifted!r}, "
                    f"absent from extract.schema.json at {f.extract_ptr}",
                )
            )

        leaf = _get(doc, f.pointer)
        if leaf is _MISSING or not isinstance(leaf, dict):
            bad.append(
                Violation(
                    f.pointer, LEAF_MISSING, f"{f.pointer}: required provenance leaf is missing"
                )
            )
            continue
        value = leaf.get("value", _MISSING)
        if value is _MISSING:
            bad.append(
                Violation(
                    f.pointer,
                    LEAF_MISSING_VALUE,
                    f"{f.pointer}: provenance leaf has no 'value' key",
                )
            )
            continue
        # Abstention is Gate 2 / abstention_coherence's business, not this gate's.
        if value is None:
            continue

        permitted = "{" + ", ".join(map(str, allowed)) + "}"
        # Pointer is the FIELD even for a bad array element -- the field is what a caller can
        # act on. The element index stays in the message.
        if f.is_array:
            if not isinstance(value, list):
                bad.append(
                    Violation(
                        f.pointer,
                        ENUM_INVALID,
                        f"{f.pointer}: expected an array of enum values, got {value!r}",
                    )
                )
                continue
            # An empty array passes: it means "stated as none", distinct from null.
            for i, element in enumerate(value):
                # Exact string equality. No casefold, no trim, no nearest-match.
                if not isinstance(element, str) or element not in allowed:
                    bad.append(
                        Violation(
                            f.pointer,
                            ENUM_INVALID,
                            f"{f.pointer}/{i}: {element!r} is not a member of {permitted}",
                        )
                    )
            if len(value) != len({repr(el) for el in value}):
                bad.append(
                    Violation(
                        f.pointer,
                        ENUM_INVALID,
                        f"{f.pointer}: array elements must be unique, got {value!r}",
                    )
                )
        else:
            if not isinstance(value, str) or value not in allowed:
                bad.append(
                    Violation(
                        f.pointer,
                        ENUM_INVALID,
                        f"{f.pointer}: {value!r} is not a member of {permitted}",
                    )
                )

    return bad


# --------------------------------------------------------------------------------------
# (2) span-groundedness -- REWRITES guardrails._provenance_violations; tolerance = ZERO
# --------------------------------------------------------------------------------------
# N step 2: the Unicode Zs category plus these explicit characters. U+200B is category Cf,
# not Zs, so it has to be named; U+00A0 is Zs but is named here for readability.
_EXPLICIT_SPACE = "\t\n\r\f\v ​"


def _is_space(ch: str) -> bool:
    return ch in _EXPLICIT_SPACE or unicodedata.category(ch) == "Zs"


def _extends_cluster(prefix: str, ch: str) -> bool:
    """Does ``ch`` belong to the same NFC composition cluster as ``prefix``?

    Two rules, and BOTH are needed -- each alone is provably wrong:

      * ``combining(ch) != 0`` -- a non-starter belongs to the preceding combining sequence.
        Needed because NFC is decompose -> canonically REORDER -> compose, and reordering
        moves marks within a combining sequence. Cutting such a sequence would reorder the
        halves independently and diverge from whole-string NFC.
      * ``_composes(prefix, ch)`` -- an empirical test for composition across the boundary.
        Needed because Hangul conjoining jamo V and T have combining class 0, so the first
        rule alone splits L+V+T sequences that NFC composes into one syllable. Asking
        ``unicodedata`` directly is exact for every script, future additions included.
    """
    if unicodedata.combining(ch) != 0:
        return True
    joined = unicodedata.normalize("NFC", prefix + ch)
    apart = unicodedata.normalize("NFC", prefix) + unicodedata.normalize("NFC", ch)
    return joined != apart


def _normalize_with_map(text: str) -> tuple[str, list[int]]:
    """Apply N to ``text``, returning the normalized string and its normalized->raw index map.

    N is LIMITED TO: (1) Unicode NFC, (2) map every space-like character to U+0020,
    (3) collapse each maximal run of U+0020 to one. Step (4), stripping the ends, applies to
    the SPAN ONLY and is done by ``_normalize_span`` -- stripping the text here would shift
    every offset.

    N does NOT change case, strip or fold punctuation, normalize quotes or dashes, remove
    diacritics, stem, lemmatize, or edit-distance anything.

    ``index_map[j]`` is the RAW index of the first character of the run that produced
    normalized character ``j``. This is what keeps reported offsets in raw source
    coordinates. NFC is applied per composition-cluster rather than to the whole string, so
    that every emitted character keeps a raw index it can be traced back to; cluster
    boundaries come from ``_composes_across``, so the result is identical to NFC over the
    whole text. Text that is already NFC (which is essentially all real input) skips the
    clustering entirely and maps one raw character per normalized character.
    """
    out: list[str] = []
    index_map: list[int] = []
    already_nfc = unicodedata.is_normalized("NFC", text)
    i, n = 0, len(text)
    while i < n:
        start = i
        if _is_space(text[i]):
            while i < n and _is_space(text[i]):
                i += 1
            out.append(" ")
            index_map.append(start)
        else:
            i += 1
            if not already_nfc:
                while (
                    i < n
                    and not _is_space(text[i])
                    and _extends_cluster(text[start:i], text[i])
                ):
                    i += 1
            chunk = text[start:i]
            for ch in chunk if already_nfc else unicodedata.normalize("NFC", chunk):
                out.append(ch)
                index_map.append(start)
    return "".join(out), index_map


def _normalize_span(span: str) -> str:
    """N applied to a span: the shared normalization, plus the ends stripped (N step 4)."""
    normalized, _ = _normalize_with_map(span)
    return normalized.strip(" ")


def _find_all(haystack: str, needle: str) -> list[int]:
    """Every occurrence index, overlapping included. An empty needle matches nothing."""
    if not needle:
        return []
    hits, start = [], 0
    while True:
        j = haystack.find(needle, start)
        if j < 0:
            return hits
        hits.append(j)
        start = j + 1


def _span_violations(doc: dict, methods_text: str) -> tuple[list[Violation], int]:
    """Returns (violations, spans_checked).

    ``spans_checked`` counts what was VERIFIED -- non-null leaves -- not what was visited;
    abstentions are excluded.
    """
    bad: list[Violation] = []
    checked = 0
    norm_text: str | None = None
    index_map: list[int] = []

    for pointer in _PROV_LEAVES:
        leaf = _get(doc, pointer)
        if leaf is _MISSING or not isinstance(leaf, dict):
            bad.append(
                Violation(
                    pointer, LEAF_MISSING, f"{pointer}: required provenance leaf is missing"
                )
            )
            continue
        value = leaf.get("value", _MISSING)
        if value is _MISSING:
            bad.append(
                Violation(
                    pointer, LEAF_MISSING_VALUE, f"{pointer}: provenance leaf has no 'value' key"
                )
            )
            continue

        # Abstention passes and requires nothing. The converse direction -- an abstention must
        # not CARRY a span -- is abstention_coherence's job in the schema, not this gate's.
        if value is None:
            continue

        checked += 1
        span = leaf.get("evidence_span")
        offset = leaf.get("offset")
        if not isinstance(span, str):
            bad.append(
                Violation(
                    pointer,
                    SPAN_MISSING_ON_NONNULL,
                    f"{pointer}: a non-null value requires a string evidence_span, got {span!r}",
                )
            )
            continue
        if not isinstance(offset, int) or isinstance(offset, bool) or offset < 0:
            bad.append(
                Violation(
                    pointer,
                    OFFSET_INVALID,
                    f"{pointer}: a non-null value requires a non-negative integer offset, "
                    f"got {offset!r}",
                )
            )
            continue

        norm_span = _normalize_span(span)
        if norm_span == "":
            bad.append(
                Violation(
                    pointer,
                    SPAN_EMPTY,
                    f"{pointer}: evidence_span is empty after whitespace normalization; a "
                    "non-null value must be grounded by a real span",
                )
            )
            continue

        # Stage 1 -- exact, byte-for-byte. First match wins: if the raw span is present, the
        # normalized pass never runs.
        raw_hits = _find_all(methods_text, span)
        if raw_hits:
            # Ambiguity: the extractor is not required to point at the first occurrence, only
            # at a real one.
            if offset not in raw_hits:
                bad.append(
                    Violation(
                        pointer,
                        SPAN_OFFSET_MISMATCH,
                        f"{pointer}: evidence_span found verbatim but not at the stated offset "
                        f"-- stated {offset}, actual {raw_hits}",
                    )
                )
            continue

        # Stage 2 -- whitespace-normalized, CASE-PRESERVED. No fuzzy fallback after this.
        if norm_text is None:
            norm_text, index_map = _normalize_with_map(methods_text)
        hits = _find_all(norm_text, norm_span)
        if not hits:
            bad.append(
                Violation(
                    pointer,
                    SPAN_NOT_FOUND,
                    f"{pointer}: evidence_span does not appear verbatim in methods_text: {span!r}",
                )
            )
            continue
        # Map normalized hits back to RAW coordinates -- offset is never a normalized index.
        expected = sorted({index_map[h] for h in hits})
        if offset not in expected:
            # A wrong offset is a VIOLATION, not something to silently repair: it means the
            # extractor was not reading where it claims to have read.
            bad.append(
                Violation(
                    pointer,
                    SPAN_OFFSET_MISMATCH,
                    f"{pointer}: evidence_span matched under whitespace normalization but not at "
                    f"the stated offset -- stated {offset}, actual {expected}",
                )
            )

    return bad, checked


# --------------------------------------------------------------------------------------
# (4) schema-validity -- the declared types, ranges, lengths, consts and shapes
# --------------------------------------------------------------------------------------
# Gates 1-3 answer "is this reading grounded?". None of them answers "is this document the
# shape it claims to be", so a grounded-but-impossible value (validated_fraction 1.7, a
# 5-character definition) used to collect the verified:true stamp. Worse, `authoritative`
# and `status` are const:false / const:"candidate" in the schema and nothing enforced them,
# so a document CLAIMING AUTHORITY could be stamped; and abstention_coherence was unchecked,
# so a null value could carry a fabricated span and offset.
#
# The constraints are validated against extract.schema.json rather than re-stated in Python.
# A hand-rolled copy would fork the review surface from the schema -- the same reason Gate 1
# reads its enums at runtime instead of hard-coding them.
_MISSING_JSONSCHEMA = (
    "The EXTRACT postcondition's schema gate needs the optional validation dependency. "
    "Install the extra: pip install 'permea-core[explain]'  (permea_explain itself ships "
    "without it, but a candidate extraction cannot be verified)."
)


@functools.lru_cache(maxsize=None)
def _validator():
    """The compiled extract.schema.json validator. Imported locally: like the live provider
    transport, the dependency is gated behind the [explain] extra and its absence must give a
    clear install hint rather than an ImportError from somewhere unrelated."""
    try:
        from jsonschema import Draft202012Validator
    except ImportError as exc:
        raise RuntimeError(_MISSING_JSONSCHEMA) from exc
    return Draft202012Validator(_load_schema("extract.schema.json"))


def _error_pointer(error) -> str | None:
    """The JSON pointer of the failing field, or None for a whole-document error.

    Truncated to the enclosing per-field-provenance leaf when the failure is inside one, so
    the pointer names the unit a caller can act on -- ``/extracted/class_balance`` rather
    than ``/extracted/class_balance/value/positive``. Same rule as the array-element pointers
    in Gate 1.
    """
    parts = [str(p).replace("~", "~0").replace("/", "~1") for p in error.absolute_path]
    if not parts:
        return None  # e.g. a missing required property, or a stray top-level key
    pointer = "/" + "/".join(parts)
    for leaf in _PROV_LEAVES:
        if pointer == leaf or pointer.startswith(leaf + "/"):
            return leaf
    return pointer


def _schema_violations(doc: dict) -> list[Violation]:
    """Validate the document against extract.schema.json in full.

    Note this is given the STAMPED document, never the raw candidate: ``extraction_provenance``
    is top-level ``required`` but may only be written by this module after the other gates
    pass, so a raw candidate is schema-invalid by construction and validating it would report
    a failure that is an artifact of the pipeline rather than of the extraction.
    """
    errors = sorted(_validator().iter_errors(doc), key=lambda e: (list(e.absolute_path), e.message))
    out: list[Violation] = []
    for error in errors:
        pointer = _error_pointer(error)
        prefix = f"{pointer}: " if pointer else ""
        out.append(
            Violation(pointer, SCHEMA_INVALID, f"{prefix}schema violation -- {error.message}")
        )
    return out


# --------------------------------------------------------------------------------------
# (3) forbidden-phrase -- REUSED AS-IS from guardrails
# --------------------------------------------------------------------------------------
def _authored_text(doc: dict) -> str:
    """The extractor's OWN prose. Enum values and evidence_span quotes are excluded."""
    parts: list[str] = []
    for pointer in _FREE_TEXT_STRING:
        leaf = _get(doc, pointer)
        if isinstance(leaf, dict) and isinstance(leaf.get("value"), str):
            parts.append(leaf["value"])
    for pointer in _FREE_TEXT_STRING_LIST:
        leaf = _get(doc, pointer)
        if isinstance(leaf, dict) and isinstance(leaf.get("value"), list):
            parts.extend(item for item in leaf["value"] if isinstance(item, str))
    if isinstance(doc.get("disclaimer"), str):
        parts.append(doc["disclaimer"])
    return "\n".join(parts)


# --------------------------------------------------------------------------------------
# demotion record -- what was reset to abstention, and how it failed. NEVER what it said.
# --------------------------------------------------------------------------------------
# The one rule this section exists to keep: everything in a document stamped verified:true is
# grounded or null. A rejected reading is neither, so it does not go in. What goes in is a
# classification computed FROM the rejected reading and a digest OF it -- both inert, neither
# reproducible into something a reader could mistake for a source quote.
CASE_VARIANT = "case_variant"
WHITESPACE_VARIANT = "whitespace_variant"
NOT_A_MEMBER = "not_a_member"
OUT_OF_RANGE = "out_of_range"
WRONG_TYPE = "wrong_type"
SPAN_ABSENT = "span_absent"
OFFSET_WRONG = "offset_wrong"
STRUCTURAL = "structural"

#: Violation kind -> classification, for the kinds that need no look at the value.
_KIND_CLASS = {
    SPAN_NOT_FOUND: SPAN_ABSENT,
    SPAN_EMPTY: SPAN_ABSENT,
    SPAN_MISSING_ON_NONNULL: WRONG_TYPE,
    OFFSET_INVALID: WRONG_TYPE,
    SPAN_OFFSET_MISMATCH: OFFSET_WRONG,
}

#: jsonschema keyword -> classification, for schema_invalid violations.
_KEYWORD_CLASS = {
    "minimum": OUT_OF_RANGE,
    "maximum": OUT_OF_RANGE,
    "exclusiveMinimum": OUT_OF_RANGE,
    "exclusiveMaximum": OUT_OF_RANGE,
    "minLength": OUT_OF_RANGE,
    "maxLength": OUT_OF_RANGE,
    "minItems": OUT_OF_RANGE,
    "maxItems": OUT_OF_RANGE,
    "type": WRONG_TYPE,
    "enum": NOT_A_MEMBER,
    "const": NOT_A_MEMBER,
}


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _classify_enum_value(pointer: str, value) -> set[str]:
    """How an out-of-enum reading missed. Reads ``value`` transiently; stores nothing from it.

    The distinction worth keeping is between a model that picked a REAL member and mangled
    its formatting and one that INVENTED a member. The first is a formatting bug in the
    extractor; the second is a fabrication. They deserve different responses, and after
    #0016/#0017 -- two live false-positives that were pure formatting -- it is worth being
    able to tell which this was without keeping the string.
    """
    field = next((f for f in _ENUM_FIELDS if f.pointer == pointer), None)
    if field is None:
        return {NOT_A_MEMBER}
    try:
        allowed = _schema_enum(
            _load_schema("label_schema.schema.json"), field.label_ptr, "label_schema.schema.json"
        )
    except RuntimeError:
        return {NOT_A_MEMBER}

    # WRONG_TYPE is reserved for a container-shape error -- an array field handed a scalar,
    # or the reverse. Within a field whose constraint IS the enum, a non-string is simply not
    # a member, which is what the schema keyword says too; calling it a type error would
    # split one fault across two classes.
    if field.is_array != isinstance(value, list):
        return {WRONG_TYPE}

    candidates = value if isinstance(value, list) else [value]
    out: set[str] = set()
    for candidate in candidates:
        if not isinstance(candidate, str):
            out.add(NOT_A_MEMBER)
        elif candidate in allowed:
            continue  # this element was fine; another one is why we are here
        elif any(candidate.casefold() == a.casefold() for a in allowed):
            out.add(CASE_VARIANT)
        elif any("".join(candidate.split()).casefold() == "".join(a.split()).casefold()
                 for a in allowed):
            out.add(WHITESPACE_VARIANT)
        else:
            out.add(NOT_A_MEMBER)
    return out or {STRUCTURAL}  # e.g. a duplicate-elements array of otherwise valid members


@functools.lru_cache(maxsize=None)
def _leaf_validator(pointer: str):
    """A validator for ONE provenance leaf, derived from extract.schema.json.

    The leaf's ``$ref`` is read out of the schema rather than kept in a Python lookup table,
    so adding or renaming a leaf cannot leave a stale mapping behind -- the same reason the
    enums are read at runtime. ``$defs`` is carried along because a leaf's sub-refs
    (evidence_span_field, abstention_coherence) resolve against the document root.
    """
    schema = _load_schema("extract.schema.json")
    node = schema["properties"]["extracted"]
    for key in pointer[len("/extracted/") :].split("/"):
        node = node["properties"][key]
    from jsonschema import Draft202012Validator  # already gated by _validator()

    return Draft202012Validator({"$defs": schema["$defs"], "allOf": [{"$ref": node["$ref"]}]})


def _keywords(error):
    """Every constraint keyword implicated, including inside anyOf/oneOf branches."""
    yield error.validator
    for sub in error.context or ():
        yield from _keywords(sub)


def _classify_schema_value(pointer: str, value, confidence) -> set[str]:
    """Classify a schema_invalid demotion by re-validating the rejected reading in isolation.

    The stored Gate 4 message is not enough to classify from: nearly every leaf permits an
    abstention, so its value sits behind ``anyOf`` and the top-level error says only "is not
    valid under any of the given schemas". The real keyword lives in the sub-errors, so the
    rejected value is validated again here -- transiently, against the leaf's own schema --
    and only the resulting classification is kept.

    A specific class (a range, a length, an enum) beats WRONG_TYPE when both appear: the null
    branch of every abstention-permitting field always contributes a bare type mismatch, so
    without this every out-of-range number would read as merely 'wrong type'.
    """
    # Grounded placeholders so abstention_coherence does not fire and drown the real fault;
    # this probe leaf is never returned or stored.
    probe = {"value": value, "evidence_span": "x", "offset": 0, "confidence": confidence}
    found: set[str] = set()
    for error in _leaf_validator(pointer).iter_errors(probe):
        for keyword in _keywords(error):
            if keyword in _KEYWORD_CLASS:
                found.add(_KEYWORD_CLASS[keyword])
    specific = found - {WRONG_TYPE}
    return specific or found or {STRUCTURAL}


def _demotion_record(demotion: Demotion) -> dict:
    """Build the inert record for one demotion. The rejected reading does not survive this."""
    kinds = sorted({v.kind for v in demotion.violations})
    # Gate 4 would reject a non-demotable kind anyway, but failing here names the caller that
    # tried it. Demoting a mirror drift would bury a schema divergence as an honest
    # abstention; demoting a missing leaf would invent an answer the model never gave.
    forbidden = sorted(set(kinds) - DEMOTABLE_KINDS)
    if forbidden:
        raise ExtractionViolation(
            f"{demotion.pointer}: {forbidden!r} is not demotable. A field may only be reset to "
            "abstention for a fault in its own reading; these name faults that abstaining "
            "would conceal."
        )
    from_enum: set[str] = set()
    from_schema: set[str] = set()
    classes: set[str] = set()
    for v in demotion.violations:
        if v.kind == ENUM_INVALID:
            from_enum |= _classify_enum_value(demotion.pointer, demotion.rejected_value)
        elif v.kind == SCHEMA_INVALID:
            from_schema |= _classify_schema_value(
                demotion.pointer, demotion.rejected_value, demotion.rejected_confidence
            )
        elif v.kind in _KIND_CLASS:
            classes.add(_KIND_CLASS[v.kind])
        else:
            classes.add(STRUCTURAL)

    # The gates overlap by design, so one bad enum arrives as both ENUM_INVALID and
    # SCHEMA_INVALID. About the VALUE the schema can only ever say NOT_A_MEMBER -- `enum` is
    # the only keyword it can trip -- while the enum classifier distinguishes a mis-cased real
    # member from an invented one from a container-shape error. Where both spoke about the
    # same value the finer reading wins; anything else the schema found (a confidence out of
    # range, say) is still kept.
    if from_enum:
        from_schema.discard(NOT_A_MEMBER)
    classes |= from_enum | from_schema

    record = {
        "pointer": demotion.pointer,
        "kinds": kinds,
        "failure_class": sorted(classes) or [STRUCTURAL],
    }
    # Digests and shapes only. Note what is NOT here: the value and the span themselves.
    if demotion.rejected_value is not None:
        record["rejected_value_sha256"] = _sha256(
            json.dumps(demotion.rejected_value, ensure_ascii=False, sort_keys=True, default=str)
        )
    if isinstance(demotion.rejected_span, str):
        record["rejected_span_sha256"] = _sha256(demotion.rejected_span)
        record["rejected_span_length"] = len(demotion.rejected_span)
    if demotion.rejected_confidence is not None:
        record["rejected_confidence"] = demotion.rejected_confidence
    return record


def _check_demotion_coherence(stamped: dict, records: list[dict]) -> None:
    """The two rules JSON Schema cannot express (see $runtime_rules).

    Both are internal contradictions in the receipt rather than faults in the candidate, so
    they raise directly instead of joining the aggregated violations: there is no reading a
    caller could demote to fix them.
    """
    pointers = [r["pointer"] for r in records]
    duplicated = sorted({p for p in pointers if pointers.count(p) > 1})
    if duplicated:
        raise ExtractionViolation(
            f"demotion record is incoherent: more than one record for {duplicated!r}. A field "
            "that failed several ways carries ONE record with several kinds."
        )
    for pointer in pointers:
        leaf = _get(stamped, pointer)
        if not isinstance(leaf, dict) or leaf.get("value", _MISSING) is not None:
            raise ExtractionViolation(
                f"demotion record is incoherent: {pointer} is recorded as demoted but its "
                "value is not null. A demotion IS an abstention; recording one against a "
                "field that still carries a value would make the receipt and the reading "
                "disagree about what happened."
            )


# --------------------------------------------------------------------------------------
# precondition
# --------------------------------------------------------------------------------------
def _check_source_text(doc: dict, methods_text: str) -> None:
    stated = doc.get("source_text_sha256")
    actual = hashlib.sha256(methods_text.encode("utf-8")).hexdigest()
    if stated != actual:
        raise StaleSourceError(
            "methods_text does not match source_text_sha256: document states "
            f"{stated!r}, supplied text hashes to {actual!r}. Every evidence_span and offset "
            "is measured against the hashed text, so the gates would be checking the wrong "
            "string."
        )


# --------------------------------------------------------------------------------------
# public surface
# --------------------------------------------------------------------------------------
def _stamp(extract_doc: dict, spans_checked: int, demotions=()) -> dict:
    """The to-be-returned document: a COPY of the candidate carrying the receipt.

    Built unconditionally so Gate 4 can validate the exact object ``write_checked`` would
    return. Building it is not the same as blessing it -- nothing is returned unless every
    gate passes.

    ``demotions`` are the fields the recovery path reset to abstention. They are DERIVED from
    structured Violations, never asserted: a caller hands over what it discarded, and the
    record is computed here. Only the classification and digests survive -- see
    ``_demotion_record``.
    """
    records = [_demotion_record(d) for d in demotions]
    stamped = copy.deepcopy(extract_doc)
    # The const:true stamps are set HERE and only here, and the document carrying them is the
    # document Gate 4 validates. A document asserting true that did not pass is
    # unconstructible through this path.
    #
    # SCOPE NOTE (open item): all_span_enums_valid asserts enum membership AND verbatim
    # grounding. It does NOT assert ENTAILMENT -- that the span semantically supports that
    # specific enum choice. Entailment is a reconciliation judgment owned by the engine; see
    # $runtime_rules in extract.schema.json and label_schema.schema.json (implemented in
    # permea_core.diagnose). Deliberately out of scope for the postcondition, not an oversight.
    #
    # The assignment is wholesale, so a candidate arriving with its own extraction_provenance
    # -- including a forged empty `demoted` -- cannot smuggle it past. An empty list here is a
    # positive assertion by the verifier that nothing was demoted, not a default.
    stamped["extraction_provenance"] = {
        "verified": True,
        "all_spans_verbatim": True,
        "all_span_enums_valid": True,
        "spans_checked": spans_checked,
        "verifier_version": VERIFIER_VERSION,
        "demoted": records,
    }
    _check_demotion_coherence(stamped, records)
    return stamped


def _collect(
    extract_doc: dict, methods_text: str, output_language: str, demotions=()
) -> tuple[list[Violation], dict]:
    """All four gates, aggregated, never short-circuited. Returns (violations, stamped_doc).

    The single place the gates are run in order. ``write_checked`` and ``collect_violations``
    both go through here, so a document can never be judged differently depending on which
    entry point the caller used.

    Gate 4 validates the STAMPED document rather than the candidate, which is what makes the
    postcondition's guarantee total: the object validated is the object returned, so there is
    no window in which verified:true rides on a shape nobody checked.
    """
    enum_bad = _enum_violations(extract_doc)
    span_bad, spans_checked = _span_violations(extract_doc, methods_text)
    phrase_bad = _forbidden_violations(_authored_text(extract_doc), output_language)
    stamped = _stamp(extract_doc, spans_checked, demotions)
    schema_bad = _schema_violations(stamped)
    return enum_bad + span_bad + phrase_bad + schema_bad, stamped


def collect_violations(
    extract_doc: dict, methods_text: str, *, output_language: str = "korean", demotions=()
) -> list[Violation]:
    """Every postcondition violation, structured, WITHOUT raising. Empty list means it passes.

    This is what a recovery step (e.g. EXTRACT demotion) consumes: each violation names the
    field at fault and the KIND of fault, so the caller can decide per field whether the
    honest response is to abstain or to fail. Deciding that from the joined message string
    would make the recovery depend on message wording.

    The source-text precondition still RAISES ``StaleSourceError`` rather than being reported
    as a violation: spans measured against the wrong string are meaningless, so there is
    nothing here for a caller to recover from.
    """
    _check_source_text(extract_doc, methods_text)
    return _collect(extract_doc, methods_text, output_language, demotions)[0]


def stamped_if_valid(
    extract_doc: dict, methods_text: str, *, output_language: str = "korean", demotions=()
):
    """``(stamped_doc, violations)`` -- the stamped candidate and why it would be refused.

    The non-raising twin of ``write_checked`` for callers that want to inspect the document
    that WOULD be written alongside the reasons it will not be. ``violations`` empty means
    ``stamped_doc`` is exactly what ``write_checked`` returns.
    """
    _check_source_text(extract_doc, methods_text)
    violations, stamped = _collect(extract_doc, methods_text, output_language, demotions)
    return stamped, violations


def check_enum_validity(extract_doc: dict) -> None:
    v = _enum_violations(extract_doc)
    if v:
        raise ExtractionViolation(join_messages(v))


def check_span_groundedness(extract_doc: dict, methods_text: str) -> None:
    v, _ = _span_violations(extract_doc, methods_text)
    if v:
        raise ExtractionViolation(join_messages(v))


def check_forbidden_phrase(extract_doc: dict, output_language: str = "korean") -> None:
    v = _forbidden_violations(_authored_text(extract_doc), output_language)
    if v:
        raise ExtractionViolation(join_messages(v))


def write_checked(
    extract_doc: dict, methods_text: str, *, output_language: str = "korean", demotions=()
) -> dict:
    """Assert every EXTRACT postcondition gate; return the stamped document, or raise.

    Returns a stamped COPY -- the caller's document is never mutated, so a failed gate cannot
    leave a half-verified artifact behind. On any violation ``ExtractionViolation`` propagates
    and nothing is written.

    INVARIANT: a returned document is ALWAYS valid against extract.schema.json in full. Gate 4
    validates the stamped object itself, so "write_checked passed" and "this artifact is
    schema-valid" are the same statement rather than two hopes.
    """
    # Precondition, not a gate: without it the gates below would check spans against a string
    # the document was never measured on.
    _check_source_text(extract_doc, methods_text)

    # All four gates run; violations are aggregated, never short-circuited.
    violations, stamped = _collect(extract_doc, methods_text, output_language, demotions)
    if violations:
        raise ExtractionViolation(
            f"extraction failed {len(violations)} postcondition check(s): "
            + join_messages(violations)
            + "\n--- offending document ---\n"
            + json.dumps(extract_doc, ensure_ascii=False, indent=2, sort_keys=True)
        )
    return stamped


# --------------------------------------------------------------------------------------
# candidate generation -- generate, verify, DEMOTE. Never loosen.
# --------------------------------------------------------------------------------------
_TEMPERATURE = 0.0  # extraction wants determinism; NARRATE's 0.2 is for prose fluency
_MAX_TOKENS = 2000

#: Human-readable field descriptions for the prompt. Descriptive prose only -- the SCHEMA is
#: the authority and Gate 4 enforces it, so a drift here costs clarity, never correctness.
#: The enum members themselves are never listed here; they are read at runtime.
_FIELD_SPECS = (
    ("task_type", "The kind of prediction task the dataset defines. Enum."),
    ("positive_class.definition", "How the methods text defines a positive example. Free text, "
                                  "at least 10 characters."),
    ("positive_class.evidence_type", "What kind of evidence supports the positive labels. Enum."),
    ("positive_class.assays", "Named assays used to establish positives. List of strings; "
                              "null = not stated, [] = stated as none."),
    ("positive_class.provenance_ref", "Where the positives came from, as the text names it. "
                                      "String."),
    ("negative_class.construction", "How the NEGATIVE set was built. Enum. This is the field "
                                    "the audit cares about most -- read it carefully and "
                                    "abstain rather than infer."),
    ("negative_class.validated_fraction", "Fraction of negatives experimentally confirmed "
                                          "non-penetrant. Number 0..1. null = not stated, "
                                          "which is different from stated as 0."),
    ("negative_class.source_pool", "The pool the negatives were drawn from. String."),
    ("negative_class.matched_on", "Covariates the negatives were matched on. List from the "
                                  "enum; null = not stated, [] = stated as none."),
    ("negative_class.known_confounds", "Confounds the text acknowledges. List from the enum; "
                                       "null = not stated, [] = stated as none."),
    ("class_balance", "Counts of positives and negatives, as one object "
                      "{\"positive\": int, \"negative\": int}, grounded by the one sentence "
                      "that states them."),
    ("label_noise_estimate", "Estimated label error rate. Number 0..1."),
)

_FENCED = re.compile(r"\A\s*```(?:json)?\s*\n(?P<body>.*)\n\s*```\s*\Z", re.DOTALL)


class ExtractionFormatError(ExtractionViolation):
    """The model's response was not a usable document at all (not JSON, or the wrong shape).

    Separated from a content violation because the two deserve opposite responses: a malformed
    response is transport-shaped and may be retried, while a gate violation must never be.
    """


def _relative(pointer: str) -> str:
    return pointer[len("/extracted/") :]


def _expected_tree() -> dict:
    """The nested key structure the model must return, derived from ``_PROV_LEAVES``."""
    tree: dict = {}
    for pointer in _PROV_LEAVES:
        node, parts = tree, _relative(pointer).split("/")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = None
    return tree


def _skeleton() -> str:
    leaf = {"value": None, "evidence_span": None, "confidence": 0.0}

    def fill(node):
        return {k: (leaf if v is None else fill(v)) for k, v in node.items()}

    return json.dumps(fill(_expected_tree()), ensure_ascii=False, indent=2)


def _allowed_enums() -> dict:
    """The enum members, read from label_schema at call time. Never hand-copied into a prompt."""
    label_schema = _load_schema("label_schema.schema.json")
    return {
        _relative(f.pointer): _schema_enum(label_schema, f.label_ptr, "label_schema.schema.json")
        for f in _ENUM_FIELDS
    }


def _unwrap(text: str) -> str:
    """Strip at most one fenced code block. Transport de-chroming, not semantic repair."""
    match = _FENCED.match(text or "")
    return match.group("body") if match else (text or "")


def _parse_subtree(raw: str) -> dict:
    """Strict parse of the model's `extracted` subtree. No repair, no partial acceptance.

    A model that cannot emit JSON is not one whose extraction should be salvaged by guessing
    at what it meant; every failure here is loud.
    """
    try:
        subtree = json.loads(_unwrap(raw))
    except json.JSONDecodeError as exc:
        raise ExtractionFormatError(f"model response is not valid JSON: {exc}") from exc
    if not isinstance(subtree, dict):
        raise ExtractionFormatError(f"model response must be a JSON object, got {type(subtree).__name__}")

    def walk(node, expected, path):
        if set(node) != set(expected):
            missing, extra = sorted(set(expected) - set(node)), sorted(set(node) - set(expected))
            raise ExtractionFormatError(
                f"{path or 'response'}: wrong keys -- missing {missing!r}, unexpected {extra!r}"
            )
        for key, child in expected.items():
            here = f"{path}/{key}" if path else key
            value = node[key]
            if not isinstance(value, dict):
                raise ExtractionFormatError(f"{here}: expected an object, got {value!r}")
            if child is not None:
                walk(value, child, here)
            elif set(value) != {"value", "evidence_span", "confidence"}:
                raise ExtractionFormatError(
                    f"{here}: a leaf must have exactly value/evidence_span/confidence, "
                    f"got {sorted(value)!r}"
                )

    walk(subtree, _expected_tree(), "")
    return subtree


def _locate(span, methods_text: str, norm_cache: dict) -> int:
    """The RAW offset of ``span`` in ``methods_text``, or 0 if it is not there.

    Deliberately the same two-stage search Gate 2 performs, through the same helpers and the
    same index map -- so an offset produced here is one Gate 2 accepts BY CONSTRUCTION, not by
    the two agreeing. A second implementation could drift from the first, and a drifting
    normalizer fails silently.

    A span that cannot be found gets offset 0 and is left for Gate 2 to reject as
    SPAN_NOT_FOUND, which routes it into the one demotion path rather than a second one.
    """
    if not isinstance(span, str):
        return 0
    raw_hits = _find_all(methods_text, span)
    if raw_hits:
        return raw_hits[0]
    if "norm" not in norm_cache:
        norm_cache["norm"], norm_cache["map"] = _normalize_with_map(methods_text)
    hits = _find_all(norm_cache["norm"], _normalize_span(span))
    # First occurrence, deterministically. Gate 2 accepts any real occurrence; a longer quote
    # is far less likely to recur, which is why the prompt asks for a whole clause.
    return norm_cache["map"][hits[0]] if hits else 0


def _assemble(subtree: dict, dataset_card, methods_text: str, resp, prompt_sha: str) -> dict:
    """Wrap the model's subtree in the envelope extract() owns.

    THE TRUST BOUNDARY IS STRUCTURAL. The model authors value/evidence_span/confidence and
    nothing else. It never sees or writes `authoritative`, `status`, `schema`, `disclaimer`,
    `source_text_sha256`, `offset`, or `extraction_provenance` -- so there is no code path by
    which a model token reaches a field asserting non-authority or verification. A model that
    could write `authoritative` could write `true`.
    """
    norm_cache: dict = {}
    extracted = copy.deepcopy(subtree)
    for pointer in _PROV_LEAVES:
        node, parts = extracted, _relative(pointer).split("/")
        for part in parts[:-1]:
            node = node[part]
        leaf = node[parts[-1]]
        if leaf.get("value") is None:
            # The canonical abstention. Whatever the model put in evidence_span is dropped:
            # a null value fabricates no provenance (abstention_coherence).
            node[parts[-1]] = {
                "value": None, "evidence_span": None, "offset": None,
                "confidence": leaf.get("confidence"),
            }
        else:
            # Offset is COMPUTED, never taken from the model. Counting characters is among the
            # things a model is worst at, and a wrong offset is a Gate 2 violation -- trusting
            # it would manufacture failures out of readings that were correct.
            leaf["offset"] = _locate(leaf.get("evidence_span"), methods_text, norm_cache)

    schema = _load_schema("extract.schema.json")
    return {
        "schema": schema["properties"]["schema"]["const"],
        "authoritative": False,
        "status": "candidate",
        "source_text_sha256": _sha256(methods_text),
        "dataset_card": copy.deepcopy(dataset_card),
        "model": {
            "provider": resp.provider,
            "model_id": resp.model_id,
            "temperature": _TEMPERATURE,
            "prompt_sha256": prompt_sha,
        },
        "extracted": extracted,
        "disclaimer": schema["properties"]["disclaimer"]["default"],
    }


def _plan_demotions(candidate: dict, violations) -> list:
    """Partition violations into demotions and hard failures, in ONE pass.

    One pass is sufficient, not merely bounded: abstention passes Gates 1 and 2 unconditionally,
    those gates are field-local, and Gate 3 is monotone under demotion (removing authored text
    can only remove forbidden phrases, never add one). So demoting every demotable violation at
    once strictly reduces the violation set and can create no new one -- a second pass could
    find nothing the first did not, and looping would be theatre.
    """
    by_pointer: dict = {}
    hard = []
    for v in violations:
        if v.kind in DEMOTABLE_KINDS and v.pointer in _PROV_LEAVES:
            by_pointer.setdefault(v.pointer, []).append(v)
        else:
            # NOT demotable, and the exclusions are the point. enum_mirror_drift is a schema
            # divergence that abstaining would bury; leaf_missing means the model never
            # answered, and model silence is not text silence; forbidden_phrase has no pointer
            # to attribute. Demoting any of these would conceal something.
            hard.append(v)

    demotions = []
    for pointer, group in by_pointer.items():
        node, parts = candidate["extracted"], _relative(pointer).split("/")
        for part in parts[:-1]:
            node = node[part]
        leaf = node[parts[-1]]
        demotions.append(
            Demotion(
                pointer,
                tuple(group),
                leaf.get("value"),
                leaf.get("evidence_span"),
                leaf.get("confidence"),
            )
        )
        # "If you cannot ground it verbatim, you do not know it." The canonical abstention --
        # confidence reset too, because a 0.9 attached to a null would read as "90% sure it is
        # not stated", which is not what the model claimed.
        node[parts[-1]] = {
            "value": None, "evidence_span": None, "offset": None, "confidence": None,
        }
    return demotions, hard


def extract(
    dataset_card,
    methods_text: str,
    *,
    provider=None,
    output_language: str = "korean",
    max_format_retries: int = 1,
) -> dict:
    """Read a methods text into a VERIFIED candidate extraction, or raise.

    Generate with a model, verify with the postcondition, and on failure DEMOTE rather than
    loosen: a field whose reading cannot be grounded is reset to abstention -- if you cannot
    quote it, you do not know it -- and the demotion is recorded. The gate is never relaxed to
    accommodate the model.

    THE ONLY TWO OUTCOMES: a document that has ALREADY passed ``write_checked`` -- the stamped
    copy carrying the const:true receipt and the demotion list -- or an exception. There is no
    unverified return value.

    A DEMOTED RESULT IS A SUCCESS. A document where nine of twelve fields are null is a
    correct, honest report that the methods text states three things. For most published
    benchmarks that is the expected result, and it is exactly the audit signal the schema
    exists to surface -- not a degraded answer.

    ``max_format_retries`` applies to malformed responses ONLY. A gate violation is never
    retried: re-prompting a model with "that span was not found, try again" optimises it for
    producing spans that pass rather than for reading correctly, which turns the verifier into
    a training signal. Demotion is the honest recovery precisely because guessing gains
    nothing from it.
    """
    provider = provider or get_provider()
    system, user = extract_prompt.build_messages(
        dataset_card,
        methods_text,
        allowed_enums=_allowed_enums(),
        field_specs=_FIELD_SPECS,
        skeleton=_skeleton(),
    )
    prompt_sha = _sha256(system)

    last: ExtractionFormatError | None = None
    for _ in range(max(0, max_format_retries) + 1):
        resp = provider.complete(
            system, user, max_tokens=_MAX_TOKENS, temperature=_TEMPERATURE
        )
        try:
            subtree = _parse_subtree(resp.text)
            break
        except ExtractionFormatError as exc:
            last = exc  # transport-shaped: retrying cannot bias what the model claims
    else:
        raise last

    candidate = _assemble(subtree, dataset_card, methods_text, resp, prompt_sha)

    violations = collect_violations(candidate, methods_text, output_language=output_language)
    demotions, hard = _plan_demotions(candidate, violations)
    if hard:
        raise ExtractionViolation(
            f"extraction failed {len(hard)} check(s) that abstention cannot honestly repair: "
            + join_messages(hard)
        )

    # extract() SUPPLIES the demotions; write_checked RECORDS them. The trust boundary here is
    # model <-> code, not caller <-> write_checked: `demotions` is produced by this function
    # from measured Violations, at the same trust level as `methods_text`, and the model
    # cannot reach it. write_checked's pointer-resolves-to-null assertion cross-checks that
    # what is claimed here matches the document actually being stamped.
    #
    # If this still raises, the residue is by construction a hard failure -- there is nothing
    # left that demoting could honestly fix -- so it propagates.
    return write_checked(
        candidate, methods_text, output_language=output_language, demotions=demotions
    )
