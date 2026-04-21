"""Taxonomy reference DB: ingest WMB-format taxonomy JSON → YAML + SQLite.

Data flow:
  JSON source → ingest_to_yaml() → kb/taxonomy/{id}/*.yaml  (canonical, versioned)
                                 → TaxonomyDB.build_from_yaml() → {id}.db  (query index)
  MBA OBO JSON → TaxonomyDB.build_anat_closure() → anat_terms/hierarchy/closure tables

The SQLite DB is always derived from the YAML files and can be rebuilt without
the original JSON source.  The anat closure tables require a separate MBA ontology
JSON fetch (see justfile: fetch-mba-ontology).
"""

from __future__ import annotations

import io
import json
import sqlite3
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Iterator

import ijson
import yaml

# Always-latest release of the BICAN Mouse Brain Atlas Ontology (OBO JSON / Obograph)
MBA_ONTOLOGY_URL = (
    "https://github.com/brain-bican/mouse_brain_atlas_ontology"
    "/releases/latest/download/mbao-full.json"
)


# ── Taxonomy metadata ──────────────────────────────────────────────────────────

@dataclass
class MapMyCellsMeta:
    """MapMyCells file references for a taxonomy."""
    at_taxonomy_id: str | None = None
    stats_s3_url: str | None = None
    markers_s3_url: str | None = None
    local_stats_path: str | None = None
    local_markers_path: str | None = None


@dataclass
class TaxonomyMeta:
    """Rich metadata for an ingested taxonomy."""
    taxonomy_id: str
    taxonomy_name: str | None = None
    species_id: str | None = None        # NCBITaxon CURIE e.g. NCBITaxon:10090
    species_label: str | None = None     # e.g. "Mus musculus"
    tissue_id: str | None = None         # UBERON CURIE e.g. UBERON:0000955
    tissue_label: str | None = None      # e.g. "brain"
    anatomy_ontology: str | None = None  # ontology used for anat[] IDs e.g. "MBA"
    source_query: str | None = None      # .cypher file path for KG-backed taxonomies
    source_file: str | None = None       # JSON/CSV/XLSX path for ad hoc taxonomies
    ingest_date: str | None = None
    level_counts: dict[str, int] = field(default_factory=dict)
    mapmycells: MapMyCellsMeta = field(default_factory=MapMyCellsMeta)


def _read_meta_input(taxonomy_id: str) -> dict[str, Any]:
    """Read optional metadata input from inputs/taxonomies/{taxonomy_id}_meta.yaml.

    Returns empty dict if file is absent or unparseable — callers treat missing
    fields as null and emit a warning.
    """
    try:
        from evidencell.paths import taxonomy_meta_input_path
        p = taxonomy_meta_input_path(taxonomy_id)
        if not p.exists():
            return {}
        with p.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def read_taxonomy_meta(taxonomy_id: str) -> TaxonomyMeta:
    """Read taxonomy_meta.yaml for a taxonomy and return a TaxonomyMeta object."""
    from evidencell.paths import taxonomy_meta_path
    p = taxonomy_meta_path(taxonomy_id)
    if not p.exists():
        raise FileNotFoundError(
            f"taxonomy_meta.yaml not found at {p}. "
            f"Run: just ingest-taxonomy-yaml <source> {taxonomy_id}"
        )
    with p.open(encoding="utf-8") as fh:
        d = yaml.safe_load(fh) or {}
    mmc_raw = d.get("mapmycells") or {}
    return TaxonomyMeta(
        taxonomy_id=d.get("taxonomy_id", taxonomy_id),
        taxonomy_name=d.get("taxonomy_name"),
        species_id=d.get("species_id"),
        species_label=d.get("species_label"),
        tissue_id=d.get("tissue_id"),
        tissue_label=d.get("tissue_label"),
        anatomy_ontology=d.get("anatomy_ontology"),
        source_query=d.get("source_query"),
        source_file=d.get("source_file"),
        ingest_date=d.get("ingest_date"),
        level_counts=d.get("level_counts", {}),
        mapmycells=MapMyCellsMeta(
            at_taxonomy_id=mmc_raw.get("at_taxonomy_id"),
            stats_s3_url=mmc_raw.get("stats_s3_url"),
            markers_s3_url=mmc_raw.get("markers_s3_url"),
            local_stats_path=mmc_raw.get("local_stats_path"),
            local_markers_path=mmc_raw.get("local_markers_path"),
        ),
    )


def _meta_to_dict(meta: TaxonomyMeta) -> dict[str, Any]:
    """Serialise TaxonomyMeta to a YAML-friendly dict."""
    mmc = meta.mapmycells
    mmc_dict: dict[str, Any] = {}
    for k in ("at_taxonomy_id", "stats_s3_url", "markers_s3_url",
               "local_stats_path", "local_markers_path"):
        v = getattr(mmc, k)
        if v is not None:
            mmc_dict[k] = v
    d: dict[str, Any] = {"taxonomy_id": meta.taxonomy_id}
    for k in ("taxonomy_name", "species_id", "species_label", "tissue_id",
               "tissue_label", "anatomy_ontology", "source_query", "source_file",
               "ingest_date"):
        v = getattr(meta, k)
        if v is not None:
            d[k] = v
    if meta.level_counts:
        d["level_counts"] = meta.level_counts
    if mmc_dict:
        d["mapmycells"] = mmc_dict
    return d


