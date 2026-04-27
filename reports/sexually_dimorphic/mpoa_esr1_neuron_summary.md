# MPOA estrogen receptor 1 (Esr1) neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:464] | [1] |
| NT | Mixed — GABAergic and glutamatergic subpopulations both documented in MPOA | — |
| Defining markers | Esr1, Ar, Pgr | [1] [2] |
| Negative markers | — | — |
| Neuropeptides | — | — |

**Definition basis:** Classical neurochemical. No CL term exists; candidate for one or more new CL terms.

**Curation note:** The MPOA Esr1 neuron is a heterogeneous population. As documented in the literature, the MPOA contains molecularly distinct Esr1-expressing subpopulations with non-overlapping functions: an Esr1+ population required for parental (pup-directed) behaviour, an Esr1+ population governing male-type mating behaviour, and an Nts+ population governing female socio-sexual behaviours [1] [2]. The classical node as currently defined likely spans multiple transcriptomic supertypes. It is flagged as a candidate for splitting into finer terms once the transcriptomic landscape is resolved.

> "Molecularly defined subpopulations of neurons expressing a variety of neuropeptides and/or hormonal receptors in the MPOA are tightly associated with reproductive behaviors. MPOA neurons expressing Gal (galanin) or Esr1 (estrogen receptor 1) are essential for parental behaviors, while MPOA neurons expressing Esr1 or Nts (neurotensin) govern male-type mating behaviors and female socio-sexual behaviors, respectively"
> — https://doi.org/10.1101/2021.09.02.458782, Neuronal Markers and Molecular Characteristics · [2] <!-- quote_key: 237425192_c17e0213 -->

> "A large hypothalamic structure, the MPOA sends projections to multiple downstream brain regions and is both larger and contains more neurons in males than in females [35]. Notably, the MPOA is home to various heterogeneous, molecularly defined, neuronal clusters, including many sexually dimorphic populations, such as androgen receptor (AR)-expressing population and estrogen receptor alpha (ESR1)expressing population [80]"
> — N et al. 2021, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 233446934_5d0fb07e -->

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype label | Cells (MPN) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_SUPT_0486 | 0486 PVpo-VMPO-MPN Hmx2 Gaba_5 | 37 (MBA:515) | 🟡 MODERATE | Esr1 DEFINING (7.72), Ar (8.15), Pgr (6.80); MBA:515 = MPN | Best candidate — GABAergic fraction only |

---

## CS20230722_SUPT_0486 — 0486 PVpo-VMPO-MPN Hmx2 Gaba_5

### Supporting evidence

SUPT_0486 is the best current candidate for the GABAergic fraction of MPOA Esr1 neurons. The supertype label encodes MPN (medial preoptic nucleus) directly, consistent with the classical soma location Medial preoptic nucleus [MBA:464]. The atlas registers 37 cells in MBA:515 (MPN), 64 cells in MBA:133 (PVpo), and 16 cells in MBA:272 (AVPV) within this supertype; the MPN compartment is therefore the minority fraction numerically, though it is the most directly concordant.

*(note: MBA:515 and MBA:464 refer to the same anatomical structure — the medial preoptic nucleus — under different atlas versions or resolution levels; the location assignment is treated as concordant.)*

All three defining markers of the classical node show high precomputed mean expression across SUPT_0486: Esr1 = 7.72 (annotated as a DEFINING atlas marker for this supertype), Ar = 8.15, Pgr = 6.80. This three-way co-expression profile is a strong marker alignment given that the classical node is defined precisely by co-expression of these steroid hormone receptor genes.

> "Since the MPOA is enriched in the expression of steroid hormone receptors genes (e.g., Esr1, androgen receptor (Ar), progesterone receptor (Pgr))"
> — https://doi.org/10.1101/2021.09.02.458782, Neuronal Markers and Molecular Characteristics · [2] <!-- quote_key: 237425192_b8087ed0 -->

### Marker evidence provenance

| Marker | Classical evidence | Atlas value | Alignment |
|---|---|---|---|
| Esr1 | Positive, transcript, defining [1] [2] | Mean expression 7.72 (DEFINING atlas marker) | Consistent |
| Ar | Positive, transcript, defining [1] [2] | Mean expression 8.15 | Consistent |
| Pgr | Positive, transcript, defining [2] | Mean expression 6.80 | Consistent |

