from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'https://bican.org/schema/celltype-evidence/v0.5/',
     'default_range': 'string',
     'description': 'Evidence graph schema for mapping cell types from the '
                    'literature (classical and transcriptomic) to community '
                    'single-cell and spatial transcriptomic atlases.\n',
     'id': 'https://bican.org/schema/celltype-evidence/v0.5',
     'imports': ['linkml:types'],
     'name': 'CellTypeEvidence',
     'prefixes': {'ABAO': {'prefix_prefix': 'ABAO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ABAO_'},
                  'BFO': {'prefix_prefix': 'BFO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/BFO_'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'DHBA': {'prefix_prefix': 'DHBA',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/DHBA_'},
                  'DOI': {'prefix_prefix': 'DOI',
                          'prefix_reference': 'https://doi.org/'},
                  'GEO': {'prefix_prefix': 'GEO',
                          'prefix_reference': 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='},
                  'HBA': {'prefix_prefix': 'HBA',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/HBA_'},
                  'HGNC': {'prefix_prefix': 'HGNC',
                           'prefix_reference': 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/'},
                  'HOMBA': {'prefix_prefix': 'HOMBA',
                            'prefix_reference': 'https://purl.brain-bican.org/ontology/homba/HOMBA_'},
                  'MBA': {'prefix_prefix': 'MBA',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/MBA_'},
                  'NCBIGene': {'prefix_prefix': 'NCBIGene',
                               'prefix_reference': 'https://www.ncbi.nlm.nih.gov/gene/'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'PMID': {'prefix_prefix': 'PMID',
                           'prefix_reference': 'https://pubmed.ncbi.nlm.nih.gov/'},
                  'SCP': {'prefix_prefix': 'SCP',
                          'prefix_reference': 'https://singlecell.broadinstitute.org/single_cell/study/'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'WMB': {'prefix_prefix': 'WMB',
                          'prefix_reference': 'https://allen-brain-cell-atlas.s3.us-west-2.amazonaws.com/metadata/WMB-taxonomy/20231215/cell_set_information.csv#'},
                  'evidencell': {'prefix_prefix': 'evidencell',
                                 'prefix_reference': 'https://w3id.org/evidencell/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'semapv': {'prefix_prefix': 'semapv',
                             'prefix_reference': 'https://w3id.org/semapv/vocab/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'}},
     'source_file': 'schema/celltype_mapping.yaml'} )

class CLClassTerm(str):
    """
    Any term in the Cell Ontology (CL) reachable from CL:0000000 (cell) via subClassOf. Used as the binding range for cl_term, cl_terms, and parent_cl_term slots.

    """
    pass


class NCBITaxonClassTerm(str):
    """
    Any taxon in NCBITaxon reachable from NCBITaxon:1 (root) via subClassOf. Used as the binding range for species, source_species, and target_species slots.

    """
    pass


class AnatomyTerm(str):
    """
    Any anatomical term reachable from UBERON:0001062 (anatomical entity) via subClassOf or part_of. Covers UBERON plus the brain-bican atlas ontologies (MBA, DHBA, HOMBA) — all three carry is_a / part_of links that bottom out at UBERON, so a single source_node suffices. Used as the binding range for anatomical_location, anatomical_region, projection_target, and brain_region slots.

    """
    pass


class DefinitionBasis(str, Enum):
    """
    What kind of evidence was used to define this cell type node.

    """
    CLASSICAL_MORPHOLOGICAL = "CLASSICAL_MORPHOLOGICAL"
    """
    Defined primarily by morphological criteria (soma shape, dendrite/axon pattern)
    """
    CLASSICAL_ELECTROPHYSIOLOGICAL = "CLASSICAL_ELECTROPHYSIOLOGICAL"
    """
    Defined primarily by electrophysiological properties
    """
    CLASSICAL_NEUROCHEMICAL = "CLASSICAL_NEUROCHEMICAL"
    """
    Defined by neurotransmitter, neuropeptide, or IHC marker expression
    """
    CLASSICAL_ANATOMICAL = "CLASSICAL_ANATOMICAL"
    """
    Defined primarily by anatomical location and projection targets
    """
    CLASSICAL_MULTIMODAL = "CLASSICAL_MULTIMODAL"
    """
    Classical type defined by combination of morphology, location, electrophysiology, neurochemistry
    """
    PRIOR_TRANSCRIPTOMIC = "PRIOR_TRANSCRIPTOMIC"
    """
    Transcriptomic type from a prior publication or dataset (not the community target atlas). Identified by a cluster label in a specific dataset (e.g. PLI3 in Osorno SCP795).

    """
    ATLAS_TRANSCRIPTOMIC = "ATLAS_TRANSCRIPTOMIC"
    """
    Cell type from the community target atlas (or a named reference atlas). Identified by a CCN cell_set_accession.

    """
    MULTIMODAL_EMERGING = "MULTIMODAL_EMERGING"
    """
    A type description being built up from multiple evidence types; may eventually become a new or revised CL term. Not yet anchored to a single classical or T-type definition.

    """


class SexBias(str, Enum):
    """
    Expected direction of sexual dimorphism in cell number or marker expression for a classical cell type. Used by find-candidates to score atlas clusters whose male_female_ratio matches the expected direction.

    """
    MALE_BIASED = "MALE_BIASED"
    """
    More cells (or higher expression) in males than females
    """
    FEMALE_BIASED = "FEMALE_BIASED"
    """
    More cells (or higher expression) in females than males
    """
    NOT_DIMORPHIC = "NOT_DIMORPHIC"
    """
    No documented sex difference in cell number or defining markers
    """


class SynonymType(str, Enum):
    """
    Category of alternative name for a cell type.
    """
    ABBREVIATION = "ABBREVIATION"
    """
    Short form or acronym, e.g. "OLM" for "oriens-lacunosum moleculare"
    """
    HISTORICAL = "HISTORICAL"
    """
    Deprecated or superseded name still found in older literature
    """
    ATLAS_LABEL = "ATLAS_LABEL"
    """
    An atlas cluster or cell set label used as a cell type name in papers (e.g. "Sst Gaba_3" used to refer to OLM cells in an atlas-integrated study)

    """
    CROSS_SPECIES = "CROSS_SPECIES"
    """
    Name used for the equivalent type in a different species
    """
    INFORMAL = "INFORMAL"
    """
    Community-specific colloquial term not formally defined in a publication
    """


class MappingRelationship(str, Enum):
    """
    The nature of the correspondence between lit_type and taxonomy_type in this edge. Relationships are directional, from lit_type to taxonomy_type. Permissible-value identifiers are CURIEs binding to SKOS predicates where applicable; custom evidencell: predicates otherwise.

    """
    skosCOLONexactMatch = "skos:exactMatch"
    """
    The lit_type and taxonomy_type describe the same cell population (one-to-one identity). Required: cardinality 1:1; location consistent (classical region + adjacent only, not distant); AT supports 1:1 (F1 > 0.75) when AT is present; no major contradictions. AT-absent cases may still be exactMatch on converging location + markers + literature, but confidence ceiling drops to MODERATE. Numeric AT gate lives in the report-time prompt + rationale, not in this description.

    """
    skosCOLONcloseMatch = "skos:closeMatch"
    """
    Same 1:1-style correspondence as exactMatch but with one or more contradictions: marker mismatch with no resolving heterogeneity in the lit, soft AT (F1 in a borderline band or coverage/purity asymmetry), location edge case, or other partial-information caveat. Pair with mapping_justification: semapv:UnreviewedManualMapping when not curator-confirmed.

    """
    skosCOLONbroadMatch = "skos:broadMatch"
    """
    The lit_type is **narrower** than the taxonomy_type; the match goes *to* the broader thing. Read `lit_OLM --skos:broadMatch--> Sst_Gaba_3_supertype` as "OLM has a broad match — the supertype is the broader thing." Apply when: the taxonomy_type is located in regions distant from the classical region + adjacent set; or the relationship is cross-cutting at rank N but collapses to a clean broader relation at rank N+1 (pick the higher rank); or multiple lit_types map to a single taxonomy_type at this rank. AT must be consistent with the broader reading when present. Always paired with `mapping_cardinality: 1:n` (the hidden-1:1 case collapses: if the specific sub-cluster is TBD, map at the next rank up).

    """
    skosCOLONnarrowMatch = "skos:narrowMatch"
    """
    The lit_type is **broader** than the taxonomy_type; the match goes *to* the narrower thing. Read `lit_classical_basket --skos:narrowMatch--> mli2_cluster` as "classical basket has a narrow match — this specific cluster is the narrower thing." Symmetric inverse of broadMatch. Always paired with `mapping_cardinality: n:1`.

    """
    evidencellCOLONPartialOverlapMatch = "evidencell:PartialOverlapMatch"
    """
    DEPRECATED (2026-05-26). Absorbed into closeMatch (1:1-ish with contradictions) + broadMatch / narrowMatch / CrossCuttingMatch per the new predicate rubric. Retained transitionally so the KB validates against the deprecated value during migration; the re-run will re-predicate the existing 42 edges. Do not emit on new edges. Will be removed after migration.

    """
    evidencellCOLONCrossCuttingMatch = "evidencell:CrossCuttingMatch"
    """
    The taxonomy_type cross-cuts the boundary of the lit_type (and usually at least one other lit_type). The transcriptomic type captures cells that the classical taxonomy would assign to multiple distinct types. E.g. MLI1 cuts across classical basket and stellate cells. Apply only when no higher rank rescues the relationship to a clean broadMatch — if cross-cutting at rank N collapses to a single broader type at rank N+1, prefer broadMatch at N+1. No SKOS equivalent.

    """
    evidencellCOLONNoCorrespondence = "evidencell:NoCorrespondence"
    """
    No corresponding type exists in the target taxonomy. Use to explicitly document failures of correspondence (e.g. a curated literature type that the atlas does not resolve at any rank). No SKOS equivalent.

    """
    evidencellCOLONUncertainRelationship = "evidencell:UncertainRelationship"
    """
    The kind of correspondence is not yet determinable from available evidence. Distinct from `evidencell:NoCorrespondence` (which asserts no mapping exists). Pair with `mapping_justification: semapv:UnspecifiedMatching` and a `reconciliation_note` describing what additional evidence would resolve the question. No SKOS equivalent.

    """


class MappingCardinality(str, Enum):
    """
    Cardinality of the mapping considered as a set relation. Required with skos:broadMatch (always 1:n) and skos:narrowMatch (always n:1); recommended with skos:exactMatch (always 1:1). The former hidden-1:1 broadMatch case collapses: if the specific sub-cluster is not yet identifiable, map at the next rank up where the relationship is cleanly 1:n.

    """
    number_1COLON1 = "1:1"
    """
    One lit_type maps to one taxonomy_type.
    """
    number_1COLONn = "1:n"
    """
    One lit_type splits across multiple taxonomy_types.
    """
    nCOLON1 = "n:1"
    """
    Multiple lit_types collapse onto one taxonomy_type.
    """


class MappingJustification(str, Enum):
    """
    Provenance of the mapping decision. Bound to the semapv mapping provenance vocabulary; SSSOM-compatible.

    """
    semapvCOLONManualMappingCuration = "semapv:ManualMappingCuration"
    """
    Mapping reviewed and approved by a human curator.
    """
    semapvCOLONUnreviewedManualMapping = "semapv:UnreviewedManualMapping"
    """
    Manually proposed (typically agent-emitted from extraction or synthesis) but not yet reviewed by a curator. The default state for new edges in this KB.

    """
    semapvCOLONLexicalMatching = "semapv:LexicalMatching"
    """
    Mapping derived from name / synonym lexical match. Lowest confidence among manual-class justifications.

    """
    semapvCOLONCompositeMatching = "semapv:CompositeMatching"
    """
    Mapping derived from multi-source evidence integration (e.g. anatomy + markers + AT F1 all converging).

    """
    semapvCOLONLogicalReasoning = "semapv:LogicalReasoning"
    """
    Mapping derived by logical reasoning over schema-encoded relations.

    """
    semapvCOLONUnspecifiedMatching = "semapv:UnspecifiedMatching"
    """
    Provenance not recorded. Use sparingly; prefer one of the other values when known.

    """


class MappingConfidence(str, Enum):
    HIGH = "HIGH"
    """
    Strong experimental anchor with no major contradictions. Two standard paths: (a) patch-seq annotation-transfer F1 > 0.75 with marker confirmation; (b) bridging or bulk RNA-seq with strong structure/function convergence at similar strength. Default for a clean exactMatch where AT is present and supportive.

    """
    MODERATE = "MODERATE"
    """
    Two or more independent evidence items with consistent support
    """
    LOW = "LOW"
    """
    Single evidence item or consistent but weak/indirect evidence
    """
    UNCERTAIN = "UNCERTAIN"
    """
    Evidence is contradictory, ambiguous, or minimal
    """
    REFUTED = "REFUTED"
    """
    Preponderance of evidence argues against this mapping
    """


class CorrespondenceType(str, Enum):
    """
    Nature of the correspondence declared by an AtSourceSet between an external dataset's annotated cell set and a classical cell type.

    """
    EXACT = "EXACT"
    """
    Source cluster is the classical type (clean identity).
    """
    PARTIAL = "PARTIAL"
    """
    Overlapping but imperfect correspondence.
    """
    SUPERSET = "SUPERSET"
    """
    Source cluster is broader than the classical type.
    """
    SUBSET = "SUBSET"
    """
    Source cluster is one molecular subtype within the classical type (e.g. one of several Foxp2 ITC clusters within intercalated cell).

    """


class EvidenceSupport(str, Enum):
    SUPPORT = "SUPPORT"
    REFUTE = "REFUTE"
    PARTIAL = "PARTIAL"
    """
    Supports some aspects but not all
    """
    WEAK = "WEAK"
    """
    Non-zero but weak evidence — e.g. marker match with anatomical mismatch, or a speculative assignment retained as placeholder.

    """
    NO_EVIDENCE = "NO_EVIDENCE"
    """
    Assessed but no relevant evidence found
    """


class EvidenceType(str, Enum):
    LITERATURE = "LITERATURE"
    """
    Peer-reviewed paper (classical anatomy, electrophysiology, prior transcriptomics)
    """
    ATLAS_METADATA = "ATLAS_METADATA"
    """
    Data taken directly from an atlas cluster metadata spreadsheet / taxonomy: markers, MERFISH location, NT type, CCF distribution.

    """
    ANNOTATION_TRANSFER = "ANNOTATION_TRANSFER"
    """
    Computational label transfer (MapMyCells, Seurat, scANVI, etc.)
    """
    SPATIAL_COLOCATION = "SPATIAL_COLOCATION"
    """
    Spatial transcriptomics or FISH-based co-location analysis
    """
    PATCH_SEQ = "PATCH_SEQ"
    """
    Patch-seq multi-modal data (electrophysiology + morphology + transcriptomics)
    """
    PROJECTION_SEQ = "PROJECTION_SEQ"
    """
    Transcriptomics combined with retrograde tracing (proj-seq)
    """
    ELECTROPHYSIOLOGY = "ELECTROPHYSIOLOGY"
    """
    Electrophysiology recordings without transcriptomics
    """
    MORPHOLOGY = "MORPHOLOGY"
    """
    Morphological characterisation (light microscopy, EM)
    """
    MARKER_ANALYSIS = "MARKER_ANALYSIS"
    """
    Custom marker gene overlap analysis beyond atlas metadata
    """
    ATLAS_QUERY = "ATLAS_QUERY"
    """
    Curator-performed interactive query against a published atlas browser (ABC Atlas, Allen Brain Map, BICCN viewer, etc.) with specified filters. Result is observation-level evidence: reproducible given the same atlas version and filter parameters. Stronger than an informal note but weaker than a peer-reviewed publication. Record the query URL and atlas version.

    """
    BULK_CORRELATION = "BULK_CORRELATION"
    """
    Cluster ranking from a paired-bulk transcriptomic correlation run. Two bulk pools (e.g. region A vs region B) are correlated against atlas cluster pseudobulks; the differential signal δ = ρ_A − ρ_B identifies clusters specifically tracking pool A. Backing record: a CorrelationRun (kb/correlation_runs/{run_id}/manifest.yaml) referenced by run_ref.

    """


class MarkerType(str, Enum):
    """
    The molecule type detected in a marker evidence source. Currently covers the two most important categories (protein vs transcript); could be extended in future to other molecule types where these are used as cell type markers (e.g. glycoproteins, lipids, metabolites) if such cases become relevant to atlas mappings.

    """
    PROTEIN = "PROTEIN"
    """
    Protein-level detection: IHC, immunofluorescence, western blot, proximity ligation assay, mass spectrometry.

    """
    TRANSCRIPT = "TRANSCRIPT"
    """
    Transcript-level detection: bulk RNA-seq, scRNA-seq, snRNA-seq, smFISH, RNAscope, MERFISH, Visium, or other spatial transcriptomics.

    """


class CellCompartment(str, Enum):
    """
    Which cellular compartment an anatomical location refers to. Critical for interpreting spatial data: MERFISH records soma position only; axonal/dendritic targets require other methods.

    """
    SOMA = "SOMA"
    """
    Cell body location
    """
    AXON_TARGET = "AXON_TARGET"
    """
    Axonal projection target region
    """
    DENDRITE = "DENDRITE"
    """
    Dendritic arbor region
    """


class MarkerCategory(str, Enum):
    """
    Functional category of a marker gene in the context of a cell type description. Used on GeneDescriptor.category to distinguish marker roles in the unified markers list. Negative markers use modifier: ABSENT rather than a separate category.

    """
    DEFINING = "DEFINING"
    """
    Global defining markers — discriminate this type across the full taxonomy (e.g. cluster_markers_combo in WMBv1).

    """
    DEFINING_SCOPED = "DEFINING_SCOPED"
    """
    Within-subclass or within-supertype scoped markers — most informative within a narrower comparison context (e.g. cluster_markers_combo_within_subclass).

    """
    TF = "TF"
    """
    Transcription factor markers (e.g. cluster_TF_markers_combo in WMBv1).
    """
    NEUROPEPTIDE = "NEUROPEPTIDE"
    """
    Neuropeptide co-transmitter markers. Pair with expression_score where available (e.g. from np_markers precomputed stats: Vip:9.2).

    """
    NT_MARKER = "NT_MARKER"
    """
    Genes providing evidence for the neurotransmitter type assertion: Gad1/Gad2 (GABA), Slc17a6/Slc17a7 (glutamate), Th (dopamine), Slc6a4 (serotonin), etc. Populate on classical nodes where NT type is inferred from marker expression rather than direct physiology.

    """
    MERFISH = "MERFISH"
    """
    MERFISH spatial transcriptomics panel markers — distinguish this type in the spatial panel (e.g. merfish_markers_combo in WMBv1).

    """


class PropertyAlignment(str, Enum):
    """
    How well a specific property aligns between type_a and type_b on a mapping edge. Used in PropertyComparison to make the basis for confidence judgments machine-readable.

    """
    CONSISTENT = "CONSISTENT"
    """
    Properties agree: same value or biologically equivalent, modulo naming conventions. E.g. "GABA-Glut" vs "Glut-GABA" (same dual-transmitter biology, different ordering).

    """
    APPROXIMATE = "APPROXIMATE"
    """
    Properties broadly agree but differ in resolution, specificity, species convention, or one is a subset of the other. E.g. "GPi shell region" (classical) vs atlas-annotated "GPi"; Sst in classical description vs Sst in 2/3 atlas clusters.

    """
    DISCORDANT = "DISCORDANT"
    """
    Properties conflict — constitutes evidence against the mapping. Document in PropertyComparison.notes and consider adding a Caveat.

    """
    NOT_ASSESSED = "NOT_ASSESSED"
    """
    Property not evaluated for this edge (data unavailable or not relevant to this mapping).

    """


class CLMappingType(str, Enum):
    """
    Whether the CL term on this node is an exact match or a broad ancestor. Mirrors SKOS mapping predicates (skos:exactMatch, skos:broadMatch).

    """
    EXACT = "EXACT"
    """
    This node IS this CL term, modulo species restriction. The CL term may be defined at species-neutral level; the node represents a species-specific instance. E.g. CL:0000617 GABAergic neuron — EXACT for a node that is clearly and fully described by this term.

    """
    BROAD = "BROAD"
    """
    This node is a subtype of this CL term; the CL term is an ancestor. The ProposedCLTerm on this node (if present) would be a new child of the CL term, extending the ontology. E.g. CL:0000679 (glutamatergic neuron) is a BROAD match for a Lugaro cell — a new CL term for Lugaro cell would be placed under it.

    """
    RELATED = "RELATED"
    """
    The CL term is related but neither exact nor strictly an ancestor. Use for partial overlaps or uncertain relationships with existing terms.

    """


class CaveatType(str, Enum):
    MERFISH_REGISTRATION_UNCERTAINTY = "MERFISH_REGISTRATION_UNCERTAINTY"
    """
    Anatomical location inferred from MERFISH CCF registration, which may be inaccurate
    """
    LOW_CELL_COUNT = "LOW_CELL_COUNT"
    """
    Fewer than ~50 cells used in this analysis; results may not be robust
    """
    DISTRIBUTED_ACROSS_CLUSTERS = "DISTRIBUTED_ACROSS_CLUSTERS"
    """
    Source type cells are spread across multiple target clusters (low coverage at finest level)
    """
    TAXONOMY_LEVEL_MISMATCH = "TAXONOMY_LEVEL_MISMATCH"
    """
    Best mapping is at a coarser taxonomy level than desired (e.g. supertype not cluster)
    """
    MARKER_NOT_SPECIFIC = "MARKER_NOT_SPECIFIC"
    """
    Defining marker(s) are not unique to this cell type in the atlas
    """
    CROSS_SPECIES_EXTRAPOLATION = "CROSS_SPECIES_EXTRAPOLATION"
    """
    Evidence is from a different species than the atlas being mapped to
    """
    SINGLE_DATASET = "SINGLE_DATASET"
    """
    Evidence comes from a single dataset; independent replication not yet available
    """
    NT_PREDICTION_UNCERTAIN = "NT_PREDICTION_UNCERTAIN"
    """
    NT type from atlas may be unreliable (e.g. nuclear RNA depletion in snRNA-seq)
    """
    PRIOR_MAPPING_ASSUMED = "PRIOR_MAPPING_ASSUMED"
    """
    This edge relies on a prior mapping step whose confidence is UNCERTAIN or LOW
    """
    AMBIGUOUS_MAPPING = "AMBIGUOUS_MAPPING"
    """
    Multiple possible target types; mapping is not clearly one-to-one. Use when the classical type spans several atlas clusters without a dominant match.

    """
    SINGLE_STUDY = "SINGLE_STUDY"
    """
    Evidence for this mapping comes from a single study (broader than SINGLE_DATASET — covers the case where independent replication is absent even with multiple datasets from one lab).

    """
    NO_DISCRIMINATING_MARKER = "NO_DISCRIMINATING_MARKER"
    """
    No single marker uniquely identifies this classical type in the atlas; mapping relies on marker combinations or other evidence.

    """
    DISCORDANT_ANATOMY = "DISCORDANT_ANATOMY"
    """
    Anatomical location of the classical type and the atlas cluster do not agree — e.g. different layers, subregions, or hemispheric distribution.

    """
    ELECTROPHYSIOLOGY_ONLY_DEFINITION = "ELECTROPHYSIOLOGY_ONLY_DEFINITION"
    """
    This classical type is defined primarily or solely by electrophysiological properties, making transcriptomic matching inherently uncertain.

    """
    OTHER = "OTHER"


class DiscoveryContextKind(str, Enum):
    """
    Semantic class of a percentile context recorded on MappingEdge.discovery_score. Today only SURVIVAL_COHORT is emitted by Stage A; the other values reserve slots for future universal / anatomical / sibling context emission so that downstream agents can reason about contexts uniformly without parsing free-text descriptions.

    """
    SURVIVAL_COHORT = "SURVIVAL_COHORT"
    """
    Candidates surviving the discovery pass's filters (region, NT, sex bias, etc.) at the queried rank. CURRENTLY THE ONLY KIND EMITTED BY STAGE A. Cohort membership is dynamic — it depends on the query filters, so two queries against the same taxonomy can yield different cohorts.

    """
    ATLAS_UNIVERSAL = "ATLAS_UNIVERSAL"
    """
    All clusters in the taxonomy at the queried rank, with no filters. Stable across queries against the same taxonomy. Emission currently dormant; reserved for revival of the legacy `_score_from_percentiles` path.

    """
    ANATOMICAL_RESTRICTION = "ANATOMICAL_RESTRICTION"
    """
    All clusters annotated to a specified anatomical region closure, with no other filters. Anticipates future anatomy-context scoring; not yet emitted by Stage A.

    """
    SIBLINGS_UNDER_PARENT = "SIBLINGS_UNDER_PARENT"
    """
    Direct children of a common parent at the queried rank. Legacy notion from the pre-2026 sibling/global scoring scheme; reserved in case it is revived.

    """


class GeneDiscoverySource(str, Enum):
    """
    Where the per-gene `val` recorded on a GeneDiscoveryDetail came from. Determines which of val / reliable / percentiles / coverage are populated.

    """
    EXPRESSION = "EXPRESSION"
    """
    Value read from the candidate's precomputed_stats HDF5. val / reliable / percentiles populated; coverage populated at rank ≥ 1.

    """
    METADATA = "METADATA"
    """
    Gene flagged as a marker in the taxonomy YAML but absent from precomputed_stats. val / reliable / percentiles all null; raw_tier = +1 (a weak presence assertion based on metadata, not measurement).

    """


class DiscoveryRegionEvidence(str, Enum):
    """
    How Stage A established that a candidate is "in region" for the queried anatomy.

    """
    SELF = "SELF"
    """
    The candidate's own anatomical annotation places it in the queried region closure.

    """
    DESCENDANT_ONLY = "DESCENDANT_ONLY"
    """
    The candidate (rank ≥ 1) was rescued because its rank-0 descendants annotate to the region, even though the candidate's own anatomical metadata is incomplete (BCKG workaround for sparse mid-rank annotation).

    """


class CellCountCompleteness(str, Enum):
    """
    Provenance class for `cell_count` / `count_in_or_near_100um` on a spatial-annotation anat row. Mirrors brain_cell_KG's `cellCountCompleteness` edge property (see issue #95). Painted CCF2020 leaf domains carry no completeness tag (count is the authoritative spatial registration); rollup edges are tagged.

    """
    exact = "exact"
    """
    Rollup whose descendants are all CCF2020 painted domains (or descendants thereof); the count is an exact sum and can be cited without caveat.

    """
    lower_bound = "lower_bound"
    """
    Rollup that includes some non-painted descendants whose cells are not captured; the count is a floor. Non-zero values mean "at least this many cells in the region"; zero is uninformative. Cite with explicit caveat in mapping rationales.

    """



class OntologyTerm(ConfiguredBaseModel):
    """
    An ontology identifier + canonical label + source name triple. All three fields are required. name_in_source is always recorded — even when it matches the canonical label — because source context is important for traceability and review.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    id: str = Field(default=..., description="""Ontology CURIE from a recognised namespace. Pattern enforces a known prefix — add new prefixes here when new ontologies are adopted (e.g. HOMBA when released). Examples: CL:0000540, UBERON:0001950, NCBITaxon:10090, MBA:1031, HBA:12898, DHBA:10344.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    label: str = Field(default=..., description="""Canonical label from the ontology (must match exactly). Required for the validator hook correction loop — the hook verifies id:label pairs against OAK local databases.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm', 'ProposedCLTerm', 'SourceGroup']} })
    name_in_source: str = Field(default=..., description="""Text as it appears in the source document or atlas. Always record — even when identical to the canonical label — because source context matters for review and traceability. Examples:
  - source \"macaque\" → label \"Primates\" (NCBITaxon:9443)
  - source \"GPi\" → label \"internal segment of globus pallidus\" (UBERON:0002474)
  - source \"GPi shell neuron\" → label \"internal globus pallidus
    shell projection neuron\" (CL:4310096)
  - source \"internal segment of globus pallidus\" → label same
    (populate identically when no discrepancy)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'NeurotransmitterType',
                       'AnnotationTransferEvidence']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(CL|UBERON|NCBITaxon|MBA|DHBA|HBA|HOMBA|ABAO):[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class AnatomicalLocation(OntologyTerm):
    """
    An anatomical region associated with a cell type, with optional compartment annotation. Inherits id, label, name_in_source from OntologyTerm. When compartment is omitted, the location applies to the whole cell or compartment is unspecified.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5',
         'mixins': ['OntologyTerm']})

    compartment: Optional[CellCompartment] = Field(default=None, description="""Which cellular compartment resides in this region. Required when a cell type spans multiple regions with different compartments (e.g. OLM: soma in SO, axon in SLM). Leave absent for atlas terminal nodes (MERFISH captures soma implicitly) and for types where location is not compartment-specific.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation']} })
    cell_count: Optional[int] = Field(default=None, description="""Number of cells of this type with soma strictly registered to this anatomical region (legacy in-region count). Populated from atlas MERFISH registration data (e.g. WMBv1 anat cell counts per cluster per region). Enables ranking of anatomical locations by cell abundance. Leave absent for non-atlas nodes.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation']} })
    cell_ratio: Optional[float] = Field(default=None, description="""Legacy BCKG-stored ratio (= cell_count / cluster total cell count). Upstream renamed the source edge property to `obsolete_cell_ratio` (cosmetic churn — same value), retained here under the legacy name for audit and continuity. New region-inclusion logic should prefer `ratio_in_or_near_100um`. Leave absent for non-atlas nodes.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation']} })
    count_in_or_near_100um: Optional[int] = Field(default=None, description="""Count of cells of this type with soma in or within 100µm of this anatomical region. Per-source contribution (one AnatomicalLocation entry per (region, source DOI) — see `sources`). Currently the authoritative spatial count; `cell_count` is restricted to soma strictly in-region. Populated from upstream brain_cell_KG `countInOrNear100um` spatial-edge property.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation']} })
    ratio_in_or_near_100um: Optional[float] = Field(default=None, description="""Fraction of cluster cells with soma in or within 100µm of this region (= count_in_or_near_100um / cluster total cell count). The active region-inclusion cutoff is applied upstream against this value; evidencell does no further thresholding. Prefer this over `cell_ratio` for new region-presence logic.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation']} })
    cell_count_completeness: Optional[CellCountCompleteness] = Field(default=None, description="""Provenance of `cell_count` / `count_in_or_near_100um` rollup on this anat term. brain_cell_KG materialises three classes of spatial-annotation edges: (a) painted CCF2020 leaf domains carry no completeness tag
    — counts are authoritative spatial registrations;
(b) `exact` rollups group only painted domains (or their
    descendants); counts are exact sums and are trustworthy;
(c) `lower_bound` rollups include some non-painted
    descendants whose cells aren't captured; counts are
    floors — non-zero means \"at least this many cells here,
    probably more\"; zero is uninformative.
Stage B mapping subagents + report-time agents should caveat `lower_bound` rollup citations accordingly. Leave absent for painted-domain entries.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation']} })
    sources: Optional[list[PropertySource]] = Field(default=None, description="""Evidence sources for this specific anatomical location assertion. Populate for classical and prior-transcriptomic nodes, especially for sub-regional claims where location is specific or contested. scope is critical where location is context-dependent. Leave empty for atlas terminal nodes (provenance implicit from atlas + cell_set_accession).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation',
                       'GeneDescriptor',
                       'TypeSynonym',
                       'ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'NeurotransmitterType',
                       'AtSourceSet']} })
    id: str = Field(default=..., description="""Ontology CURIE from a recognised namespace. Pattern enforces a known prefix — add new prefixes here when new ontologies are adopted (e.g. HOMBA when released). Examples: CL:0000540, UBERON:0001950, NCBITaxon:10090, MBA:1031, HBA:12898, DHBA:10344.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    label: str = Field(default=..., description="""Canonical label from the ontology (must match exactly). Required for the validator hook correction loop — the hook verifies id:label pairs against OAK local databases.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm', 'ProposedCLTerm', 'SourceGroup']} })
    name_in_source: str = Field(default=..., description="""Text as it appears in the source document or atlas. Always record — even when identical to the canonical label — because source context matters for review and traceability. Examples:
  - source \"macaque\" → label \"Primates\" (NCBITaxon:9443)
  - source \"GPi\" → label \"internal segment of globus pallidus\" (UBERON:0002474)
  - source \"GPi shell neuron\" → label \"internal globus pallidus
    shell projection neuron\" (CL:4310096)
  - source \"internal segment of globus pallidus\" → label same
    (populate identically when no discrepancy)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'NeurotransmitterType',
                       'AnnotationTransferEvidence']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^(CL|UBERON|NCBITaxon|MBA|DHBA|HBA|HOMBA|ABAO):[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class CLMapping(ConfiguredBaseModel):
    """
    A Cell Ontology term binding for a node, with an explicit mapping type. Every non-terminal node should have a cl_mapping. Use EXACT when this node IS the CL term (modulo species). Use BROAD when the CL term is an ancestor and a new child term is needed. The presence of proposed_cl_term on the node indicates a new term is being drafted.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    cl_term: OntologyTerm = Field(default=..., description="""The CL term (existing or most appropriate ancestor)""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CLClassTerm'}],
         'domain_of': ['CLMapping']} })
    mapping_type: CLMappingType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CLMapping']} })
    mapping_notes: Optional[str] = Field(default=None, description="""Free text explaining the basis for this mapping type, especially for BROAD/RELATED.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CLMapping']} })


class GeneDescriptor(ConfiguredBaseModel):
    """
    A gene identified by the universal naming triple (name_in_source | id | label). For genes, symbol fills both the name_in_source and label roles: gene symbols ARE their own canonical labels in scientific usage, and recording the symbol as written in the source preserves species case convention (Sst vs SST) and the exact source wording. ncbi_gene_id is the stable cross-species identifier (the id role). Evidence sources for the marker assertion are recorded in the sources list.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    symbol: str = Field(default=..., description="""Gene symbol exactly as it appears in the source: e.g. Sst, Pvalb, Slc17a6 (mouse convention) or SST, PVALB, SLC17A6 (human convention). Serves as both name_in_source and label — gene symbols are their own canonical identifiers in scientific usage. ncbi_gene_id gives the stable cross-species identifier.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDescriptor', 'GeneExpression']} })
    modifier: Optional[str] = Field(default=None, description="""Expression context: HIGH, LOW, ABSENT, ENRICHED""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDescriptor']} })
    ncbi_gene_id: Optional[str] = Field(default=None, description="""NCBI Gene ID as CURIE, e.g. NCBIGene:20604 (Mus musculus Sst). Species-specific; preferred for multi-species use. Use Translator NodeNormalization for cross-species mapping: https://github.com/NCATSTranslator/NodeNormalization
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDescriptor']} })
    hgnc_id: Optional[str] = Field(default=None, description="""HGNC ID (human-only). Deprecated in favour of ncbi_gene_id; retained for backward compatibility.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDescriptor']} })
    category: Optional[MarkerCategory] = Field(default=None, description="""Functional category of this marker in the unified markers list. Use when populating GeneDescriptor entries in CellTypeNode.markers. Leave absent for entries in the legacy separate fields (defining_markers, neuropeptides, merfish_markers) where the field name itself encodes the category.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDescriptor']} })
    expression_score: Optional[float] = Field(default=None, description="""Expression level score from precomputed atlas stats. Populated for NEUROPEPTIDE markers from np_markers precomputed data (e.g. Vip:9.2 means Vip neuropeptide score = 9.2 in this cluster's stats). Leave absent for markers without quantitative score data.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDescriptor']} })
    sources: Optional[list[MarkerSource]] = Field(default=None, description="""Evidence sources for this marker assertion. Multiple sources allowed — e.g. protein evidence from one paper and transcript evidence from another. Populate for classical and prior-transcriptomic nodes. Leave empty for atlas node markers (atlas_markers, merfish_markers) — provenance is implicit from the parent node's atlas + cell_set_accession.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation',
                       'GeneDescriptor',
                       'TypeSynonym',
                       'ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'NeurotransmitterType',
                       'AtSourceSet']} })

    @field_validator('ncbi_gene_id')
    def pattern_ncbi_gene_id(cls, v):
        pattern=re.compile(r"^NCBIGene:[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ncbi_gene_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ncbi_gene_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('hgnc_id')
    def pattern_hgnc_id(cls, v):
        pattern=re.compile(r"^HGNC:[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid hgnc_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid hgnc_id format: {v}"
            raise ValueError(err_msg)
        return v


class CellTypeColocation(ConfiguredBaseModel):
    """
    A cell type that co-localises with or is spatially associated with the type being described. Used to record relative positional context separately from the absolute anatomical location.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    neighboring_type: str = Field(default=..., description="""Name or local node ID of the colocating cell type, e.g. \"GPi core neuron (PVALB+)\", \"Purkinje cell\", \"classical_basket\"
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation']} })
    spatial_relationship: Optional[str] = Field(default=None, description="""Spatial relationship descriptor. Suggested values: ADJACENT, PROXIMAL, DISTAL, INTERSPERSED, SAME_LAYER, LAYER_BORDER. Free text also acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation']} })
    notes: Optional[str] = Field(default=None, description="""Free-text context or citation supporting this colocation claim""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })


class HasMarkerType(ConfiguredBaseModel):
    """
    Mixin that adds a controlled marker_type field (PROTEIN | TRANSCRIPT). Applied to MarkerSource to give the most important methodological distinction as controlled vocabulary, while keeping the base PropertySource generic.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5',
         'mixin': True})

    marker_type: MarkerType = Field(default=..., description="""The molecule type detected: PROTEIN or TRANSCRIPT. The specific technique goes in PropertySource.method (free text).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMarkerType']} })


class PropertySource(ConfiguredBaseModel):
    """
    Evidence source for a single property assertion on a node. Used as the nested sources list on property objects: NeurotransmitterType.sources, ElectrophysiologyProfile.sources, MorphologyProfile.sources, AnatomicalLocation.sources. For marker assertions use MarkerSource (extends PropertySource with the controlled marker_type field).
    Leave sources lists empty on ATLAS_TRANSCRIPTOMIC nodes — provenance is implicit from atlas + cell_set_accession (see header convention).
    Property-specific guidance for LLM population:
    NeurotransmitterType.sources — method should describe how NT type was
      established: \"IHC (GABA/glutamate antibody)\",
      \"scRNA-seq (Gad2/Slc17a6 co-expression)\",
      \"electrophysiology (inhibitory PSPs recorded)\". Scope is important —
      NT type can differ across species or developmental stage.

    ElectrophysiologyProfile.sources — ref to the recording study. Scope
      should note age, temperature, and preparation (acute slice, in vivo, etc.).

    MorphologyProfile.sources — method e.g. \"Golgi stain\", \"biocytin fill +
      confocal\", \"electron microscopy\". Snippet from the cell description section.

    AnatomicalLocation.sources — ref establishing the location claim.
      Scope is critical where location is context-specific or contested.
      For sub-regional claims (e.g. \"shell region\"), cite specifically.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    ref: str = Field(default=..., description="""DOI (https://doi.org/...) or PMID (PMID:xxxxxxxx)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })
    method: Optional[str] = Field(default=None, description="""How this property was detected or established. Free text. Examples: \"IHC\", \"patch-clamp (acute slice)\", \"Golgi stain\", \"scRNA-seq\", \"smFISH\", \"retrograde tracing + scRNA-seq\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'AnnotationTransferEvidence',
                       'ProjectionSeqEvidence',
                       'MarkerAnalysisEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    scope: Optional[str] = Field(default=None, description="""Experimental context: species, age, brain region, preparation. E.g. \"adult mouse GPi\", \"human GPi post-mortem tissue\", \"P21 mouse cerebellum\". Populate where context affects generalisability of the claim.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })
    snippet: Optional[str] = Field(default=None, description="""Verbatim quote from the cited source supporting this assertion. Strongly recommended — primary material for reviewers at the evidence gate. Must be exact text from the source, no paraphrase. If quote_key is set, snippet may be omitted (dereferenceable from references.json). If both are present, snippet is the verified text.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource', 'LiteratureEvidence']} })
    quote_key: Optional[str] = Field(default=None, description="""Content-hashed key into the region's references.json quote store. Format: {corpus_id}_{hash8} where hash8 is the first 8 hex chars of SHA-256 of the normalised quote text. Allows quote lookup without embedding full text in the KB YAML. Set by asta-report-ingest and cite-traverse workflows. Reports dereference to include snippet text.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })
    notes: Optional[str] = Field(default=None, description="""Curator-derived analysis notes for this source: computed statistics, re-analysis observations, cross-subtype comparisons. Distinct from snippet (which must be a verbatim quote from the cited source). Examples: \"Detected in 46/46 cells (100%); mean counts 305273\", \"Htr3a-OLM 43% vs Sst-OLM 26% — subtype-specific expression\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })
    support: Optional[EvidenceSupport] = Field(default=None, description="""Whether this source supports, refutes, or is ambiguous for the property assertion. Set by cite-traverse and evidence-extraction workflows. Omit when support level is implicit (e.g. all sources on a property are assumed SUPPORT unless stated otherwise).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })
    source: Optional[str] = Field(default=None, description="""Workflow provenance tag identifying when/how this source was added. E.g. \"cite_traverse_2026_04_10\", \"asta_survey_2026_03\". Machine-set; not for human editing.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'GeneDiscoveryDetail',
                       'PrecomputedExpression']} })
    added_by: Optional[str] = Field(default=None, description="""Identifier of the agent or workflow run that wrote this entry. E.g. \"evidence_extraction_olm_cell_ca1_2026-04-22\". Machine-set; not for human editing.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })

    @field_validator('ref')
    def pattern_ref(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|https://doi\.org/.+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ref format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ref format: {v}"
            raise ValueError(err_msg)
        return v


class TypeSynonym(ConfiguredBaseModel):
    """
    An alternative name or abbreviation for a cell type, with evidence provenance. Captures the name as used in specific sources — abbreviations, historical terms, atlas labels, informal community terms. Sources cite the papers where this name is used or defined, enabling synonym-expanded queries in lit mining.
    Population guidance: extract synonyms as the first processing step for each paper. Set snippet to the passage where the name is introduced or defined. Multiple sources if the term appears across several papers.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    term: str = Field(default=..., description="""The synonym string exactly as used in the source. Required. Examples: \"OLM\", \"O-LM interneuron\", \"oriens-lacunosum moleculare cell\", \"Sst Gaba_3\" (when used as a cell type name in a paper).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['TypeSynonym']} })
    synonym_type: Optional[SynonymType] = Field(default=None, description="""Category of synonym — ABBREVIATION, HISTORICAL, ATLAS_LABEL, CROSS_SPECIES, or INFORMAL. Omit if unclear.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['TypeSynonym']} })
    sources: Optional[list[PropertySource]] = Field(default=None, description="""Papers where this synonym is used for this cell type. Each PropertySource: ref = citing paper; snippet = passage where name is defined or first used (quote_key also accepted); method = how the name is used in context (e.g. \"primary label throughout\", \"defined in introduction as abbreviation\"). Multiple sources if the term appears across multiple papers.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation',
                       'GeneDescriptor',
                       'TypeSynonym',
                       'ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'NeurotransmitterType',
                       'AtSourceSet']} })


class MarkerSource(PropertySource, HasMarkerType):
    """
    Evidence source for a marker assertion. Extends PropertySource with a controlled marker_type field (PROTEIN | TRANSCRIPT). Use in GeneDescriptor.sources. marker_type should always be populated.
    Examples:
      - marker_type: PROTEIN
        method: \"IHC (SST antibody)\"
        scope: \"adult human GPi\"
        snippet: \"SST+/SLC17A6+/SLC32A1+ neurons are located on the borders of the GPi\"
        ref: \"https://doi.org/10.1016/j.neuron.2017.03.017\"

      - marker_type: TRANSCRIPT
        method: \"snRNA-seq\"
        scope: \"adult mouse, WMBv1\"
        snippet: \"Sst neuropeptide marker present in clusters 1996 and 1997\"
        ref: \"https://doi.org/10.1038/s41586-023-06812-z\"

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5',
         'mixins': ['HasMarkerType']})

    marker_type: MarkerType = Field(default=..., description="""The molecule type detected: PROTEIN or TRANSCRIPT. The specific technique goes in PropertySource.method (free text).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasMarkerType']} })
    ref: str = Field(default=..., description="""DOI (https://doi.org/...) or PMID (PMID:xxxxxxxx)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })
    method: Optional[str] = Field(default=None, description="""How this property was detected or established. Free text. Examples: \"IHC\", \"patch-clamp (acute slice)\", \"Golgi stain\", \"scRNA-seq\", \"smFISH\", \"retrograde tracing + scRNA-seq\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'AnnotationTransferEvidence',
                       'ProjectionSeqEvidence',
                       'MarkerAnalysisEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    scope: Optional[str] = Field(default=None, description="""Experimental context: species, age, brain region, preparation. E.g. \"adult mouse GPi\", \"human GPi post-mortem tissue\", \"P21 mouse cerebellum\". Populate where context affects generalisability of the claim.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })
    snippet: Optional[str] = Field(default=None, description="""Verbatim quote from the cited source supporting this assertion. Strongly recommended — primary material for reviewers at the evidence gate. Must be exact text from the source, no paraphrase. If quote_key is set, snippet may be omitted (dereferenceable from references.json). If both are present, snippet is the verified text.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource', 'LiteratureEvidence']} })
    quote_key: Optional[str] = Field(default=None, description="""Content-hashed key into the region's references.json quote store. Format: {corpus_id}_{hash8} where hash8 is the first 8 hex chars of SHA-256 of the normalised quote text. Allows quote lookup without embedding full text in the KB YAML. Set by asta-report-ingest and cite-traverse workflows. Reports dereference to include snippet text.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })
    notes: Optional[str] = Field(default=None, description="""Curator-derived analysis notes for this source: computed statistics, re-analysis observations, cross-subtype comparisons. Distinct from snippet (which must be a verbatim quote from the cited source). Examples: \"Detected in 46/46 cells (100%); mean counts 305273\", \"Htr3a-OLM 43% vs Sst-OLM 26% — subtype-specific expression\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })
    support: Optional[EvidenceSupport] = Field(default=None, description="""Whether this source supports, refutes, or is ambiguous for the property assertion. Set by cite-traverse and evidence-extraction workflows. Omit when support level is implicit (e.g. all sources on a property are assumed SUPPORT unless stated otherwise).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })
    source: Optional[str] = Field(default=None, description="""Workflow provenance tag identifying when/how this source was added. E.g. \"cite_traverse_2026_04_10\", \"asta_survey_2026_03\". Machine-set; not for human editing.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'GeneDiscoveryDetail',
                       'PrecomputedExpression']} })
    added_by: Optional[str] = Field(default=None, description="""Identifier of the agent or workflow run that wrote this entry. E.g. \"evidence_extraction_olm_cell_ca1_2026-04-22\". Machine-set; not for human editing.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource']} })

    @field_validator('ref')
    def pattern_ref(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|https://doi\.org/.+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ref format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ref format: {v}"
            raise ValueError(err_msg)
        return v


class ElectrophysiologyProfile(ConfiguredBaseModel):
    """
    Electrophysiological characterisation of a cell type: e-type classification and firing properties, with evidence provenance. Replaces the former electrophysiology_class string + ephys_sources list pair.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    description: str = Field(default=..., description="""E-type label and firing properties. Free text. E.g. \"fast-spiking\", \"regular-spiking adapting with pronounced sag (Ih)\", \"theta spiking resonance, high input resistance\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'Caveat',
                       'DiscoveryContext',
                       'CellTypeMappingGraph',
                       'AnnotationTransferDataset',
                       'BulkDataset']} })
    sources: Optional[list[PropertySource]] = Field(default=None, description="""Evidence sources for this electrophysiology characterisation. ref to the recording study; snippet from the e-type description. scope should note age, temperature, and preparation type (e.g. \"P21 mouse, acute slice, 32°C\").
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation',
                       'GeneDescriptor',
                       'TypeSynonym',
                       'ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'NeurotransmitterType',
                       'AtSourceSet']} })


class MorphologyProfile(ConfiguredBaseModel):
    """
    Morphological characterisation of a cell type: key structural features with evidence provenance. Replaces the former morphology_notes string + morphology_sources list pair.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    description: str = Field(default=..., description="""Key morphological features. Free text. E.g. \"large soma, radially-projecting dendrites into ML\", \"horizontal dendrites in SO, axon ramifies in SLM\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'Caveat',
                       'DiscoveryContext',
                       'CellTypeMappingGraph',
                       'AnnotationTransferDataset',
                       'BulkDataset']} })
    sources: Optional[list[PropertySource]] = Field(default=None, description="""Evidence sources for this morphology characterisation. method e.g. \"Golgi stain\", \"biocytin fill + confocal\", \"electron microscopy\". Snippet from cell description section.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation',
                       'GeneDescriptor',
                       'TypeSynonym',
                       'ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'NeurotransmitterType',
                       'AtSourceSet']} })


class NeurotransmitterType(ConfiguredBaseModel):
    """
    The neurotransmitter identity of a cell type, recorded as the universal naming triple: name_in_source (verbatim source label) + cl_terms (CL ontology identifiers) + sources (evidence provenance).
    Used for both classical and atlas nodes — replaces the previous split between nt_type (free string) and atlas_nt_type (verbatim string).
    For dual/co-transmitter types, list both CL terms in cl_terms. The name_in_source captures the compound label as written in the source (e.g. \"Glut-GABA\", \"GABA-Glut (dual)\") — ordering may differ between atlases (WMBv1 lists dominant NT first; HMBA BG lists GABA first by convention). Use name_in_source to preserve this exactly; the cl_terms list is order-independent.
    CL terms for common neurotransmitter types:
      CL:0000617  GABAergic neuron
      CL:0000679  glutamatergic neuron
      CL:0000108  cholinergic neuron
      CL:0000084  glycinergic neuron  (Note: verify in current CL release)
      CL:0000700  dopaminergic neuron
      CL:0000561  serotonergic neuron (Note: verify in current CL release)
    For types not covered by a single CL term, record the closest available and note the limitation in sources[].scope or a node-level notes field.
    On ATLAS_TRANSCRIPTOMIC nodes: set name_in_source to the verbatim atlas label; cl_terms recommended but optional (atlas naming is primary). Leave sources empty — provenance is implicit from atlas + cell_set_accession.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    name_in_source: str = Field(default=..., description="""NT label exactly as written in the source paper or atlas, e.g. \"GABA\", \"Glut-GABA\", \"GABA-Glut (dual)\", \"GABA/Glycine\", \"Glut\". Preserves source naming convention including ordering, which can differ between atlases for the same biology.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'NeurotransmitterType',
                       'AnnotationTransferEvidence']} })
    cl_terms: Optional[list[OntologyTerm]] = Field(default=None, description="""CL ontology terms for this NT type. One entry per transmitter (e.g. two entries for a dual-transmitter type). Each OntologyTerm carries id, label, and name_in_source (the individual substance name as it appears in the source, e.g. \"GABA\", \"Glut\"). Strongly recommended for classical nodes; optional for atlas terminal nodes where atlas naming is primary.
""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CLClassTerm'}],
         'domain_of': ['NeurotransmitterType']} })
    sources: Optional[list[PropertySource]] = Field(default=None, description="""Evidence sources establishing this NT type. One or more PropertySource entries with ref, method, scope, snippet. method should describe how NT type was established, e.g. \"IHC (GABA antibody)\", \"scRNA-seq (Gad2/Slc17a6 co-expression)\", \"electrophysiology (inhibitory PSPs recorded)\". scope is important — NT type can differ across species or developmental stage. Leave empty on ATLAS_TRANSCRIPTOMIC nodes (provenance implicit).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation',
                       'GeneDescriptor',
                       'TypeSynonym',
                       'ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'NeurotransmitterType',
                       'AtSourceSet']} })


class PropertyComparison(ConfiguredBaseModel):
    """
    A structured comparison of one property between type_a and type_b on a mapping edge. Complements evidence items: evidence items provide detailed justification; property_comparisons give a machine-readable property-level alignment summary that makes the basis for the confidence judgment explicit and reportable.
    Populate at minimum: nt_type, location, all defining markers. Use NOT_ASSESSED when data for a property is unavailable.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    property: str = Field(default=..., description="""Name of the property compared. Suggested values: nt_type, location, marker_{gene_symbol}, morphology, electrophysiology, projection_target, ccf_distribution. Free text — be specific, e.g. \"marker_Sst\" not \"marker\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyComparison']} })
    node_a_value: str = Field(default=..., description="""Value of this property as recorded on type_a. Use the actual text from the node, not a paraphrase.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyComparison']} })
    node_b_value: str = Field(default=..., description="""Value of this property as recorded on type_b (verbatim from node or its source metadata).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyComparison']} })
    alignment: PropertyAlignment = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyComparison']} })
    notes: Optional[str] = Field(default=None, description="""Brief explanation of the alignment call. Required for APPROXIMATE and DISCORDANT. E.g. \"Same biology; WMBv1 orders dual NT with dominant first (Glut-GABA vs GABA-Glut), convention difference only.\"
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })


class HierarchyNode(ConfiguredBaseModel):
    """
    One level of an atlas taxonomy hierarchy (used in AtlasCellSetRef)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    level: str = Field(default=..., description="""Taxonomy level string, e.g. CLASS, SUBCLASS, SUPERTYPE, CLUSTER (WMBv1) or GROUP (HMBA BG). See schema header comment for atlas-specific values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyNode', 'PrecomputedExpression']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyNode', 'CellTypeNode', 'CellTypeMappingGraph']} })
    cell_set_accession: Optional[str] = Field(default=None, description="""CCN accession at this level, e.g. CS20230722_SUPT_1145""", json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyNode', 'CellTypeNode', 'AtlasMetadataEvidence']} })


class ProposedCLTerm(ConfiguredBaseModel):
    """
    Draft or approved Cell Ontology term entry for the classical/named type being described. Generated from the evidence graph by traversing from this node to terminal atlas nodes. A node with cl_mapping.mapping_type = BROAD should have a ProposedCLTerm whose parent_cl_term = cl_mapping.cl_term, placing the new term as a child in the hierarchy.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    cl_id: Optional[str] = Field(default=None, description="""Existing CL term ID this proposed term is updating, when applicable (e.g. when adding/refining a definition for an existing CL term). Leave absent for brand-new proposed terms — temporary CL: placeholder IDs must not be used, as they cannot be validated against the live ontology. Track the term request in `term_request_url` instead.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProposedCLTerm']} })
    term_request_url: Optional[str] = Field(default=None, description="""URL of the CL new-term-request issue tracking this proposed term (e.g. https://github.com/obophenotype/cell-ontology/issues/N). Populated once a term request has been filed via the cl-term-request workflow. The eventual CL ID assigned on merge replaces this field with cl_id.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProposedCLTerm']} })
    label: Optional[str] = Field(default=None, description="""Term label""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm', 'ProposedCLTerm', 'SourceGroup']} })
    parent_cl_term: Optional[OntologyTerm] = Field(default=None, description="""The CL term this proposed term is a child of. For nodes with cl_mapping.mapping_type = BROAD, this should match cl_mapping.cl_term. For nodes with cl_mapping.mapping_type = EXACT, this field is typically not needed. Drives placement in the CL hierarchy and should be confirmed with CL editors.
""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'CLClassTerm'}],
         'domain_of': ['ProposedCLTerm']} })
    definition: Optional[str] = Field(default=None, description="""Proposed CL definition text. Standard template: \"A [parent_cl_term.label] that is [distinguishing_feature]. These cells are located in [location]. Reference transcriptomic data for this type can be found in [atlas] in cell set [accession].\"
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProposedCLTerm']} })
    comment: Optional[str] = Field(default=None, description="""Proposed CL comment: the mapping rationale derived from the evidence chain. Template: \"Mapping to [type] is based on [evidence summary]. [Caveats if any].\"
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProposedCLTerm']} })
    xrefs: Optional[list[str]] = Field(default=None, description="""References — DOIs, PMIDs, atlas URLs, and CCN cell set accessions. The CCN accession of the terminal node(s) should always be included here.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProposedCLTerm']} })
    status: Optional[str] = Field(default=None, description="""DRAFT | SUBMITTED | ACCEPTED""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProposedCLTerm', 'AnnotationTransferDataset']} })


class CellTypeNode(ConfiguredBaseModel):
    """
    A named cell type at any level of description: classical, prior transcriptomic, atlas cluster, or emerging multimodal. Nodes are connected by MappingEdges to form the evidence graph. Terminal nodes are atlas cell sets.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    id: str = Field(default=..., description="""Locally unique ID within this graph. Suggested format: lowercase_underscored, e.g. \"lugaro\", \"pli3_osorno\", \"wmb_1145\"
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    name: str = Field(default=..., description="""Human-readable name, e.g. \"Lugaro cell\", \"CB PLI Gly-Gaba_2 (supertype 1145)\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyNode', 'CellTypeNode', 'CellTypeMappingGraph']} })
    synonyms: Optional[list[TypeSynonym]] = Field(default=None, description="""Alternative names and abbreviations for this cell type, with evidence provenance. Populated during literature mining — synonym extraction is the first processing step for each paper (both survey and targeted paths). Used to expand queries in subsequent searches.
Include all forms that appear in the literature or atlases: abbreviations (OLM), long forms if non-obvious, historical names, atlas labels used as cell type names. Do NOT include the canonical name field value itself.
For ATLAS_TRANSCRIPTOMIC nodes: include the atlas cluster label in synonyms only if that label is used as a cell type name in at least one non-atlas paper.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    definition_basis: DefinitionBasis = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    species: Optional[OntologyTerm] = Field(default=None, description="""NCBITaxon term""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'NCBITaxonClassTerm'}],
         'domain_of': ['CellTypeNode', 'CellTypeMappingGraph', 'BulkDataset']} })
    anatomical_location: Optional[list[AnatomicalLocation]] = Field(default=None, description="""Anatomical location(s) of this cell type. Each entry is an AnatomicalLocation (OntologyTerm + optional compartment). Prefer Allen atlas terms (MBA for mouse; DHBA or HBA for human/primate); use UBERON as fallback. Look up via OLS4. name_in_source carries the region name as written in the source (e.g. \"GPi shell region\", \"GPi\"). Multiple entries for types that span regions or are defined relative to multiple structures. Set compartment (SOMA, AXON_TARGET, DENDRITE) when a type has different compartments in different regions (e.g. OLM: soma in SO, axon in SLM). Leave compartment absent when location is not compartment-specific or compartment is unknown.
""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'AnatomyTerm'}],
         'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    colocated_types: Optional[list[CellTypeColocation]] = Field(default=None, description="""Other cell types that co-localise with or are spatially adjacent to this type. Records relative positional context separately from the anatomical location above (e.g. \"adjacent to GPi core neurons\").
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    cl_mapping: Optional[CLMapping] = Field(default=None, description="""CL term binding with mapping type (EXACT or BROAD). Every non-terminal node should have a cl_mapping. EXACT: this node IS this CL term (modulo species). BROAD: this node is a subtype; a ProposedCLTerm would be a new child of the cl_term. Terminal nodes (atlas cell sets) may also have a cl_mapping once cognate CL terms exist.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    proposed_cl_term: Optional[ProposedCLTerm] = Field(default=None, description="""Draft CL term for this node — populated when authoring a new or revised CL entry. For BROAD cl_mapping nodes: proposed_cl_term.parent_cl_term = cl_mapping.cl_term. For EXACT cl_mapping nodes: proposed_cl_term.cl_id = cl_mapping.cl_term.id (updating an existing term).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    is_terminal: Optional[bool] = Field(default=None, description="""True if this node is a cell set in the community target atlas (the mapping destination). Terminal nodes should have cell_set_accession populated.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    defining_markers: Optional[list[GeneDescriptor]] = Field(default=None, description="""Markers used to define this type. For classical/literature nodes: markers from the original type description. For atlas nodes: defining markers from the atlas (cluster.markers.combo or equivalent).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    negative_markers: Optional[list[GeneDescriptor]] = Field(default=None, description="""Markers explicitly shown to be absent (all node types).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    neuropeptides: Optional[list[GeneDescriptor]] = Field(default=None, description="""Neuropeptide co-transmitters expressed by this cell type (all node types). For classical nodes: from literature (populate sources on each GeneDescriptor). For atlas nodes: from atlas np.markers column (sources left empty). Separate from defining_markers because neuropeptide identity is a distinct functional property — though a gene may appear in both lists (e.g. Sst as a defining marker AND as a neuropeptide co-transmitter). Examples: Sst, Vip, Cck, Npy, Pnoc.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    at_source_sets: Optional[list[AtSourceSet]] = Field(default=None, description="""Annotated cell set(s), in external dataset(s), that correspond to this classical cell type — the result of an agentic judgement made by reading the dataset's describing paper (NOT inferable from transcriptomic overlap alone). Authored by lit-ingest / evidence-extraction once a dataset's annotation labels are available. Each entry names a (dataset_accession, source_label) pair plus the nature of the correspondence, and carries quote-backed `sources` exactly like defining_markers. `emit-stage-b` iterates these to attach ANNOTATION_TRANSFER evidence, resolving the AT run operationally from (dataset_accession, target_taxonomy, source_label). Distinct from prior_dataset_accession/prior_cluster_label, which assert that the node *is* a prior transcriptomic cluster.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    nt_type: Optional[NeurotransmitterType] = Field(default=None, description="""Neurotransmitter type of this cell type. Applies to both classical and atlas terminal nodes (unified field, replaces atlas_nt_type). Carries the naming triple: name_in_source (verbatim source label), cl_terms (CL identifiers), sources (evidence provenance).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    electrophysiology: Optional[ElectrophysiologyProfile] = Field(default=None, description="""Electrophysiological characterisation with nested evidence sources. Replaces former electrophysiology_class (string) + ephys_sources (list) pair.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    morphology: Optional[MorphologyProfile] = Field(default=None, description="""Morphological characterisation with nested evidence sources. Replaces former morphology_notes (string) + morphology_sources (list) pair.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    prior_dataset_accession: Optional[str] = Field(default=None, description="""Dataset accession where this T-type was defined, e.g. SCP795, GEO:GSE173954. Used when definition_basis = PRIOR_TRANSCRIPTOMIC.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    prior_cluster_label: Optional[str] = Field(default=None, description="""Cluster label in the prior dataset, e.g. \"PLI3\", \"MLI1\". Used when definition_basis = PRIOR_TRANSCRIPTOMIC.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    prior_reference: Optional[str] = Field(default=None, description="""DOI or PMID of the paper defining this cluster, e.g. \"https://doi.org/10.1038/s41593-022-01057-x\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    atlas: Optional[str] = Field(default=None, description="""Atlas identifier, e.g. \"WMBv1\", \"HMBA_BG_Consensus\", \"BICAN_10x_Multiome_2024\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AtlasMetadataEvidence',
                       'AtlasQueryEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    taxonomy_id: Optional[str] = Field(default=None, description="""Taxonomy version identifier, e.g. CCN202307220""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferResultSet',
                       'TaxonomyNodeList',
                       'AtlasReference']} })
    cell_set_accession: Optional[str] = Field(default=None, description="""CCN cell set accession at this node's taxonomy level, e.g. CS20230722_SUPT_1145""", json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyNode', 'CellTypeNode', 'AtlasMetadataEvidence']} })
    taxonomy_level: Optional[str] = Field(default=None, description="""Taxonomy level string, e.g. CLASS, SUBCLASS, SUPERTYPE, CLUSTER (WMBv1) or GROUP (HMBA BG). See schema header comment for atlas-specific values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'TaxonomyNodeList']} })
    taxonomy_rank: Optional[int] = Field(default=None, description="""Integer rank for cross-taxonomy level ordering. 0 = most specific (leaf/terminal), incrementing toward root. Derivable from taxonomy_level + taxonomy_meta.yaml level_hierarchy when not set explicitly.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'TaxonomyNodeList']} })
    parent_hierarchy: Optional[list[HierarchyNode]] = Field(default=None, description="""All parent levels in the atlas taxonomy, from immediate parent to root""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    n_cells: Optional[int] = Field(default=None, description="""Number of cells of this type in the 10x dataset, summed across all regions. Populated from the atlas taxonomy source (e.g. WMBv1 KG node `cell_count` property). Distinct from `anatomical_location[].cell_count`, which is the per-region MerFish count. Leave absent for non-atlas nodes.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferMetricRow',
                       'DiscoveryAtSignal',
                       'ChildClusterExpression']} })
    merfish_markers: Optional[list[GeneDescriptor]] = Field(default=None, description="""MERFISH panel markers distinguishing this type (merfish.markers.combo)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    markers: Optional[list[GeneDescriptor]] = Field(default=None, description="""Unified marker list for atlas taxonomy nodes. Replaces the separate defining_markers / neuropeptides / merfish_markers fields for atlas nodes; use GeneDescriptor.category to distinguish marker roles (DEFINING, DEFINING_SCOPED, TF, NEUROPEPTIDE, NT_MARKER, MERFISH). Negative markers use modifier: ABSENT. The legacy separate fields are retained for backward compatibility with existing draft KB YAML.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    neighborhood: Optional[str] = Field(default=None, description="""Atlas-assigned neighborhood or supergroup label (e.g. \"Subpallium-GABA\"). Populated from atlas metadata; provides coarser grouping above taxonomy class level. Leave absent for non-atlas nodes.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    male_female_ratio: Optional[float] = Field(default=None, description="""Male/Female cell count ratio from source taxonomy (>1 = male-biased, <1 = female-biased). Stored to 2 dp. Null when balanced or data unavailable. Computed from Male and Female fraction properties in the source taxonomy metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    ccf_distribution: Optional[str] = Field(default=None, description="""CCF region distribution from atlas, e.g. \"CB:0.72,NA:0.25\" (from CCF_broad.freq column)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    sex_bias: Optional[SexBias] = Field(default=None, description="""Expected direction of sexual dimorphism in cell number or defining-marker expression. Set on classical nodes only. Used by find-candidates to score atlas clusters whose male_female_ratio matches the expected direction. Leave absent when sex dimorphism is not documented for this type.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    definition_references: Optional[list[str]] = Field(default=None, description="""General source citations for this node's defining properties — the key papers that established or characterised this cell type. DOI or PMID strings. Not property-scoped; for property-specific provenance use the nested sources on electrophysiology, morphology, anatomical_location, nt_type, and marker GeneDescriptors. Not needed for atlas terminal nodes — use metadata_url on AtlasMetadataEvidence instead.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    precomputed_expression: Optional[PrecomputedExpression] = Field(default=None, description="""Precomputed expression statistics for key genes from the atlas taxonomy. Used for property comparison scoring on mapping edges. Populated by the precomputed-stats workflow for atlas terminal nodes. Leave absent for classical/prior-transcriptomic nodes.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    cell_set_designation: Optional[str] = Field(default=None, description="""CAS taxonomy designation string for this cell set (e.g. \"Vip\", \"49_Vip\"). From CAS-format taxonomy ingest. Distinct from name which may be editorially adjusted.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    rationale_dois: Optional[list[str]] = Field(default=None, description="""DOIs cited as rationale for this cell set's designation in the source CAS taxonomy. From CAS-format taxonomy metadata.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode']} })
    notes: Optional[str] = Field(default=None, description="""Any caveats or observations not captured by other fields""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })

    @field_validator('prior_reference')
    def pattern_prior_reference(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|https://doi\.org/.+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid prior_reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid prior_reference format: {v}"
            raise ValueError(err_msg)
        return v


class EvidenceItem(ConfiguredBaseModel):
    """
    Base class for all evidence items supporting a mapping edge
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class LiteratureEvidence(EvidenceItem):
    """
    Evidence from a peer-reviewed paper. Must include verbatim snippet from abstract (or open-access full text). Used for: classical type definitions, prior T-type characterisations, cross-modal bridging papers.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    reference: str = Field(default=..., description="""PMID:xxxxxxxx or https://doi.org/xxxxx""", json_schema_extra = { "linkml_meta": {'domain_of': ['LiteratureEvidence']} })
    snippet: str = Field(default=..., description="""Exact verbatim text from the cited paper's abstract (or full text if open access). Must be a literal substring of the cached reference — no paraphrasing.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource', 'LiteratureEvidence']} })
    study_type: Optional[str] = Field(default=None, description="""Type of study: MORPHOLOGICAL, ELECTROPHYSIOLOGICAL, TRANSCRIPTOMIC, MULTIMODAL, FUNCTIONAL, REVIEW
""", json_schema_extra = { "linkml_meta": {'domain_of': ['LiteratureEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })

    @field_validator('reference')
    def pattern_reference(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|https://doi\.org/.+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid reference format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid reference format: {v}"
            raise ValueError(err_msg)
        return v


class AtlasMetadataEvidence(EvidenceItem):
    """
    Evidence drawn directly from an atlas taxonomy metadata file (the cluster spreadsheet). Captures: anatomical location (from MERFISH registration), NT type, defining markers, CCF distribution. Primary evidence type for atlas-to-classical mappings based on atlas-provided information. E.g. GPi shell neuron mapping based on HMBA metadata.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    atlas: str = Field(default=..., description="""Atlas identifier, e.g. \"HMBA_BG_Consensus\", \"WMBv1\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AtlasMetadataEvidence',
                       'AtlasQueryEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    cell_set_accession: Optional[str] = Field(default=None, description="""CCN accession for the referenced cell set""", json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyNode', 'CellTypeNode', 'AtlasMetadataEvidence']} })
    anatomical_location: Optional[list[AnatomicalLocation]] = Field(default=None, description="""Anatomical location from atlas curation. AnatomicalLocation with name_in_source set to the verbatim atlas annotation (e.g. \"GPi\", \"GPi shell and surrounding GPi core neurons\"). id/label from Allen atlas (MBA/DHBA) or UBERON. Compartment is typically absent for atlas entries (MERFISH captures soma position implicitly).
""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'AnatomyTerm'}],
         'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    ccf_distribution: Optional[str] = Field(default=None, description="""CCF region frequency distribution from atlas, e.g. \"GPi:0.78,GPe:0.12\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    nt_type: Optional[NeurotransmitterType] = Field(default=None, description="""NT type as recorded in the atlas taxonomy. Use NeurotransmitterType: set name_in_source to the verbatim atlas label (e.g. \"Glut-GABA\"); cl_terms recommended. Leave sources empty — provenance is implicit from this evidence item's atlas + metadata_url.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    nt_consistent_with_classical: Optional[bool] = Field(default=None, description="""DEPRECATED in v0.5 — superseded by MappingEdge.property_comparisons, which captures NT type alignment (and all other properties) in a general, structured way. Retained for backward compatibility. Use property_comparisons with property: \"nt_type\" instead.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtlasMetadataEvidence', 'AnnotationTransferEvidence']} })
    defining_markers: Optional[list[GeneDescriptor]] = Field(default=None, description="""Defining markers from the atlas metadata (cluster.markers.combo or equivalent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    negative_markers: Optional[list[GeneDescriptor]] = Field(default=None, description="""Markers explicitly absent (e.g. Pvalb-negative in GPi shell)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    neuropeptides: Optional[list[GeneDescriptor]] = Field(default=None, description="""Neuropeptide co-transmitters from the atlas (np.markers column or equivalent). Mirrors atlas node neuropeptides — same data, snapshot on the evidence item.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    merfish_markers: Optional[list[GeneDescriptor]] = Field(default=None, description="""MERFISH panel markers for this cell set (from merfish.markers.combo)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'AtlasMetadataEvidence']} })
    metadata_url: Optional[str] = Field(default=None, description="""URL or accession of the metadata file used""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtlasMetadataEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class AtlasQueryEvidence(EvidenceItem):
    """
    Evidence from a curator-performed interactive query against a published atlas browser (ABC Atlas, Allen Brain Map, BICCN viewer, etc.) with specified filters. Documents what was observed when filtering the atlas by anatomy, neurotransmitter type, gene expression, or other parameters. Reproducible given the same atlas version and filter set.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    atlas: str = Field(default=..., description="""Atlas name and version, e.g. \"ABC Atlas v20231215\", \"Allen Brain Map WMBv1.0\"
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AtlasMetadataEvidence',
                       'AtlasQueryEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    query_url: str = Field(default=..., description="""URL capturing the exact query state (filters applied). Use the atlas browser's share/permalink feature where available. Short URLs are acceptable if the target is stable (e.g. tinyurl pointing to ABC Atlas with filters).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtlasQueryEvidence']} })
    filters_applied: Optional[str] = Field(default=None, description="""Human-readable description of the filters used, e.g. \"anatomy=HPF; NT=GABA; expression=Chrna2\". Redundant with query_url but improves readability without loading the URL.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtlasQueryEvidence']} })
    atlas_version: Optional[str] = Field(default=None, description="""Explicit data version string from the atlas if distinct from the atlas name, e.g. \"20231215\" or \"WMBv1.0.0\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtlasQueryEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class AnnotationTransferLevelResult(ConfiguredBaseModel):
    """
    Annotation transfer metrics at a single taxonomy level
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    taxonomy_level: str = Field(default=..., description="""Taxonomy level string (e.g. CLASS, SUBCLASS, SUPERTYPE, CLUSTER)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'TaxonomyNodeList']} })
    taxonomy_rank: Optional[int] = Field(default=None, description="""Integer rank of this level. 0 = most specific (leaf), incrementing toward root. Allows cross-taxonomy comparison of mapping granularity.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'TaxonomyNodeList']} })
    best_target_name: str = Field(default=..., description="""Name of the best-matching target at this level""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult']} })
    best_target_accession: Optional[str] = Field(default=None, description="""CCN accession of the best-matching target""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult']} })
    coverage: Optional[float] = Field(default=None, description="""Fraction of source cells mapping to this target. High coverage = the source type is concentrated on this target. Equivalent to recall in standard ML terms. Surfaced as `Cov` in figure annotations and `coverage` in `at_figures --emit-metrics` JSON sidecars. Renamed from `group_purity` in the 2026-05-25 nomenclature standardisation (hard cutover).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'GeneDiscoveryDetail']} })
    purity: Optional[float] = Field(default=None, description="""Fraction of cells in the target that come from this source. High purity = the target is specifically populated by this source type. Equivalent to precision in standard ML terms. Surfaced as `Pur` in figure annotations and `purity` in `at_figures --emit-metrics` JSON sidecars. Renamed from `target_purity` in the 2026-05-25 nomenclature standardisation (hard cutover).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult', 'AnnotationTransferMetricRow']} })
    f1_score: Optional[float] = Field(default=None, description="""Harmonic mean of coverage and purity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult']} })
    n_cells_mapped: Optional[int] = Field(default=None, description="""Number of source cells mapped to this target at this level (after bootstrap filter)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult']} })
    median_bootstrap: Optional[float] = Field(default=None, description="""Median bootstrap confidence score for cells mapped to this target""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult', 'AnnotationTransferMetricRow']} })


class AnnotationTransferMetricRow(ConfiguredBaseModel):
    """
    One row of (source_label, taxonomy_level, target_accession) → metrics from an annotation-transfer run. Uniquely keyed on (source_label, taxonomy_level, target_accession). Container for the canonical per-(source, target) F1/precision/recall values that `AnnotationTransferResultSet` stores. Distinct from `AnnotationTransferLevelResult`: the latter records the source's best target at each level (one row per (source, level)); this class records every (source, level, target) triple seen by the AT run.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    source_label: str = Field(default=..., description="""Source cluster / cohort label as it appears in the AT run input.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow', 'AtSourceSet']} })
    taxonomy_level: str = Field(default=..., description="""Taxonomy level (CLASS / SUBCLASS / SUPERTYPE / CLUSTER).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'TaxonomyNodeList']} })
    taxonomy_rank: Optional[int] = Field(default=None, description="""Integer rank of this level. 0 = most specific (leaf), incrementing toward root.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'TaxonomyNodeList']} })
    target_name: Optional[str] = Field(default=None, description="""Name of the target at this level (e.g. \"0206 Pvalb Gaba_2\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow', 'DiscoveryAtSignal']} })
    target_accession: str = Field(default=..., description="""CCN accession of the target (e.g. CS20230722_SUPT_0206).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow', 'BulkCorrelationEvidence']} })
    n_cells: Optional[int] = Field(default=None, description="""Number of source cells mapping to this target at this level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferMetricRow',
                       'DiscoveryAtSignal',
                       'ChildClusterExpression']} })
    coverage: Optional[float] = Field(default=None, description="""Fraction of source cells mapping to this target (= recall in standard ML terms). Same semantic as `AnnotationTransferLevelResult.coverage`. Surfaced as `Cov` in figure annotations and `coverage` in `--emit-metrics` JSON sidecars.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'GeneDiscoveryDetail']} })
    purity: Optional[float] = Field(default=None, description="""Fraction of cells in the target coming from this source (= precision in standard ML terms). Same semantic as `AnnotationTransferLevelResult.purity`. Surfaced as `Pur` in figure annotations and `purity` in `--emit-metrics` JSON sidecars.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult', 'AnnotationTransferMetricRow']} })
    f1: Optional[float] = Field(default=None, description="""Harmonic mean of coverage and purity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow', 'DiscoveryAtSignal']} })
    median_bootstrap: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult', 'AnnotationTransferMetricRow']} })
    mean_bootstrap: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow']} })


class AnnotationTransferResultSet(ConfiguredBaseModel):
    """
    The complete set of per-(source, level, target) F1/precision/recall metrics for one annotation-transfer run. Schema-compliant successor to the implicit \"CSV columns are the contract\" convention used by `f1_matrix*.csv` / `f1_scores_*.csv` files. Lives alongside the run's `manifest.yaml` as `at_results.yaml` (canonical source of truth) — or `at_results_<variant>.yaml` for variant normalisations (e.g. `at_results_by_class.yaml` for Chamberland-style within-class dropout-robust scoring). `MappingEdge.evidence[].metrics_by_level` is populated by `src/evidencell/at_metrics.py` reading this set with (run_ref, source_label, edge.taxonomy_type) — never by an LLM agent. Raw CSVs are retained as audit trail under `raw/` but are not the contract.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    run_id: str = Field(default=..., description="""AnnotationTransferRun.id this result set belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferResultSet']} })
    taxonomy_id: str = Field(default=..., description="""Target taxonomy (e.g. CCN20230722).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferResultSet',
                       'TaxonomyNodeList',
                       'AtlasReference']} })
    normalisation: Optional[str] = Field(default=None, description="""Variant tag when the same run emits multiple normalisations (e.g. \"by_class\" for within-class dropout-robust scoring; null or \"base\" for standard F1 over the full dataset).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferResultSet', 'BulkDataFile']} })
    source_csv_relpath: Optional[str] = Field(default=None, description="""Path (relative to the run dir) of the raw CSV this YAML was derived from, for audit. Optional once the YAML is the canonical source of truth.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferResultSet']} })
    generated_at: Optional[str] = Field(default=None, description="""ISO8601 timestamp when this result set was written.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferResultSet']} })
    generator: Optional[str] = Field(default=None, description="""Script / tool that produced this YAML (e.g. \"src/evidencell/at_metrics.py::migrate_csv\").
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferResultSet']} })
    rows: list[AnnotationTransferMetricRow] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferResultSet']} })


class AnnotationTransferEvidence(EvidenceItem):
    """
    Evidence from computational label transfer between transcriptomic datasets. Minimal required fields: target_atlas + method. Report quality with best_f1_score (simple) or metrics_by_level (detailed). Covers two scenarios:
      (a) External dataset → community atlas: e.g. PLI3 cells (Osorno SCP795) → WMBv1.
          Source cluster identified by dataset accession + cluster label.
      (b) Allen taxonomy → Allen taxonomy: e.g. HMBA BG → WMBv1, or one atlas version
          to another. Source cluster identified by CCN cell_set_accession on both sides.
          Populate source_cell_set_accession when the source node has a CCN accession.

    For evidence items derived from a stored AnnotationTransferRun (parallels the BulkCorrelationEvidence/CorrelationRun pattern), populate `run_ref` with the run id; the renderer follows it to the run manifest at kb/annotation_transfer_runs/{run_id}/manifest.yaml for full provenance, F1 matrix, and figures. The per-evidence `method`, `tool_version`, `code_reference`, `bootstrap_threshold` etc. become redundant in that case and may be omitted on new evidence items (kept for back-compat with existing evidence ingested before the run schema landed).

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    target_atlas: str = Field(default=..., description="""Atlas the cells were mapped to, e.g. \"WMBv1\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence',
                       'CellTypeMappingGraph',
                       'AnnotationTransferRun']} })
    method: str = Field(default=..., description="""Transfer method, e.g. \"MapMyCells (default parameters)\", \"Seurat v4 label transfer\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'AnnotationTransferEvidence',
                       'ProjectionSeqEvidence',
                       'MarkerAnalysisEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    run_ref: Optional[str] = Field(default=None, description="""AnnotationTransferRun.id (pointing at kb/annotation_transfer_runs/{run_id}/manifest.yaml). Optional — when populated, the run carries the full F1 matrix, script provenance, and figures; this evidence item is a thin pointer at the relevant target_accession's row in that matrix. New evidence items should populate run_ref; existing evidence remains valid via its inline method/tool_version fields.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'BulkCorrelationEvidence']} })
    source_species: Optional[OntologyTerm] = Field(default=None, description="""NCBITaxon term for the species of the source dataset. Required when source and target species differ (cross-species transfer). E.g. {id: NCBITaxon:9443, label: Primates} for primate → mouse WMBv1.
""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'NCBITaxonClassTerm'}],
         'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    target_species: Optional[OntologyTerm] = Field(default=None, description="""NCBITaxon term for the species of the target atlas. E.g. {id: NCBITaxon:10090, label: Mus musculus} for WMBv1.
""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'NCBITaxonClassTerm'}],
         'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    source_dataset_accession: Optional[str] = Field(default=None, description="""Accession of the source dataset. E.g. SCP:SCP795, GEO:GSE173954, NeMO:nemo_xxxxxxx For cross-Allen-taxonomy transfers, this may be the taxonomy_id (e.g. CCN202307220) or the atlas identifier (e.g. \"HMBA_BG_Consensus\").
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    source_cluster_label: Optional[str] = Field(default=None, description="""Cluster label in the source dataset (e.g. \"PLI3\", \"MLI1\", \"5178 CB PLI Gly-Gaba_1\").
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    correspondence: Optional[CorrespondenceType] = Field(default=None, description="""Nature of the source-cluster → classical-type correspondence, copied from the node's declaring `at_source_sets` entry (issue #126). Records whether the annotated source cell set is an EXACT match, a SUBSET (one molecular subtype within the classical type), a SUPERSET, or a PARTIAL overlap — so a lumped/partial correspondence is not read as a clean identity.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AtSourceSet']} })
    best_f1_score: Optional[float] = Field(default=None, description="""F1 score at the best-mapping taxonomy level. Minimum quality metric; use when full metrics_by_level is unavailable. Derive from metrics_by_level[best_mapping_level].f1_score when present.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence']} })
    best_mapping_level: Optional[str] = Field(default=None, description="""Taxonomy level name at which best_f1_score was achieved. E.g. \"SUPERTYPE\" for PLI3→1145 (F1=0.96) vs \"CLUSTER\" for PLI1→5178 (F1=0.94).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence']} })
    best_mapping_rank: Optional[int] = Field(default=None, description="""Taxonomy rank at which best_f1_score was achieved (0 = leaf). Cross-taxonomy-comparable alternative to best_mapping_level.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence']} })
    source_cell_set_accession: Optional[str] = Field(default=None, description="""CCN cell set accession of the source cluster, if available. Populate for cross-Allen-taxonomy transfers where the source node is an atlas cell set with a stable CCN identifier.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence']} })
    n_cells_total: Optional[int] = Field(default=None, description="""Total cells from this cluster before bootstrap filtering""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    n_cells_after_filter: Optional[int] = Field(default=None, description="""Cells retained after bootstrap filtering""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    bootstrap_threshold: Optional[float] = Field(default=None, description="""Bootstrap score cutoff applied (e.g. 0.8 = cells with score <0.8 discarded)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    metrics_by_level: Optional[list[AnnotationTransferLevelResult]] = Field(default=None, description="""Full per-level metrics (optional). Include when multi-level analysis is relevant; omit when best_f1_score suffices. Populated programmatically by `src/evidencell/at_metrics.py` from `kb/annotation_transfer_runs/{run_ref}/at_results.yaml` using (run_ref, source_cluster_label, edge.taxonomy_type). MUST NOT be transcribed by an LLM agent — see the schema description of `AnnotationTransferResultSet` for the rationale. For each level, records the best target the source mapped to; when the edge's taxonomy_type matches the source's best at some level, `best_target_accession` at that level equals `edge.taxonomy_type` (the typical pattern). When it doesn't, the row is informational — the supporting agent should also look up F1 for (source, edge.taxonomy_type) specifically and surface that in the explanation.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence']} })
    f1_source_relpath: Optional[str] = Field(default=None, description="""Path (relative to the AT run dir) of the `AnnotationTransferResultSet` YAML that fed `metrics_by_level` for this evidence item. Defaults to `at_results.yaml` (the canonical base file); used to disambiguate when a run emits multiple variant normalisations (e.g. `at_results_by_class.yaml`).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence']} })
    nt_consistent_with_classical: Optional[bool] = Field(default=None, description="""DEPRECATED in v0.5 — superseded by MappingEdge.property_comparisons. Retained for backward compatibility.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtlasMetadataEvidence', 'AnnotationTransferEvidence']} })
    name_in_source: Optional[str] = Field(default=None, description="""Label of the target cluster as it appears in the target taxonomy (the name the source cluster was mapped to). Preserves the exact source wording for review. E.g. \"49_Vip\", \"7_Lamp5 Lhx6\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'NeurotransmitterType',
                       'AnnotationTransferEvidence']} })
    tool_version: Optional[str] = Field(default=None, description="""Version of tool used, e.g. \"MapMyCells v1.2\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    code_reference: Optional[str] = Field(default=None, description="""URL or accession of the notebook/script that produced these results. E.g. https://github.com/Cellular-Semantics/cellular_semantics_notebooks/tree/main/MLI-PLI%20annotation
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    source_groups: Optional[list[SourceGroup]] = Field(default=None, description="""Optional. When this evidence's metrics were computed by pooling multiple raw source clusters into one pseudo-source, record the composition here. Absence means per-source metrics keyed by source_cluster_label.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class SourceGroup(ConfiguredBaseModel):
    """
    Composition of a pooled pseudo-source used to compute an AnnotationTransferEvidence's metrics. `label` is the pseudo-source name (also the `--pool ...:NAME` argument fed to at_figures); `members` is the list of raw source_label values (as they appear in the f1_matrix.csv source_label column) that were combined. Optional `rationale` records justification that the pool reading is defensible across the available property panels; absence means no such justification is on file.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    label: str = Field(default=..., description="""Pseudo-source name. Must match the `--pool ...:NAME` argument and the source_label key in the figure-rendering sidecar from `at_figures --emit-metrics`, so stored metrics and rendered figure are joinable on a shared key.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm', 'ProposedCLTerm', 'SourceGroup']} })
    members: list[str] = Field(default=..., description="""Raw source_label values (from f1_matrix.csv) combined into the pseudo-source.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceGroup']} })
    rationale: Optional[str] = Field(default=None, description="""Optional. Justification that the pool reading is defensible across the available property panels. May be supplied by a human curator or by a synthesis agent. Multiple independent lines of evidence are encouraged — record each as its own sentence or bullet, with citations to the underlying evidence (AT run id, paper PMID/DOI, edge id, etc.) where applicable. Example justifications (combine where multiple apply):
  - \"Annotation transfer to the target taxonomy is
    indistinguishable between the pooled types: both source
    cohorts map to the same target cluster set with comparable
    F1 distributions (cite run_id).\"
  - \"Literature reports no distinguishing electrophysiology,
    morphology, or connectivity between the pooled types
    (cite paper).\"
  - \"Pooled types share defining markers and neurotransmitter
    type; no differential expression of canonical
    subtype-discriminating genes is reported.\"
  - \"Pool reflects the originating cohort's own grouping
    convention (e.g. shared sample-collection criterion);
    no further cross-panel check has been performed.\"
Absence is not a gate — it just means no justification is on file. A future workflow run may populate or extend the rationale; existing entries should not be overwritten without curator review.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceGroup', 'MappingEdge']} })


class SpatialColocationEvidence(EvidenceItem):
    """
    Evidence from spatial transcriptomics or FISH co-location analysis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    spatial_dataset: Optional[str] = Field(default=None, description="""Dataset accession or publication reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialColocationEvidence']} })
    spatial_technology: Optional[str] = Field(default=None, description="""MERFISH, Visium, seqFISH+, smFISH, FISH, ExSEQ""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialColocationEvidence']} })
    anatomical_region: Optional[OntologyTerm] = Field(default=None, json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'AnatomyTerm'}],
         'domain_of': ['SpatialColocationEvidence']} })
    probes_used: Optional[list[str]] = Field(default=None, description="""Gene probes in the spatial assay""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialColocationEvidence']} })
    colocation_metric: Optional[str] = Field(default=None, description="""Metric: Moran's I, nearest-neighbour distance, co-expression fraction""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialColocationEvidence']} })
    colocation_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialColocationEvidence']} })
    registration_method: Optional[str] = Field(default=None, description="""How cells/spots were registered to CCF, if applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialColocationEvidence']} })
    registration_uncertainty: Optional[bool] = Field(default=None, description="""Set true if registration accuracy is a known concern (adds MERFISH_REGISTRATION_UNCERTAINTY caveat)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialColocationEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class PatchSeqEvidence(EvidenceItem):
    """
    Evidence from patch-seq (simultaneous electrophysiology + morphology + transcriptomics). Can come from atlas-associated datasets or third-party studies.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    dataset_accession: Optional[str] = Field(default=None, description="""Dataset accession, e.g. Allen Cell Types DB, NeMO, DANDI""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence',
                       'ProjectionSeqEvidence',
                       'ElectrophysiologyEvidence',
                       'MorphologyEvidence',
                       'MarkerAnalysisEvidence',
                       'AtSourceSet']} })
    n_cells_matched: Optional[int] = Field(default=None, description="""Number of patch-seq cells matching this type definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence']} })
    transcriptomic_match_score: Optional[float] = Field(default=None, description="""Average transcriptomic correspondence score for matched cells""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence']} })
    morphology_features: Optional[list[str]] = Field(default=None, description="""Morphological features consistent with the type, e.g. \"axonal arborisation in Purkinje layer\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence']} })
    ephys_features: Optional[list[str]] = Field(default=None, description="""Key E-type features, e.g. \"fast-spiking\", \"Rin: 120-180 MOhm\", \"no adaptation\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence']} })
    matched_cluster_id: Optional[str] = Field(default=None, description="""Atlas cluster ID matched by these patch-seq cells""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class ProjectionSeqEvidence(EvidenceItem):
    """
    Evidence from projection-seq or retrograde tracing combined with transcriptomics. Used to link projection target identity with transcriptomic type.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    dataset_accession: Optional[str] = Field(default=None, description="""Dataset accession""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence',
                       'ProjectionSeqEvidence',
                       'ElectrophysiologyEvidence',
                       'MorphologyEvidence',
                       'MarkerAnalysisEvidence',
                       'AtSourceSet']} })
    projection_target: Optional[OntologyTerm] = Field(default=None, description="""Brain region where axons project to""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'AnatomyTerm'}],
         'domain_of': ['ProjectionSeqEvidence']} })
    fraction_projecting: Optional[float] = Field(default=None, description="""Fraction of the cell set with projections to this target""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProjectionSeqEvidence']} })
    method: Optional[str] = Field(default=None, description="""retrograde tracing + scRNAseq, proj-seq, MERFISH + anterograde tracing""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'AnnotationTransferEvidence',
                       'ProjectionSeqEvidence',
                       'MarkerAnalysisEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class ElectrophysiologyEvidence(EvidenceItem):
    """
    Electrophysiology evidence without transcriptomics
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    dataset_accession: Optional[str] = Field(default=None, description="""Dataset or publication reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence',
                       'ProjectionSeqEvidence',
                       'ElectrophysiologyEvidence',
                       'MorphologyEvidence',
                       'MarkerAnalysisEvidence',
                       'AtSourceSet']} })
    etype_label: Optional[str] = Field(default=None, description="""E-type classification label""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyEvidence']} })
    key_features: Optional[list[str]] = Field(default=None, description="""Quantitative features matching the classical type""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyEvidence', 'MorphologyEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class MorphologyEvidence(EvidenceItem):
    """
    Morphological characterisation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    dataset_accession: Optional[str] = Field(default=None, description="""Dataset or publication reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence',
                       'ProjectionSeqEvidence',
                       'ElectrophysiologyEvidence',
                       'MorphologyEvidence',
                       'MarkerAnalysisEvidence',
                       'AtSourceSet']} })
    imaging_method: Optional[str] = Field(default=None, description="""Golgi stain, biocytin fill, EM, expansion microscopy""", json_schema_extra = { "linkml_meta": {'domain_of': ['MorphologyEvidence']} })
    key_features: Optional[list[str]] = Field(default=None, description="""Morphological features, e.g. \"ascending axon collateral\", \"beaded dendrites\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyEvidence', 'MorphologyEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class MarkerAnalysisEvidence(EvidenceItem):
    """
    Custom marker gene overlap analysis (beyond what atlas metadata provides). E.g. intersecting DEG lists between a prior study and an atlas.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    dataset_accession: Optional[str] = Field(default=None, description="""Dataset used for analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence',
                       'ProjectionSeqEvidence',
                       'ElectrophysiologyEvidence',
                       'MorphologyEvidence',
                       'MarkerAnalysisEvidence',
                       'AtSourceSet']} })
    markers_examined: Optional[list[str]] = Field(default=None, description="""Gene symbols examined""", json_schema_extra = { "linkml_meta": {'domain_of': ['MarkerAnalysisEvidence']} })
    overlap_metric: Optional[str] = Field(default=None, description="""Jaccard index (top-50 DEGs), Fisher exact p, AUC, hypergeometric""", json_schema_extra = { "linkml_meta": {'domain_of': ['MarkerAnalysisEvidence']} })
    overlap_value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['MarkerAnalysisEvidence']} })
    method: Optional[str] = Field(default=None, description="""Analysis method, e.g. \"DEG intersection, Seurat FindMarkers\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'AnnotationTransferEvidence',
                       'ProjectionSeqEvidence',
                       'MarkerAnalysisEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class BulkCorrelationEvidence(EvidenceItem):
    """
    Edge evidence linking a mapping target to a CorrelationRun + contrast + free-form statistics map. Parallels AnnotationTransferEvidence in shape: a thin pointer at a separately-stored analysis (kb/correlation_runs/{run_id}/) together with the relevant target accession and the numeric receipts.
    Conventional keys for paired-bulk Spearman analyses (not enforced):
      rho_a, rho_b, delta, rank, rank_total
    Other statistic families (KL divergence, OT distance, regression β, F1) use whatever keys make sense for that family. The CorrelationRun manifest records the statistic_kind that interprets the keys.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    run_ref: str = Field(default=..., description="""CorrelationRun.id (kb/correlation_runs/{run_id}/manifest.yaml)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'BulkCorrelationEvidence']} })
    contrast_ref: str = Field(default=..., description="""CorrelationContrast.id within the referenced run""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkCorrelationEvidence']} })
    target_accession: str = Field(default=..., description="""WMBv1 (or other atlas) cluster/supertype accession the evidence supports""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow', 'BulkCorrelationEvidence']} })
    statistics: Optional[str] = Field(default=None, description="""Free-form name:value map of statistic name → numeric value. YAML-inline mapping. Validated structurally only — key names are conventional, not enforced.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkCorrelationEvidence']} })
    evidence_type: EvidenceType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    supports: EvidenceSupport = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    explanation: str = Field(default=..., description="""Why this evidence supports/refutes/partially supports the mapping. Should be concise and citable — this text feeds the CL comment.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    figure_urls: Optional[list[str]] = Field(default=None, description="""URLs to supporting figures or database screenshots. Use for visual evidence that complements the text explanation, e.g.:
  - Atlas browser views showing spatial distribution across species
  - UMAP/t-SNE plots showing cluster location
  - Dot plots showing marker expression profiles
  - Supplementary data figures from papers
  - OLS/ontology browser entry screenshots
Prefer stable, persistent URLs (DOI-resolved figures, database entry pages). Allen Brain Cell Atlas browser URLs, OLS term pages, and Figshare/Zenodo figure links are all acceptable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker (see ManualCurationMarker class). When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this evidence item verbatim rather than regenerating it. Use to lock a curator-authored evidence item (typically a LiteratureEvidence entry added manually) against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class Caveat(ConfiguredBaseModel):
    """
    A typed caveat about the reliability or completeness of this mapping edge. Caveats are distinct from EvidenceItems: they document limitations, not positive support.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    caveat_type: CaveatType = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Caveat']} })
    description: str = Field(default=..., description="""Specific explanation of this caveat in the context of this mapping. Will appear in the CL comment and community report.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'Caveat',
                       'DiscoveryContext',
                       'CellTypeMappingGraph',
                       'AnnotationTransferDataset',
                       'BulkDataset']} })
    manually_curated: Optional[ManualCurationMarker] = Field(default=None, description="""Optional human-curation marker. When present, downstream mechanical re-emits (e.g. emit-stage-b --rewrite-existing) MUST preserve this caveat verbatim rather than regenerating it. Use to lock a curator-authored caveat against future analysis-pipeline rewrites.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceItem', 'Caveat']} })


class ManualCurationMarker(ConfiguredBaseModel):
    """
    Provenance marker indicating that the containing item is human-authored and should be preserved by mechanical re-emit passes. Attached to mixed-source items (EvidenceItem, Caveat) where mechanical and manual entries can coexist in the same list. Today no curators are writing the KB directly, so this field is rarely populated; future reviewer / curator tooling will set it when committing manual edits.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    by: str = Field(default=..., description="""Curator name or ORCID URI (e.g. \"https://orcid.org/0000-0002-...\").
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManualCurationMarker']} })
    committed_date: date = Field(default=..., description="""Date the manual edit was committed. (Renamed from `date` to avoid a Python name/type collision in the generated Pydantic models — a slot named `date` with `range: date` renders as the non-importable `date: date`.)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ManualCurationMarker']} })
    notes: Optional[str] = Field(default=None, description="""Optional free-text rationale for the manual override. Useful when the manual entry contradicts what a mechanical re-emit would produce.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })


class DiscoveryContext(ConfiguredBaseModel):
    """
    A named percentile context referenced by DiscoveryScore.expression_detail[*].percentiles[*].context_id. Each context describes the population of candidates that defines \"100th percentile\" for that comparison. Critical for downstream readers — \"0.94 of 142 survivors\" is not the same claim as \"0.94 of 5322 atlas-wide clusters\". Without an explicit context registry, percentile values are ambiguous and cannot be interpreted by the report-time agent.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    id: str = Field(default=..., description="""Local identifier (e.g. 'cohort', 'universal', 'anat_hippocampus') referenced by GenePercentile.context_id. Stable within one discovery_score block; not a global ID.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    kind: DiscoveryContextKind = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryContext']} })
    rank: Optional[int] = Field(default=None, description="""Taxonomy rank at which the context is defined (0 = leaf cluster, 1 = supertype, …). For SURVIVAL_COHORT must match the parent DiscoveryScore.rank.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryContext', 'DiscoveryScore']} })
    n_members: int = Field(default=..., description="""Number of candidates in this context. Required for interpreting any percentile — 0.95 of 12 is much weaker discriminator than 0.95 of 500.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryContext']} })
    filters: Optional[list[str]] = Field(default=None, description="""For SURVIVAL_COHORT — the filters that defined survival (e.g. ['region=hippocampal_formation', 'nt_type=Gaba']). Empty for ATLAS_UNIVERSAL. Format is free-text key=value intended for agent consumption, not for programmatic parsing.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryContext']} })
    description: Optional[str] = Field(default=None, description="""Optional human-readable expansion (e.g. 'GABAergic clusters annotated to hippocampal formation closure'). For agent consumption when the structured fields above are insufficient.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'Caveat',
                       'DiscoveryContext',
                       'CellTypeMappingGraph',
                       'AnnotationTransferDataset',
                       'BulkDataset']} })


class GenePercentile(ConfiguredBaseModel):
    """
    A single gene's specificity within one named context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    context_id: str = Field(default=..., description="""References DiscoveryScore.contexts[*].id.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenePercentile']} })
    pct: Optional[float] = Field(default=None, description="""Percentile of val within the context's members (0–1). Interpret with the context's n_members — 0.95 of 12 is a much weaker discriminator than 0.95 of 500. Null when val is null (i.e. source=metadata).
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['GenePercentile']} })


class GeneDiscoveryDetail(ConfiguredBaseModel):
    """
    Stage A's per-gene observation for one queried gene against one candidate. Six fields capture orthogonal aspects: measurement (val, reliable, source), specificity within context(s) (percentiles[]), score contribution before and after modifiers (raw_tier, applied_score), and rank ≥ 1 distribution (coverage). Read all six together; any one in isolation can mislead.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    gene: str = Field(default=..., description="""Gene symbol. A leading '-' marks a NEGATIVE marker — i.e. the cell type was specified to NOT express this gene, and credit is awarded for absence. The prefix survives every downstream surface so the reading polarity is never ambiguous.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiscoveryDetail']} })
    val: Optional[float] = Field(default=None, description="""Precomputed mean expression (log scale) for this gene on this candidate. Null when the gene is not in the precomputed_stats HDF5 (source=metadata).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiscoveryDetail']} })
    reliable: Optional[bool] = Field(default=None, description="""True iff val ≥ MIN_DETECTABLE (currently 1.0). False means the value is at noise floor — for positive markers, treat as 'not actually expressed'; for negative markers, confirms absence.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiscoveryDetail']} })
    raw_tier: Optional[int] = Field(default=None, description="""Integer tier from the cohort-relative scoring table BEFORE any modifiers. Positive markers: +2 (reliable & cohort_pct ≥ 0.95), +1 (reliable, cohort_pct < 0.95), 0 (not reliable). Negative markers: +1 (correctly absent), −1 (present, cohort_pct < 0.95 — contradicts but unsurprising), −2 (cohort_pct ≥ 0.95 — aberrantly high). +1 for metadata-only marker assertions.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiscoveryDetail']} })
    applied_score: Optional[float] = Field(default=None, description="""Score actually contributed to DiscoveryScore.score after modifiers. At rank ≥ 1 the rank-0 coverage dampener (sqrt(coverage)) shrinks raw_tier proportionally, so applied_score = raw_tier × sqrt(coverage) when coverage is populated. At rank 0, applied_score == raw_tier. When applied_score differs from raw_tier, the gap is the modifier signal — investigate `coverage` next.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiscoveryDetail']} })
    source: GeneDiscoverySource = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'GeneDiscoveryDetail',
                       'PrecomputedExpression']} })
    coverage: Optional[float] = Field(default=None, description="""AT RANK ≥ 1 ONLY (null at rank 0). Fraction of this candidate's rank-0 descendants that express the gene at ≥ MIN_DETECTABLE. Reveals whether a supertype-mean is broadly supported (coverage ≈ 0.75 — most children carry the signal) or driven by a minority (coverage ≈ 0.25 — the supertype-mean is misleading; the signal probably belongs to one child cluster). Low coverage at rank ≥ 1 is a HIDDEN-1:1 signal — see §1.2 of the confidence review.
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'GeneDiscoveryDetail']} })
    percentiles: Optional[list[GenePercentile]] = Field(default=None, description="""Per-context specificity records. Today exactly one entry per gene (context_id='cohort'); the list shape is forward-compatible with universal / anatomical context emission.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDiscoveryDetail']} })


class DiscoveryAtSignal(ConfiguredBaseModel):
    """
    Cohort-scoring view of the AT hit that contributed to DiscoveryScore.score. The AUTHORITATIVE AT record lives in MappingEdge.evidence[] as AnnotationTransferEvidence; this block exists only to make the cohort-ranking reasoning auditable — i.e. \"+3 of the discovery score came from an AT F1 ≥ 0.5 hit\".

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    f1: Optional[float] = Field(default=None, ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow', 'DiscoveryAtSignal']} })
    n_cells: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferMetricRow',
                       'DiscoveryAtSignal',
                       'ChildClusterExpression']} })
    target_level: Optional[str] = Field(default=None, description="""Taxonomy level of the AT target (cluster, supertype, …).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryAtSignal']} })
    target_name: Optional[str] = Field(default=None, description="""Name of the AT target the source mapped to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow', 'DiscoveryAtSignal']} })
    score: Optional[int] = Field(default=None, description="""AT bucket contribution to DiscoveryScore.score (+1 / +2 / +3 at F1 thresholds ≥ floor / 0.3 / 0.5).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryAtSignal', 'DiscoveryScore']} })


class DiscoveryScore(ConfiguredBaseModel):
    """
    Stage A find_candidates output recorded on the MappingEdge it produced. A SINGLE SIGNAL AMONG MANY — does NOT re-state overall confidence. Stage A scores cohort-relative gene overlap; it does NOT see AT-pooling caveats, cluster-level region scatter, literature, or morphology. Report-time agents must treat `score` as one input, weighed against marker comparisons, AT metrics, and literature evidence — never as a confidence value. See workflows/gen-report.md \"How to read discovery_score\" for the reader's guide.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    score: Optional[int] = Field(default=None, description="""Composite Stage A score for this candidate. Sum of contributions from: region match (+2), NT match (+2), per-gene marker tiers (see GeneDiscoveryDetail.applied_score), AT-F1 bucket (+1/+2/+3 at thresholds F1 ≥ floor / 0.3 / 0.5), region-exact bonus (+1), optional criteria. Cohort-relative ranking matters more than the absolute number; compare against `next_best_score` and `cohort_size`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryAtSignal', 'DiscoveryScore']} })
    rank_in_cohort: Optional[int] = Field(default=None, description="""1-based rank of this candidate in the discovery cohort (1 = top scorer). Combined with `cohort_size` and `next_best_score`, lets the report-time agent reason about cohort dominance.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    cohort_size: Optional[int] = Field(default=None, description="""Total number of candidates returned by this discovery pass — i.e. members of the SURVIVAL_COHORT context (see contexts[]). Required to interpret `rank_in_cohort` and any `cohort` percentile.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    next_best_score: Optional[int] = Field(default=None, description="""Score of the cohort runner-up. A large gap (e.g. 8 vs 3) indicates the top candidate dominated the cohort; a small gap signals ambiguity between near-tied candidates.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    rank: Optional[int] = Field(default=None, description="""Taxonomy rank queried at Stage A (0 = leaf cluster, 1 = supertype, 2 = subclass, …). Determines whether GeneDiscoveryDetail.coverage is populated (only at rank ≥ 1).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryContext', 'DiscoveryScore']} })
    region_fraction: Optional[float] = Field(default=None, description="""Strict in-region fraction: the candidate's `cell_count` on the curator-queried anat term ÷ the candidate's total spatially-registered cells (= MAX cell_count across the candidate's anat rows, which under KG closure aggregation is the broadest rollup, typically MBA:997 \"brain\"). NOT normalised against `n_cells` — the 10x transcriptomic count and the MERFISH spatial count are different samples and aren't directly comparable. With closure aggregation upstream the numerator is computed against the *highest* matching anat term to avoid double-counting parent + descendant rows. Retained for audit / continuity; new region-presence logic should prefer `region_fraction_100um`.
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    region_fraction_100um: Optional[float] = Field(default=None, description="""Proximity fraction: the candidate's `count_in_or_near_100um` on the queried anat term ÷ the candidate's total spatially-registered cells (= MAX count_in_or_near_100um across its anat rows). The canonical \"what fraction of this candidate's spatial cells sit in or near the target region?\" signal — handles registration-edge cases (CA1 ↔ subiculum etc.) without LLM judgement. Drives the graded region score at Stage A: ≥ 0.5 → +2, ≥ 0.1 → +1, > 0 → +0.5, else 0. None when the candidate has no proximity rows in `effective_anat` (e.g. DESCENDANT_ONLY rescue path) or no spatial registration at all.
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    region_count_completeness: Optional[CellCountCompleteness] = Field(default=None, description="""Provenance of the anat row that produced `region_fraction_100um` (the winning row under MAX-over-matched-rows). Painted CCF2020 leaf domains have no tag here (count is authoritative spatial registration). `exact` flags a trustworthy upstream rollup. `lower_bound` flags a rollup that includes non-painted descendants whose cells aren't counted — the fraction is a floor; downstream agents should caveat citations explicitly.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    region_evidence: Optional[DiscoveryRegionEvidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    contexts: Optional[list[DiscoveryContext]] = Field(default=None, description="""Registry of percentile contexts referenced by expression_detail[*].percentiles[*].context_id. Today only SURVIVAL_COHORT (id='cohort') is emitted; future passes may add ATLAS_UNIVERSAL or ANATOMICAL_RESTRICTION. Each context captures the cohort definition so a reader can interpret a percentile correctly.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    expression_detail: Optional[list[GeneDiscoveryDetail]] = Field(default=None, description="""Per-gene record of what Stage A saw for the genes the curator queried. Negative markers are keyed with a '-' prefix on `gene` (e.g. '-Slc17a7') and earn credit for being ABSENT.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })
    at_signal: Optional[DiscoveryAtSignal] = Field(default=None, description="""Optional. Annotation-transfer hit that contributed to `score`. Cohort-scoring provenance only — the authoritative AT record lives in MappingEdge.evidence[] as AnnotationTransferEvidence.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['DiscoveryScore']} })


class MappingEdge(ConfiguredBaseModel):
    """
    An evidenced mapping assertion between two CellTypeNodes. Edges are directional (lit_type → taxonomy_type) but the relationship field describes the nature of the correspondence, not a hierarchy.
    Transitivity: edges can be chained. E.g.:
      classical_lugaro --[skos:exactMatch, Osorno 2022]--> pli3_osorno
      pli3_osorno --[skos:exactMatch, MapMyCells]--> wmb_supertype_1145

    Cross-cutting: use multiple edges, all pointing at the same taxonomy_type:
      classical_basket   --[evidencell:CrossCuttingMatch]--> mli1_kozareva
      classical_stellate --[evidencell:PartialOverlapMatch]--> mli1_kozareva

    Splits / merges: use one edge per pair, all with skos:broadMatch (split) or skos:narrowMatch (merge), each carrying mapping_cardinality 1:n or n:1.
    Phase 2 schema overhaul (2026-05-12): type_a → lit_type, type_b → taxonomy_type. The old slot names are retained as deprecated aliases for the PR1 → PR2 transition window; drop after KB sweep completes.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    id: str = Field(default=..., description="""Unique edge ID, e.g. \"edge_lugaro_to_pli3\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    lit_type: str = Field(default=..., description="""ID of the source node (reference to CellTypeNode.id). Typically a curated literature / classical type. Renamed from `type_a` in the Phase 2 schema overhaul (PR2 KB sweep, 2026-05-12).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    taxonomy_type: str = Field(default=..., description="""ID of the target node (reference to CellTypeNode.id). Typically an atlas / transcriptomic taxonomy node. For atlas/taxonomy nodes, use the cell_set_accession as the id (e.g. CS20230722_SUPT_0179). The node must be declared in the graph's nodes list — a minimal stub (id, name, definition_basis, taxonomy_id, cell_set_accession) suffices for taxonomy references. Renamed from `type_b` in the Phase 2 schema overhaul (PR2 KB sweep, 2026-05-12).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    relationship: MappingRelationship = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    mapping_cardinality: Optional[MappingCardinality] = Field(default=None, description="""Cardinality of the mapping as a set relation. Required when relationship is skos:broadMatch or skos:narrowMatch; recommended on skos:exactMatch / skos:closeMatch (typically 1:1). Phase 2 schema overhaul (2026-05-12).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    mapping_justification: Optional[MappingJustification] = Field(default=None, description="""Provenance of the mapping decision. Default for new edges: semapv:UnreviewedManualMapping. Promote to semapv:ManualMappingCuration on curator review. Phase 2 schema overhaul (2026-05-12).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    confidence: Optional[MappingConfidence] = Field(default=None, description="""Ordinal mapping verdict. Phase 3 (2026-05-13): authority for this slot moved from Stage B (map-cell-type Step 3 synthesis) to report time (gen-report synthesis). Set by the report-gen agent alongside `confidence_score`, `rationale`, and the `rationale_*` provenance fields. Optional (`required: false`) because edges that have not been through report generation carry no headline verdict — honest state, not a regression. Pre-Phase-3 edges were swept clear of `confidence` in the Phase 3 invalidation migration; they regain it on the first gen-report pass. Spreadsheet / CAP exports should render edges with no confidence as \"(verdict pending)\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    confidence_score: Optional[float] = Field(default=None, description="""Numeric confidence (0-1). Phase 3 (2026-05-13): written by the report-time agent alongside the ordinal `confidence`; the two agree by construction. Not curator-derived; no ordinal → numeric fallback. SSSOM-compatible.
""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    rationale: Optional[str] = Field(default=None, description="""Short prose verdict distilled from the full report by the report-time agent. Phase 3 (2026-05-13). Format constraint: must cite specific structured fields (F1 values, accessions, marker counts) rather than free-form claims; an automated post-write check parses these citations and verifies them against the edge's structured data and references. The agent MUST NOT read prior `rationale` / `confidence` / `confidence_score` as input when regenerating — inputs are structured data + evidence + property_comparisons + the pool-candidates pre-pass.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceGroup', 'MappingEdge']} })
    report_path: Optional[str] = Field(default=None, description="""Relative path or URL to the full report that backs the `rationale`. Phase 3 (2026-05-13). Written by the report-gen orchestrator at write-back time.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    rationale_generated_at: Optional[datetime ] = Field(default=None, description="""Timestamp at which the report-time agent wrote `rationale`. Phase 3 (2026-05-13).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    rationale_source_hash: Optional[str] = Field(default=None, description="""SHA256 8-char digest over the canonical edge + endpoint-node payload at rationale-generation time (excluding the rationale-suite fields themselves). On every read and on `just qc`, the hash is recomputed from current state and compared; mismatch marks the rationale stale (still shown, flagged for regeneration). Whole-edge granularity — any change in the hashed inputs invalidates the whole rationale. Phase 3 (2026-05-13).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    reconciliation_note: Optional[str] = Field(default=None, description="""Structured cross-edge note. Two uses: (1) Phase 2 framing — curator's synthesis when parallel evidence sources DISAGREE (e.g. divergent F1 from two AT runs on different datasets, or marker evidence pointing one way while anatomy points another); distinct from per-property notes / rationale fields. (2) Phase 3 (2026-05-13) extension — agent-side cross-edge indistinguishability note. When the report-time agent calls two source groups indistinguishable across available property panels (the Winterer Sst-OLM / Htr3a-OLM pattern; see #61, #62), the structured cross-reference goes here while the per-edge narrative goes in `rationale`. Paired with a lit-to-lit `skos:closeMatch` edge when the indistinguishability spans all available panels (not just AT).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    reviewed_by: Optional[str] = Field(default=None, description="""Name or ORCID of the human reviewer who confirmed this edge, distinct from the curator who created or last edited the record. Phase 2 schema overhaul (2026-05-12).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    discovery_score: Optional[DiscoveryScore] = Field(default=None, description="""Stage A find_candidates output for this candidate, recorded verbatim on the edge that consumed it. A single signal among many — NOT a re-statement of overall confidence. See the DiscoveryScore class description and the gen-report \"How to read discovery_score\" prompt for reader guidance. Populated by Stage B at edge creation (workflows/map-cell-type.md Step 3) or by backfill from on-disk discovery JSONs (just backfill-discovery-score). Optional — edges that predate the discovery JSON convention will have no value.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    evidence: list[EvidenceItem] = Field(default=..., description="""All evidence items directly supporting this specific edge (min 1)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    property_comparisons: Optional[list[PropertyComparison]] = Field(default=None, description="""Structured property-by-property comparison between lit_type and taxonomy_type. Makes the basis for the confidence judgment machine-readable and surfaceable in reports. Populate at minimum: nt_type, location, and all defining markers. Use NOT_ASSESSED where data is unavailable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    caveats: Optional[list[Caveat]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge', 'CorrelationRun', 'AnnotationTransferRun']} })
    unresolved_questions: Optional[list[str]] = Field(default=None, description="""Specific outstanding questions about this edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    proposed_experiments: Optional[list[str]] = Field(default=None, description="""Experiments that would resolve or strengthen this edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    curator: Optional[str] = Field(default=None, description="""Name or ORCID of person who curated this edge""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge']} })
    creation_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge', 'CellTypeMappingGraph']} })
    updated_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge', 'CellTypeMappingGraph']} })


class CellTypeMappingGraph(ConfiguredBaseModel):
    """
    A graph of cell type mapping evidence for a brain region or cell class. Contains CellTypeNodes (classical types, prior T-types, atlas cell sets) connected by MappingEdges (each with evidence and confidence). Terminal nodes (is_terminal=true) are community atlas cell sets.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5',
         'tree_root': True})

    name: str = Field(default=..., description="""e.g. \"Cerebellar cortex interneurons — WMBv1\", \"Basal ganglia GPi types — HMBA\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyNode', 'CellTypeNode', 'CellTypeMappingGraph']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'Caveat',
                       'DiscoveryContext',
                       'CellTypeMappingGraph',
                       'AnnotationTransferDataset',
                       'BulkDataset']} })
    brain_region: Optional[OntologyTerm] = Field(default=None, description="""Brain region covered by this evidence graph. OntologyTerm with Allen atlas term preferred (MBA/DHBA); UBERON as fallback.
""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'AnatomyTerm'}],
         'domain_of': ['CellTypeMappingGraph']} })
    target_atlas: str = Field(default=..., description="""The community atlas that terminal nodes belong to""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence',
                       'CellTypeMappingGraph',
                       'AnnotationTransferRun']} })
    species: Optional[OntologyTerm] = Field(default=None, description="""Primary species (NCBITaxon)""", json_schema_extra = { "linkml_meta": {'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'REQUIRED',
                       'range': 'NCBITaxonClassTerm'}],
         'domain_of': ['CellTypeNode', 'CellTypeMappingGraph', 'BulkDataset']} })
    nodes: list[CellTypeNode] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeMappingGraph', 'TaxonomyNodeList']} })
    edges: list[MappingEdge] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeMappingGraph']} })
    creation_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge', 'CellTypeMappingGraph']} })
    updated_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge', 'CellTypeMappingGraph']} })
    notes: Optional[str] = Field(default=None, description="""Free-text notes about scope, limitations, or outstanding issues""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })
    source_atlas: Optional[str] = Field(default=None, description="""When this graph represents cross-taxonomy annotation transfer, the atlas that nodes were transferred FROM (the source taxonomy). E.g. \"WMBv1 (CCN20230722)\" for WMB→CTX-HPF transfers.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeMappingGraph']} })
    annotation_transfer_datasets: Optional[list[AnnotationTransferDataset]] = Field(default=None, description="""Datasets used or planned for annotation transfer experiments targeting cell types in this graph. Tracked at graph level so multiple nodes can reference the same dataset.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeMappingGraph']} })


class AnnotationTransferDataset(ConfiguredBaseModel):
    """
    A dataset used for annotation transfer (MapMyCells or equivalent). Tracked at graph level to avoid duplication across nodes.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    accession: str = Field(default=..., description="""Dataset accession, e.g. \"GEO:GSE142546\", \"SCP795\".
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferDataset']} })
    publication: Optional[str] = Field(default=None, description="""DOI or PMID of the associated publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferDataset']} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the dataset and its relevance""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'Caveat',
                       'DiscoveryContext',
                       'CellTypeMappingGraph',
                       'AnnotationTransferDataset',
                       'BulkDataset']} })
    cell_types: Optional[list[str]] = Field(default=None, description="""Node IDs (within this graph) that this dataset targets.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferDataset']} })
    status: Optional[str] = Field(default=None, description="""Processing status, e.g. \"pending_retrieval\", \"processed\", \"awaiting_sra_reprocessing\". Free text.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProposedCLTerm', 'AnnotationTransferDataset']} })

    @field_validator('publication')
    def pattern_publication(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|https://doi\.org/.+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publication format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publication format: {v}"
            raise ValueError(err_msg)
        return v


class AtSourceSet(ConfiguredBaseModel):
    """
    A single (dataset, annotated-cell-set) correspondence declared on a CellTypeNode: an annotated cell set in an external dataset that corresponds to this classical cell type. Encodes the agentic judgement (recovered here; lost when candidate selection became programmatic in #96) of which source annotation maps to which literature type — a judgement that requires reading the dataset's describing paper, not transcriptomic overlap. `emit-stage-b` resolves the AT run operationally from (dataset_accession, target_taxonomy, source_label) and emits one ANNOTATION_TRANSFER evidence item per entry. A type may declare several entries (lumping across source clusters, or spanning datasets); each becomes an independent AT evidence item.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    dataset_accession: str = Field(default=..., description="""Accession of the source dataset, e.g. \"ArrayExpress:E-MTAB-12096\", \"GEO:GSE142546\". Together with source_label this is stable biology from the paper; the AT run supplying the numbers is resolved at map time and is NOT recorded on the node.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PatchSeqEvidence',
                       'ProjectionSeqEvidence',
                       'ElectrophysiologyEvidence',
                       'MorphologyEvidence',
                       'MarkerAnalysisEvidence',
                       'AtSourceSet']} })
    source_label: str = Field(default=..., description="""Annotated cluster label in the source dataset, as it appears in the paper and in the AT run's result rows, e.g. \"GABA-52-Calb2-Rgs12\". This is the real key used to disambiguate among AT runs of the same dataset against the same taxonomy.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferMetricRow', 'AtSourceSet']} })
    correspondence: Optional[CorrespondenceType] = Field(default=None, description="""Nature of the source-cluster → classical-type match, so a lumped or partial correspondence is not read as a clean identity.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AtSourceSet']} })
    sources: Optional[list[PropertySource]] = Field(default=None, description="""Quote-backed provenance for the correspondence — the verbatim paper quote(s) justifying \"this annotated cell set corresponds to this classical type\". Same shape and validation as defining_markers / anatomical_location sources (hook-validated against references.json). The load-bearing justification lives here, not in notes.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnatomicalLocation',
                       'GeneDescriptor',
                       'TypeSynonym',
                       'ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'NeurotransmitterType',
                       'AtSourceSet']} })
    notes: Optional[str] = Field(default=None, description="""Free-text colour (heterogeneity observations, cross-references). Not the load-bearing justification — that belongs in sources.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })


