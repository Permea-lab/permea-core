"""The diagnose rule engine: an EvalRun in, fired warning codes out.

Reads an already-computed :class:`permea_core.eval.run.EvalRun` and fires the ACTIVE
permea-eval/1.0 warning codes (see :mod:`permea_core.contracts.warnings`), applying the
materiality thresholds the registry deliberately left as diagnose-layer policy.

Boundaries:
- This layer NEVER re-runs the engine. It consumes an EvalRun; it does not import
  ``eval.engine``/``eval.bootstrap`` and calls nothing that fits models.
- Pure Python comparison logic -- it needs neither numpy nor scikit-learn. The ``EvalRun``
  / ``MetricRow`` types are imported under ``TYPE_CHECKING`` only (read duck-typed at
  runtime), so ``import permea_core.diagnose.diagnose`` stays ML-free.
- Deterministic: same EvalRun + same DiagnosePolicy -> identical Diagnosis. No I/O, no
  randomness, no hidden state; fired warnings are emitted in fixed registry order.

CLOSED-SCHEMA SEAM: every result field is typed and sourced from the EvalRun (or the policy
threshold that fired the code). ``evidence_str`` is machine-generated from the ``Evidence``
numbers via a fixed template -- there is NO free-form text field an LLM could inject into. A
future narration layer (the configured narration provider) reads FROM a Diagnosis, never INTO it. The hook is not
built here.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import TYPE_CHECKING

from permea_core.contracts.warnings import REGISTRY, Severity

if TYPE_CHECKING:  # types only -- avoids importing the sklearn-backed engine at runtime
    from permea_core.eval.run import EvalRun, MetricRow


# --------------------------------------------------------------------------------------
# Policy (deferred materiality thresholds live here, not in the registry)
# --------------------------------------------------------------------------------------
DEFAULT_HEADLINE_MODEL = "rf"  # strongest real model (dummy/logreg are baselines)
DEFAULT_HEADLINE_METRIC = "pr_auc"  # honest discrimination metric under class imbalance
DEFAULT_MATERIALITY_MIN_ABS_DELTA = 0.02  # absolute Δ on the [0,1] metric scale
DEFAULT_MIN_CLUSTERS = 50  # tail-percentile bootstrap needs enough independent units


@dataclass(frozen=True, slots=True)
class DiagnosePolicy:
    """Overridable, closed policy. Same policy + same EvalRun -> same Diagnosis."""

    headline_model: str = DEFAULT_HEADLINE_MODEL
    headline_metric: str = DEFAULT_HEADLINE_METRIC
    materiality_min_abs_delta: float = DEFAULT_MATERIALITY_MIN_ABS_DELTA
    min_clusters: int = DEFAULT_MIN_CLUSTERS


DEFAULT_POLICY = DiagnosePolicy()


# --------------------------------------------------------------------------------------
# Closed result objects
# --------------------------------------------------------------------------------------
@dataclass(frozen=True, slots=True)
class Evidence:
    """The specific numbers that fired a warning. Every field comes from the EvalRun
    (or the policy threshold that was applied). No free-form text."""

    model: str | None = None
    metric: str | None = None
    delta_point: float | None = None
    ci_lo: float | None = None
    ci_hi: float | None = None
    ci_excludes_zero: bool | None = None
    n_clusters: int | None = None
    resample_unit: str | None = None
    headline_condition: str | None = None
    identity_definition_declared: bool | None = None
    threshold_used: float | None = None  # the policy number that made it fire (audit trail)


@dataclass(frozen=True, slots=True)
class FiredWarning:
    """One fired code, self-contained (title/severity snapshotted from the registry)."""

    code: str
    title: str
    severity: Severity
    evidence: Evidence
    evidence_str: str  # machine-generated from `evidence`, fixed template


@dataclass(frozen=True, slots=True)
class SeveritySummary:
    critical: int
    warn: int
    info: int
    total: int


@dataclass(frozen=True, slots=True)
class RunContext:
    """The input EvalRun's identity/config, echoed for interpretation + provenance."""

    representation: str
    headline_condition: str
    identity_definition: dict[str, str] | None
    resample_unit: str
    #: Confidence level of every CI in this report, as a percent (95.0). Sits beside
    #: ``resample_unit`` because both describe the bootstrap that produced the intervals, and
    #: it is run-level rather than per-warning: the level is the same whichever codes fired.
    #: Emitting it as a real number is also what lets a narration say "95% CI" -- the
    #: numeric-provenance guardrail traces every number in prose to a report field, and
    #: before this field existed there was nothing for the "95" to trace to. ``None`` when
    #: the bootstrap was skipped and no interval exists.
    ci_level_pct: float | None
    n: int
    pos: int
    neg: int
    n_clusters: int
    data_sha256: str | None


@dataclass(frozen=True, slots=True)
class Diagnosis:
    context: RunContext
    fired: tuple[FiredWarning, ...]  # deterministic registry order
    summary: SeveritySummary

    def to_dict(self) -> dict:
        """Faithful, JSON-ready serialization of this closed diagnosis.

        This dict IS the permea-eval/1.0 diagnosis contract: the narration layer (the
        configured narration provider) and the Drylab web UI read FROM it, never INTO it. Every value comes from
        this object -- nothing is added, and there is no free-form field to inject into
        (``evidence_str`` is already machine-generated from the evidence numbers). Severity
        StrEnums are emitted as their string values so the output is pure JSON scalars.
        """
        d = asdict(self)
        d["fired"] = list(d["fired"])  # asdict keeps tuples; JSON uses arrays (lists)
        for f in d["fired"]:
            f["severity"] = str(f["severity"])
        return d


