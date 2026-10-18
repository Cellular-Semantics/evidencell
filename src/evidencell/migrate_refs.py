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
    load_store,
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

    if is_split_layout(refs_path):
        result.skipped = "already split"
        return result
    if not refs_path.exists():
        result.skipped = "no references.json"
        return result

    before = load_store(refs_path)
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
    # before removing the only other copy.
    if _load_split(d) != normalised_before:
        raise AssertionError(
            f"{region}: split files written but do not reload correctly; "
            f"references.json left in place. Inspect {d} before retrying."
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
