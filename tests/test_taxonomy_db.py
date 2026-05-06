"""Tests for taxonomy_db module.

Tier: fast (uses test_single_row.json fixture; no network/OAK).
Full WMBv1 ingest test is marked @pytest.mark.slow (just test only).
"""

import json
import sqlite3
from pathlib import Path

import pytest
import yaml

from evidencell.taxonomy_db import (
    MapMyCellsMeta,
    TaxonomyDB,
    TaxonomyMeta,
    clean_taxonomy_json,
    ingest_cas_to_yaml,
    ingest_to_yaml,
    iter_taxonomy_rows,
    read_taxonomy_meta,
    _SCHEMA_HASH,
    _expression_score,
    _neg_expression_score,
    _freshness_at,
    _is_cas_format,
    _meta_to_dict,
)

FIXTURE_DIR = Path(__file__).parent.parent / "inputs" / "taxonomies"
SINGLE_ROW = FIXTURE_DIR / "test_single_row.json"
CAS_FIXTURE = FIXTURE_DIR / "test_cas_fixture.json"


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


def test_anat_multi_source_expansion(tmp_path):
    """A merged-edge anat entry with parallel cell_count/source lists expands
    into one AnatomicalLocation per source, each with its own count and a
    single PropertySource carrying the DOI."""
    yao = "https://doi.org/10.1038/s41586-023-06808-9"
    zhuang = "https://doi.org/10.1038/s41586-023-06812-z"
    fixture = [{
        "cl": None,
        "node": {
            "labels": ["CCN20230722_cluster", "Individual"],
            "properties": {
                "curie": "WMB:CS20230722_CLUS_TEST",
                "short_form": "CS20230722_CLUS_TEST",
                "label": "TEST cluster",
            },
        },
        "parent_curie": None,
        "level": "CCN20230722_cluster",
        "anat": [
            {
                "anat_id": "MBA:133",
                "anat_label": "Periventricular preoptic",
                "cell_count": [135, 1],
                "cell_ratio": [0.6, 0.2],
                "source": [yao, zhuang],
            },
            {
                "anat_id": "MBA:515",
                "anat_label": "Medial preoptic",
                "cell_count": [26],
                "cell_ratio": [0.115556],
                "source": [yao],
            },
        ],
    }]
    src = tmp_path / "merged.json"
    src.write_text(json.dumps(fixture))
    out = tmp_path / "out"
    out.mkdir()
    ingest_to_yaml(src, "TEST_MERGED", out)
    cluster_yaml = yaml.safe_load((out / "CCN20230722_cluster.yaml").read_text())
    node = cluster_yaml["nodes"][0]
    anat = node["anatomical_location"]
    by_region: dict[str, list[dict]] = {}
    for loc in anat:
        by_region.setdefault(loc["id"], []).append(loc)
    # MBA:133 expands into two entries (Yao + Zhuang); order matches input.
    pvpo = by_region["MBA:133"]
    assert len(pvpo) == 2
    assert pvpo[0]["cell_count"] == 135
    assert pvpo[0]["sources"][0]["ref"] == yao
    assert pvpo[0]["sources"][0]["method"] == "MERFISH (Yao 2024)"
    assert pvpo[1]["cell_count"] == 1
    assert pvpo[1]["sources"][0]["ref"] == zhuang
    assert pvpo[1]["sources"][0]["method"] == "MERFISH (Zhuang 2023)"
    # Single-source region stays as one entry.
    mpo = by_region["MBA:515"]
    assert len(mpo) == 1
    assert mpo[0]["cell_count"] == 26
    assert mpo[0]["sources"][0]["ref"] == yao


def test_ingest_to_yaml_idempotent(tmp_path):
    counts1 = ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    counts2 = ingest_to_yaml(SINGLE_ROW, "TEST_TAX", tmp_path)
    assert counts1 == counts2


# ── CAS-format ingest ────────────────────────────────────────────────────────


def test_is_cas_format_detection():
    """_is_cas_format correctly identifies CAS vs VFB graph export."""
    cas = {"annotations": [], "labelsets": []}
    assert _is_cas_format(cas) is True
    vfb = [{"wmb": {}, "cl": None}]
    assert _is_cas_format(vfb) is False
    assert _is_cas_format({"annotations": []}) is False  # missing labelsets


