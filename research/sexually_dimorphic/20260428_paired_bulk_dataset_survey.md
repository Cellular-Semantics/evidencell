# Paired-bulk RNA-seq dataset survey for sexually dimorphic classical types

Date: 2026-04-28
Method: WebSearch on PubMed/GEO/lab pages. ~30 minutes effort. No WebFetch (denied) — accession numbers below were captured from search snippets and should be confirmed against the GEO record before use.

Goal: identify mouse paired-bulk RNA-seq datasets compatible with the differential-correlation method validated for Kiss1 RP3V vs ARC (Stephens/Manchishi 2024, PMID:37934722). Stephens 2024 already covers `avpv_th_neuron` and `avpv_kiss1_neuron` — those are skipped here.

---

## Headline finding

**Knoedler et al. 2022 (Cell, PMID:35008425 — confirm) is the single highest-value dataset for this project.** TRAP-seq paired bulk profiling of four Esr1+ neuronal populations — BNSTpr, POA, MeA, VMHvl — across female-receptive (FR), female-non-receptive (FNR), and intact male (M) states. GEO **GSE183092** (TRAP-seq) and **GSE183093** (snRNA-seq companion). This single deposit gives paired comparators for **at least four** of our nine classical types: vmhvl_esr1_pr, mpoa_esr1, bnst_crf (via Esr1+ BNSTpr proxy), and gives a region-level male/female comparator for sdn_poa_calbindin and arc_aromatase by extension.

---

## 1. avpv_th_neuron — covered by Stephens 2024. SKIP.

## 2. avpv_kiss1_neuron — covered by Stephens 2024. DONE.

## 3. sdn_poa_calbindin_neuron (SDN-POA Calb1+, male-biased)

No FACS-sorted Calb1-Cre bulk RNA-seq dataset was found targeting the SDN-POA specifically. The Calb1-Cre transgenic studies that exist (e.g. Tsuneoka 2023, J Neurosci 43(44):7322) used the line for circuit tracing and behavior, not transcriptomics.

**Best candidate (indirect):** Knoedler 2022 POA TRAP-seq (GSE183092). Esr1+ POA bulk includes the medial preoptic Esr1+ pool that overlaps SDN-POA Calb+ neurons (CALB-SDN expresses Esr1 and is testosterone-dependent). Paired comparator: male vs female POA Esr1+. The differential should reflect male-biased CALB-SDN content. Mouse, processed counts on GEO.

**Alternative:** Moffitt 2018 (Science, PMID:30385464) preoptic snRNA-seq + MERFISH. Single-cell, not bulk — not directly compatible with the paired-bulk method, but pseudobulk by cluster could be derived if needed.

**Status:** No clean direct dataset. Indirect via Knoedler POA TRAP only.

## 4. mpoa_esr1_neuron (MPOA ESR1+, sexually dimorphic)

**Primary candidate:** Knoedler 2022 (Cell, PMID:35008425 — confirm). TRAP-seq from POA Esr1+ neurons across M / FR / FNR. **GEO: GSE183092.** Paired comparators: male vs receptive female vs non-receptive female within the same Esr1+ population. Mouse. Bulk-equivalent (TRAP polysome IP, not FACS). Processed counts likely available.

**Secondary candidate:** Pubertal preoptic study (Bayless et al., bioRxiv 2021.09.02.458782, since published) — scRNAseq of MPOA Vgat+ Esr1+ across pubertal time points and gonadectomy ± hormone replacement. Single-cell rather than paired bulk; less directly suited to the differential method but pseudobulk-by-state could substitute.

**Tertiary:** Knoedler/Bayless 2025 bioRxiv (2025.02.26.640339) — Esr1 conditional KO in MPOA GABAergic neurons, RNA-seq comparator likely deposited. Confirm GEO.

## 5. vmhvl_esr1_pr_neuron (VMHvl ESR1+/PR+, both sexes)

**Primary candidate:** Knoedler 2022 — VMHvl Esr1+ TRAP-seq pool. **GEO: GSE183092.** Paired comparators across sex/estrous as above. Mouse. Bulk-equivalent.

