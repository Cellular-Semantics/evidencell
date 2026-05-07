# WMB Sexually Dimorphic Neuron Survey
**Taxonomy:** CCN20230722 (Whole Mouse Brain v1)
**Date:** 2026-04-24
**Method:** DB query on `male_female_ratio` field; thresholds >3.0 (male-biased) and <0.33 (female-biased) following map-cell-type orchestrator conventions.

### A note on the ratio scale

`male_female_ratio` is male cell count ÷ female cell count, so the scale is inherently asymmetric: female bias is compressed into 0–1 while male bias is unbounded. A ratio of 0.02 and a ratio of 50 represent the same degree of imbalance (~98% one sex) but look very different as numbers. The thresholds >3 and <0.33 are exact reciprocals, representing equal imbalance (3:1) in opposite directions. Throughout this report all ratios are expressed as **% of the dominant sex** (% male for male-biased, % female for female-biased), which is directly comparable across both directions. The raw ratio is retained in parentheses for cross-reference.

---

## Overview

Of 5,322 clusters with sex ratio data, **336 show strong sex bias** (6.3% of all clusters):

| Bias | Count |
|---|---|
| Male-biased (>75% male) | 202 |
| Female-biased (>75% female) | 134 |

Sex bias is strongly concentrated in the hypothalamus/extended amygdala (HY-EA-Glut-GABA neighbourhood), which accounts for 83 of the 202 male-biased clusters and 15 of the female-biased ones. Female bias is more broadly distributed, with the midbrain/hindbrain (MB-HB-Glut-Sero-Dopa and MB-HB-CB-GABA) contributing more female-biased clusters than male-biased.

| Neighbourhood | Total | Male-biased | Female-biased |
|---|---|---|---|
| HY-EA-Glut-GABA | 1006 | 83 | 15 |
| MB-HB-Glut-Sero-Dopa | 1430 | 27 | 60 |
| MB-HB-CB-GABA | 1040 | 21 | 45 |
| Pallium-Glut | 500 | 25 | 6 |
| Subpallium-GABA;HY-EA-Glut-GABA | 394 | 18 | 4 |
| TH-EPI-Glut | 148 | 19 | 1 |

---

## Top Male-Biased Clusters

### Extreme bias (≥91% male)

| Accession | Name | % male (ratio) | NT | Key markers |
|---|---|---|---|---|
| CS20230722_CLUS_1306 | 1306 MEA-BST Lhx6 Nfib Gaba_5 | 99% M (99.0) | GABA | Cyp19a1, Cplx3, Kcng1, Frem3; NP: Tac1, Pnoc, Cck |
| CS20230722_CLUS_1293 | 1293 MEA-BST Lhx6 Nfib Gaba_2 | 99% M (99.0) | GABA | Cyp19a1, Pappa, Isl1, Fmn1; NP: Cck, Cartpt, Pnoc, Tac1 |
| CS20230722_CLUS_1562 | 1562 BST-MPN Six3 Nrgn Gaba_6 | 97% M (32.3) | GABA | Sytl4, Cyp19a1, Six3, Gal; NP: Cartpt, Pnoc, Penk, Gal, Sst |
| CS20230722_CLUS_1685 | 1685 SBPV-PVa Six6 Satb2 Gaba_1 | 97% M (32.3) | GABA | Six6, Npr3, Tmem215 |
| CS20230722_CLUS_1881 | 1881 PVpo-VMPO-MPN Hmx2 Gaba_1 | 97% M (32.3) | GABA | Apoc3, Pvalb, Crabp1; NP: Gal, Cartpt |
| CS20230722_CLUS_2281 | 2281 ARH-PVp Tbx3 Glut_3 | 97% M (32.3) | Glut | 4933406B17Rik, Tac2; NP: Pdyn, Tac2, Gal |
| CS20230722_CLUS_1890 | 1890 PVpo-VMPO-MPN Hmx2 Gaba_2 | 95% M (19.0) | GABA | Apoc3, Thbs4, Cd36; NP: Gal, Nts, Penk, Pnoc |
| CS20230722_CLUS_4088 | 4088 PB Evx2 Glut_9 | 94% M (15.7) | Glut | Pth2, Pth2r; NP: Sst, Adcyap1 |
| CS20230722_CLUS_1304 | 1304 MEA-BST Lhx6 Nfib Gaba_5 | 93% M (13.3) | GABA | Adprhl1, Cartpt, Sox6; NP: Cartpt, Gal, Pnoc |
| CS20230722_CLUS_2247 | 2247 MPN-MPO-PVpo Hmx2 Glut_3 | 93% M (13.3) | Glut | Eomes, Apoc3; NP: Gal, Adcyap1, Cartpt |

