# VMHvl estrogen-receptor alpha / progesterone receptor neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Ventromedial hypothalamic nucleus [MBA:693] *(ventrolateral subdivision, VMHvl)* | [1] |
| Neurotransmitter | Not stated; VMHvl neurons are predominantly glutamatergic *(note: inferred from atlas label; no NT source cited for this classical node)* | — |
| Defining markers | *Esr1*, *Pgr*, *Nkx2-1*, *Tac1* | [1], [2] |
| Negative markers | None reported | — |
| Neuropeptides | Tac1 (substance P precursor) | [1] |

**Heterogeneity note.** This classical node is acknowledged to be molecularly heterogeneous. At least three functional subpopulations have been described within the broader ERα/PR VMHvl population: (i) *Pgr*+ neurons required for mating in both sexes and fighting in males; (ii) ERα/*Nkx2-1*/*Tac1*+ neurons driving estrogen-dependent female locomotion; and (iii) additional ERα-expressing subtypes with distinct projections and sex-related functions. Seventeen transcriptomic types have been identified by snRNA-seq (Kim 2019). This node may need to be split into multiple sub-nodes in future iterations. No CL term exists; the node is a candidate for new CL term(s).

> "Estrogen-receptor alpha (ERα) neurons in the ventrolateral region of the ventromedial hypothalamus (VMHVL) control an array of sex-specific responses to maximize reproductive success. In females, these VMHVL neurons are believed to coordinate metabolism and reproduction. However, it remains unknown whether specific neuronal populations control distinct components of this physiological repertoire. Here, we identify a subset of ERα VMHVL neurons that promotes hormone-dependent female locomotion. Activating Nkx2-1-expressing VMHVL neurons via pharmacogenetics elicits a female-specific burst of spontaneous movement, which requires ERα and Tac1 signaling. Disrupting the development of Nkx2-1(+) VMHVL neurons results in female-specific obesity, inactivity, and loss of VMHVL neurons coexpressing ERα and Tac1. Unexpectedly, two responses controlled by ERα(+) neurons, fertility and brown adipose tissue thermogenesis, are unaffected. We conclude that a dedicated subset of VMHVL neurons marked by ERα, NKX2-1, and Tac1 regulates estrogen-dependent fluctuations in physical activity and constitutes one of several neuroendocrine modules that drive sex-specific responses."
> — S et al. 2015, Developmental and Hormonal Regulation · [1] <!-- quote_key: 27794167_af52b501 -->

