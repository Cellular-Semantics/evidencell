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


metamodel_version = "1.12.0"
version = "0.1.1"


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


linkml_meta = LinkMLMeta({'default_prefix': 'https://bican.org/schema/celltype-evidence/references/v0.1/',
     'default_range': 'string',
     'description': 'Schema for the evidencell reference store: papers, their '
                    'verbatim quotes, and the deepsearch documents quotes were '
                    'extracted from.\n',
     'id': 'https://bican.org/schema/celltype-evidence/references/v0.1',
     'imports': ['linkml:types'],
     'name': 'EvidencellReferences',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'schema/references.yaml'} )

class SourceMethod(str, Enum):
    """
    How a quote's text was obtained. This is an evidence-strength distinction, not bookkeeping: ASTA_REPORT text is ASTA's prose about a paper, whereas the full-text and abstract methods are text from the paper itself. A quote whose method is ASTA_REPORT should carry a source_document identifying which report it came from.

    """
    ASTA_REPORT = "ASTA_REPORT"
    """
    Taken from an ASTA deep-research PDF, which summarises and paraphrases the cited paper. Not necessarily verbatim from the paper.

    """
    ASTA_SNIPPET = "ASTA_SNIPPET"
    """
    Retrieved via Semantic Scholar snippet_search over the ASTA corpus.
    """
    EUROPEPMC_FULLTEXT = "EUROPEPMC_FULLTEXT"
    """
    Retrieved from the paper's full text via Europe PMC.
    """
    TARGETED_FULLTEXT_RETRIEVAL = "TARGETED_FULLTEXT_RETRIEVAL"
    """
    Retrieved from the paper's full text by a targeted follow-up fetch.
    """
    ABSTRACT_ONLY = "ABSTRACT_ONLY"
    """
    Taken from the paper's abstract, full text being unavailable.
    """
    PRIMARY = "PRIMARY"
    """
    Transcribed from the primary paper by a curator, where no automated retrieval path was available.

    """


class ResolutionConfidence(str, Enum):
    """
    Confidence that this record identifies the paper the citation intended. Set at ingest by the resolution step, not by later edits.

    """
    HIGH = "HIGH"
    """
    Identifier matched exactly (DOI or PMID round-tripped).
    """
    MODERATE = "MODERATE"
    """
    Matched on title and authors; identifiers absent or partial.
    """
    LOW = "LOW"
    """
    Best-effort match; needs review before the record is trusted.
    """
    UNRESOLVED = "UNRESOLVED"
    """
    No confident match found. The citation should not be relied on.
    """



