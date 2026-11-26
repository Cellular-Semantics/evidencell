# Bakken et al. 2021 mouse LGN clusters: what the labels refer to (#249)

Paper: Bakken et al. 2021 *eLife* 10:e64875, PMID:34473054, PMC8412930
(corpus 237389962). Data: GEO:GSE182211, mouse SMART-seq v4, 2,187 cells
(2,114 after dropping "Low Quality"). Mapping to WMBv1 (CCN20230722):
`kb/annotation_transfer_runs/at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1/`.

Sources read (2026-11-26):
- Full-text JATS (Europe PMC REST `PMC8412930/fullTextXML`). The artl-mcp
  `get_europepmc_full_text` tool returned empty for this paper, so the XML
  was fetched directly.
- Figure 4, Figure 4—figure supplement 1 and Figure 5—figure supplement 1
  images (eLife IIIF).
- Supplementary file 1 (specimen annotations, per cell).
- Supplementary file 4 (cluster markers, mouse sheet).
- GEO `GSE182211_mouse_LGN_2021_metadata.csv.gz` (sha256 c99ab4f2…, the
  same file as the run record).

Quotes are in `references/thalamus/quotes/237389962.json` (`added_by:
20261126_at_bakken2021_labels`). Figure content, i.e. cluster names on axes,
dot-plot markers and Fig 4C dot positions, is read from the images and is
not quotable text. It is recorded here as figure readings.

## Q3 first: which GEO label column is authoritative

**`cluster_label`.**
- Supplementary file 1 is the paper's own per-cell table. Joined on
  `sample_name`, its `cluster_label` is identical to GEO `cluster_label` for
  all 2,187 mouse cells, except that the paper writes the dLGN interneuron
  clusters as `Chrna6_1`, `Chrna6_2` and `Chrna6_3`. These are GEO `Chrna1`,
  `Chrna2` and `Chrna3`, 1:1.
- Figure 4A gives the cluster sizes Chrna1 146, Chrna2 252, Chrna3 54,
  GABA1 54, GABA2 26, GABA3 42, GABA4 19, GABA5 127, GABA6 82, LGv 15,
  LP 194 and LGd 1012. These match `cluster_label` counts: the GEO deposit
  has GABA5 126 and LP 193, an off-by-one each from QC.
- Figure 4A's markers also match `cluster_label`: GABA1 is Pvalb (RT) and
  GABA3 is Htr1a.
- `org_cl.lab` is a permutation of the names: Chrna1↔Chrna2, and
  GABA1→GABA5's cells, etc. It is permuted the same way in Supplementary
  file 1. Under it, "Chrna1" would be 252 cells and "GABA1" 126, which
  contradicts Figure 4A. It is not the published naming.
- `cluster_label.int` is `cluster_label` with the suffix `_Mo`.

The #233 runs used `cluster_label` and are correct. The pooled Chrna1–3 set
is identical under every column.

## Label → paper-type key

Dissection counts are from GEO `dissection_roi`. "Fig 4C" is the location of
the cluster's dot in the Figure 4C schematic. The paper says the anatomical
locations come from the clusters' marker genes checked against Allen Brain
Atlas ISH (quote `237389962_39108050`, `237389962_91b45608`). The WMB column
is context only. It is the existing mapping and was never used to name or
assign a cluster.

