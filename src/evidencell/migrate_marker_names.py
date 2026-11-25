"""One-off migration of KB markers to the #244 GeneDescriptor shape.

Before: ``symbol`` held the source's wording (paper or atlas metadata).
After:  ``name_in_source`` holds that wording; ``symbol`` is the official
symbol of ``ncbi_gene_id`` and is present only alongside it.

- Graph markers (``kb/graphs/**``): ``symbol`` → ``name_in_source``; a
  marker with ``ncbi_gene_id`` gains ``symbol`` = the gene's current label
  (NodeNormalization, via the hook's gene record cache).
- Taxonomy markers (``kb/taxonomy/**``, incl. ``.yaml.gz``): rename only.

Edits are made line by line so file formatting is untouched, and each file
is verified afterwards: the edited text must parse to exactly the expected
transform of the original (``safe_load``), or the file is left unchanged.

    python -m evidencell.migrate_marker_names [--check]
"""

from __future__ import annotations

import argparse
import copy
import gzip
import sys
from pathlib import Path
from typing import Any

import yaml
from ruamel.yaml import YAML

from evidencell.gene_identity import _GeneRecordCache, gene_id_cache_path
from evidencell.paths import repo_root

MARKER_FIELDS = (
    "defining_markers", "negative_markers", "neuropeptides", "merfish_markers", "markers",
)


def _marker_lists(doc: Any) -> list[list]:
    """Every marker list in a graph or taxonomy document: nodes[*].<field>
    and edges[*].evidence[*].<field> (atlas metadata evidence)."""
    holders: list = []
    if isinstance(doc, dict):
        holders.extend(doc.get("nodes") or [])
        for edge in doc.get("edges") or []:
            if isinstance(edge, dict):
                holders.extend(edge.get("evidence") or [])
    return [
        h[f] for h in holders if isinstance(h, dict)
        for f in MARKER_FIELDS if isinstance(h.get(f), list)
    ]


def _expected(doc: Any, labels: dict[str, str]) -> Any:
    new = copy.deepcopy(doc)
    for lst in _marker_lists(new):
        for i, m in enumerate(lst):
            if not isinstance(m, dict) or "symbol" not in m or "name_in_source" in m:
                continue
            out = {}
            for k, v in m.items():
                if k == "symbol":
                    out["name_in_source"] = v
                    if m.get("ncbi_gene_id"):
                        out["symbol"] = labels[m["ncbi_gene_id"]]
                else:
                    out[k] = v
            lst[i] = out
    return new


def _scalar(v: str) -> str:
    return yaml.safe_dump(v, default_flow_style=True, width=10**6).strip().removesuffix("\n...")


def migrate_text(text: str, labels: dict[str, str]) -> str:
    """Rename marker ``symbol`` keys in ``text`` (line edits located with
    ruamel), inserting the official ``symbol`` after ``name_in_source``
    where the marker has an ``ncbi_gene_id``."""
    doc = YAML().load(text)
    lines = text.split("\n")
    inserts: dict[int, str] = {}
    # Rightmost edits first, so earlier columns on a line stay valid.
    edits = []
    for lst in _marker_lists(doc):
        for m in lst:
            if not hasattr(m, "lc") or "symbol" not in m or "name_in_source" in m:
                continue
            edits.append((*m.lc.key("symbol"), m))
    for row, col, m in sorted(edits, key=lambda e: (e[0], -e[1])):
        line = lines[row]
        assert line[col:].startswith("symbol:"), (row, line)
        sym = _scalar(labels[m["ncbi_gene_id"]]) if m.get("ncbi_gene_id") else None
        if sym and m.fa.flow_style():
            # {symbol: X, ...}: add ", symbol: <official>" after X's value.
            vcol = m.lc.value("symbol")[1]
            end = min((i for i in (line.find(",", vcol), line.find("}", vcol)) if i >= 0))
            line = line[:end] + ", symbol: " + sym + line[end:]
        elif sym:
            inserts[row] = " " * col + "symbol: " + sym
        lines[row] = line[:col] + "name_in_source" + line[col + len("symbol"):]
    for row in sorted(inserts, reverse=True):
        lines.insert(row + 1, inserts[row])
    return "\n".join(lines)


def _read(path: Path) -> str:
    if path.suffix == ".gz":
        return gzip.decompress(path.read_bytes()).decode("utf-8")
    return path.read_text(encoding="utf-8")


def _write(path: Path, text: str) -> None:
    if path.suffix == ".gz":
        path.write_bytes(gzip.compress(text.encode("utf-8"), mtime=0))
    else:
        path.write_text(text, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="python -m evidencell.migrate_marker_names")
    p.add_argument("--check", action="store_true", help="report, don't write")
    p.add_argument("--graphs-only", action="store_true", help="skip kb/taxonomy")
    args = p.parse_args(argv)

    root = repo_root()
    graphs = sorted((root / "kb" / "graphs").rglob("*.yaml"))
    taxonomy = [] if args.graphs_only else sorted(
        f for f in (root / "kb" / "taxonomy").rglob("*")
        if f.name.endswith((".yaml", ".yaml.gz")) and f.name != "taxonomy_meta.yaml"
    )

    # Official symbols for every curated ID (graph files only carry IDs).
    ids: set[str] = set()
    for f in graphs:
        for lst in _marker_lists(yaml.safe_load(f.read_text(encoding="utf-8"))):
            ids |= {m["ncbi_gene_id"] for m in lst if isinstance(m, dict) and m.get("ncbi_gene_id")}
    cache = _GeneRecordCache(gene_id_cache_path(), root / "kb" / "taxonomy")
    records, unreachable = cache.get(ids)
    cache.save()
    bad = sorted(set(unreachable) | {i for i in ids if not records.get(i, {}).get("label")})
    if bad:
        print(f"ERROR: no official symbol for {len(bad)} ID(s): {', '.join(bad)}", file=sys.stderr)
        return 1
    labels = {i: records[i]["label"] for i in ids}

    changed = 0
    for f in [*graphs, *taxonomy]:
        text = _read(f)
        old = yaml.safe_load(text)
        new_text = migrate_text(text, labels)
        if new_text == text:
            continue
        if yaml.safe_load(new_text) != _expected(old, labels):
            print(f"ERROR: {f.relative_to(root)}: edited text does not parse to the "
                  "expected transform; left unchanged", file=sys.stderr)
            return 1
        changed += 1
        if not args.check:
            _write(f, new_text)
    print(f"{'would change' if args.check else 'changed'} {changed} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