### Notable male-biased clusters (82–91% male)

- **SCH Six6 Cdc14a Gaba** clusters (CS20230722_CLUS_1607, _1605): 85–83% M; AVP+/NMS+; suprachiasmatic nucleus. Likely the male-enriched AVP population in SCN classically linked to circadian and social behaviour.
- **RT-ZI Gnb3 Gaba** clusters (_1585–_1591): 84–89% M; Sst/Npy/Pnoc+; reticular thalamus/zona incerta — unexpected locus.
- **ZI Pax6 Gaba_7** (CS20230722_CLUS_1761): 82% M; zona incerta; Pnoc/Cartpt+.
- **DMH Hmx2 Gaba_3** (CS20230722_CLUS_1939): 82% M; Dopa; Gal/Penk+; Esr2+ — oestrogen receptor expression in a male-biased dopaminergic dorsomedial hypothalamic cluster is notable.
- **DG Glut_1** (CS20230722_CLUS_0502): 82% M; dentate gyrus; Grp/Cck+. Male-biased granule cell cluster — unexpected at T-type level.
- **L2/3 IT CTX Glut_4** (CS20230722_CLUS_0120): 89% M; cortex; Cck/Pdyn+.
- **TH Prkcd Grin2c Glut** family (_2651–_2667): 82–87% M; thalamic nuclei; Cck dominant.
- **AHN Onecut3 Gaba** clusters (_1699–_1708): 82–85% M; anterior hypothalamic nucleus; varied NP profiles.

---

## Top Female-Biased Clusters

### Extreme bias (≥91% female)

| Accession | Name | % female (ratio) | NT | Key markers |
|---|---|---|---|---|
| CS20230722_CLUS_1915 | 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 | 98% F (0.02) | Dopa | **Kiss1**, Slc18a2; NP: Cartpt, Gal, Pdyn, Penk |
| CS20230722_CLUS_4581 | 4581 SPVC Ccdc172 Glut_1 | 95% F (0.05) | Glut | Ccdc172, Slc38a11; NP: Cck, Sst, Nts, Adcyap1 |
| CS20230722_CLUS_4344 | 4344 PGRN-PARN-MDRN Hoxb5 Glut_2 | 94% F (0.06) | Glut | Spp1, Otp |
| CS20230722_CLUS_1895 | 1895 PVpo-VMPO-MPN Hmx2 Gaba_2 | 94% F (0.06) | GABA | Csta2, Mafa, Kcns3; NP: Nts, Pnoc, Penk |
| CS20230722_CLUS_1898 | 1898 PVpo-VMPO-MPN Hmx2 Gaba_2 | 94% F (0.06) | GABA | Brs3, Plekhg1, Cd24a; NP: Nts |
| CS20230722_CLUS_2290 | 2290 VMH Fezf1 Glut_1 | 93% F (0.08) | Glut | Sel1l2, Nts, Isl1; NP: Adcyap1, Tac1, Nts, Cartpt |
| CS20230722_CLUS_4246 | 4246 NTS Phox2b Glut_3 | 92% F (0.09) | Glut | Prok1, Arhgap28, Gal; NP: Gal, Adcyap1, Cartpt |
| CS20230722_CLUS_2251 | 2251 MPN-MPO-PVpo Hmx2 Glut_3 | 92% F (0.09) | Glut | Eomes, Radx, Foxp2; NP: Adcyap1, Cartpt, Gal |
| CS20230722_CLUS_2282 | 2282 ARH-PVp Tbx3 Glut_3 | 90% F (0.11) | Glut | Nr5a2, Tac2, Glra2; NP: Tac2, Pdyn |
| CS20230722_CLUS_1301 | 1301 MEA-BST Lhx6 Nfib Gaba_4 | 91% F (0.10) | GABA | Prdm13, F5, Lhx6; NP: Gal, Pdyn, Pnoc, Trh |

### Notable female-biased clusters (80–91% female)

