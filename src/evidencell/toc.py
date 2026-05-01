"""Taxonomy-indexed table of contents for mapping reports.

Generates a markdown contents page indexed by the taxonomy hierarchy,
listing classical-type mapping reports whose confidence meets a threshold.
Branches without qualifying content are pruned.

CLI:
  python -m evidencell.toc <taxonomy_id> [--root ACCESSION]
                           [--min-confidence MODERATE]
                           [--output PATH]
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import yaml

from evidencell.paths import (
    repo_root,
    reports_dir_for_region,
    taxonomy_db_path,
    taxonomy_meta_path,
)

CONFIDENCE_ORDER = ["REFUTED", "UNCERTAIN", "LOW", "MODERATE", "HIGH"]


def _confidence_rank(value: str | None) -> int:
    if value is None:
        return -1
    try:
        return CONFIDENCE_ORDER.index(value.upper())
    except ValueError:
        return -1


@dataclass
class Edge:
    classical_id: str
    taxonomy_node_id: str
    confidence: str
    region: str
    source_file: Path


@dataclass
class TaxonomyNode:
    node_id: str
    label: str
    level: str
    rank: int
    parent_id: str | None
    children: list["TaxonomyNode"] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)


def load_mappings(kb_root: Path | None = None) -> list[Edge]:
    """Scan kb/draft and kb/mappings for MappingEdges. Graduated wins on duplicates."""
    root = kb_root or (repo_root() / "kb")
    by_classical_target: dict[tuple[str, str], Edge] = {}
    # Process draft first, then mappings (graduated overwrites draft).
    for sub in ("draft", "mappings"):
        sub_dir = root / sub
        if not sub_dir.exists():
            continue
        for yaml_file in sorted(sub_dir.rglob("*.yaml")):
            try:
                with yaml_file.open() as fh:
                    data = yaml.safe_load(fh)
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            edges = data.get("edges") or []
            region = _region_from_path(yaml_file)
            for edge in edges:
                if not isinstance(edge, dict):
                    continue
                a = edge.get("type_a")
                b = edge.get("type_b")
                conf = edge.get("confidence")
                if not (a and b and conf):
                    continue
                key = (a, b)
                by_classical_target[key] = Edge(
                    classical_id=a,
                    taxonomy_node_id=b,
                    confidence=conf,
                    region=region,
                    source_file=yaml_file,
                )
    return list(by_classical_target.values())


def _region_from_path(yaml_file: Path) -> str:
    parts = yaml_file.resolve().parts
    for i, part in enumerate(parts):
        if part == "kb" and i + 2 < len(parts):
            return parts[i + 2]
    return "unknown"


def find_report_file(region: str, classical_id: str) -> Path | None:
    """Return the report file for a classical node, or None if absent."""
    candidate = reports_dir_for_region(region) / f"{classical_id}_summary.md"
    return candidate if candidate.exists() else None


def load_taxonomy_tree(
    taxonomy_id: str,
    root_accession: str | None = None,
) -> dict[str, TaxonomyNode]:
    """Load nodes from the taxonomy SQLite DB into a node_id → TaxonomyNode dict.

    If `root_accession` is given, restricts to that node and its descendants.
    """
    db_path = taxonomy_db_path(taxonomy_id)
    if not db_path.exists():
        raise FileNotFoundError(
            f"Taxonomy DB not found: {db_path}. "
            "Run 'just build-taxonomy-db {taxonomy_id}' first."
        )
    conn = sqlite3.connect(db_path)
    try:
        rows = conn.execute(
            "SELECT node_id, label, taxonomy_level, taxonomy_rank, parent_id FROM nodes"
        ).fetchall()
    finally:
        conn.close()
    nodes: dict[str, TaxonomyNode] = {
        row[0]: TaxonomyNode(
            node_id=row[0],
            label=row[1],
            level=row[2],
            rank=row[3] if row[3] is not None else -1,
            parent_id=row[4],
        )
        for row in rows
    }
    if root_accession is not None:
        if root_accession not in nodes:
            raise ValueError(
                f"Root accession '{root_accession}' not found in taxonomy {taxonomy_id}."
            )
        keep: set[str] = set()
        stack = [root_accession]
        children_index: dict[str, list[str]] = defaultdict(list)
        for n in nodes.values():
            if n.parent_id:
                children_index[n.parent_id].append(n.node_id)
        while stack:
            cur = stack.pop()
            if cur in keep:
                continue
            keep.add(cur)
            stack.extend(children_index.get(cur, []))
        nodes = {nid: n for nid, n in nodes.items() if nid in keep}
        # Detach root parent so it renders as the top of the tree.
        nodes[root_accession].parent_id = None
    return nodes


def attach_edges(
    nodes: dict[str, TaxonomyNode],
    edges: Iterable[Edge],
    min_confidence: str,
) -> None:
    """Attach edges to taxonomy nodes, filtered by confidence threshold."""
    threshold = _confidence_rank(min_confidence)
    if threshold < 0:
        raise ValueError(f"Unknown confidence: {min_confidence}")
    for edge in edges:
        if _confidence_rank(edge.confidence) < threshold:
            continue
        node = nodes.get(edge.taxonomy_node_id)
        if node is None:
            continue
        node.edges.append(edge)


def build_tree(nodes: dict[str, TaxonomyNode]) -> list[TaxonomyNode]:
    """Wire parent/child links; return root nodes (parent_id is None or absent)."""
    roots: list[TaxonomyNode] = []
    for node in nodes.values():
        if node.parent_id and node.parent_id in nodes:
            nodes[node.parent_id].children.append(node)
        else:
            roots.append(node)
    # Sort children by label for stable output.
    for node in nodes.values():
        node.children.sort(key=lambda n: n.label)
    roots.sort(key=lambda n: n.label)
    return roots


def prune_empty(node: TaxonomyNode) -> bool:
    """Recursively prune branches with no edges. Return True if node has content."""
    surviving = []
    for child in node.children:
        if prune_empty(child):
            surviving.append(child)
    node.children = surviving
    return bool(node.edges) or bool(node.children)


def _level_label(level: str) -> str:
    mapping = {
        "class": "Class",
        "subclass": "Subclass",
        "supertype": "Supertype",
        "cluster": "Cluster",
        "neurotransmitter": "Neurotransmitter",
    }
    return mapping.get(level.lower(), level.title())


def _heading_depth_for(rank: int, top_rank: int) -> int:
    """H2 for top rank; descend by 1 per rank step. Capped at H6."""
    depth = 2 + (top_rank - rank)
    return min(max(depth, 2), 6)


def render_markdown(
    roots: list[TaxonomyNode],
    taxonomy_meta: dict,
    min_confidence: str,
) -> str:
    name = taxonomy_meta.get("taxonomy_name", taxonomy_meta.get("taxonomy_id", "Taxonomy"))
    tax_id = taxonomy_meta.get("taxonomy_id", "")
    species = taxonomy_meta.get("species_label", "")
    source_file = taxonomy_meta.get("source_file", "")

    lines = [
        f"# {name} — mapping contents",
        "",
        f"Taxonomy ID: `{tax_id}`" + (f" · Species: {species}" if species else ""),
    ]
    if source_file:
        lines.append(f"Source: `{source_file}`")
    lines.append(f"Minimum mapping confidence: **{min_confidence.upper()}**")
    lines.append("")

    if not roots:
        lines.append("_No mapping reports meet the confidence threshold._")
        return "\n".join(lines) + "\n"

    top_rank = max((r.rank for r in roots), default=0)

    for root in roots:
        _emit_node(root, top_rank=top_rank, lines=lines)

    return "\n".join(lines) + "\n"


def _emit_node(node: TaxonomyNode, top_rank: int, lines: list[str]) -> None:
    depth = _heading_depth_for(node.rank, top_rank)
    hashes = "#" * depth
    lines.append(f"{hashes} {_level_label(node.level)} — {node.label}")
    lines.append("")
    if node.edges:
        for edge in sorted(node.edges, key=lambda e: e.classical_id):
            report = find_report_file(edge.region, edge.classical_id)
            if report is not None:
                rel = report.relative_to(repo_root())
                # Make link relative to reports/_toc/ output location.
                link = "../" + str(rel.relative_to("reports"))
            else:
                link = ""
            label = edge.classical_id
            confidence = edge.confidence
            if link:
                lines.append(f"- [{label}]({link}) — {confidence}")
            else:
                lines.append(f"- {label} — {confidence} _(no report file)_")
        lines.append("")
    for child in node.children:
        _emit_node(child, top_rank, lines)


def generate(
    taxonomy_id: str,
    root_accession: str | None = None,
    min_confidence: str = "MODERATE",
) -> str:
    """End-to-end: load DB + mappings, build pruned tree, render markdown."""
    nodes = load_taxonomy_tree(taxonomy_id, root_accession=root_accession)
    edges = [e for e in load_mappings() if e.taxonomy_node_id in nodes]
    attach_edges(nodes, edges, min_confidence)
    roots = build_tree(nodes)
    surviving_roots = [r for r in roots if prune_empty(r)]
    meta_path = taxonomy_meta_path(taxonomy_id)
    meta = yaml.safe_load(meta_path.read_text()) if meta_path.exists() else {"taxonomy_id": taxonomy_id}
    return render_markdown(surviving_roots, meta, min_confidence)


def _default_output_path(taxonomy_id: str, root_accession: str | None) -> Path:
    out_dir = repo_root() / "reports" / "_toc"
    if root_accession:
        return out_dir / f"{taxonomy_id}_{root_accession}.md"
    return out_dir / f"{taxonomy_id}.md"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("taxonomy_id")
    parser.add_argument("--root", help="Root accession to scope a subtree.")
    parser.add_argument(
        "--min-confidence",
        default="MODERATE",
        choices=CONFIDENCE_ORDER,
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    markdown = generate(
        taxonomy_id=args.taxonomy_id,
        root_accession=args.root,
        min_confidence=args.min_confidence,
    )
    out = args.output or _default_output_path(args.taxonomy_id, args.root)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(markdown)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
