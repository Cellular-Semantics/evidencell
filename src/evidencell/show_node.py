"""
show_node — print a concise NODE_CONTEXT summary for a given node_id.

Usage:
    uv run python -m evidencell.show_node <kb_file> <node_id>
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


def node_context(kb_file: Path, node_id: str) -> str:
    """Return a NODE_CONTEXT string for the given node, or raise ValueError."""
    doc = yaml.safe_load(kb_file.read_text(encoding="utf-8"))
    nodes = doc.get("nodes") or []
    node = next((n for n in nodes if n.get("id") == node_id), None)
    if node is None:
        raise ValueError(f"Node '{node_id}' not found in {kb_file}")

    markers = [m.get("symbol", "?") for m in (node.get("defining_markers") or [])]
    locs = [loc.get("label", "?") for loc in (node.get("anatomical_location") or [])]
    nt = (node.get("nt_type") or {}).get("name_in_source", "unknown")

    lines = [
        f"NODE: {node_id} — {node.get('name', '?')}",
        f"Markers: {', '.join(markers) or 'not yet characterised'}",
        f"Anatomy: {', '.join(locs) or 'unknown'}",
        f"NT type: {nt}",
    ]
    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python -m evidencell.show_node <kb_file> <node_id>", file=sys.stderr)
        sys.exit(1)
    kb_file = Path(sys.argv[1])
    node_id = sys.argv[2]
    try:
        print(node_context(kb_file, node_id))
    except (ValueError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
