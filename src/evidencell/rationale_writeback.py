"""Parse Phase 3 verdict blocks from a generated report and write the
holistic verdict back to the corresponding ``MappingEdge`` YAML.

The Phase 3 ``gen-report`` orchestrator runs the synthesis subagent to
produce a Markdown report. At the end of the report (after References),
the synthesis subagent emits one fenced YAML ``verdict:`` block per
covered edge, each wrapped by HTML comment delimiters:

    <!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_SUPT_0216 -->
    ```yaml
    verdict:
      confidence: MODERATE
      confidence_score: 0.65
      rationale: >
        Reln (F1=0.95 in at_run_..._winterer_olm_..._mmc_wmbv1)
        and Chrna2 (marker_Chrna2 CONSISTENT, immunohistochemistry +
        scRNA-seq) anchor the close-match; region_fraction = 0.31
        is borderline (caveat).
      reconciliation_note: >
        ...
      lit_to_lit_edges:
        - lit_a: sst_olm_cell_ca1
          lit_b: htr3a_olm_cell_ca1
          mapping_justification: semapv:CompositeMatching
      unresolved_questions:
        - "Consider unifying ..."
    ```
    <!-- verdict-block-end -->

This module:

1. Parses verdict blocks from the report Markdown.
2. Verifies the rationale prose's quantitative claims against the
   edge's structured data — F1 values, taxonomy accessions, marker
   counts, ``run_ref`` citations, evidence modality citations
   (Q5 anti-hallucination check; the Phase 3 prompt requires
   modality-aware citations only).
3. Writes the verdict + computed ``rationale_source_hash`` +
   ``rationale_generated_at`` + ``report_path`` back to the matching
   ``MappingEdge`` in the KB graph YAML, using ruamel round-trip to
   minimise formatting churn.
4. Optionally creates lit-to-lit ``skos:closeMatch`` edges per
   ``lit_to_lit_edges`` entries when the synthesis agent calls
   cross-panel indistinguishability.

CLI::

    python -m evidencell.rationale_writeback \
        REPORT_FILE GRAPH_FILE [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

from . import _rationale_hash


# YAML 1.1's sexagesimal interpretation would parse `1:1` (and `n:1`)
# as integers (61 and so on). The Phase 2 KB only uses `1:n` for
# existing splits, which contains a non-digit so the quirk doesn't
# trigger. When the report-time agent creates a new lit-to-lit
# edge with cardinality `1:1`, we force-quote it via this helper
# so downstream readers (yaml.safe_load) see the intended string.
def _safe_cardinality(value: str) -> DoubleQuotedScalarString:
    return DoubleQuotedScalarString(value)


_VERDICT_START_RE = re.compile(
    r"<!--\s*verdict-block-start:\s*(?P<edge_id>[A-Za-z0-9_\-]+)\s*-->"
)
_VERDICT_END = "<!-- verdict-block-end -->"
_SOURCE_GROUPS_START_RE = re.compile(
    r"<!--\s*source-groups-rationale-start:\s*(?P<edge_id>[A-Za-z0-9_\-]+)\s*-->"
)
_SOURCE_GROUPS_END = "<!-- source-groups-rationale-end -->"
_YAML_FENCE_START = "```yaml"
_YAML_FENCE_END = "```"


# ─── Schema enums (mirrored from schema/celltype_mapping.yaml) ──────────────
#
# Kept in sync with the schema by code-review. The writer validates enum
# values before any YAML edit; a violation fails the edge's write-back
# atomically rather than letting an invalid value through to the
# pre-edit hook.

_MAPPING_RELATIONSHIP_VALUES = frozenset({
    "skos:exactMatch",
    "skos:closeMatch",
    "skos:broadMatch",
    "skos:narrowMatch",
    "evidencell:PartialOverlapMatch",  # deprecated but still permitted
    "evidencell:CrossCuttingMatch",
    "evidencell:NoCorrespondence",
    "evidencell:UncertainRelationship",
})

_MAPPING_CARDINALITY_VALUES = frozenset({"1:1", "1:n", "n:1"})

_MAPPING_JUSTIFICATION_VALUES = frozenset({
    "semapv:ManualMappingCuration",
    "semapv:UnreviewedManualMapping",
    "semapv:LexicalMatching",
    "semapv:CompositeMatching",
    "semapv:LogicalReasoning",
    "semapv:UnspecifiedMatching",
})

_CAVEAT_TYPE_VALUES = frozenset({
    "MERFISH_REGISTRATION_UNCERTAINTY",
    "LOW_CELL_COUNT",
    "DISTRIBUTED_ACROSS_CLUSTERS",
    "TAXONOMY_LEVEL_MISMATCH",
    "MARKER_NOT_SPECIFIC",
    "CROSS_SPECIES_EXTRAPOLATION",
    "SINGLE_DATASET",
    "NT_PREDICTION_UNCERTAIN",
    "PRIOR_MAPPING_ASSUMED",
    "AMBIGUOUS_MAPPING",
    "SINGLE_STUDY",
    "NO_DISCRIMINATING_MARKER",
    "DISCORDANT_ANATOMY",
    "ELECTROPHYSIOLOGY_ONLY_DEFINITION",
    "OTHER",
})

_MAPPING_CONFIDENCE_VALUES = frozenset({
    "HIGH", "MODERATE", "LOW", "UNCERTAIN", "REFUTED",
})


# ─── Parsing ────────────────────────────────────────────────────────────────


def parse_verdict_blocks(report_text: str) -> list[dict[str, Any]]:
    """Extract verdict blocks from a report's Markdown text.

    Returns a list of dicts with keys ``edge_id`` and ``verdict``
    (the parsed YAML body). Malformed blocks are skipped silently —
    caller should compare returned count against expected.
    """
    out: list[dict[str, Any]] = []
    pos = 0
    while True:
        m = _VERDICT_START_RE.search(report_text, pos)
        if m is None:
            break
        edge_id = m.group("edge_id")
        end_idx = report_text.find(_VERDICT_END, m.end())
        if end_idx == -1:
            break
        block_inner = report_text[m.end():end_idx]
        # Find the fenced YAML block inside.
        fence_start = block_inner.find(_YAML_FENCE_START)
        if fence_start == -1:
            pos = end_idx + len(_VERDICT_END)
            continue
        yaml_start = block_inner.find("\n", fence_start) + 1
        fence_end = block_inner.find(_YAML_FENCE_END, yaml_start)
        if fence_end == -1:
            pos = end_idx + len(_VERDICT_END)
            continue
        yaml_body = block_inner[yaml_start:fence_end]
        try:
            parsed = yaml.safe_load(yaml_body) or {}
        except Exception:
            pos = end_idx + len(_VERDICT_END)
            continue
        verdict = parsed.get("verdict")
        if isinstance(verdict, dict):
            out.append({"edge_id": edge_id, "verdict": verdict})
        pos = end_idx + len(_VERDICT_END)
    return out


def parse_source_groups_rationale_blocks(
    report_text: str,
) -> list[dict[str, Any]]:
    """Extract ``source-groups-rationale`` blocks from the report.

    Each block is wrapped in HTML-comment delimiters identifying the
    edge id, with a fenced YAML body shaped like::

        source_groups_rationale:
          - run_ref: at_run_...        # optional; disambiguates when
                                        # multiple AT evidence items
                                        # exist on the edge
            source_group_label: ...    # required; matches
                                        # SourceGroup.label
            rationale: >
              ...prose...

    Returns a list of dicts with ``edge_id`` and ``entries`` (list of
    per-source-group dicts). Malformed blocks are skipped silently.
    """
    out: list[dict[str, Any]] = []
    pos = 0
    while True:
        m = _SOURCE_GROUPS_START_RE.search(report_text, pos)
        if m is None:
            break
        edge_id = m.group("edge_id")
        end_idx = report_text.find(_SOURCE_GROUPS_END, m.end())
        if end_idx == -1:
            break
        block_inner = report_text[m.end():end_idx]
        fence_start = block_inner.find(_YAML_FENCE_START)
        if fence_start == -1:
            pos = end_idx + len(_SOURCE_GROUPS_END)
            continue
        yaml_start = block_inner.find("\n", fence_start) + 1
        fence_end = block_inner.find(_YAML_FENCE_END, yaml_start)
        if fence_end == -1:
            pos = end_idx + len(_SOURCE_GROUPS_END)
            continue
        yaml_body = block_inner[yaml_start:fence_end]
        try:
            parsed = yaml.safe_load(yaml_body) or {}
        except Exception:
            pos = end_idx + len(_SOURCE_GROUPS_END)
            continue
        entries = parsed.get("source_groups_rationale")
        if isinstance(entries, list):
            out.append({"edge_id": edge_id, "entries": entries})
        pos = end_idx + len(_SOURCE_GROUPS_END)
    return out


def validate_verdict_enums(verdict: dict[str, Any]) -> list[str]:
    """Check that any controlled-vocabulary fields on a verdict block
    carry schema-permitted values. Returns a list of human-readable
    error strings; empty list = all enum claims valid.

    Validated fields:
    - ``confidence`` (MappingConfidence enum)
    - ``relationship`` (MappingRelationship enum)
    - ``mapping_cardinality`` (MappingCardinality enum)
    - ``mapping_justification`` (MappingJustification enum)
    - ``caveats[*].caveat_type`` (CaveatType enum)
    """
    errors: list[str] = []
    conf = verdict.get("confidence")
    if conf is not None and conf not in _MAPPING_CONFIDENCE_VALUES:
        errors.append(
            f"confidence={conf!r} is not a valid MappingConfidence value. "
            f"Expected one of: {sorted(_MAPPING_CONFIDENCE_VALUES)}."
        )
    rel = verdict.get("relationship")
    if rel is not None and rel not in _MAPPING_RELATIONSHIP_VALUES:
        errors.append(
            f"relationship={rel!r} is not a valid MappingRelationship "
            f"value. Expected one of: "
            f"{sorted(_MAPPING_RELATIONSHIP_VALUES)}."
        )
    card = verdict.get("mapping_cardinality")
    if card is not None and str(card) not in _MAPPING_CARDINALITY_VALUES:
        errors.append(
            f"mapping_cardinality={card!r} is not a valid value. "
            f"Expected one of: {sorted(_MAPPING_CARDINALITY_VALUES)}."
        )
    just = verdict.get("mapping_justification")
    if just is not None and just not in _MAPPING_JUSTIFICATION_VALUES:
        errors.append(
            f"mapping_justification={just!r} is not a valid value. "
            f"Expected one of: {sorted(_MAPPING_JUSTIFICATION_VALUES)}."
        )
    for i, cav in enumerate(verdict.get("caveats") or []):
        if not isinstance(cav, dict):
            errors.append(
                f"caveats[{i}] is not a mapping; expected an object with "
                f"caveat_type + description."
            )
            continue
        ct = cav.get("caveat_type")
        if ct is None:
            errors.append(
                f"caveats[{i}] missing required field caveat_type."
            )
        elif ct not in _CAVEAT_TYPE_VALUES:
            errors.append(
                f"caveats[{i}].caveat_type={ct!r} is not a valid CaveatType "
                f"value. Expected one of: {sorted(_CAVEAT_TYPE_VALUES)}."
            )
        if not cav.get("description"):
            errors.append(
                f"caveats[{i}] missing required field description."
            )
    return errors


# ─── Anti-hallucination check (Q5) ──────────────────────────────────────────


# Patterns we extract from rationale prose and verify against structured
# data. Each pattern returns a list of (claim_text, structured_lookup_key).
_F1_PATTERN = re.compile(r"F1\s*=\s*(?P<value>0?\.\d+)")
_ACCESSION_PATTERN = re.compile(r"\bCS\w+_(?:CLUS|SUPT|SUBC|CLAS)_\d+\b")
_RUN_REF_PATTERN = re.compile(r"\bat_run_[A-Za-z0-9_]+\b")
_MARKER_COUNT_PATTERN = re.compile(
    r"\b(?P<m>\d+)\s+of\s+(?P<n>\d+)\s+markers?\s+CONSISTENT\b",
    re.IGNORECASE,
)

# Modality alias map: rationale-side token → set of variants any one
# of which counts as a match in the methods blob. Lets the agent
# paraphrase ("Cre-line" for "Cre transgenic line") without tripping
# the check.
_MODALITY_ALIASES: dict[str, tuple[str, ...]] = {
    "patch-seq":            ("patch-seq", "patch seq", "patch clamp"),
    "patch seq":            ("patch-seq", "patch seq", "patch clamp"),
    "scrna-seq":            ("scrna-seq", "scrna seq", "single-cell rna", "rna-seq"),
    "scrna seq":            ("scrna-seq", "scrna seq", "single-cell rna", "rna-seq"),
    "single-cell rna":      ("scrna-seq", "scrna seq", "single-cell rna", "rna-seq"),
    "bulk rna":             ("bulk rna", "bulk-rna"),
    "in situ hybridization": ("in situ hybridization", "ish",),
    "immunohistochemistry": ("immunohistochemistry", "ihc"),
    "ihc":                  ("immunohistochemistry", "ihc"),
    "biocytin":             ("biocytin",),
    "electrophysiology":    ("electrophysiology", "patch clamp", "whole-cell"),
    "morphology":           ("morphology", "morphological", "biocytin"),
    "morphological":        ("morphology", "morphological", "biocytin"),
    "cre-line":             ("cre-line", "cre line", "cre transgenic", "cre driver", "intersectional genetics", "intersectional cre", "flp transgenic"),
    "cre line":             ("cre-line", "cre line", "cre transgenic", "cre driver", "intersectional genetics", "intersectional cre", "flp transgenic"),
    "optogenetics":         ("optogenetics", "optogenetic"),
    "mapmycells":           ("mapmycells", "cell_type_mapper"),
    # NOTE: MERFISH / smFISH / FISH not included as modality-check
    # tokens. Spatial transcriptomics methods are implicit in atlas
    # anat panels (WMBv1 anat is MERFISH-derived in all current
    # taxonomies) but rarely appear as literal `method:` strings on
    # edge evidence items — the linkage is structural, via the
    # taxonomy_meta and cluster.yaml. Requiring a literal MERFISH
    # mention to validate a rationale's "MERFISH soma" citation would
    # be too strict for the value it adds.
}

# MapMyCells operates on scRNA-seq input by definition. When an AT
# evidence item's method string contains "MapMyCells" or "cell_type_mapper",
# we treat that as a scRNA-seq modality citation by implication, so the
# rationale's "scRNA-seq" / "single-cell RNA" / "rna-seq" claims pass.
_MAPMYCELLS_IMPLIES_SCRNA = ("mapmycells", "cell_type_mapper")
_SCRNA_TOKENS = ("scrna-seq", "scrna seq", "single-cell rna", "rna-seq")


def _edge_accessions(edge: dict) -> set[str]:
    """Collect all taxonomy accessions referenced anywhere on an edge."""
    out: set[str] = set()
    tt = edge.get("taxonomy_type")
    if tt:
        out.update(_ACCESSION_PATTERN.findall(tt))
    for pc in edge.get("property_comparisons") or []:
        if not isinstance(pc, dict):
            continue
        for v in (pc.get("node_b_value"), pc.get("node_a_value")):
            if isinstance(v, str):
                out.update(_ACCESSION_PATTERN.findall(v))
    for ev in edge.get("evidence") or []:
        if not isinstance(ev, dict):
            continue
        for m in ev.get("metrics_by_level") or []:
            if isinstance(m, dict):
                acc = m.get("best_target_accession")
                if isinstance(acc, str):
                    out.update(_ACCESSION_PATTERN.findall(acc))
    return out


def _edge_f1_values(edge: dict) -> set[str]:
    """Collect all F1 values appearing in AT evidence, rounded to 2dp
    and formatted as `0.NN` strings for comparison."""
    out: set[str] = set()
    for ev in edge.get("evidence") or []:
        if not isinstance(ev, dict):
            continue
        if ev.get("evidence_type") != "ANNOTATION_TRANSFER":
            continue
        for m in ev.get("metrics_by_level") or []:
            if not isinstance(m, dict):
                continue
            f1 = m.get("f1_score")
            try:
                out.add(f"{float(f1):.2f}".lstrip("0") or "0.00")
                # Also include the leading-zero form for tolerance.
                out.add(f"{float(f1):.2f}")
            except (TypeError, ValueError):
                continue
    return out


def _edge_run_refs(edge: dict) -> set[str]:
    out: set[str] = set()
    for ev in edge.get("evidence") or []:
        if isinstance(ev, dict):
            run_ref = ev.get("run_ref")
            if isinstance(run_ref, str):
                out.add(run_ref)
    return out


def _edge_consistent_marker_count(edge: dict) -> tuple[int, int]:
    """Return (n_consistent, n_total_marker_family_PCs).

    "Marker" is interpreted in the biological sense: any
    PropertyComparison whose ``property`` starts with one of the
    marker-family prefixes (``marker_``, ``neuropeptide_``, ``tf_``,
    ``np_``, ``negative_marker_``). Agents talk about "N of M markers
    CONSISTENT" colloquially across this whole family; schema-level
    separation between marker subtypes is not the granularity the
    rationale lives at.
    """
    n_total = 0
    n_consistent = 0
    marker_family = (
        "marker_",
        "neuropeptide_",
        "tf_",
        "np_",
        "negative_marker_",
    )
    for pc in edge.get("property_comparisons") or []:
        if not isinstance(pc, dict):
            continue
        prop = (pc.get("property") or "").lower()
        if not any(prop.startswith(pfx) for pfx in marker_family):
            continue
        n_total += 1
        if (pc.get("alignment") or "").upper() == "CONSISTENT":
            n_consistent += 1
    return n_consistent, n_total


def _edge_method_text(
    edge: dict,
    lit_node: dict | None = None,
    taxonomy_node: dict | None = None,
) -> str:
    """Concatenate all method / evidence_type strings on an edge and
    its endpoint nodes for modality-citation checking.

    Edge-level sources: evidence items' `method`, `evidence_type`,
    `source_cluster_label`, `source_dataset_accession`; property
    comparisons' source methods.

    Endpoint-node sources (added 2026-05-13): the lit_node's and
    taxonomy_node's PropertySources on every property panel
    (defining_markers, nt_type, anatomical_location, electrophysiology,
    morphology, definition_references). The rationale legitimately
    cites modalities used to characterise either endpoint — e.g. a
    Chrna2-Cre line used to label OLM cells is a Cre-line modality,
    even if the AT evidence's method string is just "MapMyCells".
    """
    parts: list[str] = []
    for ev in edge.get("evidence") or []:
        if not isinstance(ev, dict):
            continue
        for k in (
            "method",
            "evidence_type",
            "source_cluster_label",
            "source_dataset_accession",
            "tool_version",
        ):
            v = ev.get(k)
            if isinstance(v, str):
                parts.append(v.lower())
    for pc in edge.get("property_comparisons") or []:
        if not isinstance(pc, dict):
            continue
        for src in pc.get("sources") or []:
            if isinstance(src, dict):
                v = src.get("method")
                if isinstance(v, str):
                    parts.append(v.lower())
    parts.extend(_collect_node_methods(lit_node))
    parts.extend(_collect_node_methods(taxonomy_node))
    return " | ".join(parts)


def _collect_node_methods(node: dict | None) -> list[str]:
    """Walk a CellTypeNode's property panels and return all `method`
    strings on PropertySource entries. Lower-cased."""
    if not isinstance(node, dict):
        return []
    out: list[str] = []
    # Top-level sources lists on profiles + anatomical_location.
    for panel_key in (
        "nt_type",
        "electrophysiology",
        "morphology",
    ):
        panel = node.get(panel_key)
        if isinstance(panel, dict):
            for src in panel.get("sources") or []:
                if isinstance(src, dict) and isinstance(src.get("method"), str):
                    out.append(src["method"].lower())
    for loc in node.get("anatomical_location") or []:
        if not isinstance(loc, dict):
            continue
        for src in loc.get("sources") or []:
            if isinstance(src, dict) and isinstance(src.get("method"), str):
                out.append(src["method"].lower())
    # Defining markers + neuropeptides + tf_markers + np_markers (lists
    # of GeneDescriptors, each with `sources`).
    for marker_panel in (
        "defining_markers",
        "neuropeptides",
        "tf_markers",
        "np_markers",
        "merfish_markers",
        "negative_markers",
    ):
        for marker in node.get(marker_panel) or []:
            if not isinstance(marker, dict):
                continue
            for src in marker.get("sources") or []:
                if isinstance(src, dict) and isinstance(src.get("method"), str):
                    out.append(src["method"].lower())
    return out


def collect_verdict_prose(verdict: dict[str, Any]) -> str:
    """Concatenate every free-text field on a verdict block whose
    quantitative claims should be checked: ``rationale``,
    ``reconciliation_note``, each ``caveats[*].description``, and each
    ``proposed_experiments[*]`` string.

    Joined with ``\\n`` so the regex patterns (F1=, accessions, etc.)
    each match within their owning sentence; the antihallucination
    check is whole-text rather than per-field, which is fine because a
    failure message naming "rationale-suite prose" remains actionable.
    """
    parts: list[str] = []
    for k in ("rationale", "reconciliation_note"):
        v = verdict.get(k)
        if isinstance(v, str) and v:
            parts.append(v)
    for cav in verdict.get("caveats") or []:
        if isinstance(cav, dict):
            d = cav.get("description")
            if isinstance(d, str) and d:
                parts.append(d)
    for exp in verdict.get("proposed_experiments") or []:
        if isinstance(exp, str) and exp:
            parts.append(exp)
    return "\n".join(parts)


def check_rationale_against_edge(
    rationale: str,
    edge: dict,
    lit_node: dict | None = None,
    taxonomy_node: dict | None = None,
    graph: dict | None = None,
) -> list[str]:
    """Verify each quantitative or methodology claim in ``rationale``
    against the edge's structured data. Returns a list of human-readable
    error strings (empty list = all claims verifiable).

    Verified claim types:

    - ``F1=0.NN`` — must match an ANNOTATION_TRANSFER
      ``metrics_by_level[*].f1_score`` rounded to 2 decimals (with
      tolerance for the leading-zero variant).
    - ``CS\\w+_(CLUS|SUPT|SUBC|CLAS)_\\d+`` accessions — must appear on
      the edge's ``taxonomy_type``, in a property_comparison value, or
      in an AT evidence item's ``metrics_by_level``.
    - ``N of M markers CONSISTENT`` — count must match the edge's
      marker_-prefixed PropertyComparisons.
    - ``at_run_…`` run_ref strings — must appear on an evidence item.
    - Modality tokens (patch-seq, scRNA-seq, ihc, morphology, ...) —
      must appear in some evidence item's ``method`` /
      ``evidence_type`` / a PropertySource's ``method``.
    """
    if not rationale:
        return []
    errors: list[str] = []
    text = rationale.lower()

    # F1 values.
    edge_f1s = _edge_f1_values(edge)
    for m in _F1_PATTERN.finditer(rationale):
        value = m.group("value")
        # Allow both ".93" and "0.93" forms.
        if value not in edge_f1s and f"0{value}" not in edge_f1s:
            errors.append(
                f"rationale cites F1={value} but no AT "
                f"metrics_by_level entry on this edge carries that "
                f"value (rounded to 2dp). Edge F1s: "
                f"{sorted(edge_f1s) or '(none)'}."
            )

    # Accessions. Accept anything appearing on this edge OR anywhere in
    # the surrounding graph (sibling-cluster references for narrative
    # context are legitimate, e.g. "OLM cells preferentially map to
    # CS20230722_CLUS_0768 rather than CLUS_0769").
    edge_accessions = _edge_accessions(edge)
    graph_accessions: set[str] = set()
    if graph is not None:
        for n in graph.get("nodes") or []:
            if isinstance(n, dict):
                acc = n.get("cell_set_accession") or n.get("id")
                if isinstance(acc, str):
                    graph_accessions.update(_ACCESSION_PATTERN.findall(acc))
        for e in graph.get("edges") or []:
            if isinstance(e, dict):
                for ee in (e,):
                    graph_accessions.update(_edge_accessions(ee))
    known_accessions = edge_accessions | graph_accessions
    for acc in set(_ACCESSION_PATTERN.findall(rationale)):
        if acc not in known_accessions:
            errors.append(
                f"rationale cites accession {acc} but it appears nowhere "
                f"on this edge or in the surrounding graph "
                f"(taxonomy_type / property_comparisons / evidence "
                f"metrics_by_level / sibling nodes)."
            )

    # run_refs.
    edge_run_refs = _edge_run_refs(edge)
    for run_ref in set(_RUN_REF_PATTERN.findall(rationale)):
        if run_ref not in edge_run_refs:
            errors.append(
                f"rationale cites run_ref {run_ref} but no evidence item "
                f"on this edge carries it. Edge run_refs: "
                f"{sorted(edge_run_refs) or '(none)'}."
            )

    # Marker counts.
    for m in _MARKER_COUNT_PATTERN.finditer(rationale):
        claimed_consistent = int(m.group("m"))
        claimed_total = int(m.group("n"))
        actual_consistent, actual_total = _edge_consistent_marker_count(edge)
        if (claimed_consistent, claimed_total) != (
            actual_consistent,
            actual_total,
        ):
            errors.append(
                f"rationale claims {claimed_consistent} of {claimed_total} "
                f"markers CONSISTENT but PropertyComparisons on this edge "
                f"show {actual_consistent} of {actual_total} marker_-prefixed "
                f"CONSISTENT alignments."
            )

    # Modality tokens — when the rationale cites a modality, at least
    # one of its accepted aliases must appear in the methods blob
    # (evidence items, property-source methods, or endpoint-node
    # property sources). Aliases let "Cre-line" match the literal
    # method string "Chrna2-Cre transgenic line"; cf. _MODALITY_ALIASES.
    methods_blob = _edge_method_text(edge, lit_node, taxonomy_node)

    # Promote MapMyCells / cell_type_mapper presence to imply scRNA-seq
    # for modality-citation purposes. MapMyCells consumes scRNA-seq by
    # definition; we don't require the AT method string to literally
    # say "scRNA-seq".
    if any(t in methods_blob for t in _MAPMYCELLS_IMPLIES_SCRNA):
        methods_blob = methods_blob + " | scrna-seq | single-cell rna"

    for token, aliases in _MODALITY_ALIASES.items():
        if token not in text:
            continue
        if not any(alias in methods_blob for alias in aliases):
            errors.append(
                f"rationale cites modality '{token}' but no evidence item, "
                f"property-source method, or endpoint-node source method "
                f"on this edge mentions any of: {sorted(set(aliases))}. "
                f"This may be a hallucinated modality claim."
            )

    return errors


def check_rationale_against_edge_structured(
    rationale: str,
    edge: dict,
    lit_node: dict | None = None,
    taxonomy_node: dict | None = None,
    graph: dict | None = None,
) -> list[dict]:
    """Structured form of :func:`check_rationale_against_edge` — same
    checks, returns ``list[dict]`` for programmatic consumption (e.g.
    feeding a focused-correction subagent in workflows/gen-report.md
    Step 4b).

    Each dict has shape::

        {
          "check": "f1_value" | "accession" | "run_ref" | "marker_count"
                   | "modality",
          "claimed": str | int | tuple,    # what the rationale said
          "expected": str | int | tuple,   # what the structured data says
          "structured_truth": {...},       # the raw edge data the
                                           # claim should match
          "message": str,                  # the human-readable string
                                           # (same as the legacy API)
        }

    Empty list = all claims verifiable.
    """
    if not rationale:
        return []
    out: list[dict] = []

    edge_f1s = _edge_f1_values(edge)
    for m in _F1_PATTERN.finditer(rationale):
        value = m.group("value")
        if value not in edge_f1s and f"0{value}" not in edge_f1s:
            out.append({
                "check": "f1_value",
                "claimed": value,
                "expected": sorted(edge_f1s) if edge_f1s else None,
                "structured_truth": {"edge_f1_values": sorted(edge_f1s)},
                "message": (
                    f"rationale cites F1={value} but no AT "
                    f"metrics_by_level entry on this edge carries that "
                    f"value (rounded to 2dp). Edge F1s: "
                    f"{sorted(edge_f1s) or '(none)'}."
                ),
            })

    edge_accessions = _edge_accessions(edge)
    graph_accessions: set[str] = set()
    if graph is not None:
        for n in graph.get("nodes") or []:
            if isinstance(n, dict):
                acc = n.get("cell_set_accession") or n.get("id")
                if isinstance(acc, str):
                    graph_accessions.update(_ACCESSION_PATTERN.findall(acc))
        for e in graph.get("edges") or []:
            if isinstance(e, dict):
                graph_accessions.update(_edge_accessions(e))
    known_accessions = edge_accessions | graph_accessions
    for acc in set(_ACCESSION_PATTERN.findall(rationale)):
        if acc not in known_accessions:
            out.append({
                "check": "accession",
                "claimed": acc,
                "expected": None,
                "structured_truth": {
                    "edge_accessions": sorted(edge_accessions),
                    "graph_accessions_sample": sorted(graph_accessions)[:10],
                },
                "message": (
                    f"rationale cites accession {acc} but it appears "
                    f"nowhere on this edge or in the surrounding graph."
                ),
            })

    edge_run_refs = _edge_run_refs(edge)
    for run_ref in set(_RUN_REF_PATTERN.findall(rationale)):
        if run_ref not in edge_run_refs:
            out.append({
                "check": "run_ref",
                "claimed": run_ref,
                "expected": sorted(edge_run_refs) if edge_run_refs else None,
                "structured_truth": {"edge_run_refs": sorted(edge_run_refs)},
                "message": (
                    f"rationale cites run_ref {run_ref} but no evidence "
                    f"item on this edge carries it. Edge run_refs: "
                    f"{sorted(edge_run_refs) or '(none)'}."
                ),
            })

    for m in _MARKER_COUNT_PATTERN.finditer(rationale):
        claimed_consistent = int(m.group("m"))
        claimed_total = int(m.group("n"))
        actual_consistent, actual_total = _edge_consistent_marker_count(edge)
        if (claimed_consistent, claimed_total) != (
            actual_consistent,
            actual_total,
        ):
            out.append({
                "check": "marker_count",
                "claimed": f"{claimed_consistent} of {claimed_total}",
                "expected": f"{actual_consistent} of {actual_total}",
                "structured_truth": {
                    "marker_prefixed_total": actual_total,
                    "marker_prefixed_consistent": actual_consistent,
                },
                "message": (
                    f"rationale claims {claimed_consistent} of "
                    f"{claimed_total} markers CONSISTENT but "
                    f"PropertyComparisons on this edge show "
                    f"{actual_consistent} of {actual_total} marker_-"
                    f"prefixed CONSISTENT alignments."
                ),
            })

    methods_blob = _edge_method_text(edge, lit_node, taxonomy_node)
    if any(t in methods_blob for t in _MAPMYCELLS_IMPLIES_SCRNA):
        methods_blob = methods_blob + " | scrna-seq | single-cell rna"
    text = rationale.lower()
    for token, aliases in _MODALITY_ALIASES.items():
        if token not in text:
            continue
        if not any(alias in methods_blob for alias in aliases):
            out.append({
                "check": "modality",
                "claimed": token,
                "expected": None,
                "structured_truth": {
                    "accepted_aliases": sorted(set(aliases)),
                    "methods_blob_excerpt": methods_blob[:200],
                },
                "message": (
                    f"rationale cites modality '{token}' but no evidence "
                    f"item, property-source method, or endpoint-node "
                    f"source method on this edge mentions any of: "
                    f"{sorted(set(aliases))}. This may be a hallucinated "
                    f"modality claim."
                ),
            })

    return out


# ─── Write-back ─────────────────────────────────────────────────────────────


def _now_iso() -> str:
    return datetime.now(tz=timezone.utc).isoformat(timespec="seconds")


def _load_yaml_rt(path: Path):
    yaml_rt = YAML(typ="rt")
    yaml_rt.preserve_quotes = True
    yaml_rt.width = 4096
    yaml_rt.indent(mapping=2, sequence=4, offset=2)
    return yaml_rt, yaml_rt.load(path)


def _dump_yaml_rt(yaml_rt, doc, path: Path) -> None:
    with path.open("w", encoding="utf-8") as fh:
        yaml_rt.dump(doc, fh)


def _find_edge(doc, edge_id: str):
    for edge in doc.get("edges") or []:
        if isinstance(edge, dict) and edge.get("id") == edge_id:
            return edge
    return None


def _find_node(doc, node_id: str):
    for node in doc.get("nodes") or []:
        if isinstance(node, dict) and node.get("id") == node_id:
            return node
    return None


def _make_lit_to_lit_edge_id(lit_a: str, lit_b: str) -> str:
    return f"edge_{lit_a}_skos_closeMatch_{lit_b}"


def write_back(
    report_path: Path,
    graph_path: Path,
    *,
    dry_run: bool = False,
    verify: bool = True,
) -> dict[str, Any]:
    """Parse ``report_path``, verify each verdict block, and write
    fields back to the matching MappingEdges in ``graph_path``.

    Returns a summary dict with keys ``parsed``, ``written``, ``errors``.
    On ``verify=True`` (default), any verification failure on any block
    blocks the entire write (atomic — partial writes are confusing).
    """
    report_text = report_path.read_text(encoding="utf-8")
    verdicts = parse_verdict_blocks(report_text)
    source_groups_blocks = parse_source_groups_rationale_blocks(report_text)

    yaml_rt, doc = _load_yaml_rt(graph_path)
    summary: dict[str, Any] = {
        "report": str(report_path),
        "graph": str(graph_path),
        "parsed": len(verdicts),
        "source_groups_blocks_parsed": len(source_groups_blocks),
        "verified": 0,
        "written": 0,
        "lit_to_lit_created": 0,
        "source_group_rationales_written": 0,
        "source_group_rationales_skipped": 0,
        "errors": [],
    }

    # First pass: verify all blocks.
    pending_writes: list[tuple[dict, dict]] = []  # (edge_node, verdict_dict)
    pending_lit_to_lit: list[dict] = []
    for vb in verdicts:
        edge_id = vb["edge_id"]
        verdict = vb["verdict"]
        edge = _find_edge(doc, edge_id)
        if edge is None:
            summary["errors"].append(
                f"verdict block names edge_id={edge_id!r} but no such "
                f"edge in {graph_path.name}."
            )
            continue

        enum_errs = validate_verdict_enums(verdict)
        if enum_errs:
            for e in enum_errs:
                summary["errors"].append(f"[{edge_id}] {e}")
            continue

        if verify:
            lit_id = edge.get("lit_type")
            tax_id = edge.get("taxonomy_type")
            errs = check_rationale_against_edge(
                collect_verdict_prose(verdict),
                edge,
                _find_node(doc, lit_id) if lit_id else None,
                _find_node(doc, tax_id) if tax_id else None,
                graph=doc,
            )
            if errs:
                for e in errs:
                    summary["errors"].append(
                        f"[{edge_id}] {e}"
                    )
                continue
        summary["verified"] += 1
        pending_writes.append((edge, verdict))
        for ll in verdict.get("lit_to_lit_edges") or []:
            if isinstance(ll, dict):
                pending_lit_to_lit.append(ll)

    if summary["errors"]:
        # Atomic: any verification error blocks the whole write.
        return summary

    # Second pass: write the verdicts.
    for edge, verdict in pending_writes:
        edge["confidence"] = verdict.get("confidence")
        if "confidence_score" in verdict:
            edge["confidence_score"] = float(verdict["confidence_score"])
        edge["rationale"] = verdict.get("rationale") or ""
        if "reconciliation_note" in verdict:
            edge["reconciliation_note"] = verdict["reconciliation_note"]
        # SSSOM trio + typed lists: write when present; leave existing
        # edge fields untouched when absent. caveats[] and
        # proposed_experiments[] are REPLACE semantics (the agent emits
        # the canonical post-synth set); unresolved_questions[] is
        # append-only below to preserve cross-run accumulation.
        if "relationship" in verdict:
            edge["relationship"] = verdict["relationship"]
        if "mapping_cardinality" in verdict:
            edge["mapping_cardinality"] = _safe_cardinality(
                str(verdict["mapping_cardinality"])
            )
        if "mapping_justification" in verdict:
            edge["mapping_justification"] = verdict["mapping_justification"]
        if "caveats" in verdict:
            edge["caveats"] = list(verdict["caveats"] or [])
        if "proposed_experiments" in verdict:
            edge["proposed_experiments"] = list(
                verdict["proposed_experiments"] or []
            )
        edge["rationale_generated_at"] = _now_iso()
        edge["report_path"] = str(
            report_path.relative_to(report_path.parent.parent.parent)
            if report_path.is_absolute()
            else report_path
        )
        # Append unresolved_questions, don't overwrite.
        new_qs = verdict.get("unresolved_questions") or []
        if new_qs:
            existing = edge.setdefault("unresolved_questions", [])
            for q in new_qs:
                if q not in existing:
                    existing.append(q)

        # Compute hash AFTER setting the new fields, but the hash
        # function excludes the rationale-suite from its inputs (see
        # _RATIONALE_SUITE_FIELDS in _rationale_hash). So this is safe.
        lit_id = edge.get("lit_type")
        tax_id = edge.get("taxonomy_type")
        edge["rationale_source_hash"] = _rationale_hash.compute_hash(
            edge,
            _find_node(doc, lit_id) if lit_id else None,
            _find_node(doc, tax_id) if tax_id else None,
        )
        summary["written"] += 1

    # Third pass: create lit-to-lit edges.
    seen_pairs: set[tuple[str, str]] = set()
    for ll in pending_lit_to_lit:
        lit_a = ll.get("lit_a")
        lit_b = ll.get("lit_b")
        if not (lit_a and lit_b):
            continue
        pair_key = tuple(sorted((lit_a, lit_b)))
        if pair_key in seen_pairs:
            continue
        seen_pairs.add(pair_key)
        new_edge_id = _make_lit_to_lit_edge_id(lit_a, lit_b)
        if _find_edge(doc, new_edge_id) is not None:
            continue  # already exists; don't duplicate
        justification = ll.get("mapping_justification") or "semapv:UnreviewedManualMapping"
        new_edge = {
            "id": new_edge_id,
            "lit_type": lit_a,
            "taxonomy_type": lit_b,
            "relationship": "skos:closeMatch",
            "mapping_cardinality": _safe_cardinality("1:1"),
            "mapping_justification": justification,
            "evidence": [
                {
                    "evidence_type": "ATLAS_METADATA",
                    "supports": "SUPPORT",
                    "explanation": (
                        f"Indistinguishable across the property panels "
                        f"available; cross-edge note recorded by report-time "
                        f"synthesis. See report at {summary['report']}."
                    ),
                }
            ],
        }
        edges_list = doc.get("edges")
        if edges_list is None:
            doc["edges"] = [new_edge]
        else:
            edges_list.append(new_edge)
        summary["lit_to_lit_created"] += 1

    # Fourth pass: populate source_groups[*].rationale on AT evidence
    # items per the source-groups-rationale blocks. Only fills when the
    # target rationale is currently empty (per the schema's
    # "never overwrite without curator review" rule).
    for sgb in source_groups_blocks:
        edge_id = sgb["edge_id"]
        edge = _find_edge(doc, edge_id)
        if edge is None:
            summary["errors"].append(
                f"source-groups-rationale block names edge_id={edge_id!r} "
                f"but no such edge in {graph_path.name}."
            )
            continue
        for entry in sgb["entries"]:
            if not isinstance(entry, dict):
                continue
            label = entry.get("source_group_label")
            rationale = entry.get("rationale")
            run_ref_filter = entry.get("run_ref")
            if not label or not rationale:
                summary["errors"].append(
                    f"[{edge_id}] source-groups-rationale entry missing "
                    f"source_group_label or rationale: {entry!r}"
                )
                continue
            wrote = _apply_source_group_rationale(
                edge, label, rationale, run_ref_filter
            )
            if wrote == "written":
                summary["source_group_rationales_written"] += 1
            elif wrote == "skipped_existing":
                summary["source_group_rationales_skipped"] += 1
            else:
                summary["errors"].append(
                    f"[{edge_id}] no source_groups entry with "
                    f"label={label!r}"
                    + (f" and run_ref={run_ref_filter!r}"
                       if run_ref_filter else "")
                    + " found on any AT evidence item."
                )

    if summary["errors"] and not dry_run:
        # Source-groups errors are non-fatal for the verdict writes
        # already queued; report them but only block the actual file
        # write when something is wrong.
        # (Verdict errors already returned above; reaching here means
        # the failures are source-groups-only.)
        pass

    if not dry_run and (
        summary["written"]
        or summary["lit_to_lit_created"]
        or summary["source_group_rationales_written"]
    ):
        _dump_yaml_rt(yaml_rt, doc, graph_path)

    return summary


def _apply_source_group_rationale(
    edge: dict,
    label: str,
    rationale: str,
    run_ref_filter: str | None,
) -> str:
    """Locate the source_groups entry on an AT evidence item of this
    edge and populate its ``rationale`` if currently empty.

    Returns one of:
    - ``"written"`` — populated an empty rationale
    - ``"skipped_existing"`` — entry already has a rationale; left alone
    - ``"not_found"`` — no matching evidence item / source_group

    When ``run_ref_filter`` is provided, only evidence items with that
    ``run_ref`` are considered (disambiguates between multiple AT
    evidence items on the same edge). When None, the first AT evidence
    item carrying a matching source_groups entry wins.
    """
    for ev in edge.get("evidence") or []:
        if not isinstance(ev, dict):
            continue
        if ev.get("evidence_type") != "ANNOTATION_TRANSFER":
            continue
        if run_ref_filter and ev.get("run_ref") != run_ref_filter:
            continue
        for sg in ev.get("source_groups") or []:
            if not isinstance(sg, dict):
                continue
            if sg.get("label") != label:
                continue
            if sg.get("rationale"):
                return "skipped_existing"
            sg["rationale"] = rationale
            return "written"
    return "not_found"


# ─── CLI ────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m evidencell.rationale_writeback",
        description=(
            "Parse verdict blocks from a gen-report Markdown report and "
            "write the verdict + currency hash back to the matching "
            "MappingEdges. Phase 3 of the map_cell_type refactor."
        ),
    )
    parser.add_argument("report_file", type=Path)
    parser.add_argument("graph_file", type=Path)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse, verify, and report what would be written; do not edit.",
    )
    parser.add_argument(
        "--skip-verify",
        action="store_true",
        help=(
            "Skip the anti-hallucination check (NOT recommended; bypasses "
            "Q5 quality gate)."
        ),
    )
    parser.add_argument(
        "--correction-mode",
        action="store_true",
        help=(
            "Emit a structured JSON failure report instead of the default "
            "summary, suitable as input to a focused-correction subagent "
            "in workflows/gen-report.md Step 4b. Forces --dry-run "
            "(never writes). Exit code 0 (success — payload is the "
            "machine-readable failure list); read stdout."
        ),
    )
    args = parser.parse_args(argv)
    import json as _json

    if args.correction_mode:
        # Structured failure report. Re-parse the report's verdict
        # blocks, find each edge, run the structured check, and emit
        # a JSON payload that a correction subagent can read directly.
        report_text = args.report_file.read_text(encoding="utf-8")
        verdicts = parse_verdict_blocks(report_text)
        _yaml_rt, doc = _load_yaml_rt(args.graph_file)

        per_edge: list[dict] = []
        for vb in verdicts:
            edge_id = vb["edge_id"]
            verdict = vb["verdict"]
            edge = _find_edge(doc, edge_id)
            if edge is None:
                per_edge.append({
                    "edge_id": edge_id,
                    "status": "missing_edge",
                    "rationale_excerpt": None,
                    "errors": [{
                        "check": "edge_lookup",
                        "claimed": edge_id,
                        "expected": None,
                        "message": (
                            f"verdict block names edge_id={edge_id!r} "
                            f"but no such edge in {args.graph_file.name}."
                        ),
                    }],
                })
                continue
            lit_id = edge.get("lit_type")
            tax_id = edge.get("taxonomy_type")
            errs = check_rationale_against_edge_structured(
                verdict.get("rationale") or "",
                edge,
                _find_node(doc, lit_id) if lit_id else None,
                _find_node(doc, tax_id) if tax_id else None,
                graph=doc,
            )
            per_edge.append({
                "edge_id": edge_id,
                "status": "verified" if not errs else "failed",
                "rationale_excerpt": (verdict.get("rationale") or "")[:400],
                "errors": errs,
            })

        payload = {
            "report": str(args.report_file),
            "graph": str(args.graph_file),
            "verdict_blocks_parsed": len(verdicts),
            "verdict_blocks_verified": sum(
                1 for r in per_edge if r["status"] == "verified"
            ),
            "verdict_blocks_failed": sum(
                1 for r in per_edge if r["status"] == "failed"
            ),
            "per_edge": per_edge,
        }
        _json.dump(payload, sys.stdout, indent=2, default=str)
        sys.stdout.write("\n")
        return 0

    summary = write_back(
        args.report_file,
        args.graph_file,
        dry_run=args.dry_run,
        verify=not args.skip_verify,
    )
    _json.dump(summary, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0 if not summary["errors"] else 2


if __name__ == "__main__":
    sys.exit(main())
