"""Taxonomy-indexed table of contents for mapping reports.

Generates a markdown contents page indexed by the taxonomy hierarchy,
listing classical-type mapping reports whose confidence meets a threshold.
Branches without qualifying content are pruned.

CLI:
  python -m evidencell.toc <taxonomy_id> [--root ACCESSION]
                           [--min-confidence MODERATE]
                           [--output PATH]
  python -m evidencell.toc --all [--min-confidence MODERATE]
                                 [--output PATH]
"""

from __future__ import annotations

import argparse
import re
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
    relationship: str | None = None


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
                    relationship=edge.get("relationship"),
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


def _load_enum_descriptions(enum_name: str) -> dict[str, str]:
    """Read permissible-value descriptions for a LinkML enum from the schema.

    Returns {} if the schema is missing (e.g. in test fixtures with a
    monkeypatched repo_root).
    """
    schema_path = repo_root() / "schema" / "celltype_mapping.yaml"
    if not schema_path.exists():
        return {}
    try:
        data = yaml.safe_load(schema_path.read_text())
    except Exception:
        return {}
    enum = (data.get("enums") or {}).get(enum_name) or {}
    out: dict[str, str] = {}
    for value, body in (enum.get("permissible_values") or {}).items():
        if not isinstance(body, dict):
            continue
        desc = body.get("description") or ""
        # Collapse whitespace from folded YAML scalars.
        out[value] = " ".join(desc.split())
    return out


def _collect_used_terms(roots: list[TaxonomyNode]) -> tuple[set[str], set[str]]:
    """Walk surviving tree; return (relationships_used, confidences_used)."""
    rels: set[str] = set()
    confs: set[str] = set()
    stack = list(roots)
    while stack:
        node = stack.pop()
        for edge in node.edges:
            if edge.relationship:
                rels.add(edge.relationship)
            confs.add(edge.confidence)
        stack.extend(node.children)
    return rels, confs


def _render_glossary(
    rels_used: set[str],
    confs_used: set[str],
    *,
    heading_offset: int = 0,
) -> list[str]:
    """Emit a glossary section for the relationship + confidence terms in use."""
    if not rels_used and not confs_used:
        return []
    rel_descs = _load_enum_descriptions("MappingRelationship")
    conf_descs = _load_enum_descriptions("MappingConfidence")
    h = "#" * (2 + heading_offset)
    sub = "#" * (3 + heading_offset)
    lines = [f"{h} Glossary", ""]
    if rels_used:
        lines += [f"{sub} Mapping relationship", ""]
        for term in sorted(rels_used):
            desc = rel_descs.get(term, "")
            lines.append(f"- **{term}** — {desc}" if desc else f"- **{term}**")
        lines.append("")
    if confs_used:
        lines += [f"{sub} Mapping confidence", ""]
        for term in sorted(confs_used, key=lambda c: -CONFIDENCE_ORDER.index(c) if c in CONFIDENCE_ORDER else 0):
            desc = conf_descs.get(term, "")
            lines.append(f"- **{term}** — {desc}" if desc else f"- **{term}**")
        lines.append("")
    return lines


def slugify(value: str) -> str:
    """Filename-safe slug: keep alphanumerics + hyphens, replace runs of other chars with `_`."""
    value = re.sub(r"[^A-Za-z0-9-]+", "_", value).strip("_")
    return value or "untitled"


