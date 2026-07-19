"""Provider transport layer.

``exaone`` is implemented. ``anthropic`` and ``openai`` are declared but not implemented:
their ``complete()`` raises ``NotImplementedError``. ``get_provider`` defaults to Exaone.
"""
from __future__ import annotations

import os

from .anthropic import AnthropicProvider
from .base import Provider, ProviderResponse
from .exaone import ExaoneProvider
from .openai import OpenAIProvider

# ``__all__`` lists the implemented provider only; the unimplemented ones are still
# importable and reachable by explicit name.
__all__ = ["Provider", "ProviderResponse", "ExaoneProvider", "get_provider"]

_PROVIDERS = {
    "exaone": ExaoneProvider,
    "anthropic": AnthropicProvider,
    "openai": OpenAIProvider,
}


def get_provider(name: str | None = None) -> Provider:
    """Return a provider by name, or by env ``PERMEA_EXPLAIN_PROVIDER`` (default ``exaone``).

    Unknown or blank names fall back to Exaone. The unimplemented providers are reachable by
    explicit name; calling ``complete()`` on one raises ``NotImplementedError``.
    """
    key = name if name is not None else os.environ.get("PERMEA_EXPLAIN_PROVIDER", "exaone")
    key = (key or "").strip().lower()
    return _PROVIDERS.get(key, ExaoneProvider)()
