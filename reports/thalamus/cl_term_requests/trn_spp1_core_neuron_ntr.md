# CL new term request: Spp1-expressing GABAergic projection neuron of the thalamic reticular nucleus core

*Drafted from `kb/graphs/thalamus/trn_spp1_core_neuron.yaml` node `trn_spp1_core_neuron` on 2026-11-27.*
*Parent (current cl_mapping): GABAergic neuron (CL:0000617) — BROAD*

**Preferred term label**
Spp1-expressing GABAergic projection neuron of the thalamic reticular nucleus core

**Synonyms** (with reference where available)
- TRN Spp1+ core GABAergic neuron (exact — the source KB node name) — PMID:32699411
- thalamic reticular nucleus core neuron (broad — names the anatomical pole without the marker) — PMID:41622438
- TRN inner neuron (related — the review's alternative wording for core neurons) — PMID:41622438
(The source KB records no `synonyms` list for this node; the entries above are drawn from the node name and from the wording used in the cited primary sources.)

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A GABAergic projection neuron with its soma in the central core of the thalamic reticular nucleus, at one pole of a continuous transcriptomic gradient spanning that nucleus (PMID:32699411; PMID:39630580). In mouse it expresses Spp1 and not Ecel1, the two markers being mutually exclusive only in neurons at the extremes of the gradient (PMID:32699411). It projects to first-order thalamic nuclei, shows high bursting activity, and contributes to sleep spindle generation and to delta rhythm power during slow-wave sleep (PMID:32699411; PMID:39630580). Core neurons of this nucleus are described as having larger somata and more extensive dendritic trees than edge neurons, allowing greater integration of synaptic inputs (PMID:41622438).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
GABAergic projection neuron (CL:0020140) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0020140

Recommended additional asserted parent:
thalamus GABAergic neuron (CL:0020129) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0020129

The source KB's `cl_mapping` records the broader CL:0000617 'GABAergic neuron'. CL:0020140 and CL:0020129 are both descendants of CL:0000617, so this is a tightening of the recorded mapping rather than a contradiction of it — see the notes below.

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
thalamic reticular nucleus (UBERON:0001903) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001903

UBERON has no term for the core (inner) subdivision of this nucleus; the whole nucleus is the most specific available term, and the core location is stated in the text definition only.

**Your ORCID**
[To be added by submitter]

**Additional notes or concerns**

*Read this first: this term describes one pole of a continuum, not a discrete cluster, and that is the main reason an editor might decline it.* Li et al. 2020 (PMID:32699411) characterise heterogeneity in this nucleus as "a transcriptomic gradient of two negatively correlated gene-expression profiles", with the two markers mutually exclusive **only** in neurons at the extremes; Hartley et al. 2024 (PMID:39630580) likewise speak of "the two transcriptional poles of this gradient". Cells lying between the poles are not covered by this term, nor by the sibling term requested for the opposite pole, so the two requested terms do not partition the nucleus. The source KB states this explicitly and warns that atlas mapping should expect a gradient rather than a one-to-one cluster correspondence. If CL's position is that classes must be discrete, this request and its sibling should be declined together, and the parent node (the thalamic reticular nucleus GABAergic neuron as a whole) proposed instead. That is a legitimate outcome and is put here rather than left for an editor to discover.

*What gap this fills.* CL has no term for a neuron of this nucleus defined by anatomy or by these markers. A full-text CL search (OLS4, 2026-11-27) for "thalamic reticular nucleus" returns no cell term located there; searches for Spp1 and Ecel1 as differentia return nothing. Two near misses are worth recording. First, CL:0020140 'GABAergic projection neuron', the proposed parent, carries a comment naming the thalamic reticular nucleus as one of the regions where it is "the main GABAergic neuron type" — so CL already recognises this population at the parent level, without distinguishing it. Second, CL:4300862 'RT-ZI Gnb3 Gaba_2 GABAergic neuron (Mmus)' is an Allen Whole Mouse Brain atlas-derived term (supertype CS20230722_SUPT_0432) whose name references the reticular nucleus; its differentia are Slc22a3, Pvalb, Fgf10 and Pou6f2, not Spp1 or Ecel1, and it is not asserted to correspond to either gradient pole. **The source KB's `cl_mapping` notes for this node state that no CL term exists for this nucleus or its subtypes; given CL:4300862 that statement is too strong and the curator should soften it.** Per the repository's CL-mapping procedure an existing `cl_mapping` is not edited by this workflow, so the node YAML has been left unchanged.

*On the proposed parent.* The KB records BROAD to CL:0000617 'GABAergic neuron' with confidence LOW. Two more specific containing terms exist and are proposed instead: CL:0020140 'GABAergic projection neuron' (these cells project to first-order thalamic nuclei, and the term's own comment names this nucleus) and CL:0020129 'thalamus GABAergic neuron' (UBERON places this nucleus under 'dorsal plus ventral thalamus', UBERON:0001897, via the ventral thalamus, verified in OLS4). Both are descendants of CL:0000617. The CL-mapping procedure asks for the most specific containing term, so the curator may wish to tighten the node's `cl_mapping` to CL:0020140.

*Marker caveats that bear on how the term should be grounded.* Spp1 and Ecel1 come from single-nucleus RNA-seq (PMID:32699411, re-reported in PMID:39630580); the review's statement that core neurons "almost exclusively express Spp1" (PMID:41622438) does not state an assay. The annotation transfer source recorded in the KB (GEO:GSE145273, author-assigned "Spp1+" segment, 264 nuclei) is itself a **binarised marker call at one end of a continuous gradient**, not an independently derived cluster, so purity rather than recall is the meaningful metric for any atlas correspondence. Editors should not read "Spp1+" as a discrete transcriptomic type.

*The projection claim is indirect, and should be read carefully.* The first-order projection was established by retrograde RetroBead tracing from first-order thalamic nuclei combined with RNA-FISH, in **separate animals** from the sequenced nuclei; 85.7% of first-order-labelled neurons of this nucleus were Spp1-positive (PMID:32699411). That is a strong association but it is not a demonstration that every Spp1-positive neuron projects to first-order nuclei, and the inference runs through the marker call. No axiom is proposed on it.

*Morphology caveat.* The larger-soma and larger-dendritic-tree description comes from a review of "core (inner)" neurons (PMID:41622438), which cites Lam et al. 2011, Li et al. 2020 and Martinez-Garcia et al. 2020; only Li et al. tie core identity to Spp1. The morphological claim is therefore about the anatomical core, and its transfer to the Spp1 pole rests on that one link. It is retained in the text definition with its source but is not axiomatised.

*A molecular overlap that is deliberately not asserted.* This population may overlap the parvalbumin-positive, rhythmogenic, first-order-projecting population described by Clemente-Perez et al. 2017 (PMID:28591583). Neither the source report nor its quotes state that correspondence, so Pvalb is not asserted here. Gad1 and Pvalb are recorded in the KB for neurons of this nucleus generally, not for this pole specifically. Note that the atlas term CL:4300862 does carry Pvalb as a differentia, which is suggestive but not evidence.

*Species.* All cited primary evidence is mouse. The source KB sets the node species to Mus musculus from the MeSH organisms of the cited primary papers, flagged for confirmation from primary literature. No taxon restriction is proposed.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'thalamic reticular nucleus' (UBERON:0001903)
- subClassOf 'expresses' (RO:0002292) some 'osteopontin' (PR:000015561) — the mouse-specific entry is 'osteopontin (mouse)' (PR:P10923). Spp1 is the gene symbol; osteopontin is its protein product, which is what PRO identifies.

Inherited from the parent and so not restated as an assertion (listed only so editors can confirm it is intended): 'capable of' (RO:0002215) some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534), which is how the source KB records the transmitter phenotype (`nt_type.cl_terms` = CL:0000617). If CL:0020129 carries an equivalence axiom over soma location in the dorsal plus ventral thalamus, the soma-location axiom above should autoclassify the term under it through the `has_soma_location o part_of` property chain.

Axioms considered and deliberately **not** proposed:
- `sends synaptic output to region` (RO:0013003) some first-order thalamic nuclei — "first-order" is a functional classification of thalamic nuclei, not an UBERON structure, so there is no filler to use. Enumerating individual nuclei would overstate what the tracing study shows. See the indirectness caveat above.
- `lacks_plasma_membrane_part` some ECEL1 — the Ecel1-negative assertion is real and is the clearest contrast with the sibling term, but the evidence is transcript-level mutual exclusivity **at the gradient extremes only**, which is precisely where an "all instances" negative axiom is least safe. The relations guide also warns that this relation can cause reasoning errors. Kept in the text definition only.
- `has characteristic` (RO:0000053) some PATO quality for high bursting, or for larger soma and dendritic extent — the bursting claim is comparative (high relative to the opposite pole) and PATO qualities describing a change or a relative increase are discouraged by the definition guidelines; the size claim is comparative in the same way and additionally rests on the review-level inference described above.
- `capable of part of` (RO:0002216) some sleep-spindle or delta-rhythm process — the contribution to spindle generation and delta power is a network-level result from in vivo subnetwork perturbation, not a process this cell carries out, and mapping it to a GO process would overstate it.

Key references:
- Li et al. 2020 — PMID:32699411 — supports: the transcriptomic gradient and its two poles; mutually exclusive Spp1 and Ecel1 at the extremes; core-like anatomical organisation; first-order projection by retrograde tracing plus RNA-FISH; high bursting; the GEO:GSE145273 dataset and its author-assigned segment labels (integrated snRNA-seq, slice electrophysiology and in vivo subnetwork perturbation, adult female mouse, 671 Gad2+ Pvalb+ nuclei)
- Hartley et al. 2024 — PMID:39630580 — supports: Spp1-positive neurons located in the central core and Ecel1-positive neurons in the bordering shell; the two transcriptional poles framing; sleep spindle and delta rhythm roles; the nucleus as a thin shell of GABAergic neurons (summary of Li et al., mouse)
- Flores et al. 2026 — PMID:41622438 — supports: the nucleus as composed of GABAergic inhibitory neurons; core (inner) neurons located mainly in the central region with larger somata and more extensive dendritic trees than edge neurons; core neurons almost exclusively expressing Spp1 (review)
- Clemente-Perez et al. 2017 — PMID:28591583 — cited only to record the parvalbumin-positive population whose overlap with this one is suspected but not asserted

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/thalamus/trn_spp1_core_neuron.yaml#trn_spp1_core_neuron`.*
*Source facts: `reports/thalamus/trn_spp1_core_neuron_facts.json`.*
