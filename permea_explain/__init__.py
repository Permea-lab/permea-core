"""permea_explain -- optional, opt-in, NON-AUTHORITATIVE narration layer.

Imports ``permea_core`` one-way and reads a frozen ``Diagnosis`` report; ``permea_core`` has
no knowledge of this package and offers no hook through which narration could re-enter the
evaluation record. The model NARRATES; it never COMPUTES -- every number in a narration is
verified to trace to the source report before anything is written.

This package is shipped in the same wheel as ``permea_core``. The live path (calling a model)
needs the ``permea[explain]`` extra for its transport dependencies; without the extra the
package still imports, but a live provider call surfaces a clean "install permea[explain]".
"""
from __future__ import annotations

from .extract import ExtractionViolation, StaleSourceError, write_checked
from .guardrails import GuardrailViolation, render_checked
from .narrate import narrate
from .providers import get_provider

__all__ = [
    "narrate",
    "get_provider",
    "render_checked",
    "GuardrailViolation",
    "write_checked",
    "ExtractionViolation",
    "StaleSourceError",
]
