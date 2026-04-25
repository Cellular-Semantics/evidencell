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
import sys
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterator

import ijson
import yaml

# Always-latest release of the BICAN Mouse Brain Atlas Ontology (OBO JSON / Obograph)
MBA_ONTOLOGY_URL = (
    "https://github.com/brain-bican/mouse_brain_atlas_ontology"
    "/releases/latest/download/mbao-full.json"
)
MBA_RELEASES_API = (
    "https://api.github.com/repos/brain-bican/"
    "mouse_brain_atlas_ontology/releases/latest"
)


def _fetch_latest_mba_release(timeout: float = 5.0) -> str | None:
    """Return the latest GitHub release tag for the MBA ontology, or None if unreachable."""
    try:
        with urllib.request.urlopen(MBA_RELEASES_API, timeout=timeout) as resp:  # noqa: S310
            return json.loads(resp.read())["tag_name"]
    except Exception:
        return None


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
    level_hierarchy: list[dict] = field(default_factory=list)  # [{level_name, rank, count, is_terminal}]
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
        level_hierarchy=d.get("level_hierarchy", []),
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
    if meta.level_hierarchy:
        d["level_hierarchy"] = meta.level_hierarchy
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
    male_female_ratio: float | None = None  # Male/Female cell count ratio, 2 dp
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


def _male_female_ratio(props: dict, fc: dict[str, list[str]]) -> float | None:
    """Compute Male/Female cell count ratio from source fractions.

    Returns ratio rounded to 2 dp, or None when either fraction is 0 or absent.
    """
    male_raw = _scalar(_first_prop(props, fc.get("male_fraction", ["Male"])))
    female_raw = _scalar(_first_prop(props, fc.get("female_fraction", ["Female"])))
    if male_raw is None or female_raw is None:
        return None
    try:
        male = float(male_raw)
        female = float(female_raw)
    except (ValueError, TypeError):
        return None
    if female == 0.0 or male == 0.0:
        return None
    return round(male / female, 2)


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
        male_female_ratio=_male_female_ratio(props, fc),
        neuronal=neuronal,
        glial=glial,
    )


def _compute_level_hierarchy(
    nodes: list[TaxonomyNode],
) -> tuple[list[dict], dict[str, int]]:
    """Derive rank assignments from parent relationships.

    Returns (level_hierarchy, level_to_rank) where level_hierarchy is the
    list for taxonomy_meta.yaml and level_to_rank maps level name → int rank.

    Algorithm: build a directed graph of level→parent_level edges from the
    nodes' parent relationships.  Leaf levels (no children) get rank 0,
    then increment toward root.  Levels that appear only as parents of
    themselves (e.g. NEUROTRANSMITTER with no parent) and have no children
    from other levels are excluded (orthogonal annotations).
    """
    # Build {node_id: level} and {level: set(parent_levels)}
    id_to_level: dict[str, str] = {}
    levels: set[str] = set()
    for n in nodes:
        lev = n.taxonomy_level.upper()
        id_to_level[n.node_id] = lev
        levels.add(lev)

    # child_level → set of parent_levels
    parent_of: dict[str, set[str]] = {lev: set() for lev in levels}
    for n in nodes:
        if n.parent_id:
            parent_lev = id_to_level.get(n.parent_id)
            if parent_lev:
                child_lev = n.taxonomy_level.upper()
                if parent_lev != child_lev:
                    parent_of[child_lev].add(parent_lev)

    # Find hierarchical levels: those that appear as child or parent of another level
    hierarchical: set[str] = set()
    for child, parents in parent_of.items():
        if parents:
            hierarchical.add(child)
            hierarchical.update(parents)

    # Topological sort: leaf (no children pointing to it as parent) → root
    # "children" of a level = levels whose parent_of set contains this level
    children_of: dict[str, set[str]] = {lev: set() for lev in hierarchical}
    for child in hierarchical:
        for parent in parent_of.get(child, set()):
            if parent in hierarchical:
                children_of[parent].add(child)

    # Assign ranks bottom-up: leaves first
    level_to_rank: dict[str, int] = {}
    assigned: set[str] = set()

    def _assign(lev: str) -> int:
        if lev in level_to_rank:
            return level_to_rank[lev]
        kids = children_of.get(lev, set())
        if not kids:
            level_to_rank[lev] = 0
            assigned.add(lev)
            return 0
        max_child_rank = max(_assign(c) for c in kids)
        rank = max_child_rank + 1
        level_to_rank[lev] = rank
        assigned.add(lev)
        return rank

    for lev in hierarchical:
        _assign(lev)

    # Count nodes per level
    level_count: dict[str, int] = {}
    for n in nodes:
        lev = n.taxonomy_level.upper()
        level_count[lev] = level_count.get(lev, 0) + 1

    # Build hierarchy list sorted by rank
    hierarchy: list[dict] = []
    for lev, rank in sorted(level_to_rank.items(), key=lambda x: x[1]):
        entry: dict = {
            "level_name": lev,
            "rank": rank,
            "count": level_count.get(lev, 0),
        }
        if rank == 0:
            entry["is_terminal"] = True
        hierarchy.append(entry)

    return hierarchy, level_to_rank


# ── YAML generation ────────────────────────────────────────────────────────────

# WMBv1 accession type-code → taxonomy level string
_ACCESSION_LEVEL_MAP: dict[str, str] = {
    "CLUS": "CLUSTER",
    "SUPT": "SUPERTYPE",
    "SUBC": "SUBCLASS",
    "CLAS": "CLASS",
    "NETT": "NEUROTRANSMITTER",
}


def _strip_accession_from_label(label: str, short_form: str) -> str:
    """Strip embedded accession suffix from atlas label.

    e.g. '0649 Vip Gaba_7 CS20230722_CLUS_0649' → '0649 Vip Gaba_7'
    """
    if short_form and label.endswith(short_form):
        return label[: -len(short_form)].strip()
    return label


