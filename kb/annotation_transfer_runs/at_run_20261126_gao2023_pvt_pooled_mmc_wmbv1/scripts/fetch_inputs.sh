#!/usr/bin/env bash
# Fetch Gao et al. 2023 (PMID:36867023) inputs: GEO:GSE208707 supplementary
# files and the eLife Supplementary file 1 (DEG tables, used only to NAME the
# re-derived labels). Usage (from the clone root): bash <this script> DATA_DIR
set -euo pipefail
D=${1:?DATA_DIR}
mkdir -p "$D"
for f in barcodes.tsv.gz genes.tsv.gz matrix.mtx.gz metadata.csv.gz; do
  curl -sSL -o "$D/GSE208707_allnuclei_$f" \
    "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE208nnn/GSE208707/suppl/GSE208707_allnuclei_$f"
done
# eLife supplementary files via Europe PMC (zip of figures + elife-81818-supp1.xlsx)
curl -sSL -o "$D/PMC10014079_supp.zip" \
  "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10014079/supplementaryFiles"
unzip -o -q -j "$D/PMC10014079_supp.zip" elife-81818-supp1.xlsx -d "$D"
ls -la "$D"