class PrecomputedExpression(ConfiguredBaseModel):
    """
    Precomputed expression statistics for key genes from the atlas taxonomy. Used for scoring property comparisons on mapping edges — e.g. \"does the atlas cluster express the classical type's defining markers?\"

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    source: str = Field(default=..., description="""Source file or dataset for the precomputed stats. E.g. \"precomputed_stats_ABC_revision_230821.h5\"
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'GeneDiscoveryDetail',
                       'PrecomputedExpression']} })
    level: Optional[str] = Field(default=None, description="""Taxonomy level these stats correspond to. E.g. \"cluster\", \"supertype\"
""", json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyNode', 'PrecomputedExpression']} })
    genes: Optional[list[GeneExpression]] = Field(default=None, description="""Per-gene expression statistics for this node.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrecomputedExpression']} })
    child_cluster_expression: Optional[list[ChildClusterExpression]] = Field(default=None, description="""Per-child-cluster expression breakdown (supertype nodes only). Enables scoring to inspect cluster-level heterogeneity.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrecomputedExpression']} })


class ChildClusterExpression(ConfiguredBaseModel):
    """
    Per-child-cluster expression breakdown for a supertype node. Enables mapping-edge scoring to inspect cluster-level heterogeneity within a supertype.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    cluster_accession: str = Field(default=..., description="""Cell set accession of the child cluster""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChildClusterExpression']} })
    n_cells: Optional[int] = Field(default=None, description="""Number of cells in this cluster""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferMetricRow',
                       'DiscoveryAtSignal',
                       'ChildClusterExpression']} })
    expression: Optional[str] = Field(default=None, description="""Gene symbol → mean expression mapping. Stored as a flat dict; keys are gene symbols, values are floats.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChildClusterExpression']} })


class GeneExpression(ConfiguredBaseModel):
    """
    Expression level of a single gene in a cell type or cluster. Minimal record: gene symbol + mean expression value.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    symbol: str = Field(default=..., description="""Gene symbol, e.g. \"Sst\", \"Pvalb\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneDescriptor', 'GeneExpression']} })
    ensembl_id: Optional[str] = Field(default=None, description="""Ensembl gene ID, e.g. \"ENSMUSG00000004366\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpression']} })
    mean_expression: Optional[float] = Field(default=None, description="""Mean expression value (log-normalised or CPM, depending on source)""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeneExpression']} })


class TaxonomyNodeList(ConfiguredBaseModel):
    """
    Container for per-level atlas taxonomy node files (e.g. cluster.yaml, supertype.yaml). Each file holds all CellTypeNode objects at one taxonomy level for one taxonomy. No edges or brain_region required — these are reference nodes, not a mapping graph.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    taxonomy_id: str = Field(default=..., description="""Taxonomy identifier, e.g. CCN20230722""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferResultSet',
                       'TaxonomyNodeList',
                       'AtlasReference']} })
    taxonomy_level: str = Field(default=..., description="""Level string for all nodes in this file, e.g. cluster, supertype""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'TaxonomyNodeList']} })
    taxonomy_rank: Optional[int] = Field(default=None, description="""Integer rank for this level. 0 = most specific (leaf/terminal), incrementing toward root. Required on hierarchical level files; omit for orthogonal annotation levels (e.g. NEUROTRANSMITTER) that sit outside the hierarchy.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferLevelResult',
                       'AnnotationTransferMetricRow',
                       'TaxonomyNodeList']} })
    nodes: list[CellTypeNode] = Field(default=..., description="""All CellTypeNode objects at this taxonomy level""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeMappingGraph', 'TaxonomyNodeList']} })


class BulkDataset(ConfiguredBaseModel):
    """
    A published bulk transcriptomic dataset that profiles labelled cell populations. First-class entity, reusable across many MappingEdges. Lives at kb/datasets/{dataset_id}.yaml.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5',
         'tree_root': True})

    id: str = Field(default=..., description="""Stable dataset identifier, e.g. dataset_GSE183092""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    record_type: Literal["BulkDataset"] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset', 'CorrelationRun', 'AnnotationTransferRun'],
         'equals_string': 'BulkDataset'} })
    source_pmid: Optional[str] = Field(default=None, description="""PubMed ID of the source publication""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    geo_accession: Optional[str] = Field(default=None, description="""GEO series accession, e.g. GSE183092""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    authors: Optional[list[str]] = Field(default=None, description="""Authors of the source publication, full names, in publication order. Used by the renderer to format a citation line for evidence items that cite this dataset via run_ref. Optional — if absent, the citation falls back to the bare PMID.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    year: Optional[int] = Field(default=None, description="""Publication year of the source publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    title: Optional[str] = Field(default=None, description="""Title of the source publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    technique: str = Field(default=..., description="""TRAP-seq, FACS-bulk, RiboTag, INTACT, laser-capture, manual-pick, FANS, ...""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    species: Optional[str] = Field(default=None, description="""NCBITaxon CURIE, e.g. NCBITaxon:10090""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode', 'CellTypeMappingGraph', 'BulkDataset']} })
    ingested_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the experimental design and what was profiled""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectrophysiologyProfile',
                       'MorphologyProfile',
                       'Caveat',
                       'DiscoveryContext',
                       'CellTypeMappingGraph',
                       'AnnotationTransferDataset',
                       'BulkDataset']} })
    data_files: Optional[list[BulkDataFile]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    pools: Optional[list[BulkPool]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset']} })
    notes: Optional[str] = Field(default=None, description="""Free-text notes (caveats, related datasets, scope limitations)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeColocation',
                       'PropertySource',
                       'PropertyComparison',
                       'CellTypeNode',
                       'ManualCurationMarker',
                       'CellTypeMappingGraph',
                       'AtSourceSet',
                       'BulkDataset']} })
    metadata: Optional[str] = Field(default=None, description="""Free-form name:value map for ancillary properties not captured elsewhere. YAML-inline mapping; key names not enforced.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset',
                       'BulkDataFile',
                       'BulkPool',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })

    @field_validator('source_pmid')
    def pattern_source_pmid(cls, v):
        pattern=re.compile(r"^PMID:[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid source_pmid format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid source_pmid format: {v}"
            raise ValueError(err_msg)
        return v


class BulkDataFile(ConfiguredBaseModel):
    """
    A single data file within a BulkDataset (typically one expression matrix).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    relpath: str = Field(default=..., description="""Path relative to the dataset's home (or to a standard cache location)""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataFile', 'ScriptReference', 'OutputReference']} })
    url: Optional[str] = Field(default=None, description="""Canonical URL where this file can be re-fetched""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataFile']} })
    sha256: Optional[str] = Field(default=None, description="""SHA-256 checksum of the file""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataFile', 'AtlasReference']} })
    keyed_by: Optional[str] = Field(default=None, description="""ensembl_id, gene_symbol, refseq, ...""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataFile']} })
    normalisation: Optional[str] = Field(default=None, description="""DESeq2_size_factor, log2(TPM+1), CPM, raw_counts, ...""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferResultSet', 'BulkDataFile']} })
    metadata: Optional[str] = Field(default=None, description="""Free-form name:value map for file-specific notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset',
                       'BulkDataFile',
                       'BulkPool',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })


class BulkPool(ConfiguredBaseModel):
    """
    A labelled bulk sample group within a BulkDataset. Replicates may be averaged or kept; n_replicates records the underlying biological N.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    id: str = Field(default=..., description="""Stable pool identifier, e.g. knoedler_VMH_FR""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    tissue: Optional[str] = Field(default=None, description="""Source tissue / region (free string; promote to OntologyTerm in future)""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkPool']} })
    sort_marker: Optional[str] = Field(default=None, description="""Esr1+, Kiss1+, Th-Cre/Esr1+, ...""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkPool']} })
    state: Optional[str] = Field(default=None, description="""Animal state at sampling — male, female_receptive, naive, post-stress, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkPool']} })
    n_replicates: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BulkPool']} })
    anatomy_id: Optional[str] = Field(default=None, description="""Optional MBA/UBERON CURIE if the tissue maps to a known atlas region""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkPool']} })
    metadata: Optional[str] = Field(default=None, description="""Free-form name:value map (animal age, gating strategy, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset',
                       'BulkDataFile',
                       'BulkPool',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })


class CorrelationRun(ConfiguredBaseModel):
    """
    A specific correlation analysis between BulkPools and an atlas pseudobulk. Lives at kb/correlation_runs/{run_id}/manifest.yaml alongside the script, data inputs, and ranked output files.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5',
         'tree_root': True})

    id: str = Field(default=..., description="""Stable run identifier, e.g. corr_run_20260428_knoedler_wmbv1""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    record_type: Literal["CorrelationRun"] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset', 'CorrelationRun', 'AnnotationTransferRun'],
         'equals_string': 'CorrelationRun'} })
    dataset_ref: str = Field(default=..., description="""BulkDataset.id this run analyses""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationRun']} })
    atlas: AtlasReference = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AtlasMetadataEvidence',
                       'AtlasQueryEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    method: CorrelationMethod = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'AnnotationTransferEvidence',
                       'ProjectionSeqEvidence',
                       'MarkerAnalysisEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    contrasts: list[CorrelationContrast] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationRun']} })
    script: Optional[ScriptReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationRun', 'AnnotationTransferRun']} })
    output: Optional[OutputReference] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationRun', 'AnnotationTransferRun']} })
    caveats: Optional[str] = Field(default=None, description="""Free-text caveats about run-specific findings (e.g. artefact patterns observed)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge', 'CorrelationRun', 'AnnotationTransferRun']} })
    code_version: Optional[str] = Field(default=None, description="""Codebase version (commit SHA, tag, or version string) at the time the run was executed. Optional — script.git_commit covers the per-script version; this field is for the broader codebase if different.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationRun', 'AnnotationTransferRun']} })
    metadata: Optional[str] = Field(default=None, description="""Free-form name:value map for ancillary run-level notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset',
                       'BulkDataFile',
                       'BulkPool',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })


class AtlasReference(ConfiguredBaseModel):
    """
    Reference to an atlas version + pseudobulk source used in a correlation run.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    taxonomy_id: str = Field(default=..., description="""e.g. CCN20230722""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AnnotationTransferResultSet',
                       'TaxonomyNodeList',
                       'AtlasReference']} })
    pseudobulk_source: Optional[str] = Field(default=None, description="""Path or URL to the precomputed_stats.h5 (or equivalent)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtlasReference']} })
    sha256: Optional[str] = Field(default=None, description="""SHA-256 of the pseudobulk source file (for reproducibility)""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataFile', 'AtlasReference']} })


class CorrelationMethod(ConfiguredBaseModel):
    """
    The statistic family and parameters used in a correlation run.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    statistic_kind: str = Field(default=..., description="""Free string naming the statistic family. Examples: spearman_rho, pearson_r, kl_divergence, ot_distance, regression_beta.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationMethod']} })
    parameters: Optional[str] = Field(default=None, description="""Free-form name:value map of method parameters (transform, gene set restriction, normalisation choices, etc.).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationMethod']} })


class CorrelationContrast(ConfiguredBaseModel):
    """
    A named contrast between two BulkPools within a CorrelationRun. The differential δ statistic = stat(cluster, pool_a) − stat(cluster, pool_b) ranks clusters by pool_a-specificity.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    id: str = Field(default=..., description="""Stable contrast identifier, e.g. corr_VMH_FR_vs_BNST_FR""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    pool_a: str = Field(default=..., description="""BulkPool.id (the \"specific\" pool — positive δ favours this)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationContrast']} })
    pool_b: str = Field(default=..., description="""BulkPool.id (the \"background\" pool)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationContrast']} })
    interpretation: Optional[str] = Field(default=None, description="""One-line free text describing what this contrast probes biologically""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationContrast']} })


class ScriptReference(ConfiguredBaseModel):
    """
    Pointer to the script that produced a CorrelationRun's output.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    relpath: str = Field(default=..., description="""Path relative to the run directory""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataFile', 'ScriptReference', 'OutputReference']} })
    python_version: Optional[str] = Field(default=None, description="""e.g. \">=3.11\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScriptReference']} })
    packages: Optional[list[str]] = Field(default=None, description="""Required Python packages (no version pins necessary)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScriptReference']} })
    git_repo_url: Optional[str] = Field(default=None, description="""Canonical repository URL where the script lives. Combined with git_commit + relpath gives a stable permalink for audit. E.g. https://github.com/Cellular-Semantics/evidencell
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScriptReference']} })
    git_commit: Optional[str] = Field(default=None, description="""Commit SHA, short SHA, or tag pinning the exact version of the script that was run. With git_repo_url + relpath, lets a reader form a permalink to the code that produced the run's output.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScriptReference']} })

    @field_validator('git_repo_url')
    def pattern_git_repo_url(cls, v):
        pattern=re.compile(r"^https://(github|gitlab)\.com/.+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid git_repo_url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid git_repo_url format: {v}"
            raise ValueError(err_msg)
        return v


class OutputReference(ConfiguredBaseModel):
    """
    Pointer to the primary ranked output file of a CorrelationRun.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    relpath: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataFile', 'ScriptReference', 'OutputReference']} })
    format: Optional[str] = Field(default=None, description="""tsv, csv, parquet, ...""", json_schema_extra = { "linkml_meta": {'domain_of': ['OutputReference']} })


class AnnotationTransferRunSummary(ConfiguredBaseModel):
    """
    Thin summary entry for one AT run in the registry index. Each entry corresponds to a full AnnotationTransferRun manifest at manifest_path.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5'})

    id: str = Field(default=..., description="""Run identifier — matches AnnotationTransferRun.id""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    target_taxonomy_id: Optional[str] = Field(default=None, description="""Taxonomy the cells were mapped to, e.g. CCN20230722""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferRunSummary', 'AnnotationTransferRun']} })
    source_dataset_accession: Optional[str] = Field(default=None, description="""Accession of the source dataset, e.g. GEO:GSE124847""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    manifest_path: str = Field(default=..., description="""Repo-relative path to the run's manifest.yaml""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferRunSummary']} })


class AnnotationTransferIndex(ConfiguredBaseModel):
    """
    Registry of all annotation-transfer runs in this repo. Lives at kb/annotation_transfer_runs/index.yaml. Auto-generated by `just register-at-run`; do not edit manually. Validated by the pre-write hook: every run_ref in KB YAML must resolve to an entry here.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5',
         'tree_root': True})

    runs: Optional[list[AnnotationTransferRunSummary]] = Field(default=None, description="""One entry per registered AT run, ordered by id.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferIndex']} })


class AnnotationTransferRun(ConfiguredBaseModel):
    """
    A specific annotation-transfer analysis (typically MapMyCells against an atlas pseudobulk). Lives at kb/annotation_transfer_runs/{run_id}/manifest.yaml alongside the F1 matrix, the input h5ad, the script, and any figures.
    Mirrors CorrelationRun in structure: each AnnotationTransferEvidence item on a MappingEdge is a thin pointer at one row of this run's F1 matrix (target_accession × source_label), with the run carrying the full provenance (input data SHA, atlas SHA, method version, code version, figures). Promotes per-evidence inline metadata (method, tool_version, code_reference, bootstrap_threshold...) to a single shared record.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/v0.5',
         'tree_root': True})

    id: str = Field(default=..., description="""Stable run identifier, e.g. at_run_20260408_winterer_olm_mmc_wmbv1""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyTerm',
                       'CellTypeNode',
                       'DiscoveryContext',
                       'MappingEdge',
                       'BulkDataset',
                       'BulkPool',
                       'CorrelationRun',
                       'CorrelationContrast',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    record_type: Literal["AnnotationTransferRun"] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset', 'CorrelationRun', 'AnnotationTransferRun'],
         'equals_string': 'AnnotationTransferRun'} })
    source_dataset_accession: Optional[str] = Field(default=None, description="""Accession of the source dataset, e.g. GEO:GSE124847""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence',
                       'AnnotationTransferRunSummary',
                       'AnnotationTransferRun']} })
    source_cluster_label: Optional[str] = Field(default=None, description="""Source cluster label or grouping convention used in the run (free string; may differ across runs of the same source dataset).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    source_species: Optional[str] = Field(default=None, description="""NCBITaxon CURIE of the source dataset species""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    target_atlas: str = Field(default=..., description="""Atlas the cells were mapped to, e.g. \"WMBv1\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence',
                       'CellTypeMappingGraph',
                       'AnnotationTransferRun']} })
    target_taxonomy_id: Optional[str] = Field(default=None, description="""e.g. CCN20230722 (when target_atlas has a versioned taxonomy id)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferRunSummary', 'AnnotationTransferRun']} })
    target_species: Optional[str] = Field(default=None, description="""NCBITaxon CURIE of the target atlas species""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    method: str = Field(default=..., description="""e.g. \"MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization)\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertySource',
                       'AnnotationTransferEvidence',
                       'ProjectionSeqEvidence',
                       'MarkerAnalysisEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    tool_version: Optional[str] = Field(default=None, description="""Specific tool version, e.g. \"cell_type_mapper v1.7.1\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    code_reference: Optional[str] = Field(default=None, description="""URL of the run's notebook or script (canonical link)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    bootstrap_threshold: Optional[float] = Field(default=None, description="""Bootstrap score cutoff applied (0–1)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    n_cells_total: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    n_cells_after_filter: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferEvidence', 'AnnotationTransferRun']} })
    atlas: Optional[AtlasReference] = Field(default=None, description="""Atlas pseudobulk + SHA (mirrors CorrelationRun.atlas)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CellTypeNode',
                       'AtlasMetadataEvidence',
                       'AtlasQueryEvidence',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })
    script: Optional[ScriptReference] = Field(default=None, description="""Script that produced the F1 matrix. Carries git_repo_url + git_commit + relpath for stable permalinks.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationRun', 'AnnotationTransferRun']} })
    output: Optional[OutputReference] = Field(default=None, description="""Primary ranked output (typically f1_matrix.tsv)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationRun', 'AnnotationTransferRun']} })
    figure: Optional[OutputReference] = Field(default=None, description="""Optional pre-rendered figure (e.g. faceted F1 heatmap). relpath is relative to the run directory.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AnnotationTransferRun']} })
    code_version: Optional[str] = Field(default=None, description="""Codebase commit/tag for the run""", json_schema_extra = { "linkml_meta": {'domain_of': ['CorrelationRun', 'AnnotationTransferRun']} })
    caveats: Optional[str] = Field(default=None, description="""Free-text caveats about run-specific findings""", json_schema_extra = { "linkml_meta": {'domain_of': ['MappingEdge', 'CorrelationRun', 'AnnotationTransferRun']} })
    metadata: Optional[str] = Field(default=None, description="""Free-form name:value map for ancillary run-level notes""", json_schema_extra = { "linkml_meta": {'domain_of': ['BulkDataset',
                       'BulkDataFile',
                       'BulkPool',
                       'CorrelationRun',
                       'AnnotationTransferRun']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
OntologyTerm.model_rebuild()
AnatomicalLocation.model_rebuild()
CLMapping.model_rebuild()
GeneDescriptor.model_rebuild()
CellTypeColocation.model_rebuild()
HasMarkerType.model_rebuild()
PropertySource.model_rebuild()
TypeSynonym.model_rebuild()
MarkerSource.model_rebuild()
ElectrophysiologyProfile.model_rebuild()
MorphologyProfile.model_rebuild()
NeurotransmitterType.model_rebuild()
PropertyComparison.model_rebuild()
HierarchyNode.model_rebuild()
ProposedCLTerm.model_rebuild()
CellTypeNode.model_rebuild()
EvidenceItem.model_rebuild()
LiteratureEvidence.model_rebuild()
AtlasMetadataEvidence.model_rebuild()
AtlasQueryEvidence.model_rebuild()
AnnotationTransferLevelResult.model_rebuild()
AnnotationTransferMetricRow.model_rebuild()
AnnotationTransferResultSet.model_rebuild()
AnnotationTransferEvidence.model_rebuild()
SourceGroup.model_rebuild()
SpatialColocationEvidence.model_rebuild()
PatchSeqEvidence.model_rebuild()
ProjectionSeqEvidence.model_rebuild()
ElectrophysiologyEvidence.model_rebuild()
MorphologyEvidence.model_rebuild()
MarkerAnalysisEvidence.model_rebuild()
BulkCorrelationEvidence.model_rebuild()
Caveat.model_rebuild()
ManualCurationMarker.model_rebuild()
DiscoveryContext.model_rebuild()
GenePercentile.model_rebuild()
GeneDiscoveryDetail.model_rebuild()
DiscoveryAtSignal.model_rebuild()
DiscoveryScore.model_rebuild()
MappingEdge.model_rebuild()
CellTypeMappingGraph.model_rebuild()
AnnotationTransferDataset.model_rebuild()
AtSourceSet.model_rebuild()
PrecomputedExpression.model_rebuild()
ChildClusterExpression.model_rebuild()
GeneExpression.model_rebuild()
TaxonomyNodeList.model_rebuild()
BulkDataset.model_rebuild()
BulkDataFile.model_rebuild()
BulkPool.model_rebuild()
CorrelationRun.model_rebuild()
AtlasReference.model_rebuild()
CorrelationMethod.model_rebuild()
CorrelationContrast.model_rebuild()
ScriptReference.model_rebuild()
OutputReference.model_rebuild()
AnnotationTransferRunSummary.model_rebuild()
AnnotationTransferIndex.model_rebuild()
AnnotationTransferRun.model_rebuild()
