"""Reviewer-facing render of KB node files, with quote text filled in.

KB YAML cites evidence by `quote_key` only, so a reviewer reading a diff sees
`quote_key: 12345678_a3f2c1d0` and nothing else. That is fine for the KB — the
quote text lives once, in the reference store — but it makes review of newly
ingested nodes a dereferencing exercise. This module renders a node together
with the text behind every key it cites.

Two modes:

* **Full** (`render_review FILE...`): every canonical node in the given files,
  quotes inline. For reading a region locally.
* **Diff** (`render_review --base REF [PATH...]`): only what changed between
  the merge base with REF and the working tree, as a structure-aware
  comparison (see `node_diff`). Quote text, edge snippets and prose diffs sit
  under `<details>` folds so the visible comment is a compact change list, and
  the output respects a byte budget (GitHub caps a comment at 65 536 chars).
  This is what the node-review PR workflow posts (issue #179).

It is deliberately *not* `render summary`. That one is a mapping report: it
leads with mapping candidates and the evidence base, and omits `notes` and the
property prose entirely. For a freshly ingested node those sections are empty
and the omitted ones are the whole point — `notes` is where contradictions and
heterogeneity caveats are recorded, and the quote text is what a reviewer is
being asked to check.

Read-only. It never writes to `kb/`, so it needs no validation hook.
"""

from __future__ import annotations

import difflib
import html
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Union

import yaml

from evidencell import node_diff as nd
from evidencell.paths import refs_dir_for_graph
from evidencell.references import load_papers, load_quotes, store_exists
from evidencell.split_graph import is_stub

# Property blocks rendered as prose + sources, in reading order.
_PROSE_PROPS = (("morphology", "Morphology"), ("electrophysiology", "Electrophysiology"))
# Marker-ish lists rendered as a symbol table.
_MARKER_PROPS = (
    ("defining_markers", "Defining markers"),
    ("negative_markers", "Negative markers"),
    ("neuropeptides", "Neuropeptides"),
)


# ── Fold-aware output pieces ────────────────────────────────────────────────


@dataclass
class Fold:
    """A `<details>` block. `rank` orders folds for dropping under a size
    budget: higher is dropped first."""
    summary: str
    body: str
    indent: str = ""
    rank: int = 0

    def render(self, dropped: bool = False) -> str:
        i = self.indent
        if dropped:
            return f"{i}<sub>{self.summary} — omitted for size; full text in the " \
                   "workflow artifact or `just node-review --base …`</sub>"
        body = "\n".join((i + ln) if ln else "" for ln in self.body.splitlines())
        return f"{i}<details><summary>{self.summary}</summary>\n\n{body}\n\n{i}</details>"


Piece = Union[str, Fold]


def _join(pieces: list[Piece], dropped: frozenset[int] = frozenset()) -> str:
    out = []
    for p in pieces:
        if isinstance(p, Fold):
            out.append(p.render(id(p) in dropped))
        else:
            out.append(p)
    return "\n".join(out)


# ── Citation helpers ────────────────────────────────────────────────────────


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


def _quote_pieces(qk: str, quotes: dict, papers: dict, fold: bool,
                  indent: str = "  ") -> list[Piece]:
    """One quote_key as an attributed blockquote (open, or folded), or a loud miss."""
    q = quotes.get(qk)
    if q is None:
        return [f"{indent}- ⚠ **`{qk}` NOT FOUND in the reference store**", ""]
    corpus_id = qk.split("_")[0]
    out: list[Piece] = [f"{indent}- {_citation(corpus_id, papers)} · "
                        f"{_ident(corpus_id, papers)} · `{qk}`"]
    flags = " · ".join(x for x in (q.get("source_method"), q.get("status")) if x)
    text = (q.get("text") or "").strip()
    # The `<!-- quote_key: X -->` annotation is what the pre-edit hook requires
    # of any blockquote under reports/. Emitting it unconditionally costs
    # nothing in a research artifact and keeps the output valid if someone
    # points --out at reports/{region}/ instead.
    quote = [f"<!-- quote_key: {qk} -->"] + [f"> {ln}" for ln in (text.splitlines() or [""])]
    if fold:
        body = "\n".join(([f"<sub>{flags}</sub>", ""] if flags else []) + quote)
        out.append(Fold("quote", body, indent=indent + "  ", rank=2))
    else:
        if flags:
            out.append(f"{indent}  <sub>{flags}</sub>")
        out += [f"{indent}  {ln}" for ln in quote]
    out.append("")
    return out


