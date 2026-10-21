#!/usr/bin/env python3
"""Per-region refresh driver: Stage A/B + refresh at ranks 0 and 1 + stale audit.

For every curated classical node in a region's KB graphs:
  - Stage A find-candidates at rank 0 and rank 1 (top-50)
  - Stage B emit-stage-b at rank 0 and rank 1 (top-5) — idempotent on existing edges
  - Stage B refresh-property-comparisons at rank 0 and rank 1 (top-K 50)
  - Aggregates a per-region stale-audit markdown listing edges where the existing
    taxonomy_type is no longer in current Stage A top-50.

Usage:
    python research/_drivers/refresh_region.py <region> [--date YYYYMMDD] [--dry-run]
"""
from __future__ import annotations
import argparse
import json
import pathlib
import subprocess
import sys
import yaml
from datetime import date

REPO = pathlib.Path(__file__).resolve().parents[2]


def run(cmd: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def parse_json_from_stdout(stdout: str) -> dict | None:
    idx = stdout.find('{')
    if idx < 0:
        return None
    try:
        return json.loads(stdout[idx:])
    except json.JSONDecodeError:
        return None


def collect_classical_nodes(region: str) -> list[tuple[pathlib.Path, str, str | None]]:
    """Return [(graph_path, node_id, taxonomy_id)] for every curated classical node."""
    out = []
    for graph_path in sorted((REPO / 'kb' / 'graphs' / region).glob('*.yaml')):
        try:
            d = yaml.safe_load(graph_path.read_text())
        except Exception as e:
            print(f'  ERR parse {graph_path}: {e}', file=sys.stderr)
            continue
        if not isinstance(d, dict):
            continue
        # determine taxonomy_id from any atlas node
        tax_id = None
        for n in d.get('nodes', []) or []:
            if isinstance(n, dict) and n.get('taxonomy_id'):
                tax_id = n['taxonomy_id']
                break
        for n in d.get('nodes', []) or []:
            if not isinstance(n, dict):
                continue
            db = n.get('definition_basis') or ''
            if isinstance(db, str) and db.startswith('CLASSICAL'):
                out.append((graph_path, n['id'], tax_id))
    return out


def per_node_refresh(graph_path: pathlib.Path, node_id: str, taxonomy_id: str, region: str, date_str: str):
    base = REPO / 'research' / region / f'refresh_{date_str}_{node_id}'
    base.mkdir(parents=True, exist_ok=True)
    summary = {
        'graph': str(graph_path.relative_to(REPO)),
        'node_id': node_id,
        'taxonomy_id': taxonomy_id,
        'ranks': {},
    }
    for rank in (0, 1):
        rk = {'stage_a': None, 'emit_b': None, 'refresh_pc': None}
        # Stage A
        disc_path = base / f'discovery_candidates_rank{rank}.json'
        rc, out, err = run(['just', 'find-candidates', str(graph_path), node_id, taxonomy_id, str(rank), '50'])
        if rc != 0:
            rk['stage_a'] = {'error': err.strip()[:500] or out.strip()[:500]}
        else:
            # find-candidates prints info to stderr-ish then JSON to stdout; capture JSON portion
            idx = out.find('{')
            if idx < 0:
                rk['stage_a'] = {'error': 'no JSON in stdout'}
            else:
                try:
                    j = json.loads(out[idx:])
                    disc_path.write_text(out[idx:])
                    rk['stage_a'] = {'n_candidates': j.get('n_candidates'),
                                     'top5': [c['node_id'] for c in j['candidates'][:5]]}
                except Exception as e:
                    rk['stage_a'] = {'error': f'json parse: {e}'}
        # Stage B emit (only if Stage A succeeded)
        if rk['stage_a'] and 'error' not in rk['stage_a']:
            rc, out, err = run(['just', 'emit-stage-b', str(graph_path), node_id, taxonomy_id, str(rank), '5',
                                '--discovery-json', str(disc_path)])
            if rc != 0:
                rk['emit_b'] = {'error': err.strip()[:500] or out.strip()[:500]}
            else:
                # parse human-readable summary
                lines = (out + err).strip().splitlines()
                rk['emit_b'] = {'last_lines': lines[-5:]}
            # Refresh PC
            rc, out, err = run(['just', 'refresh-property-comparisons', str(graph_path), node_id, taxonomy_id, str(rank), '--top-k', '50'])
            if rc != 0:
                rk['refresh_pc'] = {'error': err.strip()[:500] or out.strip()[:500]}
            else:
                j = parse_json_from_stdout(out)
                if j is None:
                    rk['refresh_pc'] = {'error': 'no JSON', 'tail': out[-200:]}
                else:
                    rk['refresh_pc'] = {
                        'edges_refreshed': j.get('edges_refreshed'),
                        'edges_skipped_taxtype_not_in_topk': j.get('edges_skipped_taxtype_not_in_topk'),
                        'skipped_details': j.get('skipped_details', []),
                        'refreshed_details': [
                            {'edge_id': r.get('edge_id'), 'taxonomy_type': r.get('taxonomy_type')}
                            for r in j.get('refreshed_details', [])
                        ],
                    }
        summary['ranks'][f'rank{rank}'] = rk
    (base / 'refresh_summary.json').write_text(json.dumps(summary, indent=2))
    return summary


def _rank_of_taxtype(tt: str) -> int | None:
    """Map a taxonomy_type accession to its rank: CLUS_*→0, SUPT_*→1, SUBC_*→2, CLAS_*→3."""
    if not isinstance(tt, str):
        return None
    u = tt.upper()
    if '_CLUS_' in u: return 0
    if '_SUPT_' in u: return 1
    if '_SUBC_' in u: return 2
    if '_CLAS_' in u: return 3
    return None


def stale_audit_md(region: str, date_str: str, all_summaries: list[dict]) -> str:
    lines = [f'# Stale-location audit — {region} — {date_str}', '',
             'Edges whose `taxonomy_type` is NOT in current Stage A top-50 at the rank that matches the edge target\'s level.',
             '(Rank-mismatch skips — e.g. supertype edge skipped at rank-0 cluster refresh — are filtered out; those are not stale.)',
             'These need curator review — current proximity-aware scoring placed the cluster/supertype outside the candidate pool.',
             '', '## Stale edges', '']
    any_stale = False
    for s in all_summaries:
        node = s['node_id']
        graph = s['graph']
        for rank_key, rk in (s.get('ranks') or {}).items():
            target_rank = int(rank_key.replace('rank', ''))
            rpc = (rk or {}).get('refresh_pc') or {}
            for d in rpc.get('skipped_details', []) or []:
                tt = d.get('taxonomy_type', '')
                tt_rank = _rank_of_taxtype(tt)
                if tt_rank is None or tt_rank != target_rank:
                    continue  # rank-mismatch — not a stale signal
                any_stale = True
                lines.append(f'### {node} (rank{target_rank}) — `{d.get("edge_id")}`')
                lines.append('')
                lines.append(f'- **Graph**: `{graph}`')
                lines.append(f'- **taxonomy_type**: `{tt}`')
                reason = d.get('skip_reason') or 'taxonomy_type not in current Stage A top-50 at matching rank'
                lines.append(f'- **Skip reason**: {reason}')
                extras = {k: v for k, v in d.items() if k not in ('edge_id', 'taxonomy_type', 'skip_reason')}
                if extras:
                    lines.append(f'- **Extras**: `{json.dumps(extras)[:300]}`')
                lines.append('')
    if not any_stale:
        lines.append('_None — all existing edges land within current top-50 at their respective ranks._')
    lines.append('')
    lines.append('## Refresh summary')
    lines.append('')
    lines.append('| Node | Rank0 refreshed / skipped | Rank1 refreshed / skipped |')
    lines.append('|---|---|---|')
    for s in all_summaries:
        node = s['node_id']
        cells = []
        for rk_key in ('rank0', 'rank1'):
            rk = (s.get('ranks') or {}).get(rk_key) or {}
            rpc = rk.get('refresh_pc') or {}
            r = rpc.get('edges_refreshed')
            k = rpc.get('edges_skipped_taxtype_not_in_topk')
            err = rpc.get('error')
            if err:
                cells.append(f'ERR: {err[:80]}')
            else:
                cells.append(f'{r} / {k}')
        lines.append(f'| `{node}` | {cells[0]} | {cells[1]} |')
    lines.append('')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('region')
    ap.add_argument('--date', default=date.today().strftime('%Y%m%d'))
    args = ap.parse_args()

    region = args.region
    nodes = collect_classical_nodes(region)
    if not nodes:
        print(f'No curated classical nodes for region {region}')
        return 1
    print(f'Region {region}: {len(nodes)} (graph, node) pairs')
    all_summaries = []
    for i, (gp, nid, tax) in enumerate(nodes, 1):
        if not tax:
            print(f'  [{i}/{len(nodes)}] {nid} in {gp.name}: SKIP no taxonomy_id')
            all_summaries.append({'graph': str(gp.relative_to(REPO)), 'node_id': nid,
                                  'taxonomy_id': None, 'ranks': {},
                                  'skipped_reason': 'no taxonomy_id discoverable'})
            continue
        print(f'  [{i}/{len(nodes)}] {nid} in {gp.name} ({tax})', flush=True)
        s = per_node_refresh(gp, nid, tax, region, args.date)
        all_summaries.append(s)
        # print 1-line summary
        rank0 = (s['ranks'].get('rank0') or {}).get('refresh_pc') or {}
        rank1 = (s['ranks'].get('rank1') or {}).get('refresh_pc') or {}
        print(f'    rank0 refreshed={rank0.get("edges_refreshed")}/skipped={rank0.get("edges_skipped_taxtype_not_in_topk")}; '
              f'rank1 refreshed={rank1.get("edges_refreshed")}/skipped={rank1.get("edges_skipped_taxtype_not_in_topk")}')
    out_dir = REPO / 'research' / region
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f'refresh_{args.date}_stale_audit.md').write_text(stale_audit_md(region, args.date, all_summaries))
    (out_dir / f'refresh_{args.date}_summary.json').write_text(json.dumps(all_summaries, indent=2))
    print(f'\nWrote: research/{region}/refresh_{args.date}_stale_audit.md')
    return 0


if __name__ == '__main__':
    sys.exit(main())
