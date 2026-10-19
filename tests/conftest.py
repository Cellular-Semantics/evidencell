"""pytest configuration for evidencell tests."""

import json
from pathlib import Path

import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "integration: tests that hit external services or large local databases (OAK, network)",
    )


def _write_store(region_dir, store):
    """Write a reference store in the split layout from a legacy-shaped dict.

    Takes `{corpus_id: {...paper..., "quotes": {...}}, "_meta": {...}}` — the
    shape fixtures were written against when the store was one file — and lays
    it out as papers/ + quotes/. Returns the region directory.

    Fixtures keep using the legacy shape because it is a compact way to express
    a store in a test; the readers under test only ever see real files.
    """
    region_dir = Path(region_dir)
    (region_dir / "papers").mkdir(parents=True, exist_ok=True)
    (region_dir / "quotes").mkdir(parents=True, exist_ok=True)
    for corpus_id, entry in store.items():
        if corpus_id == "_meta":
            (region_dir / "_meta.json").write_text(json.dumps(entry))
            continue
        if not isinstance(entry, dict):
            continue
        paper = {k: v for k, v in entry.items() if k != "quotes"}
        paper.setdefault("corpus_id", corpus_id)
        (region_dir / "papers" / f"{corpus_id}.json").write_text(json.dumps(paper))
        (region_dir / "quotes" / f"{corpus_id}.json").write_text(
            json.dumps(entry.get("quotes") or {})
        )
    return region_dir


@pytest.fixture
def write_store():
    """Fixture form of `_write_store`, for tests that build a store fixture."""
    return _write_store
