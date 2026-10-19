"""One-time migration: references.json → papers/ + quotes/.

Splits each region's monolithic store into write-once identity records and
append-only quote files. `quote_key` is unchanged, so no KB YAML or report is
affected — this moves where quotes live, not what they are called.

The migration is verified rather than trusted: for every region it reloads the
store through `load_store()` and asserts the result is byte-identical to what
the monolith produced. If it is not, nothing is deleted.

    just migrate-refs-split --dry-run
    just migrate-refs-split
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

from evidencell.paths import repo_root
from evidencell.references import (
    _META_FILE,
    _PAPERS_DIR,
    _QUOTES_DIR,
    _load_split,
    _write_json,
    is_split_layout,
)


@dataclass
class RegionResult:
    region: str
    papers: int = 0
    quotes: int = 0
    skipped: str = ""


def migrate_region(refs_path: Path, *, dry_run: bool = False) -> RegionResult:
    """Split one region's references.json. Returns what was (or would be) written."""
    region = refs_path.parent.name
    result = RegionResult(region=region)

    if is_split_layout(refs_path.parent):
        result.skipped = "already split"
        return result
    if not refs_path.exists():
        result.skipped = "no references.json"
        return result

    # Read the monolith directly. load_store() is split-only now; the
    # migration is the single place that still knows the old format, which is
    # where that knowledge belongs.
    before = json.loads(refs_path.read_text(encoding="utf-8"))
    d = refs_path.parent

    papers: dict[str, dict] = {}
    quotes: dict[str, dict] = {}
    meta: dict = {}
    for corpus_id, entry in before.items():
        if corpus_id == "_meta":
            meta = entry
            continue
        if not isinstance(entry, dict):
            continue
        papers[corpus_id] = {k: v for k, v in entry.items() if k != "quotes"}
        quotes[corpus_id] = entry.get("quotes") or {}

    result.papers = len(papers)
    result.quotes = sum(len(q) for q in quotes.values())

    # A monolith with no paper entries would otherwise write no papers/ dir, so
    # is_split_layout() stays False, the verification below re-reads the
    # monolith and trivially passes, and the unlink leaves the region with no
    # store in either layout — silently disabling every provenance check for it.
    if not papers:
        result.skipped = "no paper entries — left as-is"
        return result

    if dry_run:
        return result

    # Verify BEFORE touching disk. Reconstruct what load_store() will return
    # from the split files and require it to equal the monolith. Writing first
    # and asserting afterwards leaves a proven-wrong split store shadowing an
    # intact references.json — is_split_layout() flips to True the moment
    # papers/ exists, so every later read would silently prefer the bad copy.
    reconstructed: dict = {}
    if meta:
        reconstructed["_meta"] = meta
    for corpus_id in sorted(papers):
        reconstructed[corpus_id] = {**papers[corpus_id], "quotes": quotes[corpus_id]}

    # An entry with no "quotes" key is semantically identical to one with an
    # empty dict; normalise before comparing so real data migrates instead of
    # tripping a spurious mismatch.
    normalised_before = {
        k: (v if k == "_meta" or not isinstance(v, dict) else {**v, "quotes": v.get("quotes") or {}})
        for k, v in before.items()
    }
    if reconstructed != normalised_before:
        missing = set(normalised_before) - set(reconstructed)
        extra = set(reconstructed) - set(normalised_before)
        differing = [k for k in set(normalised_before) & set(reconstructed)
                     if normalised_before[k] != reconstructed[k]]
        raise AssertionError(
            f"{region}: split would not round-trip; nothing written. "
            f"missing={sorted(missing)[:5]} extra={sorted(extra)[:5]} "
            f"differing={sorted(differing)[:5]}"
        )

    for corpus_id, payload in papers.items():
        _write_json(d / _PAPERS_DIR / f"{corpus_id}.json", payload)
    for corpus_id, payload in quotes.items():
        _write_json(d / _QUOTES_DIR / f"{corpus_id}.json", payload)
    if meta:
        _write_json(d / _META_FILE, meta)

    # Belt and braces: confirm the files on disk actually reload as expected
    # before removing the only other copy. If they do not, remove what was
    # written — leaving them would make is_split_layout() true and every later
    # read would silently prefer the bad copy over the intact monolith.
    if _load_split(d) != normalised_before:
        import shutil
        for sub in (_PAPERS_DIR, _QUOTES_DIR):
            shutil.rmtree(d / sub, ignore_errors=True)
        (d / _META_FILE).unlink(missing_ok=True)
        raise AssertionError(
            f"{region}: split files did not reload correctly; they have been "
            f"removed and references.json is untouched. Inspect {refs_path} "
            f"before retrying."
        )

    refs_path.unlink()
    return result


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="migrate-refs-split",
        description="Split references.json into papers/ + quotes/ per region.",
    )
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would be written; change nothing")
    ap.add_argument("--region", help="migrate only this region")
    args = ap.parse_args(argv)

    root = repo_root()
    refs_root = root / "references"
    if not refs_root.is_dir():
        print("No references/ directory.")
        return 0

    stores = sorted(refs_root.glob("*/references.json"))
    if args.region:
        stores = [p for p in stores if p.parent.name == args.region]
        if not stores:
            print(f"No references.json for region '{args.region}'.")
            return 1

    # Regions already split have no references.json to glob, so report them too.
    for d in sorted(p for p in refs_root.iterdir() if p.is_dir()):
        if is_split_layout(d) and not (d / "references.json").exists():
            print(f"  {d.name:<22} already split")

    total_p = total_q = 0
    failures = 0
    for refs_path in stores:
        try:
            r = migrate_region(refs_path, dry_run=args.dry_run)
        except Exception as exc:
            # Keep going: an earlier region may already be migrated, and the
            # operator needs the full picture to know which is which.
            failures += 1
            print(f"  {refs_path.parent.name:<22} FAILED — {exc}")
            continue
        if r.skipped:
            print(f"  {r.region:<22} skipped — {r.skipped}")
            continue
        verb = "would write" if args.dry_run else "wrote"
        print(f"  {r.region:<22} {verb} {r.papers} papers, {r.quotes} quotes")
        total_p += r.papers
        total_q += r.quotes

    if stores:
        verb = "Would migrate" if args.dry_run else "Migrated"
        print(f"\n{verb} {total_p} papers and {total_q} quotes "
              f"across {len(stores)} region(s).")
        if not args.dry_run:
            print("Round-trip verified; references.json removed per region.")
    if failures:
        print(f"\n{failures} region(s) FAILED — see above. "
              f"Their references.json is intact and nothing was written for them.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# ── Normalisation: bring stored records onto the schema ──────────────────────

def normalise_paper(entry: dict) -> tuple[dict, list[str]]:
    """Return (normalised entry, list of changes applied).

    Two divergences accumulated before the store had a schema, both lossless to
    correct:

    * `authors` as a list of ``{"name": ...}`` objects in dentate_gyrus, where
      every other region (and `_normalise_authors`, the canonical producer)
      stores plain strings. The objects carry no key beyond ``name``.
    * a top-level `pmcid` duplicating ``externalIds.PubMedCentral``. Every
      stored value already appears in the block, so the top-level field is
      redundant; `externalIds` is the single home for external identifiers.
    """
    changes: list[str] = []
    out = dict(entry)

    authors = out.get("authors")
    if isinstance(authors, list) and any(isinstance(a, dict) for a in authors):
        out["authors"] = [
            a.get("name", "") if isinstance(a, dict) else a for a in authors
        ]
        changes.append("authors: objects -> names")

    if "pmcid" in out:
        pmcid = out.pop("pmcid")
        if pmcid:
            ext = dict(out.get("externalIds") or {})
            if not ext.get("PubMedCentral"):
                ext["PubMedCentral"] = pmcid
                changes.append("pmcid -> externalIds.PubMedCentral")
                out["externalIds"] = ext
            else:
                changes.append("pmcid dropped (already in externalIds)")
        else:
            changes.append("pmcid dropped (empty)")

    return out, changes


def normalise_store(root: Path | None = None, *, dry_run: bool = False) -> dict:
    """Normalise every paper record in every region. Returns a change tally."""
    root = root or repo_root()
    tally: dict[str, int] = {}
    touched = 0
    for paper_file in sorted((root / "references").rglob("papers/*.json")):
        entry = json.loads(paper_file.read_text(encoding="utf-8"))
        out, changes = normalise_paper(entry)
        if not changes:
            continue
        touched += 1
        for c in changes:
            tally[c] = tally.get(c, 0) + 1
        if not dry_run:
            _write_json(paper_file, out)
    tally["_files_touched"] = touched
    return tally


# ── SourceDocument records + quote backfill ──────────────────────────────────

_SOURCES_DIR = "sources"


def _source_id(pdf_path: str) -> str:
    """Stable id for a deepsearch document, derived from its filename."""
    stem = Path(pdf_path).stem.lower()
    slug = "".join(c if c.isalnum() else "_" for c in stem)
    while "__" in slug:
        slug = slug.replace("__", "_")
    return slug.strip("_")


def build_source_documents(root: Path | None = None, *, dry_run: bool = False) -> dict:
    """Create SourceDocument records and link quotes to them.

    The link from a quote to the document it came from currently exists only as
    a naming convention: quote.added_by names a directory under research/ whose
    run_config.json may name a pdf_file. Nothing validates that chain and it is
    broken for most runs. This materialises the link that *can* be recovered as
    first-class records, and leaves the rest visibly absent rather than
    pretending the provenance exists.

    A document whose PDF was never committed is still recorded, with
    ``available: false`` — the quotes drawn from it remain attributed even
    though the document cannot be re-read.
    """
    root = root or repo_root()

    # run_id -> pdf path, from the run configs that name one
    runs: dict[str, str] = {}
    for rc in sorted((root / "research").rglob("run_config.json")):
        try:
            cfg = json.loads(rc.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if cfg.get("pdf_file"):
            runs[rc.parent.name] = cfg["pdf_file"]

    # Which regions' quotes reference each run
    docs: dict[tuple[str, str], dict] = {}
    linked = unlinked = 0
    for qfile in sorted((root / "references").rglob("quotes/*.json")):
        region = qfile.parent.parent.name
        quotes = json.loads(qfile.read_text(encoding="utf-8"))
        changed = False
        for q in quotes.values():
            run = q.get("added_by")
            pdf = runs.get(run) if run else None
            if not pdf:
                if (q.get("source_method") or "").lower() == "asta_report":
                    unlinked += 1
                continue
            sid = _source_id(pdf)
            doc = docs.setdefault((region, sid), {
                "source_id": sid,
                "path": pdf,
                "available": (root / pdf).exists(),
                "region": region,
                "runs": [],
            })
            if run not in doc["runs"]:
                doc["runs"].append(run)
            if q.get("source_document") != sid:
                q["source_document"] = sid
                changed = True
            linked += 1
        if changed and not dry_run:
            _write_json(qfile, quotes)

    if not dry_run:
        for (region, sid), doc in docs.items():
            doc["runs"] = sorted(doc["runs"])
            _write_json(root / "references" / region / _SOURCES_DIR / f"{sid}.json", doc)

    return {
        "documents": len(docs),
        "available": sum(1 for d in docs.values() if d["available"]),
        "quotes_linked": linked,
        "asta_report_quotes_unlinked": unlinked,
    }
