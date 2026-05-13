# PVN corticotropin-releasing factor receptor 1 (CRFR1) neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

PVN corticotropin-releasing factor receptor 1 (CRFR1) neurons are a population of
paraventricular hypothalamic neurons defined by expression of the CRFR1 receptor
together with the gonadal hormone receptors Esr1 and Ar [1]. The population shows
a male-biased sexual dimorphism (males > females) that emerges during puberty or
early adulthood and depends on circulating gonadal hormones in males [1]. Because
CRFR1 marks neurons that *receive* corticotropin-releasing factor input within
the PVN, mapping this classical type to a WMBv1 atlas cluster matters for linking
HPA-axis stress circuitry to transcriptomic identity.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | [1] |
| Defining markers | Crhr1, Esr1, Ar (all transcript/protein co-expression) | [1] |
| Sex bias | Male-biased (males > females); emerges at puberty; gonadectomy reduces CRFR1+ cells in males only | [1] |
| Cell Ontology | corticotropin-releasing neuron (CL:4072021) — RELATED only | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Rosinger 2019 (CRFR1 reporter mouse line; immunohistochemistry) · adult mouse PVN · [1]
- **Defining markers (Crhr1, Esr1, Ar):** Rosinger 2019 (CRFR1 reporter line; co-expression assessed by immunohistochemistry against ERα and androgen receptor) · [1]
  > Sex differences in neural structures are generally believed to underlie sex differences reported in anxiety, depression, and the hypothalamic-pituitary-adrenal axis, although the specific circuitry involved is largely unclear. Using a corticotropin-releasing factor receptor 1 (CRFR1) reporter mouse line, we report a sexually dimorphic distribution of CRFR1 expressing cells within the paraventricular hypothalamus (PVN; males > females). Relative to adult levels, PVN CRFR1-expressing cells are sparse and not sexually dimorphic at postnatal days 0, 4, or 21. This suggests that PVN cells might recruit CRFR1 during puberty or early adulthood in a sex-specific manner. The adult sex difference in PVN CRFR1 persists in old mice (20-24 months). Adult gonadectomy (6 weeks) resulted in a significant decrease in CRFR1-immunoreactive cells in the male but not female PVN. CRFR1 cells show moderate co-expression with estrogen receptor alpha (ERα) and high co-expression with androgen receptor, indicating potential mechanisms through which circulating gonadal hormones might regulate CRFR1 expression and function. Finally, we demonstrate that a psychological stressor, restraint stress, induces a sexually dimorphic pattern of neural activation in PVN CRFR1 cells (males >females) as assessed by co-localization with the transcription/neural activation marker phosphorylated CREB. Given the known role of CRFR1 in regulating stress-associated behaviors and hormonal responses, this CRFR1 PVN sex difference might contribute to sex differences in these functions.
  > — Rosinger et al. 2019, Introduction · [1] <!-- quote_key: 143424909_2b990710 -->

</details>

### Cell Ontology mapping

**Cell Ontology mapping:** corticotropin-releasing neuron [[CL:4072021](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4072021)] (RELATED).

The RELATED-only mapping is interpreted in the Discussion section below.

---

## Results

One supertype candidate was assessed: 0585 PVH-SO-PVa Otp Glut_1
[CS20230722_SUPT_0585] is the primary mapping at MODERATE confidence with a
PARTIAL_OVERLAP relationship — PVN location, glutamatergic NT, and
steroid-receptor co-expression align, but the Crhr1 transcript mean across the
supertype is low, indicating CRFR1+ neurons form a subset.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | — | 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] | 183 | 🟡 MODERATE | PVN location CONSISTENT · Esr1/Ar APPROXIMATE · Crhr1 APPROXIMATE (low) | Best candidate |

Total: 1 edge (PARTIAL_OVERLAP).

### Property alignment — 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585]

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | MBA:38 (PVN) n=98 (primary location) | not assessed | CONSISTENT |
| NT type | not stated; PVN principal neurons predominantly glutamatergic | Glutamatergic (PVH-SO-PVa Otp Glut) | not assessed | CONSISTENT |
| Crhr1 expression | POSITIVE (transcript, primary defining marker) | precomputed mean_expression=0.84 | not assessed | APPROXIMATE |
| Esr1 expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=3.65 (DEFINING_SCOPED atlas marker) | not assessed | APPROXIMATE |
| Ar expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=4.95 | not assessed | APPROXIMATE |
| Sex ratio | Male-biased (males > females); not quantified per cluster in source [1] | not available | not assessed (MFR=2.7 reported for CLUS_2382, parent SUPT_0589 — alternative candidate) | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + MERFISH location | Atlas metadata | PARTIAL | PVN n=98; Esr1=3.65; Ar=4.95; Crh=2.5; Crhr1=0.84 | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

