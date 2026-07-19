"""violations.py -- the structured violation record shared by both verification layers.

NARRATE's guardrails and EXTRACT's postcondition both answer the same question -- "what is
wrong with this candidate?" -- and both used to answer it with a bare ``list[str]``. A string
is enough to RAISE with, but not enough to ACT on: EXTRACT's demotion step has to decide, per
field, whether a violation means "this reading is ungrounded, abstain instead" or "something
is wrong that abstaining would hide". Recovering that from prose by splitting on ``": "``
would make the recovery logic depend on message wording, so the wording becomes a silent
API. This module carries the two facts the caller actually needs -- WHICH field, and WHAT
KIND -- beside the message rather than inside it.

The message text itself is unchanged and is still what gets raised, so this record is purely
additive: every ``kind`` below names a check that already existed.

TWO DISTINCTIONS THIS TYPE EXISTS TO PRESERVE. Both are cases where flattening would let a
recovery step hide something:

  * ``enum_mirror_drift`` is NOT ``enum_invalid``. Drift means label_schema and
    extract.schema.json disagree about what an enum permits -- a schema bug that has nothing
    to do with the value in hand, which may be read perfectly. Its message is prefixed with a
    field pointer like any other, so a demoter keying on the pointer alone would quietly
    convert a schema divergence into an "honest abstention". It is its own kind so that
    cannot happen by accident.

  * ``forbidden_phrase`` carries ``pointer=None``, truthfully. The phrase check scans the
    extractor's authored prose as one concatenated string and genuinely cannot say which
    field a term came from. Inventing a plausible pointer would be worse than admitting the
    gap: it would let a demoter blank a field on no evidence.
"""
from __future__ import annotations

from typing import NamedTuple


class Violation(NamedTuple):
    """One failed check.

    ``pointer`` is the JSON pointer of the FIELD at fault, or ``None`` when the check is not
    attributable to one field. For a bad element inside an array-valued field the pointer is
    the FIELD, not the element -- ``/extracted/negative_class/matched_on`` rather than
    ``.../matched_on/2`` -- because the field is the unit a caller can act on. The element
    index is still named in ``message``.

    ``message`` is exactly the text that was raised before this type existed, and is what the
    public checks still join and raise.
    """

    pointer: str | None
    kind: str
    message: str


# --- NARRATE (guardrails.py) ----------------------------------------------------------
#: A standalone number in the narration traces to no report value.
NUMERIC_UNTRACED = "numeric_untraced"
#: The narration names a PERMEA-W### code that is not in the fired set.
UNFIRED_CODE = "unfired_code"

# --- EXTRACT (extract.py) -------------------------------------------------------------
#: A non-null enum value is not a member of its enum (or is the wrong container shape).
ENUM_INVALID = "enum_invalid"
#: label_schema permits a value that extract.schema.json omits. A SCHEMA fault, not a value
#: fault -- see the module docstring. Never demotable.
ENUM_MIRROR_DRIFT = "enum_mirror_drift"
#: A required per-field-provenance leaf is absent from the document.
LEAF_MISSING = "leaf_missing"
#: A leaf is present but carries no "value" key at all.
LEAF_MISSING_VALUE = "leaf_missing_value"
#: A non-null value carries no usable evidence_span.
SPAN_MISSING_ON_NONNULL = "span_missing_on_nonnull"
#: A non-null value carries no usable offset.
OFFSET_INVALID = "offset_invalid"
#: The evidence_span is empty once whitespace-normalized.
SPAN_EMPTY = "span_empty"
#: The evidence_span does not appear in methods_text at all.
SPAN_NOT_FOUND = "span_not_found"
#: The evidence_span appears, but not at the stated offset.
SPAN_OFFSET_MISMATCH = "span_offset_mismatch"
#: The document violates extract.schema.json -- a declared type, range, length, const or
#: shape. Deliberately overlaps the enum gate: an invalid enum is also schema-invalid, and
#: both are reported. Suppressing the overlap would mean re-deriving what the other gates
#: cover, which is exactly the schema-forking this gate exists to avoid.
SCHEMA_INVALID = "schema_invalid"

# --- shared ---------------------------------------------------------------------------
#: A forbidden phrase appears in authored prose. Always ``pointer=None``.
FORBIDDEN_PHRASE = "forbidden_phrase"

#: The closed set. A kind outside this set is a bug, not a new category -- tests assert it.
KINDS = frozenset(
    {
        NUMERIC_UNTRACED,
        UNFIRED_CODE,
        ENUM_INVALID,
        ENUM_MIRROR_DRIFT,
        LEAF_MISSING,
        LEAF_MISSING_VALUE,
        SPAN_MISSING_ON_NONNULL,
        OFFSET_INVALID,
        SPAN_EMPTY,
        SPAN_NOT_FOUND,
        SPAN_OFFSET_MISMATCH,
        SCHEMA_INVALID,
        FORBIDDEN_PHRASE,
    }
)


#: The kinds a field may be DEMOTED for -- reset to abstention because its reading could not
#: be verified. The complement is deliberate and is enforced by the schema's demotion_record:
#: ``enum_mirror_drift`` is a schema divergence (demoting it would bury a schema bug as an
#: honest abstention), ``leaf_missing``/``leaf_missing_value`` mean the model never answered
#: (model silence is not text silence), and ``forbidden_phrase`` has no pointer to demote.
DEMOTABLE_KINDS = frozenset(
    {
        ENUM_INVALID,
        SPAN_NOT_FOUND,
        SPAN_EMPTY,
        SPAN_MISSING_ON_NONNULL,
        SPAN_OFFSET_MISMATCH,
        OFFSET_INVALID,
        SCHEMA_INVALID,
    }
)


class Demotion(NamedTuple):
    """A field the recovery path reset to abstention, with the reading it discarded.

    TRANSIENT. ``rejected_value`` and ``rejected_span`` are carried only so the verifier can
    CLASSIFY and HASH them; neither is ever written to the artifact. Everything in a document
    stamped verified:true is grounded or null, and a rejected span in particular is text that
    looks like a source quote and is not.
    """

    pointer: str
    violations: tuple  # the Violation records that caused it
    rejected_value: object = None
    rejected_span: object = None
    rejected_confidence: object = None


def join_messages(violations) -> str:
    """Render violations back to the exact joined text the layers have always raised."""
    return "; ".join(v.message for v in violations)