| GEO `cluster_label` | Paper name (Fig 4A / Supp 1) | n | Fig 4A markers | Supp 4 top markers | Fig 4C location | LGv | LP | dLGN core | dLGN shell | 2018 label (GEO `old.cluster`, majority) | WMB landing (context only) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Chrna1 | Chrna1 / Chrna6_1 | 146 | Chrna6, Styk1, Dscaml1 | Plcb1, Unc5d, Gad1, Pcdh20, Chrnb3 | dLGN (C1) | 0 | 1 | 126 | 19 | LGN Inh Chrna6 Dscaml1 (131) | 0872 SCsg Gabrr2 Gaba_1 |
| Chrna2 | Chrna2 / Chrna6_2 | 252 | Chrna6, Pax7, Pde3a | Synpr, Trpm3, Scgn, Gad1 | dLGN **and** LGv (C2) | 2 | 9 | 146 | 95 | LGN Inh Chrna6 Pax7 (140) / Cnr1 (98) | 0872 |
| Chrna3 | Chrna3 / Chrna6_3 | 54 | Chrna6, Alyref, Dapk3 | Lmo1, Marcks, Scgn, Gad1, Otx2 | dLGN (C3) | 2 | 14 | 38 | 0 | LGN Inh Chrna6 Dscaml1 (22) / Pax7 (20) | 0872 |
| GABA1 | GABA1 | 54 | Pvalb | Pvalb, Trh, Sst | RT (G1) | 19 | 0 | 32 | 3 | RT Inh Pvalb (43) | 0435 RT-ZI Gnb3 Gaba_5 |
| GABA2 | GABA2 | 26 | Spata20 | Fxyd6, Aldoc, Pax6, Cartpt | LGv (G2) | 3 | 0 | 20 | 3 | vLGN Inh Spata20 (25) | 0465 ZI Pax6 Gaba_7 |
| GABA3 | GABA3 | 42 | Dscaml1, Htr1a | Pcdh15, Nxph1, Dgkb | LGv (G3) | 31 | 0 | 10 | 1 | vLGN Inh Shox2 Htr1a (27) | 0840 LGv-SPFp-SPFm Nkx2-2 Tcf7l2 Gaba_7 |
| GABA4 | GABA4 | 19 | Penk | Penk, Resp18, Vgf, Calb2 | IGL **and** LGv (G4) | 17 | 0 | 0 | 2 | vLGN Inh Shox2 Sox14 (11) | 0835 / 0838 |
| GABA5 | GABA5 | 126 | Dlx5, Stc1 | Sst, Rmst, Resp18 | LGv (G5) | 65 | 3 | 38 | 20 | vLGN Inh Dlx5 Cbln2 (73) | split: 109 LGv-ZI Otx2, 0469 ZI Pax6 |
| GABA6 | GABA6 | 82 | Rspo2 | Npy, Penk, Fxyd6, Rab3b | IGL (G6) | 10 | 0 | 42 | 30 | vLGN Inh Shox2 Sox14 (50) / Rspo2 (21) | 0834–0838 |
| LGd | dLGN | 1012 | Scn4b, Adamts19, Slc17a6 | Prkcd, Pcp4 | dLGN | 0 | 0 | 682 | 330 | LGN Exc Scn4b | 2650 TH Prkcd Grin2c Glut_2 |
| LGv | LGv (glutamatergic) | 15 | Slc17a7, Neurod6 | Nrgn, Snca, Lamp5, Arc, Egr1 | LGv | 15 | 0 | 0 | 0 | HIP Exc Neurod6 (11) | 0023/0024 L4/5 IT CTX Glut |
| LP | LP | 193 | Slc17a6, Calb1, Gpr4 | Calb2, Calb1, Necab1 | LP | 0 | 155 | 31 | 7 | LP Exc Glra3 (51), Outlier (54) | 0659 / 0657 / 0660 / 0658 |
| Oligo1–3 | Oligo1–3 | 53/28/12 | — | MOL / OPC / COP genes | — | 14/4/2 | 1/1/1 | 22/13/6 | 16/10/3 | — | MOL / OPC / COP |
| Low Quality | — | 73 | — | — | — | 2 | 2 | 38 | 31 | — | dropped |
| **all** | | 2187 | | | | 186 | 187 | 1244 | 570 | | |

The `dLGN-core` dissection is evidently leaky. It holds 32 RT cells (GABA1),
38 GABA5, 42 GABA6, 20 GABA2 and 31 LP cells. The authors say as much
(quote `237389962_93431f28`), so dissection origin on its own does not
locate a cluster.

## Answers

### Q1. GABA2–6

- **What the paper says.**
  - GABA2–6 are not dLGN cells: "the mouse GABA2-6 types are not found in
    dLGN but are located only in the adjacent thalamic nuclei; IGL, LGv, and
    LP (Figure 4C)" (`237389962_6fbaf310`).
  - They form the forebrain-derived, Sox14-negative GABAergic branch defined
    by Npy, Nkx2-2 and Dlx1/2/5/6 (`237389962_23c05f79`; Fig 5—figure
    supplement 1A/D, integrated subclass bar).
  - Figure 4C places G2, G3 and G5 in LGv, G6 in IGL and G4 in both IGL and
    LGv. None is placed in LP, although the text lists LP.
  - Beyond markers and this placement, the paper says nothing about any
    GABA2–6 cluster: no lamina (vLGNe/vLGNi), projection target, morphology
    or physiology.
  - By eye, Fig 5—figure supplement 1D shows moderate Sox14 in GABA4 and
    GABA6. The text says only that "some types in … LGv and … IGL express
    Sox14" (`237389962_23ad2cf2`) and does not name them.
