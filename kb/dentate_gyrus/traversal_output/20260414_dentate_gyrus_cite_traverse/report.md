# Literature Review: dg_neuroblast, dg_immature_granule_neuron, dg_mature_granule_neuron — dentate gyrus neurogenesis electrophysiology patch-clamp immature granule neuron neuroblast neuropeptide species mouse rat

> **Query:** dentate gyrus neurogenesis electrophysiology patch-clamp immature granule neuron neuroblast neuropeptide species mouse rat
> **Node context:** Adult hippocampal neurogenesis lineage in the dentate gyrus spanning DCX+/Ki67+/PSA-NCAM+ proliferating neuroblasts in the subgranular zone, postmitotic DCX+/NeuN+/PSA-NCAM+ immature granule neurons in the inner granule cell layer, and terminally differentiated calbindin+/NeuN+/Tbr1+ mature glutamatergic granule neurons projecting mossy fibers to CA3.
> **Evidence:** 26 summaries from 23 unique papers
> **Sources:** 0 asta_snippet, 7 europepmc_fulltext, 17 asta_report, 2 abstract_only

## Electrophysiological maturation: the silent -> GABA -> glutamate -> fast GABA sequence

Whole-cell patch-clamp recordings from retrovirally GFP-labelled adult-born dentate granule cells in mouse establish a stereotyped sequence of synaptic and intrinsic maturation that is the most direct evidence available for the electrophysiology_class gaps in all three nodes. Espósito et al. 2005 [PMC fulltext, 2] define four functional stages: a silent progenitor/neuroblast phase (1-7 dpi) with high input resistance and small capacitance, a slow GABAergic-only phase (8-18 dpi), a phase in which glutamatergic inputs are added (>=18 dpi), and a final acquisition of fast perisomatic GABAergic inputs.

> "All GFP+ neurons studied between 1 and 7 dpi were silent, and their morphology seemed to correspond to class A or B." [2]
> "Neurons with GABAergic but not glutamatergic afferents were first observed at 8 dpi." [2]
> "Glutamatergic PSCs were detected in GFP+ neurons bearing GABAergic inputs from 18 dpi onwards." [2]

Quantitative passive membrane property values are available for each stage and directly fill the dg_neuroblast and dg_immature_granule_neuron electrophysiology gaps:

> "Silent neurons: Vrest (mV): − 50.6 ± 2.3; Cm (pF): 6.4 ± 0.4; Rinput (MΩ): 4.3 ± 0.5" [2]
> "GABA neurons: Vrest (mV): − 45.6 ± 2.3; Cm (pF): 11.7 ± 1.2; Rinput (MΩ): 2.9 ± 0.4" [2]
> "GABA and glu neurons: Vrest (mV): − 63.2 ± 2.8; Cm (pF): 24.6 ± 1.4; Rinput (MΩ): 0.62 ± 0.10" [2]

Ge et al. 2006 [PMC fulltext, 1] extend this picture with precise dpi milestones for synaptic input acquisition and identify tonic GABA activation as the earliest functional signal, preceding any phasic synaptic input:

> "At 3 days post viral injection (3 dpi), none of the GFP+ cells recorded under voltage-clamp (Vm= −65 mV) exhibited any spontaneous synaptic currents" [1]
> "tonic current in all GFP+ DGCs recorded from 3 dpi and onwards (n = 48)" [1]
> "Bicuculline (10 μM)-sensitive GABAergic PSCs...and CNQX (50 μM)-sensitive glutamatergic PSCs...were first detected in some GFP+ DGCs at 7 dpi and 14 dpi, respectively" [1]

The progression to functional, electrically mature granule neurons is documented by van Praag et al. 2002 [PMC fulltext, 5], providing the first direct patch-clamp evidence that adult-born cells fire action potentials and have membrane properties distinct from mature granule cells, supporting the dg_mature_granule_neuron electrophysiology baseline:

> "newly generated cells in the adult mouse hippocampus have neuronal morphology and can display passive membrane properties, action potentials and functional synaptic inputs similar to those found in mature dentate granule cells" [5]
> "membrane potentials recorded in response to depolarizing current steps displayed repetitive spiking with increasing frequency, reaching a plateau at about 140 Hz" [5]
> "Membrane capacitance (pF): Newly generated 42.3 (10.2); Mature 99.2 (12.7); P=0.003" [5]
> "newly generated granule cells are functionally integrated into the circuitry by 4 weeks" [5]

