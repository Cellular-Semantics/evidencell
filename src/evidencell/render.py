"""
evidencell render.py — Fact extractor and Markdown report generator.

Two-layer pipeline:
  1. `facts`   — deterministic extraction: reads KB YAML + references.json, emits
                 report_facts.json with every claim labelled by YAML provenance.
                 No LLM, no hallucination risk.
  2. `summary` / `drilldowns` / `index`
               — direct Markdown output (programmatic mode; use gen-report orchestrator
                 for LLM-assisted synthesis with hallucination guard).

CLI usage:
  python -m evidencell.render facts      <graph_file> --node NODE_ID [--output-dir DIR]
  python -m evidencell.render summary    <graph_file> [--node NODE_ID] [--output-dir DIR]
  python -m evidencell.render drilldowns <graph_file> --node NODE_ID [--pmid PMID] [--output-dir DIR]
  python -m evidencell.render index      <region> [--output-dir DIR]
"""

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml


# ── Constants ─────────────────────────────────────────────────────────────────

CONF_ORDER = {"HIGH": 0, "MODERATE": 1, "LOW": 2, "UNCERTAIN": 3, "REFUTED": 4}
CONF_BADGES = {
    "HIGH": "🟢 HIGH",
    "MODERATE": "🟡 MODERATE",
    "LOW": "🔴 LOW",
    "UNCERTAIN": "⚪ UNCERTAIN",
    "REFUTED": "⛔ REFUTED",
}
EVIDENCE_TYPE_LABELS = {
    "LITERATURE": "Literature",
    "ATLAS_METADATA": "Atlas metadata",
    "ANNOTATION_TRANSFER": "Annotation transfer",
    "SPATIAL_COLOCATION": "Spatial co-location",
    "PATCH_SEQ": "Patch-seq",
    "PROJECTION_SEQ": "Projection-seq",
    "ELECTROPHYSIOLOGY": "Electrophysiology",
    "MORPHOLOGY": "Morphology",
    "MARKER_ANALYSIS": "Marker analysis",
    "ATLAS_QUERY": "Atlas query",
}
REL_LABELS = {
    "EQUIVALENT": "≡ EQUIVALENT",
    "PARTIAL_OVERLAP": "~ PARTIAL OVERLAP",
    "CROSS_CUTTING": "✕ CROSS-CUTTING",
    "TYPE_A_SPLITS": "→ TYPE_A_SPLITS",
    "TYPE_A_MERGES": "← TYPE_A_MERGES",
    "SUBSET": "⊂ SUBSET",
    "SUPERSET": "⊃ SUPERSET",
    "NO_CORRESPONDENCE": "∅ NO CORRESPONDENCE",
    "UNCERTAIN": "? UNCERTAIN",
}

DRAFT_BANNER = (
    "> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.\n"
    "> All edges require expert review before use."
)
MERFISH_LOCATION_NOTE = (
    "> **Location note.** WMBv1 location data derives from MERFISH spatial\n"
    "> registration and records **soma position** only. Axonal and dendritic\n"
    "> projection targets are not reflected in atlas cluster location fields and\n"
    "> are not used in mapping assessments."
)


# ── Data class ────────────────────────────────────────────────────────────────

@dataclass
class RefEntry:
    label: str            # "[1]" or "[A]"
    pmid: str | None
    doi: str | None
    corpus_id: str | None
    query_url: str | None
    citation_line: str    # "Author et al. Year · PMID:…"
    used_for: str         # one-line purpose


# ── Helper functions ──────────────────────────────────────────────────────────

def _ot(term: dict | None) -> str:
    """Format an OntologyTerm dict as 'label (id)'."""
    if not term:
        return ""
    label = term.get("label", "")
    tid = term.get("id", "")
    if label and tid:
        return f"{label} ({tid})"
    return label or tid


def _conf_badge(conf: str) -> str:
    return CONF_BADGES.get(conf, conf)


def _rel_badge(rel: str) -> str:
    return REL_LABELS.get(rel, rel)


def _evidence_type_label(et: str) -> str:
    return EVIDENCE_TYPE_LABELS.get(et, et)


def _ref_identifier(ref_str: str) -> tuple[str, str]:
    """Parse 'PMID:31420995' or bare PMID into ('pmid', '31420995')."""
    if ref_str.startswith("PMID:"):
        return "pmid", ref_str[5:]
    if ref_str.startswith("DOI:"):
        return "doi", ref_str[4:]
    # Bare PMID (numeric) or DOI
    if ref_str.replace(".", "").replace("/", "").replace("-", "").isdigit():
        return "pmid", ref_str
    return "doi", ref_str


def _find_corpus_by_pmid(bare_pmid: str, refs: dict) -> dict | None:
    for entry in refs.values():
        if isinstance(entry, dict) and entry.get("pmid") == bare_pmid:
            return entry
    return None


def _find_corpus_by_doi(bare_doi: str, refs: dict) -> dict | None:
    for entry in refs.values():
        if isinstance(entry, dict) and entry.get("doi") == bare_doi:
            return entry
    return None


def _format_citation_line(entry: dict) -> str:
    """Format a references.json entry as 'Author et al. YYYY · PMID:…'"""
    authors = entry.get("authors", [])
    year = entry.get("year", "")
    pmid = entry.get("pmid", "")
    doi = entry.get("doi", "")
    if len(authors) == 0:
        author_str = "Unknown"
    elif len(authors) == 1:
        author_str = authors[0].split()[-1]
    elif len(authors) == 2:
        author_str = f"{authors[0].split()[-1]} & {authors[1].split()[-1]}"
    else:
        author_str = f"{authors[0].split()[-1]} et al."
    parts = [f"{author_str} {year}"]
    if pmid:
        parts.append(f"PMID:{pmid}")
    elif doi:
        parts.append(f"DOI:{doi}")
    return " · ".join(parts)


# ── Reference index builder ───────────────────────────────────────────────────