# ── JSON cleaning ──────────────────────────────────────────────────────────────

def clean_taxonomy_json(path: Path) -> bytes:
    """Return cleaned bytes ready for ijson streaming.

    Fixes three encoding issues found in wmbv1_full.json:
    1. UTF-8 BOM at start of file
    2. Literal \\n / \\r bytes inside JSON string values (invalid JSON)
    3. Double-escaped quotes \\\\" inside prose (should be \\")
    """
    with path.open("rb") as fh:
        raw = fh.read()

    # Strip BOM
    if raw[:3] == b"\xef\xbb\xbf":
        raw = raw[3:]

    # Fix literal newlines/carriage-returns inside strings (byte-level state machine)
    out = bytearray()
    in_string = False
    escape_next = False
    for b in raw:
        if escape_next:
            out.append(b)
            escape_next = False
        elif b == ord("\\") and in_string:
            out.append(b)
            escape_next = True
        elif b == ord('"'):
            out.append(b)
            in_string = not in_string
        elif in_string and b == 0x0A:  # literal \n in string
            out.extend(b"\\n")
        elif in_string and b == 0x0D:  # literal \r in string
            out.extend(b"\\r")
        else:
            out.append(b)

    cleaned = bytes(out)

    # Fix double-escaped quotes inside prose (\\" → \")
    cleaned = cleaned.replace(b'\\\\"', b'\\"')

    return cleaned


def iter_taxonomy_rows(cleaned: bytes) -> Iterator[dict]:
    """Stream taxonomy rows from cleaned JSON bytes via ijson."""
    yield from ijson.items(io.BytesIO(cleaned), "item")


# ── Node extraction ────────────────────────────────────────────────────────────

@dataclass
class TaxonomyNode:
    node_id: str
    short_form: str
    label: str
    taxonomy_id: str
    taxonomy_level: str
    parent_id: str | None
    cl_id: str | None
    cl_label: str | None
    cell_ontology_term: str | None  # label string when cl object absent
    nt_type: str | None
    defining_markers_scoped: list[str] = field(default_factory=list)
    defining_markers: list[str] = field(default_factory=list)
    tf_markers: list[str] = field(default_factory=list)
    merfish_markers: list[str] = field(default_factory=list)
    np_markers: str | None = None
    neighborhood: str | None = None
    circadian_ratio: float | None = None  # Light fraction, only when skewed
    anat: list[dict] = field(default_factory=list)
    rationale: str | None = None
    rationale_dois: list[str] = field(default_factory=list)
    sex_bias: str | None = None
    # class-level extras
    neuronal: bool | None = None
    glial: bool | None = None


def _extract_level(labels: list[str], taxonomy_id: str) -> str:
    """Extract taxonomy level from wmb.labels list by stripping the taxonomy_id prefix."""
    prefix = f"{taxonomy_id}_"
    for lbl in labels:
        if lbl.startswith(prefix):
            return lbl.removeprefix(prefix)
    return "unknown"


def _scalar(val: object) -> str | None:
    """Return a scalar string from a value that may be a single-element list."""
    if val is None:
        return None
    if isinstance(val, list):
        return str(val[0]) if val else None
    return str(val)


def _split_markers(combo: str | list | None) -> list[str]:
    """Split a marker combo field into individual gene symbols.

    Source fields may be a bare comma-separated string ("Sst,Pvalb") or a
    single-element list wrapping one (["Sst,Pvalb"]).  Either way, split on
    commas and return clean gene symbol strings.
    """
    if not combo:
        return []
    if isinstance(combo, list):
        # Flatten: each element may itself be a comma-separated string
        genes: list[str] = []
        for item in combo:
            genes.extend(g.strip() for g in str(item).split(",") if g.strip())
        return genes
    return [g.strip() for g in combo.split(",") if g.strip()]


def _first_prop(props: dict, keys: list[str]) -> object:
    """Return the first non-None value found in props for any of the given keys."""
    for key in keys:
        v = props.get(key)
        if v is not None:
            return v
    return None


def _load_field_config(taxonomy_id: str) -> dict[str, list[str]]:
    """Load source→target field mappings from kb/taxonomy/{id}/field_mapping.json.

    Returns {target_field: [source_wmb_property_key, ...]} — keys to try in order,
    first non-None wins.  Falls back to an empty dict (callers use hardcoded defaults)
    if the file is absent or unparseable.
    """
    try:
        from evidencell.paths import taxonomy_dir
        cfg_path = taxonomy_dir(taxonomy_id) / "field_mapping.json"
        if not cfg_path.exists():
            return {}
        with cfg_path.open(encoding="utf-8") as fh:
            cfg = json.load(fh)
    except Exception:
        return {}

    target_to_keys: dict[str, Any] = {}

    # Top-level row_keys: maps canonical column names → actual row dict keys
    row_keys_raw = cfg.get("row_keys", {})
    if row_keys_raw:
        # Drop documentation-only keys (start with "_")
        target_to_keys["row_keys"] = {
            k: v for k, v in row_keys_raw.items()
            if not k.startswith("_") and isinstance(v, str)
        }

    # field_mappings: maps wmb.properties.* source paths → target field names
    for section in cfg.get("field_mappings", {}).values():
        for mapping in section:
            src = mapping.get("source", "")
            tgt = mapping.get("target", "")
            if not src or not tgt:
                continue
            # Only handle wmb.properties.* paths; strip list-index notation e.g. "[0]"
            if src.startswith("wmb.properties."):
                key = src.removeprefix("wmb.properties.").split("[")[0]
                existing = target_to_keys.setdefault(tgt, [])
                if isinstance(existing, list) and key not in existing:
                    existing.append(key)
    return target_to_keys


