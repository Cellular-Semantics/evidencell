"""Mechanical Stage B emitter — issue #96.

Replaces the per-candidate LLM mapping subagent (workflows/map-cell-type.md
Step 3) with a programmatic emitter that produces structural MappingEdge
skeletons from Stage A discovery JSON + classical/atlas YAML + AT
artifacts.

The emitter is structural-only. LLM-flavoured pieces (LITERATURE evidence
selection with verbatim snippets, unresolved_questions, proposed_experiments,
predicate selection, confidence/rationale) are deferred to gen-report's
single synthesis call, which writes them back via verdict-block writeback
(Phase 3 design).

Rules — see the module's `_property_comparisons`, `_caveats`,
`_atlas_metadata_evidence`, and `_at_evidence` helpers for the exact
deterministic logic. Any deviation should fail a test, not be papered
over in the emitter.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Mapping

import yaml
from ruamel.yaml import YAML

from evidencell.at_metrics import (
    QUERY_NORM_CAVEAT,
    apply_query_norm_caveat,
    compute_edge_metrics,
    load_run_manifest,
    resolve_run_for_source,
    validate_query_normalization,
)
from evidencell.expression_cache import ExpressionUnavailable
from evidencell.kb_io import roundtrip_yaml
from evidencell.gene_identity import Pin, marker_gene_ids, marker_name
from evidencell.paths import repo_root
from evidencell.taxonomy_db import MIN_DETECTABLE


def _yaml_rt() -> YAML:
    """Round-trip YAML config matching rationale_writeback — preserves
    quotes so quote_keys like `1015389_e9028538` don't get YAML-coerced
    to float on load + dump."""
    return roundtrip_yaml()


# Region-fraction tiers for LOCATION alignment, from
# workflows/map-cell-type.md Step 3 (proximity-aware rules).
LOC_TIER_CONSISTENT: float = 0.5
LOC_TIER_APPROXIMATE: float = 0.1

# AT F1 thresholds for caveat triggers, mirroring the Stage A AT bucket
# cutoff (F1 < 0.5 at cluster level → cells distributed across multiple
# atlas clusters).
AT_F1_DISTRIBUTED: float = 0.5

# Map taxonomy_rank → schema level string (for accession-prefix mapping
# in YAML / DB queries).
_RANK_TO_LEVEL_NAME: dict[int, str] = {
    0: "cluster",
    1: "supertype",
    2: "subclass",
    3: "class",
}

# ─── public entry ────────────────────────────────────────────────────────────


def emit_stage_b(
    classical_node_file: Path,
    classical_node_id: str,
    taxonomy_id: str,
    rank: int,
    top_k: int = 5,
    discovery_json_path: Path | None = None,
    write: bool = True,
) -> list[dict]:
    """Emit MappingEdge skeletons for the top-K Stage A candidates.

    Reads the discovery JSON (canonical path if ``discovery_json_path`` is
    None), loads classical + atlas node data + AT artifact, and constructs
    one ``MappingEdge`` dict per candidate by deterministic rules.

    When ``write=True`` (default), appends the edges to
    ``classical_node_file``'s ``edges:`` section (after de-dup against
    existing edge ids) and adds taxonomy-ref stub nodes where missing.

    Returns the list of edge dicts (regardless of ``write``).
    """
    graph_file = Path(classical_node_file).resolve()
    yaml_rt = _yaml_rt()
    with graph_file.open(encoding="utf-8") as fh:
        graph = yaml_rt.load(fh)
    classical = _find_node(graph, classical_node_id)
    if not classical:
        raise ValueError(
            f"Classical node {classical_node_id!r} not found in {graph_file}"
        )

    candidates = _load_candidates(
        discovery_json_path=discovery_json_path,
        classical_node_id=classical_node_id,
        taxonomy_id=taxonomy_id,
        rank=rank,
    )
    candidates = candidates[:top_k]

    for c in candidates:
        c["_classical_cache"] = classical

    # AT evidence is driven by the classical node's declared source-set
    # correspondences (issue #126): (dataset_accession, source_label) pairs
    # authored by lit-ingest after reading the dataset's describing paper.
    # The AT run supplying the numbers is resolved operationally at map time
    # (never stored on the node). Full cutover — nodes without at_source_sets
    # emit no ANNOTATION_TRANSFER evidence.
    at_source_sets = classical.get("at_source_sets") or []

    edges: list[dict] = []
    for cand in candidates:
        atlas = _load_atlas_node(
            taxonomy_id, cand["node_id"], rank,
            symbols=_classical_expression_symbols(classical),
            gene_ids=marker_gene_ids(classical),
        )
        edges.append(_build_edge(
            classical_node_id=classical_node_id,
            candidate=cand,
            atlas=atlas,
            taxonomy_id=taxonomy_id,
            at_source_sets=at_source_sets,
        ))

    if write:
        _write_back(graph_file, graph, edges, candidates, taxonomy_id, yaml_rt)

    return edges


# ─── per-candidate edge construction ─────────────────────────────────────────


def _build_edge(
    *,
    classical_node_id: str,
    candidate: dict,
    atlas: dict | None,
    taxonomy_id: str,
    at_source_sets: list[dict],
) -> dict:
    """Construct one MappingEdge dict from a Stage A candidate."""
    taxonomy_type = candidate["node_id"]
    ds = candidate.get("discovery_score") or {}
    at_signal = ds.get("at_signal") or {}

    edge: dict = {
        "id": f"edge_{classical_node_id}_to_{taxonomy_type}",
        "lit_type": classical_node_id,
        "taxonomy_type": taxonomy_type,
        "relationship": "evidencell:UncertainRelationship",
        "mapping_justification": "semapv:UnreviewedManualMapping",
    }

    edge["evidence"] = _evidence_list(
        atlas=atlas,
        candidate=candidate,
        ds=ds,
        at_source_sets=at_source_sets,
        taxonomy_id=taxonomy_id,
        taxonomy_type=taxonomy_type,
    )

    pc = _property_comparisons(
        classical_node_id=classical_node_id,
        candidate=candidate,
        atlas=atlas,
        ds=ds,
    )
    edge["property_comparisons"] = pc
    edge["caveats"] = _caveats(pc, ds, at_signal)
    # discovery_score: copied verbatim onto the edge. The candidate dict
    # carries an internal `_classical_cache` we strip from ds (it isn't
    # part of discovery_score anyway, but defensive).
    edge["discovery_score"] = {k: v for k, v in ds.items() if not k.startswith("_")}
    return edge


# ─── property comparisons (rule-based) ────────────────────────────────────────


def _property_comparisons(
    *,
    classical_node_id: str,
    candidate: dict,
    atlas: dict | None,
    ds: dict,
) -> list[dict]:
    """Build the property_comparisons list by deterministic rule.

    Order: nt_type, location (one row per classical SOMA), then per-gene
    rows for defining_markers, negative_markers, neuropeptides.
    """
    # Classical node is read from disk lazily here; the caller already
    # validated its presence. For real callers, pass a pre-loaded dict
    # via `_classical_cache` on the candidate (set in emit_stage_b).
    classical = candidate.get("_classical_cache")
    if classical is None:
        raise RuntimeError(
            "_property_comparisons requires the classical node dict "
            "cached on the candidate; emit_stage_b must populate it"
        )

    out: list[dict] = []

    # ── nt_type ─────────────────────────────────────────────────────────────
    classical_nt = (classical.get("nt_type") or {}).get("name_in_source")
    atlas_nt = (
        (atlas or {}).get("nt_type") or {}
    ).get("name_in_source") if atlas else None
    if classical_nt and atlas_nt:
        out.append({
            "property": "nt_type",
            "node_a_value": classical_nt,
            "node_b_value": atlas_nt,
            # Candidate survived the Stage A filter, which means NT
            # passed the prefix-match rule. Mark CONSISTENT.
            "alignment": "CONSISTENT",
            "notes": "Both classical and atlas annotated GABAergic." if classical_nt.lower().startswith("gaba") else "Stage A NT prefix-match passed.",
        })
    else:
        out.append({
            "property": "nt_type",
            "node_a_value": classical_nt or "not asserted",
            "node_b_value": atlas_nt or "not asserted",
            "alignment": "NOT_ASSESSED",
            "notes": "NT data missing on one side.",
        })

    # ── location ────────────────────────────────────────────────────────────
    rf100 = ds.get("region_fraction_100um")
    rf_strict = ds.get("region_fraction")
    completeness = ds.get("region_count_completeness")
    region_evidence = ds.get("region_evidence")
    classical_soma = [
        loc for loc in (classical.get("anatomical_location") or [])
        if (loc.get("compartment") in (None, "SOMA"))
    ]
    classical_loc_str = "; ".join(
        f"{loc.get('label') or loc.get('name_in_source') or '?'} "
        f"[{loc.get('id') or '?'}]"
        for loc in classical_soma
    ) or "not asserted"

    alignment = _location_alignment(rf100, region_evidence)
    node_b = _atlas_location_summary(atlas, ds)
    notes = _location_notes(rf100, rf_strict, completeness, region_evidence)
    out.append({
        "property": "location",
        "node_a_value": classical_loc_str,
        "node_b_value": node_b,
        "alignment": alignment,
        "notes": notes,
    })

    # ── markers / neuropeptides / negative markers ──────────────────────────
    expr_detail = {e["gene"]: e for e in (ds.get("expression_detail") or [])}
    atlas_expr = (atlas or {}).get("expression") or {}
    not_measured = (atlas or {}).get("not_measured") or {}
    expr_source = (atlas or {}).get("expression_source")
    # Classical marker name → the atlas symbol it resolved to (#216), for
    # matching the atlas metadata marker lists. Expression is keyed by the
    # classical name itself.
    gene_symbols = (atlas or {}).get("gene_symbols") or {}
    atlas_marker_meta = _atlas_marker_categories(atlas)
    # Stage A metadata-vs-expression discrepancies, keyed by gene; copied
    # into the matching comparison's notes (#189). They don't change alignment.
    discrepancies = {
        d["gene"]: d for d in (candidate.get("marker_discrepancies") or [])
    }

    def _gene_ctx(sym: str, canon: str) -> dict:
        return {
            "atlas_val": atlas_expr.get(sym),
            "atlas_meta_category": atlas_marker_meta.get(canon) or atlas_marker_meta.get(sym),
            "not_measured_reason": not_measured.get(sym),
            "expression_source": expr_source,
            "stage_a_expression_source": candidate.get("expression_source"),
            "discrepancy": discrepancies.get(sym) or discrepancies.get(canon),
        }

    for m in (classical.get("defining_markers") or []):
        sym = marker_name(m)
        if not sym:
            continue
        canon = str(gene_symbols.get(sym) or sym)
        out.append(_marker_comparison(
            property_name=f"marker_{sym}",
            symbol=sym,
            is_negative=False,
            classical_label="defining marker",
            expr_entry=expr_detail.get(sym) or expr_detail.get(canon),
            **_gene_ctx(sym, canon),
        ))

    for m in (classical.get("negative_markers") or []):
        sym = marker_name(m)
        if not sym:
            continue
        canon = str(gene_symbols.get(sym) or sym)
        out.append(_marker_comparison(
            property_name=f"negative_marker_{sym}",
            symbol=sym,
            is_negative=True,
            classical_label="ABSENT (classical negative marker)",
            expr_entry=expr_detail.get(f"-{sym}") or expr_detail.get(f"-{canon}") or expr_detail.get(canon),
            **_gene_ctx(sym, canon),
        ))

    for m in (classical.get("neuropeptides") or []):
        sym = marker_name(m)
        if not sym:
            continue
        canon = str(gene_symbols.get(sym) or sym)
        out.append(_marker_comparison(
            property_name=f"neuropeptide_{sym}",
            symbol=sym,
            is_negative=False,
            classical_label="neuropeptide (classical)",
            expr_entry=expr_detail.get(sym) or expr_detail.get(canon),
            **_gene_ctx(sym, canon),
        ))

    return out


def _location_alignment(rf100: float | None, region_evidence: str | None) -> str:
    """LOCATION alignment from region_fraction_100um tier rules."""
    if rf100 is None:
        return "NOT_ASSESSED"
    if region_evidence == "DESCENDANT_ONLY":
        # BCKG rescue path — own anat empty, only descendants survived.
        # Treat as DISCORDANT so the LLM at gen-report time can re-rank.
        return "DISCORDANT"
    if rf100 >= LOC_TIER_CONSISTENT:
        return "CONSISTENT"
    if rf100 >= LOC_TIER_APPROXIMATE:
        return "APPROXIMATE"
    return "DISCORDANT"


def _location_notes(
    rf100: float | None,
    rf_strict: float | None,
    completeness: str | None,
    region_evidence: str | None,
) -> str:
    parts: list[str] = []
    if rf100 is not None:
        parts.append(f"region_fraction_100um: {rf100:.3f}")
    if rf_strict is not None:
        parts.append(f"strict region_fraction: {rf_strict:.3f}")
    if completeness:
        parts.append(f"region_count_completeness: {completeness}")
        if completeness == "lower_bound":
            parts.append(
                "winning rollup includes non-painted CCF2020 descendants — "
                "count is a floor"
            )
    if region_evidence:
        parts.append(f"region_evidence: {region_evidence}")
    return "; ".join(parts) if parts else "no region data on candidate"


def _atlas_location_summary(atlas: dict | None, ds: dict) -> str:
    """Build the node_b_value string for the location row from atlas data.

    Prefers painted CCF2020 leaf domains (completeness=None) over `exact`
    rollups over `lower_bound` rollups — broad rollups are uninformative
    when painted leaves are available. Picks top-3 by
    `count_in_or_near_100um` within the strongest available class.
    """
    if not atlas:
        return f"region_fraction_100um={ds.get('region_fraction_100um')}"
    locs = atlas.get("anatomical_location") or []
    # Deduplicate per anat_id; keep highest count_100um across per-source rows.
    by_id: dict[str, tuple[int, str, str | None]] = {}
    for loc in locs:
        aid = loc.get("id")
        if not aid:
            continue
        c100 = loc.get("count_in_or_near_100um") or 0
        existing = by_id.get(aid, (0, "", None))
        if c100 > existing[0]:
            by_id[aid] = (
                c100,
                loc.get("label") or loc.get("name_in_source") or "?",
                loc.get("cell_count_completeness"),
            )
    if not by_id:
        return "no atlas anat data"
    # Bucket by completeness class; pick the strongest non-empty bucket.
    painted = [(aid, t) for aid, t in by_id.items() if t[2] is None]
    exact = [(aid, t) for aid, t in by_id.items() if t[2] == "exact"]
    lower = [(aid, t) for aid, t in by_id.items() if t[2] == "lower_bound"]
    pool = painted or exact or lower
    top = sorted(pool, key=lambda kv: -kv[1][0])[:3]
    out = []
    for aid, (c100, label, comp) in top:
        suffix = f" [{comp}]" if comp else " [painted]"
        out.append(f"{label} [{aid}] count_100um={c100}{suffix}")
    return "; ".join(out)


def _classical_expression_symbols(classical: dict) -> list[str]:
    """Marker names of a classical node's defining markers, negative
    markers and neuropeptides — the genes Stage B compares. They resolve to
    atlas genes in ``TaxonomyDB.expression`` (pinned by each marker's
    ``ncbi_gene_id``; see :func:`gene_identity.marker_gene_ids`)."""
    out: list[str] = []
    for field in ("defining_markers", "negative_markers", "neuropeptides"):
        for m in classical.get(field) or []:
            sym = marker_name(m)
            if sym and sym not in out:
                out.append(sym)
    return out


def _atlas_marker_categories(atlas: dict | None) -> dict[str, str]:
    """Map gene symbol → category from atlas-side markers list."""
    if not atlas:
        return {}
    out: dict[str, str] = {}
    for m in atlas.get("markers") or []:
        sym = marker_name(m)
        cat = m.get("category")
        if sym and cat and sym not in out:
            out[sym] = cat
    return out


def _marker_comparison(
    *,
    property_name: str,
    symbol: str,
    is_negative: bool,
    classical_label: str,
    expr_entry: dict | None,
    atlas_val: float | None,
    atlas_meta_category: str | None,
    not_measured_reason: str | None = None,
    expression_source: str | None = None,
    stage_a_expression_source: str | None = None,
    discrepancy: dict | None = None,
) -> dict:
    """Build one property_comparison for a marker / neuropeptide.

    A measured value's stats file is stamped into ``notes``
    (:data:`ATLAS_EXPRESSION_NOTE`) so reports cite where the edge's numbers
    came from, not whatever the DB cache holds at render time.
    """
    # Atlas-side value: prefer expr_entry (cohort-relative) if Stage A
    # scored this gene; else the accessor's mean expression; else
    # NOT_ASSESSED, which only happens for a gene that can't be measured.
    val = None
    cohort_pct = None
    coverage = None
    if expr_entry is not None:
        val = expr_entry.get("val")
        # cohort_pct lives under percentiles[].pct with context_id=cohort
        for pct in expr_entry.get("percentiles") or []:
            if pct.get("context_id") == "cohort":
                cohort_pct = pct.get("pct")
                break
        coverage = expr_entry.get("coverage")
    # Which stats file the value came from: the discovery JSON's for a
    # Stage A value (absent in discovery JSONs that predate it), else the
    # accessor's.
    value_source = expression_source
    if val is not None:
        value_source = stage_a_expression_source or expression_source
    if val is None:
        val = atlas_val

    classical_text = f"{symbol} — {classical_label}"
    if val is None:
        if not_measured_reason:
            why = f"Gene not measured in {expression_source or 'the atlas stats file'} ({not_measured_reason})."
        else:
            why = (
                f"No expression value for this atlas node in "
                f"{expression_source or 'the atlas stats file'}."
            )
        return {
            "property": property_name,
            "node_a_value": classical_text,
            "node_b_value": "not measured",
            "alignment": "NOT_ASSESSED",
            "notes": _with_discrepancy(why, discrepancy),
        }

    node_b_parts = [f"{symbol}: {val:.2f}"]
    if cohort_pct is not None:
        node_b_parts.append(f"cohort_pct {cohort_pct:.3f}")
    if coverage is not None:
        node_b_parts.append(f"child-coverage {coverage:.3f}")
    if atlas_meta_category:
        node_b_parts.append(f"atlas category: {atlas_meta_category}")
    node_b = "; ".join(node_b_parts)

    alignment = _marker_alignment(val, cohort_pct, is_negative)
    notes = _marker_notes(symbol, val, cohort_pct, coverage, alignment, is_negative)
    if value_source:
        notes = f"{notes}; {ATLAS_EXPRESSION_NOTE}{value_source}"
    notes = _with_discrepancy(notes, discrepancy)

    return {
        "property": property_name,
        "node_a_value": classical_text,
        "node_b_value": node_b,
        "alignment": alignment,
        "notes": notes,
    }


# Prefix of the stats-file stamp in a marker comparison's notes; render.py
# reads it back for the report's Methods section.
ATLAS_EXPRESSION_NOTE = "atlas expression from "

_DISCREPANCY_TEXT = {
    "LISTED_NOT_EXPRESSED": (
        "atlas metadata lists this gene as a marker but measured expression is "
        "low/absent — check for a metadata error, gene-version difference or "
        "scope mismatch"
    ),
    "EXPRESSED_NOT_LISTED": (
        "highly expressed among siblings but not in the atlas metadata marker lists"
    ),
    "LISTED_NO_EXPRESSION_DATA": (
        "atlas metadata lists this gene as a marker but it has no expression data"
    ),
}


def _with_discrepancy(notes: str, discrepancy: dict | None) -> str:
    """Append a Stage A metadata/expression discrepancy to a PC's notes."""
    if not discrepancy:
        return notes
    kind = discrepancy.get("kind", "")
    text = _DISCREPANCY_TEXT.get(kind, kind)
    pct = discrepancy.get("sibling_pct")
    suffix = f" (sibling percentile {pct:.3f})" if pct is not None else ""
    return f"{notes}; METADATA DISCREPANCY {kind}: {text}{suffix}"