def build_reference_index(
    graph: dict,
    refs: dict,
    node_id: str | None = None,
) -> dict[str, RefEntry]:
    """
    Scan all evidence items for a node's edges (and node property sources) in
    document order. Assign [1]..[N] to literature/AT references, [A]..[Z] to
    AtlasQueryEvidence query_urls. Returns lookup keyed by normalized ref string.

    Only identifiers that actually appear in the graph are included — no invention.
    """
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    all_edges = graph.get("edges", [])
    edges = [e for e in all_edges if e.get("type_a") == node_id] if node_id else all_edges

    lit_n = [0]    # running counter for [1]..[N]
    qry_n = [0]    # running counter for [A]..[Z]
    index: dict[str, RefEntry] = {}

    def _add_lit(ref_str: str, used_for: str = "") -> str:
        ref_type, bare = _ref_identifier(ref_str)
        key = f"{ref_type}:{bare}"
        if key in index:
            return index[key].label
        if ref_type == "pmid":
            entry = _find_corpus_by_pmid(bare, refs)
        else:
            entry = _find_corpus_by_doi(bare, refs)
        lit_n[0] += 1
        label = f"[{lit_n[0]}]"
        if entry:
            citation_line = _format_citation_line(entry)
            pmid = entry.get("pmid")
            doi = entry.get("doi")
            corpus_id = entry.get("corpus_id")
        else:
            citation_line = ref_str
            pmid = bare if ref_type == "pmid" else None
            doi = bare if ref_type == "doi" else None
            corpus_id = None
        index[key] = RefEntry(
            label=label, pmid=pmid, doi=doi, corpus_id=corpus_id,
            query_url=None, citation_line=citation_line, used_for=used_for,
        )
        return label

    def _add_qry(query_url: str, atlas: str = "", filters: str = "") -> str:
        if query_url in index:
            return index[query_url].label
        qry_n[0] += 1
        label = f"[{chr(ord('A') + qry_n[0] - 1)}]"
        cite = f"{atlas}" if atlas else "Atlas query"
        index[query_url] = RefEntry(
            label=label, pmid=None, doi=None, corpus_id=None,
            query_url=query_url, citation_line=cite, used_for=filters,
        )
        return label

    # Scan classical node property sources (appear before edge evidence in document)
    if node_id and node_id in nodes_by_id:
        node = nodes_by_id[node_id]
        for src in node.get("location_sources", []):
            if src.get("ref"):
                _add_lit(src["ref"], "soma location")
        nt = node.get("nt_type") or {}
        for src in nt.get("sources", []):
            if src.get("ref"):
                _add_lit(src["ref"], "neurotransmitter type")
        for marker in node.get("defining_markers", []):
            sym = marker.get("symbol", "")
            for src in marker.get("sources", []):
                if src.get("ref"):
                    _add_lit(src["ref"], f"{sym} marker")
        for marker in node.get("neuropeptides", []):
            sym = marker.get("symbol", "")
            for src in marker.get("sources", []):
                if src.get("ref"):
                    _add_lit(src["ref"], f"{sym} neuropeptide")

    # Scan edge evidence items
    for edge in edges:
        for ev in edge.get("evidence", []):
            et = ev.get("evidence_type", "")
            if et == "LITERATURE":
                ref = ev.get("reference", "")
                if ref:
                    _add_lit(ref, (ev.get("explanation") or "")[:80].strip())
            elif et == "ATLAS_QUERY":
                qurl = ev.get("query_url", "")
                if qurl:
                    _add_qry(
                        qurl,
                        atlas=ev.get("atlas", ""),
                        filters=ev.get("filters_applied", ""),
                    )

    return index


# ── Structural helpers ────────────────────────────────────────────────────────

def _location_note(graph: dict) -> str | None:
    """
    Return the MERFISH soma-only location note if any terminal node has anatomical_location.
    """
    for node in graph.get("nodes", []):
        if node.get("is_terminal") and node.get("anatomical_location"):
            return MERFISH_LOCATION_NOTE
    return None


def _candidate_verdict(edge: dict, nodes_by_id: dict) -> str:
    """
    Derive verdict from confidence + property_comparisons.
    HIGH/MODERATE → 'Best candidate'
    LOW → 'Speculative'
    UNCERTAIN with DISCORDANT marker → 'Eliminated ({marker})'
    UNCERTAIN otherwise → 'Uncertain'
    """
    conf = edge.get("confidence", "")
    if conf in ("HIGH", "MODERATE"):
        return "Best candidate"
    if conf == "LOW":
        return "Speculative"
    if conf in ("UNCERTAIN", "REFUTED"):
        for pc in edge.get("property_comparisons", []):
            if pc.get("alignment") == "DISCORDANT" and "marker" in pc.get("property", ""):
                prop = pc["property"].replace("marker_", "")
                return f"Eliminated ({prop})"
        return "Eliminated" if conf == "UNCERTAIN" else "Refuted"
    return conf


def _best_edge(edges: list[dict], node_id: str) -> dict | None:
    """Return highest-confidence edge where type_a == node_id."""
    candidates = [e for e in edges if e.get("type_a") == node_id]
    if not candidates:
        return None
    return min(candidates, key=lambda e: CONF_ORDER.get(e.get("confidence", "REFUTED"), 99))


def _group_experiments(edges: list[dict]) -> list[dict]:
    """
    Collect proposed_experiments[] across edges.
    Group by leading method keyword. Deduplicate near-identical strings.
    Returns list of {group: str, experiments: [str], edge_ids: [str]}.
    """
    METHOD_KEYS = [
        ("MapMyCells", "MapMyCells / annotation transfer"),
        ("MapMyCell", "MapMyCells / annotation transfer"),
        ("patch-seq", "Patch-seq"),
        ("Patch-seq", "Patch-seq"),
        ("MERFISH", "MERFISH / spatial transcriptomics"),
        ("scRNA-seq", "scRNA-seq / single-cell"),
        ("snRNA-seq", "scRNA-seq / single-cell"),
    ]
    groups: dict[str, dict] = {}

    for edge in edges:
        for exp in edge.get("proposed_experiments", []):
            exp_str = exp.strip() if isinstance(exp, str) else str(exp)
            group_name = "Other"
            for keyword, name in METHOD_KEYS:
                if keyword in exp_str:
                    group_name = name
                    break
            if group_name not in groups:
                groups[group_name] = {"group": group_name, "experiments": [], "edge_ids": []}
            # Deduplicate: skip if a nearly identical string already present
            already = any(
                abs(len(x) - len(exp_str)) < 20 and x[:40] == exp_str[:40]
                for x in groups[group_name]["experiments"]
            )
            if not already:
                groups[group_name]["experiments"].append(exp_str)
            eid = edge.get("id", "")
            if eid and eid not in groups[group_name]["edge_ids"]:
                groups[group_name]["edge_ids"].append(eid)

    return list(groups.values())


