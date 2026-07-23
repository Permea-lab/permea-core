"""guardrails.py -- post-hoc checks on any provider's narration of a Diagnosis.

The engine owns every number and every fired warning; these checks verify that a narration
never violates that, whatever provider produced it. ``render_checked`` is how the app calls
voice: it asserts all checks and returns the text, or raises so nothing downstream is
written.

  (a) numeric provenance : every standalone number in the text traces to a report value,
                           matched at the token's OWN decimal precision -- this normalizes
                           the ``evidence_str`` ``.4f`` vs raw-float ``evidence`` mismatch
                           (a "-0.0500" in prose matches a -0.05 typed field). Thousands
                           separators are stripped before tokenizing, so a group-formatted
                           "2,959" is read as the one number it denotes.
  (b) forbidden-phrase   : no over-claim -- (i) unbacked causation/biology, (ii) escalating
                           a WARN to certainty/fraud, (iii) invented remediation, (iv)
                           authority words. Korean + English.
  (c) fidelity           : the narration names no PERMEA-W### code that is not in ``fired``.

Lifted from drylab ``voice/guardrails.py``: the identifier-token strip, ``render_checked``,
``GuardrailViolation``, and the recursive number collector (retargeted to a report, now in
``source.collect_numbers``). The precision-aware matching, the Diagnosis-domain forbidden
list, and the fidelity check are new / rewritten for this layer.

Severity distortion (a WARN narrated as certainty/fraud) is guarded by forbidden-phrase
category (ii) rather than by free-text severity-word scanning: scanning bare words like
"warning"/"경고" false-positives on faithful negations such as "no warnings were raised",
and rejecting a faithful narration is a worse failure here than the miss.
"""
from __future__ import annotations

import re

from . import source
from .violations import (
    FORBIDDEN_PHRASE,
    NUMERIC_UNTRACED,
    UNFIRED_CODE,
    Violation,
    join_messages,
)

VERIFIER_VERSION = "permea-explain-narrate-guardrails/0.1"

# A standalone signed integer or decimal. The leading sign is captured so a negative field
# (e.g. delta_point = -0.05) is matched with its sign, not as its absolute value.
_NUM_TOKEN = re.compile(r"-?\d+(?:\.\d+)?")

# Identifier-like tokens (PERMEA-W101, ref_b58ee4, physchem_rf, the hex of a data_sha256):
# digits inside them are part of an opaque reference, not numeric facts, so strip identifiers
# before reading standalone numbers. A maximal run of [A-Za-z0-9_] is blanked WHOLE whenever
# it carries a letter or underscore, so its digits go whether they LEAD or TRAIL the letters:
# "PERMEA-W101" -> "PERMEA" and "W101" both vanish (101 never read), and a digit-first hash
# "41dba61b...8004d" vanishes entire (the leading 41 never read). A pure-digit run carries no
# letter and is left for the number tokenizer, unchanged.
#
# The earlier form, [A-Za-z_][A-Za-z0-9_]*, required the run to START on a letter/underscore.
# That blanked trailing digits ("abc42" whole) but not leading ones ("42abc" left "42"), so a
# sha256 that began with hex digits left those digits behind as a bare, untraceable number and
# false-failed a narration that faithfully quoted the hash. Blanking is now symmetric.
_ALNUM_RUN = re.compile(r"[A-Za-z0-9_]+")
_HAS_LETTER_OR_UNDERSCORE = re.compile(r"[A-Za-z_]")

_WCODE = re.compile(r"PERMEA-W[0-9]{3}")

# Thousands separators. "2,959" and 2959 are the same number, but the number tokenizer above
# splits at the comma and reads "2" and "959", neither of which traces -- so a narration that
# group-formatted a count correctly got rejected. The commas are stripped before tokenizing,
# and ONLY when they form real 3-digit groups:
#   (?<![\d.,])      not glued to a preceding number, so "0.05,100" is two numbers, not 05100
#   \d{1,3}(?:,\d{3})+   1-3 digits then one or more exact 3-digit groups
#   (?!,?\d)         no 4th digit and no short trailing group, so "1,2345" and "1,234,56"
#                    are left malformed and still fail
# This is a decimal-point convention, never a decimal comma: "." separates the fraction (the
# report emits .4f forms like -0.0500) and "," only ever groups. A comma is therefore never
# read as a decimal point, and two distinct numbers are never merged into one.
_THOUSANDS_GROUPED = re.compile(r"(?<![\d.,])(\d{1,3}(?:,\d{3})+)(?!,?\d)")


class GuardrailViolation(AssertionError):
    """Raised when a narration violates the voice contract. Nothing is written on raise."""


# --------------------------------------------------------------------------------------
# (a) numeric provenance -- precision-aware
# --------------------------------------------------------------------------------------
def _strip_thousands_separators(text: str) -> str:
    """Join validly grouped digits: "2,959" -> "2959". Anything else is left alone."""
    return _THOUSANDS_GROUPED.sub(lambda m: m.group(1).replace(",", ""), text)


def _blank_identifiers(text: str) -> str:
    """Blank every [A-Za-z0-9_] run that carries a letter or underscore, whole.

    A pure-digit run denotes a number and is left in place; a run that also holds a letter or
    underscore is an opaque identifier (a warning code, a column name, a hash) and is removed
    entirely -- leading digits included, so a digit-first hash leaves nothing behind."""
    return _ALNUM_RUN.sub(
        lambda m: " " if _HAS_LETTER_OR_UNDERSCORE.search(m.group(0)) else m.group(0),
        text,
    )


