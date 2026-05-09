"""LLM-backed adjacency check for the Stage A region filter.

When find_candidates' programmatic region filter would drop a candidate that
has annotated regions but none in the queried region, this module gets a
"closely associated?" verdict from a small Claude model. Claude Haiku 4.5
is the default — it knows brain anatomy adjacency well enough to handle
cases like CA1 ↔ subiculum where the MBA hierarchy says "siblings" but the
biology is closer.

Failure-permissive by design: if the API key is missing, the network is down,
or the model errors out, the function returns ``True`` for all candidates so
they pass through. Callers can re-impose the strict drop by checking
``adjudicated_with_llm`` in the return dict if they want to.

Verdicts are cached in a small SQLite store at
``$XDG_CACHE_HOME/evidencell/llm_adjacency.db`` (default
``~/.cache/evidencell/...``) keyed on the (queried_region, sorted-candidate-
regions) tuple. Cache hits skip the LLM entirely.
"""

from __future__ import annotations

import json
import logging
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

log = logging.getLogger(__name__)


_DEFAULT_MODEL = "claude-haiku-4-5"
_CACHE_FILENAME = "llm_adjacency.db"
_CACHE_DDL = """\
CREATE TABLE IF NOT EXISTS adjacency_cache (
    cache_key TEXT PRIMARY KEY,
    queried_region TEXT NOT NULL,
    candidate_regions_json TEXT NOT NULL,
    verdict INTEGER NOT NULL,
    cached_at TEXT NOT NULL
);
"""


def _cache_dir() -> Path:
    """Return the cache directory, creating it if needed."""
    base = os.environ.get("XDG_CACHE_HOME") or str(Path.home() / ".cache")
    d = Path(base) / "evidencell"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _cache_key(queried_region: str, candidate_regions: list[str]) -> str:
    """Build the cache key from a queried region and candidate region set."""
    sorted_cands = sorted(candidate_regions)
    return f"{queried_region}||{','.join(sorted_cands)}"


def _open_cache() -> sqlite3.Connection:
    """Open (creating if needed) the adjacency-verdict cache database."""
    path = _cache_dir() / _CACHE_FILENAME
    con = sqlite3.connect(path)
    con.executescript(_CACHE_DDL)
    return con


def _cache_lookup(
    queried_region: str, candidates: list[dict]
) -> dict[str, bool | None]:
    """Look up cached verdicts. Returns ``{node_id: bool | None}`` where
    ``None`` means cache miss."""
    out: dict[str, bool | None] = {}
    if not candidates:
        return out
    con = _open_cache()
    try:
        for c in candidates:
            regions = sorted(c.get("region_ids") or [])
            key = _cache_key(queried_region, regions)
            row = con.execute(
                "SELECT verdict FROM adjacency_cache WHERE cache_key = ?",
                (key,),
            ).fetchone()
            out[c["node_id"]] = bool(row[0]) if row is not None else None
    finally:
        con.close()
    return out


def _cache_store(
    queried_region: str, candidates: list[dict], verdicts: dict[str, bool]
) -> None:
    """Persist verdicts for cache misses."""
    if not verdicts:
        return
    con = _open_cache()
    try:
        ts = datetime.now(tz=timezone.utc).isoformat()
        for c in candidates:
            nid = c["node_id"]
            if nid not in verdicts:
                continue
            regions = sorted(c.get("region_ids") or [])
            key = _cache_key(queried_region, regions)
            con.execute(
                "INSERT OR REPLACE INTO adjacency_cache "
                "(cache_key, queried_region, candidate_regions_json, "
                "verdict, cached_at) VALUES (?, ?, ?, ?, ?)",
                (key, queried_region, json.dumps(regions),
                 1 if verdicts[nid] else 0, ts),
            )
        con.commit()
    finally:
        con.close()


def _build_prompt(
    queried_region: str,
    queried_region_label: str | None,
    candidates: list[dict],
) -> str:
    """Build the user-prompt body listing candidates for adjacency adjudication."""
    queried_display = (
        f"{queried_region_label} ({queried_region})"
        if queried_region_label
        else queried_region
    )
    lines = [
        "You are evaluating whether atlas cell-type clusters belong to a "
        f"region anatomically adjacent or closely associated with the "
        f"queried region: {queried_display}.",
        "",
        "For each candidate below, answer YES if any of its annotated regions "
        "is adjacent to or closely associated with the queried region (a known "
        "neighbouring substructure, a tightly coupled circuit partner, or a "
        "neighbouring layer/subfield). Answer NO if none of its regions are "
        "anatomically related at this resolution.",
        "",
        "Return STRICT JSON with a single key 'verdicts', an array of "
        "{candidate_id, adjacent: bool} objects, one per candidate, in the "
        "order listed below. No prose outside the JSON.",
        "",
        "Candidates:",
    ]
    for c in candidates:
        regions = c.get("regions") or []
        if regions:
            region_strs = [
                f"{r.get('label','?')} ({r.get('id','?')})"
                for r in regions
            ]
            line = f"  - {c['node_id']}: " + "; ".join(region_strs)
        else:
            line = f"  - {c['node_id']}: <no regions>"
        lines.append(line)
    return "\n".join(lines)