def _node_b_info(edge: dict, nodes_by_id: dict) -> dict:
    """Extract display info for the atlas (type_b) node of an edge."""
    b_id = edge.get("type_b", "")
    b_node = nodes_by_id.get(b_id, {})
    return {
        "id": b_id,
        "name": b_node.get("name", b_id),
        "accession": b_node.get("cell_set_accession", ""),
        "supertype": "",  # filled from parent_hierarchy if present
        "n_cells": b_node.get("n_cells"),
        "taxonomy_level": b_node.get("taxonomy_level", ""),
    }


# ── Quotes extraction ─────────────────────────────────────────────────────────

def _collect_quotes(graph: dict, refs: dict, node_id: str) -> dict:
    """
    Collect all quotes referenced by quote_key fields in the node and its edges.
    Returns {quote_key: {text, section, claims}} — verbatim from references.json.
    Raises KeyError if a quote_key is present in YAML but absent from references.json.
    """
    quotes: dict = {}
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    node = nodes_by_id.get(node_id, {})

    def _add_quote(qk: str) -> None:
        if not qk or qk in quotes:
            return
        # Find in references.json
        corpus_id = qk.split("_")[0]
        corpus = refs.get(corpus_id, {})
        quote_obj = corpus.get("quotes", {}).get(qk)
        if quote_obj is None:
            raise KeyError(
                f"quote_key '{qk}' not found in references.json "
                f"(corpus_id='{corpus_id}'). Fix YAML or update references.json."
            )
        quotes[qk] = {
            "text": quote_obj["text"],
            "section": quote_obj.get("section", ""),
            "claims": quote_obj.get("claims", []),
        }

    # Node property sources
    for src in node.get("location_sources", []):
        _add_quote(src.get("quote_key", ""))
    for src in (node.get("nt_type") or {}).get("sources", []):
        _add_quote(src.get("quote_key", ""))
    for marker in node.get("defining_markers", []):
        for src in marker.get("sources", []):
            _add_quote(src.get("quote_key", ""))
    for marker in node.get("neuropeptides", []):
        for src in marker.get("sources", []):
            _add_quote(src.get("quote_key", ""))

    # Edge evidence
    for edge in graph.get("edges", []):
        if edge.get("type_a") != node_id:
            continue
        for ev in edge.get("evidence", []):
            _add_quote(ev.get("quote_key", ""))

    return quotes


# ── Facts extractor (primary output) ─────────────────────────────────────────