def test_cas_ingest_creates_files(tmp_path):
    counts = ingest_cas_to_yaml(CAS_FIXTURE, "TEST_CAS", tmp_path)
    assert sum(counts.values()) == 4  # 1 class + 1 subclass + 2 clusters
    assert (tmp_path / "taxonomy_meta.yaml").exists()
    assert (tmp_path / "cluster.yaml").exists()
    assert (tmp_path / "subclass.yaml").exists()
    assert (tmp_path / "class.yaml").exists()


def test_cas_ingest_meta(tmp_path):
    ingest_cas_to_yaml(CAS_FIXTURE, "TEST_CAS", tmp_path)
    meta = yaml.safe_load((tmp_path / "taxonomy_meta.yaml").read_text())
    assert meta["taxonomy_id"] == "TEST_CAS"
    assert meta["source_file"] == "test_cas_fixture.json"
    assert meta["level_counts"]["CLUSTER"] == 2
    assert meta["level_counts"]["SUBCLASS"] == 1
    assert meta["level_counts"]["CLASS"] == 1
    # CAS ingest picks up title as taxonomy_name when no meta input
    assert meta["taxonomy_name"] == "Test CAS Taxonomy"


def test_cas_ingest_node_fields(tmp_path):
    ingest_cas_to_yaml(CAS_FIXTURE, "TEST_CAS", tmp_path)
    data = yaml.safe_load((tmp_path / "cluster.yaml").read_text())
    assert data["taxonomy_level"] == "CLUSTER"
    assert data["taxonomy_rank"] == 0
    nodes = data["nodes"]
    assert len(nodes) == 2
    node = nodes[0]  # sorted by accession
    assert node["cell_set_accession"].startswith("TEST_CAS_")
    assert node["taxonomy_level"] == "CLUSTER"
    assert node["taxonomy_rank"] == 0
    assert node["definition_basis"] == "ATLAS_TRANSCRIPTOMIC"
    assert node["is_terminal"] is True


def test_cas_ingest_parent_hierarchy(tmp_path):
    ingest_cas_to_yaml(CAS_FIXTURE, "TEST_CAS", tmp_path)
    data = yaml.safe_load((tmp_path / "cluster.yaml").read_text())
    node = data["nodes"][0]
    ph = node.get("parent_hierarchy", [])
    assert len(ph) == 1
    assert ph[0]["level"] == "SUBCLASS"
    assert ph[0]["name"] == "Sst"
    assert ph[0]["cell_set_accession"] == "TEST_CAS_444"


def test_cas_ingest_rationale_dois(tmp_path):
    ingest_cas_to_yaml(CAS_FIXTURE, "TEST_CAS", tmp_path)
    data = yaml.safe_load((tmp_path / "cluster.yaml").read_text())
    node = data["nodes"][0]
    assert "rationale_dois" in node
    assert "https://doi.org/10.1016/j.cell.2021.04.021" in node["rationale_dois"]


def test_cas_ingest_designation(tmp_path):
    ingest_cas_to_yaml(CAS_FIXTURE, "TEST_CAS", tmp_path)
    data = yaml.safe_load((tmp_path / "cluster.yaml").read_text())
    node = data["nodes"][0]
    assert "cell_set_designation" in node


def test_cas_ingest_idempotent(tmp_path):
    counts1 = ingest_cas_to_yaml(CAS_FIXTURE, "TEST_CAS", tmp_path)
    counts2 = ingest_cas_to_yaml(CAS_FIXTURE, "TEST_CAS", tmp_path)
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


def test_taxonomy_db_get_node_by_accession(populated_db):
    db, _, _ = populated_db
    # Pick any real node and round-trip its accession both ways (bare and CURIE)
    with db._connect() as con:
        row = con.execute(
            "SELECT node_id, short_form, label FROM nodes LIMIT 1"
        ).fetchone()
    assert row is not None
    full = row["node_id"]
    bare = row["short_form"]
    by_full = db.get_node_by_accession(full)
    by_bare = db.get_node_by_accession(bare)
    assert by_full is not None and by_bare is not None
    assert by_full["short_form"] == bare
    assert by_bare["node_id"] == full
    assert db.get_node_by_accession("WMB:does_not_exist") is None
    assert db.get_node_by_accession("") is None


