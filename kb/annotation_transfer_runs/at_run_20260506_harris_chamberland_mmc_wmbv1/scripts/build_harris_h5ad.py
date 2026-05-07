"""Build a MapMyCells-ready h5ad from Harris 2018 TSVs.

Inputs:
  annotation_transfer/data/harris2018/expression.tsv     (genes x cells, gene symbols, UMI counts)
  annotation_transfer/data/harris2018/cell_metadata.tsv  (metadata rows x cells)
  annotation_transfer/data/harris2018/analysis_results.tsv (Class, nbtSNE_x, nbtSNE_y, Latent_factor x cells)
  conf/gene_mapping_CCN20230722.tsv                      (ensembl_id -> symbol)

Output:
  annotation_transfer/data/harris2018/harris_CA1_inhibitory.h5ad

  Layout: cells x genes; .X = raw integer counts (CSR sparse); var indexed by Ensembl ID;
          obs has Class, Label (Harris's published labels) plus chamberland_subfamily column
          derived from the Sst+Tac1 / Sst+Nos1 / Ndnf+Nkx2-1 / Chrna2 expression-product rules.
"""
from __future__ import annotations
import csv, json, sys
from pathlib import Path
import numpy as np
import scipy.sparse as sp
import pandas as pd
import anndata as ad

ROOT = Path('/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell')
HD = ROOT / 'annotation_transfer/data/harris2018'
OUT = HD / 'harris_CA1_inhibitory.h5ad'

print('Reading expression.tsv (this will take a moment)...', flush=True)
# expression.tsv: first row = cell names, first column = gene symbols, rest = ints
import io
with open(HD/'expression.tsv') as f:
    header = f.readline().rstrip('\n').split('\t')
    cell_names = [c for c in header[1:] if c]  # strip trailing empty
print(f'  cells: {len(cell_names)}')

# Stream rows: gene_symbol, then n_cells ints
gene_symbols = []
data_rows = []
indptr = [0]
indices = []
data = []
with open(HD/'expression.tsv') as f:
    next(f)  # skip header
    for line_num, line in enumerate(f, 1):
        parts = line.rstrip('\n').split('\t')
        gene_symbols.append(parts[0])
        # parts[1:] may have trailing empty from trailing tab; clip to len(cell_names)
        vals = parts[1:1+len(cell_names)]
        for j, v in enumerate(vals):
            if not v: continue
            iv = int(v)
            if iv != 0:
                indices.append(j)
                data.append(iv)
        indptr.append(len(data))
        if line_num % 5000 == 0:
            print(f'  rows: {line_num}', flush=True)
print(f'  genes: {len(gene_symbols)}, nnz: {len(data)}')

# CSR: shape (n_genes, n_cells); transpose to (n_cells, n_genes)
X_genes_x_cells = sp.csr_matrix((data, indices, indptr),
                                shape=(len(gene_symbols), len(cell_names)),
                                dtype=np.int32)
X = X_genes_x_cells.T.tocsr()
print(f'  X: {X.shape} nnz={X.nnz}')

# Read metadata + analysis_results
def read_tsv_rows(path):
    with open(path) as f:
        header = f.readline().rstrip('\n').split('\t')
        cells = [c for c in header[1:] if c]
        rows = {}
        for line in f:
            parts = line.rstrip('\n').split('\t')
            rows[parts[0]] = parts[1:1+len(cells)]
    return cells, rows

cell_names_md, meta = read_tsv_rows(HD/'cell_metadata.tsv')
cell_names_ar, ana = read_tsv_rows(HD/'analysis_results.tsv')
assert cell_names_md == cell_names, f'metadata cell order mismatch'
assert cell_names_ar == cell_names, f'analysis_results cell order mismatch'

obs = pd.DataFrame(index=cell_names)
def clean(vals):
    return [str(v).replace('\x00','').strip() for v in vals]
for key in ('Class', 'Label'):
    if key in ana: obs[key] = clean(ana[key])
    elif key in meta: obs[key] = clean(meta[key])
