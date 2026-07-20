"""PermeaBench diagnose layer: an EvalRun in, fired warning codes out.

Pure, deterministic rule engine over an already-computed evaluation. ML-free; imports the
warning registry and reads an EvalRun's numbers, never re-running the engine.
"""

from .rules import (
    DEFAULT_HEADLINE_METRIC,
    DEFAULT_HEADLINE_MODEL,
    DEFAULT_MATERIALITY_MIN_ABS_DELTA,
    DEFAULT_MIN_CLUSTERS,
    DEFAULT_POLICY,
    Diagnosis,
    DiagnosePolicy,
    Evidence,
    FiredWarning,
    RunContext,
    SeveritySummary,
    diagnose,
)

__all__ = [
    "DEFAULT_HEADLINE_METRIC",
    "DEFAULT_HEADLINE_MODEL",
    "DEFAULT_MATERIALITY_MIN_ABS_DELTA",
    "DEFAULT_MIN_CLUSTERS",
    "DEFAULT_POLICY",
    "Diagnosis",
    "DiagnosePolicy",
    "Evidence",
    "FiredWarning",
    "RunContext",
    "SeveritySummary",
    "diagnose",
]