def test_taxonomy_db_get_parent_hierarchy(populated_db):
    db, _, _ = populated_db
    with db._connect() as con:
        row = con.execute(
            "SELECT short_form FROM nodes WHERE parent_id IS NOT NULL LIMIT 1"
        ).fetchone()
    if row is None:
        pytest.skip("Fixture has no nodes with a parent")
    chain = db.get_parent_hierarchy(row["short_form"])
    # Chain may be empty when the named parent is missing from the DB (single-
    # row fixtures); when present, every entry must carry the canonical keys.
    assert isinstance(chain, list)
    for entry in chain:
        assert {"level", "name", "cell_set_accession"} <= entry.keys()
    # Unknown accession produces empty chain, not an error
    assert db.get_parent_hierarchy("WMB:does_not_exist") == []


def test_taxonomy_db_find_candidates_empty(populated_db):
    db, _, _ = populated_db
    results = db.find_candidates(anat_ids=["MBA:99999999"], level="cluster")
    assert isinstance(results, list)


def test_taxonomy_db_find_candidates_scores(populated_db):
    db, _, _ = populated_db
    # Any matches should have _score > 0 (use level= for backward compat with test fixtures)
    all_nodes = db.find_candidates(level="cluster")
    for nd in all_nodes:
        assert "_score" not in nd or nd["_score"] >= 0


def test_taxonomy_db_find_candidates_requires_rank_or_level(populated_db):
    db, _, _ = populated_db
    with pytest.raises(ValueError, match="Either rank or level"):
        db.find_candidates()


# ── Expression scoring helpers (#34) ─────────────────────────────────────────

def test_expression_score_thresholds():
    assert _expression_score(10.0) == 2   # high
    assert _expression_score(5.0) == 2    # boundary
    assert _expression_score(2.5) == 1    # moderate
    assert _expression_score(1.0) == 1    # boundary
    assert _expression_score(0.5) == 0    # scattered
    assert _expression_score(0.1) == 0    # boundary
    assert _expression_score(0.05) == -2  # absent
    assert _expression_score(0.0) == -2   # absent


def test_neg_expression_score_inverts():
    assert _neg_expression_score(10.0) == -2
    assert _neg_expression_score(2.5) == -1
    assert _neg_expression_score(0.5) == 0
    assert _neg_expression_score(0.0) == 2  # absent → confirms expectation


def test_find_candidates_expression_scoring(populated_db):
    """Expression data boosts candidates with high expression of queried markers."""
    db, _, _ = populated_db

    # Use level= to avoid needing rank in test fixture
    # No expression data → binary +1 per marker
    binary_results = db.find_candidates(
        markers=["Sst"],
        level="cluster",
    )

    # Build expression data: node 1 has Sst=8.0 (high), node 2 has Sst=0.0 (absent)
    # Extract node IDs from the DB
    import sqlite3
    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute("SELECT node_id FROM nodes WHERE taxonomy_level='cluster' ORDER BY node_id").fetchall()
    node_ids = [r["node_id"] for r in rows]

    expr = {}
    if len(node_ids) >= 2:
        expr[node_ids[0]] = {"Sst": 8.0}   # high → +2
        expr[node_ids[1]] = {"Sst": 0.0}   # absent → −2

    expr_results = db.find_candidates(
        markers=["Sst"],
        level="cluster",
        expression_data=expr,
    )

    # If expression data is provided and node_ids[0] has Sst=8.0, its score should be 2
    # instead of 1 (binary), and node_ids[1] with Sst=0.0 should score −2 (filtered by score>0)
    if len(node_ids) >= 2 and expr:
        high_expr_node = next((c for c in expr_results if c["node_id"] == node_ids[0]), None)
        absent_node = next((c for c in expr_results if c["node_id"] == node_ids[1]), None)
        if high_expr_node:
            assert high_expr_node["_score"] == 2  # +2 for high expression
        if absent_node:
            assert absent_node["_score"] == -2  # −2 for absent defining marker