def _marker_alignment(
    val: float, cohort_pct: float | None, is_negative: bool,
) -> str:
    """Alignment from val + cohort_pct, matching the Stage A scoring tiers."""
    if val < MIN_DETECTABLE:
        # Absent on the atlas side.
        return "CONSISTENT" if is_negative else "DISCORDANT"
    # Above MIN_DETECTABLE.
    if is_negative:
        return "DISCORDANT"
    # Positive marker: present.
    # cohort_pct in [0.1, 0.5) is the boundary band → APPROXIMATE.
    if cohort_pct is not None and 0.1 <= cohort_pct < 0.5:
        return "APPROXIMATE"
    return "CONSISTENT"


def _marker_notes(
    symbol: str,
    val: float,
    cohort_pct: float | None,
    coverage: float | None,
    alignment: str,
    is_negative: bool,
) -> str:
    parts: list[str] = []
    parts.append(f"val={val:.2f}")
    if val < MIN_DETECTABLE:
        parts.append(f"below MIN_DETECTABLE ({MIN_DETECTABLE})")
    if cohort_pct is not None:
        parts.append(f"cohort percentile {cohort_pct:.3f}")
    if coverage is not None:
        parts.append(f"child-cluster coverage {coverage:.3f}")
        if coverage < 0.5:
            parts.append("HIDDEN-1:1 signal — concentrated in a subset of children")
    return "; ".join(parts)


