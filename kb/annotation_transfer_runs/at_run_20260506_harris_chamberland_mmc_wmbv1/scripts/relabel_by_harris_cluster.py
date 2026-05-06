"""Re-derive Chamberland subfamily labels by applying their gene-pair rules
to Harris cluster mean expression (not per-cell). Dropout-robust because
cluster means average over hundreds of cells per Harris Class.

For each Harris Class (e.g. Sst.Pnoc.Calb1.Igfbp5):
  - compute mean expression of Sst, Tac1, Ndnf, Nkx2-1, Nos1, Chrna2 over
    cells in that Class
  - apply Chamberland's rules in priority order Chrna2 > Ndnf > Sst::Nos1
    > Sst::Tac1 (each rule requires Sst expression as well, since Chamberland
    operates within the Sst-IN subclass)
  - assign the Harris Class to a Chamberland subfamily, or 'non_Sst_other'
    when the Class mean Sst is below detection or it falls into a
    non-Sst lineage (Pvalb, Vip, Cck, Calb2)
  - propagate the Class assignment back to each cell as its label

Outputs: labels_chamberland_by_class.json
         class_to_subfamily.tsv (per-Class assignment table for methods)
"""
from __future__ import annotations
import json
from pathlib import Path
import anndata as ad
import numpy as np
import pandas as pd

ROOT = Path('/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell')
HD = ROOT / 'annotation_transfer/data/harris2018'
A = ad.read_h5ad(HD/'harris_CA1_inhibitory.h5ad')
print(f'cells={A.n_obs} genes={A.n_vars}')

sym = A.var['symbol'].to_dict()
ens_to_sym = {e: s for e, s in sym.items()}
sym_to_ens = {s: e for e, s in ens_to_sym.items()}

genes = ['Sst','Tac1','Ndnf','Nkx2-1','Nos1','Chrna2','Pvalb','Vip','Cck','Calb2','Lhx6']
gene_idx = {g: A.var_names.get_loc(sym_to_ens[g]) for g in genes if g in sym_to_ens}
print('found gene cols:', list(gene_idx.keys()))

# Per-Class cluster means
classes = A.obs['Class'].astype(str).values
unique_classes = sorted(set(classes) - {'nan',''})
rows = []
for c in unique_classes:
    mask = classes == c
    if mask.sum() < 5: continue
    sub_X = A.X[mask, :].toarray() if hasattr(A.X[mask, :], 'toarray') else np.asarray(A.X[mask, :])
    means = {g: float(sub_X[:, gene_idx[g]].mean()) for g in gene_idx}
    means['_class'] = c
    means['_n'] = int(mask.sum())
    rows.append(means)
df = pd.DataFrame(rows).set_index('_class')
df = df.sort_values('_n', ascending=False)

# Apply Chamberland rules at cluster-mean level. Priority: Chrna2 > Ndnf > Nos1 > Tac1.
# All require Sst > threshold (we use 1.0 — at cluster-mean level this is conservative;
# Sst-IN clusters typically have Sst mean > 5).
def assign_subfamily(r):
    sst = r.get('Sst', 0)
    if sst < 1.0:
        # not Sst-positive at cluster level — Pvalb/Vip/Cck/Calb2 etc.
        return 'non_Sst'
    chrna2 = r.get('Chrna2', 0)
    ndnf = r.get('Ndnf', 0)
    nos1 = r.get('Nos1', 0)
    tac1 = r.get('Tac1', 0)
    # Cluster-mean thresholds: scaled up from per-cell thresholds since cluster means smooth dropout
    if chrna2 > 0.3:
        return 'Chrna2'
    if ndnf > 1.0:
        return 'Ndnf'
    if nos1 > 1.5:
        return 'Sst_Nos1'
    if tac1 > 0.5:
        return 'Sst_Tac1'
    return 'Sst_other'  # Sst+ but not matching any subfamily rule

df['subfamily'] = df.apply(assign_subfamily, axis=1)
df_sf = df[['_n','Sst','Chrna2','Ndnf','Nkx2-1','Nos1','Tac1','Pvalb','subfamily']]
df_sf = df_sf.rename(columns={'_n':'n_cells'})
print('\n--- Per-Class Chamberland subfamily assignment ---')
print(df_sf.to_string(float_format=lambda x: f'{x:.2f}'))

# Save TSV
out_tsv = HD / 'class_to_subfamily.tsv'
df_sf.to_csv(out_tsv, sep='\t', float_format='%.3f')
print(f'\nWrote {out_tsv}')

# Propagate Class -> subfamily to per-cell labels
class_to_sf = df_sf['subfamily'].to_dict()
cell_to_sf = {cell: class_to_sf.get(str(cls), 'unassigned')
              for cell, cls in zip(A.obs_names, classes)}
out_json = HD / 'labels_chamberland_by_class.json'
out_json.write_text(json.dumps(cell_to_sf, indent=1))
print(f'Wrote {out_json}')

# Summary
counts = pd.Series(list(cell_to_sf.values())).value_counts()
print('\nCell counts per derived subfamily:')
print(counts)
