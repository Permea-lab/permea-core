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
    """Structured metric summary written into result artifacts."""

    values: dict[str, float] = field(default_factory=dict)
