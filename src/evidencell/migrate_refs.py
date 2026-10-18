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
    if dry_run:
        return result

    for corpus_id, payload in papers.items():
        _write_json(d / _PAPERS_DIR / f"{corpus_id}.json", payload)
    for corpus_id, payload in quotes.items():
        _write_json(d / _QUOTES_DIR / f"{corpus_id}.json", payload)
    if meta:
        _write_json(d / _META_FILE, meta)

    # Verify before destroying anything: the split store must reload to exactly
    # what the monolith held.
    after = load_store(refs_path)
    if after != before:
        missing = set(before) - set(after)
        extra = set(after) - set(before)
        raise AssertionError(
            f"{region}: round-trip mismatch, refusing to delete references.json. "
            f"missing={sorted(missing)[:5]} extra={sorted(extra)[:5]}"
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
    for refs_path in stores:
        r = migrate_region(refs_path, dry_run=args.dry_run)
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
