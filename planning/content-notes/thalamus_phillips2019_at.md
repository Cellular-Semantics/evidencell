# Phillips 2019 thalamic projection-seq — AT interpretation notes

Source: Phillips et al. 2019, *A repeated molecular architecture across thalamic
pathways*, Nat Neurosci (PMID:31527803). Code: https://github.com/aschulmann/ThalamoSeq

AT runs (→ WMBv1, CCN20230722), registered 2026-11-15:
- `kb/annotation_transfer_runs/at_run_20261115_phillips2019_projection_mmc_wmbv1/` — 5 projection-system labels
- `kb/annotation_transfer_runs/at_run_20261115_phillips2019_syscluster_mmc_wmbv1/` — 17 per-system clusters (same `mmc_results.csv`)

Branch / PR: `content/thalamus-at-phillips2019`, draft PR #211.
Target nodes: `kb/graphs/thalamus/dlgn_relay_neuron.yaml`,
`kb/graphs/thalamus/thalamic_glutamatergic_projection_neuron.yaml`.

Tags: `#annotation-transfer` `#thalamus`

---

## The experiments

Both datasets share one preparation:
1. A retrograde label is injected into a cortical area: rAAV2-retro (Cre-dependent GFP or tdTomato), DiI, or red retrobeads.
2. Survival time is at least 3 weeks for virus and at least 4 days for tracers.
3. Coronal slices of 200–300 µm are cut, and the labelled thalamic region is microdissected by eye against the Paxinos atlas.
4. The tissue is dissociated with pronase plus activity blockers, and fluorescent cells are hand-picked.

| | GSE133911 (pooled) | GSE133912 (single-cell) |
|---|---|---|
| Unit | Pooled labelled cells from **one dissected nucleus** | One labelled cell per well (Smart-seq2 lysis, barcoded 3′ RT + UMIs) |
| Scale | 8 projection targets, 22 nuclei, 120 samples | 1,972 cells, 20 mice, 5 cortical targets |
| Label | Nucleus **and** projection target | Projection target only (+ authors' clusters) |
| Use in paper | Defines primary/secondary/tertiary axis (PC1 ≈ mediolateral) | Shows that axis repeats within each projection system |

Collection details for the single-cell data:
- For each system the authors collected "only the major projection complex in thalamus ... avoiding the relatively sparsely labeled midline cells" (Fig. 5 legend).
- The collection is therefore biased against tertiary nuclei.
- Clusters (Vis_1 etc.) were defined per system, "irrespective of nuclear boundaries".

Injection coordinates (Supp. Table 3; mm from bregma):

| System | Antero-posterior | Lateral | Depth |
|---|---|---|---|
| Visual | 2.9 and 3.8 caudal | 1.7–3.0 | — |
| Somatosensory | 0.85–1.5 caudal | 2.25–2.75 | 0.4 |
| Motor | 0.3–0.8 rostral | 1.4–1.6 | — |
| Prefrontal | 1.7–2.0 rostral | 0.4–1.6 | 1.5–3.0 |
| Auditory | 3.16–3.5 caudal | 4.5 | 2.0–2.25 |

## Interpretation caveats for the AT results

1. **A label names the target cortex, not a nucleus or cell type.** Projection labels span several WMB supertypes, so F1 peaks at only 0.42–0.62 (supertype). Read `label_distribution.tsv`, not the best-F1 target.
2. **Nucleus composition per system is inferred, not recorded.**
   - Neither the metadata nor Supp. Table 3 names the nuclei.
   - The working composition (Visual = LGd+LP, Motor = VA/VL, Somatosensory = VB+PO, Auditory = MGB, Prefrontal = MD) comes from `thal_singlecell.Rmd` object names and Fig. 7a.
   - The mapping shows this is incomplete for Visual. About 20% of Visual cells land in LD-dominant supertype 0658 (LD 0.77) / cluster 2655 (LD 0.53).
   - This is plausibly explained by the 2.9 mm-caudal visual injections reaching higher-order/medial visual areas that get LD input.
3. **Within-dataset purity can be a design artefact.** CLUS_2650 (LGd 0.72) is 100% Visual partly because no other system dissected LGd.
4. **Clusters shared across systems are ambiguous.**
   - Motor, Somatosensory and Visual cells all populate the PO/VPM-dominant clusters 0659/2663 and 0654/2648.
   - This may be real multi-target projection (PO → S1 and M1) or label spread / DiI fibre-of-passage uptake. This dataset cannot separate them.
   - A minority of a label in a cluster is weak evidence about that cluster's projection.
5. **Retrograde label = projects to *at least* the injected area.** Collaterals are invisible.
6. **Midline/intralaminar nuclei are under-sampled.**
   - Cells that do appear are edge-of-dissection catches: PVT CLUS_2621 in Prefrontal, RE/VM supertype 0669.
   - Absence of a tertiary cluster tells you nothing.
7. **The dominant-nucleus column comes from MERFISH CCF registration and is boundary-prone.** Auditory cells land mainly in 0660/2665, annotated "LP 0.50; SGN". That is the caudal LP–SGN–POL–MGd border, not literally LP neurons projecting to auditory cortex.
8. **Technical**
   - Dissociation stress genes are likely present.
   - 22,169 / 36,679 gene symbols mapped to Ensembl IDs.
   - Bootstrap thresholds apply per level, so counts differ between levels (Vis: 55 cells at CLUS_2650 vs 31 at parent SUPT_0655).

## Consequences for the KB nodes

- **`dlgn_relay_neuron`**
  - What the AT supports: some visual-cortex-projecting neurons fall in CLUS_2650, whose cells sit mostly in LGd per WMB MERFISH. Vis_1 → 2650 has F1 0.77.
  - The LGd location comes only from WMB anatomy, not the source data. So:
    - Visual is a **SUPERSET** of dLGN relay.
    - Vis_1 = dLGN must **not** be authored as an `at_source_sets` correspondence (circular).
  - The nucleus-resolved GSE133911 samples (LGd labelled from V1) are the way to close this. Run them through the correlation route.
- **`thalamic_glutamatergic_projection_neuron`**
  - All 5 systems are SUBSETs.
  - Cluster-level detail adds little.
  - Anterior group (AD/AV/AM) and midline nuclei are not represented in the single-cell data.

Proposed `at_source_sets` (quotes verified verbatim; in PR #211 body):
- `dlgn_relay_neuron`: Visual, SUPERSET; quotes `202579938_7a08d6ac`, `202579938_08d61862`.
- `thalamic_glutamatergic_projection_neuron`: all 5 systems, SUBSET; quotes `7a08d6ac`, `0401b688`, `9ec9148a`, `8271cf07`.

## Status / TODO

- [x] MapMyCells + F1 scoring (both label schemes)
- [x] Manifests written, `at_metrics migrate`, `just register-at-run`, `just validate-at-results-all` (after #209 fix, merged in #212)
- [ ] F1 [GATE] review (PR #211)
- [ ] Author `at_source_sets` + quotes on the two nodes (no edges exist yet, so no edge/confidence changes)
- [ ] GSE133911 pooled correlation run (own record)
- [ ] Follow-ups:
  - PVT (Pfr_3 → CLUS_2621)
  - AD/AV/AM via pooled data
  - MD, VAL/VM, LD candidate nodes
