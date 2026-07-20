"""Tests for the live Exaone provider.

Strictly offline. No test here sets a real token and none makes a network call: the wire
shape is asserted by *constructing* the request, and the one end-to-end test replaces the
transport function. A test that reached a real deployment would be a test that can fail for
reasons having nothing to do with this repo.
"""
from __future__ import annotations

import inspect
import sys
from pathlib import Path

import pytest

import permea_explain.providers.exaone as exaone_module
from permea_explain import narrate
from permea_explain.providers import get_provider
from permea_explain.providers.base import Provider, ProviderResponse
from permea_explain.providers.exaone import (
    BASE_URL_ENV,
    ENDPOINT_ID_ENV,
    TOKEN_ENV,
    ExaoneProvider,
    base_url,
    build_request,
)

from test_explain_narrate import FAITHFUL, FakeProvider, _report_file

TOKEN = "test_token_not_real"
ENDPOINT = "ep_test_endpoint_id"
BASE_URL = "https://llm.invalid/v1/chat/completions"


@pytest.fixture(autouse=True)
def _no_ambient_credentials(monkeypatch):
    """Never let real exported credentials or a real deployment URL leak into a test."""
    monkeypatch.delenv(TOKEN_ENV, raising=False)
    monkeypatch.delenv(ENDPOINT_ID_ENV, raising=False)
    monkeypatch.delenv(BASE_URL_ENV, raising=False)
    monkeypatch.delenv("PERMEA_EXPLAIN_PROVIDER", raising=False)


# --- selection ---------------------------------------------------------------------------

def test_default_provider_is_exaone():
    assert isinstance(get_provider(), ExaoneProvider)


def test_provider_selected_by_name_and_by_env(monkeypatch):
    assert isinstance(get_provider("exaone"), ExaoneProvider)
    monkeypatch.setenv("PERMEA_EXPLAIN_PROVIDER", "exaone")
    assert isinstance(get_provider(), ExaoneProvider)


def test_provider_reads_endpoint_id_from_env(monkeypatch):
    monkeypatch.setenv(ENDPOINT_ID_ENV, ENDPOINT)
    assert get_provider("exaone").model_id == ENDPOINT


def test_reserved_slots_stay_unwired():
    from permea_explain.providers.anthropic import AnthropicProvider
    from permea_explain.providers.openai import OpenAIProvider

    for cls in (AnthropicProvider, OpenAIProvider):
        with pytest.raises(NotImplementedError):
            cls().complete("s", "u", max_tokens=10)


# --- configuration errors: no silent fallback --------------------------------------------

def test_missing_token_raises_clear_error(monkeypatch):
    monkeypatch.setenv(ENDPOINT_ID_ENV, ENDPOINT)
    with pytest.raises(RuntimeError, match=f"{TOKEN_ENV} is not set"):
        ExaoneProvider().complete("s", "u", max_tokens=10)


def test_missing_endpoint_id_raises_clear_error(monkeypatch):
    monkeypatch.setenv(TOKEN_ENV, TOKEN)
    with pytest.raises(RuntimeError, match=f"{ENDPOINT_ID_ENV} is not set"):
        ExaoneProvider().complete("s", "u", max_tokens=10)


def test_missing_credentials_do_not_fall_back(monkeypatch):
    """An unconfigured provider raises rather than narrating from somewhere else."""
    with pytest.raises(RuntimeError):
        ExaoneProvider().complete("s", "u", max_tokens=10)


def test_missing_extra_raises_install_hint(monkeypatch):
    """Without the [explain] extra the live path names the extra, it does not ImportError."""
    monkeypatch.setitem(sys.modules, "requests", None)  # makes `import requests` raise
    with pytest.raises(RuntimeError, match=r"permea-core\[explain\]"):
        ExaoneProvider(token=TOKEN, endpoint_id=ENDPOINT).complete("s", "u", max_tokens=10)


# --- wire shape: constructed, never sent -------------------------------------------------

