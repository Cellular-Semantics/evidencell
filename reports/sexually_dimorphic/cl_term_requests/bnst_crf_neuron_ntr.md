# CL new term request: GABAergic corticotropin-releasing neuron of the anterolateral bed nuclei of the stria terminalis

*Drafted from `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml` node `bnst_crf_neuron` on 2026-09-11.*
*Parent (current cl_mapping): corticotropin-releasing neuron (CL:4072021) — BROAD*

**Preferred term label**
GABAergic corticotropin-releasing neuron of the anterolateral bed nuclei of the stria terminalis

**Synonyms** (with reference where available)
- dlBNST CRF neuron (narrow — names the dorsolateral subdivision specifically) — PMID:32277042 (Salimando et al. 2020)
- BNSTDL CRF neuron (narrow — same dorsolateral subdivision) — PMID:28439099 (Asok et al. 2017)
- BNSTALG CRF neuron (related — rat anterolateral group nomenclature) — PMID:24009552

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A corticotropin-releasing neuron with its soma in the anterolateral bed nuclei of the stria terminalis, chiefly the dorsolateral and oval subnuclei (PMID:23554470; PMID:33633549; PMID:21310239). Unlike the hypothalamic paraventricular population, it is GABAergic: single-cell RT-PCR in rat detects Gad1 (GAD67) and no vesicular glutamate transporter transcript, and about 98% of Crh-expressing dorsolateral cells in mouse are GABAergic (PMID:24009552; PMID:30362199). In mouse this population is female-biased, females having larger and more numerous such cells than males; the difference is absent at postnatal day 5 and is gonadal-hormone dependent (PMID:30691514). Axons reach the lateral hypothalamic area and paraventricular hypothalamic nucleus (PMID:42549128; PMID:30038273). Membrane properties are heterogeneous, with at least four electrophysiological subtypes (PMID:23325234).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
corticotropin-releasing neuron (CL:4072021) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_4072021

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
anterior division of bed nuclei of stria terminalis (UBERON:0011173) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011173

Narrower term available if editors prefer maximal specificity for the oval subnucleus:
oval nucleus of stria terminalis (UBERON:0011176) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011176
(verified in OLS4: UBERON:0011176 is part of UBERON:0011173, which is in turn part of bed nucleus of stria terminalis, UBERON:0001880; an alternative Allen-derived term, UBERON:0023958 'bed nuclei of the stria terminalis oval nucleus', exists but is asserted only under UBERON:0001880 and is not placed in the anterior division)

**Your ORCID**
[To be added by submitter]

**Additional notes or concerns**

*What gap this fills.* CL:4072021 'corticotropin-releasing neuron' currently has no asserted subclasses (checked in OLS4, 2026-09-11), and a search of CL for any bed-nucleus-of-the-stria-terminalis neuron term returns nothing. The CL:4072021 definition enumerates the paraventricular nucleus, hippocampus, piriform area, central amygdalar nucleus, Barrington's nucleus and inferior olivary complex as locations and does **not** mention the bed nuclei of the stria terminalis, so the BNST population is not covered by the existing text definition either. This is therefore a genuine gap, and the request is for a location- and transmitter-restricted child.

*Be aware that the molecular differentia are weak.* This should be stated plainly rather than discovered by an editor later. The only positive marker that defines this population is *Crh* — which is exactly what the parent term already asserts. The real differentia on offer are **anatomical** (anterolateral/dorsolateral BNST, including the oval nucleus) and **transmitter-based** (GABAergic, in contrast to the neuroendocrine paraventricular CRF population). A prior KB-wide survey of candidate CL contributions scored this node as the weakest of four candidates: legitimate for CL as a location-restricted child, but not meeting a "defining molecular description" bar. That assessment still substantially holds. If CL editors require a molecular differentia beyond the parent's own marker, this request should be declined or deferred rather than padded.

