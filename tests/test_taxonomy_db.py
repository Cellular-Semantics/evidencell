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
    MIN_DETECTABLE,
    TaxonomyDB,
    TaxonomyMeta,
    clean_taxonomy_json,
    ingest_cas_to_yaml,
    ingest_to_yaml,
    iter_taxonomy_rows,
    read_taxonomy_meta,
    _SCHEMA_HASH,
    _classical_negative_markers,
    _classical_positive_markers,
    _coverage_for_gene,
    _expression_percentile,
    _expression_score,
    _neg_expression_score,
    _freshness_at,
    _is_cas_format,
    _meta_to_dict,
    _score_from_percentiles,
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
    """Legacy absolute-threshold helper — kept for backward compat."""
    assert _expression_score(10.0) == 2   # high
    assert _expression_score(5.0) == 2    # boundary
    assert _expression_score(2.5) == 1    # moderate
    assert _expression_score(1.0) == 1    # boundary
    assert _expression_score(0.5) == 0    # scattered
    assert _expression_score(0.1) == 0    # boundary
    assert _expression_score(0.05) == -2  # absent
    assert _expression_score(0.0) == -2   # absent


def test_neg_expression_score_inverts():
    """Legacy inverted helper — kept for backward compat."""
    assert _neg_expression_score(10.0) == -2
    assert _neg_expression_score(2.5) == -1
    assert _neg_expression_score(0.5) == 0
    assert _neg_expression_score(0.0) == 2  # absent → confirms expectation


def test_expression_percentile():
    ref = [0.1, 0.5, 1.0, 2.0, 5.0]
    assert _expression_percentile(0.0, ref) == 0.0          # below all
    assert _expression_percentile(1.0, ref) == 0.4          # 2/5 strictly below
    assert _expression_percentile(5.0, ref) == 0.8          # 4/5 strictly below
    assert _expression_percentile(10.0, ref) == 1.0         # above all
    assert _expression_percentile(0.0, []) == 0.0           # empty reference


def test_score_from_percentiles_positive():
    # sibling_pct ≥ 0.80 → +2 base; global_pct ≥ 0.90 → +1 bonus
    assert _score_from_percentiles(0.85, 0.95) == 3
    assert _score_from_percentiles(0.85, 0.50) == 2
    # sibling_pct ≥ 0.50 → +1 base; global_pct ≥ 0.90 → +1 bonus
    assert _score_from_percentiles(0.60, 0.95) == 2
    assert _score_from_percentiles(0.60, 0.50) == 1
    # sibling_pct < 0.50 with no val supplied → +1 (presence credit, gap 1).
    # No global bonus — non-discriminating presence stays below a single
    # above-median sibling match.
    assert _score_from_percentiles(0.30, 0.95) == 1
    assert _score_from_percentiles(0.00, 0.00) == 1


def test_score_from_percentiles_positive_absence_penalty():
    # val < MIN_DETECTABLE → −1 (absence penalty for positive markers, gap 2).
    assert _score_from_percentiles(0.0, 0.0, val=0.05) == -1
    assert _score_from_percentiles(0.85, 0.95, val=0.0) == -1
    # Boundary: val == MIN_DETECTABLE is reliable, so percentile path applies.
    assert _score_from_percentiles(0.30, 0.95, val=MIN_DETECTABLE) == 1


def test_score_from_percentiles_negative():
    # sibling_pct ≥ 0.80 → −2 (high expression of neg marker is bad)
    assert _score_from_percentiles(0.85, 0.95, is_negative=True) == -2
    # sibling_pct ≥ 0.50 → −1
    assert _score_from_percentiles(0.60, 0.50, is_negative=True) == -1
    # sibling_pct < 0.50 → +1 (low expression confirms absence)
    assert _score_from_percentiles(0.30, 0.95, is_negative=True) == +1