- **Dissection.** See the table. GABA3 (31/42) and GABA4 (17/19) are mainly
  from the LGv dissection. GABA5 is split (65 LGv, 58 dLGN). GABA2 (20/26)
  and GABA6 (72/82) are mainly from dLGN-core/shell dissections. GABA6 is an
  IGL type per Fig 4C, and IGL lies between dLGN and LGv with no IGL
  dissection of its own, so a dLGN-dissection origin fits.
- **Correspondence to vLGN nodes.**
  - `vlgn_gabaergic_neuron`: GABA2, GABA3 and GABA5 are **SUBSET** (each a
    cluster the paper places in LGv only). GABA4 is **PARTIAL** (IGL + LGv).
    GABA6 is not declared (IGL).
  - `lgv_igl_gabaergic_neuron` (umbrella, one entry): pooled
    "LGv/IGL GABA (GABA2-6)" is **SUBSET**, from derived run
    `at_run_20261126_bakken2021_lgn_lgvigl_mmc_wmbv1`. It is a subset
    because Chrna2 is also placed partly in LGv.
  - `vlgne_gabaergic_neuron`, `vlgni_gabaergic_neuron`,
    `vlgn_local_gabaergic_interneuron`, `vlgn_sc_projecting_gabaergic_neuron`:
    **not declared**. The paper gives no lamina, projection or local/projection
    information for any cluster.
  - `lgv_igl_sox14_gabaergic_neuron`: **not declared**. The paper puts
    GABA2–6 in the Sox14-negative branch and does not say which LGv/IGL
    types are Sox14+. Moderate Sox14 in GABA4/GABA6 in Fig 5—fs1D and the
    2018 label "Shox2 Sox14" are suggestive only. Follow-up: check Sox14 in
    the deposited counts before considering a PARTIAL entry.
- **GABA2 and zona incerta.**
  - The data do not support "ZI contamination of the LGv dissection": only
    3 of the 26 GABA2 cells came from the LGv dissection. Most came from
    dLGN-core.
  - The paper places GABA2 in LGv (Fig 4C; marker Spata20 checked against
    ABA ISH), and the 2018 label was already "vLGN Inh Spata20".
  - Supp 4 lists Pax6 among GABA2's top markers. Pax6 marks prethalamic
    derivatives, which include both LGv and ZI, so it doesn't discriminate.
  - The WMB landing (0465 ZI Pax6 Gaba_7; its clusters 1758/1759/1764 carry
    LGv among their top MERFISH nuclei) leaves ZI identity open.
  - Declared SUBSET on the paper's word, with this caveat in the entry
    notes. If the reviewer prefers a stricter rule (declare only where the
    paper and the dissection agree), drop the GABA2 entry.

### Q2. Chrna1/2/3

- **What the paper says.** These are the three GABAergic types assigned to
  dLGN (`237389962_d5bb7157`). They are Chrna6/Sox14+ and homologous to the
  primate SOX14+ dLGN GABAergic types (`237389962_35ac48b3`). The
  Discussion states that Sox14+ interneurons are the only mouse dLGN
  GABAergic interneurons; the Sox14− ones sit only in adjacent nuclei
  (`237389962_64554fbd`).
- **Names.** Fig 4A uses Chrna1/2/3. Fig 4B, Fig 5—fs1D and Supp 1 use
  Chrna6_1/2/3.
- **Location.** Fig 4C places C1 and C3 in dLGN, and C2 in dLGN and LGv.
- **Dissection.** All three are mainly dLGN-core. Chrna2 also has many
  shell cells (95). Chrna3 has 14 LP-dissected cells and no shell cells.
- **Are they distinct types?** Only by markers (Styk1; Pax7/Pde3a;
  Alyref/Dapk3). The paper gives no position, morphology, physiology or
  projection difference between them. All three fall in one integrated
  Sox14+ branch across species (Fig 5D, 5—fs1A), with no per-cluster
  species homology. Alyref and Dapk3, the Chrna3 markers, are also high in
  the glutamatergic LGv and LP clusters (Fig 4A), so Chrna3 may partly
  reflect a quality or doublet signal. The paper does not discuss this.