- **VMH Fezf1 Glut** clusters (_2290, _2292): 93–89% F; Tac1/Adcyap1/Nts/Cartpt+; ventromedial hypothalamus.
- **ARH-PVp Tbx3 Glut_3** (_2282): 90% F; Tac2/Pdyn+; arcuate nucleus. Compare with _2281 (97% M, same supertype — striking intra-supertype dimorphism).
- **CA1-ProS Glut_4** (CS20230722_CLUS_0285): 84% F; Cck/Grp+; hippocampal pyramidal layer.
- **NTS Phox2b Glut** clusters (_4246, _4283, _4291): 92–85% F; nucleus of the solitary tract; Gal/Adcyap1/Cartpt/Tac1+.
- **MEA-BST Lhx6 Nfib Gaba_1** (CS20230722_CLUS_1286): 83% F; Cck/Cartpt/Pnoc+; Esr2+.
- **DTN-LDT-IPN Otp Pax3 Gaba_2** clusters (_4779–_4781): 89–84% F; Vip/Tac1/Chrna2+; dorsal tegmental/laterodorsal tegmentum.

---

## Biological interpretation and candidate clusters for investigation

### Tier 1 — Well-established sexually dimorphic nuclei, strong atlas signal

**1. Kiss1+ PVpo/MPN Dopa neurons** (CS20230722_CLUS_1915, 98% F)
The extreme female bias and Kiss1 expression place this squarely within the AVPV/PeN kisspeptin population — the critical sex-hormone-sensitive GnRH pulse/surge generator. The most strongly female-biased cluster in the atlas. **Priority 1 classical node target.**

**2. VMH Fezf1 Glut** female-biased clusters (_2290, _2292, 93–89% F)
VMHvl is a canonical sexually dimorphic nucleus controlling female sexual behaviour and aggression. Tac1/Adcyap1/Nts-expressing glutamatergic VMH neurons are consistent with published VMHvl female-specific types. **Priority 1.**

**3. Cyp19a1+ MEA-BST Lhx6 Nfib Gaba** clusters (_1293, _1306, 99% M)
Cyp19a1 (aromatase) expression in MEA/BST defines a known male-biased population involved in male-typical social and reproductive behaviour. Essentially male-only clusters. **Priority 1.**

**4. BST-MPN Six3 Nrgn Gaba with Cyp19a1** (_1562, 97% M)
Also Cyp19a1+; BST/medial preoptic nucleus. Likely part of the same aromatase-expressing male circuit; distinct Six3/Nrgn TF signature from the Lhx6/Nfib supertype above.

**5. ARH-PVp Tbx3 Glut_3 dimorphic pair** (_2281 at 97% M vs _2282 at 90% F)
Two clusters in the same supertype show opposite sex composition of nearly equal magnitude. Both Tac2+ (NKB); _2281 additionally expresses Gal, _2282 expresses Nr5a2. Likely the male/female NKB populations in arcuate nucleus. Strong candidate for a sex-segregated T-type model. **Priority 1.**

### Tier 2 — Strong signal, less canonical locus

**6. SCH Six6 Cdc14a Gaba AVP+** clusters (_1607, _1605, 85–83% M)
Male-enriched AVP neurons in suprachiasmatic nucleus. Classical literature supports male-biased AVP in SCN; Nms co-expression on _1607 links these to SCN identity.

**7. PVpo-VMPO-MPN Hmx2 Gaba_2** female cluster family (_1888, _1891, _1894, _1895, _1898, 94–85% F)
Multiple female-biased POA clusters with Nts/Gal/Pnoc dominance. The Hmx2 supertype contains both male-biased and female-biased clusters at this rank, suggesting fine-grained dimorphism within a single T-type lineage.

**8. NTS Phox2b Glut female clusters** (_4246 at 92% F; _4283, _4291 at 85–83% F)
Female-biased brainstem visceral sensory neurons. Sex differences in NTS are known in energy balance and cardiovascular regulation.

**9. DMH Hmx2 Gaba_3 dopaminergic Esr2+** (CS20230722_CLUS_1939, 82% M)
Male-biased dopaminergic dorsomedial hypothalamic cluster with ERβ expression — paradoxical oestrogen-sensitive male cell type.

**10. DG Glut_1 male-biased** (CS20230722_CLUS_0502, 82% M; Grp/Cck+)
Male-biased dentate gyrus granule cell cluster. Adult neurogenesis in DG is sexually regulated; a male-enriched T-type is unexpected and could reflect developmental or activity-dependent biases.

### Tier 3 — Surprising or under-studied loci

**11. PB Evx2 Glut_9** clusters (_4087, _4088, 90–94% M; Pth2/Pth2r, Sst/Adcyap1)
Strongly male-biased Pth2-expressing parabrachial neurons. Sex bias in PTH2/PB signalling is not well-documented.

