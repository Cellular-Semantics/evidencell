#!/usr/bin/env bash
# Fetch Li et al. 2020 TRN inputs: GEO:GSE145273 TPM tables + SCP344 "Type" annotation.
# Run from the repo root. GEO files are gitignored-by-convention under
# annotation_transfer/inputs/datasets/ (do not commit them).
set -euo pipefail
GEO_DIR=annotation_transfer/inputs/datasets/li2020_trn
OUT_DIR=research/thalamus/annotation_transfer/li2020_trn
mkdir -p "$GEO_DIR" "$OUT_DIR"

for f in GSE145273_TPM.TRN.tsv.gz GSE145273_TPM.nonTRN.tsv.gz GSE145273_TPM.patch.tsv.gz; do
  [ -s "$GEO_DIR/$f" ] || curl -sSfL -o "$GEO_DIR/$f" \
    "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE145nnn/GSE145273/suppl/$f"
done

# SCP344 downloads need a login, but the public explore API returns the
# biSNE cluster with its per-cell "Type" annotation.
curl -sSf "https://singlecell.broadinstitute.org/single_cell/api/v1/studies/SCP344/clusters/biSNE?annotation_name=Type&annotation_type=group&annotation_scope=study&fields=coordinates,cells,annotation&subsample=all" \
  | python3 -I -c '
import json, sys
d = json.load(sys.stdin)["data"]
print("NAME\tType\tbiSNE_x\tbiSNE_y")
for c, t, x, y in zip(d["cells"], d["annotations"], d["x"], d["y"]):
    print(f"{c}\t{t}\t{x}\t{y}")
' > "$OUT_DIR/scp344_type.tsv"
wc -l "$OUT_DIR/scp344_type.tsv"