def _circadian(light: str | None) -> float | None:
    """Return Light fraction only when skewed (>0.7 or <0.3), else None."""
    if light is None:
        return None
    try:
        val = float(light)
    except (ValueError, TypeError):
        return None
    return val if (val > 0.7 or val < 0.3) else None


def _extract_node(row: dict, taxonomy_id: str, fc: dict[str, list[str]]) -> TaxonomyNode:
    """Extract a TaxonomyNode from a raw VFB graph export row.

    fc — field config from _load_field_config(); maps target field name to an ordered
    list of wmb.properties keys to try.  row_keys in fc maps canonical column names
    (node, parent_curie, cl, anat) to the actual keys in the row dict, enabling
    backward compat with WMBv1 JSON (which uses 'wmb' and 'wmb_parent.curie').
    Hardcoded defaults are used as fallbacks so existing taxonomies without a
    field_mapping.json continue to work.
    """
    rk = fc.get("row_keys", {})
    wmb = row[rk.get("node", "node")]
    props = wmb.get("properties", {})
    labels = wmb.get("labels", [])
    level = _extract_level(labels, taxonomy_id)

    cl_obj = row.get(rk.get("cl", "cl"))
    cl_props = cl_obj.get("properties", {}) if cl_obj else {}

    # cell_ontology_term is a list in source; take first element
    cot_raw = props.get("cell_ontology_term")
    if isinstance(cot_raw, list):
        cot_raw = cot_raw[0] if cot_raw else None

    # rationale / rationale_dois are lists; take first element for rationale
    rat_raw = props.get("rationale")
    rationale = rat_raw[0] if isinstance(rat_raw, list) and rat_raw else rat_raw

    dois_raw = props.get("rationale_dois")
    rationale_dois = dois_raw if isinstance(dois_raw, list) else []

    # anat
    anat_entries = []
    for a in (row.get(rk.get("anat", "anat")) or []):
        entry = {
            "id": a.get("anat_id"),
            "label": a.get("anat_label"),
            "cell_count": a.get("cell_count"),
            "cell_ratio": a.get("cell_ratio"),
        }
        if isinstance(entry["cell_count"], list):
            entry["cell_count"] = entry["cell_count"][0] if entry["cell_count"] else None
        anat_entries.append(entry)

    # Neuronal / Glial booleans (class level)
    neuronal = _scalar(_first_prop(props, fc.get("neuronal", ["Neuronal"])))
    glial = _scalar(_first_prop(props, fc.get("glial", ["Glial"])))

    return TaxonomyNode(
        node_id=props.get("curie", ""),
        short_form=props.get("short_form", ""),
        label=props.get("label", ""),
        taxonomy_id=taxonomy_id,
        taxonomy_level=level,
        parent_id=row.get(rk.get("parent_curie", "parent_curie")),
        cl_id=cl_props.get("curie"),
        cl_label=cl_props.get("label"),
        cell_ontology_term=cot_raw if not cl_props.get("curie") else None,
        nt_type=_scalar(_first_prop(props, fc.get("nt_type", ["nt_type_label"]))),
        defining_markers_scoped=_split_markers(_first_prop(
            props,
            fc.get("defining_markers_scoped", [
                "cluster_markers_combo_4within_subclass4",
                "supertype_markers_combo_4within_subclass4",
            ]),
        )),
        defining_markers=_split_markers(_first_prop(
            props,
            fc.get("defining_markers", [
                "cluster_markers_combo",
                "supertype_markers_combo",
                "subclass_markers_combo",
            ]),
        )),
        tf_markers=_split_markers(_first_prop(
            props,
            fc.get("tf_markers", ["cluster_TF_markers_combo", "subclass_tf_markers_combo"]),
        )),
        merfish_markers=_split_markers(_first_prop(
            props,
            fc.get("merfish_markers", ["merfish_markers_combo"]),
        )),
        np_markers=_scalar(_first_prop(props, fc.get("np_markers", ["np_markers"]))),
        neighborhood=_scalar(_first_prop(props, fc.get("neighborhood", ["neighborhood"]))),
        circadian_ratio=_circadian(_scalar(_first_prop(
            props,
            fc.get("circadian_ratio", ["Light"]),
        ))),
        anat=anat_entries,
        rationale=rationale,
        rationale_dois=rationale_dois,
        sex_bias=_scalar(_first_prop(
            props,
            fc.get("sex_bias", ["sex_bias", "CCN20230722_sex_bias"]),
        )),
        neuronal=neuronal,
        glial=glial,
    )


# ── YAML generation ────────────────────────────────────────────────────────────