**12. L5 ET CTX Glut male clusters** (_0366, _0373, 83–85% M; Cck/Adcyap1/Cartpt)
Male-biased layer 5 extratelencephalic projection neurons. Could link to known sex differences in corticospinal/corticobulbar projections.

**13. MEA Slc17a7 Glut** clusters (_0193, _0196, _0197, _0199, _0200; 81–91% M)
Multiple male-biased glutamatergic MEA clusters (Pallium-Glut neighbourhood; Cck+). Distinct from the canonical GABAergic Cyp19a1 clusters.

---

## Summary table of priority targets for classical node creation

| Priority | Classical type | Target accession(s) | Sex bias | Key biology |
|---|---|---|---|---|
| 1 | AVPV/PeN Kiss1 kisspeptin neuron | CS20230722_CLUS_1915 | 98% F | GnRH surge generator |
| 1 | VMHvl Tac1/Adcyap1 Glut | CS20230722_CLUS_2290, _2292 | 93–89% F | Female sex behaviour, aggression |
| 1 | MEA/BST Cyp19a1 Lhx6 GABA | CS20230722_CLUS_1293, _1306 | 99% M | Aromatase+ male social/repro circuit |
| 1 | ARH NKB dimorphic pair | CS20230722_CLUS_2281 (M) + _2282 (F) | 97% M / 90% F | Reproductive neuroendocrine axis |
| 2 | SCN AVP male | CS20230722_CLUS_1607 | 85% M | Circadian sex differences |
| 2 | POA Nts/Gal female (SDN-POA) | CS20230722_CLUS_1888–1898 family | 94–85% F | Sexual differentiation of POA |
| 2 | NTS Prok1/Gal female | CS20230722_CLUS_4246 | 92% F | Energy balance / visceral sensation |
| 2 | DMH Esr2 Dopa male | CS20230722_CLUS_1939 | 82% M | ERβ+ male HY dopamine neuron |
| 3 | DG Grp/Cck male | CS20230722_CLUS_0502 | 82% M | Sex-biased adult neurogenesis? |
| 3 | PB Pth2/Pth2r male | CS20230722_CLUS_4088 | 94% M | Nociception/stress sex differences |

---

## Supertype-level analysis

Supertypes where all (or nearly all) child clusters are strongly dimorphic represent T-type lineages that are genuinely sex-segregated at the transcriptomic level — stronger evidence than any single cluster.

### Supertypes where every cluster is strongly dimorphic

| Supertype | Name | Clusters | Male-biased | Female-biased | Range | Notes |
|---|---|---|---|---|---|---|
| CS20230722_SUPT_0556 | ARH-PVp Tbx3 Glut_3 | 2 | 1 | 1 | 97% M ↔ 90% F | Opposite-sex pair; NKB/KNDy arcuate |
| CS20230722_SUPT_0486 | PVpo-VMPO-MPN Hmx2 Gaba_5 | 5 | 2 | 2 (+1 neutral) | 98% F ↔ 91% M | Contains Kiss1+ cluster; full sex spectrum |
| CS20230722_SUPT_0660 | TH Prkcd Grin2c Glut_7 | 3 | 3 | 0 | 84–91% M | All male; Cck+; thalamic |
| CS20230722_SUPT_0673 | MG-POL-SGN Nts Glut_2 | 3 | 3 | 0 | 83–90% M | All male; Adcyap1/Cck/Nts/Grp+; auditory thalamus |
| CS20230722_SUPT_0672 | MG-POL-SGN Nts Glut_1 | 3 | 3 | 0 | 78–84% M | All male; Cck/Crh+; auditory thalamus |
| CS20230722_SUPT_1063 | PDTg-PCG Pax6 Gaba_3 | 2 | 0 | 2 | 86–80% F | All female; Sst+; pedunculotegmental |

### Supertypes with ≥75% dimorphic clusters (≥3 clusters)

| Supertype | Name | Dimorphic/Total | Bias | Notes |
|---|---|---|---|---|
| CS20230722_SUPT_0776 | CUN-PPN Evx2 Meis2 Glut_1 | 12/16 | 61–90% F | Cuneiform/PPN; Cck/Penk dominant; Lepr+ cluster |
| CS20230722_SUPT_0454 | SBPV-PVa Six6 Satb2 Gaba_2 | 5/6 | 74–89% M | Subparaventricular/anterior hypothalamic area |
| CS20230722_SUPT_0092 | L5 ET CTX Glut_3 | 4/5 | 75–85% M | Layer 5 extratelencephalic cortex; Cck/Adcyap1/Cartpt |
| CS20230722_SUPT_0457 | AHN Onecut3 Gaba_2 | 4/5 | 75–85% M | Anterior hypothalamic nucleus |