def _call_anthropic(
    prompt: str, model: str, max_tokens: int = 1024
) -> dict:
    """Invoke the Anthropic API and parse the JSON response.

    Returns ``{"verdicts": [{"candidate_id": ..., "adjacent": ...}, ...]}``
    on success, or raises on any error (caller handles fail-permissive).
    """
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(
        block.text for block in response.content
        if getattr(block, "type", None) == "text"
    )
    # The model is asked for STRICT JSON, but be defensive: locate first
    # '{' and last '}' to strip any preamble/postamble.
    first = text.find("{")
    last = text.rfind("}")
    if first < 0 or last < 0:
        raise ValueError(f"No JSON object in response: {text[:200]!r}")
    return json.loads(text[first : last + 1])


def check_adjacency_batch(
    queried_region: str,
    candidates: list[dict],
    queried_region_label: str | None = None,
    model: str = _DEFAULT_MODEL,
) -> dict[str, bool]:
    """Adjudicate adjacency for a batch of candidates.

    Args:
        queried_region: MBA (or other) ID of the queried soma region.
        candidates: list of dicts shaped like
            ``{"node_id": str, "regions": [{"id": str, "label": str}, ...]}``.
            Empty regions list passes through (no drop).
        queried_region_label: human label for the queried region (improves
            LLM context). Optional.
        model: Anthropic model name (default: claude-haiku-4-5).

    Returns:
        ``{node_id: bool}`` — True means "pass the region filter via adjacency".

    Failure-permissive: on missing API key, network error, or malformed
    response, returns True for every candidate (don't drop on infrastructure
    failures). The reason is logged to stderr.
    """
    if not candidates:
        return {}

    # Annotate each candidate with a stable region_ids list for cache keying.
    for c in candidates:
        c.setdefault(
            "region_ids", [r.get("id", "") for r in (c.get("regions") or [])]
        )

    # Cache lookup phase.
    cache = _cache_lookup(queried_region, candidates)
    pending = [c for c in candidates if cache.get(c["node_id"]) is None]

    out: dict[str, bool] = {
        nid: v for nid, v in cache.items() if v is not None
    }

    if not pending:
        return out

    # Skip LLM if no API key is configured (fail-permissive).
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            f"  llm_adjacency: ANTHROPIC_API_KEY not set; "
            f"passing {len(pending)} pending candidate(s) through unchecked",
            file=sys.stderr,
        )
        for c in pending:
            out[c["node_id"]] = True
        return out

    prompt = _build_prompt(queried_region, queried_region_label, pending)
    try:
        parsed = _call_anthropic(prompt, model=model)
        new_verdicts: dict[str, bool] = {}
        verdict_list = parsed.get("verdicts") or []
        # Tolerate index-based or id-based responses.
        if (
            verdict_list
            and isinstance(verdict_list[0], dict)
            and "candidate_id" in verdict_list[0]
        ):
            for v in verdict_list:
                cid = v.get("candidate_id")
                adj = bool(v.get("adjacent"))
                if cid:
                    new_verdicts[cid] = adj
        else:
            # Fallback: positional matching against pending list.
            for c, v in zip(pending, verdict_list):
                new_verdicts[c["node_id"]] = bool(v.get("adjacent")) if isinstance(v, dict) else False
    except Exception as exc:  # noqa: BLE001
        print(
            f"  llm_adjacency: LLM call failed ({type(exc).__name__}: {exc}); "
            f"passing {len(pending)} pending candidate(s) through unchecked",
            file=sys.stderr,
        )
        new_verdicts = {c["node_id"]: True for c in pending}

    # Any pending candidate not in the response also gets a permissive default.
    for c in pending:
        if c["node_id"] not in new_verdicts:
            new_verdicts[c["node_id"]] = True

    _cache_store(queried_region, pending, new_verdicts)
    out.update(new_verdicts)
    return out
