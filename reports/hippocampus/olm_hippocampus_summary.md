# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*2026-03-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_OLM.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum oriens [UBERON:0005371]; stratum lacunosum-moleculare [UBERON:0007640] | [1] [2] [1] [3] |
| NT | GABAergic | [4] [5] |
| Markers | Sst+, Chrna2+, mGluR1+ | [6] [7] [2] [8] |
| Negative | PV−, CB−, CR−, NOS−, VIP− | |
| Neuropeptides | Sst, Npy, Pnoc | [7] [9] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0769 Sst Gaba_3 [CS20230722_CLUS_0769] | 0216 Sst Gaba_3 | 454 | 🟡 MODERATE | Best candidate |
| 2 | 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] | 0203 Lamp5 Lhx6 Gaba_1 | 125 | 🔴 LOW | Speculative |
| — | 0785 Sst Gaba_6 [CS20230722_CLUS_0785] | 0219 Sst Gaba_6 | 210 | ⛔ REFUTED | Eliminated (Chrna2) |
| — | 0788 Sst Gaba_6 [CS20230722_CLUS_0788] | 0219 Sst Gaba_6 | 73 | ⛔ REFUTED | Eliminated (Chrna2) |
| — | 0789 Sst Gaba_6 [CS20230722_CLUS_0789] | 0219 Sst Gaba_6 | 262 | ⛔ REFUTED | Eliminated (Chrna2) |

All edges: `skos:broadMatch`

---

## 0769 Sst Gaba_3 · 🟡 MODERATE

*`CS20230722_CLUS_0769` · 454 cells (10x) · supertype: 0216 Sst Gaba_3*

**Supporting evidence:**

- Best CA1 signal. Sst subclass consistent. CA1 SO (87 cells) — primary OLM location. Full neuropeptide triad: Sst, Npy, Pnoc. No SLM. Significant prosubiculum (61) and posterior amygdala (95) distribution. [Atlas metadata]
- MapMyCells annotation transfer of the pooled OLM cohort (46 cells; Sst-OLM + Htr3a-OLM combined; GSE124847, Winterer 2019) strongly supports the parent Sst Gaba_3 supertype (43/45 classified cells; pooled F1=0.97; pooled CLASS/SUBCLASS F1=0.99) but OLM cells scatter across sibling clusters 0767–0774 within it. Cluster 0769 specifically received 0/46 cells — OLM cells preferentially map to cluster 0768 (22/45, best pooled cluster-level F1=0.65). This indicates OLM identity is captured at the Sst Gaba_3 supertype rather than at any single child cluster. The high pooled supertype F1 reflects removal of the inter-source mis-attribution penalty that depresses per-source F1; both Sst-OLM and Htr3a-OLM converge on the same Sst Gaba_3 supertype. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=stratum oriens (UBERON:0005371); SLM (UBERON:0007640) / B=CA1 SO (MBA:399, 87 cells); prosubiculum; posterior amygdala. CA1 SO matches — strongest CA1 signal. SLM absent. Extra-hippocampal spread.
- **marker_Chrna2** (APPROXIMATE): A=Chrna2 — defining marker / B=Chrna2 expressed (scattered) in Sst Gaba_3 supertype per ABC Atlas. ABC Atlas filter (HPF/GABA/Chrna2) retains Sst Gaba_3 but eliminates Sst Gaba_6. Expression scattered across clusters of this supertype — not a defining marker at cluster level, but present. https://tinyurl.com/a4f3kd4v

- mGluR1 (Grm1) not resolvable from atlas metadata.
- Prosubiculum (61 cells) and posterior amygdala (95 cells) — cluster may include non-OLM Sst interneurons from adjacent regions.
- Annotation transfer maps OLM cells to Sst Gaba_3 supertype but to sibling clusters (primarily 0768), not 0769. May indicate the mapping is more appropriate at supertype than cluster level.

**What would upgrade confidence:**