- **Decision: keep the pool, EXACT, on `dlgn_gabaergic_interneuron`.**
  - Per the paper, the three clusters together are the whole mouse dLGN
    GABAergic interneuron population.
  - They are not characterised as separate classical types.
  - Per-cluster entries would all land on the same WMB supertype (0872), at
    F1 diluted by siblings (0.22–0.71). That adds no mapping resolution.
  - Caveat in the entry notes: Fig 4C also places Chrna2 in LGv, so the pool
    could hold a few LGv Sox14+ cells. Only 4 of 452 cells came from the LGv
    dissection.
  - No child nodes proposed. The paper provides no classical basis for them.

### Q4. `LGv` glutamatergic (n = 15) and `LP`

- **LGv.**
  - The paper treats this as an LGv glutamatergic type: Fig 4C dot in LGv;
    "glutamatergic mouse LGv neurons clustered separately because this
    region was not sampled in primates" (`237389962_b395129c`).
  - All 15 cells come from the LGv dissection.
  - The paper's own Fig 4A shows Slc17a7 and Neurod6 as its markers, and
    Supp 4 lists Nrgn, Lamp5, Arc and Egr1. That is a cortical/hippocampal
    pyramidal profile. 11/15 cells carried the 2018 label "HIP Exc Neurod6",
    and the cells map to WMB L4/5 IT CTX.
  - Conclusion: the paper does not call it contamination. Its own markers
    and the depositor's earlier label point to hippocampal/cortical
    contamination of the LGv dissection. Treat it as uninformative for
    thalamus. No declaration.
- **LP.**
  - The paper treats it as one LP relay type that resembles macaque inferior
    pulvinar and K neurons (`237389962_efeb9148`). It reports no LP
    heterogeneity.
  - The split across WMB supertypes 0659/0657/0660/0658 (best F1 0.74,
    coverage 0.59) is therefore not explained by the paper. It may reflect
    LP subdivisions that WMB resolves and that the paper's sampling did not.
  - The 31 dLGN-core cells in this cluster also show dissection spill.
  - No LP node, so no declaration.

### Q5. dLGN core vs shell

- The paper reports one glutamatergic dLGN cluster. Its main axis of
  variation follows core vs shell (`237389962_45eeb70e`): graded rather than
  discrete, "TC neurons in mouse dLGN cannot be grouped into discrete types
  based on gene expression, although many genes show graded expression
  differences between core and shell regions" (`237389962_72e7c5bb`).
- RNAscope validation: core Pvalb/Scnn1a, shell Necab1/Calb1, plus a few
  intermediate cells.
- Both dissections landing in WMB 2650 matches what the paper reports, a
  continuum within one type. It is not a limit of WMB resolution.
- Not declared. `dlgn_core_relay_neuron` / `dlgn_shell_relay_neuron` are in
  open PR #234. Revisit once it merges, using
  `at_run_20261117_bakken2021_lgn_coreshell_mmc_wmbv1`, most likely as
  PARTIAL (dissection-enriched, graded).

## Declarations made (2026-11-26, branch content/thalamus-at-bakken2021-labels)

| Node | source_label | Run | Correspondence |
|---|---|---|---|
| `vlgn_gabaergic_neuron` | GABA2 | at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1 | SUBSET |
| `vlgn_gabaergic_neuron` | GABA3 | same | SUBSET |
| `vlgn_gabaergic_neuron` | GABA5 | same | SUBSET |
| `vlgn_gabaergic_neuron` | GABA4 | same | PARTIAL |
| `lgv_igl_gabaergic_neuron` | LGv/IGL GABA (GABA2-6) | at_run_20261126_bakken2021_lgn_lgvigl_mmc_wmbv1 | SUBSET |
| `dlgn_gabaergic_interneuron` | dLGN GABA (Chrna1-3) | at_run_20261117_bakken2021_lgn_dlgnin_mmc_wmbv1 | EXACT (kept; notes and sources revised) |

## Follow-ups

- Once #234 merges, declare core/shell on the new dLGN relay subtype nodes.
- Check Sox14 in the deposited counts for GABA4/GABA6. That decides whether
  a PARTIAL entry on `lgv_igl_sox14_gabaergic_neuron` is warranted.
- IGL-only nodes are out of scope here. GABA6 (and the IGL part of GABA4) is
  the candidate for `igl_gabaergic_neuron` once the IGL/TRN subtype work in
  evidencell_1 and evidencell_5 lands.