def _quote_block(qk: str, quotes: dict, papers: dict) -> list[str]:
    """Open (unfolded) quote block — the full-mode rendering."""
    return [p for p in _quote_pieces(qk, quotes, papers, fold=False) if isinstance(p, str)]


def _source_pieces(s: dict, quotes: dict, papers: dict, fold: bool,
                   indent: str = "  ") -> list[Piece]:
    out: list[Piece] = []
    bits = [b for b in (s.get("method"), s.get("scope")) if b]
    if bits:
        out.append(f"{indent}- *{' · '.join(bits)}*")
    qk = s.get("quote_key")
    if qk:
        out += _quote_pieces(qk, quotes, papers, fold, indent)
    elif s.get("ref"):
        out += [f"{indent}- {s['ref']} (no quote_key)", ""]
    return out


def _sources_pieces(sources: Any, quotes: dict, papers: dict, fold: bool) -> list[Piece]:
    out: list[Piece] = []
    for s in sources or []:
        if isinstance(s, dict):
            out += _source_pieces(s, quotes, papers, fold)
    return out


def _sources_lines(sources: Any, quotes: dict, papers: dict) -> list[str]:
    return [p for p in _sources_pieces(sources, quotes, papers, False) if isinstance(p, str)]


def _loc_label(loc: dict) -> tuple[str, str]:
    """(label, term id) for an anatomical_location entry.

    KB entries carry `id`/`label` directly; `anatomical_structure` is the
    older nested shape and is still accepted.
    """
    t = loc.get("anatomical_structure") or {}
    label = loc.get("label") or t.get("label") or loc.get("name_in_source") or "?"
    return str(label), str(loc.get("id") or t.get("id") or "")


# ── Node body ───────────────────────────────────────────────────────────────


def _node_pieces(node: dict, quotes: dict, papers: dict, fold: bool,
                 heading: str | None = None) -> list[Piece]:
    L: list[Piece] = []
    L.append(heading or f"## {node.get('name') or node.get('id')}")
    L.append("")
    sp = node.get("species")
    if isinstance(sp, dict):
        sp = f"{sp.get('label') or sp.get('name_in_source') or ''} ({sp.get('id')})".strip()
    L.append(f"`{node.get('id')}` · {node.get('definition_basis') or 'no definition_basis'}"
             f" · species: {sp if sp is not None else '*null*'}")
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
        L.append("### Notes / caveats" if not fold else "**Notes / caveats**")
        L.append("")
        L.extend(str(node["notes"]).strip().splitlines())
        L.append("")

    h = "###" if not fold else "####"
    nt = node.get("nt_type") or {}
    if nt:
        L += [f"{h} Neurotransmitter", "", f"**{nt.get('name_in_source') or '—'}**", ""]
        L += _sources_pieces(nt.get("sources"), quotes, papers, fold)

    for key, title in _MARKER_PROPS:
        items = [m for m in node.get(key) or [] if isinstance(m, dict)]
        if not items:
            continue
        L += [f"{h} {title}", ""]
        for m in items:
            sym = m.get("name_in_source") or m.get("symbol") or "?"
            L += [f"**{sym}**", ""]
            L += _sources_pieces(m.get("sources"), quotes, papers, fold)
        L.append("")

    for key, title in _PROSE_PROPS:
        blk = node.get(key) or {}
        if not blk:
            continue
        L += [f"{h} {title}", ""]
        if blk.get("description"):
            L += [str(blk["description"]).strip(), ""]
        L += _sources_pieces(blk.get("sources"), quotes, papers, fold)

    locs = [x for x in node.get("anatomical_location") or [] if isinstance(x, dict)]
    if locs:
        L += [f"{h} Anatomical location", ""]
        for loc in locs:
            label, tid = _loc_label(loc)
            rel = loc.get("relationship_type") or loc.get("compartment") or ""
            L.append(f"**{label}** {('`'+tid+'`') if tid else ''} {('— '+rel) if rel else ''}"
                     .strip())
            L.append("")
            if loc.get("notes"):
                L += [f"  {loc['notes']}", ""]
            L += _sources_pieces(loc.get("sources"), quotes, papers, fold)

    colo = [c for c in node.get("colocated_types") or [] if isinstance(c, dict)]
    if colo:
        L += [f"{h} Colocated types", ""]
        for c in colo:
            L.append(f"- **{c.get('neighboring_type')}** — {c.get('spatial_relationship')}")
            if c.get("notes"):
                L.append(f"  <sub>{c['notes']}</sub>")
        L.append("")

    refs = node.get("definition_references") or []
    if refs:
        L += [f"{h} Definition references", ""]
        L += [f"- {r}" for r in refs]
        L.append("")
    return L


