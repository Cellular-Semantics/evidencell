# Skill: Retrieve and Convert Dataset for MapMyCells

## When to use

Use this skill when you need to take a single-cell transcriptomic dataset (given as a file path, URL, or accession) and prepare it for MapMyCells annotation transfer.

## Input

The user provides one of:
- A local file path (h5ad, RDS, loom, mtx directory, CSV)
- A URL to download from
- A dataset accession (GEO:GSExxxxx, SCP:SCPxxx, CellxGene URL)

The user may also specify:
- Which cluster/annotation column to use as source labels
- Which subset of cells to extract

## Steps

### Step 1: Preflight — estimate resources

Run the preflight check before loading:

```bash
cd annotation_transfer
uv run annotation-transfer preflight <FILE_OR_DIR>
```

If the report says WARNING (dataset may exceed available RAM):
- **STOP and report to the user** with the numbers (est. memory vs available)
- Ask whether to proceed, subsample, or abort
- Do NOT attempt to load without user confirmation

### Step 2: Determine format and load

Inspect the file to determine its format:

**h5ad files** (`.h5ad`):
```python
import anndata as ad
adata = ad.read_h5ad(path)
```

**Seurat RDS files** (`.rds`, `.RDS`):
Requires R with Seurat and SeuratDisk installed. Run via Rscript:
```r
library(Seurat)
library(SeuratDisk)

obj <- readRDS("input.rds")

# Upgrade if old Seurat version
if (!inherits(obj, "Seurat")) {
  obj <- UpdateSeuratObject(obj)
}

DefaultAssay(obj) <- "RNA"

# Convert factors to strings
obj@meta.data[] <- lapply(obj@meta.data, function(x) if (is.factor(x)) as.character(x) else x)

# Keep counts only, no scaled data
obj <- DietSeurat(obj, assays="RNA", layers=c("counts", "data"),
                  dimreducs=c("umap","pca"), graphs=FALSE)

SaveH5Seurat(obj, filename="output.h5seurat", overwrite=TRUE)
Convert("output.h5seurat", dest="h5ad", overwrite=TRUE)
```
Then load the resulting h5ad with anndata.

**10x mtx bundles** (directory with `matrix.mtx.gz`, `barcodes.tsv.gz`, `features.tsv.gz`):
```python
import scanpy as sc
adata = sc.read_10x_mtx(path, var_names="gene_symbols")
```

**Loom files** (`.loom`):
```python
import scanpy as sc
adata = sc.read_loom(path)
```

**CSV/TSV expression matrices**:
Inspect the file to determine layout (genes as rows vs columns, metadata mixed in). Load with pandas, construct AnnData manually.

### Step 3: Inspect annotations — agentic loop

After loading into AnnData, inspect the available annotations:

```python
print(f"Shape: {adata.shape}")
print(f"\nobs columns: {list(adata.obs.columns)}")
for col in adata.obs.columns:
    if adata.obs[col].dtype == object or adata.obs[col].nunique() < 100:
        print(f"\n{col} ({adata.obs[col].nunique()} unique values):")
        print(adata.obs[col].value_counts().head(10))
```

Based on the output:
1. **Propose** which column to use as the source cluster label for F1 computation
2. **Present the proposal to the user** with the value counts
3. If the user wants a different column or granularity, iterate
4. If the dataset needs to be sliced (e.g., only GABAergic cells), propose the filter

Common column names to look for:
- Cluster: `cluster`, `seurat_clusters`, `clusters`, `louvain`, `leiden`
- Cell type: `cell_type`, `celltype`, `subclass`, `annotation`, `celltype_level_1`
- Subcluster: `subcluster`, `subclass`, `celltype_level_2`

### Step 4: Check data quality

Verify the data is suitable for MapMyCells:

```python
import scipy.sparse as sp
import numpy as np

# Check if X has integer counts
if sp.issparse(adata.X):
    sample = adata.X[:100, :].toarray()
else:
    sample = adata.X[:100, :]

is_integer = np.allclose(sample, np.round(sample))
is_nonneg = sample.min() >= 0
print(f"Integer counts in X: {is_integer}")
print(f"Non-negative X: {is_nonneg}")

# Check raw
if adata.raw is not None:
    raw_sample = adata.raw.X[:100, :].toarray() if sp.issparse(adata.raw.X) else adata.raw.X[:100, :]
    print(f"Integer counts in raw.X: {np.allclose(raw_sample, np.round(raw_sample))}")
    print(f"raw.X will be used for counts")

# Check gene symbols
print(f"\nFirst 10 var_names: {list(adata.var_names[:10])}")
print(f"var columns: {list(adata.var.columns)}")
```

If X is normalised/scaled but raw.X has counts, `convert.py` handles this automatically.
If neither X nor raw has integer counts, report to the user — the dataset may need special handling.

### Step 5: Convert

Run the conversion using the annotation_transfer CLI or Python API:

```bash
uv run annotation-transfer convert input.h5ad output_mmc.h5ad \
  --cluster-col <CHOSEN_COL> \
  --cluster-value <OPTIONAL_FILTER> \
  --label-col <LABEL_COL> \
  -y
```

Or in Python:
```python
from annotation_transfer.convert import prepare_for_mapmycells, save_source_labels

labels = prepare_for_mapmycells(
    adata, output_path,
    cluster_col="cluster",
    cluster_value="GABAergic",  # optional filter
    label_col="subtype",
)
save_source_labels(labels, output_path.with_suffix(".labels.json"))
```

### Step 6: Verify output

```python
import anndata as ad
result = ad.read_h5ad(output_path)
print(f"Output shape: {result.shape}")
print(f"obs columns: {list(result.obs.columns)}")
print(f"var columns: {list(result.var.columns)}")
print(f"Sparse: {sp.issparse(result.X)}, CSR: {sp.isspmatrix_csr(result.X)}")
```

## Output

Two files:
1. `<name>_mmc.h5ad` — MapMyCells-ready h5ad
2. `<name>_mmc.labels.json` — cell_id → source cluster label mapping (for F1 scoring)

## Important notes

- **Never skip the preflight check** for files > 100MB
- **Always present annotation column choices to the user** — don't guess silently
- Gene symbols must match the target taxonomy (mouse: `Sst`, human: `SST`)
- The conversion strips all metadata except cell_id and gene_id — this is intentional
- If an RDS file fails to convert, check the Seurat version and try updating