def _standalone_number_tokens(text: str) -> list[str]:
    """Numeric tokens that stand alone -- NOT digit runs inside an identifier.

    Grouping commas are removed first, so a group-formatted count is assembled into the one
    number it denotes. This changes only how a token is ASSEMBLED from the prose; what counts
    as a match against the report is unchanged.
    """
    without_ids = _blank_identifiers(_strip_thousands_separators(text))
    return _NUM_TOKEN.findall(without_ids)


def _token_decimals(tok: str) -> int:
    return len(tok.split(".", 1)[1]) if "." in tok else 0


def _provenance_violations(text: str, report: dict) -> list[Violation]:
    """A narration is prose, not a document, so no violation here has a field pointer."""
    allowed = source.collect_numbers(report)
    bad: list[Violation] = []
    for tok in _standalone_number_tokens(text):
        k = _token_decimals(tok)
        val = round(float(tok), k)
        # Traced iff some source value, rounded to the token's own precision, equals it.
        # A 4-decimal "-0.0500" matches a -0.05 field; a fabricated "0.73" matches nothing.
        if not any(round(s, k) == val for s in allowed):
            bad.append(
                Violation(
                    None,
                    NUMERIC_UNTRACED,
                    f"numeric token {tok!r} does not trace to any report value",
                )
            )
    return bad


# --------------------------------------------------------------------------------------
# (b) forbidden-phrase -- Diagnosis domain (a conservative, reviewed seed)
# --------------------------------------------------------------------------------------
# Deliberately narrow: each phrase is a clear over-claim unlikely in a faithful narration,
# to catch the bad without false-failing good output. The list grows as narrations are
# reviewed. Categories: (i) causation/biology, (ii) certainty/fraud escalation,
# (iii) invented remediation, (iv) authority words.
_FORBIDDEN_EN = (
    # (i) unbacked causation / biology -- this report is about evaluation validity, not
    #     whether a given peptide crosses the barrier
    "will cross",
    "will not cross",
    "penetration probability",
    "chance of crossing",
    # (ii) escalating a finding to certainty / fraud
    "is fraud",
    "is fraudulent",
    "deliberately fabricated",
    # (iii) inventing remediation the report does not state
    "we recommend",
    "you should",
    "to fix this",
    # (iv) authority words
    "scientifically proven",
    "conclusively proven",
    "hereby confirmed",
)
_FORBIDDEN_KO = (
    # (i)
    "통과할 것",
    "통과하지 않을 것",
    "침투 확률",
    "투과 확률",
    # (ii)
    "조작이다",
    "조작되었다",
    "사기이다",
    # (iii)
    "권장합니다",
    "권장한다",
    "해결하려면",
    # (iv)
    "과학적으로 입증",
    "확정적으로 입증",
)


def _forbidden_terms(output_language: str) -> tuple[str, ...]:
    lang = (output_language or "").strip().lower()
    terms = _FORBIDDEN_EN
    if lang in ("korean", "ko"):
        terms = terms + _FORBIDDEN_KO
    return terms


def _forbidden_violations(text: str, output_language: str) -> list[Violation]:
    """``pointer`` is None by necessity: the scan sees one concatenated string, so it cannot
    say which field a term came from. EXTRACT reuses this check unchanged and inherits that
    honestly -- see the note in ``violations``."""
    low = text.lower()
    return [
        Violation(None, FORBIDDEN_PHRASE, f"forbidden phrase present: {term!r}")
        for term in _forbidden_terms(output_language)
        if term.lower() in low
    ]


# --------------------------------------------------------------------------------------
# (c) fidelity -- no fabricated warning codes
# --------------------------------------------------------------------------------------
def _fidelity_violations(text: str, report: dict) -> list[Violation]:
    fired_codes = {f.get("code") for f in report.get("fired", [])}
    return [
        Violation(
            None, UNFIRED_CODE, f"narration names {code!r}, which is not in the fired set"
        )
        for code in _WCODE.findall(text)
        if code not in fired_codes
    ]


# --------------------------------------------------------------------------------------
# public surface
# --------------------------------------------------------------------------------------
def numbers_in_narrative(text: str) -> list[str]:
    """Every standalone numeric literal extracted from the narration (for the receipt)."""
    return _standalone_number_tokens(text)


def collect_violations(
    text: str, report: dict, *, output_language: str = "korean"
) -> list[Violation]:
    """Every guardrail violation, structured, WITHOUT raising. Empty list means the narration
    passes. ``render_checked`` is this function plus the raise, so the two can never disagree
    about what counts as a violation."""
    return (
        _provenance_violations(text, report)
        + _forbidden_violations(text, output_language)
        + _fidelity_violations(text, report)
    )


def check_number_provenance(text: str, report: dict) -> None:
    v = _provenance_violations(text, report)
    if v:
        raise GuardrailViolation(join_messages(v))


def check_forbidden_phrase(text: str, output_language: str = "korean") -> None:
    v = _forbidden_violations(text, output_language)
    if v:
        raise GuardrailViolation(join_messages(v))


def check_fidelity(text: str, report: dict) -> None:
    v = _fidelity_violations(text, report)
    if v:
        raise GuardrailViolation(join_messages(v))


def render_checked(text: str, report: dict, *, output_language: str = "korean") -> str:
    """Assert all guardrails on ``text`` against ``report``; return it, or raise on any violation."""
    violations = collect_violations(text, report, output_language=output_language)
    if violations:
        raise GuardrailViolation(
            f"narration failed {len(violations)} guardrail check(s): "
            + join_messages(violations)
            + f"\n--- offending output ---\n{text}"
        )
    return text