def render_node(node: dict, quotes: dict, papers: dict) -> str:
    """Render one CellTypeNode as reviewer Markdown (quotes inline)."""
    return _join(_node_pieces(node, quotes, papers, fold=False))


def _load_store(refs_dir: Path) -> tuple[dict, dict]:
    if store_exists(refs_dir):
        return load_quotes(refs_dir), load_papers(refs_dir)
    print(f"WARNING: no reference store at {refs_dir}; quotes cannot be "
          "dereferenced and every cited key will render as NOT FOUND.",
          file=sys.stderr)
    return {}, {}


def render_file(graph_file: Path) -> str:
    """Render every node in one KB graph file."""
    graph_file = Path(graph_file)
    doc = yaml.safe_load(graph_file.read_text(encoding="utf-8")) or {}
    quotes, papers = _load_store(refs_dir_for_graph(graph_file))
    nodes = [n for n in (doc.get("nodes") or []) if isinstance(n, dict)]
    # Stubs exist only so edge endpoints resolve; with edges not rendered they
    # are noise, and in a mapped file they outnumber the canonical node.
    stubs = [n for n in nodes if is_stub(n)]
    parts = [render_node(n, quotes, papers) for n in nodes if not is_stub(n)]
    edges = doc.get("edges") or []
    body = "\n\n---\n\n".join(parts)
    if edges or stubs:
        body += (f"\n\n---\n\n*{len(edges)} mapping edge(s) and {len(stubs)} "
                 "reference stub(s) in this file are not rendered here — use "
                 "`just gen-report` for mapping review, or `--base` for a diff "
                 "that includes edges.*\n")
    return body


# ── Diff mode ───────────────────────────────────────────────────────────────

_FIELD_LABELS = {
    "defining_markers": "Defining marker", "negative_markers": "Negative marker",
    "neuropeptides": "Neuropeptide", "anatomical_location": "Location",
    "colocated_types": "Colocated type", "nt_type": "NT type",
    "cl_mapping": "CL mapping", "cl_term": "term", "morphology": "Morphology",
    "electrophysiology": "Electrophysiology",
    "definition_references": "Definition reference", "notes": "Notes",
    "species": "Species", "name": "Name", "definition_basis": "Definition basis",
    "name_in_source": "name in source", "description": "description",
    "relationship": "Relationship", "confidence": "Confidence",
    "mapping_cardinality": "Cardinality", "mapping_justification": "Justification",
    "lit_type": "lit_type", "taxonomy_type": "taxonomy_type", "caveats": "Caveat",
    "property_comparisons": "Property comparison", "synonyms": "Synonym",
    "proposed_cl_term": "Proposed CL term", "brain_region": "Brain region",
}
_SEV_RANK = {s: i for i, s in enumerate(nd.SEVERITY_ORDER)}


def _fmt(v: Any) -> str:
    if nd._empty(v):
        return "*none*"
    if isinstance(v, dict):
        if v.get("label") and v.get("id"):
            return f"{v['label']} (`{v['id']}`)"
        if v.get("id"):
            return f"`{v['id']}`"
        s = ", ".join(f"{k}: {_fmt(x)}" for k, x in v.items() if not nd._empty(x))
        return s if len(s) < 160 else s[:157] + "…"
    if isinstance(v, list):
        return ", ".join(_fmt(x) for x in v)
    return f"`{v}`" if isinstance(v, str) and len(v) < 60 and " " not in v else str(v)


