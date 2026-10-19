#!/usr/bin/env python3
"""Merge trilaminar ASTA report quotes into references/{region}/.

Every write goes through `evidencell.references.write_quote_to_refs()`, which is
idempotent, computes the content-hashed `{corpus_id}_{sha256[:8]}` quote key, and
builds paper entries via `_build_paper_entry()` so the field shape is enforced in
code rather than by an agent's care. Do not hand-edit the store — three prior
asta-ingest pilots shipped wrong field shapes doing exactly that (see
planning/asta_ingest_lessons_sexually_dimorphic.md, planning/minirefs_author_rendering_fix.md).

The ASTA report repeats the same quote in several sections (100 instances / 33 unique
texts for this report). Duplicates collapse on the content hash; the section recorded
is that of the first occurrence.

Usage:
    python research/_drivers/merge_trilaminar_refs.py --dry-run
    python research/_drivers/merge_trilaminar_refs.py
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from evidencell.references import compute_quote_key, write_quote_to_refs  # noqa: E402

RUN_DIR = ROOT / "research" / "hippocampus" / "trilaminar_20260911"
ADDED_BY = "asta_ingest_trilaminar_20260911"
SOURCE_METHOD = "asta_report"


def build_plan(quotes: dict, catalogue: dict) -> tuple[list[dict], list[str]]:
    """Map author_key -> corpus_id and dedupe quote texts. Returns (plan, unmapped)."""
    key_to_corpus: dict[str, str] = {}
    for corpus_id, entry in catalogue.items():
        for ak in entry.get("author_keys", []):
            key_to_corpus[ak] = corpus_id

    plan: list[dict] = []
    unmapped: list[str] = []
    seen: set[tuple[str, str]] = set()

    for author_key, block in quotes.items():
        corpus_id = key_to_corpus.get(author_key)
        if corpus_id is None:
            unmapped.append(author_key)
            continue
        for q in block.get("quotes", []):
            text = q.get("text", "").strip()
            if not text:
                continue
            qk = compute_quote_key(corpus_id, text)
            if (corpus_id, qk) in seen:
                continue
            seen.add((corpus_id, qk))
            plan.append(
                {
                    "corpus_id": corpus_id,
                    "author_key": author_key,
                    "quote_key": qk,
                    "text": text,
                    "section": q.get("section") or "",
                }
            )
    return plan, unmapped


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quotes", type=pathlib.Path, default=RUN_DIR / "extracted_quotes.json")
    ap.add_argument("--catalogue", type=pathlib.Path, default=RUN_DIR / "paper_catalogue.json")
    ap.add_argument(
        "--refs", type=pathlib.Path, default=ROOT / "references" / "hippocampus"
    )
    ap.add_argument("--added-by", default=ADDED_BY)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    quotes = json.loads(args.quotes.read_text())
    catalogue = json.loads(args.catalogue.read_text())
    existing = json.loads(args.refs.read_text()) if args.refs.exists() else {}

    plan, unmapped = build_plan(quotes, catalogue)
    if unmapped:
        print(f"ERROR: {len(unmapped)} author_key(s) absent from the catalogue: {unmapped}", file=sys.stderr)
        return 2

    new_papers = sorted({p["corpus_id"] for p in plan} - set(existing))
    known_papers = sorted({p["corpus_id"] for p in plan} & set(existing))
    new_quotes = [
        p for p in plan
        if p["quote_key"] not in (existing.get(p["corpus_id"], {}).get("quotes") or {})
    ]

    total_instances = sum(len(b.get("quotes", [])) for b in quotes.values())
    print(f"reference store      : {args.refs.relative_to(ROOT)} ({len(existing) - 1} papers before)")
    print(f"quote instances      : {total_instances}")
    print(f"unique (corpus,quote): {len(plan)}")
    print(f"already present      : {len(plan) - len(new_quotes)}")
    print(f"to add               : {len(new_quotes)} quotes")
    print(f"papers new           : {len(new_papers)}  {new_papers}")
    print(f"papers already known : {len(known_papers)}  {known_papers}")

    print("\nper-paper breakdown (new quotes / unique quotes):")
    for corpus_id in sorted({p["corpus_id"] for p in plan}, key=lambda c: -len([1 for p in plan if p["corpus_id"] == c])):
        uniq = [p for p in plan if p["corpus_id"] == corpus_id]
        fresh = [p for p in uniq if p in new_quotes]
        entry = catalogue[corpus_id]
        tag = "NEW " if corpus_id in new_papers else "have"
        pmid = f"PMID:{entry['pmid']}" if entry["pmid"] else f"DOI:{entry['doi']}"
        print(f"  {tag} {corpus_id:>10s}  {len(fresh):2d}/{len(uniq):2d}  {entry['author_keys'][0]:<28s} {pmid}")

    if args.dry_run:
        print("\nDRY RUN — nothing written.")
        return 0

    written = 0
    for p in plan:
        write_quote_to_refs(
            region_dir=args.refs,
            corpus_id=p["corpus_id"],
            quote_text=p["text"],
            section=p["section"],
            source_method=SOURCE_METHOD,
            added_by=args.added_by,
            paper_meta=catalogue[p["corpus_id"]],
        )
        written += 1

    after = json.loads(args.refs.read_text())
    n_quotes = sum(len(v.get("quotes") or {}) for k, v in after.items() if k != "_meta")
    print(f"\nWrote {written} quote calls. The store now has {len(after) - 1} papers, {n_quotes} quotes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
