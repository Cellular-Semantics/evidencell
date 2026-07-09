#!/usr/bin/env python3
"""Move 4 Chamberland subfamily classical nodes + atlas stubs + edges from the
standalone hippocampus_chamberland_subfamilies.yaml graph into the general
hippocampus_GABAergic_interneurons.yaml graph (per GH #54).

Unlike merge_ingest_into_mapping (asta-ingest case) and merge_olm_graph (duplicate
node case), the Chamberland subfamilies are LEGITIMATELY DISTINCT from the existing
classical types in the destination graph (e.g. chrna2_olm_subfamily_chamberland is
not the same node as olm_cell_ca1). The move is a structural relocation — no
classical-field merging.

Steps:
  1. Move the 4 Chamberland classical nodes verbatim into the GABAergic graph.
  2. Move atlas-stub nodes from Chamberland → GABAergic graph, deduping by
     cell_set_accession (most should already exist; subfamily-specific ones won't).
  3. Move the 44 edges verbatim (their lit_type / taxonomy_type stay the same).
  4. Remove all nodes + edges from the Chamberland graph; retire the file.

Cross-mapping edges between subfamilies and classical types (per #54's
"Provisional relationship" column) are CURATOR JUDGEMENT on predicate/cardinality
and are NOT added by this driver. The relocated nodes coexist in the same graph
as the classical counterparts; the curator can add `lit_to_lit` MappingEdge
entries in a follow-up.

Usage:
    python research/_drivers/merge_chamberland_graph.py --dry-run
    python research/_drivers/merge_chamberland_graph.py
"""
from __future__ import annotations
import argparse
import copy
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research' / '_drivers'))
from merge_ingest_into_mapping import yaml  # noqa: E402

SRC_GRAPH = 'kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml'
DST_GRAPH = 'kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml'

CHAMBERLAND_CLASSICALS = {
    'chrna2_olm_subfamily_chamberland',
    'ndnf_nkx2_1_olm_subfamily_chamberland',
    'sst_nos1_subfamily_chamberland',
    'sst_tac1_subfamily_chamberland',
}


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

    # ── Step 1: move classical nodes ──────────────────────────────────────
    dst_node_ids = set(n.get('id') for n in dst_nodes)
    classicals_moved = 0
    for nid in CHAMBERLAND_CLASSICALS:
        src_n = next((n for n in src_nodes if n.get('id') == nid), None)
        if not src_n:
            print(f'  classical {nid}: NOT FOUND in source; skipping')
            continue
        if nid in dst_node_ids:
            print(f'  classical {nid}: ALREADY in destination; skipping')
            continue
        dst_nodes.append(copy.deepcopy(src_n))
        dst_node_ids.add(nid)
        classicals_moved += 1
    print(f'\n=== Step 1: classical move ===')
    print(f'  moved: {classicals_moved}')

    # ── Step 2: atlas stubs ───────────────────────────────────────────────
    dst_acc = set(n.get('cell_set_accession') for n in dst_nodes if n.get('cell_set_accession'))
    moved_stubs = 0
    skipped_stubs = 0
    src_atlas_stub_ids = set()
    for n in src_nodes:
        if n.get('id') in CHAMBERLAND_CLASSICALS:
            continue
        if not n.get('cell_set_accession'):
            continue
        src_atlas_stub_ids.add(n['id'])
        if n['cell_set_accession'] in dst_acc:
            skipped_stubs += 1
        else:
            dst_nodes.append(copy.deepcopy(n))
            dst_acc.add(n['cell_set_accession'])
            moved_stubs += 1
    print(f'\n=== Step 2: atlas stub move ===')
    print(f'  moved: {moved_stubs}')
    print(f'  skipped (already in dst): {skipped_stubs}')

    # ── Step 3: edges ─────────────────────────────────────────────────────
    # Build conflict index by (lit_type, taxonomy_type)
    dst_edge_index = {(e.get('lit_type'), e.get('taxonomy_type')): e for e in dst_edges}
    moved_edges = 0
    skipped_edges = 0
    for e in src_edges:
        if e.get('lit_type') not in CHAMBERLAND_CLASSICALS:
            continue
        key = (e.get('lit_type'), e.get('taxonomy_type'))
        if key in dst_edge_index:
            skipped_edges += 1
        else:
            dst_edges.append(copy.deepcopy(e))
            dst_edge_index[key] = e
            moved_edges += 1
    print(f'\n=== Step 3: edge move ===')
    print(f'  moved: {moved_edges}')
    print(f'  skipped (already in dst): {skipped_edges}')

    # ── Step 4: scrub src ─────────────────────────────────────────────────
    src_nodes_new = [n for n in src_nodes
                     if n.get('id') not in CHAMBERLAND_CLASSICALS and n.get('id') not in src_atlas_stub_ids]
    src_edges_new = [e for e in src_edges if e.get('lit_type') not in CHAMBERLAND_CLASSICALS]
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
