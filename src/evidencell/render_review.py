"""Reviewer-facing render of KB node files, with quote text filled in.

KB YAML cites evidence by `quote_key` only, so a reviewer reading a diff sees
`quote_key: 12345678_a3f2c1d0` and nothing else. That is fine for the KB — the
quote text lives once, in the reference store — but it makes review of newly
ingested nodes a dereferencing exercise. This module renders a node together
with the text behind every key it cites.

It is deliberately *not* `render summary`. That one is a mapping report: it
leads with mapping candidates and the evidence base, and omits `notes` and the
property prose entirely. For a freshly ingested node those sections are empty
and the omitted ones are the whole point — `notes` is where contradictions and
heterogeneity caveats are recorded, and the quote text is what a reviewer is
being asked to check.

Read-only. It never writes to `kb/`, so it needs no validation hook.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from evidencell.paths import refs_dir_for_graph
from evidencell.references import load_papers, load_quotes, store_exists

# Property blocks rendered as prose + sources, in reading order.
_PROSE_PROPS = (("morphology", "Morphology"), ("electrophysiology", "Electrophysiology"))
# Marker-ish lists rendered as a symbol table.
_MARKER_PROPS = (
    ("defining_markers", "Defining markers"),
    ("negative_markers", "Negative markers"),
    ("neuropeptides", "Neuropeptides"),
)


def _citation(corpus_id: str, papers: dict) -> str:
    """Short human citation for a corpus_id, falling back to the id itself."""
    p = papers.get(str(corpus_id)) or {}
    keys = p.get("author_keys") or []
    if keys:
        return str(keys[0])
    authors = p.get("authors") or []
    first = (authors[0].split()[-1] if authors else "Unknown")
    year = p.get("year") or "n.d."
    return f"{first} et al., {year}"


def _ident(corpus_id: str, papers: dict) -> str:
    p = papers.get(str(corpus_id)) or {}
    if p.get("pmid"):
        return f"PMID:{p['pmid']}"
    if p.get("doi"):
        return f"DOI:{p['doi']}"
    return f"CorpusId:{corpus_id}"


def _quote_block(qk: str, quotes: dict, papers: dict) -> list[str]:
    """Render one quote_key as an attributed blockquote, or a loud miss."""
    q = quotes.get(qk)
    if q is None:
        return [f"  - ⚠ **`{qk}` NOT FOUND in the reference store**", ""]
    corpus_id = qk.split("_")[0]
    out = [f"  - {_citation(corpus_id, papers)} · {_ident(corpus_id, papers)} · `{qk}`"]
    status = q.get("status")
    method = q.get("source_method")
    flags = " · ".join(x for x in (method, status) if x)
    if flags:
        out.append(f"    <sub>{flags}</sub>")
    text = (q.get("text") or "").strip()
    # The `<!-- quote_key: X -->` annotation is what the pre-edit hook requires
    # of any blockquote under reports/. Emitting it unconditionally costs
    # nothing in a research artifact and keeps the output valid if someone
    # points --out at reports/{region}/ instead.
    out.append(f"    <!-- quote_key: {qk} -->")
    for line in text.splitlines() or [""]:
        out.append(f"    > {line}")
    out.append("")
    return out


def _sources_lines(sources: Any, quotes: dict, papers: dict) -> list[str]:
    out: list[str] = []
    for s in sources or []:
        if not isinstance(s, dict):
            continue
        bits = [b for b in (s.get("method"), s.get("scope")) if b]
        if bits:
            out.append(f"  - *{' · '.join(bits)}*")
        qk = s.get("quote_key")
        if qk:
            out.extend(_quote_block(qk, quotes, papers))
        elif s.get("ref"):
            out.append(f"  - {s['ref']} (no quote_key)")
            out.append("")
    return out


def render_node(node: dict, quotes: dict, papers: dict) -> str:
    """Render one CellTypeNode as reviewer Markdown."""
    L: list[str] = []
    L.append(f"## {node.get('name') or node.get('id')}")
    L.append("")
    L.append(f"`{node.get('id')}` · {node.get('definition_basis') or 'no definition_basis'}"
             f" · species: {node.get('species') if node.get('species') is not None else '*null*'}")
    L.append("")

    cm = node.get("cl_mapping") or {}
    term = (cm.get("cl_term") or {}) if isinstance(cm, dict) else {}
    if term:
        L.append(f"**CL:** {term.get('label')} ({term.get('id')}) — "
                 f"**{cm.get('mapping_type')}**")
        if cm.get("mapping_notes"):
            L.append("")
            L.append(f"> {str(cm['mapping_notes']).strip()}")
        L.append("")

    # notes first — this is the curator content a reviewer most needs to see.
    if node.get("notes"):
        L.append("### Notes / caveats")
        L.append("")
        for line in str(node["notes"]).strip().splitlines():
            L.append(line)
        L.append("")

    nt = node.get("nt_type") or {}
    if nt:
        L.append("### Neurotransmitter")
        L.append("")
        L.append(f"**{nt.get('name_in_source') or '—'}**")
        L.append("")
        L.extend(_sources_lines(nt.get("sources"), quotes, papers))

    for key, heading in _MARKER_PROPS:
        items = node.get(key) or []
        if not items:
            continue
        L.append(f"### {heading}")
        L.append("")
        for m in items:
            if not isinstance(m, dict):
                continue
            sym = m.get("name_in_source") or m.get("symbol") or "?"
            L.append(f"**{sym}**")
            L.append("")
            L.extend(_sources_lines(m.get("sources"), quotes, papers))
        L.append("")

    for key, heading in _PROSE_PROPS:
        blk = node.get(key) or {}
        if not blk:
            continue
        L.append(f"### {heading}")
        L.append("")
        if blk.get("description"):
            L.append(str(blk["description"]).strip())
            L.append("")
        L.extend(_sources_lines(blk.get("sources"), quotes, papers))

    locs = node.get("anatomical_location") or []
    if locs:
        L.append("### Anatomical location")
        L.append("")
        for loc in locs:
            if not isinstance(loc, dict):
                continue
            t = loc.get("anatomical_structure") or {}
            label = t.get("label") or loc.get("name_in_source") or "?"
            tid = t.get("id") or ""
            rel = loc.get("relationship_type") or ""
            L.append(f"**{label}** {('`'+tid+'`') if tid else ''} {('— '+rel) if rel else ''}".strip())
            L.append("")
            if loc.get("notes"):
                L.append(f"  {loc['notes']}")
                L.append("")
            L.extend(_sources_lines(loc.get("sources"), quotes, papers))

    colo = node.get("colocated_types") or []
    if colo:
        L.append("### Colocated types")
        L.append("")
        for c in colo:
            if not isinstance(c, dict):
                continue
            L.append(f"- **{c.get('neighboring_type')}** — {c.get('spatial_relationship')}")
            if c.get("notes"):
                L.append(f"  <sub>{c['notes']}</sub>")
        L.append("")

    refs = node.get("definition_references") or []
    if refs:
        L.append("### Definition references")
        L.append("")
        for r in refs:
            L.append(f"- {r}")
        L.append("")
    return "\n".join(L)


def render_file(graph_file: Path) -> str:
    """Render every node in one KB graph file."""
    graph_file = Path(graph_file)
    doc = yaml.safe_load(graph_file.read_text(encoding="utf-8")) or {}
    refs_dir = refs_dir_for_graph(graph_file)
    if store_exists(refs_dir):
        quotes, papers = load_quotes(refs_dir), load_papers(refs_dir)
    else:
        quotes, papers = {}, {}
        print(f"WARNING: no reference store at {refs_dir}; quotes cannot be "
              "dereferenced and every cited key will render as NOT FOUND.",
              file=sys.stderr)
    parts = [render_node(n, quotes, papers) for n in (doc.get("nodes") or [])
             if isinstance(n, dict)]
    edges = doc.get("edges") or []
    body = "\n\n---\n\n".join(parts)
    if edges:
        body += (f"\n\n---\n\n*{len(edges)} mapping edge(s) in this file are not "
                 "rendered here — use `just gen-report` for mapping review.*\n")
    return body


def main(argv: list[str] | None = None) -> int:
    import argparse

    p = argparse.ArgumentParser(
        prog="python -m evidencell.render_review",
        description="Render KB node files for review, with quote text filled in.",
    )
    p.add_argument("targets", nargs="+", type=Path,
                   help="KB graph YAML file(s), or a region directory.")
    p.add_argument("--out", type=Path, default=None,
                   help="Write to this file instead of stdout.")
    args = p.parse_args(argv)

    files: list[Path] = []
    for t in args.targets:
        files.extend(sorted(t.glob("*.yaml")) if t.is_dir() else [t])
    if not files:
        print("No KB YAML files found in the given targets.", file=sys.stderr)
        return 1

    chunks = [f"# Node review — {len(files)} file(s)", ""]
    for f in files:
        chunks.append(f"<!-- {f} -->")
        chunks.append(render_file(f))
        chunks.append("")
    text = "\n".join(chunks)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"Written: {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