### 0585 PVH-SO-PVa Otp Glut_1 · 🟡 MODERATE

**Supporting evidence**

- 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] has Paraventricular hypothalamic nucleus [MBA:38] as primary soma location with n=98 MERFISH cells, matching the PVN soma location reported by Rosinger 2019 [1].
- Esr1 precomputed mean expression = 3.65 (annotated as a DEFINING_SCOPED atlas marker on SUPT_0585) and Ar precomputed mean expression = 4.95 align with the moderate ERα / high AR co-expression profile reported for PVN CRFR1 neurons [1].
- Crh precomputed mean expression = 2.5 on SUPT_0585 supports the supertype's identity as a PVN neuroendocrine population, consistent with CRFR1+ neurons receiving local CRH signalling within the PVN.
- Glutamatergic NT classification (PVH-SO-PVa Otp Glut) is consistent with the predominant fast-transmitter phenotype of PVN principal neurons *(note: NT type was not explicitly stated in Rosinger 2019; inferred from PVN principal-neuron neurochemistry)*.
- A rank-0 child cluster, CLUS_2382 (parent supertype SUPT_0589), shows male_female_ratio = 2.7 — consistent with the male-biased dimorphism reported by Rosinger 2019 [1]. This raises SUPT_0589 as an alternative or co-equal target (see Concerns).

**Marker evidence provenance**

- **Crhr1 (defining):** Protein-level evidence (CRFR1 reporter mouse line + anti-CRFR1 immunohistochemistry) from Rosinger 2019 [1]. The reporter line provides direct cell-type specificity — the marker IS the defining feature. ⚠ **Atlas annotation/expression note:** SUPT_0585 precomputed Crhr1 mean = 0.84 is low. Crhr1 is *not* annotated as DEFINING on SUPT_0585, so this is not a classical atlas-annotation discrepancy; it is interpreted as a subset-expression pattern (CRFR1+ neurons being a minority of SUPT_0585). Flagged in Concerns.
- **Esr1 (defining):** Co-localised with CRFR1 reporter signal by immunohistochemistry in Rosinger 2019 [1] ("moderate" co-expression). SUPT_0585 precomputed mean = 3.65, annotated DEFINING_SCOPED — supports the supertype-level signal.
- **Ar (defining):** Co-localised with CRFR1 reporter signal by immunohistochemistry in Rosinger 2019 [1] ("high" co-expression). SUPT_0585 precomputed mean = 4.95 — strong supertype-level signal.
- **Single-source caveat:** All three defining markers rest on the same primary publication (Rosinger 2019 [1]). A targeted cite-traverse for "CRFR1 Esr1 Ar paraventricular hypothalamus" or "Crhr1 reporter mouse hypothalamus sex difference" would strengthen marker provenance without new experiments.

**Concerns**

- **Crhr1 APPROXIMATE (low):** SUPT_0585 mean Crhr1 = 0.84 indicates the CRFR1+ subset is a minority of cells in this supertype. The PVN CRFR1 classical type is contained within but not coextensive with SUPT_0585 — hence the PARTIAL_OVERLAP relationship.
- **AMBIGUOUS_MAPPING caveat:** SUPT_0589 (parent of CLUS_2382, MFR=2.7) is an alternative mapping target worth curator assessment; the male-biased sex ratio on CLUS_2382 may better match the dimorphism phenotype than the location-driven choice of SUPT_0585.
- **SINGLE_DATASET caveat:** Full characterisation of pvn_crfr1_neuron rests on Rosinger 2019 [1] alone — confidence is capped at MODERATE pending secondary literature validation.
- **Esr1 / Ar APPROXIMATE rather than CONSISTENT:** classical reports describe protein-level co-expression as moderate/high; atlas precomputed values quantify transcript means but cannot directly confirm cell-level co-expression within the CRFR1+ subset.
- **Sex ratio NOT_ASSESSED at supertype level:** MFR is computed at rank 0 only; the supertype-level mapping cannot confirm the male bias directly.
- **NT type inference:** Rosinger 2019 [1] does not explicitly state glutamatergic identity; consistency is based on PVN principal-neuron neurochemistry *(note: interpretation beyond the cited facts)*.

