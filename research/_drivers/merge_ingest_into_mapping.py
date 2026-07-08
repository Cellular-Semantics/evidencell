#!/usr/bin/env python3
"""Merge an asta-ingest classical stub node into its mapping-graph counterpart.

For each (ingest_graph, ingest_node_id, mapping_graph, mapping_node_id) pair:
  - Additive merge: every property block on the ingest stub is unioned into the
    mapping node. Properties present on the ingest stub but absent on the
    mapping node are copied wholesale.
  - Sources on shared property entries are unioned by (ref, quote_key) identity.
  - notes: concatenated with a separator (curator can clean up later).
  - definition_references: union of flat string list.
  - Adds the ingest-stub id as a synonym (TypeSynonym, synonym_type: HISTORICAL).
  - Removes the ingest classical node from the ingest graph.

Usage:
    python research/_drivers/merge_ingest_into_mapping.py --dry-run
    python research/_drivers/merge_ingest_into_mapping.py            # writes
"""
from __future__ import annotations
import argparse
import copy
import sys
import pathlib
from ruamel.yaml import YAML

ROOT = pathlib.Path(__file__).resolve().parents[2]
yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096
yaml.indent(mapping=2, sequence=4, offset=2)


# (ingest_graph, ingest_node_id, mapping_graph, mapping_node_id)
PAIRS = [
    ('kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml', 'ca1_pyramidal_cell',
     'kb/graphs/hippocampus/hippocampus_glutamatergic.yaml', 'ca1_pc_hippocampus'),
    ('kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml', 'ca3_pyramidal_cell',
     'kb/graphs/hippocampus/hippocampus_glutamatergic.yaml', 'ca3_pc_hippocampus'),
    ('kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml', 'dg_granule_cell',
     'kb/graphs/hippocampus/hippocampus_glutamatergic.yaml', 'dg_granule_cell_hippocampus'),
    ('kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml', 'dg_mossy_cell',
     'kb/graphs/hippocampus/hippocampus_glutamatergic.yaml', 'hilar_mossy_cell_hippocampus'),
]


def source_key(s: dict) -> tuple:
    """De-dup identity for a PropertySource: ref + quote_key (if present)."""
    return (s.get('ref'), s.get('quote_key'))


def union_sources(existing: list, incoming: list) -> tuple[list, int]:
    """Append incoming PropertySources to existing list, skipping duplicates by source_key. Returns (new_list, n_added)."""
    if existing is None:
        existing = []
    existing_keys = set(source_key(s) for s in existing)
    added = 0
    for s in incoming or []:
        if source_key(s) not in existing_keys:
            existing.append(copy.deepcopy(s))
            existing_keys.add(source_key(s))
            added += 1
    return existing, added


def merge_list_entries(target_list: list | None, source_list: list | None, key_fn) -> tuple[list, dict]:
    """Merge two lists of property entries (anat, markers, etc.).

    - For each entry in source_list, find matching entry in target_list by key_fn.
    - If found: union the `sources` sub-list.
    - If not found: append the entry verbatim.
    Returns (merged_list, stats).
    """
    stats = {'entries_appended': 0, 'sources_added': 0, 'entries_merged_sources': 0}
    if target_list is None:
        target_list = []
    if source_list is None:
        return target_list, stats
    target_idx = {key_fn(e): i for i, e in enumerate(target_list)}
    for src_entry in source_list:
        k = key_fn(src_entry)
        if k in target_idx:
            tgt_entry = target_list[target_idx[k]]
            tgt_sources = tgt_entry.get('sources') or []
            new_sources, n_added = union_sources(tgt_sources, src_entry.get('sources'))
            tgt_entry['sources'] = new_sources
            if n_added > 0:
                stats['sources_added'] += n_added
                stats['entries_merged_sources'] += 1
        else:
            target_list.append(copy.deepcopy(src_entry))
            stats['entries_appended'] += 1
    return target_list, stats