*Directionality of the GABAergic claim (please do not invert it).* Nguyen et al. 2016 (PMID:26718312), as quantified and reported by Companion & Thiele 2018 (PMID:30362199), established that ~98% of CRF-positive neurons in the dorsolateral BNST are GABAergic — that is, P(GABAergic | CRF+) ≈ 0.98. The converse statement (that ~98% of BNST GABAergic neurons are CRF+) appears in at least one secondary source and is **false**: CRF+ cells are only a small minority (~8%) of anterodorsal BNST neurons, and the region's GABAergic population is a peptide-defined mosaic (Pdyn, Penk, Nts, Npy, Pnoc, Sst, Tac1, Tac2, Avp; Prkcd/Drd1 in the oval nucleus; PMID:33633549). Only the Nguyen direction is asserted here. Note also that Nguyen et al. report the BNST CRF population as comprising both GABAergic and glutamatergic subpopulations; this request covers the GABAergic majority only, and the glutamatergic minority is modelled separately in the source KB.

*Relationship to the electrophysiological "Type III" class — not equivalent.* In rat BNSTALG, ~95% of Type III neurons express *Crh* mRNA, i.e. P(CRF+ | Type III) = 0.95 (PMID:24009552). The converse, P(Type III | CRF+), has **not** been measured, and whole-cell recordings from identified BNST CRF neurons resolve at least four electrophysiologically separable subtypes (PMID:23325234). Type III is therefore a **subset** of this population, not a synonym for it. A sibling new-term request is being drafted for the Type III CRF neuron as a prospective child of the term requested here; the two must not be conflated. (A prior version of the source KB additionally mis-attributed CRF identity to "type II" dlBNST neurons on the basis of PMID:23554470; those type II cells are cells that *respond* to bath-applied CRF and were never shown to express *Crh*. That error has been corrected in the KB and is flagged here so it is not reintroduced.)

*Negative markers that deliberately are not axiomatised.*
- **Oxt-negative** (0/19 cells, PMID:24009552). Real, but its evidential role is contrast with **paraventricular parvocellular** CRF neurons (83% Oxt+ in the same study), not discrimination among BNST neighbours — no BNST population is reported as Oxt+. It does not function as a differentia against sibling terms under the same parent, so it is kept out of the definition and out of the axioms. The measurement was also made in Type III cells specifically, i.e. in a subset of this population.
- **Calb1-negative.** Used in the source KB to distinguish this population from the calbindin-positive, male-biased, Kiss1+ principal nucleus of the BNST. Not axiomatisable: calbindin is a cytosolic calcium-binding protein, so `lacks_plasma_membrane_part` would be biologically wrong. Editors should also know that this particular negative assertion carries **no per-marker citation** in the source KB, so it is reported here as prose only and should be re-sourced before any use in a logical definition. An independent signal of the same issue: the closest whole-brain atlas match for this population (Allen WMBv1 supertype CS20230722_SUPT_0393, "CEA-BST Rai14 Pdyn Crh Gaba_2") shows substantial Calb1 expression, most likely because the supertype aggregates Calb1-negative CRF neurons with Calb1-positive BNST neurons.

*Unresolved anatomical granularity (a caveat on the source data, not on UBERON).* The source KB records three separate soma-location entries — dorsolateral BNST, oval nucleus of the BNST, and anterolateral BNST — but all three point at the same Allen Mouse Brain Atlas parent term MBA:351 ('Bed nuclei of the stria terminalis'), because the MERFISH annotation used in the KB has no sub-nucleus assignment. UBERON does carry the subdivisions (verified above), and UBERON:0011173 is proposed because it is the smallest UBERON term that contains all three named subdivisions. Whether the population is best circumscribed at the anterior-division level, or specifically at the oval nucleus, is not resolved by the current evidence.

*Morphology.* No morphological reconstruction data exist for this population anywhere in the source corpus, and none is asserted. The only morphology-adjacent datum is the female-biased soma-size difference cited in the definition. Nguyen et al. 2016 explicitly list correlating BNST neurochemical markers with morphology as future work.