def extract_node_facts(
    graph: dict,
    refs: dict,
    node_id: str,
    graph_file: Path,
) -> dict:
    """
    Build report_facts dict for one classical node.
    This is the structured intermediate representation passed to the synthesis subagent.
    All fields trace directly to YAML source — no inference, no LLM.
    """
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    node = nodes_by_id.get(node_id)
    if node is None:
        raise ValueError(f"Node '{node_id}' not found in graph")
    if node.get("is_terminal"):
        raise ValueError(f"Node '{node_id}' is a terminal (atlas) node; reports are for classical nodes")

    all_edges = graph.get("edges", [])
    node_edges = sorted(
        [e for e in all_edges if e.get("type_a") == node_id],
        key=lambda e: CONF_ORDER.get(e.get("confidence", "UNCERTAIN"), 99),
    )

    # Detect draft vs canonical
    status = "draft" if "draft" in str(graph_file) else "canonical"

    # Check for MERFISH location data
    has_merfish = any(
        n.get("is_terminal") and n.get("anatomical_location")
        for n in graph.get("nodes", [])
    )

    # Build reference index
    ref_index = build_reference_index(graph, refs, node_id)
    # key → label string lookup
    ref_labels: dict[str, str] = {k: v.label for k, v in ref_index.items()}

    def _ref_label(ref_str: str) -> str:
        ref_type, bare = _ref_identifier(ref_str)
        return ref_labels.get(f"{ref_type}:{bare}", f"[?{ref_str}]")

    def _query_label(qurl: str) -> str:
        return ref_labels.get(qurl, f"[?{qurl[:20]}]")

    # Classical node properties
    cl = node.get("cl_mapping") or {}
    cl_term_str = _ot(cl.get("cl_term")) if cl else ""

    nt_obj = node.get("nt_type") or {}
    nt_sources_labels = [_ref_label(s["ref"]) for s in nt_obj.get("sources", []) if s.get("ref")]

    def _marker_refs(marker: dict) -> list[str]:
        return [_ref_label(s["ref"]) for s in marker.get("sources", []) if s.get("ref")]

    soma_locations = []
    for loc in node.get("anatomical_location", []):
        soma_locations.append({
            "id": loc.get("id", ""),
            "label": loc.get("label", ""),
            "name_in_source": loc.get("name_in_source", ""),
        })

    location_refs = [_ref_label(s["ref"]) for s in node.get("location_sources", []) if s.get("ref")]

    # Edges
    edge_facts = []
    for edge in node_edges:
        b_info = _node_b_info(edge, nodes_by_id)
        verdict = _candidate_verdict(edge, nodes_by_id)

        # Evidence items with ref labels
        ev_items = []
        for ev in edge.get("evidence", []):
            et = ev.get("evidence_type", "")
            item: dict = {
                "evidence_type": et,
                "supports": ev.get("supports", ""),
                "explanation": (ev.get("explanation") or "").strip(),
            }
            if et == "LITERATURE":
                ref = ev.get("reference", "")
                item["ref_label"] = _ref_label(ref) if ref else ""
                item["reference"] = ref
                item["snippet"] = (ev.get("snippet") or "").strip()
                item["study_type"] = ev.get("study_type", "")
            elif et == "ATLAS_QUERY":
                qurl = ev.get("query_url", "")
                item["ref_label"] = _query_label(qurl) if qurl else ""
                item["query_url"] = qurl
                item["atlas"] = ev.get("atlas", "")
                item["filters_applied"] = ev.get("filters_applied", "")
                item["atlas_version"] = ev.get("atlas_version", "")
            elif et == "ATLAS_METADATA":
                item["atlas"] = ev.get("atlas", "")
                item["cell_set_accession"] = ev.get("cell_set_accession", "")
                item["metadata_url"] = ev.get("metadata_url", "")
            elif et == "ANNOTATION_TRANSFER":
                item["method"] = ev.get("method", "")
                item["target_atlas"] = ev.get("target_atlas", "")
                item["source_dataset_accession"] = ev.get("source_dataset_accession", "")
                item["best_f1_score"] = ev.get("best_f1_score")
                item["best_mapping_level"] = ev.get("best_mapping_level", "")
                item["source_species"] = ev.get("source_species", "")
                item["target_species"] = ev.get("target_species", "")
                item["metrics_by_level"] = ev.get("metrics_by_level", [])
            ev_items.append(item)

        edge_facts.append({
            "id": edge["id"],
            "node_b_id": b_info["id"],
            "node_b_name": b_info["name"],
            "node_b_accession": b_info["accession"],
            "supertype": b_info["supertype"],
            "n_cells": b_info["n_cells"],
            "taxonomy_level": b_info["taxonomy_level"],
            "confidence": edge.get("confidence", ""),
            "relationship": edge.get("relationship", ""),
            "verdict": verdict,
            "evidence_items": ev_items,
            "property_comparisons": edge.get("property_comparisons", []),
            "caveats": edge.get("caveats", []),
            "unresolved_questions": edge.get("unresolved_questions", []),
            "proposed_experiments": edge.get("proposed_experiments", []),
            "notes": edge.get("notes", ""),
        })

    # Quotes: collect all quote_keys referenced in node + edges
    # (may raise KeyError if quote_key absent from references.json)
    try:
        quotes = _collect_quotes(graph, refs, node_id)
    except KeyError as exc:
        print(f"WARNING: {exc}", file=sys.stderr)
        quotes = {}

    # Reference index as serialisable dict
    ref_index_serial = {
        k: {
            "label": v.label,
            "pmid": v.pmid,
            "doi": v.doi,
            "corpus_id": v.corpus_id,
            "query_url": v.query_url,
            "citation_line": v.citation_line,
            "used_for": v.used_for,
        }
        for k, v in ref_index.items()
    }

    return {
        "graph_meta": {
            "name": graph.get("name", ""),
            "target_atlas": graph.get("target_atlas", ""),
            "brain_region": _ot(graph.get("brain_region")),
            "species": _ot(graph.get("species")),
            "status": status,
            "creation_date": str(graph.get("creation_date", "")),
            "graph_file": str(graph_file),
            "has_merfish_location": has_merfish,
        },
        "reference_index": ref_index_serial,
        "classical_nodes": [{
            "id": node_id,
            "name": node.get("name", ""),
            "definition_basis": node.get("definition_basis", ""),
            "cl_term": cl_term_str,
            "cl_mapping_type": cl.get("mapping_type", "") if cl else "",
            "nt": nt_obj.get("name_in_source", ""),
            "nt_refs": nt_sources_labels,
            "defining_markers": [
                {
                    "symbol": m.get("symbol", ""),
                    "refs": _marker_refs(m),
                }
                for m in node.get("defining_markers", [])
            ],
            "negative_markers": [m.get("symbol", "") for m in node.get("negative_markers", [])],
            "neuropeptides": [
                {
                    "symbol": m.get("symbol", ""),
                    "refs": _marker_refs(m),
                }
                for m in node.get("neuropeptides", [])
            ],
            "soma_locations": soma_locations,
            "location_refs": location_refs,
            "morphology_notes": node.get("morphology_notes", ""),
            "electrophysiology_class": node.get("electrophysiology_class", ""),
            "notes": node.get("notes", ""),
        }],
        "edges": edge_facts,
        "quotes": quotes,
    }


# ── Programmatic Markdown renderers ───────────────────────────────────────────