def merge_node(target: dict, source: dict, source_id: str) -> dict:
    """Mutate target in place by merging source into it. Return stats dict."""
    stats = {}

    # 1. Property-list fields keyed by 'id' or 'symbol'
    for field, key_field in [
        ('anatomical_location', 'id'),
        ('defining_markers', 'symbol'),
        ('neuropeptides', 'symbol'),
        ('negative_markers', 'symbol'),
    ]:
        src_val = source.get(field)
        if not src_val:
            continue
        merged, s = merge_list_entries(target.get(field), src_val, lambda e, k=key_field: e.get(k) or e.get('label'))
        target[field] = merged
        stats[field] = s

    # 2. Dict fields with .sources sub-list
    for field in ['nt_type', 'electrophysiology', 'morphology']:
        src_val = source.get(field)
        if not src_val:
            continue
        if not target.get(field):
            target[field] = copy.deepcopy(src_val)
            stats[field] = {'whole_block_copied': True, 'n_sources': len(src_val.get('sources') or [])}
        else:
            tgt_sources = target[field].get('sources') or []
            new_sources, n_added = union_sources(tgt_sources, src_val.get('sources'))
            target[field]['sources'] = new_sources
            stats[field] = {'sources_added': n_added}

    # 3. node-level evidence list (LITERATURE evidence_items + their sources)
    if source.get('evidence'):
        target.setdefault('evidence', [])
        existing_evidence_keys = set()
        for e in target['evidence']:
            # Identity: evidence_type + first ref + first quote_key
            srcs = e.get('sources') or []
            first_ref = srcs[0].get('ref') if srcs else None
            first_qk = srcs[0].get('quote_key') if srcs else None
            existing_evidence_keys.add((e.get('evidence_type'), first_ref, first_qk))
        ev_appended = 0
        for src_ev in source['evidence']:
            srcs = src_ev.get('sources') or []
            first_ref = srcs[0].get('ref') if srcs else None
            first_qk = srcs[0].get('quote_key') if srcs else None
            k = (src_ev.get('evidence_type'), first_ref, first_qk)
            if k not in existing_evidence_keys:
                target['evidence'].append(copy.deepcopy(src_ev))
                existing_evidence_keys.add(k)
                ev_appended += 1
        if ev_appended > 0:
            stats['evidence'] = {'items_appended': ev_appended}

    # 4. definition_references — flat string list
    src_refs = source.get('definition_references') or []
    if src_refs:
        tgt_refs = list(target.get('definition_references') or [])
        existing = set(tgt_refs)
        added = []
        for r in src_refs:
            if r not in existing:
                tgt_refs.append(r)
                existing.add(r)
                added.append(r)
        target['definition_references'] = tgt_refs
        if added:
            stats['definition_references'] = {'added': added}

    # 5. notes — concatenate with separator if both present
    src_notes = source.get('notes')
    if src_notes:
        tgt_notes = target.get('notes')
        if tgt_notes:
            sep = f"\n\n---\n[Migrated from asta-ingest stub `{source_id}` on 2026-06-10]\n\n"
            target['notes'] = tgt_notes.rstrip() + sep + src_notes.lstrip()
        else:
            target['notes'] = f"[Migrated from asta-ingest stub `{source_id}` on 2026-06-10]\n\n" + src_notes
        stats['notes'] = {'merged': True}

    # 6. species — copy if mapping node lacks it
    if source.get('species') and not target.get('species'):
        target['species'] = copy.deepcopy(source['species'])
        stats['species'] = {'whole_block_copied': True}

    # 7. Add ingest-stub id as synonym (HISTORICAL)
    target.setdefault('synonyms', [])
    if not any((s.get('term') == source_id) for s in target['synonyms']):
        target['synonyms'].append({
            'term': source_id,
            'synonym_type': 'HISTORICAL',
        })
        stats['synonyms'] = {'added_term': source_id}

    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    ingest_files_to_save = {}
    mapping_files_to_save = {}

    for ing_path, ing_id, mp_path, mp_id in PAIRS:
        ing_path_full = ROOT / ing_path
        mp_path_full = ROOT / mp_path

        if ing_path not in ingest_files_to_save:
            ingest_files_to_save[ing_path] = yaml.load(ing_path_full.read_text())
        if mp_path not in mapping_files_to_save:
            mapping_files_to_save[mp_path] = yaml.load(mp_path_full.read_text())

        ing_doc = ingest_files_to_save[ing_path]
        mp_doc = mapping_files_to_save[mp_path]

        ing_nodes = ing_doc.get('nodes', [])
        mp_nodes = mp_doc.get('nodes', [])
        ing_idx = next((i for i, n in enumerate(ing_nodes) if n.get('id') == ing_id), None)
        mp_idx = next((i for i, n in enumerate(mp_nodes) if n.get('id') == mp_id), None)
        if ing_idx is None or mp_idx is None:
            print(f'  ! could not locate ingest={ing_id} or mapping={mp_id}; skipping')
            continue

        ing_node = ing_nodes[ing_idx]
        mp_node = mp_nodes[mp_idx]

        print(f'\n=== {ing_id} → {mp_id} ===')
        stats = merge_node(mp_node, ing_node, ing_id)
        for k, v in stats.items():
            print(f'  {k}: {v}')

        # Remove the ingest node
        del ing_nodes[ing_idx]
        print(f'  removed ingest stub from {ing_path}')

    if args.dry_run:
        print('\n--dry-run: no files written')
        return 0

    for path, doc in mapping_files_to_save.items():
        with (ROOT / path).open('w') as f:
            yaml.dump(doc, f)
        print(f'wrote {path}')
    for path, doc in ingest_files_to_save.items():
        with (ROOT / path).open('w') as f:
            yaml.dump(doc, f)
        print(f'wrote {path}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
