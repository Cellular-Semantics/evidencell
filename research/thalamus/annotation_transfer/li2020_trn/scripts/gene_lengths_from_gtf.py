"""Gene lengths (bp, union of exons) keyed by Ensembl gene ID, for `at-normalize --gene-lengths`.

Li et al. 2020 quantified with RSEM against mm10 (GRCm38) and published only
TPM, which is gene-length normalised. WMBv1 is 10x (UMI, not length
normalised), so the TPM is multiplied back by length/1000 before rescaling to
CPM. RSEM's per-gene effective lengths were not deposited; the union-of-exons
length from Ensembl release 102 (the last GRCm38 annotation) is used as the
closest available stand-in.

Keyed by Ensembl gene ID because prepare_li2020_trn.py remaps the GEO symbols
to WMBv1's Ensembl IDs before normalisation.

Usage:
  uv run --project annotation_transfer python -I \
    research/thalamus/annotation_transfer/li2020_trn/scripts/gene_lengths_from_gtf.py \
    annotation_transfer/inputs/datasets/li2020_trn/ensembl/Mus_musculus.GRCm38.102.gtf.gz \
    annotation_transfer/inputs/datasets/li2020_trn/gene_lengths_ens102.tsv
"""

from __future__ import annotations

import gzip
import re
import sys
from collections import defaultdict
from pathlib import Path

GENE_ID = re.compile(r'gene_id "([^"]+)"')


def union_length(intervals: list[tuple[int, int]]) -> int:
    total, cur_s, cur_e = 0, None, None
    for s, e in sorted(intervals):
        if cur_e is None or s > cur_e + 1:
            if cur_e is not None:
                total += cur_e - cur_s + 1
            cur_s, cur_e = s, e
        else:
            cur_e = max(cur_e, e)
    if cur_e is not None:
        total += cur_e - cur_s + 1
    return total


def main(gtf: Path, out: Path) -> None:
    exons: dict[str, list[tuple[int, int]]] = defaultdict(list)
    with gzip.open(gtf, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.split("\t", 8)
            if parts[2] != "exon":
                continue
            gid = GENE_ID.search(parts[8]).group(1)
            exons[gid].append((int(parts[3]), int(parts[4])))

    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        f.write("gene_id\tlength_bp\n")
        for gid in sorted(exons):
            f.write(f"{gid}\t{union_length(exons[gid])}\n")
    print(f"{len(exons)} Ensembl genes; wrote {out}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