if 'Class' not in obs.columns and 'Label' in obs.columns:
    obs['Class'] = obs['Label']
print('  Class label coverage:', obs['Class'].value_counts().head(3).to_dict())

# var: gene symbols + ensembl ids via mapping
gm = pd.read_csv(ROOT/'conf/gene_mapping_CCN20230722.tsv', sep='\t')
sym2ens = dict(zip(gm['symbol'], gm['ensembl_id']))
ens_ids = [sym2ens.get(s, '') for s in gene_symbols]
n_unmapped = sum(1 for e in ens_ids if not e)
print(f'  genes unmapped to Ensembl: {n_unmapped}/{len(gene_symbols)}')
# Drop unmapped genes
keep = [i for i, e in enumerate(ens_ids) if e]
X = X[:, keep]
gene_symbols = [gene_symbols[i] for i in keep]
ens_ids = [ens_ids[i] for i in keep]
# Deduplicate: if two symbols map to same ensembl, keep first
seen = set(); keep2 = []
for i, e in enumerate(ens_ids):
    if e not in seen:
        seen.add(e); keep2.append(i)
X = X[:, keep2]
gene_symbols = [gene_symbols[i] for i in keep2]
ens_ids = [ens_ids[i] for i in keep2]
print(f'  after Ensembl dedup: {X.shape}')
var = pd.DataFrame({'symbol': gene_symbols}, index=ens_ids)
var.index.name = 'ensembl_id'

# Chamberland-derived subfamily labels
sym_to_col = {s: i for i, s in enumerate(gene_symbols)}
def col(s):
    j = sym_to_col.get(s)
    return np.asarray(X[:, j].todense()).ravel() if j is not None else np.zeros(X.shape[0])
sst = col('Sst'); tac1 = col('Tac1'); ndnf = col('Ndnf'); nkx21 = col('Nkx2-1')
nos1 = col('Nos1'); chrna2 = col('Chrna2')
# Chamberland's rule: expression product > 1 (raw counts, very lenient threshold)
sst_pos = sst > 0
# Chamberland's intersectional Cre/Flp lines target lineage-defined populations; in adult
# expression Nkx2-1 is largely silent (developmental MGE TF), so the operational adult
# transcriptomic equivalent of Ndnf::Nkx2-1 is Sst+/Ndnf+. Tac1 / Nos1 / Chrna2 are
# adult-expressed; their gene-product rules are applied as Chamberland describes.
sst_tac1 = (sst * tac1) > 1
sst_nos1 = (sst * nos1) > 1
ndnf_high = (ndnf > 1) & sst_pos
chrna2_pos = (chrna2 > 0) & sst_pos

subfam = np.full(X.shape[0], 'unassigned', dtype=object)
# Apply low->high priority so higher-priority (more specific) labels overwrite
subfam[sst_tac1 & sst_pos] = 'Sst_Tac1'
subfam[sst_nos1 & sst_pos] = 'Sst_Nos1'
subfam[ndnf_high] = 'Ndnf'           # Sst+/Ndnf+ (operational Ndnf::Nkx2-1)
subfam[chrna2_pos] = 'Chrna2'         # Sst+/Chrna2+ (highest specificity for OLM-Chrna2)
obs['chamberland_subfamily'] = subfam
print('  chamberland_subfamily counts:', dict(pd.Series(subfam).value_counts()))

A = ad.AnnData(X=X, obs=obs, var=var)
A.write_h5ad(OUT)
print(f'WROTE {OUT}  shape={A.shape}')

# Source label JSONs (cell_id -> label)
labels_class = {cell_id: str(c) for cell_id, c in zip(A.obs_names, A.obs['Class'])}
labels_subfam = {cell_id: str(c) for cell_id, c in zip(A.obs_names, A.obs['chamberland_subfamily'])}
(HD/'labels_harris_class.json').write_text(json.dumps(labels_class, indent=1))
(HD/'labels_chamberland_subfamily.json').write_text(json.dumps(labels_subfam, indent=1))
print('Wrote labels_harris_class.json, labels_chamberland_subfamily.json')