> "Another molecularly defined sexually dimorphic VMHvl subpopulation that controls sex-typical behaviors in both sexes is the progesterone receptor (PR)-expressing neurons. This subpopulation is required for the normal display of mating in both sexes and for fighting in males."
> — N et al. 2021, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 233446934_8cb6b0bc -->

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0564 VMH Fezf1 Glut_2 [CS20230722_SUPT_0564] | SUPERTYPE | — | 🟡 MODERATE | MBA:693 dominant location; *Nkx2-1* strong; *Pgr* moderate; *Esr1*/*Tac1* subset-level | Best candidate |

---

## 0564 VMH Fezf1 Glut_2 — MODERATE

**CS20230722_SUPT_0564** is a WMBv1 supertype in the VMH Fezf1 glutamatergic lineage (n = 360 cells with MBA:693 as dominant location). It is the best available atlas match for the broader *vmhvl_esr1_pr_neuron* classical type.

### Supporting evidence

The property comparison is overall supportive but reflects the acknowledged heterogeneity of the classical node:

- **Anatomical location**: SUPT_0564 has the Ventromedial hypothalamic nucleus [MBA:693] as its primary location, directly consistent with the VMHvl soma location of the classical type. *(note: the atlas uses the full VMH MBA term; VMHvl-specificity is not encoded at this resolution.)*
- **Neurotransmitter**: The supertype label "Glut_2" denotes a glutamatergic identity, consistent with the known predominant NT phenotype of VMHvl neurons, although NT was not explicitly stated in the classical node's source references.
- **Nkx2-1**: Precomputed mean expression = 5.34 — strong expression, CONSISTENT with *Nkx2-1* as a defining marker.
- **Pgr**: Precomputed mean expression = 4.54 — moderate-to-strong expression, APPROXIMATE alignment with *Pgr* as a defining marker.
- **Esr1**: Precomputed mean expression = 2.35 — moderate expression, APPROXIMATE alignment. *Esr1* marks a subset of cells within the supertype rather than the full population.
- **Tac1**: Precomputed mean expression = 1.39 — low expression, APPROXIMATE alignment. This is consistent with *Tac1* marking only the ERα/*Nkx2-1*/*Tac1*+ functional subpopulation rather than all *Esr1*/*Pgr*+ neurons.

### Marker evidence provenance

All expression values cited above are precomputed atlas metadata (WMBv1 mean expression statistics); no primary literature evidence has yet been extracted for marker expression in SUPT_0564 specifically. The classical marker citations are [1] (*Esr1*, *Nkx2-1*, *Tac1*) and [2] (*Pgr*).

### Concerns

1. **AMBIGUOUS_MAPPING — heterogeneous classical node.** The classical *vmhvl_esr1_pr_neuron* spans at least three functional/molecular subpopulations and ~17 transcriptomic types (Kim 2019). A single supertype-level match is therefore cross-cutting by design; no one atlas supertype is expected to fully capture this classical node.

2. **Missing co-primary candidate — SUPT_0563.** CS20230722_SUPT_0563 (VMH Fezf1 Glut_1) is the parent supertype of the two most female-biased rank-0 clusters in the WMBv1 taxonomy (CLUS_2290, male-to-female ratio = 0.08; CLUS_2292, MFR = 0.12). This supertype was not retrieved in the rank-1 database query and has not been assessed. Given that female-biased lordosis circuits are a defining feature of the broader ERα VMHvl population, SUPT_0563 should be evaluated as a co-primary CROSS_CUTTING target.

3. **High Calb1 expression in SUPT_0564.** The gene with the highest mean expression in this supertype is *Calb1* (mean = 8.0). *Calb1* is not a defining marker of *vmhvl_esr1_pr_neuron* and is instead a canonical marker of the sexually dimorphic nucleus of the preoptic area (SDN-POA) calbindin neurons — a distinct classical type. High *Calb1* in SUPT_0564 may indicate that this supertype contains, or is dominated by, a *Calb1*+/*Esr1*+ subpopulation not previously characterised in the VMHvl. Primary literature verification is needed before accepting this mapping at MODERATE confidence.

### What would upgrade confidence

- Addition of SUPT_0563 as a co-primary mapping target, with explicit evaluation of its female-biased cluster composition, would provide a more complete picture of the atlas landscape for this classical node.
- ISH or MERFISH data confirming co-localisation of *Esr1*, *Pgr*, *Nkx2-1*, and *Tac1* within SUPT_0564 cells in the VMHvl would strengthen the marker alignment.
- Clarification of the *Calb1* expression pattern (co-localised with *Esr1*/*Pgr* vs. marking a distinct subpopulation) would resolve the specificity concern and either support or challenge this mapping.
- Literature evidence (from the ASTA corpus survey or targeted retrieval) linking SUPT_0564 clusters to the classical *Esr1*/*Pgr* VMHvl literature would raise confidence to HIGH.
- Splitting the classical node into functional sub-nodes (Pgr+/mating, ERα/Nkx2-1/Tac1+/locomotion, etc.) and remapping each individually would yield more precise, single-valued mapping edges.

---

## Open questions

1. Should SUPT_0563 (VMH Fezf1 Glut_1) be added as a co-primary CROSS_CUTTING target for the female-biased lordosis subpopulation? *(note: SUPT_0563 was not retrieved in the rank-1 DB query; requires manual assessment.)*
2. Does *Calb1* co-localise with *Esr1*/*Pgr* in VMHvl neurons (suggesting a novel *Calb1*+/*Esr1*+ subpopulation), or does it mark a distinct subpopulation within SUPT_0564 unrelated to the classical *vmhvl_esr1_pr_neuron* type?

---

## Proposed experiments

### ISH / MERFISH

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Multiplex FISH for *Esr1*, *Pgr*, *Nkx2-1*, *Tac1* in VMHvl | SUPT_0564 spatial clusters | Co-expression frequencies and spatial distribution within VMHvl | Confirms marker alignment; distinguishes subpopulations |
| *Calb1* / *Esr1* co-expression in VMHvl | SUPT_0564 | Co-expression rate | Resolves whether *Calb1*+ cells are the same or different from *Esr1*/*Pgr*+ cells |

### Transcriptomics / database query

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Rank-1 DB query including SUPT_0563 | CS20230722_SUPT_0563 | Expression of *Esr1*, *Pgr*, *Nkx2-1*, *Tac1*, *Calb1* in SUPT_0563 | Determines whether SUPT_0563 should be a co-primary mapping target |
| Rank-0 (cluster-level) mapping for female-biased clusters CLUS_2290 and CLUS_2292 | Individual rank-0 clusters | Cluster-level marker profiles | Identifies which atlas clusters best represent the lordosis/female-biased ERα subpopulation |

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564 | ATLAS_METADATA | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | S et al. 2015 | PMID:25543145 | Soma location; *Esr1*, *Nkx2-1*, *Tac1* markers; neuropeptide *Tac1* |
| [2] | N et al. 2021 | PMID:33910083 | *Pgr* marker; sexually dimorphic VMHvl subpopulation |
