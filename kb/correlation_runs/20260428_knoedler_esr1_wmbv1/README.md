# Knoedler 2022 Esr1+ TRAP-seq → WMBv1 correlation

Run id: `corr_run_20260428_knoedler_esr1_wmbv1` ([manifest.yaml](manifest.yaml))
Dataset: `dataset_GSE183092` ([kb/datasets/GSE183092_knoedler_2022.yaml](../../datasets/GSE183092_knoedler_2022.yaml))

## Headline findings

| Classical node | Knoedler-supported update | Top hit |
|---|---|---|
| `vmhvl_esr1_pr_neuron` | **Add SUPT_0563 as co-primary CROSS_CUTTING target.** SUPT_0563 takes 3 of top-4 by δ(VMH_FR − BNST_FR), with female-biased CLUS_2290 (MFR 0.08) and CLUS_2292 (MFR 0.12) directly validated as the lordosis subpopulation flagged in the existing edge's open-questions section. | CLUS_2293 (SUPT_0563, VMH Fezf1 Glut_1) δ=0.0180 |
| `mpoa_esr1_neuron` | Top hit is SUPT_0521 (AVPV-MEPO-SFO Tbr1 Glut_3, **glutamatergic**), not the currently-mapped GABAergic SUPT_0486 (rank-5 sister SUPT_0482 is the existing lineage). Suggests classical node may need a glut/GABA split. | CLUS_2085 (SUPT_0521) δ=0.0151 |
| `bnst_crf_neuron` | SUPT_0358 (MEA-BST Lhx6 Nfib Gaba_2) candidate; CLUS_1290 maps to BST proper, CLUS_1293 carries MFR 99 (extreme male bias). Esr1 proxy — not direct CRF evidence; co-localisation needs ISH/MERFISH. | CLUS_1295 (SUPT_0358) δ=0.0161 |
| MeA Esr1+ (no current node) | Strong, anatomically clean signal — candidate for a new `mea_esr1_neuron` mapping if literature warrants. | CLUS_0197 (SUPT_0055 MEA Slc17a7 Glut_1, MFR 10.11) δ=0.0519 |

## Methodological caveat — cross-sex within-region δ is artefactual

Three within-region male-vs-female contrasts (POA, VMH, BNST) all return the same top hits — hindbrain Calcb cholinergic motor neurons. These have no anatomical or functional connection to any input region. Suspected cause: global male/female expression bias (Y-linked dosage, batch, TRAP pulldown efficiency).

**Rule:** paired-bulk δ requires the two pools to differ in **cell population** (region/marker/state) **holding sex constant**. `sdn_poa_calbindin_neuron` male-bias mapping cannot be answered with this method; alternative paired-bulk source (SDN-vs-surround dissection in same-sex animals) is needed.

## Reproduce

```
python kb/correlation_runs/20260428_knoedler_esr1_wmbv1/correlate.py
```

Outputs in `ranked_contrasts/`. Inputs in `data/` (region CSVs from GEO; checksums in [manifest.yaml](manifest.yaml)) plus `conf/mapmycells/CCN20230722/precomputed_stats.h5` and `conf/gene_mapping_CCN20230722.tsv` (project-relative).
