"""Antibody RRID check for the pre-edit hook (#244).

A marker's evidence may name the antibody it was detected with
(``MarkerSource.antibody``), optionally with an Antibody Registry RRID.
:func:`check_antibody_rrids` confirms every such RRID exists, via the
SciCrunch resolver. Lookups are cached in ``conf/rrid_cache.json``
(gitignored) so the check runs offline for RRIDs already seen; an uncached
RRID that can't be looked up is reported as unchecked (a soft skip, printed
by the hook), never passed silently.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterator

# Overridable for tests (e.g. an unreachable URL to exercise the soft skip).
RRID_RESOLVER_URL = os.environ.get("EVIDENCELL_RRID_URL", "https://scicrunch.org/resolver")

_MARKER_FIELDS = ("defining_markers", "negative_markers", "neuropeptides", "markers")


def rrid_cache_path() -> Path:
    """``conf/rrid_cache.json``, or ``$EVIDENCELL_RRID_CACHE``."""
    from evidencell.paths import repo_root

    override = os.environ.get("EVIDENCELL_RRID_CACHE")
    return Path(override) if override else repo_root() / "conf" / "rrid_cache.json"


def _iter_rrids(doc: dict) -> Iterator[tuple[str, str, str]]:
    """(node_id, marker name, rrid) for every antibody RRID in a KB graph."""
    for node in doc.get("nodes") or []:
        if not isinstance(node, dict):
            continue
        for key in _MARKER_FIELDS:
            for m in node.get(key) or []:
                if not isinstance(m, dict):
                    continue
                name = m.get("name_in_source") or m.get("symbol") or "?"
                for src in m.get("sources") or []:
                    ab = src.get("antibody") if isinstance(src, dict) else None
                    if isinstance(ab, dict) and ab.get("rrid"):
                        yield node.get("id", "?"), name, ab["rrid"]


def lookup_rrid(rrid: str, *, timeout: float = 20) -> dict:
    """``{"name": …}`` for a registered antibody, ``{"missing": True}`` if the
    resolver doesn't know it. Raises on network failure."""
    # SciCrunch answers 403 to urllib's default User-Agent.
    req = urllib.request.Request(
        f"{RRID_RESOLVER_URL}/{rrid}.json", headers={"User-Agent": "evidencell"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return {"missing": True}
        raise
    hits = (data.get("hits") or {}).get("hits") or []
    if not hits:
        return {"missing": True}
    item = hits[0].get("_source", {}).get("item", {})
    return {"name": item.get("name") or ""}


def check_antibody_rrids(
    doc: dict, *, cache_path: Path | None = None
) -> tuple[list[str], list[str]]:
    """Validate every antibody RRID on a KB graph's marker sources.

    Returns ``(errors, unchecked)``: ``unchecked`` lists ``"RRID: reason"``
    for RRIDs that could not be looked up (offline and not cached).
    """
    entries = list(_iter_rrids(doc))
    if not entries:
        return [], []
    path = cache_path or rrid_cache_path()
    try:
        cache: dict[str, dict] = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        cache = {}
    dirty = False
    unreachable: set[str] = set()
    for rrid in sorted({e[2] for e in entries} - set(cache)):
        try:
            cache[rrid] = lookup_rrid(rrid)
            dirty = True
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
            unreachable.add(rrid)
    if dirty:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(cache, sort_keys=True), encoding="utf-8")
        except OSError:
            pass
    errors = [
        f"{node_id}: marker {name!r} antibody {rrid} is not in the Antibody Registry "
        "(SciCrunch resolver). Use the RRID the source states, or omit rrid."
        for node_id, name, rrid in entries
        if cache.get(rrid, {}).get("missing")
    ]
    unchecked = [f"{r}: SciCrunch resolver unreachable, not cached" for r in sorted(unreachable)]
    return errors, unchecked