def _node_to_dict(n: TaxonomyNode) -> dict:
    d: dict = {
        "node_id": n.node_id,
        "short_form": n.short_form,
        "label": n.label,
        "taxonomy_level": n.taxonomy_level,
        "parent_id": n.parent_id,
        "cl_id": n.cl_id,
        "cl_label": n.cl_label,
        "cell_ontology_term": n.cell_ontology_term,
        "nt_type": n.nt_type,
        "defining_markers_scoped": n.defining_markers_scoped or None,
        "defining_markers": n.defining_markers or None,
        "tf_markers": n.tf_markers or None,
        "merfish_markers": n.merfish_markers or None,
        "np_markers": n.np_markers,
        "neighborhood": n.neighborhood,
        "circadian_ratio": n.circadian_ratio,
        "anat": n.anat or None,
        "rationale": n.rationale,
        "rationale_dois": n.rationale_dois or None,
        "sex_bias": n.sex_bias,
    }
    # class-level extras
    if n.neuronal is not None:
        d["neuronal"] = n.neuronal
    if n.glial is not None:
        d["glial"] = n.glial
    # drop all-null/empty fields for readability
    return {k: v for k, v in d.items() if v is not None}


def ingest_to_yaml(source: Path, taxonomy_id: str, output_dir: Path) -> dict[str, int]:
    """Generate per-level YAML files from source taxonomy JSON.

    Also reads inputs/taxonomies/{taxonomy_id}_meta.yaml (if present) and writes
    an enriched taxonomy_meta.yaml with name, species, tissue, anatomy_ontology,
    and MapMyCells references.

    Returns {level: node_count}.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    cleaned = clean_taxonomy_json(source)
    fc = _load_field_config(taxonomy_id)

    # Accumulate nodes by level
    by_level: dict[str, list[dict]] = {}
    for row in iter_taxonomy_rows(cleaned):
        node = _extract_node(row, taxonomy_id, fc)
        by_level.setdefault(node.taxonomy_level, []).append(_node_to_dict(node))

    counts: dict[str, int] = {}
    for level, nodes in sorted(by_level.items()):
        out_file = output_dir / f"{level}.yaml"
        with out_file.open("w", encoding="utf-8") as fh:
            yaml.dump(nodes, fh, allow_unicode=True, sort_keys=False, default_flow_style=False)
        counts[level] = len(nodes)

    # Read optional metadata input and merge with computed fields
    meta_input = _read_meta_input(taxonomy_id)
    if not meta_input:
        import sys
        print(
            f"  [info] No metadata input found at inputs/taxonomies/{taxonomy_id}_meta.yaml. "
            "Name, species, tissue, and MapMyCells fields will be null in taxonomy_meta.yaml.",
            file=sys.stderr,
        )
    mmc_raw = meta_input.get("mapmycells") or {}
    meta = TaxonomyMeta(
        taxonomy_id=taxonomy_id,
        taxonomy_name=meta_input.get("taxonomy_name"),
        species_id=meta_input.get("species_id"),
        species_label=meta_input.get("species_label"),
        tissue_id=meta_input.get("tissue_id"),
        tissue_label=meta_input.get("tissue_label"),
        anatomy_ontology=meta_input.get("anatomy_ontology"),
        source_query=meta_input.get("source_query"),
        source_file=source.name,
        ingest_date=str(date.today()),
        level_counts=counts,
        mapmycells=MapMyCellsMeta(
            at_taxonomy_id=mmc_raw.get("at_taxonomy_id"),
            stats_s3_url=mmc_raw.get("stats_s3_url"),
            markers_s3_url=mmc_raw.get("markers_s3_url"),
            local_stats_path=mmc_raw.get("local_stats_path"),
            local_markers_path=mmc_raw.get("local_markers_path"),
        ),
    )
    meta_file = output_dir / "taxonomy_meta.yaml"
    with meta_file.open("w", encoding="utf-8") as fh:
        yaml.dump(_meta_to_dict(meta), fh, allow_unicode=True, sort_keys=False)

    return counts


# ── SQLite backend ─────────────────────────────────────────────────────────────

_DDL = """\
CREATE TABLE IF NOT EXISTS nodes (
  node_id                TEXT PRIMARY KEY,
  short_form             TEXT NOT NULL,
  label                  TEXT NOT NULL,
  taxonomy_id            TEXT NOT NULL,
  taxonomy_level         TEXT NOT NULL,
  parent_id              TEXT,
  cl_id                  TEXT,
  cl_label               TEXT,
  cell_ontology_term     TEXT,
  nt_type                TEXT,
  defining_markers_scoped TEXT,
  defining_markers       TEXT,
  tf_markers             TEXT,
  merfish_markers        TEXT,
  np_markers             TEXT,
  neighborhood           TEXT,
  circadian_ratio        REAL,
  rationale              TEXT,
  rationale_dois         TEXT,
  sex_bias               TEXT
);

CREATE TABLE IF NOT EXISTS anat (
  node_id    TEXT NOT NULL REFERENCES nodes(node_id),
  anat_id    TEXT NOT NULL,
  anat_label TEXT NOT NULL,
  cell_count INTEGER,
  cell_ratio REAL
);

CREATE INDEX IF NOT EXISTS idx_nodes_level  ON nodes(taxonomy_level);
CREATE INDEX IF NOT EXISTS idx_nodes_cl     ON nodes(cl_id);
CREATE INDEX IF NOT EXISTS idx_nodes_nt     ON nodes(nt_type);
CREATE INDEX IF NOT EXISTS idx_anat_node    ON anat(node_id);
CREATE INDEX IF NOT EXISTS idx_anat_region  ON anat(anat_id);
"""

_CLOSURE_DDL = """\
CREATE TABLE IF NOT EXISTS anat_terms (
  anat_id   TEXT PRIMARY KEY,
  label     TEXT NOT NULL,
  uberon_id TEXT
);

