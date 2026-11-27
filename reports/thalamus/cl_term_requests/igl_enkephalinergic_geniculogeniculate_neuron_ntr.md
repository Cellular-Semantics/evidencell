# CL new term request: enkephalinergic GABAergic projection neuron of the intergeniculate leaflet

*Drafted from `kb/graphs/thalamus/igl_enkephalinergic_geniculogeniculate_neuron.yaml` node `igl_enkephalinergic_geniculogeniculate_neuron` on 2026-11-27.*
*Parent (current cl_mapping): none — this node has no `cl_mapping` in the source KB.*

**WARNING TO THE SUBMITTER: this draft has no asserted parent term.** The source KB node carries no `cl_mapping`, so no parent has been curator-approved. The parent slot below is left as `[parent term required]` and MUST be filled in before this request is posted. Candidate parents found by search are listed in the notes, but choosing between them is a curator decision that this workflow does not make.

**Preferred term label**
enkephalinergic GABAergic projection neuron of the intergeniculate leaflet

**Synonyms** (with reference where available)
- intergeniculate leaflet enkephalinergic geniculo-geniculate neuron (exact — the source KB node name) — PMID:23103793
- enkephalin-positive neuron of the geniculo-geniculate tract (exact) — PMID:23103793
- IGL ENK neuron (related — abbreviation-based, not proposed for the ontology) — PMID:27916729
(The source KB records no `synonyms` list for this node; the entries above are drawn from the node name and from the wording used in the cited primary sources.)

**Definition** (with inline references; PMID:XXXXXX or DOI format)
A GABAergic projection neuron with its soma in the intergeniculate leaflet of the lateral geniculate complex, one of the two principal GABAergic populations of that leaflet and interspersed with the neuropeptide Y-synthesising population (PMID:23103793; PMID:27916729). It contains enkephalin (Penk in rat) and does not synthesise neuropeptide Y (PMID:30803080; PMID:27208616). Its axons form the geniculo-geniculate tract innervating the contralateral leaflet, and it receives direct retinal innervation (PMID:23103793; PMID:25856520). It carries a T-type calcium current, and neurons identified as projecting to the contralateral leaflet fire in an infra-slow oscillatory pattern of rhythmic bursts, sustained in the light and diminished or absent in darkness (PMID:23103793; PMID:28041911).