def _infer_level_from_accession(accession: str) -> str:
    """Infer taxonomy level string from a WMBv1 accession code.

    e.g. 'CS20230722_SUPT_0179' → 'SUPERTYPE'. Returns 'UNKNOWN' if no
    recognised type-code is found.
    """
    for part in accession.split("_"):
        if part in _ACCESSION_LEVEL_MAP:
            return _ACCESSION_LEVEL_MAP[part]
    return "UNKNOWN"


def _parse_np_markers(np_markers: str | None) -> list[dict]:
    """Parse packed np_markers string ('Vip:9.2,Penk:6.8') into GeneDescriptor dicts."""
    if not np_markers:
        return []
    entries: list[dict] = []
    for part in np_markers.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" in part:
            sym, score_str = part.rsplit(":", 1)
            try:
                entries.append({"symbol": sym.strip(), "category": "NEUROPEPTIDE",
                                 "expression_score": float(score_str)})
                continue
            except ValueError:
                pass
        entries.append({"symbol": part, "category": "NEUROPEPTIDE"})
    return entries


def _node_to_dict(n: TaxonomyNode, meta: TaxonomyMeta, name_lookup: dict[str, str]) -> dict:
    """Convert a TaxonomyNode to a schema-compliant CellTypeNode dict.

    meta  — used for species fields
    name_lookup — accession/CURIE → clean name, for parent_hierarchy.name
    """
    name = _strip_accession_from_label(n.label, n.short_form)
    tax_level = n.taxonomy_level.upper()

    # Unified markers list
    markers: list[dict] = []
    for sym in n.defining_markers:
        markers.append({"symbol": sym, "category": "DEFINING"})
    for sym in n.defining_markers_scoped:
        markers.append({"symbol": sym, "category": "DEFINING_SCOPED"})
    for sym in n.tf_markers:
        markers.append({"symbol": sym, "category": "TF"})
    for sym in n.merfish_markers:
        markers.append({"symbol": sym, "category": "MERFISH"})
    markers.extend(_parse_np_markers(n.np_markers))

    # NeurotransmitterType
    nt_type_obj: dict | None = None
    if n.nt_type:
        nt_type_obj = {"name_in_source": n.nt_type}

    # CL mapping (cell type, not NT type)
    # OntologyTerm requires id + label + name_in_source (all three).
    cl_mapping: dict | None = None
    if n.cl_id and n.cl_label:
        cl_term: dict = {
            "id": n.cl_id,
            "label": n.cl_label,
            "name_in_source": n.cell_ontology_term or n.cl_label,
        }
        cl_mapping = {"cl_term": cl_term, "mapping_type": "EXACT"}

    # Anatomical location (soma only)
    anat_locs: list[dict] = []
    for a in n.anat:
        anat_id = a.get("id")
        if not anat_id:
            continue
        loc: dict = {
            "id": anat_id,
            "label": a.get("label", ""),
            "name_in_source": a.get("label", ""),
            "compartment": "SOMA",
        }
        if a.get("cell_count") is not None:
            loc["cell_count"] = a["cell_count"]
        anat_locs.append(loc)

    # Parent hierarchy (single immediate parent for atlas nodes)
    parent_hierarchy: list[dict] = []
    if n.parent_id:
        parent_acc = n.parent_id.split(":", 1)[-1] if ":" in n.parent_id else n.parent_id
        parent_name = name_lookup.get(parent_acc) or name_lookup.get(n.parent_id) or parent_acc
        parent_hierarchy.append({
            "level": _infer_level_from_accession(parent_acc),
            "name": parent_name,
            "cell_set_accession": parent_acc,
        })

    # Species from taxonomy metadata
    species: dict | None = None
    if meta.species_id or meta.species_label:
        species = {}
        if meta.species_id:
            species["id"] = meta.species_id
        if meta.species_label:
            species["label"] = meta.species_label
            species["name_in_source"] = meta.species_label

    d: dict = {
        "id": n.node_id,
        "name": name,
        "cell_set_accession": n.short_form,
        "taxonomy_id": n.taxonomy_id,
        "taxonomy_level": tax_level,
        "definition_basis": "ATLAS_TRANSCRIPTOMIC",
        "is_terminal": tax_level == "CLUSTER",
    }
    if parent_hierarchy:
        d["parent_hierarchy"] = parent_hierarchy
    if nt_type_obj:
        d["nt_type"] = nt_type_obj
    if markers:
        d["markers"] = markers
    if cl_mapping:
        d["cl_mapping"] = cl_mapping
    if anat_locs:
        d["anatomical_location"] = anat_locs
    if n.neighborhood:
        d["neighborhood"] = n.neighborhood
    if n.male_female_ratio is not None:
        d["male_female_ratio"] = n.male_female_ratio
    if species:
        d["species"] = species
    return d


