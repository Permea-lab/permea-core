"""Cross-layer invariant: no ACTIVE warning description may carry a numeric literal.

WHY THIS EXISTS. ``permea_explain.prompt._registry_context`` injects the title and
description of every FIRED code into the NARRATE prompt as non-numeric context, and
``prompt``'s module docstring asserts that the numeric allowed-set comes strictly from the
report's typed fields, "never from registry prose". That assertion was FALSE in practice:
W001/W002 carried "permea-eval/1.0", W101 carried "Paper 1 P1", and W501 hardcoded a "95%"
CI level. A faithful narration that translated the context it was handed therefore emitted
numbers with no report field behind them, and the number-provenance guard correctly -- but
uselessly -- withheld it. Two live runs were lost to exactly this.

The fix removed the literals; this test keeps them removed. It is deliberately a test and
not a guardrail relaxation: the guard stays strict, and we remove the CAUSE instead.

It reuses ``guardrails._standalone_number_tokens`` rather than reimplementing a number
regex, so the invariant is stated in terms of the SAME extractor that will judge the
narration at runtime. If that tokenizer changes, this test tracks it automatically and
cannot drift into checking something subtly different.

RESERVED codes are exempt: they have no firing logic, so they can never reach a prompt.
W201/W301 ("Paper 1 P2"/"P3") and W403 ("n_jobs=-1", "~1e-7") still carry literals and must
be sanitised before any of them is promoted to ACTIVE -- ``test_reserved_codes_are_the_only
_exemption`` pins that list so a promotion cannot silently skip the cleanup.
"""

from __future__ import annotations

import pytest

from permea_core.contracts.warnings import WARNINGS, Status, active
from permea_explain.guardrails import _standalone_number_tokens

#: RESERVED codes known to still carry numerals. Not a permanent exemption -- an entry here
#: is a debt to pay at promotion time, which is why the set is pinned rather than ignored.
KNOWN_NUMERIC_RESERVED = {"PERMEA-W201", "PERMEA-W301", "PERMEA-W403"}


@pytest.mark.parametrize("warning", active(), ids=lambda w: w.code)
def test_active_description_has_no_numeric_literal(warning):
    """An ACTIVE code's prompt-visible prose must contribute no numeric token.

    ``title + description`` is exactly what ``_registry_context`` puts in the prompt, so a
    token found here is a token the model may faithfully copy into a narration that then
    fails the provenance gate for a number no report field can back.
    """
    prompt_visible = f"{warning.title} {warning.description}"
    tokens = _standalone_number_tokens(prompt_visible)
    assert tokens == [], (
        f"{warning.code} is ACTIVE and its prompt-visible prose yields numeric token(s) "
        f"{tokens}. A narration that copies one cannot trace it to any report field, so the "
        f"number-provenance guard will withhold an otherwise honest narration. Rewrite the "
        f"prose without the literal (drop the version tag / citation / hardcoded level); do "
        f"not relax the guard."
    )


def test_reserved_codes_are_the_only_exemption():
    """Pin which RESERVED codes still owe a cleanup, so promoting one cannot skip it."""
    offenders = {
        w.code
        for w in WARNINGS
        if w.status is Status.RESERVED
        and _standalone_number_tokens(f"{w.title} {w.description}")
    }
    assert offenders == KNOWN_NUMERIC_RESERVED, (
        f"RESERVED codes carrying numerals changed: {offenders}. If a code was promoted to "
        f"ACTIVE, sanitise its prose first; if one was cleaned, drop it from "
        f"KNOWN_NUMERIC_RESERVED."
    )


def test_extractor_actually_bites():
    """Non-vacuity: the assertion must fail on the prose this fix removed.

    Without this, a tokenizer that returned [] for everything would make the test above pass
    silently. These are the exact literals that cost two live runs.
    """
    assert _standalone_number_tokens("Under permea-eval/1.0 it is required") == ["1.0"]
    assert _standalone_number_tokens("This is the core Paper 1 P1 finding") == ["1"]
    assert _standalone_number_tokens("The paired-bootstrap 95% CI on the delta") == ["95"]
