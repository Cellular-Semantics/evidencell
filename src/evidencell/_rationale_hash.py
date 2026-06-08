"""Rationale-currency hash for Phase 3 verdict-at-report-time.

The report-time gen-report orchestrator writes a holistic verdict
(``confidence`` ordinal, ``confidence_score`` numeric, ``rationale``
prose) back to each ``MappingEdge`` after the synthesis subagent
produces a report. To detect when the verdict has gone stale because
upstream evidence drifted, the orchestrator computes a hash over the
canonical edge + endpoint-node payload at write time and stores it as
``rationale_source_hash``. On every read and every ``just qc`` pass,
the hash is recomputed from current state and compared.

**Hash inputs** (Q9 in the Phase 3 design decisions): the edge's
structured fields (excluding the rationale-suite outputs themselves)
plus the two endpoint ``CellTypeNode``s' canonical content. Whole-edge
granularity (Q11) — any change in the hashed inputs invalidates the
whole rationale.

**Hash output**: SHA256 8-char hex digest (matches the pattern used
elsewhere in evidencell: ``src/evidencell/figures.py:_content_hash``,
``src/evidencell/taxonomy_db.py:_compute_schema_hash``,
``src/evidencell/references.py``).

This module is intentionally side-effect-free and easy to unit-test.
The orchestrator calls :func:`compute_hash` at write-back time;
``just qc`` calls :func:`is_stale` on every edge with a stored hash.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

# Fields that the report-time agent writes — excluded from the hash
# inputs so that a re-hash on read doesn't inadvertently include the
# rationale itself.
_RATIONALE_SUITE_FIELDS = frozenset(
    {
        "rationale",
        "confidence",
        "confidence_score",
        "rationale_generated_at",
        "rationale_source_hash",
        "report_path",
        # Phase-3 filter+synth merge: the SSSOM trio + typed caveats +
        # proposed_experiments are also report-time outputs. Excluded
        # from the hash so the agent's own write doesn't invalidate the
        # hash it just computed. A subsequent curator edit to any of
        # these fields would not be caught as staleness, which is the
        # intended trade-off — these fields are the rationale-suite's
        # own outputs, not its inputs.
        "relationship",
        "mapping_cardinality",
        "mapping_justification",
        "caveats",
        "proposed_experiments",
        # `reconciliation_note` is also report-time-writable (Q7), but
        # it captures cross-edge agreement and should be part of the
        # hash so a curator's manual reconciliation invalidates the
        # rationale on re-run. Keep it in.
    }
)

# Node fields excluded from the hash: timestamps and bookkeeping that
# change without affecting the mapping decision.
_NODE_BOOKKEEPING_FIELDS = frozenset(
    {
        "creation_date",
        "updated_date",
        "curator",
        "reviewed_by",
    }
)


def _canonicalise(value: Any) -> Any:
    """Return a JSON-serialisable shape with dict keys sorted at every
    level, so equivalent data produces a stable serialisation regardless
    of insertion order."""
    if isinstance(value, dict):
        return {k: _canonicalise(value[k]) for k in sorted(value)}
    if isinstance(value, list):
        return [_canonicalise(v) for v in value]
    return value


def canonical_payload(
    edge: dict[str, Any],
    lit_node: dict[str, Any] | None,
    taxonomy_node: dict[str, Any] | None,
) -> dict[str, Any]:
    """Build the canonical hashable payload for an edge + its endpoints.

    Excludes the rationale-suite fields from the edge (they're the
    output we're hashing the inputs of) and bookkeeping fields from
    both endpoint nodes. Endpoint nodes may be ``None`` when the
    referenced node isn't in the graph (e.g. lit-to-lit edges where
    one endpoint is in another graph file); the hash falls back to a
    placeholder so the absent node doesn't silently match a different
    absent node.
    """
    return {
        "edge": {
            k: _canonicalise(v)
            for k, v in (edge or {}).items()
            if k not in _RATIONALE_SUITE_FIELDS
        },
        "lit_node": (
            {
                k: _canonicalise(v)
                for k, v in (lit_node or {}).items()
                if k not in _NODE_BOOKKEEPING_FIELDS
            }
            if lit_node is not None
            else {"_absent": True}
        ),
        "taxonomy_node": (
            {
                k: _canonicalise(v)
                for k, v in (taxonomy_node or {}).items()
                if k not in _NODE_BOOKKEEPING_FIELDS
            }
            if taxonomy_node is not None
            else {"_absent": True}
        ),
    }


def compute_hash(
    edge: dict[str, Any],
    lit_node: dict[str, Any] | None,
    taxonomy_node: dict[str, Any] | None,
) -> str:
    """Return the 8-char SHA256 prefix of the canonical edge+endpoint
    payload. Stable under dict-key reordering and irrelevant whitespace.
    """
    payload = canonical_payload(edge, lit_node, taxonomy_node)
    serialised = json.dumps(payload, sort_keys=True, default=str)
    return hashlib.sha256(serialised.encode("utf-8")).hexdigest()[:8]


def is_stale(
    edge: dict[str, Any],
    lit_node: dict[str, Any] | None,
    taxonomy_node: dict[str, Any] | None,
) -> bool:
    """Return True if the edge's stored ``rationale_source_hash`` does
    not match the freshly computed hash. Edges without a stored hash
    are considered stale (no rationale written yet, or migration
    artefact — the QC output will flag them as needing regeneration).
    """
    stored = (edge or {}).get("rationale_source_hash")
    if not stored:
        return True
    return compute_hash(edge, lit_node, taxonomy_node) != stored
