"""Utilities for reading and writing references.json quote stores.

references.json is the authoritative store for verified quotes and paper metadata.
PropertySource.quote_key values in KB YAML files must exist in references.json
before the pre-edit hook will allow the write.

The quote_key format is: {corpus_id}_{sha256[:8]} where the hash is over the
normalised quote text (lowercase + collapsed whitespace). This matches the
computation documented in workflows/asta-report-ingest.md and tested here.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def compute_quote_key(corpus_id: str, text: str) -> str:
    """Return the content-hashed quote key for a given corpus_id and quote text.

    Normalisation: lowercase + collapse all whitespace to single spaces.
    This matches the computation in asta-report-ingest.md so that quotes
    ingested by different workflows produce the same key for identical text.

    Args:
        corpus_id: Semantic Scholar numerical corpus ID (string).
        text: Verbatim quote text (will be normalised before hashing).

    Returns:
        Quote key in the form "{corpus_id}_{hash8}".
    """
    normalised = " ".join(text.lower().split())
    h = hashlib.sha256(normalised.encode()).hexdigest()[:8]
    return f"{corpus_id}_{h}"


def write_quote_to_refs(
    refs_path: Path,
    corpus_id: str,
    quote_text: str,
    section: str,
    source_method: str,
    added_by: str,
    paper_meta: dict | None = None,
) -> str:
    """Add a quote to references.json if not already present. Returns quote_key.

    Idempotent: if the quote_key already exists (same normalised text), the
    existing entry is left unchanged and the key is returned.

    If the corpus_id entry does not exist in references.json, a new paper entry
    is created using paper_meta. If paper_meta is None and the paper is not
    already in references.json, a minimal stub entry is created.

    Args:
        refs_path: Path to the region's references.json file.
        corpus_id: Semantic Scholar numerical corpus ID (string).
        quote_text: Verbatim quote text (exact substring from source).
        section: Paper section where quote was found.
        source_method: How the quote was retrieved (e.g. "asta_snippet",
            "europepmc_fulltext"). Use SourceMethod enum values from workflow_schema.
        added_by: Identifier for the workflow run adding this quote
            (e.g. "evidence_extraction_olm_hippocampus_20260421").
        paper_meta: Optional dict with paper metadata from paper_catalogue.json.
            Used to populate the paper entry if it doesn't exist yet.
            Expected keys (all optional): title, year, authors, pmid, doi,
            author_keys, resolution_confidence.

    Returns:
        The quote_key (e.g. "201041756_a3f8c291").
    """
    quote_key = compute_quote_key(corpus_id, quote_text)

    refs: dict = {}
    if refs_path.exists():
        with refs_path.open() as fh:
            refs = json.load(fh)

    # Ensure _meta exists
    if "_meta" not in refs:
        refs["_meta"] = {
            "region": refs_path.parent.name,
            "last_updated": "",
            "last_updated_by": "",
        }

    # Ensure paper entry exists
    if corpus_id not in refs:
        meta = paper_meta or {}
        refs[corpus_id] = _build_paper_entry(corpus_id, meta)

    paper_entry = refs[corpus_id]
    if "quotes" not in paper_entry:
        paper_entry["quotes"] = {}

    # Add quote if not already present (idempotent)
    if quote_key not in paper_entry["quotes"]:
        paper_entry["quotes"][quote_key] = {
            "text": quote_text,
            "section": section,
            "claims": [],
            "source_method": source_method,
            "status": "pending",
            "added_by": added_by,
        }

    # Update _meta timestamp
    refs["_meta"]["last_updated"] = datetime.now(timezone.utc).isoformat()
    refs["_meta"]["last_updated_by"] = added_by

    refs_path.parent.mkdir(parents=True, exist_ok=True)
    with refs_path.open("w") as fh:
        json.dump(refs, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    return quote_key


def _build_paper_entry(corpus_id: str, meta: dict) -> dict:
    """Build a references.json paper entry from paper_catalogue metadata."""
    # Build author_keys: ["Last et al., Year"] style
    author_keys: list[str] = meta.get("author_keys", [])
    if not author_keys:
        authors = meta.get("authors", [])
        year = meta.get("year", "")
        if authors:
            # authors may be list of strings or list of dicts with "name"
            first = authors[0]
            if isinstance(first, dict):
                first = first.get("name", "")
            last = first.split()[-1] if first else "Unknown"
            suffix = f" et al., {year}" if len(authors) > 1 else f", {year}"
            author_keys = [f"{last}{suffix}"]

    # Resolve pmid — paper_catalogue uses externalIds.PubMed
    pmid = meta.get("pmid", "")
    if not pmid:
        ext = meta.get("externalIds", {})
        pmid = str(ext.get("PubMed", "")) if ext else ""

    # Resolve doi
    doi = meta.get("doi", "")
    if not doi:
        ext = meta.get("externalIds", {})
        doi = ext.get("DOI", "") if ext else ""

    return {
        "corpus_id": corpus_id,
        "author_keys": author_keys,
        "title": meta.get("title", ""),
        "year": meta.get("year", None),
        "authors": _normalise_authors(meta.get("authors", [])),
        "pmid": pmid,
        "doi": doi,
        "resolution_confidence": meta.get("resolution_confidence", "LOW"),
        "quotes": {},
    }


def _normalise_authors(authors: list) -> list[str]:
    """Normalise authors list to list of name strings."""
    result = []
    for a in authors:
        if isinstance(a, str):
            result.append(a)
        elif isinstance(a, dict):
            result.append(a.get("name", ""))
    return result
