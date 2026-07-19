"""anthropic.py -- declared provider slot. Not implemented.

Conforms to the ``Provider`` interface so it can be implemented later without changing the
interface; ``complete()`` raises ``NotImplementedError``.
"""
from __future__ import annotations

from .base import Provider, ProviderResponse


class AnthropicProvider(Provider):
    """Reserved slot -- conforms to the interface, not yet wired to a live model."""

    name = "anthropic"

    @property
    def model_id(self) -> str:
        return ""

    def complete(
        self,
        system: str,
        user: str,
        *,
        max_tokens: int,
        temperature: float | None = None,
        stop: list[str] | None = None,
    ) -> ProviderResponse:
        raise NotImplementedError("wired later")
