# Annotation transfer — KB import tasks

Curation tasks: run `annotation-transfer` orchestrator then write resulting
`AnnotationTransferEvidence` blocks into the relevant KB graph.

---

## OLM hippocampus

- Dataset: GSE124847
- Branch: `at/olm-hippocampus`
- AT results: → WMBv1 (CCN20230722)
- Status: Pipeline complete; KB import orchestrator not yet run
- Tags: `#annotation-transfer`

## Harris 2018 CA1 inhibitory neurons — hippocampus

- Dataset: GSE99888 (Harris 2018, 3663 CA1 inhibitory neurons STRT-seq)
- AT run: `kb/annotation_transfer_runs/at_run_20260506_harris_chamberland_mmc_wmbv1/`
- Status: **Complete** — imported 2026-05-11 into `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`
- Evidence added:
  - ivy_cell → SUPT_0203: Harris Class `Cacna2d1.Lhx6.Reln` (SUPPORT, F1=0.825)
  - olm_cell → SUPT_0216: Harris `Sst.Pnoc.Calb1.Igfbp5` (SUPPORT, recall=0.965) + Chamberland Chrna2 → CLUS_0771 (SUPPORT, F1=0.649)
  - bistratified → CLUS_0737: Chamberland `Sst_Tac1` (PARTIAL, subclass F1=0.578, cluster purity=0.939)
  - is_interneuron → SUPT_0179: Harris `Calb2.Vip.Igfbp4` (PARTIAL, F1=0.612)
  - NEW edge cck_basket → SUPT_0187 Sncg Gaba_3: Harris `Cck.Cxcl14.Vip` (PARTIAL, F1=0.768, recall=0.951)
- Tags: `#annotation-transfer`

## PV hippocampus

- Dataset: GSE142546 (Que 2021, PV patch-seq)
- Branch: `at/pv-hippocampus`
- Status: Awaiting SRA reprocessing before AT can run
- Tags: `#annotation-transfer`
