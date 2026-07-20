"""source.py -- read-only adapter over a frozen Diagnosis report.

Loads the JSON that ``permea_core``'s diagnose layer produced (``Diagnosis.to_dict()``),
hashes the frozen file, and extracts the set of numbers the report contains. This module
only ever reads: ``permea_explain`` never writes back into any ``permea_core`` type. The
arrow points one way.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def load_report(path) -> tuple[dict, str]:
    """Return ``(report_dict, sha256_hex)`` for a frozen diagnosis report file.

    The hash is over the file's raw bytes: the report is immutable, so this pins a narration
    to exactly one set of numbers, and any later edit to the report is detectably stale.
    """
    raw = Path(path).read_bytes()
    report = json.loads(raw)
    return report, hashlib.sha256(raw).hexdigest()


def collect_numbers(obj, acc: set[float] | None = None) -> set[float]:
    """Every numeric leaf in the report (int/float; booleans excluded). No rounding here.

    Precision is the guardrail's concern -- values are kept at full precision so a narration
    token can be matched at the token's own decimal precision (see ``guardrails``). Numbers
    that live only inside string leaves (e.g. the "95" in an ``evidence_str`` "95% CI", or
    that string's ``.4f`` renderings) are intentionally NOT collected: the authoritative
    numbers are the typed numeric fields, and the ``.4f`` forms of those fields are matched
    by precision, not by re-parsing prose.
    """
    if acc is None:
        acc = set()
    if isinstance(obj, bool):
        return acc
    if isinstance(obj, (int, float)):
        acc.add(float(obj))
    elif isinstance(obj, dict):
        for v in obj.values():
            collect_numbers(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            collect_numbers(v, acc)
    return acc
