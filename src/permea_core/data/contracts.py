"""Typed data contracts for benchmark inputs.

These contracts define the minimum shared language between data ingestion,
benchmark assembly, and runner execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class DeliveryContext:
    """Structured delivery descriptors associated with a sequence record."""

    modality: str
    route: str | None = None
    formulation: str | None = None
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class SequenceRecord:
    """Canonical input record for sequence-first benchmark workflows."""

    record_id: str
    sequence: str
    sequence_type: str
    target_label: float | str | None = None
    delivery_context: DeliveryContext | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class DatasetRef:
    """Reference to a source or derived dataset used in a run."""

    dataset_id: str
    dataset_version: str
    location: str
    split_name: str | None = None
    manifest_ref: str | None = None
