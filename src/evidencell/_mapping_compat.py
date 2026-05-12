"""Phase 2 schema overhaul — back-compat shim for the PR1 → PR2 window.

Phase 2 renames MappingEdge slots ``type_a`` → ``lit_type`` and
``type_b`` → ``taxonomy_type`` and rewrites the ``MappingRelationship``
enum to CURIE-style identifiers (``EQUIVALENT`` → ``skos:exactMatch``
etc.). The schema retains the old slot names and old enum values as
deprecated entries so that existing KB YAML continues to validate
during the migration window.

This module is the single read-path source of truth for code that
walks ``MappingEdge`` instances loaded from YAML. It abstracts over
the old / new field names and old / new enum values so the rest of
``src/evidencell/`` can be written against the post-Phase-2 names
only.

**This module is deleted at the end of PR2** (after the KB-wide sweep
rewrites every edge using new field names and CURIE enum values).
Removing the import and inlining the new-name access at each call
site is the PR2 chore.

See planning/phase_2_schema_overhaul_plan.md and
planning/phase_2_decisions_2026-05-12.md.
"""

from __future__ import annotations

import warnings
from typing import Any, Iterable

# ──────────────────────────────────────────────────────────────────
# Field-name shim
# ──────────────────────────────────────────────────────────────────

_LIT_TYPE_KEYS = ("lit_type", "type_a")
_TAXONOMY_TYPE_KEYS = ("taxonomy_type", "type_b")

_warned_field_names: set[str] = set()


def lit_type(edge: dict[str, Any]) -> str | None:
    """Return the edge's source (lit_type) node id, accepting the
    deprecated ``type_a`` alias during the PR1 → PR2 window. Emits a
    single ``DeprecationWarning`` per distinct old-name encounter
    point so logs stay quiet but the migration progress is visible.
    """
    return _read_aliased(edge, _LIT_TYPE_KEYS, deprecated_key="type_a")


def taxonomy_type(edge: dict[str, Any]) -> str | None:
    """Return the edge's target (taxonomy_type) node id, accepting the
    deprecated ``type_b`` alias during the PR1 → PR2 window."""
    return _read_aliased(edge, _TAXONOMY_TYPE_KEYS, deprecated_key="type_b")


def _read_aliased(
    edge: dict[str, Any],
    candidate_keys: Iterable[str],
    deprecated_key: str,
) -> str | None:
    for key in candidate_keys:
        if key in edge:
            if key == deprecated_key:
                _warn_once(
                    f"MappingEdge field `{deprecated_key}` is deprecated "
                    f"(Phase 2 schema overhaul). Use `{candidate_keys[0]}`. "
                    f"PR2 KB sweep will migrate this edge."
                )
            return edge[key]
    return None


def _warn_once(message: str) -> None:
    if message in _warned_field_names:
        return
    _warned_field_names.add(message)
    warnings.warn(message, DeprecationWarning, stacklevel=3)


# ──────────────────────────────────────────────────────────────────
# Relationship-value shim
# ──────────────────────────────────────────────────────────────────
#
# Maps deprecated ALL_CAPS MappingRelationship values to their new
# CURIE counterparts (and, where applicable, the implied
# mapping_cardinality). Read-path consumers should treat the returned
# CURIE as the canonical relationship; cardinality is returned
# alongside so that downstream code can use it for display / scoring
# without storing it on the edge yet (the KB sweep in PR2 will
# materialise both fields).

_RELATIONSHIP_REMAP: dict[str, tuple[str, str | None]] = {
    "EQUIVALENT":         ("skos:exactMatch",                   None),
    "PARTIAL_OVERLAP":    ("evidencell:PartialOverlapMatch",    None),
    "CROSS_CUTTING":      ("evidencell:CrossCuttingMatch",      None),
    "NO_CORRESPONDENCE":  ("evidencell:NoCorrespondence",       None),
    "TYPE_A_SPLITS":      ("skos:broadMatch",                   "1:n"),
    "TYPE_A_MERGES":      ("skos:narrowMatch",                  "n:1"),
    "SUBSET":             ("skos:broadMatch",                   "1:1"),
    "SUPERSET":           ("skos:narrowMatch",                  "n:1"),
    "OVERLAPS":           ("skos:closeMatch",                   None),
    "UNCERTAIN":          ("",                                  None),
    "CANDIDATE_SYNONYM":  ("skos:closeMatch",                   None),
}


def normalise_relationship(
    edge: dict[str, Any],
) -> tuple[str | None, str | None]:
    """Return ``(relationship, mapping_cardinality)`` for an edge,
    normalising deprecated ALL_CAPS values to their CURIE counterparts.

    - If the edge carries a new CURIE value (``skos:exactMatch`` etc.),
      it is returned as-is along with the explicit ``mapping_cardinality``
      field if present.
    - If the edge carries a deprecated ALL_CAPS value, the lookup
      returns the CURIE plus the implied cardinality (e.g.
      ``TYPE_A_SPLITS`` → ``("skos:broadMatch", "1:n")``).
    - ``UNCERTAIN`` returns ``("", None)`` — the relationship is
      effectively unset; consumers should treat this as missing and
      may consult ``mapping_justification`` instead.

    The deprecation warning fires on the first ALL_CAPS encounter per
    distinct value.
    """
    rel = edge.get("relationship")
    cardinality = edge.get("mapping_cardinality")
    if rel is None:
        return None, cardinality
    if rel in _RELATIONSHIP_REMAP:
        new_rel, implied_card = _RELATIONSHIP_REMAP[rel]
        _warn_once(
            f"MappingRelationship `{rel}` is deprecated "
            f"(Phase 2 schema overhaul). Use `{new_rel}`. "
            f"PR2 KB sweep will migrate this edge."
        )
        return new_rel, cardinality or implied_card
    return rel, cardinality


# ──────────────────────────────────────────────────────────────────
# Display helpers
# ──────────────────────────────────────────────────────────────────


def display_relationship(
    relationship: str | None,
    cardinality: str | None = None,
) -> str:
    """Format a relationship + optional cardinality for human-facing
    display strings (reports, TOC, log messages).

    Examples:
      ``display_relationship("skos:exactMatch")`` → ``"skos:exactMatch"``
      ``display_relationship("skos:broadMatch", "1:n")`` → ``"skos:broadMatch (1:n)"``
      ``display_relationship(None)`` → ``"(no relationship)"``
    """
    if not relationship:
        return "(no relationship)"
    if cardinality:
        return f"{relationship} ({cardinality})"
    return relationship