- *Unresolved:* Are the CA1 SO cells OLM-morphology? What are the amygdala cells?
- *Unresolved:* Why do OLM cells map to cluster 0768 rather than 0769? Do these clusters differ in hippocampal enrichment?
- *Unresolved:* Why do OLM cells preferentially map to CS20230722_CLUS_0768 rather than CS20230722_CLUS_0769 within Sst Gaba_3?
- *Unresolved:* Why do OLM cells map preferentially to CS20230722_CLUS_0768 rather than CS20230722_CLUS_0769 within CS20230722_SUPT_0216?
- *Proposed:* Chrna2-Cre + MapMyCells for CA1 stratum oriens neurons.
- *Proposed:* Targeted scRNA-seq or MERFISH of Chrna2+ stratum oriens neurons.

---

## 0727 Lamp5 Lhx6 Gaba_1 · 🔴 LOW

*`CS20230722_CLUS_0727` · 125 cells (10x) · supertype: 0203 Lamp5 Lhx6 Gaba_1*

**Supporting evidence:**

- Partial property overlap. GABA consistent. CA3 SO + SLM match OLM anatomy. Sst and Pnoc neuropeptides present but Npy absent. Subclass is Lamp5 Lhx6, NOT Sst — discordant with canonical OLM identity. Chrna2/Grm1 not assessable. [Atlas metadata]

**Concerns:**

- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Lamp5 Lhx6 subclass. All 45 successfully classified cells mapped to Sst Gaba subclass (Sst Gaba_3 supertype). Zero support for this Lamp5 Lhx6 cluster as an OLM target. [Annotation transfer]
- **location** (APPROXIMATE): A=stratum oriens (UBERON:0005371); SLM (UBERON:0007640) / B=CA3 SO (MBA:486); CA3 SLM (MBA:471). SO and SLM present. CA3-enriched, not CA1.
- **marker_Sst** (APPROXIMATE): A=Sst — defining marker / B=Sst in neuropeptides, NOT defining_markers; Lamp5 Lhx6 subclass. Sst expressed but not defining. Subclass is Lamp5 Lhx6, not Sst.
- **neuropeptide_Npy** (DISCORDANT): A=Npy / B=absent. OLM expresses Npy; this cluster does not.
- Lamp5 Lhx6 subclass (CGE-derived), not Sst (MGE-derived). Biologically surprising for canonical Sst+ MGE-derived OLM. Requires independent validation.
- Chrna2 and mGluR1 not resolvable from atlas metadata.

**What would upgrade confidence:**

- *Unresolved:* Is Sst expression in this Lamp5 Lhx6 cluster biologically meaningful? OLM morphology/ephys present?
- *Unresolved:* Do any OLM-morphology cells fall into CS20230722_CLUS_0727 despite the Lamp5 Lhx6 subclass mismatch?
- *Unresolved:* Do any OLM-morphology cells fall into CS20230722_CLUS_0727 despite the Lamp5 Lhx6 (CGE) vs Sst (MGE) lineage mismatch?
- *Proposed:* Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens.
- *Proposed:* Chrna2-Cre + MapMyCells to test Chrna2+ neuron mapping.

---

## Eliminated candidates

**Primary reason:** Shared disqualifying signal: Chrna2 is DISCORDANT across all UNCERTAIN edges.

**0785 Sst Gaba_6** (210 cells)
- Filtering the ABC Atlas on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the Sst Gaba_6 supertype entirely. Chrna2 is a defining marker of OLM interneurons; its absence from this supertype argues against any cluster within it being OLM. [A]
- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Sst Gaba_6 supertype. All 45 successfully classified cells mapped to Sst Gaba_3 supertype instead. Zero support for this Sst Gaba_6 cluster as an OLM target.
- marker_Chrna2: ABC Atlas filter (HPF/GABA/Chrna2) eliminates Sst Gaba_6. https://tinyurl.com/a4f3kd4v

- neuropeptide_Pnoc: OLM expresses Pnoc; absent from this cluster.