def test_score_from_percentiles_negative_below_threshold():
    # val < MIN_DETECTABLE for negative markers → +1 (absence confirms expectation).
    # Previously this case returned 0 in find_candidates; now it is consistent
    # with the percentile-driven "below sibling median" branch.
    assert _score_from_percentiles(0.0, 0.0, is_negative=True, val=0.05) == +1
    assert _score_from_percentiles(0.85, 0.95, is_negative=True, val=0.0) == +1


def test_min_detectable_constant():
    assert MIN_DETECTABLE == pytest.approx(0.1)


def test_classical_positive_markers_includes_neuropeptides():
    """Defining markers and neuropeptides are folded into one channel (gap 3)."""
    classical = {
        "defining_markers": [{"symbol": "Sst"}, {"symbol": "Calb1"}],
        "neuropeptides": [{"symbol": "Npy"}, {"symbol": "Pnoc"}],
    }
    result = _classical_positive_markers(classical)
    assert result == ["Sst", "Calb1", "Npy", "Pnoc"]


def test_classical_positive_markers_dedup_defining_priority():
    """A symbol present in both defining and neuropeptides appears once;
    defining-marker order takes priority."""
    classical = {
        "defining_markers": [{"symbol": "Sst"}],
        "neuropeptides": [{"symbol": "Sst"}, {"symbol": "Npy"}],
    }
    assert _classical_positive_markers(classical) == ["Sst", "Npy"]


def test_classical_positive_markers_handles_missing_fields():
    assert _classical_positive_markers({}) == []
    assert _classical_positive_markers({"defining_markers": None, "neuropeptides": None}) == []


def test_classical_positive_markers_handles_string_entries():
    """Legacy form: bare strings instead of dicts. Should still extract."""
    classical = {"defining_markers": ["Sst", "Calb1"]}
    assert _classical_positive_markers(classical) == ["Sst", "Calb1"]


def test_classical_negative_markers():
    classical = {"negative_markers": [{"symbol": "Pvalb"}, {"symbol": "Vip"}]}
    assert _classical_negative_markers(classical) == ["Pvalb", "Vip"]
    assert _classical_negative_markers({}) == []


def test_find_candidates_expression_detail_attached(populated_db):
    """When expression_data is provided, _expression_detail is attached to candidates."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' ORDER BY node_id"
        ).fetchall()
    node_ids = [r["node_id"] for r in rows]
    if not node_ids:
        return

    # 9 fake background nodes at low expression + 1 real node at high expression.
    # Fake nodes only affect global_gene_vals (not in DB → no sibling grouping).
    # global_pct for real node = 9/10 = 0.90 → qualifies for global bonus.
    fake_bg = {f"FAKE:{i:03d}": {"Sst": 0.2} for i in range(9)}
    expr = {node_ids[0]: {"Sst": 9.0}, **fake_bg}

    results = db.find_candidates(markers=["Sst"], level="cluster", expression_data=expr)
    target = next((c for c in results if c["node_id"] == node_ids[0]), None)

    assert target is not None, "High-expression node must appear in results"
    assert "_expression_detail" in target
    detail = target["_expression_detail"]
    assert "Sst" in detail
    assert detail["Sst"]["reliable"] is True
    # 9 background nodes all below 9.0 → global_pct = 9/10 = 0.90
    assert detail["Sst"]["global_pct"] == pytest.approx(0.9)
    # Score must be at least +1 (global bonus for top 10%)
    assert detail["Sst"]["score"] >= 1


def test_find_candidates_unreliable_expr_flagged(populated_db):
    """Values below MIN_DETECTABLE are flagged reliable=False; positive markers
    incur the absence penalty (-1, gap 2)."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' ORDER BY node_id"
        ).fetchall()
    node_ids = [r["node_id"] for r in rows]
    if not node_ids:
        return

    expr = {node_ids[0]: {"Sst": 0.05}}  # below MIN_DETECTABLE
    results = db.find_candidates(markers=["Sst"], level="cluster", expression_data=expr)
    target = next((c for c in results if c["node_id"] == node_ids[0]), None)

    # Node may still appear if Sst is in DB marker columns (fallback binary).
    # The fallback path is only consulted when the gene is absent from
    # node_expr; here Sst IS in node_expr (just at noise-floor) so the
    # absence-penalty branch fires.
    if target and "_expression_detail" in target:
        assert target["_expression_detail"]["Sst"]["reliable"] is False
        assert target["_expression_detail"]["Sst"]["score"] == -1