**Secondary candidate:** Hashikawa et al. 2017 (Nature Neuroscience 20:1580–1590, PMID:28920934). Bulk RNA-seq of manually microdissected VMHvl anatomical subdivisions (VMHpvll vs VMHpvlm) in female mice, used to identify Cckar+ lateral and Crhbp+ medial markers. Paired comparator: anatomical subdivision (lateral vs medial) within VMHvl. **GEO: search for this paper's accession — listed in the article supplement. Candidates from search: GSM2778984, possibly under a parent GSE.** Mouse. Bulk RNA-seq, processed.

**Tertiary candidate:** Kim et al. 2019 (Cell 179:713–728, PMID:31626767) — multimodal SMART-seq + 10x scRNAseq of VMHvl. Single-cell, not paired bulk. Pseudobulk derivable. Listed in earlier searches as GSE156245 (confirm).

## 6. arc_aromatase_neuron (ARC Cyp19a1+, dimorphic)

No Cyp19a1-Cre / aromatase-Cre FACS-sorted bulk RNA-seq dataset of arcuate cells was found. Cyp19a1-IRES-Cre lines exist (Cyagen) but no published transcriptomics from them in ARC.

**Indirect candidate:** Stephens/Manchishi 2024 (already done) — Kiss1ARC vs Kiss1RP3V. Subset of ARC kisspeptin neurons partially overlap aromatase+ population in ARC. Differential ARC-specificity already captured.

**Indirect candidate 2:** Campbell et al. 2017 (Nat Neurosci 20:484–496, PMID:28166221) — drop-seq of ARC and median eminence. Not paired bulk; single-cell. **GEO: GSE93374.** Pseudobulk by cluster could give an aromatase+ vs aromatase− contrast within ARC.

**Status:** No direct paired-bulk dataset. Method would need pseudobulk-from-scRNAseq or rely on indirect ARC-vs-region contrast.

## 7. pmv_otr_neuron (PMv OTR+, male-biased)

No Oxtr-Cre or DAT-Cre PMv-targeted bulk RNA-seq dataset was found. Stagkourakis 2018 (Nat Neurosci 21:834–842) used DAT-tdTomato for circuit/behavior work in PMv but did not publish bulk RNA-seq of sorted PMvDAT cells. The follow-up Stagkourakis 2025/2026 (Nat Commun, PMID:41022751, "Maternal aggression…") may include PMvDAT TRAP/RiboTag — search captured the abstract but accession not surfaced. **Action: pull this paper's data-availability section.**

**Indirect candidate:** Mickelsen et al. 2020 (eLife 9:e58901, "Cellular taxonomy and spatial organization of the murine ventral posterior hypothalamus") — scRNAseq of ventral posterior hypothalamus including PMv. Not paired bulk. **GEO: search for this paper's accession.** Pseudobulk derivable.

**Status:** No direct paired-bulk dataset confirmed. Stagkourakis 2025 maternal aggression paper is the most likely source — needs follow-up.

## 8. pvn_crfr1_neuron (PVN CRFR1+, sexually dimorphic)

No Crhr1-Cre PVN-specific FACS or TRAP bulk RNA-seq dataset surfaced. Crhr1-Cre and Crhr1-FlpO lines exist but transcriptomics from PVN Crhr1+ cells specifically is not published as far as the search reached.

**Indirect candidate:** Berkhout et al. 2024 (J Neuroendocrinol 36:e13367, PMID:38281730) — integrated PVN scRNAseq atlas. Single-cell only. Pseudobulk-by-cluster could approximate the Crh-Nr3c1 type as a paired comparator vs other PVN neuroendocrine types.

**Status:** No direct paired-bulk dataset.

## 9. bnst_crf_neuron (BNST CRF+, sexually dimorphic)

No direct CRF-Cre BNST FACS bulk RNA-seq dataset surfaced. Itoga et al. 2021 (Sci Rep 11:13422) on BNST CRF pain encoding used calcium imaging, not RNA-seq.