def ingest_to_yaml(source: Path, taxonomy_id: str, output_dir: Path) -> dict[str, int]:
    """Generate per-level TaxonomyNodeList YAML files from source taxonomy JSON.

    Each output file contains a TaxonomyNodeList with schema-compliant CellTypeNode
    objects, wrapped as:
        taxonomy_id: <id>
        taxonomy_level: <LEVEL>
        nodes: [...]

    Also reads inputs/taxonomies/{taxonomy_id}_meta.yaml (if present) and writes
    an enriched taxonomy_meta.yaml.

    Returns {level: node_count}.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    cleaned = clean_taxonomy_json(source)
    fc = _load_field_config(taxonomy_id)

    # Read metadata early so _node_to_dict can embed species
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
        level_counts={},  # filled below
        mapmycells=MapMyCellsMeta(
            at_taxonomy_id=mmc_raw.get("at_taxonomy_id"),
            stats_s3_url=mmc_raw.get("stats_s3_url"),
            markers_s3_url=mmc_raw.get("markers_s3_url"),
            local_stats_path=mmc_raw.get("local_stats_path"),
            local_markers_path=mmc_raw.get("local_markers_path"),
        ),
    )

    # First pass: extract all TaxonomyNode objects and build name lookup
    all_nodes: list[TaxonomyNode] = []
    for row in iter_taxonomy_rows(cleaned):
        all_nodes.append(_extract_node(row, taxonomy_id, fc))

    # name_lookup: bare accession and CURIE → clean name (for parent_hierarchy)
    name_lookup: dict[str, str] = {}
    for n in all_nodes:
        clean_name = _strip_accession_from_label(n.label, n.short_form)
        if n.short_form:
            name_lookup[n.short_form] = clean_name
        if n.node_id:
            name_lookup[n.node_id] = clean_name

    # Compute level hierarchy and assign ranks to nodes
    level_hierarchy, level_to_rank = _compute_level_hierarchy(all_nodes)

    # Second pass: convert to CellTypeNode dicts grouped by level
    by_level: dict[str, list[dict]] = {}
    for n in all_nodes:
        d = _node_to_dict(n, meta, name_lookup)
        lev_upper = n.taxonomy_level.upper()
        rank = level_to_rank.get(lev_upper)
        if rank is not None:
            d["taxonomy_rank"] = rank
        by_level.setdefault(n.taxonomy_level, []).append(d)

    # Write one TaxonomyNodeList YAML per level
    counts: dict[str, int] = {}
    for level, nodes in sorted(by_level.items()):
        lev_upper = level.upper()
        header: dict[str, Any] = {
            "taxonomy_id": taxonomy_id,
            "taxonomy_level": lev_upper,
        }
        rank = level_to_rank.get(lev_upper)
        if rank is not None:
            header["taxonomy_rank"] = rank
        header["nodes"] = nodes
        out_file = output_dir / f"{level}.yaml"
        with out_file.open("w", encoding="utf-8") as fh:
            yaml.dump(
                header,
                fh,
                allow_unicode=True,
                sort_keys=False,
                default_flow_style=False,
            )
        counts[level] = len(nodes)

    meta.level_counts = counts
    meta.level_hierarchy = level_hierarchy
    meta_file = output_dir / "taxonomy_meta.yaml"
    with meta_file.open("w", encoding="utf-8") as fh:
        yaml.dump(_meta_to_dict(meta), fh, allow_unicode=True, sort_keys=False)

    return counts


# ── CAS (Cell Annotation Schema) ingest ──────────────────────────────────────


def _is_cas_format(data: dict | list) -> bool:
    """Return True if the JSON data looks like CAS v5+ format."""
    return isinstance(data, dict) and "annotations" in data and "labelsets" in data


def _cas_level_name(labelset_name: str) -> str:
    """Normalise a CAS labelset name to a taxonomy level string.

    CAS labelset names are arbitrary (e.g. "cluster_label", "subclass_label").
    Strip common suffixes to produce a cleaner level name for YAML output.
    """
    # Strip _label suffix if present (common CAS convention)
    name = labelset_name
    if name.endswith("_label"):
        name = name[: -len("_label")]
    return name.upper()


def ingest_cas_to_yaml(
    source: Path, taxonomy_id: str, output_dir: Path
) -> dict[str, int]:
    """Generate per-level TaxonomyNodeList YAML files from CAS-format JSON.

    CAS (Cell Annotation Schema) v5+ format stores annotations as a flat list
    with ``labelset`` indicating the taxonomy level.  Labelset names are
    arbitrary — the ``rank`` field on each labelset definition provides the
    canonical ordering (0 = leaf / most specific).

    Produces the same per-level YAML + taxonomy_meta.yaml output as
    ``ingest_to_yaml()``.

    Returns {level: node_count}.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    with source.open(encoding="utf-8") as fh:
        data = json.load(fh)

    if not _is_cas_format(data):
        raise ValueError(
            f"{source} is not CAS format (expected top-level 'annotations' + 'labelsets')"
        )

    # Build labelset → rank mapping
    labelset_rank: dict[str, int] = {}
    for ls in data["labelsets"]:
        labelset_rank[ls["name"]] = ls.get("rank", 0)

    # Read optional metadata input
    meta_input = _read_meta_input(taxonomy_id)
    if not meta_input:
        print(
            f"  [info] No metadata input found at inputs/taxonomies/{taxonomy_id}_meta.yaml. "
            "Name, species, tissue fields will be null in taxonomy_meta.yaml.",
            file=sys.stderr,
        )

    # Extract reference DOI from first annotation that has one
    # (currently unused — retained for future taxonomy-level citation)
    _ref_doi = None  # noqa: F841
    for ann in data["annotations"]:
        dois = ann.get("rationale_dois", [])
        if dois:
            _ref_doi = dois[0]  # noqa: F841
            break

    mmc_raw = meta_input.get("mapmycells") or {}
    meta = TaxonomyMeta(
        taxonomy_id=taxonomy_id,
        taxonomy_name=meta_input.get("taxonomy_name") or data.get("title"),
        species_id=meta_input.get("species_id"),
        species_label=meta_input.get("species_label"),
        tissue_id=meta_input.get("tissue_id"),
        tissue_label=meta_input.get("tissue_label"),
        anatomy_ontology=meta_input.get("anatomy_ontology"),
        source_file=source.name,
        ingest_date=str(date.today()),
        level_counts={},
        mapmycells=MapMyCellsMeta(
            at_taxonomy_id=mmc_raw.get("at_taxonomy_id"),
            stats_s3_url=mmc_raw.get("stats_s3_url"),
            markers_s3_url=mmc_raw.get("markers_s3_url"),
            local_stats_path=mmc_raw.get("local_stats_path"),
            local_markers_path=mmc_raw.get("local_markers_path"),
        ),
    )

    # Species dict from metadata
    species: dict | None = None
    if meta.species_id or meta.species_label:
        species = {}
        if meta.species_id:
            species["id"] = meta.species_id
        if meta.species_label:
            species["label"] = meta.species_label
            species["name_in_source"] = meta.species_label

    # Build name lookup for parent_hierarchy resolution
    name_lookup: dict[str, str] = {}
    for ann in data["annotations"]:
        acc = ann.get("cell_set_accession", "")
        label = ann.get("cell_label", "")
        if acc and label:
            name_lookup[acc] = label

    # Convert annotations to CellTypeNode dicts grouped by level
    by_level: dict[str, list[dict]] = {}
    for ann in data["annotations"]:
        labelset = ann.get("labelset", "")
        level = _cas_level_name(labelset)
        rank = labelset_rank.get(labelset, 0)
        acc = ann.get("cell_set_accession", "")
        label = ann.get("cell_label", "")
        parent_acc = ann.get("parent_cell_set_accession")

        # Build node CURIE: taxonomy_id prefix + accession
        # CAS accessions are already prefixed (e.g. CS202106160_79)
        # but some use hash-based format (e.g. subclass_label:HASH)
        node_id = f"CTX-HPF:{acc}" if acc else ""

        # Determine if terminal (leaf level = rank 0)
        is_terminal = rank == 0

        # Parent hierarchy
        parent_hierarchy: list[dict] = []
        if parent_acc:
            parent_name = name_lookup.get(parent_acc, parent_acc)
            # Infer parent level from its labelset (look up in annotations)
            parent_level = "UNKNOWN"
            for other in data["annotations"]:
                if other.get("cell_set_accession") == parent_acc:
                    parent_level = _cas_level_name(other.get("labelset", ""))
                    break
            parent_hierarchy.append({
                "level": parent_level,
                "name": parent_name,
                "cell_set_accession": parent_acc,
            })

        # Author annotation fields
        aaf = ann.get("author_annotation_fields", {})

        d: dict = {
            "id": node_id,
            "name": label,
            "cell_set_accession": acc,
            "taxonomy_id": taxonomy_id,
            "taxonomy_level": level,
            "taxonomy_rank": rank,
            "definition_basis": "ATLAS_TRANSCRIPTOMIC",
            "is_terminal": is_terminal,
        }
        if parent_hierarchy:
            d["parent_hierarchy"] = parent_hierarchy
        if species:
            d["species"] = species
        # Preserve rationale DOIs as-is
        dois = ann.get("rationale_dois", [])
        if dois:
            d["rationale_dois"] = dois
        # Preserve designation from author_annotation_fields
        designation = aaf.get("cell_set_designation")
        if designation:
            d["cell_set_designation"] = designation

        by_level.setdefault(level, []).append(d)

    # Write one TaxonomyNodeList YAML per level
    counts: dict[str, int] = {}
    for level, nodes in sorted(by_level.items()):
        # Use rank from first node for filename (levels are arbitrary names)
        safe_name = level.lower().replace("/", "_").replace(" ", "_")
        out_file = output_dir / f"{safe_name}.yaml"
        # Sort nodes by accession for stable output
        nodes.sort(key=lambda n: n.get("cell_set_accession", ""))
        with out_file.open("w", encoding="utf-8") as fh:
            yaml.dump(
                {
                    "taxonomy_id": taxonomy_id,
                    "taxonomy_level": level,
                    "taxonomy_rank": labelset_rank.get(
                        next(
                            (ls for ls in labelset_rank if _cas_level_name(ls) == level),
                            "",
                        ),
                        0,
                    ),
                    "nodes": nodes,
                },
                fh,
                allow_unicode=True,
                sort_keys=False,
                default_flow_style=False,
            )
        counts[level] = len(nodes)

    meta.level_counts = counts
    # Build level_hierarchy from labelset_rank + counts
    cas_hierarchy: list[dict] = []
    for ls_name, ls_rank in sorted(labelset_rank.items(), key=lambda x: x[1]):
        level = _cas_level_name(ls_name)
        if level in counts:
            entry: dict = {"level_name": level, "rank": ls_rank, "count": counts[level]}
            if ls_rank == 0:
                entry["is_terminal"] = True
            cas_hierarchy.append(entry)
    meta.level_hierarchy = cas_hierarchy
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
  taxonomy_rank          INTEGER,
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
  male_female_ratio      REAL
);

