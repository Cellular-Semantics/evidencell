# Li et al. 2020 TRN → WMBv1 (CCN20230722) — annotation transfer

**Status: mapped and scored; awaiting the F1-matrix `[GATE]`.** Mapping was
unblocked by #208 / PR #222 (`--normalization log2CPM`). There are two run records
sharing one MapMyCells output (`mmc_results.csv` here):

- `kb/annotation_transfer_runs/at_run_20261117_li2020_trn_pvalb_mmc_wmbv1` (plain)
- `kb/annotation_transfer_runs/at_run_20261117_li2020_trn_spp1ecel1_mmc_wmbv1` (relabel)

Their manifests carry the full caveats.

## Results (headline)

| Label (n) | Best target | Level | Coverage | Purity | F1 |
|---|---|---|---|---|---|
| TRN Pvalb+ (670) | 093 RT-ZI Gnb3 Gaba | subclass | 0.996 | 1.0* | 0.998 |
| Spp1+ (264) | 0435 RT-ZI Gnb3 Gaba_5 | supertype | 0.996 | 0.50 | 0.67 |
| Spp1+ (264) | 1604 RT-ZI Gnb3 Gaba_5 | cluster | 0.98 | 0.76 | 0.86 |
| Ecel1+ (212) | 1601 RT-ZI Gnb3 Gaba_5 | cluster | 0.22 | 0.78 | 0.34 |

\* single-label run: purity is 1.0 by construction.

- **Core (Spp1+) ↔ CLUS 1604.** F1 rises with resolution (0.57 → 0.67 → 0.86).
  The rest of 1604 is mostly DN/DP. In the WMBv1 precomputed means, 1604 is the
  only 093 cluster with high Spp1 (7.6 log2CPM) and low Ecel1 (0.9).
- **Shell (Ecel1+) ↔ "093 minus 1604", one-to-many.** 95% of confidently mapped
  Ecel1+ cells fall outside 1604, spread over the Ecel1-high, Spp1-low clusters
  1601, 1593, 1588, 1600, 1602, 1603 and supertypes 0431–0434, at purity
  0.72–0.92 for the larger ones. No single target reaches F1 0.6, so read purity
  over F1 here.
- **Not robustness-sensitive.** Re-mapping without the gene-length correction
  agrees cell-for-cell at 99.9% (subclass), 98.7% (supertype) and 95.4% (cluster).

## SCP344 name/annotation offset (important)

As returned by the SCP344 API, the cell names are **shifted one row** against
the `Type` annotation (and the biSNE coordinates). The first name, `TRN_X`, is
an R row-names artefact. Paired as returned, `Type` agrees with the paper's
binarised Spp1/Ecel1 calls (ln(TPM+1) > 1.1) for 34% of cells (chance); shifted
by one row, for 99.9%, and the counts then match the paper exactly (Spp1+ 264,
Ecel1+ 212). `scp344_type.tsv` is kept exactly as returned.
`prepare_li2020_trn.py` applies the shift and asserts the agreement. The label
file staged in PR #210 before this fix was wrong.

## Source

- Paper: Li et al. 2020 *Nature* 583:819, "Distinct subnetworks of the thalamic
  reticular nucleus", PMID:32699411, doi:10.1038/s41586-020-2504-5.
- Expression: GEO:GSE145273 suppl `GSE145273_TPM.TRN.tsv.gz` (Smart-seq2
  snRNA-seq, RSEM). 1687 nuclei from micro-dissected Pvalb-tdTomato TRN, plus
  thalamus and GPe control dissections. Despite the filename, the values are
  **ln(TPM+1)**: the paper says "log(TPM+1)", and the median number of genes at
  ≥ 1.1 is 3909, which matches the paper's reported median complexity. There are
  no raw counts or metadata on GEO. Raw reads: PRJNA606580 (not used).
- Labels: Broad Single Cell Portal **SCP344**, which holds only the 671 TRN
  Gad2+ Pvalb+ nuclei, with an author-deposited per-cell `Type` annotation
  (after alignment: Spp1+ 264, Ecel1+ 212, DN 160, DP 34). These match the
  paper's Extended Data Fig. 3d counts (Spp1+ 264, DP+DN 195, Ecel1+ 212). The file downloads need
  a login, but the public explore API returns the cluster plus annotation;
  `scripts/fetch_inputs.sh` saves it as `scp344_type.tsv`. **The labels are
  not re-derived here**, but they are re-aligned (see above).

## Label schemes (two separate AnnotationTransferRun records, one shared MapMyCells output)

| Run | Labels file | Labels | Node(s) |
|---|---|---|---|
| `..._pvalb_...` (plain) | `labels_trn_pvalb.json` | all 670 cells → `TRN Pvalb+` | `trn_gabaergic_neuron` (PARTIAL) |
| `..._spp1ecel1_...` (relabel) | `labels_spp1_ecel1_type.json` | SCP344 `Type`: Spp1+ 264, Ecel1+ 212, DN 160, DP 34 | `trn_spp1_core_neuron` (Spp1+, EXACT), `trn_ecel1_shell_neuron` (Ecel1+, EXACT); DP/DN are scored but not attached |

