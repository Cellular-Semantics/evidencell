"""Tests for taxonomy_db module.

Tier: fast (uses test_single_row.json fixture; no network/OAK).
Full WMBv1 ingest test is marked @pytest.mark.slow (just test only).
"""

import json
import sqlite3
import tempfile
from pathlib import Path

import pytest
import yaml

from evidencell.taxonomy_db import (
    MapMyCellsMeta,
    TaxonomyDB,
    TaxonomyMeta,
    clean_taxonomy_json,
    ingest_to_yaml,
    iter_taxonomy_rows,
    read_taxonomy_meta,
    _meta_to_dict,
)

FIXTURE_DIR = Path(__file__).parent.parent / "inputs" / "taxonomies"
SINGLE_ROW = FIXTURE_DIR / "test_single_row.json"


# ── clean_taxonomy_json ────────────────────────────────────────────────────────

def test_clean_json_bom(tmp_path):
    f = tmp_path / "bom.json"
    f.write_bytes(b"\xef\xbb\xbf[]")
    assert clean_taxonomy_json(f) == b"[]"


def test_clean_json_no_bom(tmp_path):
    f = tmp_path / "nobom.json"
    f.write_bytes(b"[]")
    assert clean_taxonomy_json(f) == b"[]"


def test_clean_json_newline_in_string(tmp_path):
    # Literal newline inside a JSON string value
    raw = b'[{"key": "line1\nline2"}]'
    f = tmp_path / "newline.json"
    f.write_bytes(raw)
    cleaned = clean_taxonomy_json(f)
    parsed = json.loads(cleaned)
    assert parsed[0]["key"] == "line1\nline2"


def test_clean_json_double_escape(tmp_path):
    # \\" in source should become \" (escaped quote)
    raw = b'[{"key": "say \\\\"hello\\\\""}]'
    f = tmp_path / "dquote.json"
    f.write_bytes(raw)
    cleaned = clean_taxonomy_json(f)
    parsed = json.loads(cleaned)
    assert '"hello"' in parsed[0]["key"]


# ── iter_taxonomy_rows ─────────────────────────────────────────────────────────

def test_iter_rows_single_row():
    cleaned = clean_taxonomy_json(SINGLE_ROW)
    rows = list(iter_taxonomy_rows(cleaned))
    assert len(rows) == 1


def test_iter_rows_top_level_keys():
    cleaned = clean_taxonomy_json(SINGLE_ROW)
    row = next(iter_taxonomy_rows(cleaned))
    # Canonical format uses 'node'; WMBv1 legacy uses 'wmb' (handled via row_keys)
    assert "node" in row or "wmb" in row


# ── ingest_to_yaml ─────────────────────────────────────────────────────────────

def test_ingest_to_yaml_creates_files(tmp_path):
    counts = ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    assert sum(counts.values()) > 0
    yaml_files = list(tmp_path.glob("*.yaml"))
    assert len(yaml_files) >= 1
    assert (tmp_path / "taxonomy_meta.yaml").exists()


def test_ingest_to_yaml_meta(tmp_path):
    ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    meta = yaml.safe_load((tmp_path / "taxonomy_meta.yaml").read_text())
    assert meta["taxonomy_id"] == "TEST_TAX"
    assert meta["source_file"] == SINGLE_ROW.name
    assert "level_counts" in meta


def test_ingest_to_yaml_node_fields(tmp_path):
    ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    for f in tmp_path.glob("*.yaml"):
        if f.name == "taxonomy_meta.yaml":
            continue
        data = yaml.safe_load(f.read_text())
        # New format: TaxonomyNodeList wrapper
        assert isinstance(data, dict), "expected TaxonomyNodeList dict"
        assert "nodes" in data
        nodes = data["nodes"]
        assert len(nodes) > 0
        node = nodes[0]
        assert "id" in node
        assert "name" in node
        assert "taxonomy_level" in node
        assert "definition_basis" in node
        assert node["definition_basis"] == "ATLAS_TRANSCRIPTOMIC"
        break