**0788 Sst Gaba_6** (73 cells)
- Filtering the ABC Atlas on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the Sst Gaba_6 supertype entirely. Chrna2 is a defining marker of OLM interneurons; its absence from this supertype argues against any cluster within it being OLM. [A]
- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Sst Gaba_6 supertype. All 45 successfully classified cells mapped to Sst Gaba_3 supertype instead. Zero support for this Sst Gaba_6 cluster as an OLM target.
- marker_Chrna2: ABC Atlas filtering on Chrna2 expression eliminates Sst Gaba_6 entirely. https://tinyurl.com/a4f3kd4v


**0789 Sst Gaba_6** (262 cells)
- Filtering the ABC Atlas on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the Sst Gaba_6 supertype entirely. Chrna2 is a defining marker of OLM interneurons; its absence from this supertype argues against any cluster within it being OLM. [A]
- MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Sst Gaba_6 supertype. All 45 successfully classified cells mapped to Sst Gaba_3 supertype instead. Zero support for this Sst Gaba_6 cluster as an OLM target.
- marker_Chrna2: ABC Atlas filtering on Chrna2 expression eliminates Sst Gaba_6 entirely. https://tinyurl.com/a4f3kd4v


---

## Proposed experiments

### 1 — Patch-seq

- Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens.
- Patch-seq of Sst+ CA1/CA3 stratum oriens neurons.
*Resolves: edge_olm_to_wmb_clus_0727, edge_olm_to_wmb_clus_0788*

### 2 — MapMyCells / annotation transfer

- Chrna2-Cre + MapMyCells to test Chrna2+ neuron mapping.
- Chrna2-Cre + MapMyCells for CA1 stratum oriens neurons.
- Chrna2-Cre + MapMyCells.
*Resolves: edge_olm_to_wmb_clus_0727, edge_olm_to_wmb_clus_0769, edge_olm_to_wmb_clus_0788, edge_olm_to_wmb_clus_0789*

### 3 — MERFISH / spatial transcriptomics

- Targeted scRNA-seq or MERFISH of Chrna2+ stratum oriens neurons.
*Resolves: edge_olm_to_wmb_clus_0769*

### 4 — Other

- Region-specific dissection of CA3 SO vs amygdala cells in this cluster.
*Resolves: edge_olm_to_wmb_clus_0789*

---

## Open questions