*Species.* Assertions are drawn from mouse and rat. The anatomical location, GABAergic identity in the *Crh*+ population, and sexual dimorphism are reported in mouse; the single-cell RT-PCR transmitter phenotyping and the Type III association are rat (BNSTALG). Taxon-restricting the term is not proposed.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'anterior division of bed nuclei of stria terminalis' (UBERON:0011173)
- subClassOf 'capable of' (RO:0002215) some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534) — this should autoclassify the term under 'GABAergic neuron' (CL:0000617), which is how the source KB records the transmitter phenotype

Inherited from the parent and so not restated as an assertion (listed only so editors can confirm it is intended): 'capable of' (RO:0002215) some 'corticotropin-releasing hormone secretion' (GO:0043396).

Axioms considered and deliberately **not** proposed:
- `expresses` some *Crh* — redundant with the parent class, which is already defined by CRH secretion.
- `sends synaptic output to region` (RO:0013003) some 'lateral hypothalamic area' (UBERON:0002430) / 'paraventricular nucleus of hypothalamus' (UBERON:0001930) — the tracing evidence (PMID:42549128; PMID:30038273) is for the BNST CRF population as a whole and identifies the lateral-hypothalamus-projecting cells as a *subpopulation*; part of the *Crh* population is local-circuit rather than long-range (PMID:33633549). An "all instances" axiom would therefore be unsound.
- `lacks_plasma_membrane_part` some calbindin / oxytocin — wrong on biological grounds (both are cytosolic or secreted, not plasma-membrane components) as well as on scope grounds; see negative-marker note above.
- `has characteristic` some PATO morphology or electrophysiology quality — no morphology data, and the electrophysiology is explicitly heterogeneous (at least four subtypes), so no single quality holds for all instances.

Key references:
- Ide et al. 2013 — PMID:23554470 — supports: soma location in dorsolateral/anterolateral BNST; also the source of the corrected "type II" CRF-response result
- Giardino & Pomrenze 2021 — PMID:33633549 — supports: anatomical distribution within the lateral BNST compartment; peptide-defined mosaic of BNST GABAergic subpopulations; local-circuit CRF interneurons
- Hazra et al. 2011 — PMID:21310239 — supports: recording-site localisation to the oval/juxtacapsular/anterolateral BNST; Type I–III physiological classification
- Dabrowska et al. 2013 — PMID:24009552 — supports: GAD67-positive and VGLUT1-3-negative phenotype by single-cell RT-PCR; ~95% of Type III neurons CRF mRNA+; Oxt-negativity versus 83% Oxt+ in PVN parvocellular CRF neurons
- Companion & Thiele 2018 — PMID:30362199 — supports: ~98% of dlBNST CRF+ neurons are GABAergic (reporting Nguyen et al. 2016)
- Nguyen et al. 2016 — PMID:26718312 — supports: the BNST CRF population comprises GABAergic and glutamatergic subpopulations; primary source for the 98% figure
- Silberman et al. 2013 — PMID:23325234 — supports: at least four electrophysiologically separable subtypes among identified BNST CRF neurons
- Uchida et al. 2019, "Female-biased sexual dimorphism of corticotropin-releasing factor neurons in the bed nucleus of the stria terminalis" — PMID:30691514 — supports: female-biased number and size of dlBNST CRF neurons; absent at P5; ovariectomy/orchiectomy dependence
- Romero et al. 2026 — PMID:42549128 — supports: anterograde tracing to the lateral hypothalamic area and paraventricular hypothalamic nucleus
- Giardino et al. 2018 — PMID:30038273 — supports: LH-projecting GABAergic BNST CRF subpopulation
- Salimando et al. 2020 — PMID:32277042 — supports: Crh-IRES-Cre labelling of dlBNST CRF neurons; GluN2D-NMDAR currents

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml#bnst_crf_neuron`.*
*Source facts: `reports/sexually_dimorphic/bnst_crf_neuron_facts.json`.*
