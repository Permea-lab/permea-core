"""base.py -- the provider-agnostic transport interface.

A Provider is pure transport: it takes a (system, user) message pair and returns text. It
knows nothing about Diagnosis, narration, or numeric provenance -- those live in the task
layer (``narrate.py`` today, ``extract.py`` later), which is exactly why both tasks can
share one Provider unchanged.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProviderResponse:
    """What a provider returns: the completion text plus the identity that produced it."""

    text: str
    provider: str  # provider name, e.g. "configured"
    model_id: str  # the concrete model id that was called


class Provider(ABC):
    """Turn a (system, user) prompt into text. Transport only -- no task knowledge."""

    #: short provider identifier (also the ``get_provider`` selector value)
    name: str = "base"

    @property
    @abstractmethod
    def model_id(self) -> str:
        """The concrete model id this provider is configured to call."""
        raise NotImplementedError

    @abstractmethod
    def complete(
        self,
        system: str,
        user: str,
        *,
        max_tokens: int,
        temperature: float | None = None,
        stop: list[str] | None = None,
    ) -> ProviderResponse:
        """Complete one (system, user) exchange, returning text plus model identity."""
        raise NotImplementedError
