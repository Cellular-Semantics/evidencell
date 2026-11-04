# AT Run: Hochgerner 2023 mouse amygdala → WMBv1 (CCN20230722)

## Purpose

Map Hochgerner 2023 naive amygdala neuronal cell types to WMBv1 clusters to
generate AnnotationTransferEvidence for amygdala KB nodes. Addresses the
AT_ABSENT ceiling on all 15 amygdala mapping edges.

## Data source

- Paper: Hochgerner et al. 2023, Nat Neurosci. PMID 37884748.
- ArrayExpress: E-MTAB-12096
- Figshare annotated matrix: https://ndownloader.figshare.com/files/36500010
  (Amy_FC_allcells_with_metadata_31-Jul-2022.txt, 3.1 GB)

## Reproduction steps

### Step 1 — Download and convert

```bash
cd annotation_transfer/inputs/datasets/hochgerner2023_amygdala/
uv run --project ../../ python convert.py
# Output: hochgerner2023_amygdala_naive_neuronal.h5ad
```

### Step 2 — Validate and convert for MapMyCells

```bash
cd annotation_transfer/
just at-convert \
  inputs/datasets/hochgerner2023_amygdala/hochgerner2023_amygdala_naive_neuronal.h5ad \
  inputs/datasets/hochgerner2023_amygdala/hochgerner2023_amygdala_ready.h5ad
```

### Step 3 — Generate source labels JSON

```python
import anndata, json
adata = anndata.read_h5ad(
    "annotation_transfer/inputs/datasets/hochgerner2023_amygdala/"
    "hochgerner2023_amygdala_naive_neuronal.h5ad"
)
labels = dict(zip(adata.obs_names, adata.obs["celltype"]))
with open(
    "kb/annotation_transfer_runs/"
    "at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/"
    "source_labels.json", "w"
) as f:
    json.dump(labels, f)
```

### Step 4 — Run MapMyCells (local)

```bash
cd annotation_transfer/
just at-map \
  inputs/datasets/hochgerner2023_amygdala/hochgerner2023_amygdala_ready.h5ad \
  CCN20230722 \
  ../../research/medial_temporal_lobe_amygdala/annotation_transfer/hochgerner2023_amygdala/
```

### Step 5 — Score F1

```bash
cd annotation_transfer/
just at-score \
  ../../research/medial_temporal_lobe_amygdala/annotation_transfer/hochgerner2023_amygdala/mmc_output.csv \
  ../kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/source_labels.json \
  ../../research/medial_temporal_lobe_amygdala/annotation_transfer/hochgerner2023_amygdala/f1_matrix.csv
```

### Step 6 — Parse results and write AnnotationTransferEvidence

Use `just at-extract-f1` per classical node:

```bash
cd annotation_transfer/
just at-extract-f1 \
  kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1 \
  cea_pkc_delta_neuron \
  "GABA-8-Prkcd-Oprk1,GABA-9-Prkcd-Ezr,GABA-10-Prkcd-Adora2a,GABA-16-Prkcd-Nts" \
  amygdala \
  --floor 0.2
```

## Hochgerner celltype → KB classical node mapping

| Hochgerner types | KB classical node |
|---|---|
| GABA-8-Prkcd-Oprk1, GABA-9-Prkcd-Ezr, GABA-10-Prkcd-Adora2a, GABA-16-Prkcd-Nts | cea_pkc_delta_neuron |
| GABA-26-Cbln4-Sst, GABA-36-Sst-Fign, GABA-37-Sst-Npy, GABA-38-Sst-Tmtc4, GABA-39-Sst-Nek7, GABA-40-Rpb4-Sst | cea_som_neuron |
| GABA-13-Adora2a-Crh | cea_crf_neuron |
| GABA-18-Isl1-Tac1, GABA-19-Isl1-Aldoc | cea_isl1_projection_neuron |
| GABA-1-Foxp2_Fmod, GABA-2-Foxp2_Adra2a, GABA-3-Foxp2_Col6a1, GABA-4-Foxp2_Htr1f | amygdala_intercalated_cell, intercalated_cell_mass_neuron |
| GABA-14-Drd1-Scn4b, GABA-15-Drd1-Ebf1 | cea_medium_spiny_neuron |
| GABA-11-Adora2a-Id4, GABA-12-Adora2a-Scn4b | cea_medium_spiny_neuron (Adora2a = A2a receptor, MSN marker) |
| GABA-41-Moxd1-Pvalb, GABA-44-Pthlh-Pvalb | bla_pv_basket_cell |
| GABA-44-Pthlh-Pvalb | bla_pv_axo_axonic_cell (Pthlh = chandelier marker) |
| GABA-45-Lamp5-Hctr2, GABA-46-Lamp5-Kit | bla_lamp5_interneuron |
| GABA-54-Scng-Kcnc2, GABA-55-Sncg-Vip, GABA-56-Sncg-Krt73 | bla_cck_basket_cell, bla_cck_cb1_basket_cell |
| GABA-35-Chodl-Moxd1 | bla_gabaergic_projection_neuron (Chodl = long-range GABAergic marker) |
| VGLUT1-2-Rspo2_Sema3e | basal_amygdala_fear_neuron (Rspo2 = fear neuron marker) |
| GABA-29-Prlr-Greb1 through GABA-34-Prlr-Satb1 | medial_amygdala_gabaergic_neuron |
