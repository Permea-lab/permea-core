"""Benchmark registry interfaces for Permea Core.

The registry is intentionally lightweight at this stage. It defines how
benchmarks are named, versioned, and surfaced to runners without yet
implementing persistence or dynamic discovery.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class BenchmarkDefinition:
    """Describes a benchmark task exposed by the repository."""

    benchmark_id: str
    benchmark_version: str
    title: str
    description: str
    input_schema_ref: str
    output_schema_ref: str
    metric_ids: tuple[str, ...] = field(default_factory=tuple)


class BenchmarkRegistry:
    """In-memory registry for benchmark definitions.

    This stub keeps the benchmark surface explicit while avoiding
    premature infrastructure decisions.
    """

    def __init__(self) -> None:
        self._definitions: dict[tuple[str, str], BenchmarkDefinition] = {}

    def register(self, definition: BenchmarkDefinition) -> None:
        """Register a benchmark definition by id and version."""
        key = (definition.benchmark_id, definition.benchmark_version)
        self._definitions[key] = definition

    def get(self, benchmark_id: str, benchmark_version: str) -> BenchmarkDefinition:
        """Return a benchmark definition or raise if it is missing."""
        key = (benchmark_id, benchmark_version)
        try:
            return self._definitions[key]
        except KeyError as exc:
            raise KeyError(
                f"Unknown benchmark definition: {benchmark_id}@{benchmark_version}"
            ) from exc

    def list_definitions(self) -> list[BenchmarkDefinition]:
        """Return all registered definitions in insertion order."""
        return list(self._definitions.values())
