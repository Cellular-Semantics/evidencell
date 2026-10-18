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

    quote_record = {
        "text": quote_text,
        "section": section,
        "claims": [],
        "source_method": source_method,
        "status": "pending",
        "added_by": added_by,
    }

    # Split layout: write identity and quote to their own files. Routing here
    # rather than at every call site is what lets existing callers keep working
    # unchanged — see planning/pub_store_split_followup.md for the plan to
    # retire this shim and have callers use save_paper/append_quote directly.
    if is_split_layout(refs_path):
        d = store_dir(refs_path)
        paper_file = d / _PAPERS_DIR / f"{corpus_id}.json"
        if not paper_file.exists():
            save_paper(refs_path, corpus_id, _build_paper_entry(corpus_id, paper_meta or {}))
        append_quote(refs_path, corpus_id, quote_key, quote_record)
        meta_path = d / _META_FILE
        meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
        meta.setdefault("region", d.name)
        meta["last_updated"] = datetime.now(timezone.utc).isoformat()
        meta["last_updated_by"] = added_by
        _write_json(meta_path, meta)
        return quote_key

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
        paper_entry["quotes"][quote_key] = quote_record

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


def _normalise_authors(authors) -> list[str]:
    """Normalise an authors field to list[str] of full names.

    Accepts list[str] (canonical), list[dict] (Semantic Scholar batch shape),
    or a comma-joined string with an optional 'et al.' suffix (the historical
    asta-report-ingest free-form-writer shape — see
    planning/minirefs_author_rendering_fix.md).
    """
    if not authors:
        return []
    if isinstance(authors, str):
        s = authors.strip()
        if not s:
            return []
        for suffix in (", et al.", ", et al", " et al.", " et al"):
            if s.endswith(suffix):
                s = s[: -len(suffix)].rstrip(",").rstrip()
                break
        return [part.strip() for part in s.split(",") if part.strip()]
    result: list[str] = []
    for a in authors:
        if isinstance(a, str):
            result.append(a)
        elif isinstance(a, dict):
            name = a.get("name", "")
            if name:
                result.append(name)
    return result


# ══════════════════════════════════════════════════════════════════════════════
# Split layout: papers/ + quotes/
# ══════════════════════════════════════════════════════════════════════════════
#
# The monolithic references.json conflated two things with different lifecycles:
# paper identity, written once at ingest and immutable thereafter, and quotes,
# which accumulate as successive deepsearches surface passages from the same
# paper. Holding both in one file meant every quote-adding write had the whole
# identity block in its blast radius.
#
#   references/{region}/
#     _meta.json                 region bookkeeping
#     papers/{corpus_id}.json    identity — write-once
#     quotes/{corpus_id}.json    {quote_key: quote} — append-only
#
# quote_key is unchanged ({corpus_id}_{hash}); this moves where quotes live, not
# what they are called, so no KB YAML or report needs touching.
#
# `load_store()` reads either layout and returns the legacy single-dict shape,
# so existing readers work untouched during migration. See
# planning/pub_store_split_followup.md for the plan to remove that shim.

_PAPERS_DIR = "papers"
_QUOTES_DIR = "quotes"
_META_FILE = "_meta.json"


def store_dir(refs_path: Path) -> Path:
    """Region store directory, given either layout's path.

    Accepts `references/{region}/references.json` or `references/{region}/`.
    """
    return refs_path.parent if refs_path.name == "references.json" else refs_path


def is_split_layout(refs_path: Path) -> bool:
    """True when the region has been migrated to papers/ + quotes/."""
    return (store_dir(refs_path) / _PAPERS_DIR).is_dir()


def store_exists(refs_path: Path) -> bool:
    """True when the region has a store in *either* layout.

    Readers must use this rather than `refs_path.exists()`. Every provenance
    check treats a missing store as "nothing to check" and returns [], so once
    references.json is gone a bare existence test would silently disable the
    entire anti-hallucination guard for every migrated region.
    """
    d = store_dir(refs_path)
    return (d / _PAPERS_DIR).is_dir() or (d / "references.json").exists()


def load_store(refs_path: Path) -> dict:
    """Read a region store in either layout, returning the legacy shape.

    Returns `{corpus_id: {...paper..., "quotes": {...}}, "_meta": {...}}` — what
    every current consumer expects. Returns `{}` when the region has no store.
    """
    d = store_dir(refs_path)

    if not is_split_layout(refs_path):
        legacy = d / "references.json"
        if not legacy.exists():
            return {}
        return json.loads(legacy.read_text(encoding="utf-8"))

    store: dict = {}
    meta_path = d / _META_FILE
    if meta_path.exists():
        store["_meta"] = json.loads(meta_path.read_text(encoding="utf-8"))

    quotes_dir = d / _QUOTES_DIR
    for paper_file in sorted((d / _PAPERS_DIR).glob("*.json")):
        corpus_id = paper_file.stem
        entry = json.loads(paper_file.read_text(encoding="utf-8"))
        quote_file = quotes_dir / f"{corpus_id}.json"
        entry["quotes"] = (
            json.loads(quote_file.read_text(encoding="utf-8"))
            if quote_file.exists() else {}
        )
        store[corpus_id] = entry
    return store


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def save_paper(refs_path: Path, corpus_id: str, entry: dict) -> Path:
    """Write a paper identity record. Refuses to overwrite an existing one.

    Identity is set once at ingest. A genuine correction (as with the Hochgerner
    corpus_id re-key) is a deliberate, reviewed act — it should not be reachable
    by a function whose job is adding papers.
    """
    path = store_dir(refs_path) / _PAPERS_DIR / f"{corpus_id}.json"
    if path.exists():
        raise FileExistsError(
            f"paper {corpus_id} already exists at {path}. Identity is write-once; "
            f"edit the file deliberately if a correction is genuinely needed."
        )
    payload = {k: v for k, v in entry.items() if k != "quotes"}
    payload.setdefault("corpus_id", corpus_id)
    _write_json(path, payload)
    return path


def append_quote(refs_path: Path, corpus_id: str, quote_key: str, quote: dict) -> bool:
    """Add one quote to a paper's quote file. Returns True if it was new.

    Append-only and idempotent: an existing key is left exactly as it is, so a
    later deepsearch surfacing the same passage cannot alter what is recorded.
    """
    path = store_dir(refs_path) / _QUOTES_DIR / f"{corpus_id}.json"
    quotes = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if quote_key in quotes:
        return False
    quotes[quote_key] = quote
    _write_json(path, quotes)
    return True
