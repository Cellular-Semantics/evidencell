# PVN corticotropin-releasing factor receptor 1 (CRFR1) neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | [1] |
| NT | Not stated; PVN principal neurons are predominantly glutamatergic *(note: inferred from regional convention, not stated explicitly in source)* | — |
| Defining markers | *Crhr1*, *Esr1*, *Ar* | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | corticotropin-releasing neuron (CL:4072021) — RELATED only | — |

**Notes.** The defining feature of this cell type is expression of corticotropin-releasing factor receptor 1 (*Crhr1*), not CRH secretion. CL:4072021 (corticotropin-releasing neuron) is therefore only a related term; no exact CL term currently exists — this node is a candidate for a new term request. The population shows male-biased sexual dimorphism (males > females), which emerges during puberty or early adulthood and persists into old age. Co-expression of estrogen receptor alpha (*Esr1*, moderate) and androgen receptor (*Ar*, high) implicates gonadal hormone-dependent regulation of CRFR1 expression. The full characterisation rests on a single primary source (Rosinger 2019) [1].

---

## Source evidence

> "Sex differences in neural structures are generally believed to underlie sex differences reported in anxiety, depression, and the hypothalamic-pituitary-adrenal axis, although the specific circuitry involved is largely unclear. Using a corticotropin-releasing factor receptor 1 (CRFR1) reporter mouse line, we report a sexually dimorphic distribution of CRFR1 expressing cells within the paraventricular hypothalamus (PVN; males > females). Relative to adult levels, PVN CRFR1-expressing cells are sparse and not sexually dimorphic at postnatal days 0, 4, or 21. This suggests that PVN cells might recruit CRFR1 during puberty or early adulthood in a sex-specific manner. The adult sex difference in PVN CRFR1 persists in old mice (20–24 months). Adult gonadectomy (6 weeks) resulted in a significant decrease in CRFR1-immunoreactive cells in the male but not female PVN. CRFR1 cells show moderate co-expression with estrogen receptor alpha (ERα) and high co-expression with androgen receptor, indicating potential mechanisms through which circulating gonadal hormones might regulate CRFR1 expression and function. Finally, we demonstrate that a psychological stressor, restraint stress, induces a sexually dimorphic pattern of neural activation in PVN CRFR1 cells (males > females) as assessed by co-localization with the transcription/neural activation marker phosphorylated CREB. Given the known role of CRFR1 in regulating stress-associated behaviors and hormonal responses, this CRFR1 PVN sex difference might contribute to sex differences in these functions."
> — Z et al. 2019, Introduction · [1] <!-- quote_key: 143424909_2b990710 -->

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype name | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_SUPT_0585 | 0585 PVH-SO-PVa Otp Glut_1 | — | 🟡 MODERATE | Location MBA:38 ✓; Glutamatergic ✓; *Esr1*=3.65 ✓; *Ar*=4.95 ✓; *Crhr1*=0.84 (low — subset only) | Best candidate |

---

## CS20230722_SUPT_0585 — 0585 PVH-SO-PVa Otp Glut_1

**Confidence: 🟡 MODERATE**

### Supporting evidence

SUPT_0585 is the highest-ranked candidate (DB score = 3) for pvn_crfr1_neuron. It maps to Paraventricular hypothalamic nucleus [MBA:38] as its primary anatomical location (n = 98 cells), directly matching the soma location of the classical type. The cluster name encodes its glutamatergic identity (PVH-SO-PVa Otp Glut), consistent with the expected neurotransmitter phenotype of PVN principal neurons.

Steroid hormone receptor markers align well: *Esr1* has a precomputed mean expression of 3.65 (flagged as a DEFINING_SCOPED atlas marker for this supertype), and *Ar* has a mean expression of 4.95 — both consistent with the co-expression of estrogen receptor alpha and androgen receptor reported in the primary source [1]. Presence of *Crh* (mean = 2.5) confirms a PVN neuroendocrine identity.

Sexual dimorphism biology is further supported by a rank-0 leaf cluster, CLUS_2382 *(note: this cluster's parent supertype is SUPT_0589, not SUPT_0585)*, which has a male_female_ratio of 2.7, consistent with the male-biased dimorphism of pvn_crfr1_neuron.

### Marker evidence provenance

All marker values are from WMBv1 precomputed expression statistics (atlas metadata); no independent literature confirmation of these expression levels is available for this specific supertype. The single primary source for pvn_crfr1_neuron (Rosinger 2019) [1] characterises CRFR1 cells by immunohistochemistry and reporter imaging, not by transcriptomic profiling.

### Concerns

1. **Low *Crhr1* expression.** *Crhr1* mean expression across SUPT_0585 is only 0.84, indicating that CRFR1-expressing neurons constitute a minority subset of this supertype, not the bulk population. The mapping is therefore at supertype level a partial overlap.
2. **Alternative target.** SUPT_0589 is the parent supertype of CLUS_2382, the male-biased leaf cluster (male_female_ratio = 2.7). It is unclear whether SUPT_0589 is a better primary mapping target than SUPT_0585, or whether both overlap with the classical type.
3. **Single-source classical type.** The entire characterisation of pvn_crfr1_neuron rests on one paper (Rosinger 2019, PMID:31055007). Confidence is capped at MODERATE until secondary literature is identified.

### What would upgrade confidence

- Identification of the specific rank-0 cluster(s) within the PVH-SO-PVa Otp Glut subclass that show the highest *Crhr1* expression combined with a male-biased sex ratio. If such a cluster exists and co-expresses *Esr1* and *Ar* at levels consistent with the classical type, confidence could be raised to HIGH.
- A second independent source characterising PVN CRFR1 neurons transcriptomically or with additional immunohistochemical markers.
- Resolution of the SUPT_0585 vs SUPT_0589 question by curator assessment of per-cluster expression profiles.

---

## Proposed experiments

No formal proposed experiments are recorded in the current evidence file. The following are suggested on the basis of the open questions:

| Method | What | Target | Expected output | Resolves |
|---|---|---|---|---|
| Taxonomy DB query | Query WMBv1 clusters within PVH-SO-PVa Otp Glut subclass ranked by *Crhr1* expression × sex ratio | SUPT_0585 / SUPT_0589 children | Ranked cluster list with expression and ratio values | Which rank-0 cluster best captures pvn_crfr1_neuron |
| Curator comparison | Compare SUPT_0585 vs SUPT_0589 property profiles and sex-ratio statistics | SUPT_0585, SUPT_0589 | Recommendation for primary mapping target | SUPT_0589 as alternative/co-equal target |

---

## Open questions

1. Which cluster within the PVH-SO-PVa Otp Glut subclass shows the highest *Crhr1* expression combined with a male-biased sex ratio?
2. Is SUPT_0589 a better or co-equal mapping target compared to SUPT_0585?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_pvn_crfr1_neuron_to_cs20230722_supt_0585 | ATLAS_METADATA | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Z et al. 2019 | PMID:31055007 | Soma location, defining markers (*Crhr1*, *Esr1*, *Ar*), sexual dimorphism characterisation |