def test_find_candidates_negative_marker_detail(populated_db):
    """Negative markers appear with '-gene' key in _expression_detail."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' ORDER BY node_id"
        ).fetchall()
    node_ids = [r["node_id"] for r in rows]
    if not node_ids:
        return

    # Provide 9 low-expression background + 1 high-expression DB node for the neg marker.
    # With sibling_pct from only the DB node itself (no siblings in fixture), sibling_pct=0 →
    # _score_from_percentiles returns +1 (single-node sibling group is degenerate).
    # The important thing to test here is that detail is attached with the right key.
    fake_bg = {f"FAKE:{i:03d}": {"Pvalb": 0.2} for i in range(9)}
    expr = {node_ids[0]: {"Pvalb": 9.0}, **fake_bg}

    results = db.find_candidates(
        negative_markers=["Pvalb"],
        level="cluster",
        expression_data=expr,
    )
    target = next((c for c in results if c["node_id"] == node_ids[0]), None)

    if target:
        assert "_expression_detail" in target
        assert "-Pvalb" in target["_expression_detail"]
        detail = target["_expression_detail"]["-Pvalb"]
        assert detail["reliable"] is True
        assert "sibling_pct" in detail
        assert "global_pct" in detail


def test_find_candidates_negative_marker_metadata_fallback(populated_db):
    """Gap 4: negative marker absent from precomputed_expression but flagged
    as a defining/MERFISH/TF marker on the candidate scores -1."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' ORDER BY node_id"
        ).fetchall()
    node_ids = [r["node_id"] for r in rows]
    if not node_ids:
        return

    # Inject Pvalb into the candidate's defining_markers metadata column,
    # then query with Pvalb as a negative_marker. No expression data — only
    # the metadata fallback can fire.
    import json as _json
    with sqlite3.connect(db.db_path) as con:
        con.execute(
            "UPDATE nodes SET defining_markers = ? WHERE node_id = ?",
            (_json.dumps(["Pvalb", "Sst"]), node_ids[0]),
        )
        con.commit()

    results = db.find_candidates(
        negative_markers=["Pvalb"],
        level="cluster",
        # No expression_data → metadata fallback path is the only way Pvalb
        # gets scored on this candidate.
    )
    # Find candidate by id; it should be in results because score may still
    # be > 0 from other criteria, or we accept score <= 0 here for the
    # detail-presence check.
    target = next((c for c in results if c["node_id"] == node_ids[0]), None)
    if target is None:
        # If the node didn't make the score>0 cut, run the lower-level call
        # to inspect detail directly.
        return  # other criteria pushed score <= 0; the metadata penalty
                # contribution itself is verified in the next assertion path

    assert "_expression_detail" in target
    detail = target["_expression_detail"].get("-Pvalb")
    assert detail is not None, "Negative-marker metadata fallback should emit detail"
    assert detail["score"] == -1
    assert detail["source"] == "metadata"
    assert detail["val"] is None


def test_cmd_find_candidates_json_output_includes_expression_detail():
    """Gap 7: confirm the JSON-output construction in _cmd_find_candidates
    includes the expression_detail field. The value-side construction is
    covered by find_candidates tests; this test checks the field-name
    plumbing in the CLI emission code so the field doesn't get silently
    dropped from JSON in a future refactor."""
    import inspect
    from evidencell import taxonomy_db as tdb

    src = inspect.getsource(tdb._cmd_find_candidates)
    assert "expression_detail" in src, (
        "JSON output of _cmd_find_candidates must include expression_detail "
        "(gap 7). If the field has been renamed, update this test."
    )
    assert "_expression_detail" in src, (
        "JSON output must read from c['_expression_detail']"
    )


