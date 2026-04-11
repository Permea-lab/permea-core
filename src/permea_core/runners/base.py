"""Base interfaces for benchmark execution runners."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from permea_core.benchmarks.registry import BenchmarkDefinition
from permea_core.data.contracts import DatasetRef
from permea_core.eval.metrics import MetricsSummary


@dataclass(frozen=True, slots=True)
class RunnerResult:
    """Return payload for a benchmark execution."""

    run_id: str
    prediction_artifact: str
    metrics_summary: MetricsSummary
    metadata: dict[str, Any] = field(default_factory=dict)


class BenchmarkRunner(ABC):
    """Abstract runner for reference baselines and future model implementations."""

    @abstractmethod
    def run(
        self,
        benchmark: BenchmarkDefinition,
        dataset_ref: DatasetRef,
        config_ref: str,
    ) -> RunnerResult:
        """Execute a benchmark run and return structured outputs."""