**Primary indirect candidate:** Knoedler 2022 BNSTpr Esr1+ TRAP-seq. **GEO: GSE183092.** BNSTprTac1/Esr1+ overlaps with male-enriched CRF+ subset (Crh+ neurons in BNST oval/principal). Paired male/female contrast. Mouse, bulk-equivalent.

**Secondary candidate:** Gegenhuber et al. 2022 (Nature 606:153–159, PMID:35508660). Bulk RNA-seq, ATAC-seq, and snRNAseq of BNSTp Esr1+ cells, neonatal and adult, both sexes. Code at github.com/gegenhu/estrogen_gene_reg. **GEO: candidate GSE199453 (from search snippets) — confirm in paper Methods/Data Availability.** Excellent paired comparator quality (M vs F BNSTp Esr1+ across developmental windows). Mouse.

**Status:** Strong indirect coverage via Gegenhuber 2022 + Knoedler 2022.

---

## Run-next prioritised list

1. **Knoedler 2022 TRAP-seq, GSE183092** — single ingestion covers paired bulk for **VMHvl Esr1+ (vmhvl_esr1_pr_neuron)**, **MPOA Esr1+ (mpoa_esr1_neuron)**, **BNSTpr Esr1+ (bnst_crf_neuron, indirect via Esr1+/Tac1+ overlap)**, and a male/female POA contrast usable for **sdn_poa_calbindin_neuron**. Highest ROI. Paired comparators are M / FR / FNR within each region and male vs female across regions. Confirm processed-counts availability and gene mapping vs WMBv1.

2. **Gegenhuber 2022 BNSTp Esr1+, candidate GSE199453** — confirms `bnst_crf_neuron` mapping with a clean adult M-vs-F BNSTp Esr1+ paired contrast. Independent replication of the Knoedler signal. Highest specificity for the BNST node.

3. **Hashikawa 2017 VMHvl bulk** — only candidate with a *within-VMHvl anatomical* paired contrast (VMHpvll vs VMHpvlm), which is the exact comparator needed to discriminate Cckar+ female lateral (CLUS-level) from Crhbp+ medial within the VMHvl Esr1+ pool. Confirm GEO accession from the paper supplement before use.

Datasets 1+2 should be tractable inside a week — both have multiple paired bulk samples per region and are explicitly designed M/F comparisons that match the Stephens-method assumption that housekeeping noise cancels in the δ.

## Datasets explicitly NOT found (honest negatives)

- No Calb1-Cre SDN-POA FACS bulk RNA-seq.
- No Cyp19a1-Cre arcuate FACS bulk RNA-seq.
- No DAT-Cre or Oxtr-Cre PMv FACS bulk RNA-seq (Stagkourakis 2025 maternal aggression paper is the lead but data availability not confirmed in search results).
- No Crhr1-Cre or Crh-Cre PVN FACS or TRAP bulk RNA-seq specific to PVN CRFR1+ cells.

For these four nodes the paired-bulk correlation method is currently blocked at the data-availability layer; pseudobulk-from-scRNAseq (Campbell 2017 ARC, Mickelsen 2020 PMv, Berkhout 2024 PVN, Moffitt 2018 POA) is the only fallback and would not give the housekeeping-noise cancellation that makes the Stephens method work.

## Caveats

- All GEO accession numbers above were captured from search-result snippets (WebFetch was denied for paper Methods sections). Each must be verified against the published Data Availability statement before download.
- Knoedler 2022 uses TRAP-seq, not FACS. TRAP gives polysome-bound mRNA, which differs subtly from total mRNA in single cells; the pseudobulk reference from WMBv1 is total RNA. This may shift the absolute correlation values but should preserve the differential δ structure that drives the method. Worth a small validation check before scaling.
- Gegenhuber 2022 RNA-seq is on BNSTp Esr1+ only — BNST CRF+ cells are not perfectly co-extensive with Esr1+. Treat as an Esr1+ proxy, not a CRF-specific assay.