**What would upgrade confidence**

- Cluster-level analysis (rank 0) under SUPT_0585 and SUPT_0589: identify the child cluster(s) with highest combined Crhr1 expression and male-biased MFR. Expected output: refined MappingEdge at CLUSTER level with quantitative Crhr1 cell-fraction.
- Secondary primary literature confirming CRFR1/Esr1/Ar co-expression in PVN neurons (target: ≥1 additional independent study). Expected output: additional LiteratureEvidence items on the edge, raising the confidence ceiling above MODERATE.
- Curator assessment of SUPT_0589 as alternative/co-equal target (resolves open question 2).
- Targeted cite-traverse for the defining marker set to strengthen marker provenance.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** pvn_crfr1_neuron is defined by co-expression of
the CRFR1 receptor (Crhr1) and the gonadal hormone receptors Esr1 and Ar in
neurons of the Paraventricular hypothalamic nucleus [MBA:38], with male-biased
sexual dimorphism emerging at puberty [1]. `definition_basis =
CLASSICAL_NEUROCHEMICAL` — the node rests on classical neurochemical /
receptor-expression evidence rather than transcriptomic clustering.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1
taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using
metadata-based scoring (region match, NT type, defining markers, sex bias when
applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the `property_comparisons`
schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on
the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH
spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. Authored-prose evidence narratives are validated
against their source `evidence_items[*].explanation` fields. The pre-write
hook rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the Discussion
section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:19+00:00 from
[kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_pvn_crfr1_neuron_to_cs20230722_supt_0585 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** PVN corticotropin-releasing factor receptor 1 (CRFR1) neuron → 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] at MODERATE confidence. Key support: atlas metadata showing PVN soma location (n=98 cells), glutamatergic NT, and steroid-receptor co-expression (Esr1=3.65, Ar=4.95). Key caveats: AMBIGUOUS_MAPPING (SUPT_0589 is a plausible alternative driven by a male-biased child cluster, CLUS_2382, MFR=2.7), and SINGLE_DATASET (the classical type rests on Rosinger 2019 [1] alone).

corticotropin-releasing neuron [[CL:4072021](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4072021)] is a related but non-identical Cell Ontology term. CL:4072021 defines neurons by CRH *secretion*, whereas the proposed PVN CRFR1 node is defined by CRFR1 *receptor* expression. These are distinct populations: CRFR1+ PVN neurons receive CRH input, they do not necessarily secrete CRH. Mapping is RELATED only. No CL term for CRFR1-receptor-expressing neurons exists — potential CL contribution.

### Proposed experiments and follow-ups

- **What:** Rank-0 cluster sweep under SUPT_0585 and SUPT_0589 with quantitative Crhr1 expression and male_female_ratio extracted per child cluster.
  - **Target:** Identify clusters with Crhr1 mean ≥ supertype mean AND MFR ≥ 1.5.
  - **Expected output:** Refined MappingEdge(s) at CLUSTER level, replacing the current SUPERTYPE-level edge or adding co-equal cluster-level mappings.
  - **Resolves:** Open questions 1 and 2.
- **What:** Targeted cite-traverse for secondary primary literature on CRFR1/Esr1/Ar PVN co-expression and dimorphism.
  - **Target:** ≥1 independent primary study confirming the co-expression profile.
  - **Expected output:** Additional LiteratureEvidence items on pvn_crfr1_neuron, raising the confidence ceiling above MODERATE.
  - **Resolves:** SINGLE_DATASET caveat.
- **What:** New CL term request for a receptor-defined sibling of CL:4072021 (e.g. "CRFR1-receptor-expressing PVN neuron").
  - **Target:** EXACT mapping at the receptor-defined cell-type level.
  - **Expected output:** CL ontology contribution; subsequent revision of `cl_mapping` to EXACT.
  - **Resolves:** RELATED-only CL mapping.

### Open questions

1. Which cluster within the PVH-SO-PVa Otp Glut subclass shows highest Crhr1 expression combined with male-biased sex ratio?
2. Is SUPT_0589 a better or co-equal mapping target compared to SUPT_0585?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rosinger et al. 2019 | [31055007](https://pubmed.ncbi.nlm.nih.gov/31055007/) | soma location; defining markers (Crhr1, Esr1, Ar); sexual dimorphism; gonadectomy effect |