## GABA is depolarising and excitatory in neuroblasts and immature granule neurons

A recurring finding across three primary patch-clamp studies is that GABA acts as a depolarising, excitatory transmitter on dg_neuroblast and dg_immature_granule_neuron stages due to NKCC1-dominated chloride homeostasis.

Tozuka et al. 2005 [abstract, 3] used GFP-targeted recordings from type-2 progenitors in nestin-GFP mice and established that these cells (the dg_neuroblast equivalent) receive direct GABAergic but not glutamatergic inputs:

> "neuronal progenitor (type-2) cells receive active direct neural inputs from the hippocampal circuitry" [3]
> "This input was GABAergic but not glutamatergic." [3]
> "The GABAergic inputs depolarized type-2 cells because of their elevated [Cl(-)](i)." [3]

Ge et al. 2006 [PMC fulltext, 1] characterise the molecular mechanism: DCX+ neurons have high NKCC1 and low KCC2, and knockdown of NKCC1 impairs dendritic arborisation, linking the depolarised EGABA to morphological maturation:

> "newborn DGCs (DCX+) in the adult brain express high levels of NKCC1 and little KCC2" [1]
> "GABA exerts a depolarising action during the initial development of new DGCs" [1]
> "newborn neurons in the adult brain...follow a stereotypical integration process-receiving tonic GABA activation first, followed by GABAergic synaptic inputs and finally glutamatergic synaptic inputs" [1]
> "shRNA-NKCC1+ DGCs exhibited significant defects in their dendritic arborisation" [1]

Espósito et al. 2005 [PMC fulltext, 2] further resolve the GABA input into two components with distinct reversal potentials, reflecting a somatic-to-dendritic chloride gradient in the immature neuron:

> "Current-voltage curves revealed two components with similar conductance (Gmax): an early current with a depolarized EGABA (-30.9 ± 1.6 mV; n = 9) and fast kinetics and a late current with a more hyperpolarized EGABA and slow kinetics (-44.5 ± 2.1 mV; n = 12)." [2]
> "GABAergic-evoked PSCs displayed a reversal potential (EGABA) of -26.9 ± 1.9 mV." [2]

## Enhanced excitability and lowered LTP threshold in immature granule neurons

Schmidt-Hieber et al. 2004 [abstract, 4] provide the key evidence that immature granule cells are functionally distinct from mature cells through enhanced synaptic plasticity mechanisms:

> "young granule cells in the adult hippocampus have substantially different active and passive membrane properties from mature cells" [4]
> "Young neurons express T-type Ca2+ channels, which are able to generate isolated calcium spikes and to amplify fast sodium action potentials" [4]
> "Associative long-term potentiation can be induced more easily in young neurons than in mature neurons under identical conditions" [4]
> "newly generated neurons express unique mechanisms to facilitate synaptic plasticity, which may be important for the formation of new memories" [4]

Background/report-derived support for enhanced excitability comes from depth_0 review material: the Stoll 2014 review [asta_report] states that "Immature neurons are highly excitable, so newly-born cells are thought to affect the dynamic properties of existing networks to which they are recruited." (CorpusId:8479504), and the depth_0 europepmc Zhao 2006 Discussion (CorpusId:18166210) notes that "Immature neurons have also been shown to have a lower threshold for long-term potentiation induction." These are consistent with the primary patch-clamp evidence above.

## Marker progression and stage identity across the neuroblast -> immature -> mature axis

The sequential marker cascade underlying the three nodes is supported in the summaries primarily by depth_0 report-derived content [asta_report]; all primary electrophysiology papers cite markers only to confirm stage identity of their recorded cells. Key report-level statements include: Stepien 2021 (CorpusId:245432259, asta_report) describing neuroblasts as DCX+/Ki67+ and immature neurons as DCX+/PSA-NCAM+/NeuN+; the Bonfanti/Peretto survey (CorpusId:279046466, asta_report) describing the type-2a (Nestin+/Sox2+) -> type-2b (Nestin+/DCX+) -> type-3 (DCX+) -> stage-5 (DCX+/NeuN+) -> stage-6 (Calbindin+/NeuN+) progression; Hodge 2008 (CorpusId:15727849, asta_report) adding Tbr2 as an intermediate progenitor marker with 96.76% co-expression with Nestin-GFP and 64.4% with DCX, and Tbr1 restricted to postmitotic granule cells; and Merz 2013 (CorpusId:14598082, asta_report) confirming that "DCX is almost exclusively expressed by immature newborn neurons in the DG and the SVZ/OB-system and is commonly used to distinguish immature neurons from non-neuronally committed precursors and mature neurons, and to estimate neurogenic activity." These report-derived claims are consistent with each other and with the node context marker panels but are not primary citations in the paper_catalogue.