### Biological highlights

**ARH-PVp Tbx3 Glut_3 (SUPT_0556) — KNDy arcuate pair**
The two clusters have opposite sex compositions of nearly equal magnitude (97% M vs 90% F) yet share Tac2 (NKB) and Pdyn expression. The male cluster (CLUS_2281) additionally expresses Gal; the female cluster (CLUS_2282) expresses Nr5a2 (SF-1) and Glra2. This is a textbook example of sex-specific T-type segregation within a single transcriptomic lineage, corresponding to the male/female NKB arcuate populations with distinct downstream functions in the reproductive axis.

**PVpo-VMPO-MPN Hmx2 Gaba_5 (SUPT_0486) — full sex spectrum in one supertype**
This supertype contains the most strongly female-biased cluster in the atlas (CLUS_1915, Kiss1+, 98% F), two strongly male-biased clusters (CLUS_1913/1914, 91% M), and one roughly balanced cluster (CLUS_1912). The Kiss1+ female cluster co-expresses Slc18a2 (VMAT2), identifying it as the dopaminergic AVPV kisspeptin population. The entire supertype captures the sex-differential preoptic area architecture within a single Hmx2 T-type lineage.

**MG-POL-SGN Nts Glut_1 and _2 (SUPT_0672, 0673) — uniformly male-biased auditory thalamus**
Two complete supertypes in medial geniculate body / pulvinar / suprageniculate nucleus are uniformly male-biased across all six clusters (78–90% M). All clusters are neuropeptide-rich (Adcyap1, Cck, Nts, Grp, Cartpt, Crh). Sex differences in auditory processing and ultrasonic vocalisation perception are documented in mice, but transcriptomic correlates in auditory thalamus are poorly mapped. High-value targets for novel classical node work.

**CUN-PPN Evx2 Meis2 Glut_1 (SUPT_0776) — predominantly female-biased cuneiform/PPN**
12 of 16 clusters are female-biased (61–90% F), with the most biased approaching female-only. One cluster (CLUS_3320) expresses Lepr (leptin receptor), linking female-biased PPN glutamatergic neurons to energy balance regulation. Sex differences in PPN glutamatergic neurons are not well characterised classically — discovery-mode target.

**L5 ET CTX Glut_3 (SUPT_0092) — male-biased corticofugal neurons**
Four of five clusters are male-biased (75–85% M), with Cck/Adcyap1/Cartpt neuropeptide expression. Sex differences in corticospinal tract size are documented anatomically but the transcriptomic basis is unknown.

---

## Notes on atlas interpretation

- Ratios of exactly 99.0 are likely a ceiling value assigned where female cell count = 0 (true ratio undefined, not literally 99:1).
- The `male_female_ratio` scale is asymmetric: female bias is compressed into 0–1, male bias is 1–∞. All values in this report are expressed as % of the dominant sex for direct comparability.
- Sex ratio reflects cell recovery in the atlas dataset, not absolute cell number in the brain. Extreme values (>90% or >85% one sex) are most reliable; values near the 75% threshold warrant caution.
- The `male_female_ratio` field was present in the cluster YAML but was not ingested into the CCN20230722 DB until this session — the DB has now been rebuilt and the field is queryable via SQL.

---

## Recommended next steps

1. **Run `map-cell-type` in discovery mode** on the four Tier 1 targets (Kiss1 kisspeptin, VMHvl, Cyp19a1 MEA, ARH NKB pair) using `just find-candidates` with the rebuilt DB.
2. **Consider novel targets** from the supertype analysis: MG-POL-SGN Nts Glut supertypes (auditory thalamus, all male-biased) and CUN-PPN Evx2 Meis2 Glut_1 (PPN, predominantly female-biased) have no well-mapped classical correlates and could be high-value discovery targets.
3. **File a dev-request** to expose `male_female_ratio` in `find-candidates` output and to display as % dominant sex for interpretability.
4. **Survey existing literature** via `workflows/survey.md` scoped to the hypothalamic nuclei above before creating classical nodes — ASTA corpus likely has strong coverage of SDN-POA, AVPV, and VMH.
5. Package the DB sex-ratio query as a reusable skill (`query-taxonomy-db` with field, threshold, and neighbourhood parameters).
