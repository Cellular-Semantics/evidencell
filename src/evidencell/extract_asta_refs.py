"""
extract_asta_refs — parse an ASTA snippet_search JSON response and extract
candidate corpus IDs for citation traversal.

Usage (called by traversal subagent):
    echo '<json>' | uv run python -m evidencell.extract_asta_refs [--query Q] [--pretty]
    cat raw.json | uv run python -m evidencell.extract_asta_refs --pretty

Output JSON schema:
    {
      "query": "...",
      "source_papers": [            # papers that had snippets returned
        {"corpus_id": "...", "title": "...", "snippet_count": N,
         "sections_seen": ["Results", "Methods", ...]}
      ],
      "gap_papers": ["corpus_id_1", ...],   # IDs queried but with 0 snippets
      "candidate_refs": [           # all corpus IDs found anywhere in the response
        {"corpus_id": "...", "title": "...", "seen_in": "source|reference|unknown"}
      ],
      "queried_ids": [...],         # the paper_ids that were passed to snippet_search
      "total_snippets": N,
      "total_candidates": N
    }

The selection of which candidate_refs to traverse is done by the SELECTION
subagent (Opus), not here. This module is purely mechanical.
"""

from __future__ import annotations

import sys
import json
import argparse
from typing import Any


def _walk(obj: Any, visitor: "callable") -> None:
    """Depth-first walk of any JSON structure, calling visitor on every dict."""
    if isinstance(obj, dict):
        visitor(obj)
        for v in obj.values():
            _walk(v, visitor)
    elif isinstance(obj, list):
        for item in obj:
            _walk(item, visitor)


def _str_id(val: Any) -> str | None:
    """Normalise a corpus ID value to a string, or return None."""
    if val is None:
        return None
    s = str(val).strip()
    return s if s else None


def parse_snippet_response(data: dict, queried_ids: list[str] | None = None) -> dict:
    """
    Parse a raw snippet_search API response and return structured extraction.

    Works against the Semantic Scholar / ASTA snippet_search response shape:
        {"data": [{"corpusId": N, "title": "...", "snippets": [...]}, ...]}
    Falls back to recursive field extraction for other shapes.
    """
    source_papers: list[dict] = []
    candidate_map: dict[str, dict] = {}   # corpus_id → {title, seen_in}
    total_snippets = 0

    def _register_candidate(cid: str, title: str = "", seen_in: str = "unknown") -> None:
        if cid not in candidate_map:
            candidate_map[cid] = {"corpus_id": cid, "title": title, "seen_in": seen_in}

    # ── Primary parse: known Semantic Scholar shape ───────────────────────────
    items = data.get("data") or data.get("results") or []
    if isinstance(items, list):
        for item in items:
            if not isinstance(item, dict):
                continue

            # Corpus ID of the source paper
            cid = _str_id(
                item.get("corpusId") or item.get("corpus_id") or item.get("paperId")
            )
            title = item.get("title", "")
            snippets = item.get("snippets") or []

            if cid:
                _register_candidate(cid, title, seen_in="source")

            if snippets:
                total_snippets += len(snippets)
                sections_seen: set[str] = set()

                for snip in snippets:
                    if not isinstance(snip, dict):
                        continue
                    # Extract section title if present
                    sec = snip.get("section") or snip.get("sectionHeader") or {}
                    if isinstance(sec, dict):
                        sec_title = sec.get("title") or sec.get("name") or ""
                    else:
                        sec_title = str(sec)
                    if sec_title:
                        sections_seen.add(sec_title)

                    # Any referenced corpus IDs inside the snippet itself
                    def _snip_visitor(d: dict) -> None:
                        for field in ("corpusId", "corpus_id", "paperId"):
                            v = _str_id(d.get(field))
                            if v and v != cid:
                                _register_candidate(v, seen_in="reference")
                    _walk(snip, _snip_visitor)

                if cid:
                    source_papers.append({
                        "corpus_id": cid,
                        "title": title,
                        "snippet_count": len(snippets),
                        "sections_seen": sorted(sections_seen) or ["unknown"],
                    })

    # ── Fallback: sweep entire response for any corpus IDs we haven't seen ────
    def _sweep_visitor(d: dict) -> None:
        for field in ("corpusId", "corpus_id", "paperId", "CorpusId"):
            v = _str_id(d.get(field))
            if v:
                title = d.get("title", "")
                _register_candidate(v, title=title, seen_in="unknown")
    _walk(data, _sweep_visitor)

    # ── Gap papers: queried but got 0 snippets ────────────────────────────────
    source_ids = {p["corpus_id"] for p in source_papers}
    queried_ids = queried_ids or []
    gap_papers = [q for q in queried_ids if q not in source_ids]

    return {
        "source_papers": source_papers,
        "gap_papers": gap_papers,
        "candidate_refs": list(candidate_map.values()),
        "queried_ids": queried_ids,
        "total_snippets": total_snippets,
        "total_candidates": len(candidate_map),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract candidate corpus IDs from an ASTA snippet_search response."
    )
    parser.add_argument("--query", default="", help="Query string (logged in output only)")
    parser.add_argument("--queried-ids", default="", help="Comma-separated IDs that were queried")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print output JSON")
    args = parser.parse_args()

    raw = sys.stdin.read().strip()
    if not raw:
        result = {"error": "empty input", "candidate_refs": [], "total_candidates": 0}
        print(json.dumps(result, indent=2 if args.pretty else None))
        sys.exit(1)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        result = {"error": f"JSON parse error: {exc}", "candidate_refs": [], "total_candidates": 0}
        print(json.dumps(result, indent=2 if args.pretty else None))
        sys.exit(1)

    queried = [q.strip() for q in args.queried_ids.split(",") if q.strip()] if args.queried_ids else []
    result = parse_snippet_response(data, queried_ids=queried)
    result["query"] = args.query

    print(json.dumps(result, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