def test_markers_by_category(tmp_path):
    """Unified markers list has entries for each category present in fixture."""
    ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    for f in tmp_path.glob("*.yaml"):
        if f.name == "taxonomy_meta.yaml":
            continue
        data = yaml.safe_load(f.read_text())
        node = data["nodes"][0]
        markers = node.get("markers", [])
        categories = {m["category"] for m in markers}
        # Fixture has all five marker types
        assert "DEFINING" in categories
        assert "DEFINING_SCOPED" in categories
        assert "TF" in categories
        assert "MERFISH" in categories
        assert "NEUROPEPTIDE" in categories
        # NEUROPEPTIDE entries carry expression_score
        np_entries = [m for m in markers if m["category"] == "NEUROPEPTIDE"]
        assert all("expression_score" in m for m in np_entries)
        assert any(m["symbol"] == "Grp" and abs(m["expression_score"] - 7.5) < 0.01 for m in np_entries)
        break


def test_anat_cell_count(tmp_path):
    """anatomical_location entries carry cell_count and compartment: SOMA."""
    ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    for f in tmp_path.glob("*.yaml"):
        if f.name == "taxonomy_meta.yaml":
            continue
        data = yaml.safe_load(f.read_text())
        node = data["nodes"][0]
        anat = node.get("anatomical_location", [])
        assert len(anat) >= 1
        loc = anat[0]
        assert loc["id"] == "MBA:512"
        assert loc["cell_count"] == 142
        assert loc["compartment"] == "SOMA"
        break


def test_ingest_to_yaml_idempotent(tmp_path):
    counts1 = ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    counts2 = ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    assert counts1 == counts2


# ── TaxonomyDB ────────────────────────────────────────────────────────────────

@pytest.fixture()
def populated_db(tmp_path):
    counts = ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    db_path = tmp_path / "TEST_TAX.db"
    db = TaxonomyDB(db_path)
    db.build_from_yaml(tmp_path)
    return db, tmp_path, counts


def test_taxonomy_db_builds(populated_db):
    db, tmp_path, _ = populated_db
    assert db.db_path.exists()
    con = sqlite3.connect(db.db_path)
    n = con.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
    con.close()
    assert n > 0


def test_taxonomy_db_rebuild_idempotent(populated_db):
    db, tmp_path, _ = populated_db
    con = sqlite3.connect(db.db_path)
    n_before = con.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
    con.close()
    db.build_from_yaml(tmp_path)
    con = sqlite3.connect(db.db_path)
    n_after = con.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
    con.close()
    assert n_before == n_after


def test_taxonomy_db_query_by_cl(populated_db):
    db, _, _ = populated_db
    # query_by_cl with a non-existent term should return empty, not error
    results = db.query_by_cl("CL:9999999")
    assert isinstance(results, list)


def test_taxonomy_db_find_candidates_empty(populated_db):
    db, _, _ = populated_db
    results = db.find_candidates(anat_ids=["MBA:99999999"])
    assert isinstance(results, list)


def test_taxonomy_db_find_candidates_scores(populated_db):
    db, _, _ = populated_db
    # Any matches should have _score > 0
    all_nodes = db.find_candidates()
    for nd in all_nodes:
        assert "_score" not in nd or nd["_score"] >= 0


# ── TaxonomyMeta ──────────────────────────────────────────────────────────────

