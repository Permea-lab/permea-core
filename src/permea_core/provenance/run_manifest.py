"""Run manifest model for benchmark provenance.

The manifest is designed to be serializable into a stable repository-facing
artifact such as YAML or JSON.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from permea_core.eval.metrics import MetricsSummary


@dataclass(frozen=True, slots=True)
class ArtifactRef:
    """Reference to an output artifact produced by a benchmark run."""

    artifact_type: str
    path: str
    description: str | None = None


@dataclass(frozen=True, slots=True)
class RunManifest:
    """Canonical provenance record for a benchmark execution."""

    benchmark_id: str
    benchmark_version: str
    run_id: str
    dataset_ref: str
    code_revision: str
    config_ref: str
    execution_timestamp: str
    output_artifacts: tuple[ArtifactRef, ...] = field(default_factory=tuple)
    metrics_summary: MetricsSummary = field(default_factory=MetricsSummary)
