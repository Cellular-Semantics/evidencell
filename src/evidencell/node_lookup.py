"""One lookup for any node, wherever it lives.

Lit nodes live in kb/graphs and are read through the in-memory index
(kb_index). Atlas nodes live in kb/taxonomy and are read through the taxonomy
DB. Callers should not need to know which tier a node is in -- see
planning/kb_index_plan.md ("What changes is the façade").

Atlas identity is (taxonomy_id, accession). An atlas stub's id is its
accession (enforced by qc_content's dangling_endpoint check), so a stub id and
a bare accession resolve to the same atlas node.

Fails closed throughout: an id that cannot be resolved raises, and so does an
atlas node whose taxonomy has no store or no usable DB. Nothing here returns a
partial record.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Literal, Mapping

from evidencell import paths
from evidencell.kb_index import get_index


class NodeNotFoundError(LookupError):
    """No lit node, atlas stub or taxonomy accession has this id."""


@dataclass(frozen=True)
class NodeView:
    kind: Literal["lit", "atlas"]
    id: str
    # lit: the KB node dict. atlas: the taxonomy DB row (canonical for atlas
    # properties; stub fields are not merged in). Read-only either way.
    data: Mapping[str, Any]
    # lit only: the file that canonically defines the node.
    source_file: Path | None
    # atlas only.
    taxonomy_id: str | None
    # KB files holding a reference stub for this node.
    stub_files: tuple[Path, ...]


def get_node(key: str) -> NodeView:
    """Resolve a lit node id, an atlas stub id or a taxonomy accession.

    Raises NodeNotFoundError if nothing has this id, paths.AmbiguousNodeError
    if more than one file canonically defines it, and
    taxonomy_db.TaxonomyDBUnavailable (or its UnknownTaxonomyError subclass)
    if an atlas node's taxonomy cannot be read.
    """
    index = get_index()
    records = index.nodes.get(key, [])
    canonical = list(dict.fromkeys(r.source_file for r in records if not r.is_stub))
    stub_files = tuple(dict.fromkeys(r.source_file for r in records if r.is_stub))

    if len(canonical) > 1:
        root = paths.repo_root()
        listed = ", ".join(str(p.relative_to(root)) for p in canonical)
        raise paths.AmbiguousNodeError(
            f"Node '{key}' is canonically defined in {len(canonical)} files: {listed}."
        )
    if canonical:
        node = next(r.node for r in records if not r.is_stub)
        return NodeView("lit", key, MappingProxyType(node), canonical[0], None, stub_files)

    atlas_stubs = [r.node for r in records
                   if r.is_stub and r.node.get("definition_basis") == paths.ATLAS_BASIS]
    if atlas_stubs:
        return _atlas_view(key, _stub_taxonomy(key, atlas_stubs), stub_files)
    if records:
        raise NodeNotFoundError(
            f"'{key}' exists only as a lit reference stub; no KB file defines it."
        )
    return _atlas_view(key, _taxonomy_for_accession(key), stub_files)


def _stub_taxonomy(key: str, stubs: list[dict]) -> str:
    taxonomy_ids = {s.get("taxonomy_id") for s in stubs}
    if len(taxonomy_ids) != 1 or None in taxonomy_ids:
        raise NodeNotFoundError(
            f"Atlas stubs for '{key}' do not agree on one taxonomy_id: "
            f"{sorted(map(str, taxonomy_ids))}."
        )
    return taxonomy_ids.pop()


def _taxonomy_for_accession(accession: str) -> str:
    """Find the one taxonomy store that defines `accession` (no DB needed)."""
    from evidencell.taxonomy_db import taxonomy_accessions

    tax_root = paths.repo_root() / "kb" / "taxonomy"
    stores = sorted(d for d in tax_root.iterdir() if d.is_dir()) if tax_root.is_dir() else []
    hits = [d.name for d in stores if accession in taxonomy_accessions(d)]
    if not hits:
        raise NodeNotFoundError(
            f"'{accession}' is not a KB node id and no taxonomy under "
            f"kb/taxonomy/ defines it as an accession."
        )
    if len(hits) > 1:
        raise NodeNotFoundError(
            f"Accession '{accession}' is defined by more than one taxonomy: {hits}."
        )
    return hits[0]


def _atlas_view(accession: str, taxonomy_id: str, stub_files: tuple[Path, ...]) -> NodeView:
    from evidencell.taxonomy_db import (
        TaxonomyDB,
        UnknownTaxonomyError,
        require_taxonomy_db,
    )

    if not paths.taxonomy_dir(taxonomy_id).is_dir():
        raise UnknownTaxonomyError(
            f"'{accession}' belongs to taxonomy '{taxonomy_id}', which has no "
            "store under kb/taxonomy/."
        )
    row = TaxonomyDB(require_taxonomy_db(taxonomy_id)).get_node_by_accession(accession)
    if row is None:
        raise NodeNotFoundError(
            f"Accession '{accession}' is not in the {taxonomy_id} DB. If the "
            f"taxonomy YAML defines it, the DB is stale: "
            f"just build-taxonomy-db {taxonomy_id}"
        )
    return NodeView("atlas", accession, MappingProxyType(row), None, taxonomy_id, stub_files)

