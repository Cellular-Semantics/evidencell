"""
Convert Hochgerner 2023 figshare UMI count table to h5ad.

Source: https://figshare.com/articles/dataset/20412573
        Amy_FC_allcells_with_metadata_31-Jul-2022.txt (3.1 GB)

Format: tab-delimited, transposed (genes x cells)
  Row 0: header  — "cellID" + cell barcodes
  Row 1: celltype (Zeisel-style labels, e.g. GABA-8-Prkcd-Oprk1)
  Row 2: sample
  Row 3: FC time  (0 = naive, 2/8/24/28 h = fear-conditioned)
  Row 4: batch
  Row 5+: gene expression (UMI counts, integer)

Filters applied:
  - FC time == "0"  (naive only)
  - celltype not in NON_NEURONAL

Strategy: download to raw file once, then single-pass from disk.
"""
import sys, os, subprocess, time
import numpy as np
import scipy.sparse as sp
import anndata as ad
import pandas as pd

URL     = "https://ndownloader.figshare.com/files/36500010"
RAW     = "raw_matrix.txt"
OUT     = "hochgerner2023_amygdala_naive_neuronal.h5ad"

NON_NEURONAL = {
    "Astro", "Astro_SC", "Astro_agt", "COP", "EC", "Epend",
    "OL", "OPC", "OPC_cycling", "Peri", "VLMC", "VSM",
    "microglia", "pvm",
}

# ── Step 1: download raw file if not already present ────────────────────────
if os.path.exists(RAW):
    print(f"Raw file already present ({os.path.getsize(RAW)/1e9:.2f} GB), skipping download.")
else:
    print(f"Downloading to {RAW} ...")
    t0 = time.time()
    cmd = ["curl", "-L", "--progress-bar", "-o", RAW, URL]
    subprocess.run(cmd, check=True)
    elapsed = time.time() - t0
    print(f"Download complete in {elapsed/60:.1f} min ({os.path.getsize(RAW)/1e9:.2f} GB).")

# ── Step 2: single-pass — metadata first, then gene rows ────────────────────
print("Parsing metadata rows...")

CHUNK = 16 * 1024 * 1024  # 16 MB read buffer

header_cells  = None
celltype_vals = None
fc_time_vals  = None

with open(RAW, "rb") as fh:
    buf = b""
    line_idx = 0
    done_meta = False

    while not done_meta:
        chunk = fh.read(CHUNK)
        if not chunk:
            break
        buf += chunk
        while b"\n" in buf:
            nl = buf.index(b"\n")
            line = buf[:nl]
            buf  = buf[nl + 1:]
            parts = line.split(b"\t")
            label = parts[0].decode("utf-8", errors="replace")

            if line_idx == 0:
                header_cells = [p.decode("utf-8", errors="replace") for p in parts[1:]]
                print(f"  Total cells: {len(header_cells)}")
            elif label == "celltype":
                celltype_vals = [p.decode("utf-8", errors="replace") for p in parts[1:]]
            elif label == "FC time":
                fc_time_vals  = [p.decode("utf-8", errors="replace") for p in parts[1:]]

            line_idx += 1
            if line_idx == 5:      # header + 4 metadata rows read
                done_meta = True
                break

assert header_cells and celltype_vals and fc_time_vals, "Metadata parse failed"

# Build cell mask
keep_mask = np.array([
    ct not in NON_NEURONAL and fc == "0"
    for ct, fc in zip(celltype_vals, fc_time_vals)
], dtype=bool)
keep_idx  = np.where(keep_mask)[0]
n_keep    = len(keep_idx)
print(f"  Naive neuronal cells: {n_keep}")

cell_barcodes  = [header_cells[i]  for i in keep_idx]
cell_celltypes = [celltype_vals[i] for i in keep_idx]

# ── Step 3: stream gene rows from disk ──────────────────────────────────────
print("Building sparse count matrix from gene rows...")

gene_names  = []
rows_data   = []   # one array per gene, dense over kept cells (uint16)
SKIP        = 5    # header + 4 metadata rows

with open(RAW, "rb") as fh:
    buf      = b""
    line_idx = 0
    logged   = 0

    while True:
        chunk = fh.read(CHUNK)
        if not chunk and not buf:
            break
        if chunk:
            buf += chunk

        while b"\n" in buf or (not chunk and buf):
            if b"\n" in buf:
                nl   = buf.index(b"\n")
                line = buf[:nl]
                buf  = buf[nl + 1:]
            else:
                line = buf
                buf  = b""

            if line_idx < SKIP:
                line_idx += 1
                continue

            parts = line.split(b"\t")
            if len(parts) < 2:
                line_idx += 1
                continue

            gene = parts[0].decode("utf-8", errors="replace")
            raw  = parts[1:]
            vals = np.array(
                [int(raw[i]) if i < len(raw) and raw[i] else 0
                 for i in keep_idx],
                dtype=np.uint16,
            )
            gene_names.append(gene)
            rows_data.append(vals)
            line_idx += 1

            if len(gene_names) - logged >= 3000:
                logged = len(gene_names)
                print(f"  {logged} genes processed ...", flush=True)

        if not chunk:
            break

print(f"  Total genes: {len(gene_names)}")

# ── Step 4: assemble AnnData ─────────────────────────────────────────────────
print("Assembling AnnData ...")
dense = np.vstack(rows_data).T          # (n_cells, n_genes)
X     = sp.csr_matrix(dense.astype(np.float32))
del dense, rows_data
print(f"  Sparse matrix: {X.shape}, nnz={X.nnz:,}")

obs = pd.DataFrame({"celltype": cell_celltypes}, index=cell_barcodes)
obs.index.name = None
var = pd.DataFrame(index=gene_names)
var.index.name = "gene_symbols"

adata = ad.AnnData(X=X, obs=obs, var=var)
print(f"Writing {OUT} ...")
adata.write_h5ad(OUT)
print("Done.")
print(f"  Shape: {adata.shape}")
print(f"  Unique celltypes: {adata.obs['celltype'].nunique()}")
print(adata.obs["celltype"].value_counts().to_string())