# --------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------
def _fire(code: str, evidence: Evidence, evidence_str: str) -> FiredWarning:
    """Build a FiredWarning, snapshotting title/severity from the registry at fire time."""
    spec = REGISTRY[code]
    return FiredWarning(
        code=code,
        title=spec.title,
        severity=spec.severity,
        evidence=evidence,
        evidence_str=evidence_str,
    )


def _ci_label(ci_level_pct: float | None) -> str:
    """``'95% CI'`` -- the level read off the run, never a literal typed in here.

    ``:g`` renders the stored 95.0 as "95", matching how the level is spoken and how the
    guardrail tokenizes it. Falls back to a bare "CI" if no level was recorded.
    """
    return "CI" if ci_level_pct is None else f"{ci_level_pct:g}% CI"


def _headline_row(run: "EvalRun", policy: DiagnosePolicy) -> "MetricRow":
    """The (headline_model, headline_metric) row. Fail loud if absent (misconfiguration)."""
    for r in run.rows:
        if r.model == policy.headline_model and r.metric == policy.headline_metric:
            return r
    raise ValueError(
        f"headline row ({policy.headline_model!r}, {policy.headline_metric!r}) "
        f"not found in EvalRun.rows"
    )


# --------------------------------------------------------------------------------------
# The rule engine
# --------------------------------------------------------------------------------------
def diagnose(run: "EvalRun", policy: DiagnosePolicy = DEFAULT_POLICY) -> Diagnosis:
    """Read an EvalRun and fire the ACTIVE warning codes. Pure and deterministic.

    Warnings are evaluated in fixed registry order: W001, W002, W003, W101, W501, W502.
    """
    fired: list[FiredWarning] = []
    hl = _headline_row(run, policy)  # fail-loud before firing anything

    # ---- W001: identity_definition undeclared ----
    # v0 fires on `is None` only. Distinguishing "defaulted vs explicitly declared" needs a
    # future EvalRun.identity_definition_source field (same class as W403 EnvironmentUnpinned:
    # the provenance is not in the schema).
    if run.identity_definition is None:
        fired.append(
            _fire(
                "PERMEA-W001",
                Evidence(identity_definition_declared=False),
                "identity_definition not declared (None)",
            )
        )

    # ---- W002: headline condition is not B ----
    if run.headline_condition != "B":
        fired.append(
            _fire(
                "PERMEA-W002",
                Evidence(headline_condition=run.headline_condition),
                f"headline_condition = {run.headline_condition!r} (expected 'B')",
            )
        )

    # ---- W003: row-level resampling ----
    if run.resample_unit == "row":
        fired.append(
            _fire(
                "PERMEA-W003",
                Evidence(resample_unit=run.resample_unit),
                "resample_unit = 'row' (cluster is the independent unit)",
            )
        )

    # ---- W101: material similarity leakage (headline row) ----
    thr = policy.materiality_min_abs_delta
    if (
        hl.ci_excludes_zero is True
        and hl.delta_point < 0
        and abs(hl.delta_point) >= thr
    ):
        fired.append(
            _fire(
                "PERMEA-W101",
                Evidence(
                    model=hl.model,
                    metric=hl.metric,
                    delta_point=hl.delta_point,
                    ci_lo=hl.ci_lo,
                    ci_hi=hl.ci_hi,
                    ci_excludes_zero=hl.ci_excludes_zero,
                    threshold_used=thr,
                ),
                f"{hl.model}/{hl.metric}: B-A delta = {hl.delta_point:.4f}, "
                f"{_ci_label(run.ci_level_pct)} [{hl.ci_lo:.4f}, {hl.ci_hi:.4f}], "
                f"|delta| >= {thr}",
            )
        )

    # ---- W501: inconclusive delta (headline row; CI includes zero) ----
    # Scope note: v0 evaluates W501 on the headline row only, so it pairs mutually-
    # exclusively with W101. A future policy could scan all reported rows.
    if hl.ci_excludes_zero is False:
        fired.append(
            _fire(
                "PERMEA-W501",
                Evidence(
                    model=hl.model,
                    metric=hl.metric,
                    delta_point=hl.delta_point,
                    ci_lo=hl.ci_lo,
                    ci_hi=hl.ci_hi,
                    ci_excludes_zero=hl.ci_excludes_zero,
                ),
                f"{hl.model}/{hl.metric}: {_ci_label(run.ci_level_pct)} "
                f"[{hl.ci_lo:.4f}, {hl.ci_hi:.4f}] includes zero",
            )
        )

    # ---- W502: underpowered (too few clusters) ----
    if run.n_clusters < policy.min_clusters:
        fired.append(
            _fire(
                "PERMEA-W502",
                Evidence(n_clusters=run.n_clusters, threshold_used=float(policy.min_clusters)),
                f"n_clusters = {run.n_clusters} < {policy.min_clusters}",
            )
        )

    context = RunContext(
        representation=run.representation,
        headline_condition=run.headline_condition,
        identity_definition=run.identity_definition,
        resample_unit=run.resample_unit,
        ci_level_pct=run.ci_level_pct,
        n=run.n,
        pos=run.pos,
        neg=run.neg,
        n_clusters=run.n_clusters,
        data_sha256=run.data_sha256,
    )
    summary = SeveritySummary(
        critical=sum(1 for f in fired if f.severity is Severity.CRITICAL),
        warn=sum(1 for f in fired if f.severity is Severity.WARN),
        info=sum(1 for f in fired if f.severity is Severity.INFO),
        total=len(fired),
    )
    return Diagnosis(context=context, fired=tuple(fired), summary=summary)