CREATE TABLE IF NOT EXISTS anat_hierarchy (
  parent_id TEXT NOT NULL,
  child_id  TEXT NOT NULL,
  PRIMARY KEY (parent_id, child_id)
);

CREATE TABLE IF NOT EXISTS anat_closure (
  ancestor_id   TEXT NOT NULL,
  descendant_id TEXT NOT NULL,
  depth         INTEGER NOT NULL,
  PRIMARY KEY (ancestor_id, descendant_id)
);

CREATE INDEX IF NOT EXISTS idx_closure_ancestor   ON anat_closure(ancestor_id);
CREATE INDEX IF NOT EXISTS idx_closure_descendant ON anat_closure(descendant_id);
CREATE INDEX IF NOT EXISTS idx_terms_uberon        ON anat_terms(uberon_id);
"""


def _iri_to_curie(iri: str) -> str | None:
    """Convert an OBO-graph IRI to a CURIE string.

    https://purl.brain-bican.org/ontology/mbao/MBA_399  →  MBA:399
    http://purl.obolibrary.org/obo/UBERON_0001954       →  UBERON:0001954
    Returns None for any IRI that doesn't fit the pattern.
    """
    term = iri.rstrip("/").rsplit("/", 1)[-1]
    if "_" not in term:
        return None
    prefix, local = term.split("_", 1)
    return f"{prefix}:{local}"


def _parse_mba_obograph(path: Path) -> tuple[list[tuple[str, str, str | None]], list[tuple[str, str]]]:
    """Parse an MBA OBO JSON (Obograph) file.

    Returns:
        terms: list of (anat_id, label, uberon_id_or_None)
        edges: list of (parent_id, child_id) for MBA→MBA is_a edges only
    """
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    graph = data["graphs"][0]

    terms: list[tuple[str, str, str | None]] = []
    for node in graph.get("nodes", []):
        curie = _iri_to_curie(node.get("id", ""))
        if not curie or not curie.startswith("MBA:"):
            continue
        label = node.get("lbl", "")
        if node.get("type") != "CLASS" or not label:
            continue
        terms.append((curie, label, None))  # uberon_id filled from edges below

    # Build a set of all MBA CURIEs for fast lookup
    mba_ids = {t[0] for t in terms}

    # uberon_id: first UBERON target of an is_a edge from each MBA term
    uberon_map: dict[str, str] = {}
    mba_edges: list[tuple[str, str]] = []

    _PART_OF = "http://purl.obolibrary.org/obo/BFO_0000050"

    for edge in graph.get("edges", []):
        pred = edge.get("pred", "")
        sub = _iri_to_curie(edge.get("sub", ""))
        obj = _iri_to_curie(edge.get("obj", ""))
        if not sub or not obj:
            continue
        if pred == "is_a":
            if sub.startswith("MBA:") and obj.startswith("MBA:") and not obj.startswith("MBA:ENTITY"):
                mba_edges.append((obj, sub))  # sub is_a obj  ⟹  obj is parent
            elif sub.startswith("MBA:") and obj.startswith("UBERON:"):
                uberon_map.setdefault(sub, obj)
        elif pred == _PART_OF:
            if sub.startswith("MBA:") and obj.startswith("MBA:") and not obj.startswith("MBA:ENTITY"):
                mba_edges.append((obj, sub))  # sub part_of obj  ⟹  obj is spatial parent

    # Splice uberon_id back into terms
    terms = [(anat_id, label, uberon_map.get(anat_id)) for anat_id, label, _ in terms]

    return terms, mba_edges


def _compute_closure(edges: list[tuple[str, str]]) -> list[tuple[str, str, int]]:
    """Compute transitive closure of a parent→child edge list.

    Returns list of (ancestor_id, descendant_id, depth).
    Also includes reflexive pairs (node, node, 0) for every node.
    """
    children: dict[str, list[str]] = defaultdict(list)
    all_nodes: set[str] = set()
    for parent, child in edges:
        children[parent].append(child)
        all_nodes.add(parent)
        all_nodes.add(child)

    closure: list[tuple[str, str, int]] = []
    for root in all_nodes:
        closure.append((root, root, 0))
        # BFS downward
        queue = [(root, 0)]
        visited: set[str] = {root}
        while queue:
            node, depth = queue.pop(0)
            for child in children[node]:
                if child not in visited:
                    visited.add(child)
                    closure.append((root, child, depth + 1))
                    queue.append((child, depth + 1))

    return closure


class TaxonomyDB:
    """SQLite query index for a taxonomy, built from YAML reference files."""

    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def build_from_yaml(self, taxonomy_dir: Path) -> None:
        """Populate DB from kb/taxonomy/{taxonomy_id}/*.yaml. Idempotent (drops + rebuilds)."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        con = sqlite3.connect(self.db_path)
        try:
            con.executescript("DROP TABLE IF EXISTS anat; DROP TABLE IF EXISTS nodes;")
            con.executescript(_DDL)
            for yaml_file in sorted(taxonomy_dir.glob("*.yaml")):
                if yaml_file.name in ("taxonomy_meta.yaml", "field_mapping.yaml"):
                    continue
                with yaml_file.open(encoding="utf-8") as fh:
                    nodes = yaml.safe_load(fh)
                if not isinstance(nodes, list):
                    continue
                for nd in nodes:
                    self._insert_node(con, nd)
            con.commit()
        finally:
            con.close()

    def _insert_node(self, con: sqlite3.Connection, nd: dict) -> None:
        con.execute(
            """INSERT OR REPLACE INTO nodes VALUES (
               :node_id, :short_form, :label, :taxonomy_id, :taxonomy_level,
               :parent_id, :cl_id, :cl_label, :cell_ontology_term, :nt_type,
               :defining_markers_scoped, :defining_markers, :tf_markers,
               :merfish_markers, :np_markers, :neighborhood, :circadian_ratio,
               :rationale, :rationale_dois, :sex_bias
            )""",
            {
                "node_id": nd.get("node_id", ""),
                "short_form": nd.get("short_form", ""),
                "label": nd.get("label", ""),
                "taxonomy_id": nd.get("taxonomy_id", nd.get("taxonomy_level", "")),
                "taxonomy_level": nd.get("taxonomy_level", ""),
                "parent_id": nd.get("parent_id"),
                "cl_id": nd.get("cl_id"),
                "cl_label": nd.get("cl_label"),
                "cell_ontology_term": nd.get("cell_ontology_term"),
                "nt_type": nd.get("nt_type"),
                "defining_markers_scoped": json.dumps(nd["defining_markers_scoped"])
                    if nd.get("defining_markers_scoped") else None,
                "defining_markers": json.dumps(nd["defining_markers"])
                    if nd.get("defining_markers") else None,
                "tf_markers": json.dumps(nd["tf_markers"])
                    if nd.get("tf_markers") else None,
                "merfish_markers": json.dumps(nd["merfish_markers"])
                    if nd.get("merfish_markers") else None,
                "np_markers": nd.get("np_markers"),
                "neighborhood": nd.get("neighborhood"),
                "circadian_ratio": nd.get("circadian_ratio"),
                "rationale": nd.get("rationale"),
                "rationale_dois": json.dumps(nd["rationale_dois"])
                    if nd.get("rationale_dois") else None,
                "sex_bias": nd.get("sex_bias"),
            },
        )
        for a in nd.get("anat") or []:
            anat_id = a.get("id")
            if not anat_id:
                continue
            con.execute(
                "INSERT INTO anat VALUES (?, ?, ?, ?, ?)",
                (
                    nd.get("node_id", ""),
                    anat_id,
                    a.get("label", ""),
                    a.get("cell_count"),
                    a.get("cell_ratio"),
                ),
            )

    def _connect(self) -> sqlite3.Connection:
        con = sqlite3.connect(self.db_path)
        con.row_factory = sqlite3.Row
        return con

    def query_by_region(self, anat_ids: list[str], level: str = "supertype") -> list[dict]:
        """Return nodes present in any of the given anatomy regions."""
        if not anat_ids:
            return []
        placeholders = ",".join("?" * len(anat_ids))
        sql = f"""
            SELECT DISTINCT n.*
            FROM nodes n
            JOIN anat a ON a.node_id = n.node_id
            WHERE a.anat_id IN ({placeholders})
              AND n.taxonomy_level = ?
            ORDER BY n.label
        """
        with self._connect() as con:
            rows = con.execute(sql, [*anat_ids, level]).fetchall()
        return [dict(r) for r in rows]

    def query_by_nt(self, nt_type: str, level: str = "supertype") -> list[dict]:
        """Return nodes matching neurotransmitter type (case-insensitive prefix)."""
        sql = """
            SELECT * FROM nodes
            WHERE nt_type LIKE ? AND taxonomy_level = ?
            ORDER BY label
        """
        with self._connect() as con:
            rows = con.execute(sql, [f"{nt_type}%", level]).fetchall()
        return [dict(r) for r in rows]

    def query_by_cl(self, cl_id: str) -> list[dict]:
        """Return all nodes with a direct CL mapping to the given term."""
        with self._connect() as con:
            rows = con.execute(
                "SELECT * FROM nodes WHERE cl_id = ? ORDER BY taxonomy_level, label",
                (cl_id,),
            ).fetchall()
        return [dict(r) for r in rows]

    def build_anat_closure(self, mba_json: Path) -> None:
        """Populate anat_terms, anat_hierarchy, and anat_closure from an MBA OBO JSON file.

        Idempotent — drops and rebuilds the three closure tables on each call.
        The main nodes/anat tables are untouched.
        """
        terms, edges = _parse_mba_obograph(mba_json)
        closure = _compute_closure(edges)

        con = sqlite3.connect(self.db_path)
        try:
            con.executescript(
                "DROP TABLE IF EXISTS anat_closure;"
                "DROP TABLE IF EXISTS anat_hierarchy;"
                "DROP TABLE IF EXISTS anat_terms;"
            )
            con.executescript(_CLOSURE_DDL)
            con.executemany(
                "INSERT INTO anat_terms VALUES (?, ?, ?)", terms
            )
            con.executemany(
                "INSERT OR IGNORE INTO anat_hierarchy VALUES (?, ?)", edges
            )
            con.executemany(
                "INSERT INTO anat_closure VALUES (?, ?, ?)", closure
            )
            con.commit()
        finally:
            con.close()

    def get_descendants(self, anat_id: str, include_self: bool = True) -> list[str]:
        """Return all descendant anat_ids for a given region (requires closure tables).

        Raises RuntimeError if closure tables haven't been built yet.
        """
        with self._connect() as con:
            try:
                rows = con.execute(
                    "SELECT descendant_id FROM anat_closure WHERE ancestor_id = ?"
                    + ("" if include_self else " AND depth > 0"),
                    (anat_id,),
                ).fetchall()
            except sqlite3.OperationalError:
                raise RuntimeError(
                    "anat_closure table not found — run build_anat_closure() first "
                    "(justfile: just build-anat-closure)"
                )
        return [r[0] for r in rows]

    def find_candidates(
        self,
        anat_ids: list[str] | None = None,
        anat_root_ids: list[str] | None = None,
        nt_type: str | None = None,
        markers: list[str] | None = None,
        level: str = "supertype",
    ) -> list[dict]:
        """Return candidate nodes matching any combination of region, NT, and markers.

        anat_ids:      exact anat region IDs (leaf match)
        anat_root_ids: region IDs resolved transitively via closure tables; all
                       descendants are included automatically (requires build_anat_closure)
        nt_type:       prefix match against cluster-propagated NT type
        markers:       gene symbols; each match adds 1 pt

        Scoring: region match = 2 pts, NT match = 2 pts, each marker match = 1 pt.
        Results sorted descending by score.
        """
        # Resolve anat_root_ids to full descendant sets via closure
        effective_anat: set[str] = set(anat_ids or [])
        if anat_root_ids:
            for root in anat_root_ids:
                effective_anat.update(self.get_descendants(root, include_self=True))

        with self._connect() as con:
            rows = con.execute(
                "SELECT * FROM nodes WHERE taxonomy_level = ?", (level,)
            ).fetchall()

        results = []
        for row in rows:
            nd = dict(row)
            score = 0

            if effective_anat:
                node_anat = {a["anat_id"] for a in self._get_anat(nd["node_id"])}
                if node_anat & effective_anat:
                    score += 2

            if nt_type and nd.get("nt_type"):
                if nd["nt_type"].lower().startswith(nt_type.lower()):
                    score += 2

            if markers:
                node_markers: set[str] = set()
                for field_name in ("defining_markers_scoped", "defining_markers",
                                   "tf_markers", "merfish_markers"):
                    raw = nd.get(field_name)
                    if raw:
                        node_markers.update(json.loads(raw))
                for m in markers:
                    if m in node_markers:
                        score += 1

            if score > 0:
                nd["_score"] = score
                results.append(nd)

        results.sort(key=lambda x: x["_score"], reverse=True)
        return results

    def _get_anat(self, node_id: str) -> list[dict]:
        with self._connect() as con:
            rows = con.execute(
                "SELECT * FROM anat WHERE node_id = ?", (node_id,)
            ).fetchall()
        return [dict(r) for r in rows]


# ── CLI entry point ────────────────────────────────────────────────────────────

def _cmd_ingest(source: str, taxonomy_id: str) -> None:
    from evidencell.paths import taxonomy_dir
    out = taxonomy_dir(taxonomy_id)
    print(f"Ingesting {source} → {out}/")
    counts = ingest_to_yaml(Path(source), taxonomy_id, out)
    total = sum(counts.values())
    for lvl, n in sorted(counts.items()):
        print(f"  {lvl}: {n:,} nodes")
    print(f"  TOTAL: {total:,} nodes")
    print(f"YAML files written to {out}/")


def _cmd_build_db(taxonomy_id: str) -> None:
    from evidencell.paths import taxonomy_dir, taxonomy_db_path
    tdir = taxonomy_dir(taxonomy_id)
    db_path = taxonomy_db_path(taxonomy_id)
    print(f"Building SQLite index from {tdir}/ → {db_path}")
    db = TaxonomyDB(db_path)
    db.build_from_yaml(tdir)
    con = sqlite3.connect(db_path)
    n_nodes = con.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
    n_anat = con.execute("SELECT COUNT(*) FROM anat").fetchone()[0]
    con.close()
    print(f"  nodes: {n_nodes:,}  anat rows: {n_anat:,}")
    print(f"DB written to {db_path}")


def _cmd_sync_mapmycells_paths(taxonomy_id: str) -> None:
    """Sync local_stats_path / local_markers_path from the AT persisted spec into
    taxonomy_meta.yaml, converting absolute paths to repo-relative."""
    from evidencell.paths import taxonomy_meta_path, repo_root
    root = repo_root()

    # Read AT persisted spec
    at_spec_path = root / "annotation_transfer" / "taxonomies" / f"{taxonomy_id}.yaml"
    if not at_spec_path.exists():
        print(f"  No AT persisted spec at {at_spec_path} — nothing to sync.")
        return

    with at_spec_path.open(encoding="utf-8") as fh:
        at_spec = yaml.safe_load(fh)

    stats_abs = at_spec.get("local_stats_path")
    markers_abs = at_spec.get("local_markers_path")

    if not stats_abs and not markers_abs:
        print("  AT spec has no local paths set — nothing to sync.")
        return

    def _to_rel(p: str | None) -> str | None:
        if not p:
            return None
        try:
            return str(Path(p).relative_to(root))
        except ValueError:
            return p  # keep absolute if not under repo root

    stats_rel = _to_rel(stats_abs)
    markers_rel = _to_rel(markers_abs)

    # Update taxonomy_meta.yaml
    meta_path = taxonomy_meta_path(taxonomy_id)
    if not meta_path.exists():
        print(f"  taxonomy_meta.yaml not found at {meta_path} — skipping.")
        return

    with meta_path.open(encoding="utf-8") as fh:
        meta = yaml.safe_load(fh) or {}

    mmc = meta.setdefault("mapmycells", {})
    if stats_rel:
        mmc["local_stats_path"] = stats_rel
    if markers_rel:
        mmc["local_markers_path"] = markers_rel

    with meta_path.open("w", encoding="utf-8") as fh:
        yaml.dump(meta, fh, allow_unicode=True, sort_keys=False)

    print(f"  Updated {meta_path}")
    if stats_rel:
        print(f"    local_stats_path:   {stats_rel}")
    if markers_rel:
        print(f"    local_markers_path: {markers_rel}")


def _cmd_show_meta(taxonomy_id: str) -> None:
    meta = read_taxonomy_meta(taxonomy_id)
    print(f"taxonomy_id:       {meta.taxonomy_id}")
    print(f"taxonomy_name:     {meta.taxonomy_name}")
    print(f"species:           {meta.species_label} ({meta.species_id})")
    print(f"tissue:            {meta.tissue_label} ({meta.tissue_id})")
    print(f"anatomy_ontology:  {meta.anatomy_ontology}")
    print(f"source_query:      {meta.source_query}")
    print(f"source_file:       {meta.source_file}")
    print(f"ingest_date:       {meta.ingest_date}")
    print(f"level_counts:      {meta.level_counts}")
    mmc = meta.mapmycells
    print("mapmycells:")
    print(f"  at_taxonomy_id:  {mmc.at_taxonomy_id}")
    print(f"  stats_s3_url:    {mmc.stats_s3_url}")
    print(f"  markers_s3_url:  {mmc.markers_s3_url}")
    print(f"  local_stats:     {mmc.local_stats_path}")
    print(f"  local_markers:   {mmc.local_markers_path}")


def _cmd_fetch_mba(dest: str) -> None:
    dest_path = Path(dest)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading MBA ontology (latest release) → {dest_path}")
    print(f"  URL: {MBA_ONTOLOGY_URL}")
    with urllib.request.urlopen(MBA_ONTOLOGY_URL) as resp:  # noqa: S310
        data = resp.read()
    dest_path.write_bytes(data)
    size_kb = len(data) // 1024
    print(f"  Downloaded {size_kb:,} KB")


def _cmd_build_closure(taxonomy_id: str, mba_json: str) -> None:
    from evidencell.paths import taxonomy_db_path
    db_path = taxonomy_db_path(taxonomy_id)
    mba_path = Path(mba_json)
    if not db_path.exists():
        print(f"ERROR: DB not found at {db_path} — run build-db first")
        raise SystemExit(1)
    if not mba_path.exists():
        print(f"ERROR: MBA JSON not found at {mba_path} — run fetch-mba-ontology first")
        raise SystemExit(1)
    print(f"Building anat closure from {mba_path} → {db_path}")
    db = TaxonomyDB(db_path)
    db.build_anat_closure(mba_path)
    con = sqlite3.connect(db_path)
    n_terms = con.execute("SELECT COUNT(*) FROM anat_terms").fetchone()[0]
    n_edges = con.execute("SELECT COUNT(*) FROM anat_hierarchy").fetchone()[0]
    n_closure = con.execute("SELECT COUNT(*) FROM anat_closure").fetchone()[0]
    n_uberon = con.execute(
        "SELECT COUNT(*) FROM anat_terms WHERE uberon_id IS NOT NULL"
    ).fetchone()[0]
    con.close()
    print(f"  anat_terms: {n_terms:,}  ({n_uberon:,} with UBERON xref)")
    print(f"  anat_hierarchy edges: {n_edges:,}")
    print(f"  anat_closure rows: {n_closure:,}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python -m evidencell.taxonomy_db ingest <source_json> <taxonomy_id>")
        print("  python -m evidencell.taxonomy_db build-db <taxonomy_id>")
        print("  python -m evidencell.taxonomy_db show-meta <taxonomy_id>")
        print("  python -m evidencell.taxonomy_db sync-mapmycells-paths <taxonomy_id>")
        print("  python -m evidencell.taxonomy_db fetch-mba <dest_path>")
        print("  python -m evidencell.taxonomy_db build-closure <taxonomy_id> <mba_json>")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "ingest" and len(sys.argv) == 4:
        _cmd_ingest(sys.argv[2], sys.argv[3])
    elif cmd == "build-db" and len(sys.argv) == 3:
        _cmd_build_db(sys.argv[2])
    elif cmd == "show-meta" and len(sys.argv) == 3:
        _cmd_show_meta(sys.argv[2])
    elif cmd == "sync-mapmycells-paths" and len(sys.argv) == 3:
        _cmd_sync_mapmycells_paths(sys.argv[2])
    elif cmd == "fetch-mba" and len(sys.argv) == 3:
        _cmd_fetch_mba(sys.argv[2])
    elif cmd == "build-closure" and len(sys.argv) == 4:
        _cmd_build_closure(sys.argv[2], sys.argv[3])
    else:
        print(f"Unknown command or wrong arguments: {sys.argv[1:]}")
        sys.exit(1)
