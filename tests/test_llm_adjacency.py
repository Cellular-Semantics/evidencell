"""Tests for evidencell.llm_adjacency — fail-permissive LLM adjacency check
for the Stage A region filter.

These tests do not call the live Anthropic API. They patch the network call
to verify cache behaviour, fail-permissive defaults, and prompt construction.
"""

from __future__ import annotations

from unittest.mock import patch

import pytest

from evidencell.llm_adjacency import (
    _build_prompt,
    _cache_key,
    check_adjacency_batch,
)


@pytest.fixture
def isolated_cache(tmp_path, monkeypatch):
    """Redirect the SQLite cache to a temp dir so tests don't share state."""
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path))
    return tmp_path


def test_cache_key_is_sort_invariant():
    """Cache key only depends on the set of candidate regions, not the order."""
    a = _cache_key("MBA:Q", ["MBA:1", "MBA:2"])
    b = _cache_key("MBA:Q", ["MBA:2", "MBA:1"])
    assert a == b


def test_check_adjacency_batch_empty():
    """Empty candidate list returns empty verdict dict."""
    assert check_adjacency_batch("MBA:Q", []) == {}


def test_check_adjacency_batch_no_api_key_passes_through(
    isolated_cache, monkeypatch
):
    """Without an API key, all pending candidates pass (fail-permissive)."""
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    candidates = [
        {"node_id": "X", "regions": [{"id": "MBA:777", "label": "Cortex"}]},
        {"node_id": "Y", "regions": [{"id": "MBA:888", "label": "Thalamus"}]},
    ]
    result = check_adjacency_batch("MBA:CA1", candidates)
    assert result == {"X": True, "Y": True}


def test_check_adjacency_batch_uses_cache(isolated_cache, monkeypatch):
    """A second call with the same (region, candidate-regions) pair skips
    the LLM and uses the cached verdict."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "fake-key")
    candidates = [
        {"node_id": "X", "regions": [{"id": "MBA:777", "label": "near"}]},
    ]

    call_count = {"n": 0}

    def fake_call(prompt, model, max_tokens=1024):
        call_count["n"] += 1
        return {"verdicts": [{"candidate_id": "X", "adjacent": True}]}

    with patch("evidencell.llm_adjacency._call_anthropic", side_effect=fake_call):
        first = check_adjacency_batch("MBA:CA1", candidates)
        second = check_adjacency_batch("MBA:CA1", candidates)

    assert first == {"X": True}
    assert second == {"X": True}
    # Second call must be served from cache, not LLM.
    assert call_count["n"] == 1


def test_check_adjacency_batch_handles_llm_error(
    isolated_cache, monkeypatch
):
    """When the LLM call raises, all pending candidates are passed (fail-permissive)."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "fake-key")
    candidates = [
        {"node_id": "X", "regions": [{"id": "MBA:777", "label": "?"}]},
        {"node_id": "Y", "regions": [{"id": "MBA:888", "label": "?"}]},
    ]
    with patch(
        "evidencell.llm_adjacency._call_anthropic",
        side_effect=RuntimeError("network down"),
    ):
        result = check_adjacency_batch("MBA:CA1", candidates)
    assert result == {"X": True, "Y": True}


def test_check_adjacency_batch_id_based_response(isolated_cache, monkeypatch):
    """Model output keyed by candidate_id round-trips correctly."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "fake-key")
    candidates = [
        {"node_id": "X", "regions": [{"id": "MBA:777", "label": "?"}]},
        {"node_id": "Y", "regions": [{"id": "MBA:888", "label": "?"}]},
    ]
    with patch(
        "evidencell.llm_adjacency._call_anthropic",
        return_value={
            "verdicts": [
                {"candidate_id": "X", "adjacent": True},
                {"candidate_id": "Y", "adjacent": False},
            ]
        },
    ):
        result = check_adjacency_batch("MBA:CA1", candidates)
    assert result == {"X": True, "Y": False}


def test_check_adjacency_batch_partial_response(isolated_cache, monkeypatch):
    """If the LLM omits a candidate from its response, that candidate is
    passed through (default permissive)."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "fake-key")
    candidates = [
        {"node_id": "X", "regions": [{"id": "MBA:777", "label": "?"}]},
        {"node_id": "Y", "regions": [{"id": "MBA:888", "label": "?"}]},
    ]
    with patch(
        "evidencell.llm_adjacency._call_anthropic",
        return_value={
            "verdicts": [{"candidate_id": "X", "adjacent": False}]
        },
    ):
        result = check_adjacency_batch("MBA:CA1", candidates)
    assert result["X"] is False
    assert result["Y"] is True  # missing → permissive default


def test_build_prompt_lists_candidates_and_queried_label():
    """Prompt includes the queried region label and each candidate's regions."""
    prompt = _build_prompt(
        queried_region="MBA:CA1",
        queried_region_label="Field CA1",
        candidates=[
            {
                "node_id": "X",
                "regions": [{"id": "MBA:Sub", "label": "Subiculum"}],
            }
        ],
    )
    assert "Field CA1" in prompt
    assert "MBA:CA1" in prompt
    assert "Subiculum" in prompt
    assert "MBA:Sub" in prompt
    assert "X" in prompt


# NOTE: end-to-end test exercising LLM-drops-via-find_candidates removed
# in the Phase 1 follow-up. The post-loop adjudication wiring in
# find_candidates was reverted (region-mismatch is now a hard programmatic
# drop). The unit tests above still verify the llm_adjacency module
# itself, retained as dormant infrastructure for a possible Phase 2 use
# case (characterising off-target expression as adjacent vs distant for
# predicate selection).