def _label(c: nd.Change, trim_items: bool = False) -> str:
    """Human label from a change path: field names labelled, item keys bold."""
    fields = set(c.field_path)
    parts = []
    path = c.path
    if trim_items and path:
        path = path[:-1]
        while path and path[-1] in ("sources", "evidence"):
            path = path[:-1]
    for p in path:
        if p in fields:
            parts.append(_FIELD_LABELS.get(p, p.replace("_", " ")))
        else:
            parts.append(f"**{p}**")
    return " › ".join(parts) or "(entity)"


def _word_diff(old: str, new: str) -> tuple[str, int, int]:
    a, b = str(old or "").split(), str(new or "").split()
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    out, plus, minus = [], 0, 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            out.append(html.escape(" ".join(a[i1:i2])))
            continue
        if i2 > i1:
            minus += i2 - i1
            out.append(f"<del>{html.escape(' '.join(a[i1:i2]))}</del>")
        if j2 > j1:
            plus += j2 - j1
            out.append(f"<ins>{html.escape(' '.join(b[j1:j2]))}</ins>")
    return " ".join(out), plus, minus


def _evidence_line(e: dict) -> str:
    bits = [e.get("evidence_type") or "?"]
    for k in ("reference", "run_ref", "cell_set_accession", "source_dataset_accession"):
        if e.get(k):
            bits.append(str(e[k]))
            break
    if e.get("supports"):
        bits.append(str(e["supports"]))
    return " · ".join(bits)


def _evidence_fold(e: dict, indent: str, rank: int) -> Fold | None:
    body = []
    if e.get("snippet"):
        body += [f"> {ln}" for ln in str(e["snippet"]).strip().splitlines()] + [""]
    if e.get("explanation"):
        body += [str(e["explanation"]).strip()]
    return Fold("snippet + explanation", "\n".join(body), indent, rank) if body else None


def _change_pieces(c: nd.Change, quotes: dict, papers: dict, rank: int) -> list[Piece]:
    sign = {"added": "➕", "removed": "➖"}.get(c.op, "✏️")
    if c.kind == "source":
        s = c.new if c.op == "added" else c.old
        s = s if isinstance(s, dict) else {}
        qk = s.get("quote_key")
        where = _label(c, trim_items=True)
        if qk:
            cid = qk.split("_")[0]
            cite = f"{_citation(cid, papers)} · {_ident(cid, papers)} · `{qk}`"
        else:
            cite = f"{s.get('ref')} (no quote_key)"
        out: list[Piece] = [f"- {sign} source on {where}: {cite}"]
        if c.op == "added" and qk and qk in quotes:
            text = (quotes[qk].get("text") or "").strip()
            body = [f"<!-- quote_key: {qk} -->"] + [f"> {ln}" for ln in text.splitlines()]
            out.append(Fold("quote", "\n".join(body), "  ", rank))
        return out
    if c.kind == "evidence":
        e = c.new if c.op == "added" else c.old
        e = e if isinstance(e, dict) else {}
        where = _label(c, trim_items=True)
        out = [f"- {sign} evidence{(' on ' + where) if where != '(entity)' else ''}: "
               f"{_evidence_line(e)}"]
        f = _evidence_fold(e, "  ", rank) if c.op == "added" else None
        return out + ([f] if f else [])
    if c.kind == "list_item":
        item = c.new if c.op == "added" else c.old
        out = [f"- {sign} {_label(c, trim_items=True)} **{c.path[-1]}**"]
        if c.op == "added" and isinstance(item, dict):
            extras = {k: v for k, v in item.items()
                      if k not in ("sources", "symbol", "name_in_source") and not nd._empty(v)}
            if extras:
                out.append(f"  <sub>{html.escape(_fmt(extras))}</sub>")
            for s in item.get("sources") or []:
                if isinstance(s, dict):
                    out += _source_pieces(s, quotes, papers, True, indent="  ")
        return out
    if c.kind == "block":
        val = c.new if c.op == "added" else c.old
        first = f"- {sign} {_label(c)}"
        if c.op != "added" or not isinstance(val, dict):
            if c.op == "modified":
                first += f": ~~{_fmt(c.old)}~~ → **{_fmt(c.new)}**"
            return [first]
        scalars = {k: v for k, v in val.items()
                   if k != "sources" and not isinstance(v, (dict, list))
                   and not nd._empty(v) and k not in nd.PROSE_FIELDS}
        if scalars:
            first += f": {_fmt(scalars)}"
        out = [first]
        for k in nd.PROSE_FIELDS:
            if val.get(k):
                out.append(Fold(k, html.escape(str(val[k]).strip()), "  ", rank))
        for s in val.get("sources") or []:
            if isinstance(s, dict):
                out += _source_pieces(s, quotes, papers, True, indent="  ")
        return out
    if c.kind == "prose":
        if nd._empty(c.old):
            return [f"- ➕ {_label(c)} added",
                    Fold("text", html.escape(str(c.new).strip()), "  ", rank)]
        if nd._empty(c.new):
            return [f"- ➖ {_label(c)} removed"]
        diff, plus, minus = _word_diff(c.old, c.new)
        return [f"- ✏️ {_label(c)} changed (+{plus} / −{minus} words)",
                Fold("word diff", diff, "  ", rank)]
    # scalar
    return [f"- {_label(c)}: ~~{_fmt(c.old)}~~ → **{_fmt(c.new)}**"
            if not nd._empty(c.old) else f"- {_label(c)}: *none* → **{_fmt(c.new)}**"]