Marker evidence for the classical node is drawn from two sources: a 2021 review of sexually dimorphic brain regions [1] and a preprint characterising MPOA neuronal subpopulations [2]. Atlas precomputed expression values represent cluster-level means from the WMBv1 taxonomy. No single-cell co-expression data are available at this stage to confirm that all three receptors are co-expressed within individual cells of SUPT_0486.

### Concerns

1. **Partial coverage (GABAergic fraction only).** SUPT_0486 belongs to the GABAergic Hmx2 subclass. MPOA Esr1 neurons are documented to include both GABAergic and glutamatergic neurons. The glutamatergic Esr1+ fraction is expected to map to one or more separate preoptic supertypes, which have not yet been identified.

2. **Functional heterogeneity unresolved at supertype level.** The classical node spans at least two distinct functional subpopulations (parental behaviour circuit and male mating behaviour circuit), and a third (Nts+, female socio-sexual) that partially overlaps Esr1 expression. These subtypes are expected to correspond to distinct clusters within SUPT_0486 or across adjacent supertypes, but cluster-level functional annotation is not yet available.

3. **Spatial spread within supertype.** The supertype encompasses three anatomical compartments (PVpo, VMPO, MPN). Only the MPN fraction (37 of ~117 total cells) is directly concordant with the classical soma location. The mapping is therefore weighted to a minority of cells within the supertype.

4. **Evidence tier.** All evidence is ATLAS_METADATA only. No literature co-citation, electrophysiology, morphology, or annotation transfer evidence has been incorporated.

> "At least two different subpopulations within the MPOA were shown to be required for the regulation of pupdirected behavior. The first is the ESR1 þ population, which is highly sexually dimorphic in its distribution and projection patterns [85]"
> — N et al. 2021, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 233446934_9f0f55ea -->

### What would upgrade confidence

- Identification of the glutamatergic Esr1+ preoptic supertype, enabling explicit splitting of the classical node into GABAergic and glutamatergic components, each with a dedicated mapping edge.
- Cluster-level Esr1/Ar/Pgr expression profiles within SUPT_0486 to identify which clusters are most specifically MPN-localised and highest in all three receptor genes.
- Annotation transfer results (MapMyCells) from a published MPOA single-cell dataset that includes Esr1+ cells, to provide cross-dataset validation.
- Literature evidence linking specific cluster accessions in SUPT_0486 to the parental behaviour or mating behaviour circuits.
- Confirmation of Nts co-expression status within SUPT_0486 clusters to disambiguate the female socio-sexual (Nts+) subpopulation from the parental/mating subpopulations.

---

## Proposed experiments

No experiments have been formally proposed in the current evidence record. The following are indicated by the open questions and caveats:

**Transcriptomic / Atlas**

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Cluster-level marker query within SUPT_0486 | Esr1, Ar, Pgr, Nts expression per cluster | Ranking of clusters by co-expression level and MPN spatial enrichment | Identifies the most specific cluster candidates within the supertype |
| Glutamatergic supertype candidate search | Preoptic glutamatergic supertypes with Esr1 expression | One or more glutamatergic MPOA Esr1 supertype candidates | Closes the coverage gap for the glutamatergic fraction |

**Cross-dataset validation**

| What | Target | Expected output | Resolves |
|---|---|---|---|
| MapMyCells annotation transfer | Published MPOA Esr1+ scRNA-seq dataset | F1 matrix mapping source clusters to WMBv1 supertypes/clusters | Provides orthogonal evidence for or against SUPT_0486 as the primary match |

---

## Open questions

1. Which clusters within SUPT_0486 have the highest Esr1/Ar/Pgr co-expression and the strongest MPN anatomical signal?
2. Does the Nts+ female socio-sexual subpopulation map to SUPT_0486 or to a separate preoptic supertype?
3. What is the glutamatergic MPOA Esr1+ supertype, and what is its accession in WMBv1?
4. Should the classical node be split into at least two terms (GABAergic MPOA Esr1 neuron / glutamatergic MPOA Esr1 neuron) before finalising mapping edges?
5. Is the MPOA Esr1+ parental behaviour population distinguishable at the cluster level from the Esr1+ male mating behaviour population within SUPT_0486?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_mpoa_esr1_neuron_to_cs20230722_supt_0486 | ATLAS_METADATA | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | N et al. 2021 | PMID:33910083 | Soma location (Medial preoptic nucleus); Esr1, Ar marker evidence; sexually dimorphic population; parental behaviour |
| [2] | https://doi.org/10.1101/2021.09.02.458782 | — | Esr1, Ar, Pgr marker evidence; MPOA subpopulation functional annotation (parental, mating, socio-sexual behaviours) |
