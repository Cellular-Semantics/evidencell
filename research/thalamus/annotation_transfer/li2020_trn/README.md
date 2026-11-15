# Li et al. 2020 TRN → WMBv1 (CCN20230722) — staged AT inputs

**Status: BLOCKED before mapping** on
[evidencell#208](https://github.com/Cellular-Semantics/evidencell/issues/208).
The AT tooling only accepts raw integer counts, and this dataset is only
published as TPM. No `AnnotationTransferRun` record exists yet. This folder holds
the inputs, the label sets and the scripts, so the run can start as soon as #208 lands.

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
  (Spp1+ 264, Ecel1+ 213, DN 160, DP 34). These match the paper's Extended
  Data Fig. 3d counts (Spp1+ 264, DP+DN 195, Ecel1+ 212). The file downloads need
  a login, but the public explore API returns the cluster plus annotation;
  `scripts/fetch_inputs.sh` saves it as `scp344_type.tsv`. **The labels are
  not re-derived here.**

## Label schemes (two separate AnnotationTransferRun records, one shared MapMyCells output)

| Run (planned) | Labels file | Labels | Node(s) |
|---|---|---|---|
| plain | `labels_trn_pvalb.json` | all 670 cells → `TRN Pvalb+` | `trn_gabaergic_neuron` (PARTIAL) |
| relabel | `labels_spp1_ecel1_type.json` | SCP344 `Type`: Spp1+ 263, Ecel1+ 213, DN 160, DP 34 | `trn_spp1_core_neuron` (Spp1+, EXACT), `trn_ecel1_shell_neuron` (Ecel1+, EXACT); DP/DN are scored but not attached |

One SCP344 cell (`TRN_X`, a Spp1+ cell) has a mangled id with no GEO column and
is dropped, leaving 670 of 671 cells.

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

## TPM handling (planned, pending #208)

The transform is X = log2(expm1(x) + 1) = log2(TPM+1), fed to MapMyCells with
`type_assignment.normalization = log2CPM`. TPM is treated as CPM-like because
both sum to 1e6 per cell. The difference is full-length gene-length
normalisation, which Smart-seq2 + RSEM applies; WMBv1 10x reference statistics
do not. Per-cell sums of expm1(x) range from 0.46 to 1.36 M rather than exactly
1e6, presumably because the table is filtered to 23,420 genes. This goes into
the run manifest's `caveats`.

## Reproduce (up to the block)

```bash
bash research/thalamus/annotation_transfer/li2020_trn/scripts/fetch_inputs.sh
uv run --project annotation_transfer python -I \
  research/thalamus/annotation_transfer/li2020_trn/scripts/prepare_li2020_trn.py \
  annotation_transfer/inputs/datasets/li2020_trn \
  research/thalamus/annotation_transfer/li2020_trn/scp344_type.tsv \
  annotation_transfer/inputs/datasets/li2020_trn \
  research/thalamus/annotation_transfer/li2020_trn
just at-preflight inputs/datasets/li2020_trn/li2020_trn_pvalb_log2tpm.h5ad   # OK: 670 x 23420
# just at-convert ... → ConversionError: X does not contain integer counts  (#208)
```

## Patch-seq (not attempted)

`GSE145273_TPM.patch.tsv.gz` has 95 Patch-seq cells in linear TPM. The paper
analysed 76, and per-cell Spp1+/Ecel1+/DP/DN calls are not deposited, so labels
would have to be derived. Also, under the same GEO accession, labels like `Spp1+`
would collide with the snRNA-seq source labels (noted on #208, see also #204).
