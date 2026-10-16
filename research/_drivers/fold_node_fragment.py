#!/usr/bin/env python3
"""Fold a standalone single-node fragment into a KB mapping graph, replacing
the existing node with the same ``id`` in place.

This is a REPLACE, not an additive merge. ``merge_ingest_into_mapping.py``
unions fields and has no removal path, which would silently preserve data an
ingest is meant to delete (e.g. a wrong defining marker, an orphan reference).

The fragment must be a standalone, schema-valid ``CellTypeMappingGraph``
document containing exactly one entry under ``nodes``. Everything else in the
target graph — other nodes, all edges, the header — is left untouched.

Usage:
    uv run python research/_drivers/fold_node_fragment.py FRAGMENT TARGET [--dry-run]
"""

from __future__ import annotations

import argparse
import difflib
import io
import sys
from pathlib import Path

from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096
yaml.indent(mapping=2, sequence=4, offset=2)


def dump_str(data) -> str:
    buf = io.StringIO()
    yaml.dump(data, buf)
    return buf.getvalue()


def load_fragment_node(fragment_path: Path) -> dict:
    frag = yaml.load(fragment_path.read_text(encoding="utf-8"))
    nodes = frag.get("nodes") or []
    if len(nodes) != 1:
        sys.exit(
            f"ERROR: fragment {fragment_path} must contain exactly one node, "
            f"found {len(nodes)}."
        )
    node = nodes[0]
    if not node.get("id"):
        sys.exit(f"ERROR: fragment node in {fragment_path} has no id.")
    return node


def fold(fragment_path: Path, target_path: Path, dry_run: bool) -> int:
    node = load_fragment_node(fragment_path)
    node_id = node["id"]

    original_text = target_path.read_text(encoding="utf-8")
    target = yaml.load(original_text)
    nodes = target.get("nodes")
    if nodes is None:
        sys.exit(f"ERROR: target {target_path} has no 'nodes' list.")

    positions = [i for i, n in enumerate(nodes) if n.get("id") == node_id]
    if len(positions) != 1:
        sys.exit(
            f"ERROR: expected exactly one node with id '{node_id}' in "
            f"{target_path}, found {len(positions)}."
        )
    idx = positions[0]

    edges_before = len(target.get("edges") or [])
    nodes_before = len(nodes)

    nodes[idx] = node

    assert len(nodes) == nodes_before
    assert len(target.get("edges") or []) == edges_before

    new_text = dump_str(target)

    diff = "".join(
        difflib.unified_diff(
            original_text.splitlines(keepends=True),
            new_text.splitlines(keepends=True),
            fromfile=f"a/{target_path}",
            tofile=f"b/{target_path}",
        )
    )
    if not diff:
        print(f"No change: node '{node_id}' already matches the fragment.")
        return 0

    print(diff)
    added = sum(1 for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++"))
    removed = sum(1 for line in diff.splitlines() if line.startswith("-") and not line.startswith("---"))
    print(
        f"\nNode '{node_id}' replaced at position {idx}/{nodes_before}; "
        f"{added} lines added, {removed} removed; "
        f"{edges_before} edges untouched."
    )

    if dry_run:
        print("--dry-run: no write performed.")
        return 0

    target_path.write_text(new_text, encoding="utf-8")
    print(f"Wrote {target_path}.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("fragment", type=Path)
    ap.add_argument("target", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    return fold(args.fragment, args.target, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