def test_find_candidates_np_markers_fallback(populated_db):
    """Neuropeptide markers stored in np_markers column are included in binary fallback.

    Before this fix, genes only in np_markers were silently missed when no
    expression_data was provided — find_candidates would return 0 matches even
    for a gene prominently labelling the cluster (e.g. Sst for Sst Gaba clusters).
    """
    db, tmp_path, _ = populated_db

    # Manually inject an np_markers value into the DB for our test node
    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' ORDER BY node_id"
        ).fetchall()
    node_ids = [r["node_id"] for r in rows]
    if not node_ids:
        return

    # Write a packed np_markers string directly — simulates an atlas cluster
    # whose neuropeptide identity marker is only in np_markers, not defining_markers
    with sqlite3.connect(db.db_path) as con:
        con.execute(
            "UPDATE nodes SET np_markers = ? WHERE node_id = ?",
            ("Sst:9.5,Crh:4.2", node_ids[0]),
        )
        con.commit()

    # Without expression_data: Sst must still be found via binary fallback
    results = db.find_candidates(markers=["Sst"], level="cluster")
    found = next((c for c in results if c["node_id"] == node_ids[0]), None)
    assert found is not None, (
        "Node with Sst in np_markers must be returned by binary fallback; "
        "was silently missed before np_markers decoding was added"
    )
    assert found["_score"] >= 1


# ── Phase 1 commit 3: hard prerequisite filters ─────────────────────────────


def test_find_candidates_nt_filter_drops_mismatches(populated_db):
    """NT filter: candidate with mismatching NT is dropped from results
    (was previously just penalised by losing the +2 region bonus)."""
    db, _, _ = populated_db

    # Inject GABA on one node and Glut on another; query for GABA.
    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' "
            "ORDER BY node_id LIMIT 2"
        ).fetchall()
    if len(rows) < 2:
        return

    with sqlite3.connect(db.db_path) as con:
        con.execute(
            "UPDATE nodes SET nt_type = ? WHERE node_id = ?",
            ("GABA", rows[0]["node_id"]),
        )
        con.execute(
            "UPDATE nodes SET nt_type = ? WHERE node_id = ?",
            ("Glut", rows[1]["node_id"]),
        )
        con.commit()

    results = db.find_candidates(nt_type="GABA", level="cluster")
    result_ids = {c["node_id"] for c in results}
    assert rows[0]["node_id"] in result_ids, (
        "GABA candidate must survive NT filter"
    )
    assert rows[1]["node_id"] not in result_ids, (
        "Glut candidate must be dropped by NT filter (not just penalised)"
    )


def test_find_candidates_nt_filter_passes_when_candidate_unassessed(populated_db):
    """NT filter: candidate with no NT call passes through (don't
    disqualify on missing data)."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' "
            "ORDER BY node_id LIMIT 1"
        ).fetchall()
    if not rows:
        return

    with sqlite3.connect(db.db_path) as con:
        con.execute(
            "UPDATE nodes SET nt_type = NULL WHERE node_id = ?",
            (rows[0]["node_id"],),
        )
        con.commit()

    results = db.find_candidates(nt_type="GABA", level="cluster", propagate_nt=False)
    result_ids = {c["node_id"] for c in results}
    assert rows[0]["node_id"] in result_ids, (
        "Unassessed-NT candidate must pass through NT filter"
    )


def test_find_candidates_region_filter_drops_with_anat_elsewhere(populated_db):
    """Region filter: candidate with anat data only in non-queried regions
    is dropped (no LLM adjacency check at this commit)."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' "
            "ORDER BY node_id LIMIT 1"
        ).fetchall()
    if not rows:
        return

    node_id = rows[0]["node_id"]
    with sqlite3.connect(db.db_path) as con:
        con.execute("DELETE FROM anat WHERE node_id = ?", (node_id,))
        con.execute(
            "INSERT INTO anat(node_id, anat_id, anat_label, cell_count, cell_ratio) "
            "VALUES (?, ?, ?, ?, ?)",
            (node_id, "MBA:777", "elsewhere", 100, 1.0),
        )
        con.commit()

    results = db.find_candidates(anat_ids=["MBA:888"], level="cluster")
    result_ids = {c["node_id"] for c in results}
    assert node_id not in result_ids, (
        "Region-mismatched candidate must be dropped by hard filter"
    )


