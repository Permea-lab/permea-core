"""extract_prompt.py -- the prompt contract for reading a methods text into a candidate.

The mirror image of ``prompt.py``. NARRATE goes report -> prose with a closed set of numbers;
EXTRACT goes prose -> structure with a closed set of enums and a hard requirement that every
stated value be quoted verbatim from the source. Both follow the same discipline: the system
message states the rules the automatic gates will enforce, so the model is told the exact
contract it will be checked against rather than being left to guess it.

The rules are stated MECHANICALLY, not morally. The model is not asked to be humble; it is
told what will happen -- a value it cannot quote is rejected, an abstention is accepted --
because that asymmetry, not politeness, is what makes abstention the safe default.

Zero computation and zero authority: this module serializes its inputs and nothing else. The
allowed enum values are passed IN by the caller, which reads them from
``label_schema.schema.json`` at runtime with the same helpers Gate 1 uses. Hand-copying them
here would fork the review surface from the schema and, worse, would fail invisibly -- the
model would faithfully return a stale value that Gate 1 then rejects, looking like a model
fault rather than a drift bug.
"""
from __future__ import annotations

import json

PROMPT_TEMPLATE_VERSION = "permea-explain-extract-prompt/0.1"

SYSTEM_PROMPT = """\
You read a dataset's METHODS TEXT and report what it SAYS about how the dataset's labels were
constructed. You are a reader, not an expert witness. Your knowledge about blood-brain barrier
datasets is not evidence and must never appear in a value.

Your output is checked automatically before it is accepted. These are the checks.

1. EVERY STATED VALUE MUST BE QUOTED. For any field where you give a non-null value, copy an
   `evidence_span` from the methods text CHARACTER FOR CHARACTER: same case, same punctuation,
   same dashes, same spacing. Do not paraphrase, translate, tidy, correct, shorten with "...",
   or join two separate sentences into one quote. The span is located in the source by exact
   search. A span that cannot be found there is rejected.

2. ABSTAINING IS A CORRECT ANSWER. If the methods text does not state a field, return
   `value: null`. null means "the methods text does not say" -- it does not mean false, zero,
   none, or unknown-but-probably. Most methods texts do not state most of these fields, so
   most of your answers should be null.

3. GUESSING IS STRICTLY WORSE THAN ABSTAINING. A value you cannot quote is rejected and
   discarded. An abstention is accepted. There is no outcome in which a guess scores better
   than a null, so when the text does not clearly state something, return null.

4. ENUMS ARE CLOSED. For enum fields return exactly one of the listed strings, byte for byte.
   Do not invent a value, re-case one, or pick the nearest fit. If the text describes
   something that matches no listed value, return null.

5. null AND [] ARE DIFFERENT CLAIMS. For list-valued fields, null means the text does not say;
   [] means the text says there were none. Do not use one for the other.

6. QUOTE ONLY FROM THE METHODS TEXT. The dataset card tells you which dataset this is. It is
   not a source of quotes and nothing may be quoted from it.

7. DO NOT OVER-CLAIM. Report what the text says about how the data was built. Do not state or
   imply whether any peptide crosses the barrier, do not call anything fraudulent or
   deliberately fabricated, do not recommend fixes, and do not describe anything as proven.

OUTPUT FORMAT. Return ONE JSON object and nothing else -- no preamble, no commentary, no
explanation. Every field below must be present. Each leaf is exactly:

  {"value": <value or null>, "evidence_span": <verbatim quote or null>, "confidence": <0..1>}

Do not include a character offset; it is computed from your quote, not taken from you. Do not
add any other key at any level. When `value` is null, `evidence_span` must be null too."""


def _fields_block(field_specs) -> str:
    lines = []
    for pointer, description in field_specs:
        lines.append(f"- {pointer}\n    {description}")
    return "\n".join(lines)


def _allowed_values_block(allowed_enums) -> str:
    """Render the runtime enum lists. ``allowed_enums`` is {pointer: [values...]}."""
    if not allowed_enums:
        return "(no enum-typed fields)"
    lines = []
    for pointer, values in allowed_enums.items():
        rendered = ", ".join(json.dumps(v, ensure_ascii=False) for v in values)
        lines.append(f"- {pointer}\n    one of: {rendered}   (or null)")
    return "\n".join(lines)


def build_messages(dataset_card, methods_text, *, allowed_enums, field_specs, skeleton) -> tuple:
    """Return ``(system, user)``.

    The methods text is reproduced VERBATIM with no wrapper that alters characters -- no line
    numbering, no re-indentation, no fencing. Every character the model sees must be a
    character the span check can find; most span failures would otherwise be introduced by the
    presentation rather than by the model.
    """
    card = json.dumps(dataset_card, ensure_ascii=False, sort_keys=True)
    user = (
        "[DATASET CARD] -- identifies the dataset. NOT quotable; nothing here may be used as "
        "an evidence_span.\n"
        f"{card}\n\n"
        "[ALLOWED VALUES] -- the closed sets. Return one of these byte for byte, or null.\n"
        f"{_allowed_values_block(allowed_enums)}\n\n"
        "[FIELDS TO EXTRACT] -- all of them must appear in your output.\n"
        f"{_fields_block(field_specs)}\n\n"
        "[RESPONSE SKELETON] -- return exactly this shape, filled in.\n"
        f"{skeleton}\n\n"
        "[METHODS TEXT] -- the ONLY source of evidence_span quotes. Copy from it exactly.\n"
        f"{methods_text}"
    )
    return SYSTEM_PROMPT, user
