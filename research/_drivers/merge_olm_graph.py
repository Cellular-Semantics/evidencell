#!/usr/bin/env python3
"""Merge hippocampus_OLM.yaml's olm_hippocampus node into hippocampus_GABAergic_interneurons.yaml's olm_cell_ca1.

Steps:
  1. Additively merge classical-node fields from olm_hippocampus into olm_cell_ca1
     (reuses merge_node from merge_ingest_into_mapping.py).
  2. Move atlas-stub nodes from OLM graph → GABAergic graph, deduping by cell_set_accession.
  3. For each edge in OLM graph (lit_type=olm_hippocampus):
     - rename id: edge_olm_to_X → edge_olm_cell_ca1_to_X
     - set lit_type: olm_cell_ca1
     - if GABAergic graph already has an edge for the same taxonomy_type with lit_type=olm_cell_ca1: SKIP (keep
       GABAergic version which has today's curator-reviewed verdict)
     - else: move the edge over
  4. Remove olm_hippocampus node from OLM graph; remove its atlas stubs from OLM graph.
  5. Report stats; OLM graph will be near-empty afterwards (curator can retire it).

Usage:
    python research/_drivers/merge_olm_graph.py --dry-run
    python research/_drivers/merge_olm_graph.py
"""
from __future__ import annotations
import argparse
import copy
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research' / '_drivers'))
from merge_ingest_into_mapping import merge_node, yaml  # noqa: E402

SRC_GRAPH = 'kb/graphs/hippocampus/hippocampus_OLM.yaml'
DST_GRAPH = 'kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml'
SRC_LIT_ID = 'olm_hippocampus'
DST_LIT_ID = 'olm_cell_ca1'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    src_path = ROOT / SRC_GRAPH
    dst_path = ROOT / DST_GRAPH
    src_doc = yaml.load(src_path.read_text())
    dst_doc = yaml.load(dst_path.read_text())

    src_nodes = src_doc.get('nodes', [])
    dst_nodes = dst_doc.get('nodes', [])
    src_edges = src_doc.get('edges', [])
    dst_edges = dst_doc.get('edges', [])

    # ── Step 1: merge classical fields ─────────────────────────────────────
    src_classical = next((n for n in src_nodes if n.get('id') == SRC_LIT_ID), None)
    dst_classical = next((n for n in dst_nodes if n.get('id') == DST_LIT_ID), None)
    if not src_classical or not dst_classical:
        print(f'Could not locate source or dest classical node')
        return 1

    merge_stats = merge_node(dst_classical, src_classical, SRC_LIT_ID)
    print(f'\n=== Step 1: merge_node({SRC_LIT_ID} → {DST_LIT_ID}) ===')
    for k, v in merge_stats.items():
        print(f'  {k}: {v}')

    # ── Step 2: move atlas stubs ───────────────────────────────────────────
    # Build set of cell_set_accession already in dst_nodes
    dst_acc = set(n.get('cell_set_accession') for n in dst_nodes if n.get('cell_set_accession'))
    moved_stubs = []
    skipped_stubs = []
    src_atlas_stub_ids = []
    src_classical_ids = {SRC_LIT_ID}
    for n in list(src_nodes):
        if n.get('id') in src_classical_ids:
            continue  # the classical node — handled below
        if not n.get('cell_set_accession'):
            continue  # not an atlas stub
        src_atlas_stub_ids.append(n['id'])
        if n['cell_set_accession'] in dst_acc:
            skipped_stubs.append(n['id'])
        else:
            dst_nodes.append(copy.deepcopy(n))
            dst_acc.add(n['cell_set_accession'])
            moved_stubs.append(n['id'])
    print(f'\n=== Step 2: atlas stub move ===')
    print(f'  moved: {len(moved_stubs)}')
    print(f'  skipped (already present in dst): {len(skipped_stubs)}')

    # ── Step 3: redirect edges ─────────────────────────────────────────────
    # Map of existing dst edges by (lit_type, taxonomy_type)
    dst_edge_index = {
        (e.get('lit_type'), e.get('taxonomy_type')): e
        for e in dst_edges
    }
    moved_edges = []
    skipped_edges = []
    for e in list(src_edges):
        if e.get('lit_type') != SRC_LIT_ID:
            continue
        # Rewrite for dst
        new_edge = copy.deepcopy(e)
        new_edge['lit_type'] = DST_LIT_ID
        old_id = new_edge.get('id', '')
        # rename: edge_olm_to_X → edge_olm_cell_ca1_to_X (or generic substitution)
        if 'olm' in old_id:
            new_id = old_id.replace('edge_olm_to_', f'edge_{DST_LIT_ID}_to_').replace('edge_olm_hippocampus_to_', f'edge_{DST_LIT_ID}_to_')
            new_edge['id'] = new_id
        # Conflict check
        key = (new_edge['lit_type'], new_edge['taxonomy_type'])
        if key in dst_edge_index:
            skipped_edges.append({'src_id': old_id, 'reason': f'dst already has edge for {DST_LIT_ID}→{new_edge["taxonomy_type"]}'})
        else:
            dst_edges.append(new_edge)
            dst_edge_index[key] = new_edge
            moved_edges.append({'src_id': old_id, 'new_id': new_edge['id'], 'target': new_edge['taxonomy_type']})
    print(f'\n=== Step 3: edge redirect ===')
    print(f'  moved: {len(moved_edges)}')
    for m in moved_edges:
        print(f'    {m["src_id"]} → {m["new_id"]}  (target {m["target"]})')
    print(f'  skipped (already in dst): {len(skipped_edges)}')
    for s in skipped_edges:
        print(f'    {s["src_id"]}: {s["reason"]}')

    # ── Step 4: scrub src ────────────────────────────────────────────────
    # Remove classical node + all atlas stubs + all edges with lit_type = SRC_LIT_ID
    src_nodes_new = [n for n in src_nodes if n.get('id') not in src_classical_ids and n.get('id') not in src_atlas_stub_ids]
    src_edges_new = [e for e in src_edges if e.get('lit_type') != SRC_LIT_ID]
    src_doc['nodes'] = src_nodes_new
    src_doc['edges'] = src_edges_new
    print(f'\n=== Step 4: scrub src ===')
    print(f'  remaining nodes in {SRC_GRAPH}: {len(src_nodes_new)}')
    print(f'  remaining edges in {SRC_GRAPH}: {len(src_edges_new)}')

    if args.dry_run:
        print('\n--dry-run: no files written')
        return 0

    dst_doc['nodes'] = dst_nodes
    dst_doc['edges'] = dst_edges
    with dst_path.open('w') as f:
        yaml.dump(dst_doc, f)
    print(f'\nwrote {DST_GRAPH}')
    with src_path.open('w') as f:
        yaml.dump(src_doc, f)
    print(f'wrote {SRC_GRAPH}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