def test_request_body_is_well_formed():
    headers, payload = build_request(
        TOKEN, ENDPOINT, "SYS", "USR", max_tokens=700, temperature=0.2
    )

    assert headers["Authorization"] == f"Bearer {TOKEN}"
    assert headers["Content-Type"] == "application/json"

    # 'model' carries the deployment identifier, not a model name.
    assert payload["model"] == ENDPOINT
    assert "EXAONE" not in payload["model"]

    assert payload["messages"] == [
        {"role": "system", "content": "SYS"},
        {"role": "user", "content": "USR"},
    ]
    assert payload["max_tokens"] == 700
    assert payload["temperature"] == 0.2
    assert payload["stream"] is False


def test_reasoning_is_disabled_and_parse_reasoning_left_default():
    _, payload = build_request(TOKEN, ENDPOINT, "SYS", "USR")
    assert payload["chat_template_kwargs"] == {"enable_thinking": False}
    # Left unset so the server default (true) keeps any trace out of `content`.
    assert "parse_reasoning" not in payload


def test_base_url_is_read_from_the_environment(monkeypatch):
    """The deployment URL is configuration, never a source constant."""
    monkeypatch.setenv(BASE_URL_ENV, BASE_URL)
    assert base_url() == BASE_URL


def test_missing_base_url_raises_clear_error():
    """No built-in default: an unconfigured URL fails loudly rather than guessing one."""
    with pytest.raises(RuntimeError, match=f"{BASE_URL_ENV} is not set"):
        base_url()


def test_no_deployment_url_is_hardcoded_in_source():
    """Regression guard for the packaging leak: a published copy carries no one deployment."""
    source = Path(inspect.getsourcefile(exaone_module)).read_text(encoding="utf-8")
    assert "https://" not in source


def test_optional_fields_omitted_when_unset():
    _, payload = build_request(TOKEN, ENDPOINT, "SYS", "USR", temperature=None)
    assert "temperature" not in payload
    assert "stop" not in payload

    _, with_stop = build_request(TOKEN, ENDPOINT, "SYS", "USR", stop=["END"])
    assert with_stop["stop"] == ["END"]


def test_token_is_never_embedded_in_the_payload():
    _, payload = build_request(TOKEN, ENDPOINT, "SYS", "USR")
    assert TOKEN not in repr(payload)


# --- interface contract: NARRATE stays provider-agnostic ---------------------------------

def test_complete_signature_matches_fake_provider():
    live = inspect.signature(ExaoneProvider.complete)
    fake = inspect.signature(FakeProvider.complete)
    base = inspect.signature(Provider.complete)
    for other in (fake, base):
        assert [(p.name, p.kind) for p in live.parameters.values()] == [
            (p.name, p.kind) for p in other.parameters.values()
        ]


def test_narrate_is_unchanged_by_the_live_provider(tmp_path, monkeypatch):
    """Same Diagnosis -> same interpretation whether the text came from Fake or Exaone.

    The transport is replaced, so no request leaves the process; everything above it -- the
    guardrails and the interpretation assembly -- is the real code path.
    """
    sent = {}

    def _fake_post(headers, payload):
        sent["headers"], sent["payload"] = headers, payload
        return FAITHFUL

    monkeypatch.setattr("permea_explain.providers.exaone._post", _fake_post)
    path, _ = _report_file(tmp_path)

    live = narrate(path, provider=ExaoneProvider(token=TOKEN, endpoint_id=ENDPOINT))
    fake = narrate(path, provider=FakeProvider(FAITHFUL))

    assert isinstance(live, dict)
    assert live["model"]["provider"] == fake["model"]["provider"] == "exaone"
    assert live["model"]["model_id"] == ENDPOINT  # the endpoint id is recorded as the model
    assert live["narrative"] == fake["narrative"]
    assert live["numeric_provenance"] == fake["numeric_provenance"]
    assert live["source_report_sha256"] == fake["source_report_sha256"]
    assert live["authoritative"] is False

    # The real prompt reached the real request builder.
    assert sent["payload"]["model"] == ENDPOINT
    assert sent["payload"]["chat_template_kwargs"]["enable_thinking"] is False
    assert sent["headers"]["Authorization"] == f"Bearer {TOKEN}"


def test_provider_response_shape_is_the_shared_one():
    assert ProviderResponse(text="t", provider="exaone", model_id=ENDPOINT).provider == "exaone"