# ─── evidence emission ──────────────────────────────────────────────────────


def _evidence_list(
    *,
    atlas: dict | None,
    candidate: dict,
    ds: dict,
    at_source_sets: list[dict],
    taxonomy_id: str,
    taxonomy_type: str,
) -> list[dict]:
    out: list[dict] = [
        _atlas_metadata_evidence(atlas=atlas, candidate=candidate, ds=ds),
    ]
    # One ANNOTATION_TRANSFER item per declared source set — emitted whether
    # or not the source transfers to this candidate. A source that does NOT
    # land here yields a NO_EVIDENCE item (negative signal, issue #126 pt 4),
    # never a silent drop.
    for src in at_source_sets:
        at_item = _at_evidence(
            source_set=src,
            taxonomy_id=taxonomy_id,
            edge_target=taxonomy_type,
        )
        if at_item is not None:
            out.append(at_item)
    return out


def _atlas_metadata_evidence(
    *, atlas: dict | None, candidate: dict, ds: dict,
) -> dict:
    """ATLAS_METADATA evidence item — always emitted, structural prose."""
    name = (atlas or {}).get("name") or candidate.get("label") or candidate.get("node_id")
    n_cells = (atlas or {}).get("n_cells")
    neighborhood = (atlas or {}).get("neighborhood")
    mfr = (atlas or {}).get("male_female_ratio")

    bits: list[str] = [f"Atlas node {name}"]
    if n_cells:
        bits.append(f"n_cells={n_cells}")
    if neighborhood:
        bits.append(f"neighborhood {neighborhood!r}")
    if mfr is not None:
        bits.append(f"male_female_ratio {mfr:.2f}")

    rf100 = ds.get("region_fraction_100um")
    rf = ds.get("region_fraction")
    completeness = ds.get("region_count_completeness")
    if rf100 is not None:
        bits.append(f"region_fraction_100um={rf100:.3f}")
    if rf is not None:
        bits.append(f"strict region_fraction={rf:.3f}")
    if completeness:
        bits.append(f"completeness={completeness}")

    return {
        "evidence_type": "ATLAS_METADATA",
        "supports": "PARTIAL",
        "explanation": "; ".join(bits) + ".",
    }


