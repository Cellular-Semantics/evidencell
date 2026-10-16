#!/usr/bin/env python3
"""Resolve paper metadata for the trilaminar ASTA report via the Europe PMC REST API.

Reads the corpus-ID -> DOI/PMID table in reference_resolution.txt (produced
earlier from Semantic Scholar `get_paper_batch`), then queries Europe PMC for the one
field that table lacks: full author lists.

Europe PMC is used in preference to the Asta Semantic Scholar MCP because it needs no
MCP session, is re-runnable from a plain shell, and additionally returns preprint ->
published links (`commentCorrectionList`).

Writes {output_dir}/paper_catalogue.json in the shape expected by
`evidencell.references.write_quote_to_refs(paper_meta=...)`:

    {"<corpus_id>": {"corpus_id", "author_keys", "title", "year",
                     "authors", "pmid", "doi", "resolution_confidence",
                     "published_version"?}}

Usage:
    python research/_drivers/resolve_trilaminar_refs.py \
        --table research/hippocampus/trilaminar_20260911/reference_resolution.txt \
        --output-dir research/hippocampus/trilaminar_20260911
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
ROW = re.compile(r"^\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|\s*$")


def parse_table(path: pathlib.Path) -> list[dict]:
    """Extract (corpus_id, author_key, title, doi, pmid) rows from the markdown table."""
    rows = []
    for line in path.read_text().splitlines():
        m = ROW.match(line)
        if not m:
            continue
        corpus_id, citation, title, doi, pmid = (g.strip() for g in m.groups())
        # "Hewitt et al._1, 2021 (journal version)" -> "Hewitt et al._1, 2021"
        author_key = re.sub(r"\s*\([^)]*\)\s*$", "", citation).strip()
        rows.append(
            {
                "corpus_id": corpus_id,
                "author_key": author_key,
                "title_from_table": title,
                "doi": "" if doi in ("", "(none)") else doi,
                "pmid": "" if pmid in ("", "(none)") else pmid,
            }
        )
    return rows


def epmc_query(query: str) -> dict | None:
    url = f"{EPMC}?{urllib.parse.urlencode({'query': query, 'resultType': 'core', 'format': 'json'})}"
    with urllib.request.urlopen(url, timeout=30) as fh:
        payload = json.load(fh)
    results = payload.get("resultList", {}).get("result", [])
    return results[0] if results else None


def fetch(row: dict) -> dict | None:
    """Query by PMID first (authoritative), fall back to DOI (catches preprints)."""
    if row["pmid"]:
        hit = epmc_query(f'ext_id:{row["pmid"]} AND src:med')
        if hit:
            return hit
    if row["doi"]:
        return epmc_query(f'doi:"{row["doi"]}"')
    return None


def full_names(record: dict) -> list[str]:
    """Prefer 'Firstname Lastname'; fall back to Europe PMC's abbreviated fullName."""
    authors = (record.get("authorList") or {}).get("author") or []
    out: list[str] = []
    for a in authors:
        first, last = a.get("firstName"), a.get("lastName")
        out.append(f"{first} {last}" if first and last else (a.get("fullName") or "").strip())
    return [n for n in out if n]


def published_version(record: dict) -> str | None:
    """For a preprint record, return 'PMID:<id>' of the published article if EPMC links one."""
    for cc in (record.get("commentCorrectionList") or {}).get("commentCorrection") or []:
        if cc.get("type") == "Preprint of" and cc.get("id"):
            return f"PMID:{cc['id']}"
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--table", type=pathlib.Path, required=True)
    ap.add_argument("--output-dir", type=pathlib.Path, required=True)
    ap.add_argument("--sleep", type=float, default=0.34, help="Politeness delay between requests")
    args = ap.parse_args(argv)

    rows = parse_table(args.table)
    if not rows:
        print(f"ERROR: no table rows parsed from {args.table}", file=sys.stderr)
        return 2
    print(f"Parsed {len(rows)} rows from {args.table.name}")

    catalogue: dict[str, dict] = {}
    failures: list[str] = []

    for row in rows:
        rec = None
        try:
            rec = fetch(row)
        except Exception as exc:  # network/transport — report, do not guess
            print(f"  !! {row['corpus_id']} {row['author_key']}: {exc}", file=sys.stderr)
        time.sleep(args.sleep)

        if rec is None:
            failures.append(f"{row['corpus_id']} ({row['author_key']})")
            # Still emit an entry from the table so the merge can proceed with
            # an explicit LOW confidence rather than silently dropping the paper.
            catalogue[row["corpus_id"]] = {
                "corpus_id": row["corpus_id"],
                "author_keys": [row["author_key"]],
                "title": row["title_from_table"],
                "year": None,
                "authors": [],
                "pmid": row["pmid"],
                "doi": row["doi"],
                "resolution_confidence": "LOW",
            }
            print(f"  -- {row['corpus_id']:>10s}  {row['author_key']:<28s}  NOT FOUND in EPMC")
            continue

        authors = full_names(rec)
        entry = {
            "corpus_id": row["corpus_id"],
            "author_keys": [row["author_key"]],
            "title": (rec.get("title") or row["title_from_table"]).rstrip("."),
            "year": int(rec["pubYear"]) if rec.get("pubYear") else None,
            "authors": authors,
            # Trust the table's PMID/DOI (Semantic Scholar), fall back to EPMC's.
            "pmid": row["pmid"] or (rec.get("pmid") or ""),
            "doi": row["doi"] or (rec.get("doi") or ""),
            "resolution_confidence": "HIGH" if authors else "MODERATE",
        }
        pub = published_version(rec)
        if pub:
            entry["published_version"] = pub
        catalogue[row["corpus_id"]] = entry
        flag = f"  -> published as {pub}" if pub else ""
        print(f"  ok {row['corpus_id']:>10s}  {row['author_key']:<28s}  {len(authors):2d} authors{flag}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out = args.output_dir / "paper_catalogue.json"
    out.write_text(json.dumps(catalogue, indent=2, ensure_ascii=False) + "\n")

    hi = sum(1 for e in catalogue.values() if e["resolution_confidence"] == "HIGH")
    print(f"\nWrote {out} — {len(catalogue)} papers ({hi} HIGH)")
    if failures:
        print(f"UNRESOLVED ({len(failures)}): {', '.join(failures)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
