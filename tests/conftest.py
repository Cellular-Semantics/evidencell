"""pytest configuration for evidencell tests."""


import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "integration: tests that hit external services or large local databases (OAK, network)",
    )


@pytest.fixture(autouse=True)
def _disable_llm_adjacency_by_default(monkeypatch):
    """Block live Claude calls from llm_adjacency unless a test explicitly
    re-enables them. Without this, find_candidates region-mismatch
    adjudication would hit the live API in any test that leaves the
    ANTHROPIC_API_KEY env var set.

    Tests that need to exercise the LLM path (with a mocked _call_anthropic)
    should override ANTHROPIC_API_KEY back to a fake value via monkeypatch.
    """
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