def _entity_name(c: nd.Change, head_docs: dict, base_docs: dict) -> str:
    for docs in (head_docs, base_docs):
        for d in docs.values():
            for n in (d or {}).get("nodes") or []:
                if isinstance(n, dict) and n.get("id") == c.entity_id and n.get("name"):
                    return str(n["name"])
    return c.entity_id


def _edges_referencing(nid: str, head_docs: dict) -> list[str]:
    return sorted(
        f"`{e.get('id')}` ({p})" for p, d in head_docs.items()
        for e in (d or {}).get("edges") or []
        if isinstance(e, dict) and nid in (e.get("lit_type"), e.get("taxonomy_type")))


@dataclass
class DiffResult:
    base: str
    merge_base: str
    files: list[str]
    changes: list[nd.Change]
    warnings: list[nd.Warning_]
    references: dict
    uncited: list[str]
    head_docs: dict
    base_docs: dict
    stores: dict

    def to_json(self) -> dict:
        refs = dict(self.references)
        refs["uncited_quotes_added"] = self.uncited
        return {"base": self.base, "merge_base": self.merge_base, "files": self.files,
                "changes": [c.to_dict() for c in self.changes],
                "warnings": [w.to_dict() for w in self.warnings],
                "references": refs}


def compute_diff(base_ref: str, root: Path, only: list[str] | None = None) -> DiffResult:
    """Everything diff mode needs, from git + the working tree under `root`."""
    mb = nd.merge_base(base_ref, root)
    paths = nd.changed_paths(mb, root)
    if only:
        prefixes = [str(Path(o)).rstrip("/") for o in only]
        paths = [p for p in paths
                 if any(p == x or p.startswith(x + "/") for x in prefixes)]
    graph_paths = [p for p in paths if nd.is_graph_path(p)]
    ref_paths = [p for p in paths if p.startswith("references/")]

    base_docs = {p: nd.load_yaml(nd.read_at(mb, p, root)) for p in graph_paths}
    head_docs = {p: nd.load_yaml(nd.read_head(p, root)) for p in graph_paths}
    changes = nd.diff_files((p, base_docs[p], head_docs[p]) for p in graph_paths)

    regions = {r for r in map(nd.region_of, graph_paths + ref_paths) if r}
    stores: dict[str, tuple[dict, dict]] = {}
    for r in sorted(regions):
        d = root / "references" / r
        stores[r] = (load_quotes(d), load_papers(d)) if store_exists(d) else ({}, {})

    warnings = nd.check_changes(changes, stores)
    refs = nd.diff_reference_store(ref_paths, mb, root)
    for ic in refs["identity_changes"]:
        warnings.append(nd.Warning_(
            f"references/…/papers/{ic['corpus_id']}.json", ic["corpus_id"],
            f"paper identity field `{ic['field']}` changed: {ic['old']!r} → {ic['new']!r}"))
    for k in refs["quotes_removed"]:
        warnings.append(nd.Warning_("references", k, f"quote `{k}` removed from the store"))
    for k in refs["quote_text_changed"]:
        warnings.append(nd.Warning_("references", k,
                                    f"text of quote `{k}` changed — its key no longer matches"))
    all_quotes: dict = {}
    for q, _ in stores.values():
        all_quotes.update(q)
    cited = nd.cited_quote_keys(head_docs.values(), all_quotes)
    uncited = sorted(k for k in refs["quotes_added"] if k not in cited)
    return DiffResult(base_ref, mb, paths, nd.sort_changes(changes), warnings, refs,
                      uncited, head_docs, base_docs, stores)