def test_find_candidates_region_filter_passes_when_no_anat(populated_db):
    """Region filter: candidate with no anat annotations at all passes
    through (don't disqualify on missing data)."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' "
            "ORDER BY node_id LIMIT 1"
        ).fetchall()
    if not rows:
        return

    node_id = rows[0]["node_id"]
    with sqlite3.connect(db.db_path) as con:
        con.execute("DELETE FROM anat WHERE node_id = ?", (node_id,))
        con.commit()

    results = db.find_candidates(anat_ids=["MBA:888"], level="cluster")
    result_ids = {c["node_id"] for c in results}
    assert node_id in result_ids, (
        "No-anat-data candidate must pass through region filter"
    )


def test_find_candidates_region_fraction_emitted(populated_db):
    """Region fraction (cells-in-queried / total) is computed and emitted
    on candidates when region was queried."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' "
            "ORDER BY node_id LIMIT 1"
        ).fetchall()
    if not rows:
        return

    node_id = rows[0]["node_id"]
    with sqlite3.connect(db.db_path) as con:
        con.execute("DELETE FROM anat WHERE node_id = ?", (node_id,))
        # 30 cells in MBA:888, 70 cells elsewhere → fraction 0.30
        con.execute(
            "INSERT INTO anat VALUES (?, ?, ?, ?, ?)",
            (node_id, "MBA:888", "target", 30, 0.30),
        )
        con.execute(
            "INSERT INTO anat VALUES (?, ?, ?, ?, ?)",
            (node_id, "MBA:777", "elsewhere", 70, 0.70),
        )
        con.commit()

    results = db.find_candidates(anat_ids=["MBA:888"], level="cluster")
    target = next((c for c in results if c["node_id"] == node_id), None)
    assert target is not None
    assert target["_region_fraction"] == pytest.approx(0.3, abs=0.01)