Calretinin-to-calbindin switching distinguishes dg_immature_granule_neuron from dg_mature_granule_neuron. Depth_0 evidence (Dayer 2005, CorpusId:15994456, asta_report) explicitly suggests that "new interneurons make a developmental switch from CR to CB expression like the adult-born dentate gyrus granule neurons" (part of a longer triple-label observation), aligning the mature node's calbindin+ identity with the immature node's transient calretinin+ phenotype. This is contextual report content rather than primary data.

The primary electrophysiology papers cited above also tie stage markers to recorded cells: van Praag 2002 [5] and Espósito 2005 [2] use retroviral GFP to target newborn neurons, Ge 2006 [1] identifies recorded cells as DCX+ by post hoc staining, and Tozuka 2005 [3] uses nestin-GFP to target type-2 neuroblast-equivalent progenitors.

## Morphological and circuit integration timeline (supporting evidence)

Morphological maturation of dg_immature_granule_neuron is documented in depth_0 europepmc_fulltext content from Zhao 2006 (CorpusId:18166210), including apical dendrites reaching the inner molecular layer at 10 dpi, the middle molecular layer at 14 dpi, and the edge of the molecular layer by 21 dpi, with spine formation starting at ~16 dpi and axons reaching CA3 at 10-11 dpi. These observations are consistent with the electrophysiological milestones (glutamatergic input acquisition at 14-18 dpi [1, 2]) from the catalogued primary papers. Because Zhao 2006 is not in the final paper_catalogue it is cited by CorpusId rather than numbered reference here; verification of these milestones against the primary source is recommended before ingestion.

## Species specificity

All five catalogued primary electrophysiology papers were conducted in mouse (predominantly adult C57BL/6): van Praag 2002 [5], Espósito 2005 [2], Ge 2006 [1], Schmidt-Hieber 2004 [4] (mouse hippocampus), and Tozuka 2005 [3] (nestin-GFP transgenic mouse). No rat patch-clamp data are present in the catalogued set. Report-derived (asta_report) depth_0 material notes primate-vs-rodent differences in immature granule cell abundance (CorpusId:279046466: "The primate hippocampus has a longer maturation period of newly generated granule cells (GCs) and a higher percentage of immature dentate GCs, compared with rodents.") but the core electrophysiological and synaptic integration data in the catalogued papers are mouse-only.

## Evidence gaps for dg_neuroblast, dg_immature_granule_neuron, dg_mature_granule_neuron

- **defining_markers:** yes (primary papers confirm DCX+/Nestin+ neuroblast, DCX+/NeuN+ immature, Calbindin+/NeuN+ mature; largely report-derived but internally consistent).
- **anatomical_location:** partial. SGZ and inner GCL are named in multiple sources, but the explicit UBERON term for the subgranular zone is not provided by any summary - gap remains open.
- **nt_type:** yes for dg_mature_granule_neuron (glutamatergic; EAAC-1 expression noted in depth_0 Dayer 2005 and Bartkowska 2022; glutamatergic PSCs recorded from mature adult-born cells in [2, 5]). For dg_immature_granule_neuron, glutamatergic fate commitment is implicit (cells acquire glutamatergic synaptic output by >=18 dpi). For dg_neuroblast, pre-synaptic commitment is described but no outgoing glutamate release is documented in the catalogued set.
- **electrophysiology_class:** partial -> substantially filled by this review. For dg_neuroblast: tonic GABA responsiveness from >=3 dpi [1], silent for synaptic output until 7 dpi [1, 2], GABA-depolarised via high NKCC1 [1, 3], with high Rin (~4.3 GΩ) and small Cm (~6.4 pF) [2]. For dg_immature_granule_neuron: slow dendritic GABAergic PSCs by 7-8 dpi [1, 2], glutamatergic PSCs by 14-18 dpi [1, 2], depolarised EGABA (-26.9 to -44.5 mV) [2], T-type Ca2+ channels and enhanced LTP [4], and transitional passive properties (Cm 11.7-24.6 pF, Vrest -45 to -63 mV) [2]. For dg_mature_granule_neuron: repetitive firing up to ~140 Hz, Vth ~-43 to -45.8 mV, Cm ~99 pF, tau_m ~33.7 ms, Vrest ~-74.8 mV [5]. Remaining gaps: formal firing-pattern classification (regular spiking, adapting, etc.) is only loosely described as "conspicuous after hyperpolarization and frequency adaptation" [5]; species-specific ephys values for rat are not available.
- **morphology_notes:** partial. Axon reaches CA3 at 10-11 dpi; dendrites reach outer molecular layer by 21 dpi; spine density rises from 0.43 to 2.61 spines/um between 21-56 dpi - but this is from depth_0 europepmc content (Zhao 2006, CorpusId:18166210) not in paper_catalogue. The Cm/tau_m differences in [5] are consistent with morphological differences but do not describe dendritic arbor shape.
- **neuropeptides:** no. No neuropeptide data appear in any summary across the full evidence set, and the run_manifest confirms this for the five catalogued primary patch-clamp papers. Neuropeptide content is a confirmed open gap for all three nodes.
- **electrophysiology species coverage:** no rat ephys data in the catalogued primary evidence; the species-per-assertion gap for rat remains open.
- **SGZ UBERON term:** not supplied by any summary.

