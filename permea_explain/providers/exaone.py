"""exaone.py -- the live Exaone provider.

Calls an OpenAI-compatible chat-completions API. Three env vars are required and none has a
default, so nothing about the deployment is baked into this source:

  PERMEA_LLM_TOKEN        API token, read from the environment only
  PERMEA_LLM_ENDPOINT_ID  deployment identifier -- this is what goes in the request's
                          ``model`` field
  PERMEA_LLM_BASE_URL     full chat-completions URL to POST to

If any is unset a live call raises: there is no silent fall back to a fake or alternative
model, because a narration that quietly came from somewhere else is worse than no narration.

Exaone is a controllable-reasoning model with reasoning ON by default. NARRATE only rephrases
numbers the engine already computed, so reasoning is switched OFF per request via
``chat_template_kwargs.enable_thinking``. ``parse_reasoning`` is left at its server-side
default (true) so no reasoning trace can reach ``content`` even if thinking were emitted.

``requests`` is imported *locally* so this module imports without the ``[explain]`` extra
installed; without it a live call surfaces a clean install hint rather than an ImportError
from somewhere unrelated.
"""
from __future__ import annotations

import os

from .base import Provider, ProviderResponse

#: Env var names. The deployment URL is configuration, not a source constant: hardcoding it
#: would put one specific deployment into every published copy of this package.
TOKEN_ENV = "PERMEA_LLM_TOKEN"
ENDPOINT_ID_ENV = "PERMEA_LLM_ENDPOINT_ID"
BASE_URL_ENV = "PERMEA_LLM_BASE_URL"

_MAX_TOKENS = 700
_TEMPERATURE = 0.2
_TIMEOUT_S = 60

_MISSING_TOKEN = (
    f"{TOKEN_ENV} is not set. The live provider reads its API token from the environment "
    f"only. Export it and retry:  export {TOKEN_ENV}=...  "
    "(narration is unavailable without it; there is no fallback provider)."
)
_MISSING_ENDPOINT = (
    f"{ENDPOINT_ID_ENV} is not set. It is the value of the request's 'model' field. Export "
    f"the deployment identifier and retry:  export {ENDPOINT_ID_ENV}=...  "
    "(there is no default and no fallback provider)."
)
_MISSING_BASE_URL = (
    f"{BASE_URL_ENV} is not set. It is the full chat-completions URL the live call POSTs to; "
    f"there is no built-in default. Export it and retry:  export {BASE_URL_ENV}=...  "
    "(narration is unavailable without it)."
)
_MISSING_EXTRA = (
    "The live provider needs the optional transport dependency. Install the extra: "
    "pip install 'permea-core[explain]'  (permea_explain itself ships without it, but a live "
    "call cannot be made)."
)


class ExaoneProvider(Provider):
    """Narrate via a live Exaone call against the configured deployment."""

    name = "exaone"

    def __init__(self, token: str | None = None, endpoint_id: str | None = None):
        # Read env at construction so selection is cheap, but validate at call time: an
        # unconfigured process must still be able to import and select the provider.
        self._token = token or os.environ.get(TOKEN_ENV)
        self._endpoint_id = endpoint_id or os.environ.get(ENDPOINT_ID_ENV)

    @property
    def model_id(self) -> str:
        """The deployment identifier -- the concrete 'model' this provider calls."""
        return self._endpoint_id or ""

    def complete(
        self,
        system: str,
        user: str,
        *,
        max_tokens: int = _MAX_TOKENS,
        temperature: float | None = _TEMPERATURE,
        stop: list[str] | None = None,
    ) -> ProviderResponse:
        if not self._token:
            raise RuntimeError(_MISSING_TOKEN)
        if not self._endpoint_id:
            raise RuntimeError(_MISSING_ENDPOINT)

        headers, payload = build_request(
            self._token,
            self._endpoint_id,
            system,
            user,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop,
        )
        text = _post(headers, payload)
        return ProviderResponse(text=text, provider=self.name, model_id=self._endpoint_id)


def build_request(
    token: str,
    endpoint_id: str,
    system: str,
    user: str,
    *,
    max_tokens: int = _MAX_TOKENS,
    temperature: float | None = _TEMPERATURE,
    stop: list[str] | None = None,
) -> tuple[dict, dict]:
    """Build the (headers, payload) for one chat completion.

    Pure: builds the request without sending it, so the wire shape is directly testable.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload: dict = {
        # 'model' carries the deployment identifier, not a model name.
        "model": endpoint_id,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_tokens": max_tokens,
        "stream": False,
        # Reasoning off: NARRATE phrases engine numbers, it does not derive anything.
        # parse_reasoning is deliberately not sent -- its default (true) keeps any trace
        # out of `content`.
        "chat_template_kwargs": {"enable_thinking": False},
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if stop:
        payload["stop"] = stop
    return headers, payload


def base_url() -> str:
    """The chat-completions URL to POST to, from the environment. Raises if unset.

    Resolved per call rather than at import so the module imports in an unconfigured process,
    matching how the token and deployment id are handled.
    """
    url = os.environ.get(BASE_URL_ENV)
    if not url:
        raise RuntimeError(_MISSING_BASE_URL)
    return url


def _post(headers: dict, payload: dict) -> str:
    """POST one non-streaming chat completion and return the assistant text."""
    try:
        import requests  # local import: only needed on the live path
    except ImportError as exc:
        raise RuntimeError(_MISSING_EXTRA) from exc

    # After the import check, so a missing extra still reports the extra rather than config.
    r = requests.post(base_url(), headers=headers, json=payload, timeout=_TIMEOUT_S)
    r.raise_for_status()
    data = r.json()
    return (data["choices"][0]["message"]["content"] or "").strip()