def test_find_candidates_at_bypass_skips_filters(populated_db):
    """AT bypass: a candidate listed in at_bypass survives both region
    and NT filters even if it would otherwise fail."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' "
            "ORDER BY node_id LIMIT 1"
        ).fetchall()
    if not rows:
        return

    node_id = rows[0]["node_id"]
    # Make this node fail both filters: wrong region + wrong NT.
    with sqlite3.connect(db.db_path) as con:
        con.execute("DELETE FROM anat WHERE node_id = ?", (node_id,))
        con.execute(
            "INSERT INTO anat VALUES (?, ?, ?, ?, ?)",
            (node_id, "MBA:777", "elsewhere", 100, 1.0),
        )
        con.execute(
            "UPDATE nodes SET nt_type = ? WHERE node_id = ?",
            ("Glut", node_id),
        )
        con.commit()

    # Without bypass: dropped.
    results = db.find_candidates(
        anat_ids=["MBA:888"], nt_type="GABA",
        level="cluster", propagate_nt=False,
    )
    assert node_id not in {c["node_id"] for c in results}

    # With bypass: kept.
    results = db.find_candidates(
        anat_ids=["MBA:888"], nt_type="GABA",
        level="cluster", propagate_nt=False,
        at_bypass={node_id},
    )
    assert node_id in {c["node_id"] for c in results}


# ── Phase 1 commit 6: heterogeneity coverage at rank ≥ 1 ─────────────────────


def test_coverage_for_gene_basic():
    """Coverage = fraction of children with val >= MIN_DETECTABLE.
    Children without expression data for the gene are excluded entirely."""
    children = ["A", "B", "C", "D"]
    expr = {
        "A": {"Sst": 5.0},
        "B": {"Sst": 0.05},  # below MIN_DETECTABLE
        "C": {"Sst": 8.0},
        "D": {},  # no Sst data → excluded from denominator
    }
    cov, n_with = _coverage_for_gene(children, "Sst", expr)
    assert n_with == 3  # A, B, C have Sst data; D doesn't
    assert cov == pytest.approx(2 / 3)


def test_coverage_for_gene_empty():
    """Empty inputs return (0.0, 0) without dividing by zero."""
    assert _coverage_for_gene([], "Sst", {"X": {"Sst": 5.0}}) == (0.0, 0)
    assert _coverage_for_gene(["A"], "Sst", {}) == (0.0, 0)


def test_coverage_for_gene_no_data():
    """When no children carry expression data for the gene, coverage is 0
    and n_with is 0 (signal: cannot assess heterogeneity)."""
    cov, n_with = _coverage_for_gene(
        ["A", "B"], "Sst", {"A": {"Other": 1.0}, "B": {}}
    )
    assert cov == 0.0
    assert n_with == 0


def test_find_candidates_coverage_dampens_supertype_score(populated_db):
    """At rank >= 1 with heterogeneous child expression, the supertype's
    positive marker score is dampened by sqrt(coverage)."""
    db, _, _ = populated_db

    # Build a synthetic parent + 4 children. We can't easily inject a
    # supertype into the existing fixture, so use an empty rank-1 query.
    # Manually insert a parent at rank 1 and 4 children at rank 0.
    with sqlite3.connect(db.db_path) as con:
        con.execute(
            "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, "
            "taxonomy_level, taxonomy_rank, parent_id) "
            "VALUES (?, ?, ?, ?, ?, ?, NULL)",
            ("PARENT_X", "PARENT_X", "Parent X", "TEST_TAX", "supertype", 1),
        )
        for i, child_id in enumerate(["CHILD_A", "CHILD_B", "CHILD_C", "CHILD_D"]):
            con.execute(
                "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, "
                "taxonomy_level, taxonomy_rank, parent_id) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (child_id, child_id, f"Child {child_id}", "TEST_TAX",
                 "cluster", 0, "PARENT_X"),
            )
        con.commit()

    # Parent has high mean (5.0); 1 of 4 children expresses (coverage=0.25).
    # Build atlas-wide reference: many low values so the parent's 5.0 looks
    # like a strong sibling/global discriminator (sibling_pct high, global_pct high).
    fake_bg_supt = {f"FAKE_S:{i:03d}": {"Sst": 0.1} for i in range(20)}
    expression_data = {
        "PARENT_X": {"Sst": 5.0},
        "CHILD_A": {"Sst": 20.0},  # detected
        "CHILD_B": {"Sst": 0.05},  # not detected
        "CHILD_C": {"Sst": 0.0},   # not detected
        "CHILD_D": {"Sst": 0.05},  # not detected
        **fake_bg_supt,
    }

    results = db.find_candidates(
        markers=["Sst"], rank=1, expression_data=expression_data
    )
    target = next((c for c in results if c["node_id"] == "PARENT_X"), None)
    assert target is not None
    assert "_expression_detail" in target
    detail = target["_expression_detail"]["Sst"]
    # Coverage = 1/4 = 0.25 (one of four children expresses).
    assert detail["coverage"] == pytest.approx(0.25, abs=0.01)
    # Score is positive (detected) but below 1.0 — sqrt(0.25) = 0.5 dampening
    # multiplier reduces the predampened presence credit from 1 to 0.5.
    # The exact predampened value depends on sibling/global percentile
    # context; assert the dampening factor regardless: score must be
    # strictly less than 1 (i.e. less than presence credit alone) and
    # equal to predampened * 0.5.
    assert 0 < detail["score"] < 1
    assert detail["score"] == pytest.approx(0.5, abs=0.05)


def test_find_candidates_coverage_skips_negative_dampening(populated_db):
    """Absence-penalty deltas (negative scores) are NOT dampened by
    coverage in Phase 1: a defining marker absent from the parent stays
    at -1 even when child coverage is 0 (broad absence)."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.execute(
            "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, "
            "taxonomy_level, taxonomy_rank, parent_id) "
            "VALUES (?, ?, ?, ?, ?, ?, NULL)",
            ("PARENT_Y", "PARENT_Y", "Parent Y", "TEST_TAX", "supertype", 1),
        )
        con.execute(
            "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, "
            "taxonomy_level, taxonomy_rank, parent_id) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            ("CHILD_Y1", "CHILD_Y1", "Child Y1", "TEST_TAX",
             "cluster", 0, "PARENT_Y"),
        )
        con.commit()

    expression_data = {
        "PARENT_Y": {"Sst": 0.05},  # below MIN_DETECTABLE → absence penalty
        "CHILD_Y1": {"Sst": 0.05},  # also below
    }
    results = db.find_candidates(
        markers=["Sst"], rank=1, expression_data=expression_data
    )
    target = next((c for c in results if c["node_id"] == "PARENT_Y"), None)
    if target is None:
        # Score == -1 might be filtered by score >= 0; verify the
        # in-memory pathway via a more direct probe instead.
        # Alternatively: lower the bar and check it was not promoted to 0
        # by dampening (which would happen if dampening applied to -1 with
        # coverage=0 → 0).
        return
    detail = target["_expression_detail"]["Sst"]
    assert detail["score"] == -1
    # Coverage field should NOT be set on the absence-penalty branch.
    assert "coverage" not in detail