## New classical types encountered

- **Type-2a neural progenitor cell (Nestin+/Sox2+, DCX-):** described as a distinct population upstream of the DCX+ neuroblast in the adult DG SGZ (CorpusId:279046466, asta_report; CorpusId:15727849, asta_report - Hodge 2008 characterises Tbr2 co-expression in these IPCs). Not already represented in the three NODE_IDS. **Suggested action: add stub** (dg_type2a_progenitor). Note: draft files for dg_type2a_progenitor/dg_type2b_progenitor already appear in the repo under kb/dentate_gyrus/traversal_output/20260414_dentate_gyrus_report_ingest/, so this may already be in progress - verify before creating duplicates.
- **Type-2b intermediate progenitor (Nestin+/DCX+, Tbr2+):** transitional between type-2a and neuroblast; characterised in Hodge 2008 asta_report (96.76% Tbr2+/nestin-GFP+ co-expression in SGZ) and CorpusId:279046466. **Suggested action: add stub if not present** (draft may already exist).
- **Type-1 radial glia-like stem cell (GFAP+/Sox2+/Nestin+):** upstream of the neuroblast in multiple depth_0 asta_reports (CorpusId:245432259, CorpusId:8479504, CorpusId:14221248). **Suggested action: defer** - upstream of the immediate lineage-of-interest, likely a separate stem cell KB node.
- **Adult-born olfactory bulb granule cell (GABAergic):** CorpusId:625292 (LOW relevance). Distinct from DG granule cell (different neurotransmitter, different region). **Suggested action: defer** - out of region scope.
- **Piriform cortex immature DCX+ neuron (semilunar-pyramidal transitional):** CorpusId:235300723, CorpusId:13799502 (MODERATE relevance, asta_report). Cross-regional analogue. **Suggested action: defer** - not part of DG region.
- **Adult neocortical DCX+ interneuron (calretinin -> calbindin switching):** CorpusId:15994456 (MODERATE, asta_report). Cross-regional context for the CR-to-CB switch also seen in DG granule cells. **Suggested action: already covered by existing DG nodes' marker progression context** - no new DG node needed.

## References

[1] Ge, Goh, Sailor, Kitabatake, Ming, Song (2006). GABA regulates synaptic integration of newly generated neurons in the adult brain. *Nature*. CorpusId:4378008
[2] Esposito, Piatti, Laplagne, Morgenstern, Ferrari, Pitossi, Schinder (2005). Neuronal differentiation in the adult hippocampus recapitulates embryonic development. *Journal of Neuroscience*. CorpusId:38501311
[3] Tozuka, Fukuda, Namba, Seki, Hisatsune (2005). GABAergic excitation promotes neuronal differentiation in adult hippocampal progenitor cells. *Neuron*. CorpusId:3154810
[4] Schmidt-Hieber, Jonas, Bischofberger (2004). Enhanced synaptic plasticity in newly generated granule cells of the adult hippocampus. *Nature*. CorpusId:4332735
[5] van Praag, Schinder, Christie, Toni, Palmer, Gage (2002). Functional neurogenesis in the adult hippocampus. *Nature*. CorpusId:4403779