After the shift, `TRN_X` has no label and no GEO column, and the last row's
label has no cell: 670 labelled cells.

The Spp1+/Ecel1+ labels are binarised marker calls along a continuous gradient,
so for the relabel run, read purity over F1 at fine levels (see
`workflows/annotation-transfer.md` § Source-label purity).

## Projection: what the AT can and cannot show

The paper links Spp1+ cells to first-order (FO) thalamic projections and
Ecel1+ cells to higher-order (HO) ones. That link comes from **retrograde
RetroBead injections into FO/HO nuclei plus RNA-FISH in separate animals**:
85.7% of FO-labelled TRN neurons were Spp1+, and 86.0% of HO-labelled ones
were Ecel1+. DP/DN cells showed no bias. The sequenced nuclei themselves have
no projection data. AT can therefore tie a WMB cluster to a projection-defined
subnetwork only indirectly: projection → FISH marker → snRNA-seq marker call
→ MapMyCells.

## Query construction (TPM handling)

The steps are in the order run (all vendored or `just` recipes):

1. `prepare_li2020_trn.py`: ln(TPM+1) table → the 670 SCP344 cells; gene
   symbols → WMBv1 Ensembl IDs via `conf/gene_mapping_CCN20230722.tsv`
   (18,591 of 23,420 kept; unmapped symbols dropped, a duplicate Ensembl ID keeps
   its first symbol, as in the Harris 2018 run). X is kept as deposited.
2. `gene_lengths_from_gtf.py`: Ensembl 102 (last GRCm38 release; the paper
   used mm10) union-of-exon lengths per gene. RSEM's effective lengths were not
   deposited, so this is the closest stand-in. All 18,591 genes have a length.
3. `just at-normalize ... --input-scale ln1p --gene-lengths ...`: undo the log,
   multiply by length/1000 (undoing the TPM length normalisation against UMI-based
   WMBv1), rescale to 1e6, log2(x+1).
4. `just at-convert ... --normalization log2CPM`, then
   `just at-map-local ... --normalization log2CPM` (cell_type_mapper 1.7.5).
5. `just at-score` per label scheme into each run directory, then
   `python -m evidencell.at_metrics migrate` and `just register-at-run`.

## Reproduce

```bash
bash research/thalamus/annotation_transfer/li2020_trn/scripts/fetch_inputs.sh
D=annotation_transfer/inputs/datasets/li2020_trn
S=research/thalamus/annotation_transfer/li2020_trn
uv run --project annotation_transfer python -I $S/scripts/gene_lengths_from_gtf.py \
  $D/ensembl/Mus_musculus.GRCm38.102.gtf.gz $D/gene_lengths_ens102.tsv
uv run --project annotation_transfer python -I $S/scripts/prepare_li2020_trn.py \
  $D $S/scp344_type.tsv $D $S .
R=$PWD; D=$R/$D; S=$R/$S
just at-normalize $D/li2020_trn_pvalb_ln1ptpm.h5ad $D/li2020_trn_pvalb_log2cpm.h5ad \
  --input-scale ln1p --gene-lengths $D/gene_lengths_ens102.tsv -y
just at-convert $D/li2020_trn_pvalb_log2cpm.h5ad $D/li2020_trn_pvalb_ready.h5ad --normalization log2CPM -y
just at-map-local $D/li2020_trn_pvalb_ready.h5ad \
  $R/conf/mapmycells/CCN20230722/precomputed_stats.h5 $R/conf/mapmycells/CCN20230722/marker_genes.json \
  $D/mmc_out/mapping_result.json --csv $S/mmc_results.csv --normalization log2CPM
K=$R/kb/annotation_transfer_runs
just at-score $S/mmc_results.csv $S/labels_trn_pvalb.json $K/at_run_20261117_li2020_trn_pvalb_mmc_wmbv1/f1_matrix.csv
just at-score $S/mmc_results.csv $S/labels_spp1_ecel1_type.json $K/at_run_20261117_li2020_trn_spp1ecel1_mmc_wmbv1/f1_matrix.csv
```

Notes on the environment:

- `cell_type_mapper` needs `cd annotation_transfer && uv sync --extra mapper`.
- On Python 3.13 it also needs `uv pip install setuptools`, because its
  marshmallow pin imports `distutils`.
- `just at-map` (taxonomy-resolved) did not find the local stats from either
  working directory, so the explicit `at-map-local` route was used. Its
  results are identical by construction.

## Patch-seq (not attempted)

`GSE145273_TPM.patch.tsv.gz` has 95 Patch-seq cells in linear TPM. The paper
analysed 76, and per-cell Spp1+/Ecel1+/DP/DN calls are not deposited, so labels
would have to be derived. Also, under the same GEO accession, labels like `Spp1+`
would collide with the snRNA-seq source labels (noted on #208, see also #204).