def _at_evidence(
    *, source_set: dict, taxonomy_id: str, edge_target: str,
) -> dict | None:
    """ANNOTATION_TRANSFER evidence item for one declared ``at_source_sets``
    entry against ``edge_target``.

    The AT run is resolved operationally from
    ``(dataset_accession, taxonomy_id, source_label)`` — never taken from
    the node. Always returns an item (never a silent drop):

      * run cannot be resolved  → NO_EVIDENCE item (loud diagnostic).
      * run resolved but the source's lineage does not reach this target
        (no metrics rows) → NO_EVIDENCE item ("does not transfer here").
      * otherwise → item with supports from the level-aware default.

    Returns None only when the source set is malformed (no source_label).
    """
    source_label = source_set.get("source_label")
    dataset_accession = source_set.get("dataset_accession")
    if not source_label or not dataset_accession:
        print(
            f"  WARNING: at_source_sets entry missing dataset_accession/"
            f"source_label: {source_set!r}. Skipping.",
            file=sys.stderr,
        )
        return None

    correspondence = source_set.get("correspondence")

    def _item(*, supports: str, run_ref: str | None, metrics: dict | None,
              explanation: str) -> dict:
        target_atlas = "WMBv1"
        query_norm = "raw"
        if run_ref:
            manifest = load_run_manifest(run_ref)
            target_atlas = manifest.get("target_atlas") or "WMBv1"
            # Hand-authored by a curator, so validate before use: an
            # unrecognised value must be a named diagnostic, not a
            # KeyError here or a schema failure after it reaches KB YAML.
            query_norm = validate_query_normalization(
                manifest.get("query_normalization"),
                context=f"{run_ref}/manifest.yaml",
            )
        method = "MapMyCells (via at_metrics.compute_edge_metrics)"
        # Keep the caveat on the evidence item itself, not only in the
        # run manifest: a consumer weighing this F1 (report synthesis
        # included) reads the item, not the manifest.
        method, explanation = apply_query_norm_caveat(
            method, explanation, query_norm
        )
        item: dict = {
            "evidence_type": "ANNOTATION_TRANSFER",
            "supports": supports,
            "source_dataset_accession": dataset_accession,
            "source_cluster_label": source_label,
            "target_atlas": target_atlas,
            "method": method,
            "explanation": explanation,
        }
        if query_norm != "raw":
            item["query_normalization"] = query_norm
        if correspondence:
            item["correspondence"] = correspondence
        if run_ref:
            item["run_ref"] = run_ref
        if metrics and metrics.get("metrics_by_level"):
            item["metrics_by_level"] = metrics["metrics_by_level"]
            best_rank = metrics.get("best_mapping_rank")
            if best_rank is not None:
                item["best_mapping_rank"] = best_rank
        return item

    run_ref = resolve_run_for_source(dataset_accession, taxonomy_id, source_label)
    if run_ref is None:
        print(
            f"  WARNING: no AT run resolves ({dataset_accession}, {taxonomy_id}, "
            f"{source_label}). Emitting NO_EVIDENCE.",
            file=sys.stderr,
        )
        return _item(
            supports="NO_EVIDENCE",
            run_ref=None,
            metrics=None,
            explanation=(
                f"Declared AT source {source_label!r} in {dataset_accession} "
                f"could not be resolved to an AT run against {taxonomy_id}; "
                f"no annotation-transfer numbers available for this edge."
            ),
        )

    try:
        metrics = compute_edge_metrics(
            run_ref=run_ref,
            source_label=source_label,
            edge_target=edge_target,
        )
    except Exception as exc:  # noqa: BLE001 — soft-skip on artifact issues
        print(
            f"  WARNING: compute_edge_metrics({run_ref}, {source_label}, "
            f"{edge_target}) failed: {exc}. Emitting NO_EVIDENCE.",
            file=sys.stderr,
        )
        return _item(
            supports="NO_EVIDENCE",
            run_ref=run_ref,
            metrics=None,
            explanation=(
                f"AT metrics for {source_label} → {edge_target} could not be "
                f"computed ({exc})."
            ),
        )

    if not metrics.get("metrics_by_level"):
        # Negative signal: the declared source does not transfer to this
        # candidate's lineage (issue #126 pt 4) — emit, don't drop.
        return _item(
            supports="NO_EVIDENCE",
            run_ref=run_ref,
            metrics=metrics,
            explanation=(
                f"Declared AT source {source_label!r} does not transfer to "
                f"{edge_target} — no metrics rows in {run_ref} reach this "
                f"target's lineage."
            ),
        )

    best_rank = metrics.get("best_mapping_rank")
    best_level = _RANK_TO_LEVEL_NAME.get(best_rank) if best_rank is not None else "?"
    return _item(
        supports=metrics.get("supports_default") or "NO_EVIDENCE",
        run_ref=run_ref,
        metrics=metrics,
        explanation=(
            f"AT transfer of {source_label} to {edge_target} — best F1 "
            f"{metrics.get('best_f1_score'):.3f} at "
            f"{best_level} level; per-level metrics populated "
            f"programmatically from {metrics.get('f1_source_relpath') or run_ref}."
        ),
    )