**Parent cell type term** (https://www.ebi.ac.uk/ols4/ontologies/cl)
[parent term required]

**Anatomical structure where the cell type is found** (https://www.ebi.ac.uk/ols4/ontologies/uberon)
intergeniculate leaflet of the lateral geniculate complex (UBERON:0035975) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0035975

**Your ORCID**
[To be added by submitter]

**Additional notes or concerns**

*No parent is asserted, and this is deliberate.* The source KB node has no `cl_mapping` at all. Its notes record why: a search for an enkephalinergic central-nervous-system neuron term found only peripheral ones, so the field was left empty and marked CANDIDATE, with the observation that any new term would sit under CL:0000617 'GABAergic neuron'. Because no parent has been curator-approved, this workflow leaves the parent slot blank rather than choosing one. **Recommended curator action: add a BROAD `cl_mapping` to this node and re-draft, or fill the parent slot by hand before posting.** For that decision, the candidates found by search (OLS4, 2026-11-27) are:

- CL:0020140 'GABAergic projection neuron' — "A projection neuron that uses GABA as a vesicular neurotransmitter". Contains this population and captures both the transmitter and the projection identity. This is the same term proposed as parent for the sibling neuropeptide Y population, which would keep the two siblings under one parent.
- CL:0020129 'thalamus GABAergic neuron' — "A GABAergic neuron that has its soma located in the dorsal plus ventral thalamus". Also contains this population: UBERON places the intergeniculate leaflet under 'dorsal plus ventral thalamus' (UBERON:0001897) via the lateral geniculate body and metathalamus, verified in OLS4.
- CL:0000617 'GABAergic neuron' — the term the source KB's own notes name. Correct but less specific than either of the above; the CL-mapping procedure asks for the most specific containing term.
- CL:0000506 'enkephalin secreting cell' — relevant but **not usable as the sole parent**: its ancestors are 'secretory cell', 'peptide hormone secreting cell' and 'endorphin secreting cell', and it is not under 'neuron'. Editors may want it as a second asserted parent.

*What gap this fills.* CL contains no term mentioning the intergeniculate leaflet (full-text search returns zero cell terms, OLS4, 2026-11-27), and no term for an enkephalinergic neuron of the central nervous system. The enkephalin-related cell terms that exist are CL:4033113 'cervicothoracic ganglion enkephalin neuron' and CL:4033118 'thoracic ganglion enkephalin neuron', both defined as sympathetic neurons, plus CL:0020050 'ascending interneuron of myenteric plexus' and the non-neuronal CL:0000506. This confirms the source KB's assessment. The geniculo-geniculate tract is the route by which the two leaflets coordinate, and it has no ontology representation at present.

*The single most important caveat: the enkephalinergic identity of the electrophysiologically defined group is partly inferred, not demonstrated.* Editors should weigh this before accepting the electrophysiology into the definition. Chrobok et al. 2016 (PMID:27208616) define the T-type-current group **only** as neurons that do not synthesise neuropeptide Y; they did not label enkephalin. Later work equates that group with enkephalinergic cells (PMID:30803080). The infra-slow oscillatory cells are described as "putatively enkephalinergic" (PMID:28041911), and in Blasiak et al. 2013 (PMID:23103793) the oscillatory cells are identified by their projection to the contralateral leaflet, not by enkephalin labelling. The neuropeptide-Y-negative group may additionally contain a reported third cell group of unknown transmitter content (PMID:23432696) and the neuropeptide-Y-lacking Type I cells of Thankachan and Rusak 2005 (PMID:16207879). **The negative marker and the electrophysiological properties may therefore describe a superset of the true enkephalinergic class.** If editors prefer a definition resting only on directly demonstrated properties, the T-type current and infra-slow oscillation sentences should be cut, leaving soma location, transmitter, peptide and projection target.

*What distinguishes this term from its sibling.* The leaflet's GABAergic neurons divide into two populations with different peptides and different targets: this one, enkephalin-positive and projecting to the contralateral leaflet, and a neuropeptide Y-positive one projecting to the suprachiasmatic nucleus (PMID:23103793; PMID:27916729). A sibling new term request is being drafted for the neuropeptide Y population. The two should be reviewed together; they are the two halves of one division and neither makes full sense alone. The source KB additionally records a hypothesis that these cells act as a powerful inhibitory element on themselves and on the neuropeptide Y cells in both leaflets, and that met-enkephalin hyperpolarises putatively enkephalinergic neurons via mu-opioid receptors (PMID:27916729). That is explicitly a hypothesis in the source and is not used as a differentia.

*Marker evidence is immunohistochemical, not transcriptomic.* The source KB records Penk as the rat-convention gene symbol for the precursor of the met-enkephalin named in the sources, and states that the evidence is protein-level. The supporting sources state the marker without specifying an assay (PMID:23103793; PMID:27916729; PMID:30803080). Editors should read the marker as peptide content.

*No morphology.* The source KB records no somatodendritic description for this population. Nothing morphological is asserted or axiomatised.

*Species.* The source KB scopes this node to Rattus norvegicus; every cited primary source is rat. CL terms are normally species-neutral and no taxon restriction is proposed, but editors should know the evidence base is single-species.

Proposed logical axioms:
- subClassOf 'has soma location' (RO:0002100) some 'intergeniculate leaflet of the lateral geniculate complex' (UBERON:0035975)
- subClassOf 'capable of' (RO:0002215) some 'gamma-aminobutyric acid secretion, neurotransmission' (GO:0061534) — this is how the source KB records the transmitter phenotype (`nt_type.cl_terms` = CL:0000617). It is listed as a proposed axiom rather than as inherited **because no parent is asserted**; if a GABAergic parent is chosen from the candidates above it becomes redundant and should be dropped.
- subClassOf 'sends synaptic output to region' (RO:0013003) some 'intergeniculate leaflet of the lateral geniculate complex' (UBERON:0035975) — the geniculo-geniculate projection, supported by three sources (PMID:23103793; PMID:27916729; PMID:25856520). Note that the projection is specifically to the **contralateral** leaflet and UBERON has no laterality-specific term for this structure, so the axiom as written loses the contralaterality. Editors who find that unacceptable should drop the axiom and keep the fact in the text definition, where it is stated precisely.
- subClassOf 'expresses' (RO:0002292) some 'proenkephalin-A' (PR:000012544) — if editors prefer a taxon-specific filler, the rat entry is 'proenkephalin-A (rat)' (PR:P04094). Please see the inferred-identity and immunohistochemistry caveats above.

Axioms considered and deliberately **not** proposed:
- `lacks_plasma_membrane_part` some neuropeptide Y — biologically wrong: neuropeptide Y is a secreted peptide, not a plasma membrane component. The negative marker is real and evidentially important (it is the only criterion by which the electrophysiological group was actually defined), but it belongs in the text definition, not in a logical axiom. It is also the locus of the superset risk described above.
- `has characteristic` (RO:0000053) some PATO quality for the T-type calcium current or the infra-slow oscillation — PATO has no term for a specific ionic current, and the oscillation is a light-state-dependent firing pattern rather than a static characteristic; the definition guidelines warn against qualities describing a change.
- `receives synaptic input in region` (RO:0013002) for the retinal innervation — the input is received in the leaflet, which the soma-location axiom already covers; an axiom naming the retina would invert the relation.

Key references:
- Blasiak et al. 2013 — PMID:23103793 — supports: the leaflet as a GABAergic population divisible into two anatomically and neurochemically distinct groups; enkephalin-positive neurons giving rise to the geniculo-geniculate tract to the contralateral leaflet; infra-slow oscillatory firing in cells identified by that projection, sustained in light (in vivo extracellular recording with antidromic identification, rat)
- Palus et al. 2017 — PMID:27916729 — supports: the two main GABAergic subpopulations of the leaflet; enkephalinergic cells connecting contralateral leaflets; mu-opioid hyperpolarisation and the inhibitory-element hypothesis (slice electrophysiology, rat)
- Palus-Chramiec et al. 2019 — PMID:30803080 — supports: leaflet GABAergic neurons co-expressing enkephalin; T-type calcium current attributed to enkephalinergic neurons (statement citing Moore et al., 1994 and the patch clamp literature, rat)
- Palus et al. 2015 — PMID:25856520 — supports: enkephalin-positive leaflet neurons connecting the two contralateral leaflets; direct retinal innervation (statement citing Takatsuji et al., 1989 and Juhl et al., 2007, rodent)
- Chrobok et al. 2016 — PMID:27208616 — supports: the T-type-current group defined as neurons that do **not** synthesise neuropeptide Y, with enkephalin identity inferred rather than labelled (whole-cell patch clamp with post hoc NPY immunohistochemistry, rat)
- Chrobok et al. 2017 — PMID:28041911 — supports: infra-slow oscillatory firing in putatively enkephalinergic leaflet neurons (in vivo extracellular recording, urethane-anaesthetised Wistar rat, light-on only)
- Blasiak A. et al. 2013 — PMID:23432696 — supports: a third leaflet cell group with unknown neurotransmitter content, bearing on the superset risk
- Thankachan and Rusak 2005 — PMID:16207879 — supports: neuropeptide-Y-lacking Type I cells, also bearing on the superset risk

---
*Drafted by evidencell cl-term-request workflow from `kb/graphs/thalamus/igl_enkephalinergic_geniculogeniculate_neuron.yaml#igl_enkephalinergic_geniculogeniculate_neuron`.*
*Source facts: `reports/thalamus/igl_enkephalinergic_geniculogeniculate_neuron_facts.json`.*