CREATE TABLE IF NOT EXISTS anat (
  node_id    TEXT NOT NULL REFERENCES nodes(node_id),
  anat_id    TEXT NOT NULL,
  anat_label TEXT NOT NULL,
  cell_count INTEGER,
  cell_ratio REAL
);

CREATE INDEX IF NOT EXISTS idx_nodes_level  ON nodes(taxonomy_level);
CREATE INDEX IF NOT EXISTS idx_nodes_rank   ON nodes(taxonomy_rank);
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
                    data = yaml.safe_load(fh)
                file_rank: int | None = None
                if isinstance(data, dict) and "nodes" in data:
                    # TaxonomyNodeList format (current)
                    nodes = data["nodes"]
                    file_rank = data.get("taxonomy_rank")  # S1: rank from file header
                elif isinstance(data, list):
                    # Legacy flat list (backward compat during migration)
                    nodes = data
                else:
                    continue
                if not isinstance(nodes, list):
                    continue
                for nd in nodes:
                    self._insert_node(con, nd, file_rank=file_rank)
            con.executescript(
                "CREATE TABLE IF NOT EXISTS _meta (key TEXT PRIMARY KEY, value TEXT);"
            )
            con.execute(
                "INSERT OR REPLACE INTO _meta VALUES ('taxonomy_built_at', ?)",
                (datetime.now(tz=timezone.utc).isoformat(),),
            )
            con.commit()
        finally:
            con.close()

    def _insert_node(
        self,
        con: sqlite3.Connection,
        nd: dict,
        file_rank: int | None = None,
    ) -> None:
        """Insert a CellTypeNode dict into the SQLite nodes + anat tables."""
        # node_id stored as bare accession (strip WMB: prefix for SQL join simplicity)
        raw_id = nd.get("id", "")
        node_id = raw_id.split(":", 1)[-1] if ":" in raw_id else raw_id
        short_form = nd.get("cell_set_accession") or node_id
        label = nd.get("name", "")
        tax_id = nd.get("taxonomy_id", "")
        tax_level = (nd.get("taxonomy_level") or "").lower()
        # S1: rank from node, falling back to file-level rank
        tax_rank = nd.get("taxonomy_rank") if nd.get("taxonomy_rank") is not None else file_rank

        # parent_id: bare accession from parent_hierarchy[0]
        parent_hierarchy = nd.get("parent_hierarchy") or []
        parent_id = parent_hierarchy[0].get("cell_set_accession") if parent_hierarchy else None

        # CL mapping
        cl_mapping = nd.get("cl_mapping") or {}
        cl_term = cl_mapping.get("cl_term") or {}
        cl_id = cl_term.get("id")
        cl_label = cl_term.get("label")
        cell_ontology_term = cl_term.get("name_in_source")

        # NT type
        nt_obj = nd.get("nt_type")
        if isinstance(nt_obj, dict):
            nt_type = nt_obj.get("name_in_source")
        elif isinstance(nt_obj, str):
            nt_type = nt_obj
        else:
            nt_type = None

        # Markers by category
        markers = nd.get("markers") or []
        defining_markers = [m["symbol"] for m in markers if m.get("category") == "DEFINING"]
        defining_markers_scoped = [m["symbol"] for m in markers if m.get("category") == "DEFINING_SCOPED"]
        tf_markers = [m["symbol"] for m in markers if m.get("category") == "TF"]
        merfish_markers = [m["symbol"] for m in markers if m.get("category") == "MERFISH"]
        np_pairs = [
            (m["symbol"], m.get("expression_score"))
            for m in markers if m.get("category") == "NEUROPEPTIDE"
        ]
        np_markers: str | None = (
            ",".join(
                f"{sym}:{score}" if score is not None else sym
                for sym, score in np_pairs
            ) or None
        )

        con.execute(
            """INSERT OR REPLACE INTO nodes VALUES (
               :node_id, :short_form, :label, :taxonomy_id, :taxonomy_level,
               :taxonomy_rank, :parent_id, :cl_id, :cl_label,
               :cell_ontology_term, :nt_type,
               :defining_markers_scoped, :defining_markers, :tf_markers,
               :merfish_markers, :np_markers, :neighborhood, :circadian_ratio,
               :rationale, :rationale_dois, :male_female_ratio
            )""",
            {
                "node_id": node_id,
                "short_form": short_form,
                "label": label,
                "taxonomy_id": tax_id,
                "taxonomy_level": tax_level,
                "taxonomy_rank": tax_rank,
                "parent_id": parent_id,
                "cl_id": cl_id,
                "cl_label": cl_label,
                "cell_ontology_term": cell_ontology_term,
                "nt_type": nt_type,
                "defining_markers_scoped": json.dumps(defining_markers_scoped)
                    if defining_markers_scoped else None,
                "defining_markers": json.dumps(defining_markers)
                    if defining_markers else None,
                "tf_markers": json.dumps(tf_markers) if tf_markers else None,
                "merfish_markers": json.dumps(merfish_markers) if merfish_markers else None,
                "np_markers": np_markers,
                "neighborhood": nd.get("neighborhood"),
                "circadian_ratio": None,  # not in CellTypeNode schema
                "rationale": None,        # not in CellTypeNode schema
                "rationale_dois": None,   # not in CellTypeNode schema
                "male_female_ratio": nd.get("male_female_ratio"),
            },
        )
        for a in nd.get("anatomical_location") or []:
            anat_id = a.get("id")
            if not anat_id:
                continue
            con.execute(
                "INSERT INTO anat VALUES (?, ?, ?, ?, ?)",
                (
                    node_id,
                    anat_id,
                    a.get("label") or a.get("name_in_source", ""),
                    a.get("cell_count"),
                    None,  # cell_ratio not in AnatomicalLocation schema
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
        """Return nodes matching neurotransmitter type (case-insensitive prefix).

        Note: in WMBv1, nt_type is only populated at cluster level. For supertype
        and above use query_by_nt_propagated() instead.
        """
        sql = """
            SELECT * FROM nodes
            WHERE nt_type LIKE ? AND taxonomy_level = ?
            ORDER BY label
        """
        with self._connect() as con:
            rows = con.execute(sql, [f"{nt_type}%", level]).fetchall()
        return [dict(r) for r in rows]

    def propagate_nt_types(
        self,
        child_level: str = "cluster",
        parent_level: str = "supertype",
    ) -> dict[str, str | None]:
        """Build a {node_id → nt_type} map for parent_level nodes by aggregating child NT.

        A parent is assigned an NT type only when ALL children at child_level share
        exactly one NT type. Returns None for mixed-NT or zero-cluster parents.
        Uses the parent_id foreign key stored in each child row.
        """
        sql = """
            SELECT parent_id,
                   COUNT(DISTINCT nt_type) AS n_types,
                   MAX(nt_type)            AS single_type
            FROM nodes
            WHERE taxonomy_level = ?
              AND parent_id      IS NOT NULL
              AND nt_type        IS NOT NULL
            GROUP BY parent_id
        """
        with self._connect() as con:
            rows = con.execute(sql, [child_level]).fetchall()
        return {
            r["parent_id"]: (r["single_type"] if r["n_types"] == 1 else None)
            for r in rows
        }

    def query_by_nt_propagated(
        self,
        nt_type: str,
        level: str = "supertype",
        child_level: str = "cluster",
    ) -> list[dict]:
        """Return nodes at level where all children share the given NT type.

        Propagates nt_type upward one hop (child_level → level). Useful for
        supertype-level NT queries in WMBv1 where nt_type is only stored on clusters.
        """
        nt_map = self.propagate_nt_types(child_level=child_level, parent_level=level)
        matching = [
            nid for nid, nt in nt_map.items()
            if nt and nt.lower().startswith(nt_type.lower())
        ]
        if not matching:
            return []
        placeholders = ",".join("?" * len(matching))
        with self._connect() as con:
            rows = con.execute(
                f"SELECT * FROM nodes WHERE node_id IN ({placeholders})"
                f"  AND taxonomy_level = ? ORDER BY label",
                [*matching, level],
            ).fetchall()
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
            con.executescript(
                "CREATE TABLE IF NOT EXISTS _meta (key TEXT PRIMARY KEY, value TEXT);"
            )
            release = _fetch_latest_mba_release()
            now = datetime.now(tz=timezone.utc).isoformat()
            if release is not None:
                con.execute(
                    "INSERT OR REPLACE INTO _meta VALUES ('anatomy_closure_release', ?)",
                    (release,),
                )
            con.execute(
                "INSERT OR REPLACE INTO _meta VALUES ('anatomy_closure_built_at', ?)",
                (now,),
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

    _ALL_MARKER_COLS: tuple[str, ...] = (
        "defining_markers_scoped", "defining_markers", "tf_markers", "merfish_markers"
    )

    def _propagate_nt_by_rank(
        self,
        child_rank: int = 0,
        parent_rank: int = 1,
    ) -> dict[str, str | None]:
        """Like propagate_nt_types but using rank instead of level names."""
        sql = """
            SELECT p.node_id AS parent_id,
                   COUNT(DISTINCT c.nt_type) AS n_types,
                   MAX(c.nt_type)            AS single_type
            FROM nodes c
            JOIN nodes p ON c.parent_id = p.node_id
            WHERE c.taxonomy_rank = ?
              AND p.taxonomy_rank = ?
              AND c.nt_type IS NOT NULL
            GROUP BY p.node_id
        """
        with self._connect() as con:
            rows = con.execute(sql, [child_rank, parent_rank]).fetchall()
        return {
            r["parent_id"]: (r["single_type"] if r["n_types"] == 1 else None)
            for r in rows
        }

    def find_candidates(
        self,
        anat_ids: list[str] | None = None,
        anat_root_ids: list[str] | None = None,
        nt_type: str | None = None,
        markers: list[str] | None = None,
        level: str | None = None,
        rank: int | None = None,
        marker_columns: list[str] | None = None,
        propagate_nt: bool = True,
    ) -> list[dict]:
        """Return candidate nodes matching any combination of region, NT, and markers.

        Specify nodes to search via *either* ``rank`` (preferred, taxonomy-agnostic)
        or ``level`` (legacy, taxonomy-specific name string).  ``rank`` takes precedence
        when both are provided.

        anat_ids:       exact anat region IDs (leaf match)
        anat_root_ids:  region IDs resolved transitively via closure tables
        nt_type:        prefix match; propagated from clusters when propagate_nt=True
                        (required for supertype/subclass in WMBv1 where nt_type is null)
        markers:        gene symbols; each match adds 1 pt
        marker_columns: which SQLite marker columns to score against; defaults to all four
                        (defining_markers_scoped, defining_markers, tf_markers, merfish_markers).
                        Pass ["defining_markers_scoped"] for scoped-only marker matching.
        propagate_nt:   when True (default), fall back to cluster-aggregated NT when the
                        node's own nt_type is null
        rank:           integer rank (0 = leaf). Selects nodes by taxonomy_rank column.
        level:          taxonomy level string (e.g. "cluster", "supertype"). Used when rank
                        is not provided, for backward compatibility.

        Scoring: region match = 2 pts, NT match = 2 pts, each marker match = 1 pt.
        Results sorted descending by score.
        """
        if rank is None and level is None:
            raise ValueError("Either rank or level must be specified")

        _marker_cols = tuple(marker_columns) if marker_columns else self._ALL_MARKER_COLS

        # Resolve anat_root_ids to full descendant sets via closure
        effective_anat: set[str] = set(anat_ids or [])
        if anat_root_ids:
            for root in anat_root_ids:
                effective_anat.update(self.get_descendants(root, include_self=True))

        # Determine whether we're at leaf rank (rank 0) for NT propagation
        is_leaf = rank == 0 if rank is not None else (level == "cluster")

        # Pre-load propagated NT map for non-leaf levels when needed
        _nt_map: dict[str, str | None] = {}
        if nt_type and propagate_nt and not is_leaf:
            if rank is not None:
                # Propagate from rank 0 (leaf) to the target rank's level name
                _nt_map = self._propagate_nt_by_rank(child_rank=0, parent_rank=rank)
            else:
                _nt_map = self.propagate_nt_types(
                    child_level="cluster", parent_level=level,  # type: ignore[arg-type]
                )

        # Select nodes by rank (preferred) or level
        with self._connect() as con:
            if rank is not None:
                rows = con.execute(
                    "SELECT * FROM nodes WHERE taxonomy_rank = ?", (rank,)
                ).fetchall()
            else:
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

            if nt_type:
                node_nt = nd.get("nt_type") or _nt_map.get(nd["node_id"])
                if node_nt:
                    nn, qt = node_nt.lower(), nt_type.lower()
                    if nn.startswith(qt) or qt.startswith(nn):
                        score += 2

            if markers:
                node_markers: set[str] = set()
                for col in _marker_cols:
                    raw = nd.get(col)
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

def _detect_cas_format(source: Path) -> bool:
    """Peek at a JSON file to check if it's CAS format (has annotations + labelsets)."""
    with source.open(encoding="utf-8") as fh:
        # Read enough to find top-level keys without loading the whole file
        try:
            data = json.load(fh)
        except json.JSONDecodeError:
            return False
    return _is_cas_format(data)


def _cmd_ingest(source: str, taxonomy_id: str) -> None:
    from evidencell.paths import taxonomy_dir
    out = taxonomy_dir(taxonomy_id)
    src = Path(source)
    is_cas = _detect_cas_format(src)
    fmt = "CAS" if is_cas else "VFB graph export"
    print(f"Ingesting {source} ({fmt} format) → {out}/")
    if is_cas:
        counts = ingest_cas_to_yaml(src, taxonomy_id, out)
    else:
        counts = ingest_to_yaml(src, taxonomy_id, out)
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


def _resolve_mba_by_name(con: "sqlite3.Connection", name: str) -> list[str]:
    """Fallback: resolve an anatomical location name to MBA IDs by label matching.

    Used when a UBERON ID has no xref in the MBA ontology.  Tries direct
    substring match first, then applies Latin→English layer synonyms and
    hippocampal field prefix normalisation (e.g. "CA1 stratum pyramidale"
    → "Field CA1, pyramidal layer").
    """
    if not name:
        return []

    norm = name.lower().strip()

    # Latin→English layer synonyms (hippocampal nomenclature)
    _LAYER_SYNONYMS = {
        "stratum pyramidale": "pyramidal layer",
        "stratum moleculare": "molecular layer",
    }

    # 1. Direct substring match on MBA label (also try with commas/punctuation stripped)
    rows = con.execute(
        "SELECT anat_id FROM anat_terms WHERE LOWER(label) LIKE ?",
        (f"%{norm}%",),
    ).fetchall()
    if rows:
        return [r[0] for r in rows]

    # 1b. Try keyword match — all significant words must appear in the label
    words = [w for w in norm.split() if len(w) > 2]
    if len(words) >= 2:
        where = " AND ".join(["LOWER(label) LIKE ?"] * len(words))
        params = [f"%{w}%" for w in words]
        rows = con.execute(
            f"SELECT anat_id FROM anat_terms WHERE {where}", params
        ).fetchall()
        if rows:
            return [r[0] for r in rows]

    # 2. Apply Latin→English synonyms and retry
    norm_sub = norm
    for latin, english in _LAYER_SYNONYMS.items():
        if latin in norm:
            norm_sub = norm.replace(latin, english)
            break

    # 3. Normalise hippocampal field prefixes: "CA1 ..." → "Field CA1, ..."
    _FIELDS = {"ca1": "Field CA1", "ca2": "Field CA2", "ca3": "Field CA3"}
    for abbrev, mba_prefix in _FIELDS.items():
        if norm_sub.startswith(abbrev + " "):
            layer_part = norm_sub[len(abbrev) + 1:]
            pattern = f"{mba_prefix}%{layer_part}%"
            rows = con.execute(
                "SELECT anat_id FROM anat_terms WHERE LOWER(label) LIKE LOWER(?)",
                (pattern,),
            ).fetchall()
            if rows:
                return [r[0] for r in rows]
            break  # only one field prefix possible

    # 4. Try synonym-substituted name without field prefix
    if norm_sub != norm:
        rows = con.execute(
            "SELECT anat_id FROM anat_terms WHERE LOWER(label) LIKE ?",
            (f"%{norm_sub}%",),
        ).fetchall()
        if rows:
            return [r[0] for r in rows]

    return []


def _cmd_find_candidates(
    graph_file: str,
    node_id: str,
    taxonomy_id: str,
    rank: int = 1,
    top_n: int = 20,
) -> None:
    """Extract a classical node's property signature from a KB YAML file
    and query the taxonomy DB for candidate atlas matches at a given rank.

    Outputs a JSON candidate list to stdout.
    """
    from evidencell.paths import taxonomy_db_path

    graph_path = Path(graph_file)
    if not graph_path.exists():
        print(f"ERROR: graph file not found: {graph_path}", file=sys.stderr)
        sys.exit(1)

    db_path = taxonomy_db_path(taxonomy_id)
    if not db_path.exists():
        print(
            f"ERROR: DB not found at {db_path} — run: just build-taxonomy-db {taxonomy_id}",
            file=sys.stderr,
        )
        sys.exit(1)

    with graph_path.open(encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)

    # Find the classical node
    nodes = doc.get("nodes") or []
    classical = None
    for nd in nodes:
        if nd.get("id") == node_id:
            classical = nd
            break

    if classical is None:
        print(f"ERROR: node '{node_id}' not found in {graph_path}", file=sys.stderr)
        sys.exit(1)

    # Extract property signature
    markers: list[str] = []
    for m in classical.get("defining_markers") or []:
        sym = m.get("symbol") if isinstance(m, dict) else m
        if sym:
            markers.append(sym)

    nt_obj = classical.get("nt_type")
    nt_type: str | None = None
    if isinstance(nt_obj, dict):
        nt_type = nt_obj.get("name_in_source")
    elif isinstance(nt_obj, str):
        nt_type = nt_obj

    # Extract soma locations only (skip AXON_TARGET, DENDRITE)
    soma_locs: list[dict] = []
    anat_ids: list[str] = []
    for loc in classical.get("anatomical_location") or []:
        compartment = loc.get("compartment")
        if compartment in ("AXON_TARGET", "DENDRITE"):
            continue
        loc_id = loc.get("id")
        if loc_id:
            soma_locs.append(loc)
            anat_ids.append(loc_id)

    db = TaxonomyDB(db_path)

    # Resolve UBERON IDs to MBA IDs via anat_terms lookup, with name fallback
    mba_ids: list[str] = []
    with db._connect() as con:
        for loc in soma_locs:
            aid = loc["id"]
            if not aid.startswith("UBERON:"):
                mba_ids.append(aid)
                continue
            rows = con.execute(
                "SELECT anat_id, label FROM anat_terms WHERE uberon_id = ?", (aid,)
            ).fetchall()
            resolved = [r[0] for r in rows]
            # Sanity check: if the xref-resolved MBA label shares no keywords
            # with the source name, the xref is likely wrong (e.g. UBERON:0005383
            # "stratum oriens" → MBA:672 "Caudoputamen").  Prefer name fallback.
            name = loc.get("name_in_source") or loc.get("label") or ""
            if resolved and name:
                name_words = {w.lower() for w in name.split() if len(w) > 2}
                xref_label = rows[0][1].lower()
                xref_words = {w.strip(",") for w in xref_label.split() if len(w) > 2}
                if not (name_words & xref_words):
                    # No word overlap — likely wrong xref
                    fallback = _resolve_mba_by_name(con, name)
                    if fallback:
                        print(
                            f"  {aid} xref → {resolved} ({rows[0][1]}) — "
                            f"name mismatch with {name!r}, using name fallback: "
                            f"{fallback}",
                            file=sys.stderr,
                        )
                        resolved = fallback
                    else:
                        print(
                            f"  WARNING: {aid} xref → {resolved} ({rows[0][1]}) — "
                            f"name mismatch with {name!r}, but no name fallback found",
                            file=sys.stderr,
                        )
            if resolved:
                mba_ids.extend(resolved)
            else:
                # Fallback: resolve by name_in_source or label
                name = loc.get("name_in_source") or loc.get("label") or ""
                fallback = _resolve_mba_by_name(con, name)
                if fallback:
                    mba_ids.extend(fallback)
                    print(
                        f"  {aid} has no MBA xref — resolved by name: "
                        f"{name!r} → {fallback}",
                        file=sys.stderr,
                    )
                else:
                    print(
                        f"  WARNING: {aid} ({name}) has no MBA mapping — skipped",
                        file=sys.stderr,
                    )

    print(f"Classical node: {node_id} ({classical.get('name', '?')})", file=sys.stderr)
    print(f"  NT type: {nt_type}", file=sys.stderr)
    print(f"  Markers: {markers}", file=sys.stderr)
    print(f"  Soma locations: {anat_ids}", file=sys.stderr)
    if mba_ids != anat_ids:
        print(f"  Resolved MBA IDs: {mba_ids}", file=sys.stderr)
    print(f"  Query rank: {rank}", file=sys.stderr)
    print(f"  Taxonomy: {taxonomy_id}", file=sys.stderr)

    # Try transitive anatomy matching (requires anat_closure table from MBA ontology).
    # Fall back to no anatomy matching if closure not built.
    query_anat = mba_ids if mba_ids else None
    try:
        candidates = db.find_candidates(
            anat_root_ids=query_anat,
            nt_type=nt_type,
            markers=markers,
            rank=rank,
        )
    except RuntimeError as exc:
        if "anat_closure" in str(exc):
            print(
                "  WARNING: anat_closure table not built — anatomy matching disabled. "
                "Run: just fetch-mba-ontology && just build-anat-closure "
                f"{taxonomy_id}",
                file=sys.stderr,
            )
            candidates = db.find_candidates(
                nt_type=nt_type,
                markers=markers,
                rank=rank,
            )
        else:
            raise

    # Trim to top_n
    candidates = candidates[:top_n]

    # Output JSON
    output = {
        "classical_node_id": node_id,
        "classical_node_name": classical.get("name", ""),
        "taxonomy_id": taxonomy_id,
        "rank": rank,
        "n_candidates": len(candidates),
        "candidates": [
            {
                "node_id": c["node_id"],
                "label": c["label"],
                "taxonomy_level": c["taxonomy_level"],
                "taxonomy_rank": c.get("taxonomy_rank"),
                "score": c["_score"],
                "nt_type": c.get("nt_type"),
                "parent_id": c.get("parent_id"),
                **({"male_female_ratio": c["male_female_ratio"]}
                   if c.get("male_female_ratio") is not None else {}),
            }
            for c in candidates
        ],
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python -m evidencell.taxonomy_db ingest <source_json> <taxonomy_id>")
        print("  python -m evidencell.taxonomy_db build-db <taxonomy_id>")
        print("  python -m evidencell.taxonomy_db show-meta <taxonomy_id>")
        print("  python -m evidencell.taxonomy_db sync-mapmycells-paths <taxonomy_id>")
        print("  python -m evidencell.taxonomy_db fetch-mba <dest_path>")
        print("  python -m evidencell.taxonomy_db build-closure <taxonomy_id> <mba_json>")
        print("  python -m evidencell.taxonomy_db find-candidates <graph_file> <node_id> <taxonomy_id> [rank] [top_n]")
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
    elif cmd == "find-candidates" and len(sys.argv) >= 5:
        _rank = int(sys.argv[5]) if len(sys.argv) > 5 else 1
        _top_n = int(sys.argv[6]) if len(sys.argv) > 6 else 20
        _cmd_find_candidates(sys.argv[2], sys.argv[3], sys.argv[4], _rank, _top_n)
    else:
        print(f"Unknown command or wrong arguments: {sys.argv[1:]}")
        sys.exit(1)