# ─── caveats (rule-based) ────────────────────────────────────────────────────


#: Query-normalisation caveat text. Defined in ``at_metrics`` alongside
#: the refresh path that has to re-derive it, so emit and refresh cannot
#: drift apart; re-exported here for callers of this module.
_QUERY_NORM_CAVEAT = QUERY_NORM_CAVEAT


def _caveats(
    property_comparisons: list[dict],
    ds: dict,
    at_signal: dict,
) -> list[dict]:
    out: list[dict] = []

    # MERFISH_REGISTRATION_UNCERTAINTY: lower_bound rollup drove the
    # region signal.
    completeness = ds.get("region_count_completeness")
    if completeness == "lower_bound":
        out.append({
            "caveat_type": "MERFISH_REGISTRATION_UNCERTAINTY",
            "description": (
                "Region signal is driven by a lower_bound rollup row — "
                "non-painted CCF2020 descendants are present and uncounted. "
                "region_fraction_100um value is a floor."
            ),
        })

    # AMBIGUOUS_MAPPING: any DISCORDANT property comparison.
    discordant = [
        pc for pc in property_comparisons if pc.get("alignment") == "DISCORDANT"
    ]
    if discordant:
        props = ", ".join(pc["property"] for pc in discordant)
        out.append({
            "caveat_type": "AMBIGUOUS_MAPPING",
            "description": (
                f"DISCORDANT property comparison(s): {props}. "
                "Mapping has unresolved counter-evidence."
            ),
        })

    # DISTRIBUTED_ACROSS_CLUSTERS: AT F1 at cluster level below the
    # bucket threshold.
    f1 = at_signal.get("f1")
    target_level = (at_signal.get("target_level") or "").lower()
    if (
        f1 is not None
        and target_level == "cluster"
        and f1 < AT_F1_DISTRIBUTED
    ):
        out.append({
            "caveat_type": "DISTRIBUTED_ACROSS_CLUSTERS",
            "description": (
                f"AT cluster-level F1 = {f1:.3f} is below the {AT_F1_DISTRIBUTED} "
                "threshold — source cells are scattered across multiple atlas "
                "clusters rather than concentrated here. Cleaner AT signal "
                "may live at a coarser taxonomy level."
            ),
        })

    return out


