"""Resolve Semantic Scholar corpus IDs to external identifiers (PMID, DOI).

Replaces the long-standing stub. The point is to make corpus → PMID a *callable
step* rather than something an agent performs by reading a catalogue and typing
a number. See the postmortem in the commit that added this module: a
cite-traverse run resolved `CorpusId:10664418` to `PubMed: 7472426` correctly,
wrote that to `paper_catalogue_flagged.json`, and then put an unrelated PMID
(a bacteriophage genomics paper) into the KB. The resolution was never the
problem; the absence of a function to call was.

Resolution is **offline-first**, in order:

  1. `references/{region}/references.json` — the validated store, keyed by
     corpus_id with `pmid`/`doi` fields already populated by
     `references.write_quote_to_refs()`.
  2. `research/**/paper_catalogue*.json` — raw MCP batch-resolve responses.
  3. The Semantic Scholar graph API — only for corpus IDs absent from both.

Layers 1–2 need no network, so the hook, CI and headless runs resolve without
credentials. Layer 3 is best-effort: the keyless API is a shared, heavily
rate-limited pool and returns 429 under normal load, so callers must treat a
network miss as "unknown", never as "does not exist". Set `S2_API_KEY` to get a
private quota.

`verify_pmid()` is a separate question — does this PMID exist at all? That goes
to Europe PMC, which is keyless and reliable, and is what catches a fabricated
identifier that no local store would know was wrong.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from evidencell.paths import repo_root

_S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"
_S2_FIELDS = "externalIds,title,authors,year,venue"
_EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

# Where a resolution came from. Callers that enforce provenance should accept
# "references" and "catalogue" without question and treat "api" as needing to be
# written into the store before it can back a KB citation.
SOURCE_REFERENCES = "references"
SOURCE_CATALOGUE = "catalogue"
SOURCE_API = "api"


@dataclass
class Resolution:
    """What we know about one corpus ID."""

    corpus_id: str
    pmid: str = ""
    doi: str = ""
    title: str = ""
    year: str = ""
    source: str = ""

    @property
    def resolved(self) -> bool:
        return bool(self.pmid or self.doi)


@dataclass
class PmidRecord:
    """A PMID confirmed to exist, with enough metadata to judge relevance."""

    pmid: str
    title: str = ""
    authors: str = ""
    year: str = ""
    journal: str = ""


# ── layer 1: the validated reference stores ───────────────────────────────────

def _from_references(root: Path) -> dict[str, Resolution]:
    out: dict[str, Resolution] = {}
    refs_dir = root / "references"
    if not refs_dir.is_dir():
        return out
    for rf in sorted(refs_dir.rglob("references.json")):
        try:
            data = json.loads(rf.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for cid, entry in data.items():
            # `_meta` is a bookkeeping block, not a paper.
            if cid.startswith("_") or not isinstance(entry, dict):
                continue
            pmid = str(entry.get("pmid") or "")
            doi = str(entry.get("doi") or "")
            if pmid or doi:
                out.setdefault(str(cid), Resolution(
                    corpus_id=str(cid), pmid=pmid, doi=doi,
                    title=str(entry.get("title") or ""),
                    year=str(entry.get("year") or ""),
                    source=SOURCE_REFERENCES,
                ))
    return out


# ── layer 2: raw MCP batch-resolve catalogues ─────────────────────────────────

def _from_catalogues(root: Path) -> dict[str, Resolution]:
    out: dict[str, Resolution] = {}
    research = root / "research"
    if not research.is_dir():
        return out
    for cf in sorted(research.rglob("paper_catalogue*.json")):
        try:
            data = json.loads(cf.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        entries = data.get("result") if isinstance(data, dict) else data
        for e in entries or []:
            if not isinstance(e, dict):
                continue
            ext = e.get("externalIds") or {}
            cid = str(ext.get("CorpusId") or "")
            if not cid:
                continue
            out.setdefault(cid, Resolution(
                corpus_id=cid,
                pmid=str(ext.get("PubMed") or ""),
                doi=str(ext.get("DOI") or ""),
                title=str(e.get("title") or ""),
                year=str(e.get("year") or ""),
                source=SOURCE_CATALOGUE,
            ))
    return out


# ── layer 3: Semantic Scholar API (best-effort) ───────────────────────────────

def _from_api(corpus_ids: list[str], *, retries: int = 3) -> dict[str, Resolution]:
    """Batch-resolve via the S2 graph API. Returns {} on any failure.

    A failure here means "unknown", never "absent". The keyless pool commonly
    returns 429; an empty result must not be read as a missing paper.
    """
    if not corpus_ids:
        return {}
    headers = {"Content-Type": "application/json"}
    if key := os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = key

    body = json.dumps({"ids": [f"CorpusId:{c}" for c in corpus_ids]}).encode()
    url = f"{_S2_BATCH}?fields={urllib.parse.quote(_S2_FIELDS)}"

    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as fh:
                results = json.load(fh)
            break
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return {}
        except (urllib.error.URLError, OSError, json.JSONDecodeError):
            return {}
    else:
        return {}

    out: dict[str, Resolution] = {}
    for requested, r in zip(corpus_ids, results or [], strict=False):
        if not isinstance(r, dict):
            continue
        ext = r.get("externalIds") or {}
        out[str(ext.get("CorpusId") or requested)] = Resolution(
            corpus_id=str(ext.get("CorpusId") or requested),
            pmid=str(ext.get("PubMed") or ""),
            doi=str(ext.get("DOI") or ""),
            title=str(r.get("title") or ""),
            year=str(r.get("year") or ""),
            source=SOURCE_API,
        )
    return out


# ── public API ────────────────────────────────────────────────────────────────

def resolve_corpus_ids(
    corpus_ids: list[str],
    *,
    root: Path | None = None,
    allow_network: bool = True,
) -> dict[str, Resolution]:
    """Resolve corpus IDs to external identifiers, offline sources first.

    Unresolved IDs are simply absent from the returned mapping — callers must
    distinguish "not in the map" (unknown) from a Resolution with empty fields.
    """
    root = root or repo_root()
    wanted = [str(c).replace("CorpusId:", "").strip() for c in corpus_ids]
    wanted = [c for c in wanted if c]

    known = _from_references(root)
    for cid, res in _from_catalogues(root).items():
        known.setdefault(cid, res)

    out = {c: known[c] for c in wanted if c in known}

    if allow_network:
        missing = [c for c in wanted if c not in out]
        out.update(_from_api(missing))

    return out


def verify_pmid(pmid: str, *, timeout: int = 30) -> PmidRecord | None:
    """Return the Europe PMC record for `pmid`, or None if no such PMID exists.

    Raises OSError/URLError on network failure — an unreachable service must not
    be mistaken for a non-existent identifier.
    """
    q = urllib.parse.quote(f"EXT_ID:{pmid} AND SRC:MED")
    url = f"{_EPMC}?query={q}&format=json&resultType=core"
    with urllib.request.urlopen(url, timeout=timeout) as fh:
        data = json.load(fh)
    results = (data.get("resultList") or {}).get("result") or []
    if not results:
        return None
    r = results[0]
    return PmidRecord(
        pmid=str(pmid),
        title=str(r.get("title") or ""),
        authors=str(r.get("authorString") or ""),
        year=str(r.get("pubYear") or ""),
        journal=str(r.get("journalTitle") or ""),
    )


# ── CLI ───────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(
        prog="fetch-reference",
        description="Resolve Semantic Scholar corpus IDs to PMID/DOI, or verify "
                    "that a PMID exists.",
    )
    ap.add_argument("ids", nargs="*", metavar="CorpusId:NNN",
                    help="corpus IDs to resolve (with or without the CorpusId: prefix)")
    ap.add_argument("--offline", action="store_true",
                    help="local stores only; never call the Semantic Scholar API")
    ap.add_argument("--verify-pmid", metavar="PMID", action="append", default=[],
                    help="check a PMID exists in Europe PMC (repeatable)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args(argv)

    if not args.ids and not args.verify_pmid:
        ap.error("give at least one corpus ID or --verify-pmid")

    payload: dict = {}
    rc = 0

    if args.ids:
        res = resolve_corpus_ids(args.ids, allow_network=not args.offline)
        payload["resolved"] = {k: vars(v) for k, v in res.items()}
        if not args.json:
            for raw in args.ids:
                cid = str(raw).replace("CorpusId:", "").strip()
                r = res.get(cid)
                if r is None:
                    print(f"CorpusId:{cid}  UNRESOLVED "
                          f"({'offline' if args.offline else 'not found locally or via API'})")
                    rc = 1
                else:
                    ident = f"PMID:{r.pmid}" if r.pmid else (f"DOI:{r.doi}" if r.doi else "—")
                    print(f"CorpusId:{cid}  {ident}  [{r.source}]  {r.title[:60]}")

    for pmid in args.verify_pmid:
        try:
            rec = verify_pmid(pmid)
        except OSError as exc:
            print(f"PMID:{pmid}  LOOKUP FAILED ({exc}) — unknown, not disproved")
            rc = 1
            continue
        payload.setdefault("verified", {})[pmid] = vars(rec) if rec else None
        if not args.json:
            if rec is None:
                print(f"PMID:{pmid}  *** DOES NOT EXIST ***")
                rc = 1
            else:
                print(f"PMID:{pmid}  {rec.title[:70]}")
                print(f"{'':16}{rec.authors[:60]} ({rec.year}) {rec.journal[:30]}")

    if args.json:
        print(json.dumps(payload, indent=2))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
