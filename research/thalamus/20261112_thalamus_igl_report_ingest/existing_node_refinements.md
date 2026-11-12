# Proposed refinements to the existing node `lgv_igl_gabaergic_neuron`

Source: ASTA deep research report `inputs/deepsearch/IGL.pdf` (focused IGL report).
Quotes are in `extracted_quotes.json` in this directory. **The existing node has not been edited.** These are suggestions for curator review.

## 1. IGL is GABAergic at population level (supports existing nt_type for the IGL part)
- Blasiak et al., 2004: "Many, if not all, neurons of the suprachiasmatic nucleus and intergeniculate leaflet contain GABA".
- Palus et al., 2015: "all IGL cells express the γ-aminobutyric acid (GABA) (Moore et al., 1993)".
- Blasiak et al._1, 2013: "The most abundant neurotransmitter synthesized by IGL neurons is c-aminobutyric acid".
- Action: add these as `nt_type.sources` for the IGL `anatomical_location` entry. At present the only source for the IGL location is the embryonic Govek et al. 2022 lineage paper.

## 2. Anatomy: IGL position and its relation to LGv (supports pooling LGv+IGL at this coarse level)
- Chrobok et al., 2016: IGL is "a flat retinorecipient thalamic structure ... historically considered to be a subdivision of the neighboring ventrolateral geniculate nucleus (VLG)".
- Palus et al., 2015 / Palus-Chramiec et al., 2019: located between the dorsal and ventral parts of the LGN.
- Pu et al., 1996 (cat): SCN-projecting neurons in the medial vLGN, which is proposed as a homologue of the rodent IGL.
- Blasiak et al._1, 2013: rodent IGL is a homologue of the primate pregeniculate nucleus.
- Action: add as sources/notes on the IGL `anatomical_location` entry. Record the cross-species homology (cat medial vLGN, primate pregeniculate nucleus) in `notes`.

## 3. Heterogeneity notes, LGv side (Sabbagh et al., 2020; mouse)
- vLGN contains transcriptomically distinct GABAergic types in the retinorecipient external lamina (vLGNe) and the non-retinorecipient internal lamina (vLGNi).
- vLGNe has four adjacent subtype-specific sublaminae. Cells in each sublamina receive monosynaptic retinal input, shown by trans-synaptic tracing and in vitro electrophysiology.
- Spp1+ and Pvalb+ are named as markers that split vLGN populations.
- The report notes that these vLGN types cannot yet be mapped one-to-one onto the IGL classes (ENK, NPY, Type I/II/III).
- Action: extend the existing "SUSPECTED HETEROGENEITY" note. This is the strongest candidate basis for future LGv-specific child nodes, such as vLGNe vs vLGNi GABAergic neurons. Those nodes are out of scope for this IGL report.
- Caveat: Gouwens et al., 2020 is about cortical interneurons and is cited only for methodology. Do not use it as a source for this node.

## 4. Additional IGL heterogeneity to note on the coarse node or on the IGL child
- Blasiak et al._1, 2013: "In the rat IGL, a third cell group is present with unknown neurotransmitter content (Moore & Card, 1994)".
- Thankachan et al., 2005: three juxtacellularly defined classes (Type I/II/III) in the "IGL/VLG". The anatomy crosses the IGL/LGv boundary, so this fits the coarse node as well as the IGL child.
- Recommendation: put the detail on the new `igl_gabaergic_neuron`. Leave only a pointer on the coarse node.

## 5. Species
- The IGL evidence is almost all rat. Cat appears only as a homology note. The existing node's evidence is mouse.
- Action: when the species field is filled, record the mixed rat and mouse basis in `notes`.

## 6. Retinorecipient / circadian function (description-level)
- Lewandowski et al., 2004 / Chrobok et al., 2017: the IGL is retinorecipient and part of the circadian timing system, and network oscillations depend on retinal input.
- Action: optional addition to the node description or notes. It fits both LGv (Sabbagh: retinorecipient vLGNe) and IGL.