1. Are the CA1 SO cells OLM-morphology? What are the amygdala cells?
2. Why do OLM cells map to cluster 0768 rather than 0769? Do these clusters differ in hippocampal enrichment?
3. Why do OLM cells preferentially map to CS20230722_CLUS_0768 rather than CS20230722_CLUS_0769 within Sst Gaba_3?
4. Why do OLM cells map preferentially to CS20230722_CLUS_0768 rather than CS20230722_CLUS_0769 within CS20230722_SUPT_0216?
5. Is Sst expression in this Lamp5 Lhx6 cluster biologically meaningful? OLM morphology/ephys present?
6. Do any OLM-morphology cells fall into CS20230722_CLUS_0727 despite the Lamp5 Lhx6 subclass mismatch?
7. Do any OLM-morphology cells fall into CS20230722_CLUS_0727 despite the Lamp5 Lhx6 (CGE) vs Sst (MGE) lineage mismatch?
8. Given Chrna2 absence, is this cluster a non-OLM Sst stratum oriens type?
9. Given Chrna2 absence at Sst Gaba_6, is CS20230722_CLUS_0785 a non-OLM Sst stratum oriens type?
10. Are SO cells OLM-morphology? What are corpus callosum cells?
11. Are the CA1 SO and CA3 SO cells in CS20230722_CLUS_0788 OLM-morphology, and what are the corpus callosum cells in the same cluster?
12. Are CA3 SO cells OLM? What is the amygdala population?
13. What is the amygdala population dominating CS20230722_CLUS_0789?
14. What is the identity of the amygdala population dominating CS20230722_CLUS_0789?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_olm_to_wmb_clus_0769 | Atlas metadata | SUPPORT |
| edge_olm_to_wmb_clus_0769 | Annotation transfer | PARTIAL |
| edge_olm_to_wmb_clus_0727 | Atlas metadata | PARTIAL |
| edge_olm_to_wmb_clus_0727 | Annotation transfer | REFUTE |
| edge_olm_to_wmb_clus_0785 | Atlas metadata | PARTIAL |
| edge_olm_to_wmb_clus_0785 | Atlas query [A] | REFUTE |
| edge_olm_to_wmb_clus_0785 | Annotation transfer | REFUTE |
| edge_olm_to_wmb_clus_0788 | Atlas metadata | PARTIAL |
| edge_olm_to_wmb_clus_0788 | Atlas query [A] | REFUTE |
| edge_olm_to_wmb_clus_0788 | Annotation transfer | REFUTE |
| edge_olm_to_wmb_clus_0789 | Atlas metadata | PARTIAL |
| edge_olm_to_wmb_clus_0789 | Atlas query [A] | REFUTE |
| edge_olm_to_wmb_clus_0789 | Annotation transfer | REFUTE |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 · PMID:20421280 | [20421280](https://pubmed.ncbi.nlm.nih.gov/20421280/) | soma location |
| [2] | Nichol et al. 2018 · PMID:29487503 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/) | soma location |
| [3] | Tecuatl et al. 2020 · PMID:33361464 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/) | soma location |
| [4] | Böhm et al. 2015 · PMID:26021702 | [26021702](https://pubmed.ncbi.nlm.nih.gov/26021702/) | neurotransmitter type |
| [5] | Oliva et al. 2000 · PMID:10777798 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | neurotransmitter type |
| [6] | Hooft et al. 2000 · PMID:10804195 | [10804195](https://pubmed.ncbi.nlm.nih.gov/10804195/) | Sst marker |
| [7] | Winterer et al. 2019 · PMID:31420995 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) | Sst marker |
| [8] | Leão et al. 2012 · PMID:23042082 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/) | Chrna2 marker |
| [9] | Thulin et al. 2025 · PMID:40757734 | [40757734](https://pubmed.ncbi.nlm.nih.gov/40757734/) | Pnoc neuropeptide |
| [A] | ABC Atlas | — | anatomy=HPF; NT=GABA; expression=Chrna2 · [view](https://tinyurl.com/a4f3kd4v) |

<!-- verdict-block-start: edge_olm_to_wmb_clus_0769 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  rationale: >
    Primary mapping to CS20230722_CLUS_0769 within CS20230722_SUPT_0216 (Sst Gaba_3)
    is anchored by atlas metadata (CA1 SO presence, full Sst/Npy/Pnoc neuropeptide
    triad, Sst subclass) and by MapMyCells annotation transfer of Winterer 2019 OLM
    cells (run_ref at_run_20260408_winterer_olm_mmc_wmbv1, scRNA-seq with MERFISH
    spatial registration on the target side) reaching pooled F1=0.99 at
    CLASS/SUBCLASS, pooled F1=0.97 at the SUPERTYPE level (CS20230722_SUPT_0216),
    and pooled F1=0.65 at the best child cluster CS20230722_CLUS_0768; cluster
    Grm1 mean_expression=8.29 is qualitatively concordant with mGluR1 being a
    defining OLM marker by electrophysiology and scRNA-seq. 4 of 6 markers
    CONSISTENT (Sst, Sst-NP, Npy-NP, Pnoc-NP) with Chrna2 APPROXIMATE and
    mGluR1 NOT_ASSESSED at the atlas defining-markers panel.
  unresolved_questions:
    - "Why do OLM cells map preferentially to CS20230722_CLUS_0768 rather than CS20230722_CLUS_0769 within CS20230722_SUPT_0216?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0727 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    CS20230722_CLUS_0727 (Lamp5 Lhx6 Gaba_1) is refuted as an OLM target by
    MapMyCells annotation transfer (run_ref at_run_20260408_winterer_olm_mmc_wmbv1,
    scRNA-seq): 0/46 OLM cells map to the Lamp5 Lhx6 subclass and all 45 classified
    cells map instead to CS20230722_SUPT_0216 (Sst Gaba_3). Npy is DISCORDANT,
    Sst is APPROXIMATE only (in neuropeptide annotations, not defining_markers),
    cluster Grm1 mean_expression=5.85 is the lowest among candidates, and Chrna2
    is absent. 2 of 6 markers CONSISTENT (Sst-NP, Pnoc-NP) against a Lamp5 Lhx6
    (CGE-derived) vs Sst (MGE-derived) subclass and developmental-lineage
    mismatch; CA3 SO + SLM anatomy (morphology-relevant) is suggestive but not
    sufficient.
  unresolved_questions:
    - "Do any OLM-morphology cells fall into CS20230722_CLUS_0727 despite the Lamp5 Lhx6 (CGE) vs Sst (MGE) lineage mismatch?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0785 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    CS20230722_CLUS_0785 (Sst Gaba_6) is refuted by two independent signals:
    (1) ABC Atlas filter (HPF + GABA + Chrna2 expression, scRNA-seq) eliminates
    the entire Sst Gaba_6 supertype, and (2) MapMyCells annotation transfer
    (run_ref at_run_20260408_winterer_olm_mmc_wmbv1, scRNA-seq) maps 0/46 OLM
    cells to Sst Gaba_6, with all 45 classified cells going to
    CS20230722_SUPT_0216 instead. Chrna2 DISCORDANT and Pnoc DISCORDANT; 3 of 6
    markers CONSISTENT (Sst, Sst-NP, Npy-NP) but the Chrna2 elimination is
    decisive. CA3-enriched anatomy further weakens the candidate. Cluster Grm1
    mean_expression=10.30 does not rescue the Chrna2 elimination.
  unresolved_questions:
    - "Given Chrna2 absence at Sst Gaba_6, is CS20230722_CLUS_0785 a non-OLM Sst stratum oriens type?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0788 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    CS20230722_CLUS_0788 (Sst Gaba_6) is refuted by ABC Atlas filter
    (HPF + GABA + Chrna2 expression, scRNA-seq) eliminating the Sst Gaba_6
    supertype and by MapMyCells annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1, scRNA-seq; 0/46 OLM cells to
    Sst Gaba_6). Chrna2 DISCORDANT; 4 of 6 markers CONSISTENT (Sst, Sst-NP,
    Npy-NP, Pnoc-NP) but the Chrna2 elimination is
    decisive. Cluster is small (50 cells total) with CA1 SO (8) plus CA3 SO (13)
    and no SLM; cluster Grm1 mean_expression=9.08 does not rescue the Chrna2
    elimination.
  unresolved_questions:
    - "Are the CA1 SO and CA3 SO cells in CS20230722_CLUS_0788 OLM-morphology, and what are the corpus callosum cells in the same cluster?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0789 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    CS20230722_CLUS_0789 (Sst Gaba_6) is refuted by ABC Atlas filter
    (HPF + GABA + Chrna2 expression, scRNA-seq) eliminating the Sst Gaba_6
    supertype and by MapMyCells annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1, scRNA-seq; 0/46 OLM cells to
    Sst Gaba_6). Chrna2 DISCORDANT; cluster is amygdala-dominated (28% amygdala
    cells; CA3 SO 25; no CA1; no SLM). 4 of 6 markers CONSISTENT (Sst, Sst-NP,
    Npy-NP, Pnoc-NP) but Chrna2 elimination plus extra-hippocampal
    (morphology/region) location are decisive. Cluster Grm1 mean_expression=8.00
    does not rescue.
  unresolved_questions:
    - "What is the identity of the amygdala population dominating CS20230722_CLUS_0789?"
```
<!-- verdict-block-end -->