def test_find_candidates_negative_markers_penalise(populated_db):
    """Candidates with high expression of negative markers are penalised."""
    db, _, _ = populated_db

    import sqlite3
    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute("SELECT node_id FROM nodes WHERE taxonomy_level='cluster' ORDER BY node_id").fetchall()
    node_ids = [r["node_id"] for r in rows]

    if not node_ids:
        return

    # Node with high expression of a negative marker → penalty
    expr = {node_ids[0]: {"Pvalb": 9.0}}
    results = db.find_candidates(
        markers=["Sst"],
        negative_markers=["Pvalb"],
        level="cluster",
        expression_data=expr,
    )
    # Sst not in expr → binary +1 if in marker columns (falls back); Pvalb=9.0 → −2
    node_result = next((c for c in results if c["node_id"] == node_ids[0]), None)
    # Score should include the −2 penalty from Pvalb
    if node_result:
        # Check penalty is applied: negative marker in expr → _neg_expression_score(9.0) = -2
        assert node_result["_score"] <= -1  # at most +1 (binary Sst) − 2 (Pvalb penalty)


# ── TaxonomyMeta ──────────────────────────────────────────────────────────────

def test_taxonomy_meta_round_trip(tmp_path):
    """TaxonomyMeta → dict → YAML → read_taxonomy_meta round-trip."""
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
        yaml.dump(_meta_to_dict(meta), allow_unicode=True, sort_keys=False),
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
    import evidencell.paths as _paths

    # Create a fake meta input at the expected path
    meta_input_dir = tmp_path / "inputs" / "taxonomies"
    meta_input_dir.mkdir(parents=True)
    (meta_input_dir / "TEST_TAX_meta.yaml").write_text(
        yaml.dump({
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
    meta = yaml.safe_load((tmp_path / "taxonomy_meta.yaml").read_text())
    assert meta["taxonomy_name"] == "Test Tax"
    assert meta["species_id"] == "NCBITaxon:10090"
    assert meta["anatomy_ontology"] == "MBA"
    assert "level_counts" in meta
    assert sum(meta["level_counts"].values()) == sum(counts.values())


@pytest.mark.slow
def test_full_wmbv1_ingest(tmp_path):
    """Full ingest of WMBv1 source JSON — slow, only in just test.

    Prefers the post-2026-04 KG export `CCN20230722.json` when present (current
    source of record) and falls back to the legacy `wmbv1_full.json` for
    backwards-compat verification.
    """
    new_source = FIXTURE_DIR / "CCN20230722.json"
    legacy_source = FIXTURE_DIR / "wmbv1_full.json"
    if new_source.exists():
        source = new_source
    elif legacy_source.exists():
        source = legacy_source
    else:
        pytest.skip("Neither CCN20230722.json nor wmbv1_full.json present")
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
    hipp_gaba = db.find_candidates(anat_ids=["MBA:399"], nt_type="GABA", level="cluster")
    assert len(hipp_gaba) > 0
    assert all(nd["_score"] > 0 for nd in hipp_gaba)

    # male_female_ratio: most clusters should have values; check YAML + DB round-trip
    nodes_with_ratio = [n for n in cluster_yaml["nodes"] if n.get("male_female_ratio") is not None]
    assert len(nodes_with_ratio) > 5000  # 5317 expected
    with db._connect() as con:
        db_count = con.execute(
            "SELECT COUNT(*) FROM nodes WHERE male_female_ratio IS NOT NULL"
        ).fetchone()[0]
    assert db_count > 5000

    # Parent-hierarchy walk on a cluster: should reach SUPERTYPE -> SUBCLASS ->
    # CLASS (real WMBv1 hierarchy). Pick any cluster with a parent_id.
    with db._connect() as con:
        cl_row = con.execute(
            "SELECT short_form FROM nodes "
            "WHERE taxonomy_level='cluster' AND parent_id IS NOT NULL LIMIT 1"
        ).fetchone()
    if cl_row is not None:
        chain = db.get_parent_hierarchy(cl_row["short_form"])
        levels = [(e.get("level") or "").upper() for e in chain]
        assert "SUPERTYPE" in levels
        assert "SUBCLASS" in levels
        assert "CLASS" in levels

    # n_cells (10x per-node count): present on the new KG export only.
    # The legacy wmbv1_full.json predates the cell_count property — skip the
    # assertion when the legacy file is the source.
    if source == new_source:
        nodes_with_n_cells = [
            n for n in cluster_yaml["nodes"] if n.get("n_cells") is not None
        ]
        assert len(nodes_with_n_cells) > 5000  # 5235 expected
        assert all(isinstance(n["n_cells"], int) and n["n_cells"] > 0
                   for n in nodes_with_n_cells)
        with db._connect() as con:
            db_n_cells_count = con.execute(
                "SELECT COUNT(*) FROM nodes WHERE n_cells IS NOT NULL"
            ).fetchone()[0]
        assert db_n_cells_count > 6000  # ~6777 across all levels expected


# ── Freshness check (DB staleness detection) ──────────────────────────────────

def test_freshness_fresh_db(populated_db):
    """A freshly-built DB is fresh; reasons list is empty."""
    db, tmp_path, _ = populated_db
    stale, reasons = _freshness_at(db.db_path, tmp_path)
    assert stale is False
    assert reasons == []


def test_freshness_missing_db(tmp_path):
    """A missing DB is reported stale with a single reason."""
    stale, reasons = _freshness_at(tmp_path / "no.db", tmp_path)
    assert stale is True
    assert len(reasons) == 1
    assert "DB not found" in reasons[0]


def test_freshness_missing_schema_hash(populated_db):
    """A DB built before staleness tracking has no schema_hash row → stale."""
    db, tmp_path, _ = populated_db
    con = sqlite3.connect(db.db_path)
    try:
        con.execute("DELETE FROM _meta WHERE key = 'schema_hash'")
        con.commit()
    finally:
        con.close()
    stale, reasons = _freshness_at(db.db_path, tmp_path)
    assert stale is True
    assert any("lacks _meta.schema_hash" in r for r in reasons)


def test_freshness_schema_hash_mismatch(populated_db):
    """A DB built against a different schema (older or experimental) → stale."""
    db, tmp_path, _ = populated_db
    con = sqlite3.connect(db.db_path)
    try:
        con.execute(
            "UPDATE _meta SET value = 'badhash0badhash0' WHERE key = 'schema_hash'"
        )
        con.commit()
    finally:
        con.close()
    stale, reasons = _freshness_at(db.db_path, tmp_path)
    assert stale is True
    assert any("schema_hash mismatch" in r for r in reasons)
    # Both the stored truncation AND the current truncation appear in the message
    assert any(_SCHEMA_HASH[:8] in r for r in reasons)


def test_freshness_yaml_newer_than_db(populated_db):
    """A YAML file edited after the DB was built → stale."""
    import os
    import time
    db, tmp_path, _ = populated_db
    # Touch a YAML file with a future mtime (cleanly newer than db.db_path)
    yaml_files = list(tmp_path.glob("*.yaml"))
    assert yaml_files, "fixture should have produced YAML files"
    target = yaml_files[0]
    future = time.time() + 60
    os.utime(target, (future, future))
    stale, reasons = _freshness_at(db.db_path, tmp_path)
    assert stale is True
    assert any("YAML newer than DB" in r for r in reasons)


def test_freshness_recovers_after_rebuild(populated_db):
    """Rebuilding the DB after a schema_hash corruption refreshes the hash."""
    db, tmp_path, _ = populated_db
    con = sqlite3.connect(db.db_path)
    try:
        con.execute(
            "UPDATE _meta SET value = 'corrupt0corrupt0' WHERE key = 'schema_hash'"
        )
        con.commit()
    finally:
        con.close()
    assert _freshness_at(db.db_path, tmp_path)[0] is True  # stale
    db.build_from_yaml(tmp_path)
    stale, reasons = _freshness_at(db.db_path, tmp_path)
    assert stale is False, f"expected fresh after rebuild, got reasons={reasons}"