def render_summary(
    graph: dict,
    refs: dict,
    node_id: str,
    out_path: Path,
    graph_file: Path,
) -> None:
    """
    Write Tier 1 summary report Markdown for one classical node.
    Programmatic mode — constructs prose from YAML fields directly.
    For higher-quality synthesis, use the gen-report orchestrator workflow.
    """
    facts = extract_node_facts(graph, refs, node_id, graph_file)
    gm = facts["graph_meta"]
    cn = facts["classical_nodes"][0]
    edges = facts["edges"]
    ref_index = facts["reference_index"]

    lines: list[str] = []

    # 1. Header
    lines.append(f"# {cn['name']} — {gm['target_atlas']} Mapping Report")
    status_tag = f"*{gm['status'].capitalize()} · {gm['creation_date']} · Source: `{gm['graph_file']}`*"
    lines.append(status_tag)
    if gm["status"] == "draft":
        lines.append("")
        lines.append(DRAFT_BANNER)
    lines.append("")
    lines.append("---")
    lines.append("")

    # 2. Location note (conditional)
    loc_note = _location_note(graph)
    if loc_note:
        lines.append(loc_note)
        lines.append("")
        lines.append("---")
        lines.append("")

    # 3. Classical type table
    lines.append("## Classical type")
    lines.append("")
    markers_str = ", ".join(
        f"{m['symbol']}+"
        for m in cn["defining_markers"]
    )
    neg_str = ", ".join(f"{s}−" for s in cn["negative_markers"])
    np_str = ", ".join(m["symbol"] for m in cn["neuropeptides"])
    def _loc_label(loc: dict) -> str:
        name = loc.get("name_in_source") or loc.get("label") or loc.get("id", "")
        loc_id = loc.get("id", "")
        return f"{name} [{loc_id}]" if loc_id else name

    loc_str = "; ".join(_loc_label(loc) for loc in cn["soma_locations"])
    loc_refs = " ".join(cn["location_refs"])
    nt_refs = " ".join(cn["nt_refs"])
    # Deduplicate refs
    all_marker_refs = list(dict.fromkeys(
        ref for m in cn["defining_markers"] for ref in m["refs"]
    ))
    cl_str = cn["cl_term"] if cn["cl_term"] else "—"

    lines.append("| Property | Value | References |")
    lines.append("|---|---|---|")
    lines.append(f"| CL term | {cl_str} | |")
    lines.append(f"| Soma location | {loc_str} | {loc_refs} |")
    lines.append(f"| NT | {cn['nt']} | {nt_refs} |")
    lines.append(f"| Markers | {markers_str} | {' '.join(all_marker_refs)} |")
    if neg_str:
        lines.append(f"| Negative | {neg_str} | |")
    if np_str:
        np_refs = " ".join(dict.fromkeys(
            ref for m in cn["neuropeptides"] for ref in m["refs"]
        ))
        lines.append(f"| Neuropeptides | {np_str} | {np_refs} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 4. Mapping candidates table
    lines.append("## Mapping candidates")
    lines.append("")
    lines.append("| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |")
    lines.append("|---|---|---|---|---|---|")
    rank = 0
    for edge in edges:
        conf = edge["confidence"]
        if conf in ("HIGH", "MODERATE", "LOW"):
            rank += 1
            rank_str = str(rank)
        else:
            rank_str = "—"
        name = edge["node_b_name"]
        acc = edge.get("node_b_accession", "")
        cluster_label = f"{name} [{acc}]" if acc else name
        n_cells = edge["n_cells"] if edge["n_cells"] is not None else "—"
        badge = _conf_badge(conf)
        verdict = edge["verdict"]
        lines.append(f"| {rank_str} | {cluster_label} | {edge['supertype']} | {n_cells} | {badge} | {verdict} |")
    lines.append("")

    if edges:
        rel = edges[0]["relationship"]
        lines.append(f"All edges: `{rel}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 5. Candidate paragraphs
    uncertain_edges = [e for e in edges if e["confidence"] in ("UNCERTAIN", "REFUTED")]
    confident_edges = [e for e in edges if e["confidence"] not in ("UNCERTAIN", "REFUTED")]

    for edge in confident_edges:
        conf = edge["confidence"]
        name = edge["node_b_name"]
        n = edge["n_cells"] if edge["n_cells"] is not None else "?"
        badge = _conf_badge(conf)
        lines.append(f"## {name} · {badge}")
        lines.append("")

        support_items = [ev for ev in edge["evidence_items"] if ev["supports"] in ("SUPPORT", "PARTIAL")]
        refute_items = [ev for ev in edge["evidence_items"] if ev["supports"] == "REFUTE"]

        if support_items:
            lines.append("**Supporting evidence:**")
            lines.append("")
            for ev in support_items:
                ref_lbl = ev.get("ref_label", "")
                et_lbl = _evidence_type_label(ev["evidence_type"])
                expl = ev.get("explanation", "")
                filt = ev.get("filters_applied", "")
                detail = filt if filt else expl
                lines.append(f"- {detail} [{et_lbl}]{' ' + ref_lbl if ref_lbl else ''}")
            lines.append("")

        concerns = []
        for ev in refute_items:
            ref_lbl = ev.get("ref_label", "")
            expl = ev.get("explanation", "")
            concerns.append(f"- {expl} [{_evidence_type_label(ev['evidence_type'])}]{' ' + ref_lbl if ref_lbl else ''}")
        for pc in edge["property_comparisons"]:
            if pc.get("alignment") in ("DISCORDANT", "APPROXIMATE"):
                note = pc.get("notes", "")
                prop = pc["property"]
                a_val = pc.get("node_a_value", "")
                b_val = pc.get("node_b_value", "")
                aln = pc["alignment"]
                concerns.append(f"- **{prop}** ({aln}): A={a_val} / B={b_val}. {note}")
        for cav in edge["caveats"]:
            desc = cav.get("description", "").strip()
            concerns.append(f"- {desc}")

        if concerns:
            lines.append("**Concerns:**")
            lines.append("")
            lines.extend(concerns)
            lines.append("")

        # Upgrade path
        upgrade_parts = []
        for q in edge.get("unresolved_questions", []):
            upgrade_parts.append(f"- *Unresolved:* {q}")
        for exp in edge.get("proposed_experiments", []):
            upgrade_parts.append(f"- *Proposed:* {exp}")
        if upgrade_parts:
            lines.append("**What would upgrade confidence:**")
            lines.append("")
            lines.extend(upgrade_parts)
            lines.append("")

        lines.append("---")
        lines.append("")

    # Eliminated / uncertain block
    if uncertain_edges:
        lines.append("## Eliminated candidates")
        lines.append("")
        # Check for shared disqualifier
        common_discordant = None
        for edge in uncertain_edges:
            for pc in edge.get("property_comparisons", []):
                if pc.get("alignment") == "DISCORDANT" and "marker" in pc.get("property", ""):
                    if common_discordant is None:
                        common_discordant = pc["property"]
                    elif common_discordant != pc["property"]:
                        common_discordant = None
                        break
        if common_discordant:
            prop = common_discordant.replace("marker_", "")
            lines.append(f"**Primary reason:** Shared disqualifying signal: {prop} is DISCORDANT across all UNCERTAIN edges.")
            lines.append("")
        for edge in uncertain_edges:
            name = edge["node_b_name"]
            n = edge["n_cells"] if edge["n_cells"] is not None else "?"
            refutes = [
                ev for ev in edge["evidence_items"] if ev["supports"] == "REFUTE"
            ]
            lines.append(f"**{name}** ({n} cells)")
            for ev in refutes:
                ref_lbl = ev.get("ref_label", "")
                expl = ev.get("explanation", "")
                lines.append(f"- {expl} {ref_lbl}".strip())
            for pc in edge.get("property_comparisons", []):
                if pc.get("alignment") == "DISCORDANT":
                    note = pc.get("notes", "")
                    lines.append(f"- {pc['property']}: {note}")
            lines.append("")
        lines.append("---")
        lines.append("")

    # 6. Proposed experiments
    all_node_edges_raw = [e_raw for e_raw in graph.get("edges", []) if e_raw.get("type_a") == node_id]
    exp_groups = _group_experiments(all_node_edges_raw)
    if exp_groups:
        lines.append("## Proposed experiments")
        lines.append("")
        for i, grp in enumerate(exp_groups, 1):
            lines.append(f"### {i} — {grp['group']}")
            lines.append("")
            for exp in grp["experiments"]:
                lines.append(f"- {exp}")
            lines.append(f"*Resolves: {', '.join(grp['edge_ids'])}*")
            lines.append("")
        lines.append("---")
        lines.append("")

    # 7. Open questions
    all_questions = []
    seen_q: set = set()
    for edge in edges:
        for q in edge.get("unresolved_questions", []):
            q_str = q.strip() if isinstance(q, str) else str(q)
            if q_str not in seen_q:
                seen_q.add(q_str)
                all_questions.append(q_str)
    if all_questions:
        lines.append("## Open questions")
        lines.append("")
        for i, q in enumerate(all_questions, 1):
            lines.append(f"{i}. {q}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # 8. Evidence base table
    lines.append("## Evidence base")
    lines.append("")
    lines.append("| Edge | Evidence types | Supports |")
    lines.append("|---|---|---|")
    for edge in edges:
        eid = edge["id"]
        for ev in edge["evidence_items"]:
            et_lbl = _evidence_type_label(ev["evidence_type"])
            ref_lbl = ev.get("ref_label", "")
            supports = ev.get("supports", "")
            lines.append(f"| {eid} | {et_lbl}{' ' + ref_lbl if ref_lbl else ''} | {supports} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 9. References
    lines.append("## References")
    lines.append("")
    lines.append("| # | Citation | PMID | Used for |")
    lines.append("|---|---|---|---|")

    # Sort: numbered first, then lettered
    lit_entries = [(k, v) for k, v in ref_index.items() if not v["label"].startswith("[A") and not v["label"][1].isalpha()]
    query_entries = [(k, v) for k, v in ref_index.items() if v["query_url"]]
    lit_entries.sort(key=lambda x: int(x[1]["label"][1:-1]) if x[1]["label"][1:-1].isdigit() else 99)

    for k, v in lit_entries:
        pmid = v.get("pmid", "")
        cite = v.get("citation_line", "")
        used = v.get("used_for", "")
        pmid_str = f"[{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)" if pmid else "—"
        lines.append(f"| {v['label']} | {cite} | {pmid_str} | {used} |")
    for k, v in query_entries:
        qurl = v.get("query_url", "")
        cite = v.get("citation_line", "")
        filters = v.get("used_for", "")
        url_str = f"[view]({qurl})" if qurl else "—"
        lines.append(f"| {v['label']} | {cite} | — | {filters} · {url_str} |")

    lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {out_path}")


def render_drilldown(
    graph: dict,
    refs: dict,
    node_id: str,
    pmid_or_corpus: str,
    out_path: Path,
    graph_file: Path,
    summary_path: Path | None = None,
) -> None:
    """
    Write Tier 2 drill-down for one paper.
    All quotes come verbatim from references.json — raises KeyError if quote_key missing.
    """
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    node_edges = [e for e in graph.get("edges", []) if e.get("type_a") == node_id]

    # Resolve corpus entry
    bare_pmid = pmid_or_corpus.removeprefix("PMID:")
    corpus_entry = _find_corpus_by_pmid(bare_pmid, refs) or refs.get(pmid_or_corpus)
    if corpus_entry is None:
        raise ValueError(f"PMID/corpus_id '{pmid_or_corpus}' not found in references.json")

    corpus_id = corpus_entry["corpus_id"]
    authors = corpus_entry.get("authors", [])
    year = corpus_entry.get("year", "")
    pmid = corpus_entry.get("pmid", "")
    doi = corpus_entry.get("doi", "")
    title = corpus_entry.get("title", "")
    quotes = corpus_entry.get("quotes", {})

    # Author string for filename
    if authors:
        first_author_last = authors[0].split()[-1]
    else:
        first_author_last = "Unknown"

    cite_line = _format_citation_line(corpus_entry)
    back_link = f"[← Back to summary report]({summary_path.name})" if summary_path else ""

    lines: list[str] = []
    lines.append(f"# Evidence Drill-down: {first_author_last} et al. {year}")

    # Find edges citing this paper in edge evidence items
    citing_edges = []
    for edge in node_edges:
        for ev in edge.get("evidence", []):
            ref = ev.get("reference", "")
            ref_type, bare = _ref_identifier(ref) if ref else ("", "")
            if bare == pmid or bare == doi or bare == corpus_id:
                citing_edges.append(edge)
                break

    # Also scan node marker sources — papers cited there provide classical-type
    # evidence that informs all edges, even if not listed per-edge.
    node = nodes_by_id.get(node_id, {})
    node_marker_refs: list[dict] = []
    for field in ("defining_markers", "negative_markers"):
        for m in node.get(field, []):
            for src in m.get("sources", []):
                ref = src.get("ref", "")
                _, bare = _ref_identifier(ref) if ref else ("", "")
                if bare == pmid or bare == doi or bare == corpus_id:
                    node_marker_refs.append(
                        {"symbol": m.get("symbol", ""), "quote_key": src.get("quote_key", "")}
                    )
    for np in node.get("neuropeptides", []):
        if isinstance(np, dict):
            for src in np.get("sources", []):
                ref = src.get("ref", "")
                _, bare = _ref_identifier(ref) if ref else ("", "")
                if bare == pmid or bare == doi or bare == corpus_id:
                    node_marker_refs.append(
                        {"symbol": np.get("symbol", ""), "quote_key": src.get("quote_key", "")}
                    )

    # If paper only cited in node markers, it applies to all edges for this node
    paper_in_node_markers = bool(node_marker_refs)
    if not citing_edges and paper_in_node_markers:
        citing_edges = list(node_edges)

    edge_desc = "; ".join(
        f"{e.get('type_a', '')} → {nodes_by_id.get(e.get('type_b', ''), {}).get('name', e.get('type_b', ''))}"
        for e in citing_edges
    )
    if citing_edges:
        lines.append(f"*Supporting: {edge_desc}*")
    if back_link:
        lines.append(f"*{back_link}*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 2. Citation + why
    lines.append(f"**{cite_line}**")
    lines.append("")
    if title:
        lines.append(f"*{title}*")
        lines.append("")

    # Explanation from first citing evidence item
    for edge in citing_edges:
        for ev in edge.get("evidence", []):
            expl = (ev.get("explanation") or "").strip()
            if expl and ev.get("evidence_type") == "LITERATURE":
                lines.append("**Why this paper matters for the mapping.**")
                lines.append(expl)
                lines.append("")
                break

    lines.append("---")
    lines.append("")

    # 3. Per-property evidence sections from quotes
    if quotes:
        lines.append("## Evidence from this paper")
        lines.append("")
        first_author_str = authors[0].split()[-1] if authors else "Unknown"
        for qk, qobj in quotes.items():
            text = qobj["text"]
            section = qobj.get("section", "")
            claims = qobj.get("claims", [])
            lines.append(f"### {section or qk}")
            lines.append("")
            lines.append(f"> {text}")
            # Attribution line: visible miniref + hidden quote_key for hook validation
            lines.append(
                f"> — {first_author_str} et al. {year}, {section} "
                f"<!-- quote_key: {qk} -->"
            )
            lines.append("")
            if claims:
                lines.append(f"*Claims: {', '.join(claims)}*")
                lines.append("")

    # 4. Summary scorecard
    # Build from node marker sources citing this paper (have quote_key + symbol);
    # cross-reference alignment from edge property_comparisons where property contains symbol.
    lines.append("## Evidence summary")
    lines.append("")
    lines.append("| Property | Claims | Best alignment | Quote key |")
    lines.append("|---|---|---|---|")
    seen_qk: set[str] = set()
    for mr in node_marker_refs:
        symbol = mr["symbol"]
        qk = mr.get("quote_key", "")
        if qk in seen_qk:
            continue
        seen_qk.add(qk)
        # Find best alignment from edge property_comparisons for this marker
        best_aln = "—"
        for edge in node_edges:
            for pc in edge.get("property_comparisons", []):
                prop = pc.get("property", "")
                if symbol.lower() in prop.lower():
                    best_aln = pc.get("alignment", "—")
                    break
        qobj = quotes.get(qk, {})
        claims = ", ".join(qobj.get("claims", [])) or "—"
        lines.append(f"| {symbol} | {claims} | {best_aln} | {qk} |")
    # Fallback: edge evidence items that directly cite this paper
    if not node_marker_refs:
        for edge in citing_edges:
            for pc in edge.get("property_comparisons", []):
                for ev in edge.get("evidence", []):
                    ref = ev.get("reference", "")
                    _, bare = _ref_identifier(ref) if ref else ("", "")
                    if bare == pmid or bare == doi or bare == corpus_id:
                        prop = pc.get("property", "")
                        b_val = pc.get("node_b_value", "")
                        aln = pc.get("alignment", "")
                        lines.append(f"| {prop} | {b_val} | {aln} | — |")
                        break

    lines.append("")
    lines.append("---")
    lines.append("")

    # 5. Critical gap
    open_qs = []
    for edge in citing_edges:
        for q in edge.get("unresolved_questions", []):
            q_str = q.strip() if isinstance(q, str) else str(q)
            if q_str not in open_qs:
                open_qs.append(q_str)
    if open_qs:
        lines.append("## Critical gap")
        lines.append("")
        for q in open_qs:
            lines.append(f"- {q}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # 6. Footer
    source_methods = list({
        qobj.get("source_method", "") for qobj in quotes.values()
        if qobj.get("source_method")
    })
    statuses = list({
        qobj.get("status", "") for qobj in quotes.values() if qobj.get("status")
    })
    lines.append(f"*Drill-down generated from: references.json (corpus_id: {corpus_id})*")
    if source_methods:
        lines.append(f"*Quotes: source_method={', '.join(source_methods)}, status={', '.join(statuses)}*")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {out_path}")


def render_index(region: str, kb_root: Path, out_path: Path) -> None:
    """
    Scan all *.yaml in kb/{draft|mappings}/{region}/.
    For each non-terminal node: name, cl_mapping, best edge (highest confidence),
    edge count by tier. Write sorted index table.
    """
    # Find region directory (draft takes precedence for display)
    region_dirs = []
    for base in (kb_root / "draft", kb_root / "mappings"):
        rdir = base / region
        if rdir.is_dir():
            region_dirs.append((rdir, "draft" if "draft" in str(base) else "canonical"))

    if not region_dirs:
        raise FileNotFoundError(f"Region '{region}' not found under {kb_root}")

    rows = []
    for rdir, status in region_dirs:
        for yaml_file in sorted(rdir.glob("*.yaml")):
            graph = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
            if not graph:
                continue
            nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
            all_edges = graph.get("edges", [])
            for node in graph.get("nodes", []):
                if node.get("is_terminal"):
                    continue
                node_id = node["id"]
                node_edges = [e for e in all_edges if e.get("type_a") == node_id]
                best = _best_edge(all_edges, node_id)
                best_conf = best["confidence"] if best else "—"
                best_b = nodes_by_id.get(best["type_b"], {}).get("name", best["type_b"]) if best else "—"

                tier_counts = {c: 0 for c in ("HIGH", "MODERATE", "LOW", "UNCERTAIN")}
                for e in node_edges:
                    c = e.get("confidence", "")
                    if c in tier_counts:
                        tier_counts[c] += 1

                cl = node.get("cl_mapping") or {}
                cl_str = _ot(cl.get("cl_term")) if cl else "—"

                tier_summary = ", ".join(
                    f"{v} {k}" for k, v in tier_counts.items() if v > 0
                )
                breakdown = f"{len(node_edges)} ({tier_summary})"

                rows.append({
                    "name": node.get("name", node_id),
                    "cl_term": cl_str,
                    "best_atlas_hit": best_b,
                    "best_conf": best_conf,
                    "candidates": breakdown,
                    "report_link": f"{node_id}_summary.md",
                    "conf_order": CONF_ORDER.get(best_conf, 99),
                })

    rows.sort(key=lambda r: (r["conf_order"], r["name"]))

    today = date.today().isoformat()
    n_types = len(rows)
    statuses = "/".join(dict.fromkeys(s for _, s in region_dirs))

    header_lines = [
        f"# {region.capitalize()} Cell Type Mapping Index",
        f"*{n_types} classical types · {today} · {statuses}*",
        "",
    ]

    table_lines = [
        "| Classical type | CL term | Best atlas hit | Best confidence | Candidates | Link |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        badge = _conf_badge(row["best_conf"])
        table_lines.append(
            f"| {row['name']} | {row['cl_term']} | {row['best_atlas_hit']} | "
            f"{badge} | {row['candidates']} | [report]({row['report_link']}) |"
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(header_lines + table_lines + [""]), encoding="utf-8")
    print(f"Written: {out_path}")


# ── CLI entry point ───────────────────────────────────────────────────────────

def _load_graph_and_refs(graph_file: Path) -> tuple[dict, dict]:
    from evidencell.paths import refs_path_for_graph

    graph = yaml.safe_load(graph_file.read_text(encoding="utf-8"))
    if not graph:
        raise ValueError(f"Empty or invalid YAML: {graph_file}")
    refs_file = refs_path_for_graph(graph_file)
    if refs_file.exists():
        refs = json.loads(refs_file.read_text(encoding="utf-8"))
    else:
        print(f"WARNING: references.json not found at {refs_file}; quotes will be unavailable", file=sys.stderr)
        refs = {}
    return graph, refs


def _classical_nodes(graph: dict) -> list[dict]:
    return [n for n in graph.get("nodes", []) if not n.get("is_terminal")]


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="python -m evidencell.render",
        description="evidencell report generator",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # facts
    p_facts = sub.add_parser("facts", help="Extract structured facts JSON for synthesis subagent")
    p_facts.add_argument("graph_file", type=Path)
    p_facts.add_argument("--node", required=True, help="Classical node id")
    p_facts.add_argument("--output-dir", type=Path, default=None)

    # summary
    p_sum = sub.add_parser("summary", help="Generate Markdown summary report (programmatic mode)")
    p_sum.add_argument("graph_file", type=Path)
    p_sum.add_argument("--node", default=None, help="Classical node id (default: all)")
    p_sum.add_argument("--output-dir", type=Path, default=None)
    p_sum.add_argument("--drilldowns", action="store_true", help="Also generate drill-downs")

    # drilldowns
    p_dd = sub.add_parser("drilldowns", help="Generate Markdown drill-down reports")
    p_dd.add_argument("graph_file", type=Path)
    p_dd.add_argument("--node", required=True, help="Classical node id")
    p_dd.add_argument("--pmid", default=None, help="Specific PMID (default: all cited papers)")
    p_dd.add_argument("--output-dir", type=Path, default=None)

    # index
    p_idx = sub.add_parser("index", help="Generate region index")
    p_idx.add_argument("region", help="Region name (e.g. hippocampus)")
    p_idx.add_argument("--output-dir", type=Path, default=None)

    args = parser.parse_args()

    if args.cmd == "facts":
        from evidencell.paths import reports_dir_for_region, region_from_graph
        graph_file = args.graph_file.resolve()
        graph, refs = _load_graph_and_refs(graph_file)
        facts = extract_node_facts(graph, refs, args.node, graph_file)
        out_dir = args.output_dir or reports_dir_for_region(region_from_graph(graph_file))
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{args.node}_facts.json"
        out_path.write_text(json.dumps(facts, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Written: {out_path}")

    elif args.cmd == "summary":
        from evidencell.paths import reports_dir_for_region, region_from_graph
        graph_file = args.graph_file.resolve()
        graph, refs = _load_graph_and_refs(graph_file)
        out_dir = args.output_dir or reports_dir_for_region(region_from_graph(graph_file))
        nodes = _classical_nodes(graph)
        if args.node:
            node_ids = [args.node]
        else:
            node_ids = [n["id"] for n in nodes]
        for nid in node_ids:
            out_path = out_dir / f"{nid}_summary.md"
            render_summary(graph, refs, nid, out_path, graph_file)
            if args.drilldowns:
                # Generate all drill-downs for this node
                from evidencell.paths import refs_path_for_graph as _rfg
                refs_file = _rfg(graph_file)
                if refs_file.exists():
                    _gen_all_drilldowns(graph, refs, nid, out_dir, graph_file)

    elif args.cmd == "drilldowns":
        from evidencell.paths import reports_dir_for_region, region_from_graph
        graph_file = args.graph_file.resolve()
        graph, refs = _load_graph_and_refs(graph_file)
        out_dir = args.output_dir or reports_dir_for_region(region_from_graph(graph_file))
        if args.pmid:
            _gen_single_drilldown(graph, refs, args.node, args.pmid, out_dir, graph_file)
        else:
            _gen_all_drilldowns(graph, refs, args.node, out_dir, graph_file)

    elif args.cmd == "index":
        # Find kb root relative to cwd
        kb_root = Path.cwd() / "kb"
        out_dir = args.output_dir
        if out_dir is None:
            from evidencell.paths import reports_dir_for_region
            out_dir = reports_dir_for_region(args.region)
        out_path = out_dir / "index.md"
        render_index(args.region, kb_root, out_path)


def _gen_single_drilldown(
    graph: dict, refs: dict, node_id: str, pmid: str, out_dir: Path, graph_file: Path
) -> None:
    bare_pmid = pmid.removeprefix("PMID:")
    corpus_entry = _find_corpus_by_pmid(bare_pmid, refs) or refs.get(pmid)
    if corpus_entry is None:
        print(f"WARNING: PMID '{pmid}' not found in references.json; skipping", file=sys.stderr)
        return
    authors = corpus_entry.get("authors", [])
    year = corpus_entry.get("year", "")
    first_author_last = authors[0].split()[-1] if authors else "Unknown"
    filename = f"{node_id}_drilldown_{first_author_last}{year}.md"
    out_path = out_dir / filename
    summary_path = out_dir / f"{node_id}_summary.md"
    render_drilldown(graph, refs, node_id, pmid, out_path, graph_file, summary_path)


def _gen_all_drilldowns(
    graph: dict, refs: dict, node_id: str, out_dir: Path, graph_file: Path
) -> None:
    """Generate drill-downs for all papers cited in the node's edges."""
    node_edges = [e for e in graph.get("edges", []) if e.get("type_a") == node_id]
    seen_pmids: set = set()
    for edge in node_edges:
        for ev in edge.get("evidence", []):
            ref = ev.get("reference", "")
            if ref and ev.get("evidence_type") == "LITERATURE":
                _, bare = _ref_identifier(ref)
                if bare not in seen_pmids:
                    seen_pmids.add(bare)
                    _gen_single_drilldown(graph, refs, node_id, ref, out_dir, graph_file)


if __name__ == "__main__":
    main()