def _counts(changes: list[nd.Change], entity: str) -> str:
    ent = [c for c in changes if c.entity == entity]
    added = {c.entity_id for c in ent if c.kind == "entity" and c.op == "added"}
    removed = {c.entity_id for c in ent if c.kind == "entity" and c.op == "removed"}
    moved = {c.entity_id for c in ent if c.kind == "entity" and c.op == "moved"}
    modified = {c.entity_id for c in ent if c.severity != "metadata"} - added - removed - moved
    bits = [f"+{len(added)}" if added else "", f"~{len(modified)}" if modified else "",
            f"−{len(removed)}" if removed else "", f"↪{len(moved)}" if moved else ""]
    return " ".join(b for b in bits if b) or "—"


def _sections(r: DiffResult, verbose: bool) -> list[tuple[str, list[Piece]]]:
    """(entity label, pieces) per entity section, in file order."""
    secs: list[tuple[str, list[Piece]]] = []
    by_file: dict[str, list[nd.Change]] = {}
    for c in r.changes:
        by_file.setdefault(c.file, []).append(c)

    for f in sorted(by_file):
        region = nd.region_of(f) or ""
        quotes, papers = r.stores.get(region, ({}, {}))
        fchanges = by_file[f]
        stub_adds = {c.entity_id for c in fchanges
                     if c.entity == "stub" and c.kind == "entity" and c.op == "added"}
        order: list[tuple[str, str]] = []
        for c in fchanges:
            k = (c.entity, c.entity_id)
            if k not in order and c.entity != "stub":
                order.append(k)
        first = True
        for ent, eid in sorted(order, key=lambda k: ("node", "edge", "graph").index(k[0])):
            ec = [c for c in fchanges if c.entity == ent and c.entity_id == eid]
            head = next((c for c in ec if c.kind == "entity"), None)
            pieces: list[Piece] = []
            if first:
                pieces += [f"## `{f}`", ""]
                first = False
            if ent == "node" and head and head.op == "added":
                pieces += _node_pieces(head.new, quotes, papers, fold=True,
                                       heading=f"### ➕ {head.new.get('name') or eid} · "
                                               f"`{eid}` — new")
                secs.append((eid, pieces))
                continue
            if ent == "edge" and head and head.op == "added":
                e = head.new
                stub = (f" <sub>(stub for `{e.get('taxonomy_type')}` added)</sub>"
                        if e.get("taxonomy_type") in stub_adds else "")
                pieces += [f"### ➕ Edge `{eid}` — new", "",
                           f"`{e.get('lit_type')}` —**{e.get('relationship')}**→ "
                           f"`{e.get('taxonomy_type')}`{stub}", ""]
                meta = " · ".join(str(e[k]) for k in
                                  ("mapping_cardinality", "mapping_justification",
                                   "confidence") if e.get(k))
                if meta:
                    pieces += [meta, ""]
                for ev in e.get("evidence") or []:
                    if isinstance(ev, dict):
                        pieces.append(f"- evidence: {_evidence_line(ev)}")
                        fo = _evidence_fold(ev, "  ", 2)
                        if fo:
                            pieces.append(fo)
                for cv in e.get("caveats") or []:
                    pieces.append(f"- caveat: {_fmt(cv)}")
                secs.append((eid, pieces + [""]))
                continue
            if head and head.op == "removed":
                title = (f"Edge `{eid}`" if ent == "edge" else
                         f"{_entity_name(head, r.head_docs, r.base_docs)} · `{eid}`")
                pieces += [f"### ➖ {title} — removed", ""]
                if ent == "node":
                    refs = _edges_referencing(eid, r.head_docs)
                    if refs:
                        pieces += [f"- ⚠ still referenced by edge(s): {', '.join(refs)}", ""]
                secs.append((eid, pieces))
                continue
            if ent == "graph":
                pieces += ["### File-level fields", ""]
            else:
                title = (f"Edge `{eid}`" if ent == "edge" else
                         f"{_entity_name(ec[0], r.head_docs, r.base_docs)} · `{eid}`")
                moved = (f" — moved from `{head.moved_from}`"
                         if head and head.op == "moved" else "")
                pieces += [f"### ✏️ {title}{moved}", ""]
            body = [c for c in ec if c.kind != "entity"]
            shown = [c for c in body if verbose or c.severity != "metadata"]
            hidden = len(body) - len(shown)
            if not shown and not hidden and not (head and head.op == "moved"):
                continue
            if not shown and ent == "graph":
                continue
            for c in shown:
                pieces += _change_pieces(c, quotes, papers, rank=_SEV_RANK[c.severity])
            if hidden:
                pieces.append(f"<sub>{hidden} metadata change(s) not shown "
                              "(dates, hashes; `--verbose` to list)</sub>")
            secs.append((eid, pieces + [""]))
    return secs