# ─── loaders ────────────────────────────────────────────────────────────────


def _find_node(graph: dict, node_id: str) -> dict | None:
    for n in graph.get("nodes") or []:
        if n.get("id") == node_id:
            return n
    return None


def _load_candidates(
    *,
    discovery_json_path: Path | None,
    classical_node_id: str,
    taxonomy_id: str,
    rank: int,
) -> list[dict]:
    """Load the Stage A discovery candidates from the canonical path, or
    a curator-supplied path. Raises if missing — the curator is expected
    to have run `just find-candidates` first.
    """
    if discovery_json_path is not None:
        path = Path(discovery_json_path)
    else:
        path = _canonical_discovery_path(classical_node_id, taxonomy_id, rank)
    if not path.exists():
        raise FileNotFoundError(
            f"Stage A discovery JSON not found at {path}. "
            "Run `just find-candidates ... {rank}` first, or pass "
            "--discovery-json explicitly."
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("candidates") or []


def _canonical_discovery_path(
    classical_node_id: str, taxonomy_id: str, rank: int,
) -> Path:
    """Find the most recent discovery JSON matching the rank.

    Convention: `research/{region}/{any-mapping-run-dir}/discovery_candidates_rank{rank}.json`.
    Picks the freshest file by mtime AND content-match on
    `classical_node_id` + `taxonomy_id` (cheap JSON header read) to
    avoid grabbing an unrelated dir's discovery file.

    The curator can override via --discovery-json.
    """
    root = repo_root()
    candidates = sorted(
        root.glob(f"research/**/discovery_candidates_rank{rank}.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    for p in candidates:
        try:
            head = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if (
            head.get("classical_node_id") == classical_node_id
            and head.get("taxonomy_id") == taxonomy_id
        ):
            return p
    return root / f"research/discovery_candidates_rank{rank}.json"  # non-existent sentinel


def _load_atlas_node(
    taxonomy_id: str,
    accession: str,
    rank: int,
    symbols: list[str] | None = None,
    gene_ids: Mapping[str, str | Pin] | None = None,
) -> dict | None:
    """Load the atlas node dict for a given accession from the taxonomy DB.

    The ``rank`` argument is accepted for backwards-compat but unused —
    the DB lookup keys off accession directly. Returns None when the
    accession isn't in the DB.

    Expression for ``symbols`` comes through ``TaxonomyDB.expression`` —
    the on-demand accessor (#189) — so genes not yet cached load from the
    MapMyCells stats file; ``gene_ids`` pins marker names to their curated
    ``ncbi_gene_id``. The returned dict carries ``expression``
    (``{symbol: mean}``), ``not_measured`` (``{symbol: reason}``),
    ``gene_symbols`` (``{symbol: atlas symbol it resolved to}``) and
    ``expression_source`` (stats file name) alongside the nodes-table
    fields, ``anatomical_location`` and metadata ``markers``.
    """
    del rank  # unused; kept in signature for backwards-compat
    from evidencell.taxonomy_db import TaxonomyDB, require_taxonomy_db

    # Raises when the DB is missing: these edges are written to the KB, and an
    # edge emitted without its atlas side would read as a real comparison.
    db = TaxonomyDB(require_taxonomy_db(taxonomy_id))
    node = db.get_node_by_accession(accession)
    if not node:
        return None

    expr = db.expression(symbols or [], accessions=[accession], gene_ids=gene_ids)
    anat_rows = db.get_node_anat_rows(accession)
    marker_cats = db.get_node_marker_categories(accession)

    nt_raw = node.get("nt_type")
    nt_obj = {"name_in_source": nt_raw} if nt_raw else None
    return {
        "id": node.get("node_id"),
        "cell_set_accession": node.get("short_form") or accession,
        "name": node.get("label"),
        "nt_type": nt_obj,
        "anatomical_location": [
            {
                "id": r["anat_id"],
                "label": r["anat_label"],
                "cell_count": r.get("cell_count"),
                "cell_ratio": r.get("cell_ratio"),
                "count_in_or_near_100um": r.get("count_in_or_near_100um"),
                "ratio_in_or_near_100um": r.get("ratio_in_or_near_100um"),
                "cell_count_completeness": r.get("cell_count_completeness"),
            }
            for r in anat_rows
        ],
        "expression": expr.for_node(accession),
        "not_measured": expr.not_measured,
        "gene_symbols": {
            name: sym for name in expr.genes if (sym := expr.gene_symbol(name)) is not None
        },
        "expression_source": expr.source_file,
        "markers": [
            {"name_in_source": sym, "category": cat}
            for sym, cat in marker_cats.items()
        ],
    }


# ─── writeback ──────────────────────────────────────────────────────────────


def _write_back(
    graph_file: Path,
    graph,
    edges: list[dict],
    candidates: list[dict],
    taxonomy_id: str,
    yaml_rt: YAML,
) -> None:
    """Append the new edges to the graph's `edges:` section + add taxonomy
    ref stubs for any referenced atlas nodes that aren't already in
    `nodes:`. Idempotent: skips edges whose id already exists. Uses the
    same ruamel round-trip handle that loaded the graph so quote-style
    is preserved across the file (avoids the underscore-float coercion
    bug on quote_keys).
    """
    existing_edge_ids = {
        e.get("id") for e in (graph.get("edges") or []) if isinstance(e, dict)
    }
    existing_node_ids = {
        n.get("id") for n in (graph.get("nodes") or []) if isinstance(n, dict)
    }

    new_edges: list[dict] = []
    new_stubs: list[dict] = []
    skipped: list[str] = []
    for edge, cand in zip(edges, candidates):
        if edge["id"] in existing_edge_ids:
            skipped.append(edge["id"])
            continue
        new_edges.append(edge)
        accession = edge["taxonomy_type"]
        if accession not in existing_node_ids:
            new_stubs.append({
                "id": accession,
                "name": cand.get("label") or accession,
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "taxonomy_id": taxonomy_id,
                "cell_set_accession": accession,
            })
            existing_node_ids.add(accession)

    if skipped:
        print(
            f"  emit-stage-b: skipped {len(skipped)} existing edge(s): "
            f"{', '.join(skipped)}",
            file=sys.stderr,
        )

    if not new_edges and not new_stubs:
        print("  emit-stage-b: nothing to write (all edges already present).", file=sys.stderr)
        return

    if graph.get("nodes") is None:
        graph["nodes"] = []
    if graph.get("edges") is None:
        graph["edges"] = []
    for stub in new_stubs:
        graph["nodes"].append(stub)
    for edge in new_edges:
        graph["edges"].append(edge)
    with graph_file.open("w", encoding="utf-8") as fh:
        yaml_rt.dump(graph, fh)
    print(
        f"  emit-stage-b: wrote {len(new_edges)} edge(s) + "
        f"{len(new_stubs)} stub node(s) to {graph_file}",
        file=sys.stderr,
    )


# ─── CLI ────────────────────────────────────────────────────────────────────


def _cli() -> None:
    p = argparse.ArgumentParser(
        prog="python -m evidencell.stage_b_emit",
        description="Mechanical Stage B emitter — issue #96.",
    )
    p.add_argument("classical_node_file", type=Path)
    p.add_argument("classical_node_id")
    p.add_argument("taxonomy_id")
    p.add_argument("rank", type=int)
    p.add_argument("top_k", type=int, nargs="?", default=5)
    p.add_argument(
        "--discovery-json", type=Path, default=None,
        help="Override the canonical discovery JSON path.",
    )
    p.add_argument(
        "--dry-run", action="store_true",
        help="Build edges but do not write back to the graph; print the YAML.",
    )
    args = p.parse_args()

    # Cache classical node on each candidate so _property_comparisons can
    # read it without re-loading the graph.
    graph_file = args.classical_node_file.resolve()
    yaml_rt = _yaml_rt()
    with graph_file.open(encoding="utf-8") as fh:
        graph = yaml_rt.load(fh)
    classical = _find_node(graph, args.classical_node_id)
    if not classical:
        print(
            f"ERROR: classical node {args.classical_node_id!r} not found in {graph_file}",
            file=sys.stderr,
        )
        sys.exit(1)

    candidates = _load_candidates(
        discovery_json_path=args.discovery_json,
        classical_node_id=args.classical_node_id,
        taxonomy_id=args.taxonomy_id,
        rank=args.rank,
    )[: args.top_k]
    for c in candidates:
        c["_classical_cache"] = classical

    at_source_sets = classical.get("at_source_sets") or []

    edges: list[dict] = []
    try:
        for cand in candidates:
            atlas = _load_atlas_node(
                args.taxonomy_id, cand["node_id"], args.rank,
                symbols=_classical_expression_symbols(classical),
                gene_ids=marker_gene_ids(classical),
            )
            edges.append(_build_edge(
                classical_node_id=args.classical_node_id,
                candidate=cand,
                atlas=atlas,
                taxonomy_id=args.taxonomy_id,
                at_source_sets=at_source_sets,
            ))
    except ExpressionUnavailable as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        # For dry-run preview we use plain yaml — these edges are
        # freshly-constructed plain dicts (no smuggled ruamel objects)
        # so safe_dump round-trip is fine and easier to eyeball.
        print(yaml.safe_dump(edges, sort_keys=False, default_flow_style=False, allow_unicode=True))
        return

    _write_back(graph_file, graph, edges, candidates, args.taxonomy_id, yaml_rt)


if __name__ == "__main__":
    _cli()