def test_taxonomy_meta_round_trip(tmp_path):
    """TaxonomyMeta → dict → YAML → read_taxonomy_meta round-trip."""
    import yaml as _yaml
    from evidencell.taxonomy_db import _meta_to_dict, read_taxonomy_meta, TaxonomyMeta, MapMyCellsMeta

    meta = TaxonomyMeta(
        taxonomy_id="TEST123",
        taxonomy_name="Test Taxonomy",
        species_id="NCBITaxon:10090",
        species_label="Mus musculus",
        tissue_id="UBERON:0000955",
        tissue_label="brain",
        anatomy_ontology="MBA",
        source_query="inputs/taxonomies/TEST123.cypher",
        ingest_date="2026-01-01",
        level_counts={"cluster": 10, "supertype": 3},
        mapmycells=MapMyCellsMeta(
            at_taxonomy_id="TEST123",
            stats_s3_url="https://example.com/stats.h5",
        ),
    )
    # Write to tmp taxonomy_meta.yaml
    tax_dir = tmp_path / "TEST123"
    tax_dir.mkdir()
    meta_path = tax_dir / "taxonomy_meta.yaml"
    meta_path.write_text(
        _yaml.dump(_meta_to_dict(meta), allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )

    # Patch taxonomy_dir to point at tmp_path
    import evidencell.paths as _paths
    orig_taxonomy_dir = _paths.taxonomy_dir

    def _mock_taxonomy_dir(tid):
        return tmp_path / tid

    _paths.taxonomy_dir = _mock_taxonomy_dir
    try:
        loaded = read_taxonomy_meta("TEST123")
    finally:
        _paths.taxonomy_dir = orig_taxonomy_dir

    assert loaded.taxonomy_id == "TEST123"
    assert loaded.taxonomy_name == "Test Taxonomy"
    assert loaded.species_id == "NCBITaxon:10090"
    assert loaded.tissue_label == "brain"
    assert loaded.anatomy_ontology == "MBA"
    assert loaded.level_counts == {"cluster": 10, "supertype": 3}
    assert loaded.mapmycells.at_taxonomy_id == "TEST123"
    assert loaded.mapmycells.stats_s3_url == "https://example.com/stats.h5"
    assert loaded.mapmycells.local_stats_path is None


def test_ingest_to_yaml_writes_enriched_meta(tmp_path, monkeypatch):
    """ingest_to_yaml reads meta input and writes enriched taxonomy_meta.yaml."""
    import yaml as _yaml
    import evidencell.paths as _paths

    # Create a fake meta input at the expected path
    meta_input_dir = tmp_path / "inputs" / "taxonomies"
    meta_input_dir.mkdir(parents=True)
    (meta_input_dir / "TEST_TAX_meta.yaml").write_text(
        _yaml.dump({
            "taxonomy_name": "Test Tax",
            "species_id": "NCBITaxon:10090",
            "species_label": "Mus musculus",
            "anatomy_ontology": "MBA",
        }),
        encoding="utf-8",
    )

    # Monkeypatch taxonomy_meta_input_path to return our tmp path
    monkeypatch.setattr(
        _paths, "taxonomy_meta_input_path",
        lambda tid: meta_input_dir / f"{tid}_meta.yaml",
    )

    counts = ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    meta = _yaml.safe_load((tmp_path / "taxonomy_meta.yaml").read_text())
    assert meta["taxonomy_name"] == "Test Tax"
    assert meta["species_id"] == "NCBITaxon:10090"
    assert meta["anatomy_ontology"] == "MBA"
    assert "level_counts" in meta
    assert sum(meta["level_counts"].values()) == sum(counts.values())


@pytest.mark.slow
def test_full_wmbv1_ingest(tmp_path):
    """Full ingest of wmbv1_full.json — slow, only in just test."""
    source = FIXTURE_DIR / "wmbv1_full.json"
    if not source.exists():
        pytest.skip("wmbv1_full.json not present")
    counts = ingest_to_yaml(source, "CCN20230722", tmp_path)
    assert counts.get("cluster", 0) == 5322
    assert counts.get("supertype", 0) == 1201
    assert counts.get("subclass", 0) == 338
    assert counts.get("class", 0) == 34
    assert counts.get("neurotransmitter", 0) == 10

    # Verify TaxonomyNodeList format
    cluster_yaml = yaml.safe_load((tmp_path / "cluster.yaml").read_text())
    assert isinstance(cluster_yaml, dict)
    assert cluster_yaml["taxonomy_level"] == "CLUSTER"
    assert len(cluster_yaml["nodes"]) == 5322

    db_path = tmp_path / "CCN20230722.db"
    db = TaxonomyDB(db_path)
    db.build_from_yaml(tmp_path)

    # Lugaro cell should have CL mapping (node_id stored as bare accession)
    lugaro = db.query_by_cl("CL:0011006")
    assert len(lugaro) >= 1
    assert any("1145" in nd["label"] for nd in lugaro)

    # Hippocampus GABA query
    hipp_gaba = db.find_candidates(anat_ids=["MBA:399"], nt_type="GABA")
    assert len(hipp_gaba) > 0
    assert all(nd["_score"] > 0 for nd in hipp_gaba)