def _header_pieces(r: DiffResult) -> list[Piece]:
    files = sorted({c.file for c in r.changes})
    out: list[Piece] = [f"# Node review — changes vs `{r.base}`", ""]
    if files:
        out += ["| File | Nodes | Edges |", "|---|---|---|"]
        for f in files:
            fc = [c for c in r.changes if c.file == f]
            out.append(f"| `{f}` | {_counts(fc, 'node')} | {_counts(fc, 'edge')} |")
        out += ["", "<sub>+ added · ~ modified · − removed · ↪ moved</sub>", ""]
    elif not r.references["papers_added"] and not r.references["quotes_added"]:
        out += ["No KB graph or reference-store changes.", ""]
    else:
        out += ["Reference-store changes only — no KB graph file changed.", ""]
    if r.warnings:
        out += [f"## ⚠ {len(r.warnings)} warning(s)", ""]
        out += [f"- **`{w.entity_id}`** ({w.file}): {w.message}" for w in r.warnings]
        out.append("")
    return out


def _reference_pieces(r: DiffResult) -> list[Piece]:
    refs = r.references
    papers_added = refs["papers_added"]
    qa = refs["quotes_added"]
    claims = refs["claims_edits"]
    if not (papers_added or qa or claims or refs["other_quote_edits"]):
        return []
    lines = []
    if papers_added:
        lines += [f"**{len(papers_added)} paper(s) added**", ""]
        for p in sorted(papers_added, key=lambda p: (str(p.get("year")), str(p.get("title")))):
            ident = (f"PMID:{p['pmid']}" if p.get("pmid") else
                     f"DOI:{p['doi']}" if p.get("doi") else f"CorpusId:{p.get('corpus_id')}")
            key = (p.get("author_keys") or [p.get("corpus_id")])[0]
            conf = p.get("resolution_confidence")
            lines.append(f"- {key} · {ident} · {html.escape(str(p.get('title') or ''))}"
                         + (f" <sub>{conf}</sub>" if conf and conf != "HIGH" else ""))
        lines.append("")
    if qa:
        lines.append(f"**{len(qa)} quote(s) added**, {len(qa) - len(r.uncited)} cited by "
                     "a changed node or edge.")
        lines.append("")
    if r.uncited:
        lines += ["Stored but not cited by any changed node or edge:", ""]
        lines += [f"- `{k}`" for k in r.uncited]
        lines.append("")
    if claims:
        lines.append(f"`claims` edited on {sum(claims.values())} quote(s) across "
                     f"{len(claims)} paper(s).")
    if refs["other_quote_edits"]:
        lines.append(f"{refs['other_quote_edits']} other quote metadata edit(s).")
    summary = (f"Reference store — {len(papers_added)} paper(s), "
               f"{len(qa)} quote(s) added")
    return ["## Reference store", "", Fold(summary, "\n".join(lines), "", 1), ""]