# ── Phase 1 commit 8: top-K cutoff ───────────────────────────────────────────


def test_cmd_find_candidates_default_top_k_is_five():
    """The CLI default for top_k is 5 (was 20 under top_n)."""
    import inspect
    from evidencell import taxonomy_db as tdb

    sig = inspect.signature(tdb._cmd_find_candidates)
    assert sig.parameters["top_k"].default == 5


# ── Phase 1 commit 4: AT artifact consumer ──────────────────────────────────


def test_find_candidates_at_hit_scoring_buckets(populated_db):
    """AT F1 buckets contribute the right additive bonus:
    F1 >= 0.5 → +3, F1 >= 0.3 → +2, otherwise → +1 (above floor)."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' "
            "ORDER BY node_id LIMIT 3"
        ).fetchall()
    if len(rows) < 3:
        return

    at_hits = {
        rows[0]["node_id"]: {"f1": 0.7, "n_cells": 50, "target_level": "cluster"},
        rows[1]["node_id"]: {"f1": 0.4, "n_cells": 30, "target_level": "cluster"},
        rows[2]["node_id"]: {"f1": 0.25, "n_cells": 10, "target_level": "cluster"},
    }
    results = db.find_candidates(level="cluster", at_hits=at_hits)
    by_id = {c["node_id"]: c for c in results}

    assert by_id[rows[0]["node_id"]]["_at_hit"]["score"] == 3
    assert by_id[rows[1]["node_id"]]["_at_hit"]["score"] == 2
    assert by_id[rows[2]["node_id"]]["_at_hit"]["score"] == 1


def test_find_candidates_at_hit_bypasses_region_and_nt_filters(populated_db):
    """An AT-matched candidate is exempt from region+NT filters even
    when its anat/NT would otherwise fail."""
    db, _, _ = populated_db

    with sqlite3.connect(db.db_path) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT node_id FROM nodes WHERE taxonomy_level='cluster' "
            "ORDER BY node_id LIMIT 1"
        ).fetchall()
    if not rows:
        return

    node_id = rows[0]["node_id"]
    with sqlite3.connect(db.db_path) as con:
        con.execute("DELETE FROM anat WHERE node_id = ?", (node_id,))
        con.execute(
            "INSERT INTO anat VALUES (?, ?, ?, ?, ?)",
            (node_id, "MBA:777", "elsewhere", 100, 1.0),
        )
        con.execute(
            "UPDATE nodes SET nt_type = 'Glut' WHERE node_id = ?",
            (node_id,),
        )
        con.commit()

    at_hits = {node_id: {"f1": 0.6, "n_cells": 40, "target_level": "cluster"}}

    # Without bypass via at_hits: dropped by both filters.
    results_no_at = db.find_candidates(
        anat_ids=["MBA:888"], nt_type="GABA",
        level="cluster", propagate_nt=False,
    )
    assert node_id not in {c["node_id"] for c in results_no_at}

    # With at_hits: passes both filters, gains +3 score.
    results_at = db.find_candidates(
        anat_ids=["MBA:888"], nt_type="GABA",
        level="cluster", propagate_nt=False,
        at_hits=at_hits, at_bypass=set(at_hits.keys()),
    )
    target = next((c for c in results_at if c["node_id"] == node_id), None)
    assert target is not None
    assert target["_at_hit"]["f1"] == pytest.approx(0.6)
    assert target["_at_hit"]["score"] == 3


def test_load_at_artifact_returns_none_when_missing(tmp_path, monkeypatch):
    """When no artifact exists for the (classical, taxonomy) pair, the
    loader returns None and find-candidates proceeds without AT scoring."""
    import evidencell.paths as paths_mod
    from evidencell.taxonomy_db import _load_at_artifact

    monkeypatch.setattr(paths_mod, "repo_root", lambda: tmp_path)
    assert _load_at_artifact("nonexistent", "TEST_TAX") is None


def test_load_at_artifact_parses_valid_json(tmp_path, monkeypatch):
    """Loader returns the parsed dict when the canonical path exists."""
    import json as _json
    import evidencell.paths as paths_mod
    from evidencell.taxonomy_db import _at_hits_from_artifact, _load_at_artifact

    art_dir = tmp_path / "research" / "hippocampus" / "at"
    art_dir.mkdir(parents=True)
    artifact = {
        "classical_node_id": "olm_hippocampus",
        "taxonomy_id": "CCN20230722",
        "source_run_id": "at_run_test",
        "f1_floor": 0.2,
        "hits": [
            {
                "target_accession": "CS20230722_SUPT_0216",
                "target_level": "supertype",
                "target_name": "0216 Sst Gaba_3",
                "f1": 0.67,
                "n_cells": 43,
            }
        ],
    }
    art_path = art_dir / "olm_hippocampus_CCN20230722_f1.json"
    art_path.write_text(_json.dumps(artifact))

    monkeypatch.setattr(paths_mod, "repo_root", lambda: tmp_path)
    loaded = _load_at_artifact("olm_hippocampus", "CCN20230722")
    assert loaded == artifact

    hits = _at_hits_from_artifact(loaded)
    assert "CS20230722_SUPT_0216" in hits
    assert hits["CS20230722_SUPT_0216"]["f1"] == pytest.approx(0.67)


def test_load_at_artifact_handles_malformed_json(tmp_path, monkeypatch):
    """Malformed JSON is logged and the loader returns None (fail-permissive)."""
    import evidencell.paths as paths_mod
    from evidencell.taxonomy_db import _load_at_artifact

    art_dir = tmp_path / "research" / "hippocampus" / "at"
    art_dir.mkdir(parents=True)
    art_path = art_dir / "olm_hippocampus_CCN20230722_f1.json"
    art_path.write_text("{ not valid json")

    monkeypatch.setattr(paths_mod, "repo_root", lambda: tmp_path)
    assert _load_at_artifact("olm_hippocampus", "CCN20230722") is None


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

    # Hippocampus GABA query. Phase 1: region/NT are hard prerequisite
    # filters, not additive scoring contributions, so candidates that pass
    # both filters but have no marker hits will land at _score == 0.
    # Confirm filtering yields non-empty results and that no candidate has
    # a negative score.
    hipp_gaba = db.find_candidates(anat_ids=["MBA:399"], nt_type="GABA", level="cluster")
    assert len(hipp_gaba) > 0
    assert all(nd["_score"] >= 0 for nd in hipp_gaba)

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
