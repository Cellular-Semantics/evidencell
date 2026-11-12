"""Structure-aware diff of KB graph files, for PR review (issue #179).

A raw text diff of KB YAML is noisy: comments, key order, list order and
folded-string re-wrapping all show up as changes, and evidence appears as bare
quote-key hashes. This module compares the *parsed* documents instead. List
items are matched by identity (node id, marker symbol, source ref + quote_key,
...) so reordering is not a change, and strings are compared with whitespace
collapsed so re-wrapping is not a change either.

The output is a flat list of `Change` records (JSON-serialisable). Rendering is
`render_review.render_diff`'s job; tests run against the records.

Read-only. Never writes to kb/.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable

import yaml

from evidencell.split_graph import is_stub

# ── Severity ────────────────────────────────────────────────────────────────
# Changes within an entity are listed most-severe first. Metadata changes are
# counted, not listed, unless the caller asks for them.

SEVERITY_ORDER = ("identity", "content", "provenance", "metadata")

_NODE_IDENTITY = {
    "id", "name", "definition_basis", "species", "nt_type", "cl_mapping",
    "is_terminal", "reference_stub", "taxonomy_id", "cell_set_accession",
}
_EDGE_IDENTITY = {
    "id", "lit_type", "taxonomy_type", "relationship", "mapping_cardinality",
    "mapping_justification", "confidence",
}
_GRAPH_IDENTITY = {"name", "brain_region", "species", "target_atlas"}
_METADATA = {
    "creation_date", "updated_date", "curator", "reviewed_by",
    "rationale_generated_at", "rationale_source_hash", "confidence_score",
    "discovery_score", "report_path", "manually_curated",
}
_PROVENANCE_KEYS = {"sources", "evidence", "definition_references"}

# Free-text fields: shown as a word diff under a fold rather than old → new.
PROSE_FIELDS = {
    "description", "notes", "explanation", "rationale", "mapping_notes",
    "snippet", "definition", "reconciliation_note",
}
_PROSE_MIN_LEN = 120  # any other string longer than this is treated as prose


# ── Identity keys for list matching ─────────────────────────────────────────


def norm_text(s: str) -> str:
    """Whitespace-collapsed, lowercased text — the quote-key normalisation."""
    return " ".join(str(s).lower().split())


def _ws(s: Any) -> Any:
    """Whitespace-collapsed string for equality (case preserved)."""
    return " ".join(s.split()) if isinstance(s, str) else s


def _short_hash(s: Any) -> str:
    return hashlib.sha256(norm_text(s or "").encode()).hexdigest()[:8]


def _marker_key(m: dict) -> str | None:
    return m.get("symbol") or m.get("name_in_source")


def _location_key(loc: dict) -> str | None:
    term = loc.get("id") or (loc.get("anatomical_structure") or {}).get("id")
    base = term or loc.get("name_in_source")
    if base is None:
        return None
    comp = loc.get("compartment")
    return f"{base}|{comp}" if comp else str(base)


def _source_key(s: dict) -> str | None:
    if not (s.get("ref") or s.get("quote_key")):
        return None
    return f"{s.get('ref') or ''}|{s.get('quote_key') or ''}"


def _evidence_key(e: dict) -> str | None:
    et = e.get("evidence_type") or "?"
    if e.get("reference") or e.get("snippet"):
        return f"{et}|{e.get('reference') or ''}|{_short_hash(e.get('snippet'))}"
    for k in ("run_ref", "cell_set_accession", "source_dataset_accession", "dataset"):
        if e.get(k):
            return f"{et}|{e[k]}"
    return None


# List field name → identity function. A new list field needs one line here.
LIST_KEYS: dict[str, Callable[[dict], str | None]] = {
    "nodes": lambda n: n.get("id"),
    "edges": lambda e: e.get("id"),
    "defining_markers": _marker_key,
    "negative_markers": _marker_key,
    "neuropeptides": _marker_key,
    "merfish_markers": _marker_key,
    "markers": _marker_key,
    "anatomical_location": _location_key,
    "colocated_types": lambda c: c.get("neighboring_type"),
    "sources": _source_key,
    "evidence": _evidence_key,
    "property_comparisons": lambda p: p.get("property"),
    "at_source_sets": lambda a: (
        f"{a.get('dataset_accession') or ''}|{a.get('source_label') or ''}" or None
    ),
}


# ── Change record ───────────────────────────────────────────────────────────


@dataclass
class Change:
    file: str
    entity: str          # node | edge | stub | graph
    entity_id: str
    op: str              # added | removed | modified | moved
    path: list[str]      # field names and item display keys, from the entity root
    kind: str            # entity | scalar | prose | block | list_item | source | evidence
    old: Any = None
    new: Any = None
    severity: str = "content"
    field_path: list[str] = field(default_factory=list)  # field names only
    moved_from: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def _empty(v: Any) -> bool:
    return v is None or v == "" or v == [] or v == {}


def _canon(v: Any) -> Any:
    """Canonical form for equality: whitespace-collapsed strings, empties dropped."""
    if isinstance(v, dict):
        return {k: _canon(x) for k, x in v.items() if not _empty(x)}
    if isinstance(v, list):
        return [_canon(x) for x in v]
    return _ws(v)


def _equal(a: Any, b: Any) -> bool:
    if _empty(a) and _empty(b):
        return True
    return json.dumps(_canon(a), sort_keys=True, default=str) == json.dumps(
        _canon(b), sort_keys=True, default=str)


def _severity(entity: str, field_path: list[str]) -> str:
    top = field_path[0] if field_path else ""
    if top in _METADATA or (field_path and field_path[-1] in _METADATA):
        return "metadata"
    identity = {"node": _NODE_IDENTITY, "stub": _NODE_IDENTITY,
                "edge": _EDGE_IDENTITY, "graph": _GRAPH_IDENTITY}.get(entity, set())
    if top in identity:
        return "identity"
    if any(p in _PROVENANCE_KEYS for p in field_path):
        return "provenance"
    return "content"


def _item_kind(list_field: str) -> str:
    return {"sources": "source", "evidence": "evidence"}.get(list_field, "list_item")


def _is_prose(field_name: str, a: Any, b: Any) -> bool:
    if field_name in PROSE_FIELDS:
        return True
    return any(isinstance(x, str) and len(x) > _PROSE_MIN_LEN for x in (a, b))


def _match(list_field: str, old: list, new: list
           ) -> tuple[list[tuple[str, Any, Any]], bool]:
    """Pair list items by identity. Returns ([(display_key, old, new)], keyed?).

    Falls back to positional pairing when items are not dicts, have no key
    function, or keys are missing/duplicated — identity matching on an
    ambiguous key would invent changes.
    """
    keyfn = LIST_KEYS.get(list_field)
    if keyfn and all(isinstance(x, dict) for x in old + new):
        ko = [keyfn(x) for x in old]
        kn = [keyfn(x) for x in new]
        if None not in ko + kn and len(set(ko)) == len(ko) and len(set(kn)) == len(kn):
            om, nm = dict(zip(ko, old)), dict(zip(kn, new))
            order = kn + [k for k in ko if k not in nm]
            return [(str(k), om.get(k), nm.get(k)) for k in order], True
    if all(not isinstance(x, (dict, list)) for x in old + new):
        # Scalar lists: set semantics (definition_references, synonyms, ...).
        so = {_ws(x): x for x in old}
        sn = {_ws(x): x for x in new}
        order = list(sn) + [k for k in so if k not in sn]
        return [(str(sn.get(k, so.get(k))), so.get(k), sn.get(k)) for k in order], True
    n = max(len(old), len(new))
    return [(f"#{i + 1}", old[i] if i < len(old) else None,
             new[i] if i < len(new) else None) for i in range(n)], False


def diff_value(old: Any, new: Any, *, file: str, entity: str, entity_id: str,
               path: list[str], field_path: list[str],
               list_field: str | None = None) -> list[Change]:
    """Recursive structural diff of one value. `list_field` is set when the
    value is an item of that list (it decides the change kind on add/remove)."""
    if _equal(old, new):
        return []

    def mk(op: str, kind: str, o: Any, n: Any) -> Change:
        return Change(file=file, entity=entity, entity_id=entity_id, op=op,
                      path=list(path), kind=kind, old=o, new=n,
                      severity=_severity(entity, field_path),
                      field_path=list(field_path))

    # A list appearing or disappearing is a set of item additions/removals, so
    # each item gets its own record (and its own identity-matched path).
    if isinstance(new, list) and _empty(old):
        old = []
    elif isinstance(old, list) and _empty(new):
        new = []

    if (_empty(old) or _empty(new)) and not (isinstance(old, list) and isinstance(new, list)):
        op = "added" if _empty(old) else "removed"
        val = new if op == "added" else old
        if list_field is not None:
            kind = _item_kind(list_field)
        elif isinstance(val, (dict, list)):
            kind = "block"
        else:
            kind = "prose" if _is_prose(field_path[-1] if field_path else "", old, new) \
                else "scalar"
            return [mk("modified", kind, old, new)]
        return [mk(op, kind, old, new)]

    if isinstance(old, dict) and isinstance(new, dict):
        out: list[Change] = []
        for k in list(new) + [k for k in old if k not in new]:
            out += diff_value(old.get(k), new.get(k), file=file, entity=entity,
                              entity_id=entity_id, path=path + [k],
                              field_path=field_path + [k])
        return out

    if isinstance(old, list) and isinstance(new, list):
        lf = field_path[-1] if field_path else ""
        pairs, _ = _match(lf, old, new)
        out = []
        for disp, o, n in pairs:
            out += diff_value(o, n, file=file, entity=entity, entity_id=entity_id,
                              path=path + [disp], field_path=field_path,
                              list_field=lf)
        return out

    if isinstance(old, (dict, list)) or isinstance(new, (dict, list)):
        return [mk("modified", "block", old, new)]

    kind = "prose" if _is_prose(field_path[-1] if field_path else "", old, new) else "scalar"
    return [mk("modified", kind, old, new)]


# ── Graph-level diff ────────────────────────────────────────────────────────


def _entity_kind(node: dict) -> str:
    return "stub" if is_stub(node) else "node"


def diff_graphs(base: dict | None, head: dict | None, *, path: str) -> list[Change]:
    """Diff two parsed KB graph documents (either may be None: added/removed file).

    File-level fields are only compared when the file exists on both sides: for
    an added or removed file they are the wrapper around its nodes, and listing
    them as changes is noise.
    """
    whole_file = base is None or head is None
    base = base or {}
    head = head or {}
    out: list[Change] = []

    for coll, default_kind in (("nodes", "node"), ("edges", "edge")):
        bo = {x["id"]: x for x in base.get(coll) or [] if isinstance(x, dict) and x.get("id")}
        hn = {x["id"]: x for x in head.get(coll) or [] if isinstance(x, dict) and x.get("id")}
        for eid in list(hn) + [k for k in bo if k not in hn]:
            o, n = bo.get(eid), hn.get(eid)
            ent = _entity_kind(n if n is not None else o or {}) \
                if coll == "nodes" else default_kind
            if o is None or n is None:
                out.append(Change(
                    file=path, entity=ent, entity_id=eid,
                    op="added" if o is None else "removed", path=[], kind="entity",
                    old=o, new=n,
                    severity="metadata" if ent == "stub" else "identity"))
                continue
            for k in list(n) + [k for k in o if k not in n]:
                if k == "id":
                    continue
                out += diff_value(o.get(k), n.get(k), file=path, entity=ent,
                                  entity_id=eid, path=[k], field_path=[k])

    for k in ([] if whole_file else list(head) + [k for k in base if k not in head]):
        if k in ("nodes", "edges"):
            continue
        out += diff_value(base.get(k), head.get(k), file=path, entity="graph",
                          entity_id=Path(path).name, path=[k], field_path=[k])
    return out


def diff_files(pairs: Iterable[tuple[str, dict | None, dict | None]]) -> list[Change]:
    """Diff many files and fold cross-file moves of canonical nodes.

    A node removed from one file and added to another in the same change set
    (e.g. a `split-graph` re-split) becomes one `moved` record plus the diff of
    its body, instead of an unrelated remove and add.
    """
    changes: list[Change] = []
    for path, b, h in pairs:
        changes += diff_graphs(b, h, path=path)

    added = {c.entity_id: c for c in changes
             if c.kind == "entity" and c.op == "added" and c.entity == "node"}
    removed = {c.entity_id: c for c in changes
               if c.kind == "entity" and c.op == "removed" and c.entity == "node"}
    moved = set(added) & set(removed)
    if not moved:
        return changes

    out = [c for c in changes
           if not (c.kind == "entity" and c.entity == "node" and c.entity_id in moved)]
    for nid in moved:
        a, r = added[nid], removed[nid]
        out.append(Change(file=a.file, entity="node", entity_id=nid, op="moved",
                          path=[], kind="entity", old=r.old, new=a.new,
                          severity="identity", moved_from=r.file))
        for k in list(a.new) + [k for k in r.old if k not in a.new]:
            if k == "id":
                continue
            for c in diff_value(r.old.get(k), a.new.get(k), file=a.file, entity="node",
                                entity_id=nid, path=[k], field_path=[k]):
                c.moved_from = r.file
                out.append(c)
    return out


def sort_changes(changes: list[Change]) -> list[Change]:
    """Stable sort: by file, entity, then severity — keeps diff order otherwise."""
    rank = {s: i for i, s in enumerate(SEVERITY_ORDER)}
    return sorted(changes, key=lambda c: (c.file, c.entity_id, rank.get(c.severity, 9)))


# ── Git access ──────────────────────────────────────────────────────────────


def _git(args: list[str], cwd: Path) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True,
                          capture_output=True, text=True).stdout


def merge_base(base_ref: str, cwd: Path) -> str:
    """Three-dot semantics, as a GitHub PR diff: compare against the merge base."""
    return _git(["merge-base", base_ref, "HEAD"], cwd).strip()


def changed_paths(base_commit: str, cwd: Path,
                  pathspecs: tuple[str, ...] = ("kb/graphs", "references")) -> list[str]:
    """Paths changed between `base_commit` and the working tree, plus untracked.

    The working tree, not HEAD, so a local run reviews uncommitted edits too;
    in CI the working tree *is* the PR head.
    """
    tracked = _git(["diff", "--name-only", base_commit, "--", *pathspecs], cwd).split()
    untracked = _git(["ls-files", "--others", "--exclude-standard", "--", *pathspecs],
                     cwd).split()
    return sorted(set(tracked) | set(untracked))


def read_at(ref: str, path: str, cwd: Path) -> str | None:
    """File content at a git ref, or None if it does not exist there."""
    r = subprocess.run(["git", "show", f"{ref}:{path}"], cwd=cwd,
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def read_head(path: str, cwd: Path) -> str | None:
    p = cwd / path
    return p.read_text(encoding="utf-8") if p.is_file() else None


def load_yaml(text: str | None) -> dict | None:
    if text is None:
        return None
    doc = yaml.safe_load(text)
    return doc if isinstance(doc, dict) else {}


def is_graph_path(p: str) -> bool:
    return p.startswith("kb/graphs/") and p.endswith(".yaml")


# ── Reference store ─────────────────────────────────────────────────────────

_PAPER_IDENTITY = ("corpus_id", "title", "year", "authors", "pmid", "doi")


def region_of(path: str) -> str | None:
    parts = Path(path).parts
    for anchor in ("graphs", "references"):
        if anchor in parts:
            i = parts.index(anchor)
            if i + 1 < len(parts):
                return parts[i + 1]
    return None


def diff_reference_store(paths: list[str], base_commit: str, cwd: Path) -> dict:
    """Summarise changes under references/{region}/ between base and working tree.

    Returns {"papers_added": [...], "identity_changes": [...],
             "quotes_added": {key: quote}, "quotes_removed": [...],
             "quote_text_changed": [...], "claims_edits": {corpus_id: n},
             "other_quote_edits": n}
    """
    out: dict[str, Any] = {
        "papers_added": [], "identity_changes": [], "quotes_added": {},
        "quotes_removed": [], "quote_text_changed": [], "claims_edits": {},
        "other_quote_edits": 0,
    }
    for p in paths:
        pp = Path(p)
        if not (p.startswith("references/") and pp.suffix == ".json"):
            continue
        kind = pp.parent.name
        if kind not in ("papers", "quotes"):
            continue
        b_txt, h_txt = read_at(base_commit, p, cwd), read_head(p, cwd)
        b = json.loads(b_txt) if b_txt else None
        h = json.loads(h_txt) if h_txt else None
        if kind == "papers":
            if b is None and h is not None:
                out["papers_added"].append(h)
            elif b is not None and h is not None:
                for f in _PAPER_IDENTITY:
                    if not _equal(b.get(f), h.get(f)):
                        out["identity_changes"].append(
                            {"corpus_id": pp.stem, "field": f,
                             "old": b.get(f), "new": h.get(f)})
            elif b is not None:
                out["identity_changes"].append(
                    {"corpus_id": pp.stem, "field": "(paper record deleted)",
                     "old": b.get("title"), "new": None})
            continue
        bq, hq = b or {}, h or {}
        for k, q in hq.items():
            if not isinstance(q, dict):
                continue
            if k not in bq:
                out["quotes_added"][k] = q
                continue
            o = bq[k]
            if not _equal(o.get("text"), q.get("text")):
                out["quote_text_changed"].append(k)
            if not _equal(o.get("claims"), q.get("claims")):
                out["claims_edits"][pp.stem] = out["claims_edits"].get(pp.stem, 0) + 1
            rest_o = {x: y for x, y in o.items() if x not in ("text", "claims")}
            rest_h = {x: y for x, y in q.items() if x not in ("text", "claims")}
            if not _equal(rest_o, rest_h):
                out["other_quote_edits"] += 1
        out["quotes_removed"] += [k for k in bq if k not in hq]
    return out


# ── Checks on content the diff introduces ───────────────────────────────────


def walk_sources(value: Any) -> Iterable[dict]:
    """Every PropertySource dict nested anywhere under `value`."""
    if isinstance(value, dict):
        for k, v in value.items():
            if k == "sources" and isinstance(v, list):
                yield from (s for s in v if isinstance(s, dict))
            else:
                yield from walk_sources(v)
    elif isinstance(value, list):
        for v in value:
            yield from walk_sources(v)


def introduced_sources(changes: list[Change]) -> list[tuple[Change, dict]]:
    out = []
    for c in changes:
        if c.op not in ("added", "moved") or c.entity not in ("node", "graph"):
            continue
        if c.kind == "source" and isinstance(c.new, dict):
            out.append((c, c.new))
        elif c.kind in ("entity", "block", "list_item") and c.op == "added":
            out += [(c, s) for s in walk_sources(c.new)]
    return out


def introduced_evidence(changes: list[Change]) -> list[tuple[Change, dict]]:
    out = []
    for c in changes:
        if c.entity != "edge" or c.op != "added":
            continue
        if c.kind == "evidence" and isinstance(c.new, dict):
            out.append((c, c.new))
        elif c.kind == "entity" and isinstance(c.new, dict):
            out += [(c, e) for e in c.new.get("evidence") or [] if isinstance(e, dict)]
    return out


def _corpus_ids_for_ref(ref: str, papers: dict) -> list[str]:
    r = str(ref).strip()
    if r.upper().startswith("PMID:"):
        pmid = r.split(":", 1)[1].strip()
        return [cid for cid, p in papers.items() if str(p.get("pmid") or "") == pmid]
    doi = r
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:", "DOI:"):
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
    doi = doi.lower()
    return [cid for cid, p in papers.items() if str(p.get("doi") or "").lower() == doi]


def snippet_is_stored(snippet: str, ref: str, quotes: dict, papers: dict) -> bool | None:
    """True if every fragment of `snippet` is a substring of a stored quote of
    the cited paper. None if the reference does not resolve in the store."""
    cids = _corpus_ids_for_ref(ref, papers)
    if not cids:
        return None
    texts = [norm_text(q.get("text") or "") for k, q in quotes.items()
             if k.split("_")[0] in cids]
    s = norm_text(snippet).strip().strip("\"'“”‘’").strip()
    frags = [f.strip(" .\"'“”") for f in s.replace("…", "...").split("...")]
    frags = [f for f in frags if f]
    return bool(frags) and all(any(f in t for t in texts) for f in frags)


@dataclass
class Warning_:
    file: str
    entity_id: str
    message: str

    def to_dict(self) -> dict:
        return asdict(self)


def check_changes(changes: list[Change], stores: dict[str, tuple[dict, dict]]
                  ) -> list[Warning_]:
    """Loud checks on content the diff introduces. `stores` maps region →
    (quotes, papers) at head."""
    warns: list[Warning_] = []
    for c, s in introduced_sources(changes):
        quotes, _ = stores.get(region_of(c.file) or "", ({}, {}))
        qk = s.get("quote_key")
        if qk and qk not in quotes:
            warns.append(Warning_(c.file, c.entity_id,
                                  f"quote_key `{qk}` NOT FOUND in the reference store"))
        elif not qk and s.get("ref"):
            warns.append(Warning_(c.file, c.entity_id,
                                  f"source cites `{s['ref']}` with no quote_key"))
    for c, e in introduced_evidence(changes):
        if e.get("evidence_type") != "LITERATURE" or not e.get("snippet"):
            continue
        quotes, papers = stores.get(region_of(c.file) or "", ({}, {}))
        ok = snippet_is_stored(e["snippet"], e.get("reference") or "", quotes, papers)
        if ok is None:
            warns.append(Warning_(c.file, c.entity_id,
                                  f"evidence reference `{e.get('reference')}` is not in the "
                                  "region's reference store; snippet cannot be verified"))
        elif not ok:
            warns.append(Warning_(c.file, c.entity_id,
                                  f"evidence snippet for `{e.get('reference')}` is not a "
                                  "verbatim substring of any stored quote of that paper"))
    return warns


def cited_quote_keys(docs: Iterable[dict | None], quotes: dict) -> set[str]:
    """Quote keys cited by these docs: by key anywhere (sources, or a key named
    in `notes`), or by an edge snippet matching the quote's text."""
    keys: set[str] = set()
    snippets: list[str] = []
    for d in docs:
        if not d:
            continue
        blob = json.dumps(d, default=str)
        keys |= {k for k in quotes if k in blob}
        for e in d.get("edges") or []:
            for ev in (e or {}).get("evidence") or []:
                if isinstance(ev, dict) and ev.get("snippet"):
                    snippets.append(norm_text(ev["snippet"]).strip("\"'“” "))
    if snippets:
        for k, q in quotes.items():
            t = norm_text(q.get("text") or "")
            if any(sn and (sn in t or t in sn) for sn in snippets):
                keys.add(k)
    return keys