def render_markdown(
    roots: list[TaxonomyNode],
    taxonomy_meta: dict,
    min_confidence: str,
    *,
    heading_offset: int = 0,
    include_header: bool = True,
    include_glossary: bool = True,
) -> str:
    """Render a single taxonomy's tree as markdown.

    `heading_offset` shifts every emitted heading down by N levels; used by
    the combined `--all` renderer so each taxonomy gets its own H2 with
    children pushed one level deeper.
    """
    name = taxonomy_meta.get("taxonomy_name", taxonomy_meta.get("taxonomy_id", "Taxonomy"))
    tax_id = taxonomy_meta.get("taxonomy_id", "")
    species = taxonomy_meta.get("species_label", "")
    source_file = taxonomy_meta.get("source_file", "")

    lines: list[str] = []
    if include_header:
        lines += [
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

    if include_glossary:
        rels_used, confs_used = _collect_used_terms(roots)
        lines += _render_glossary(rels_used, confs_used, heading_offset=heading_offset)

    top_rank = max((r.rank for r in roots), default=0)

    for root in roots:
        _emit_node(root, top_rank=top_rank, lines=lines, heading_offset=heading_offset)

    return "\n".join(lines) + ("\n" if not lines or lines[-1] != "" else "")


def _emit_node(
    node: TaxonomyNode,
    top_rank: int,
    lines: list[str],
    heading_offset: int = 0,
) -> None:
    depth = _heading_depth_for(node.rank, top_rank) + heading_offset
    depth = min(depth, 6)
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
            tags = " · ".join(t for t in (edge.relationship, edge.confidence) if t)
            if link:
                lines.append(f"- [{label}]({link}) — {tags}")
            else:
                lines.append(f"- {label} — {tags} _(no report file)_")
        lines.append("")
    for child in node.children:
        _emit_node(child, top_rank, lines, heading_offset=heading_offset)


def _build_taxonomy(
    taxonomy_id: str,
    root_accession: str | None,
    min_confidence: str,
) -> tuple[list[TaxonomyNode], dict, TaxonomyNode | None]:
    """Shared pipeline: nodes → edges → tree → prune. Returns (surviving_roots, meta, root_node).

    `root_node` is the requested subtree root if `root_accession` was given, else None.
    """
    nodes = load_taxonomy_tree(taxonomy_id, root_accession=root_accession)
    edges = [e for e in load_mappings() if e.taxonomy_node_id in nodes]
    attach_edges(nodes, edges, min_confidence)
    roots = build_tree(nodes)
    surviving_roots = [r for r in roots if prune_empty(r)]
    meta_path = taxonomy_meta_path(taxonomy_id)
    meta = (
        yaml.safe_load(meta_path.read_text())
        if meta_path.exists()
        else {"taxonomy_id": taxonomy_id}
    )
    root_node = nodes.get(root_accession) if root_accession else None
    return surviving_roots, meta, root_node


def generate(
    taxonomy_id: str,
    root_accession: str | None = None,
    min_confidence: str = "MODERATE",
) -> str:
    """End-to-end: load DB + mappings, build pruned tree, render markdown."""
    surviving_roots, meta, _ = _build_taxonomy(taxonomy_id, root_accession, min_confidence)
    return render_markdown(surviving_roots, meta, min_confidence)


def list_taxonomy_ids() -> list[str]:
    """Return all taxonomy IDs that have a built SQLite DB under kb/taxonomy/."""
    tax_dir = repo_root() / "kb" / "taxonomy"
    if not tax_dir.exists():
        return []
    out = []
    for sub in sorted(tax_dir.iterdir()):
        if sub.is_dir() and (sub / f"{sub.name}.db").exists():
            out.append(sub.name)
    return out


def generate_all(min_confidence: str = "MODERATE") -> str:
    """Combined TOC across all taxonomies. H1 title; each taxonomy gets H2 + offset children."""
    taxonomy_ids = list_taxonomy_ids()
    lines = [
        "# Taxonomy-indexed mapping reports",
        "",
        f"Minimum mapping confidence: **{min_confidence.upper()}**",
        "",
    ]
    if not taxonomy_ids:
        lines.append("_No taxonomies found under `kb/taxonomy/`._")
        return "\n".join(lines) + "\n"

    rendered: list[tuple[dict, list[TaxonomyNode], str]] = []
    for tax_id in taxonomy_ids:
        surviving_roots, meta, _ = _build_taxonomy(tax_id, None, min_confidence)
        if not surviving_roots:
            continue
        rendered.append((meta, surviving_roots, tax_id))

    if not rendered:
        lines.append("_No mapping reports meet the confidence threshold._")
        return "\n".join(lines).rstrip() + "\n"

    # One unified glossary at the top, covering every taxonomy in the report.
    rels_used: set[str] = set()
    confs_used: set[str] = set()
    for _, roots, _ in rendered:
        r, c = _collect_used_terms(roots)
        rels_used |= r
        confs_used |= c
    lines += _render_glossary(rels_used, confs_used)

    for meta, surviving_roots, tax_id in rendered:
        name = meta.get("taxonomy_name", tax_id)
        species = meta.get("species_label", "")
        lines.append(f"## {name}")
        lines.append("")
        meta_bits = [f"`{tax_id}`"]
        if species:
            meta_bits.append(species)
        lines.append(" · ".join(meta_bits))
        lines.append("")
        body = render_markdown(
            surviving_roots,
            meta,
            min_confidence,
            heading_offset=1,
            include_header=False,
            include_glossary=False,
        )
        lines.append(body.rstrip())
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _default_output_path(
    taxonomy_id: str,
    root_accession: str | None,
    taxonomy_meta: dict | None = None,
    root_node: TaxonomyNode | None = None,
) -> Path:
    """Build a human-readable default path under reports/_toc/.

    Full taxonomy → `{TaxonomyName}.md`
    Subtree      → `{TaxonomyName}__{NodeLabel}.md`

    Falls back to IDs when name/label lookups are unavailable.
    """
    out_dir = repo_root() / "reports" / "_toc"
    tax_slug = slugify((taxonomy_meta or {}).get("taxonomy_name") or taxonomy_id)
    if root_accession:
        node_slug = slugify(root_node.label if root_node else root_accession)
        return out_dir / f"{tax_slug}__{node_slug}.md"
    return out_dir / f"{tax_slug}.md"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("taxonomy_id", nargs="?", help="Taxonomy ID (omit when using --all).")
    parser.add_argument("--all", action="store_true", help="Combined TOC across every taxonomy.")
    parser.add_argument("--root", help="Root accession to scope a subtree.")
    parser.add_argument(
        "--min-confidence",
        default="MODERATE",
        choices=CONFIDENCE_ORDER,
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    if args.all:
        if args.taxonomy_id or args.root:
            parser.error("--all is incompatible with positional taxonomy_id or --root")
        markdown = generate_all(min_confidence=args.min_confidence)
        out = args.output or (repo_root() / "reports" / "_toc" / "all_taxonomies.md")
    else:
        if not args.taxonomy_id:
            parser.error("taxonomy_id is required unless --all is given")
        surviving_roots, meta, root_node = _build_taxonomy(
            args.taxonomy_id, args.root, args.min_confidence
        )
        markdown = render_markdown(surviving_roots, meta, args.min_confidence)
        out = args.output or _default_output_path(
            args.taxonomy_id, args.root, taxonomy_meta=meta, root_node=root_node
        )

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(markdown)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