def render_diff(r: DiffResult, budget: int = 0, verbose: bool = False) -> str:
    """Markdown for a DiffResult, kept under `budget` bytes when budget > 0.

    Visible change lines and warnings are never dropped. Under pressure, fold
    bodies go first (least severe, latest first), then whole entity sections
    from the end, replaced by a list of what was omitted. Never cuts mid-tag.
    """
    header = _header_pieces(r)
    secs = _sections(r, verbose)
    tail = _reference_pieces(r)

    def build(dropped: frozenset[int], keep: int) -> str:
        pieces = list(header)
        for _, p in secs[:keep]:
            pieces += p
        omitted = [eid for eid, _ in secs[keep:]]
        if omitted:
            pieces += ["", f"**{len(omitted)} more changed entit(ies) omitted for size:** "
                       + ", ".join(f"`{e}`" for e in omitted)
                       + " — full render in the workflow artifact, or run "
                       "`just node-review --base …` locally.", ""]
        pieces += tail
        return _join(pieces, dropped)

    keep = len(secs)
    text = build(frozenset(), keep)
    if budget <= 0 or len(text.encode()) <= budget:
        return text

    folds: list[tuple[int, int, Fold]] = []
    for si, (_, p) in enumerate(secs):
        for x in p:
            if isinstance(x, Fold):
                folds.append((x.rank, si, x))
    for x in tail:
        if isinstance(x, Fold):
            folds.append((x.rank, len(secs), x))
    # Highest rank (least severe) first; within a rank, latest section first.
    folds.sort(key=lambda t: (-t[0], -t[1]))
    dropped: set[int] = set()
    for _, _, fo in folds:
        dropped.add(id(fo))
        text = build(frozenset(dropped), keep)
        if len(text.encode()) <= budget:
            return text
    while keep > 0 and len(text.encode()) > budget:
        keep -= 1
        text = build(frozenset(dropped), keep)
    return text


# ── CLI ─────────────────────────────────────────────────────────────────────


def _git_root() -> Path:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                         text=True, check=True).stdout.strip()
    return Path(out)


def main(argv: list[str] | None = None) -> int:
    import argparse

    p = argparse.ArgumentParser(
        prog="python -m evidencell.render_review",
        description="Render KB node files for review, with quote text filled in. "
                    "With --base, render only what changed vs that ref.",
    )
    p.add_argument("targets", nargs="*", type=Path,
                   help="KB graph YAML file(s) or directories. Required without "
                        "--base; with --base, restricts the diff to these paths.")
    p.add_argument("--base", default=None,
                   help="Diff mode: compare the working tree against the merge base "
                        "with this ref (e.g. origin/main).")
    p.add_argument("--format", choices=("md", "json"), default="md",
                   help="Diff mode output format (default md).")
    p.add_argument("--budget", type=int, default=60000,
                   help="Diff mode: max output bytes for md (default 60000; 0 = no limit).")
    p.add_argument("--verbose", action="store_true",
                   help="Diff mode: list metadata changes instead of counting them.")
    p.add_argument("--out", type=Path, default=None,
                   help="Write to this file instead of stdout.")
    args = p.parse_args(argv)

    if args.base:
        root = _git_root()
        only = None
        if args.targets:
            only = [str(t.resolve().relative_to(root)) for t in args.targets]
        r = compute_diff(args.base, root, only)
        if args.format == "json":
            text = json.dumps(r.to_json(), indent=2, default=str) + "\n"
        else:
            text = render_diff(r, budget=args.budget, verbose=args.verbose)
    else:
        if not args.targets:
            p.error("targets are required without --base")
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
