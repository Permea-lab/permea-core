"""Metric interfaces for benchmark evaluation."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class MetricDefinition:
    """Declares a metric expected by a benchmark."""

    metric_id: str
    display_name: str
    direction: str
    description: str


@dataclass(frozen=True, slots=True)
class MetricsSummary:
    """Structured metric summary written into result artifacts.

    This is the single carrier of computed metric values across Permea Core: the card,
    run-manifest, and runner layers all reference this type, and it is populated by the
    honest-evaluation engine (``permea_core.eval.engine``) via :meth:`from_scores`. There
    is intentionally no second "metrics" implementation.
    """

    values: dict[str, float] = field(default_factory=dict)

    @classmethod
    def from_scores(
        cls, y, scores, threshold: float
    ) -> "MetricsSummary":
        """Build a summary from labels + out-of-fold scores using the engine's metrics.

        The metric set and numerics are exactly the engine's ``metrics_at`` (roc_auc,
        pr_auc, mcc, f1, balanced_acc, precision, recall). The import is deferred so that
        importing this module stays free of numpy/scikit-learn -- the card and manifest
        layers depend on ``MetricsSummary`` but must remain dependency-light.
        """
        from permea_core.eval.engine import metrics_at

        return cls(values=metrics_at(y, scores, threshold))