class Paper(ConfiguredBaseModel):
    """
    One publication, keyed by Semantic Scholar corpus ID. Written once at ingest and immutable thereafter — a quote-adding write must never alter identity. Correcting a stored identifier is a deliberate, reviewed change.
    Note corpus_id is the store key and the namespace for every quote_key on this paper, so it must be the canonical Semantic Scholar record. S2 can hold more than one record for the same paper; resolving by DOI alone has already selected a secondary record once. Prefer the record carrying the PubMed crosslink.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/references/v0.1'})

    corpus_id: str = Field(default=..., description="""Semantic Scholar corpus ID, digits only. The file stem and store key.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    title: str = Field(default=..., description="""Paper title as resolved, without trailing punctuation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    year: int = Field(default=..., description="""Publication year.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    authors: list[str] = Field(default=..., description="""Full author names, one per entry. Not a comma-joined string, and no \"et al.\" suffix — citation rendering reads these directly. `references._normalise_authors()` is the canonical producer; it accepts the Semantic Scholar object shape and flattens it here.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    author_keys: list[str] = Field(default=..., description="""Human-facing citation labels, e.g. \"Hochgerner et al., 2018\". Derived from authors + year at ingest.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    doi: Optional[str] = Field(default=None, description="""Bare DOI path, no \"DOI:\" prefix and no https:// URL. Absent if unknown.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    pmid: Optional[str] = Field(default=None, description="""PubMed ID, digits only, no \"PMID:\" prefix. Absent if unknown.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    venue: Optional[str] = Field(default=None, description="""Journal or venue name, where recorded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    externalIds: Optional[ExternalIds] = Field(default=None, description="""Identifier block as returned by the resolver — DOI, CorpusId, PubMed, PubMedCentral, MAG. The single home for external identifiers; do not add parallel top-level fields duplicating its members.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })
    resolution_confidence: ResolutionConfidence = Field(default=..., description="""Confidence that this record is the intended paper.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Paper']} })


class ExternalIds(ConfiguredBaseModel):
    """
    External identifiers for a paper, as returned by Semantic Scholar. PubMedCentral lives here rather than as a top-level pmcid field.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/references/v0.1'})

    DOI: Optional[str] = Field(default=None, description="""Bare DOI path.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIds']} })
    PubMed: Optional[str] = Field(default=None, description="""PubMed ID, digits only.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIds']} })
    PubMedCentral: Optional[str] = Field(default=None, description="""PMC ID, digits only, without the \"PMC\" prefix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIds']} })
    CorpusId: Optional[int] = Field(default=None, description="""Semantic Scholar corpus ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIds']} })
    MAG: Optional[str] = Field(default=None, description="""Microsoft Academic Graph ID, for older records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExternalIds']} })


class Quote(ConfiguredBaseModel):
    """
    One passage attributed to a paper. The quote's key is {corpus_id}_{sha256(normalised text)[:8]}, so the key is an assertion about the text it indexes; altering text without re-deriving the key is rejected at write time.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/references/v0.1'})

    text: str = Field(default=..., description="""The passage, exactly as extracted. Immutable once written — the key hashes it. If the recorded text is wrong, add a corrected quote rather than editing this one.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })
    section: Optional[str] = Field(default=None, description="""Where in the source document the passage appeared. Free text: values are real headings from papers and ASTA reports, and no closed vocabulary describes them honestly.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })
    source_method: Optional[str] = Field(default=None, description="""How the text was obtained; see the SourceMethod enum for the intended vocabulary. Deliberately typed as a string rather than the enum: 22 legacy quotes record an experimental method here instead of a retrieval method (e.g. \"patch-clamp (rat hippocampal slice)\"), and mapping those onto retrieval values would fabricate provenance that was never recorded. `just qc-content` reports non-conforming values so the backlog is visible and shrinks, while a newly written wrong value fails immediately.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })
    source_document: Optional[str] = Field(default=None, description="""Identifier of the SourceDocument this passage came from. Expected whenever source_method is ASTA_REPORT. Optional because some early deepsearch PDFs were never committed and may not be recoverable; the content sweep reports absences rather than blocking on them.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })
    claims: Optional[list[str]] = Field(default=None, description="""Node property categories this passage supports, e.g. defining_markers or anatomical_location. Deliberately unconstrained: the written vocabulary has forked into near-duplicates and around half of quotes carry none, so a consumer cannot assume the field is populated or that two spellings mean different things. Treat it as advisory until the vocabulary is settled.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })
    status: Optional[str] = Field(default=None, description="""Curation state of this quote. Free text pending a defined vocabulary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })
    added_by: Optional[str] = Field(default=None, description="""Identifier of the run that added this quote. The only per-quote link back to the originating workflow run.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })
    cell_type_hint: Optional[str] = Field(default=None, description="""Node this passage was extracted for, as judged at extraction time. A hint for downstream selection, not an assertion about the node.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })
    property_hint: Optional[str] = Field(default=None, description="""Node property this passage was judged to support at extraction time. Advisory; `claims` is the curated equivalent.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quote']} })


class QuoteSet(ConfiguredBaseModel):
    """
    The quotes recorded for one paper — the contents of quotes/{corpus_id}.json, keyed by quote_key. Append-only.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/references/v0.1'})

    quotes: Optional[list[Quote]] = Field(default=None, description="""quote_key -> Quote.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuoteSet']} })


class SourceDocument(ConfiguredBaseModel):
    """
    A document that quotes were extracted from — at present always an ASTA deep-research PDF. Makes the link from a quote to its originating document a first-class record rather than a filename convention threaded through run directories.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/references/v0.1'})

    source_id: str = Field(default=..., description="""Stable identifier, derived from the document filename.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDocument']} })
    path: str = Field(default=..., description="""Repository-relative path, e.g. inputs/deepsearch/trilaminar_cells.pdf. May point at a file that was never committed; see `available`.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDocument']} })
    available: bool = Field(default=..., description="""Whether the document is present in the repository. False records a known-missing source: the quotes remain valid and attributed, but the document behind them cannot be re-read.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDocument']} })
    region: Optional[str] = Field(default=None, description="""Region whose store this document belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDocument', 'StoreMeta']} })
    runs: Optional[list[str]] = Field(default=None, description="""Workflow run identifiers that ingested this document. Matches the added_by values on quotes drawn from it.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDocument']} })
    recovery_notes: Optional[str] = Field(default=None, description="""For an unavailable document: where it was looked for and what was concluded. A negative result is expensive to establish and cheap to lose — without it the same search gets repeated, or worse, absence is assumed to be an oversight that someone can simply correct.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDocument']} })


class StoreMeta(ConfiguredBaseModel):
    """
    Bookkeeping for one region's store — the contents of _meta.json.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://bican.org/schema/celltype-evidence/references/v0.1'})

    region: str = Field(default=..., description="""Region name; matches the directory name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDocument', 'StoreMeta']} })
    last_updated: Optional[str] = Field(default=None, description="""ISO-8601 timestamp of the most recent write.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StoreMeta']} })
    last_updated_by: Optional[str] = Field(default=None, description="""Identifier of the run that made the most recent write.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StoreMeta']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Paper.model_rebuild()
ExternalIds.model_rebuild()
Quote.model_rebuild()
QuoteSet.model_rebuild()
SourceDocument.model_rebuild()
StoreMeta.model_rebuild()
