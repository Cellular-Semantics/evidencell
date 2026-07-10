"""Tests for src/evidencell/at_metrics.py — migration, lookup,
compute_edge_metrics."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from evidencell import at_metrics
from evidencell._models import AnnotationTransferResultSet


# ─── Fixtures ─────────────────────────────────────────────────────────


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


@pytest.fixture
def fake_taxonomy_db(tmp_path: Path, monkeypatch) -> Path:
    """Build a minimal CCN20230722 taxonomy SQLite DB at tmp_path and
    monkeypatch ``at_metrics._taxonomy_db_path`` to return it.

    Covers the lineage relationships needed by the AT-metric tests
    (OLM Sst-OLM ancestry, AAC chandelier-vs-basket divergence, BIC
    Pvalb-vs-Sst supertypes). Self-contained — runs on any environment
    including fresh clones / CI without the real KB taxonomy DB on
    disk. The schema mirrors ``kb/taxonomy/{taxonomy_id}/{taxonomy_id}.db``
    sufficiently for ``ancestor_accession_by_level`` to walk parent_ids.
    """
    import sqlite3

    db_path = tmp_path / "CCN20230722.db"
    conn = sqlite3.connect(str(db_path))
    try:
        conn.execute(
            "CREATE TABLE nodes ("
            " node_id TEXT PRIMARY KEY,"
            " short_form TEXT,"
            " label TEXT,"
            " taxonomy_id TEXT,"
            " taxonomy_level TEXT,"
            " taxonomy_rank INTEGER,"
            " parent_id TEXT"
            ")"
        )
        # (short_form, label, taxonomy_level, taxonomy_rank, parent_short)
        rows = [
            # Class
            ("CS20230722_CLAS_07", "07 CTX-MGE GABA",     "CLASS",     3, None),
            ("CS20230722_CLAS_03", "03 OB-CR Glut",        "CLASS",     3, None),
            ("CS20230722_CLAS_04", "04 DG-IMN Glut",       "CLASS",     3, None),
            # Subclasses (parents = class)
            ("CS20230722_SUBC_051", "051 Pvalb chandelier", "SUBCLASS", 2, "CS20230722_CLAS_07"),
            ("CS20230722_SUBC_052", "052 Pvalb Gaba",       "SUBCLASS", 2, "CS20230722_CLAS_07"),
            ("CS20230722_SUBC_053", "053 Sst Gaba",         "SUBCLASS", 2, "CS20230722_CLAS_07"),
            ("CS20230722_SUBC_036", "036 HPF CR Glut",      "SUBCLASS", 2, "CS20230722_CLAS_03"),
            # Supertypes (parents = subclass)
            ("CS20230722_SUPT_0204", "0204 Pvalb chandelier Gaba_1", "SUPERTYPE", 1, "CS20230722_SUBC_051"),
            ("CS20230722_SUPT_0206", "0206 Pvalb Gaba_2",            "SUPERTYPE", 1, "CS20230722_SUBC_052"),
            ("CS20230722_SUPT_0216", "0216 Sst Gaba_3",              "SUPERTYPE", 1, "CS20230722_SUBC_053"),
            ("CS20230722_SUPT_0219", "0219 Sst Gaba_6",              "SUPERTYPE", 1, "CS20230722_SUBC_053"),
            ("CS20230722_SUPT_0135", "0135 HPF CR Glut_1",           "SUPERTYPE", 1, "CS20230722_SUBC_036"),
            # Clusters (parents = supertype)
            ("CS20230722_CLUS_0732", "0732 Pvalb chandelier Gaba_1", "CLUSTER", 0, "CS20230722_SUPT_0204"),
            ("CS20230722_CLUS_0737", "0737 Pvalb Gaba_2",            "CLUSTER", 0, "CS20230722_SUPT_0206"),
            ("CS20230722_CLUS_0739", "0739 Pvalb Gaba_2",            "CLUSTER", 0, "CS20230722_SUPT_0206"),
            ("CS20230722_CLUS_0768", "0768 Sst Gaba_3",              "CLUSTER", 0, "CS20230722_SUPT_0216"),
        ]
        conn.executemany(
            "INSERT INTO nodes (node_id, short_form, label, taxonomy_id, "
            "taxonomy_level, taxonomy_rank, parent_id) "
            "VALUES (?, ?, ?, 'CCN20230722', ?, ?, ?)",
            [
                # node_id, short_form, label, taxonomy_level, taxonomy_rank, parent_id
                (sf, sf, label, level, rank, parent)
                for sf, label, level, rank, parent in rows
            ],
        )
        conn.commit()
    finally:
        conn.close()

    monkeypatch.setattr(at_metrics, "_taxonomy_db_path", lambda tid: db_path)
    return db_path


@pytest.fixture
def shape_a_run(tmp_path: Path) -> Path:
    """Shape A: f1_scores_best.csv (one row per (source, level), best
    target only). Mimics Que 2021 / Hochgerner DG runs."""
    run = tmp_path / "at_run_demo_shape_a"
    _write(
        run / "manifest.yaml",
        "id: at_run_demo_shape_a\nrecord_type: AnnotationTransferRun\n"
        "target_taxonomy_id: CCN20230722\n",
    )
    _write(
        run / "f1_scores_best.csv",
        "source_label,level,best_target,n_cells,coverage,purity,f1,median_boot\n"
        # AAC: best at supertype is 0206 (Pvalb basket), NOT a chandelier target.
        "AAC,class,07 CTX-MGE GABA,6,1.0,0.078,0.146,1.0\n"
        "AAC,subclass,052 Pvalb Gaba,5,0.833,0.066,0.122,1.0\n"
        "AAC,supertype,0206 Pvalb Gaba_2,5,0.833,0.065,0.121,1.0\n"
        "AAC,cluster,0739 Pvalb Gaba_2,5,0.833,0.138,0.238,1.0\n"
        # BC: best at supertype IS 0206 (matches BC edges typically).
        "BC,class,07 CTX-MGE GABA,53,1.0,0.697,0.821,1.0\n"
        "BC,supertype,0206 Pvalb Gaba_2,53,0.898,0.697,0.785,1.0\n"
        "BC,cluster,0739 Pvalb Gaba_2,31,0.794,0.861,0.826,1.0\n",
    )
    return run


@pytest.fixture
def shape_b_run(tmp_path: Path) -> Path:
    """Shape B: f1_matrix.csv (full per-(source, level, target) matrix).
    Mimics Winterer OLM / Chamberland runs."""
    run = tmp_path / "at_run_demo_shape_b"
    _write(
        run / "manifest.yaml",
        "id: at_run_demo_shape_b\nrecord_type: AnnotationTransferRun\n"
        "target_taxonomy_id: CCN20230722\n",
    )
    _write(
        run / "f1_matrix.csv",
        "source_label,level,target_name,n_cells,coverage,purity,f1,mean_boot,median_boot\n"
        "Sst-OLM,class,07 CTX-MGE GABA,23,1.0,0.34,0.51,0.98,1.0\n"
        "Sst-OLM,subclass,053 Sst Gaba,23,1.0,0.51,0.68,0.98,1.0\n"
        "Sst-OLM,supertype,0216 Sst Gaba_3,22,0.96,0.51,0.67,0.99,1.0\n"
        "Sst-OLM,supertype,0219 Sst Gaba_6,1,0.04,0.02,0.03,0.92,0.92\n"
        "Sst-OLM,cluster,0768 Sst Gaba_3,11,0.48,0.69,0.56,0.97,1.0\n",
    )
    return run


@pytest.fixture
def shape_b_run_variants(tmp_path: Path) -> Path:
    """Shape B with two CSV variants (mimics Chamberland by-class)."""
    run = tmp_path / "at_run_demo_variants"
    _write(
        run / "manifest.yaml",
        "id: at_run_demo_variants\ntarget_taxonomy_id: CCN20230722\n",
    )
    _write(
        run / "f1_matrix_chamberland.csv",
        "source_label,level,target_name,n_cells,coverage,purity,f1,mean_boot,median_boot\n"
        "Chrna2,supertype,0216 Sst Gaba_3,74,0.90,0.12,0.21,0.98,1.0\n",
    )
    _write(
        run / "f1_matrix_chamberland_by_class.csv",
        "source_label,level,target_name,n_cells,coverage,purity,f1,mean_boot,median_boot\n"
        "Chrna2,supertype,0216 Sst Gaba_3,126,0.95,0.20,0.33,0.98,1.0\n",
    )
    return run


# ─── Accession derivation ─────────────────────────────────────────────


def test_derive_accession_strips_leading_digits():
    assert at_metrics._derive_target_accession(
        "CCN20230722", "SUPERTYPE", "0206 Pvalb Gaba_2"
    ) == "CS20230722_SUPT_0206"
    assert at_metrics._derive_target_accession(
        "CCN20230722", "CLASS", "07 CTX-MGE GABA"
    ) == "CS20230722_CLAS_07"
    assert at_metrics._derive_target_accession(
        "CCN20230722", "CLUSTER", "0739 Pvalb Gaba_2"
    ) == "CS20230722_CLUS_0739"


def test_derive_accession_unknown_taxonomy_uses_taxonomy_id_as_prefix():
    """Falls back to passing taxonomy_id through unchanged."""
    assert at_metrics._derive_target_accession(
        "FUTURE_TAX", "SUPERTYPE", "0100 Foo"
    ) == "FUTURE_TAX_SUPT_0100"


def test_derive_accession_rejects_missing_leading_digits():
    with pytest.raises(ValueError, match="no leading numeric"):
        at_metrics._derive_target_accession(
            "CCN20230722", "SUPERTYPE", "Pvalb_chandelier"
        )


def test_normalise_level_rejects_garbage():
    with pytest.raises(ValueError):
        at_metrics._normalise_level("NOTALEVEL")


# ─── Migration ────────────────────────────────────────────────────────


def test_migrate_shape_a_writes_at_results_yaml(shape_a_run):
    written = at_metrics.migrate_run(shape_a_run)
    assert len(written) == 1
    yaml_path = written[0]
    assert yaml_path.name == "at_results.yaml"
    doc = yaml.safe_load(yaml_path.read_text())
    rs = AnnotationTransferResultSet(**doc)
    assert rs.run_id == "at_run_demo_shape_a"
    assert rs.taxonomy_id == "CCN20230722"
    # 4 AAC rows + 3 BC rows
    assert len(rs.rows) == 7
    # Accessions are derived from target_name + level infix
    aac_super = [
        r for r in rs.rows
        if r.source_label == "AAC" and r.taxonomy_level == "SUPERTYPE"
    ][0]
    assert aac_super.target_accession == "CS20230722_SUPT_0206"
    assert aac_super.f1 == pytest.approx(0.121)


def test_migrate_shape_b_writes_at_results_yaml(shape_b_run):
    written = at_metrics.migrate_run(shape_b_run)
    assert len(written) == 1
    rs = AnnotationTransferResultSet(**yaml.safe_load(written[0].read_text()))
    assert len(rs.rows) == 5  # 1 class + 1 subclass + 2 supertype + 1 cluster
    # mean_bootstrap is captured (Shape B has it; Shape A doesn't)
    supertype_rows = [r for r in rs.rows if r.taxonomy_level == "SUPERTYPE"]
    assert all(r.mean_bootstrap is not None for r in supertype_rows)


def test_migrate_shape_b_variants_writes_two_yamls(shape_b_run_variants):
    written = at_metrics.migrate_run(shape_b_run_variants)
    names = sorted(p.name for p in written)
    assert names == [
        "at_results_chamberland.yaml",
        "at_results_chamberland_by_class.yaml",
    ]
    by_class = [p for p in written if "by_class" in p.name][0]
    rs = AnnotationTransferResultSet(**yaml.safe_load(by_class.read_text()))
    assert rs.normalisation == "chamberland_by_class"


def test_migrate_skips_mmc_results_csv(tmp_path):
    """Files that don't match f1_scores_*.csv / f1_matrix*.csv are ignored."""
    run = tmp_path / "noise_run"
    _write(
        run / "manifest.yaml",
        "id: noise_run\ntarget_taxonomy_id: CCN20230722\n",
    )
    _write(run / "mmc_results.csv", "# raw cell assignments\n")
    written = at_metrics.migrate_run(run)
    assert written == []


def test_migrate_requires_taxonomy_id(tmp_path):
    """Without a manifest target_taxonomy_id and no --taxonomy override,
    migration fails loud."""
    run = tmp_path / "no_manifest"
    _write(
        run / "f1_matrix.csv",
        "source_label,level,target_name,n_cells,coverage,purity,f1,mean_boot,median_boot\n"
        "X,class,07 CTX-MGE GABA,10,1.0,0.5,0.7,0.9,1.0\n",
    )
    with pytest.raises(ValueError, match="taxonomy_id"):
        at_metrics.migrate_run(run)


# ─── Lookup ───────────────────────────────────────────────────────────


@pytest.fixture
def migrated_shape_a(shape_a_run):
    at_metrics.migrate_run(shape_a_run)
    return shape_a_run


@pytest.fixture
def migrated_shape_b(shape_b_run):
    at_metrics.migrate_run(shape_b_run)
    return shape_b_run


def test_load_result_set_canonical(migrated_shape_a, tmp_path):
    rs = at_metrics.load_result_set(
        run_ref=migrated_shape_a.name, runs_root=tmp_path
    )
    assert rs.run_id == "at_run_demo_shape_a"


def test_lookup_metrics_match(migrated_shape_a, tmp_path):
    rs = at_metrics.load_result_set(migrated_shape_a.name, runs_root=tmp_path)
    # BC's best supertype IS 0206 — should find it
    found = at_metrics.lookup_metrics(rs, "BC", "CS20230722_SUPT_0206")
    assert "SUPERTYPE" in found
    assert found["SUPERTYPE"].f1 == pytest.approx(0.785)


def test_lookup_metrics_no_match_for_off_target(migrated_shape_a, tmp_path):
    """AAC's best at every level is NOT SUPT_0204 (chandelier). In a
    Shape A run we never recorded F1 for AAC→0204, so lookup returns
    empty — the structural fix that the audit was after."""
    rs = at_metrics.load_result_set(migrated_shape_a.name, runs_root=tmp_path)
    found = at_metrics.lookup_metrics(rs, "AAC", "CS20230722_SUPT_0204")
    assert found == {}


def test_source_best_at_each_level(migrated_shape_a, tmp_path):
    rs = at_metrics.load_result_set(migrated_shape_a.name, runs_root=tmp_path)
    best = at_metrics.source_best_at_each_level(rs, "AAC")
    assert set(best) == {"CLASS", "SUBCLASS", "SUPERTYPE", "CLUSTER"}
    assert best["SUPERTYPE"].target_accession == "CS20230722_SUPT_0206"
    # Source-best for CLUSTER is 0739 (basket), highest AAC F1
    assert best["CLUSTER"].target_accession == "CS20230722_CLUS_0739"


# ─── compute_edge_metrics ─────────────────────────────────────────────


def test_compute_edge_metrics_strict_match_returns_populated(
    migrated_shape_b, tmp_path
):
    """OLM Sst-OLM → SUPT_0216, **strict** mode: edge target IS source
    best at supertype. Returns exactly one row, supports=SUPPORT."""
    payload = at_metrics.compute_edge_metrics(
        run_ref=migrated_shape_b.name,
        source_label="Sst-OLM",
        edge_target="CS20230722_SUPT_0216",
        runs_root=tmp_path,
        lineage_aware=False,
    )
    assert len(payload["metrics_by_level"]) == 1  # SUPERTYPE row only
    assert payload["best_mapping_rank"] == 1
    assert payload["best_f1_score"] == pytest.approx(0.67)
    assert payload["supports_default"] == "SUPPORT"
    assert payload["f1_source_relpath"] == "at_results.yaml"
    assert payload["source_best_summary"]["SUPERTYPE"]["is_edge_target"] is True
    assert payload["lineage_aware"] is False


def test_compute_edge_metrics_lineage_aware_walks_ancestors(
    migrated_shape_b, fake_taxonomy_db, tmp_path
):
    """Lineage-aware default: walks parent_ids in the taxonomy DB.
    Uses a self-contained fake taxonomy DB (built by the fixture) so
    the test runs on fresh clones / CI without depending on the real
    `kb/taxonomy/CCN20230722/CCN20230722.db` being on disk.

    For Sst-OLM → SUPT_0216 with the fixture's three Sst-OLM rows
    (CLAS_07, SUBC_053, SUPT_0216), all three are ancestors of the
    edge target — lineage-aware should populate all three rows.
    """
    payload = at_metrics.compute_edge_metrics(
        run_ref=migrated_shape_b.name,
        source_label="Sst-OLM",
        edge_target="CS20230722_SUPT_0216",
        runs_root=tmp_path,
        lineage_aware=True,
    )
    levels = [r["taxonomy_level"] for r in payload["metrics_by_level"]]
    assert levels == ["CLASS", "SUBCLASS", "SUPERTYPE"]
    assert payload["supports_default"] == "SUPPORT"
    assert payload["lineage_aware"] is True


def test_compute_edge_metrics_strict_off_target_empty(
    migrated_shape_a, tmp_path
):
    """AAC → SUPT_0204 (chandelier) in **strict** mode:
    metrics_by_level = [] (AAC has no row for SUPT_0204);
    supports_default = NO_EVIDENCE."""
    payload = at_metrics.compute_edge_metrics(
        run_ref=migrated_shape_a.name,
        source_label="AAC",
        edge_target="CS20230722_SUPT_0204",
        runs_root=tmp_path,
        lineage_aware=False,
    )
    assert payload["metrics_by_level"] == []
    assert payload["best_f1_score"] is None
    assert payload["supports_default"] == "NO_EVIDENCE"
    assert payload["source_best_summary"]["SUPERTYPE"]["target_accession"] == (
        "CS20230722_SUPT_0206"
    )
    assert all(
        not v["is_edge_target"]
        for v in payload["source_best_summary"].values()
    )


def test_compute_edge_metrics_lineage_aware_diverges_at_subclass(
    migrated_shape_a, fake_taxonomy_db, tmp_path
):
    """AAC → SUPT_0204 (chandelier) in **lineage-aware** mode:
    SUPT_0204's lineage is CLAS_07 / SUBC_051 / SUPT_0204. AAC has
    rows for CLAS_07 (yes) but its subclass best is SUBC_052 (basket),
    NOT SUBC_051 (chandelier). So lineage-aware finds AAC at CLASS
    only — one row at CLASS, no rows at SUBCLASS/SUPERTYPE.

    This is the Bucket-C structural finding: the present-at-CLASS +
    absent-below pattern IS the evidence that the mapping is unsupported.
    """
    payload = at_metrics.compute_edge_metrics(
        run_ref=migrated_shape_a.name,
        source_label="AAC",
        edge_target="CS20230722_SUPT_0204",
        runs_root=tmp_path,
        lineage_aware=True,
    )
    levels = [r["taxonomy_level"] for r in payload["metrics_by_level"]]
    assert levels == ["CLASS"]
    # F1=0.146 → PARTIAL band (above 0.10 noise floor, below 0.6).
    assert payload["supports_default"] == "PARTIAL"
    # source_best_summary still shows where AAC actually went.
    assert payload["source_best_summary"]["SUPERTYPE"]["target_accession"] == (
        "CS20230722_SUPT_0206"
    )
    assert payload["source_best_summary"]["SUPERTYPE"]["is_edge_target_lineage"] is False


def test_compute_edge_metrics_noise_floor_demotes_partial_to_no_evidence(
    migrated_shape_b, tmp_path
):
    """Sst-OLM → SUPT_0219 has F1=0.03 (well below 0.10 noise floor).
    Strict mode: the SUPT_0219 row exists, F1=0.03, NO_EVIDENCE."""
    payload = at_metrics.compute_edge_metrics(
        run_ref=migrated_shape_b.name,
        source_label="Sst-OLM",
        edge_target="CS20230722_SUPT_0219",
        runs_root=tmp_path,
        lineage_aware=False,
    )
    assert len(payload["metrics_by_level"]) == 1
    assert payload["best_f1_score"] == pytest.approx(0.03)
    assert payload["supports_default"] == "NO_EVIDENCE"


def test_compute_edge_metrics_partial_band(migrated_shape_a, tmp_path):
    """BC → CLUS_0739 best F1 = 0.826 → SUPPORT. Move target to one with
    F1 between 0.10 and 0.60 by using AAC's class row F1=0.146."""
    payload = at_metrics.compute_edge_metrics(
        run_ref=migrated_shape_a.name,
        source_label="AAC",
        edge_target="CS20230722_CLAS_07",
        runs_root=tmp_path,
    )
    assert payload["best_f1_score"] == pytest.approx(0.146)
    assert payload["supports_default"] == "PARTIAL"


def test_compute_edge_metrics_variant_selects_correct_yaml(
    shape_b_run_variants, tmp_path
):
    """Multiple at_results files → must pass variant= to pick one."""
    at_metrics.migrate_run(shape_b_run_variants)
    # Base (chamberland)
    base = at_metrics.compute_edge_metrics(
        run_ref=shape_b_run_variants.name,
        source_label="Chrna2",
        edge_target="CS20230722_SUPT_0216",
        variant="chamberland",
        runs_root=tmp_path,
    )
    assert base["best_f1_score"] == pytest.approx(0.21)
    assert base["f1_source_relpath"] == "at_results_chamberland.yaml"
    # by-class
    by_class = at_metrics.compute_edge_metrics(
        run_ref=shape_b_run_variants.name,
        source_label="Chrna2",
        edge_target="CS20230722_SUPT_0216",
        variant="chamberland_by_class",
        runs_root=tmp_path,
    )
    assert by_class["best_f1_score"] == pytest.approx(0.33)
    assert by_class["f1_source_relpath"] == "at_results_chamberland_by_class.yaml"


def test_load_result_set_missing_yaml_raises(tmp_path):
    run = tmp_path / "empty_run"
    run.mkdir()
    with pytest.raises(FileNotFoundError):
        at_metrics.load_result_set("empty_run", runs_root=tmp_path)


def test_load_result_set_unknown_variant_raises(
    shape_b_run_variants, tmp_path
):
    at_metrics.migrate_run(shape_b_run_variants)
    with pytest.raises(FileNotFoundError, match="variant"):
        at_metrics.load_result_set(
            shape_b_run_variants.name, variant="nonexistent", runs_root=tmp_path
        )


# ─── Refresh sweep ────────────────────────────────────────────────────


def test_refresh_kb_dry_run_does_not_write(
    tmp_path, shape_b_run, monkeypatch
):
    """refresh_kb in dry_run mode does not modify edge YAMLs."""
    at_metrics.migrate_run(shape_b_run)

    # Build a tiny KB graph using the migrated run
    kb_root = tmp_path / "kb_graphs"
    graph_path = kb_root / "demo.yaml"
    graph = {
        "edges": [
            {
                "id": "edge_demo_olm",
                "lit_type": "demo_olm",
                "taxonomy_type": "CS20230722_SUPT_0216",
                "evidence": [
                    {
                        "evidence_type": "ANNOTATION_TRANSFER",
                        "run_ref": shape_b_run.name,
                        "source_cluster_label": "Sst-OLM",
                        "supports": "PARTIAL",
                        "metrics_by_level": [
                            {
                                "taxonomy_level": "SUPERTYPE",
                                "best_target_accession": "CS20230722_SUPT_0219",
                                "best_target_name": "wrong",
                                "f1_score": 999.0,
                            },
                        ],
                    },
                ],
            },
        ],
    }
    _write(graph_path, yaml.safe_dump(graph))

    summary = at_metrics.refresh_kb(
        dry_run=True, kb_root=kb_root, runs_root=tmp_path
    )
    assert any("demo.yaml" in k for k in summary)
    # File unchanged
    reloaded = yaml.safe_load(graph_path.read_text())
    assert (
        reloaded["edges"][0]["evidence"][0]["metrics_by_level"][0]["f1_score"]
        == 999.0
    )


def test_refresh_kb_apply_rewrites_metrics(
    tmp_path, shape_b_run, fake_taxonomy_db
):
    """With dry_run=False, refresh writes the new metrics back."""
    at_metrics.migrate_run(shape_b_run)
    kb_root = tmp_path / "kb_graphs"
    graph_path = kb_root / "demo.yaml"
    _write(
        graph_path,
        yaml.safe_dump({
            "edges": [
                {
                    "id": "edge_demo_olm",
                    "lit_type": "demo_olm",
                    "taxonomy_type": "CS20230722_SUPT_0216",
                    "evidence": [
                        {
                            "evidence_type": "ANNOTATION_TRANSFER",
                            "run_ref": shape_b_run.name,
                            "source_cluster_label": "Sst-OLM",
                            "supports": "PARTIAL",
                            "metrics_by_level": [
                                {
                                    "taxonomy_level": "SUPERTYPE",
                                    "best_target_accession": "wrong",
                                    "best_target_name": "wrong",
                                    "f1_score": 999.0,
                                },
                            ],
                        },
                    ],
                },
            ],
        }),
    )
    at_metrics.refresh_kb(
        dry_run=False, kb_root=kb_root, runs_root=tmp_path
    )
    reloaded = yaml.safe_load(graph_path.read_text())
    ev = reloaded["edges"][0]["evidence"][0]
    levels = ev["metrics_by_level"]
    # Lineage-aware default: SUPT_0216's ancestors are CLAS_07,
    # SUBC_053, SUPT_0216. The fixture has all three rows for Sst-OLM,
    # so we expect 3 rows in metrics_by_level.
    assert len(levels) == 3
    accessions = [r["best_target_accession"] for r in levels]
    assert accessions == [
        "CS20230722_CLAS_07",
        "CS20230722_SUBC_053",
        "CS20230722_SUPT_0216",
    ]
    # f1_source_relpath now recorded
    assert ev["f1_source_relpath"] == "at_results.yaml"


def test_refresh_kb_skips_evidence_without_run_ref(tmp_path, shape_b_run):
    at_metrics.migrate_run(shape_b_run)
    kb_root = tmp_path / "kb_graphs"
    graph_path = kb_root / "demo.yaml"
    _write(
        graph_path,
        yaml.safe_dump({
            "edges": [{
                "id": "edge_demo",
                "lit_type": "demo",
                "taxonomy_type": "CS20230722_SUPT_0216",
                "evidence": [
                    {"evidence_type": "ANNOTATION_TRANSFER",
                     "source_cluster_label": "Sst-OLM"},  # no run_ref
                ],
            }]
        }),
    )
    summary = at_metrics.refresh_kb(
        dry_run=False, kb_root=kb_root, runs_root=tmp_path
    )
    # Default `only_with_run_ref=True` → evidence without run_ref is
    # silently skipped and the file contributes no rows → summary empty.
    assert summary == {}


# ─── Level-aware supports_default (issue #126 pt 5) ───────────────────


def test_supports_default_downgraded_for_coarse_only_cluster_edge(
    migrated_shape_b, fake_taxonomy_db, tmp_path
):
    """A cluster-level edge (rank 0) must NOT earn SUPPORT from a coarse
    subclass/supertype match when its own cluster-level F1 is weak.

    Sst-OLM → CLUS_0768: cluster F1 = 0.56 (< 0.6), while subclass = 0.68
    and supertype = 0.67. Global best is 0.68 (subclass, rank 2), but no
    row at the edge's own rank (0) clears 0.6 → PARTIAL, not SUPPORT.
    """
    payload = at_metrics.compute_edge_metrics(
        run_ref=migrated_shape_b.name,
        source_label="Sst-OLM",
        edge_target="CS20230722_CLUS_0768",
        runs_root=tmp_path,
        lineage_aware=True,
    )
    # Global best is still reported at the coarser level.
    assert payload["best_f1_score"] == pytest.approx(0.68)
    # But SUPPORT is gated on the edge's own rank or finer.
    assert payload["supports_default"] == "PARTIAL"


def test_supports_default_support_when_own_level_strong(
    migrated_shape_b, fake_taxonomy_db, tmp_path
):
    """A supertype-level edge (rank 1) whose own-level F1 clears 0.6 keeps
    SUPPORT even though a marginally-higher coarser row exists.

    Sst-OLM → SUPT_0216: supertype F1 = 0.67 (>= 0.6) → SUPPORT, despite
    subclass = 0.68 being the global best.
    """
    payload = at_metrics.compute_edge_metrics(
        run_ref=migrated_shape_b.name,
        source_label="Sst-OLM",
        edge_target="CS20230722_SUPT_0216",
        runs_root=tmp_path,
        lineage_aware=True,
    )
    assert payload["supports_default"] == "SUPPORT"


# ─── Run resolution: resolve_run_for_source + load_run_manifest ───────


def _make_run(
    tmp_path: Path, run_id: str, dataset: str, taxonomy: str, source_label: str,
    *, target_atlas: str = "WMBv1",
) -> None:
    """Create a minimal migrated AT run dir under tmp_path with a manifest
    carrying (source_dataset_accession, target_taxonomy_id, target_atlas)
    and one f1_matrix row for source_label."""
    run = tmp_path / run_id
    _write(
        run / "manifest.yaml",
        f"id: {run_id}\nrecord_type: AnnotationTransferRun\n"
        f"target_taxonomy_id: {taxonomy}\n"
        f"source_dataset_accession: {dataset}\n"
        f"target_atlas: {target_atlas}\n",
    )
    _write(
        run / "f1_matrix.csv",
        "source_label,level,target_name,n_cells,coverage,purity,f1,mean_boot,median_boot\n"
        f"{source_label},supertype,0216 Sst Gaba_3,22,0.96,0.51,0.67,0.99,1.0\n",
    )
    at_metrics.migrate_run(run)


def test_resolve_run_for_source_unique(tmp_path):
    _make_run(tmp_path, "at_run_20260101_a_mmc_wmbv1", "GEO:GSE1", "CCN20230722", "Foo")
    got = at_metrics.resolve_run_for_source(
        "GEO:GSE1", "CCN20230722", "Foo", runs_root=tmp_path
    )
    assert got == "at_run_20260101_a_mmc_wmbv1"


def test_resolve_run_for_source_disambiguates_by_label(tmp_path):
    """One dataset backs two runs with different source labelings. The
    (dataset, taxonomy) pair is non-unique — source_label is the real key."""
    _make_run(tmp_path, "at_run_20260101_coarse_mmc_wmbv1", "GEO:GSE9", "CCN20230722", "Coarse")
    _make_run(tmp_path, "at_run_20260202_fine_mmc_wmbv1", "GEO:GSE9", "CCN20230722", "Fine")
    assert at_metrics.resolve_run_for_source(
        "GEO:GSE9", "CCN20230722", "Fine", runs_root=tmp_path
    ) == "at_run_20260202_fine_mmc_wmbv1"
    assert at_metrics.resolve_run_for_source(
        "GEO:GSE9", "CCN20230722", "Coarse", runs_root=tmp_path
    ) == "at_run_20260101_coarse_mmc_wmbv1"


def test_resolve_run_for_source_tie_break_latest(tmp_path, capsys):
    """When two runs of the same dataset+taxonomy both contain the label,
    pick the latest by date-stamped id and warn."""
    _make_run(tmp_path, "at_run_20260101_v1_mmc_wmbv1", "GEO:GSE7", "CCN20230722", "Dup")
    _make_run(tmp_path, "at_run_20260303_v2_mmc_wmbv1", "GEO:GSE7", "CCN20230722", "Dup")
    got = at_metrics.resolve_run_for_source(
        "GEO:GSE7", "CCN20230722", "Dup", runs_root=tmp_path
    )
    assert got == "at_run_20260303_v2_mmc_wmbv1"
    assert "matched 2 runs" in capsys.readouterr().err


def test_resolve_run_for_source_none_when_label_absent(tmp_path):
    _make_run(tmp_path, "at_run_20260101_a_mmc_wmbv1", "GEO:GSE1", "CCN20230722", "Foo")
    # right dataset+taxonomy, wrong label
    assert at_metrics.resolve_run_for_source(
        "GEO:GSE1", "CCN20230722", "Missing", runs_root=tmp_path
    ) is None
    # wrong dataset
    assert at_metrics.resolve_run_for_source(
        "GEO:NOPE", "CCN20230722", "Foo", runs_root=tmp_path
    ) is None


def test_load_run_manifest(tmp_path):
    _make_run(tmp_path, "at_run_20260101_a_mmc_wmbv1", "GEO:GSE1", "CCN20230722",
              "Foo", target_atlas="WMBv2")
    manifest = at_metrics.load_run_manifest(
        "at_run_20260101_a_mmc_wmbv1", runs_root=tmp_path
    )
    assert manifest.get("target_atlas") == "WMBv2"
    assert at_metrics.load_run_manifest("nonexistent", runs_root=tmp_path) == {}


# ─── at_coverage (pre-mapping trigger check, issue #126 follow-up) ────


def _write_graph(tmp_path: Path, nodes: list[dict]) -> Path:
    g = tmp_path / "graph.yaml"
    _write(g, yaml.safe_dump({"name": "g", "nodes": nodes}))
    return g


def test_at_coverage_resolved_and_unresolved(tmp_path):
    _make_run(tmp_path, "at_run_20260101_a_mmc_wmbv1", "GEO:GSE1", "CCN20230722", "Foo")
    graph = _write_graph(tmp_path, [
        {"id": "classical_hit", "definition_basis": "CLASSICAL_MULTIMODAL",
         "at_source_sets": [{"dataset_accession": "GEO:GSE1", "source_label": "Foo"}]},
        {"id": "classical_miss", "definition_basis": "CLASSICAL_NEUROCHEMICAL",
         "at_source_sets": [{"dataset_accession": "GEO:GSE1", "source_label": "NopeLabel"}]},
        # atlas node with at_source_sets is ignored (not CLASSICAL)
        {"id": "atlas_node", "definition_basis": "ATLAS_TRANSCRIPTOMIC",
         "at_source_sets": [{"dataset_accession": "GEO:GSE1", "source_label": "Foo"}]},
        # classical node with no at_source_sets is skipped
        {"id": "classical_nodecl", "definition_basis": "CLASSICAL_ANATOMICAL"},
    ])
    rows = at_metrics.at_coverage(graph, "CCN20230722", runs_root=tmp_path)
    by_node = {r["node_id"]: r for r in rows}
    assert set(by_node) == {"classical_hit", "classical_miss"}
    assert by_node["classical_hit"]["run_ref"] == "at_run_20260101_a_mmc_wmbv1"
    assert by_node["classical_miss"]["run_ref"] is None


def test_at_coverage_empty_when_no_declarations(tmp_path):
    graph = _write_graph(tmp_path, [
        {"id": "c", "definition_basis": "CLASSICAL_MULTIMODAL"},
        {"id": "a", "definition_basis": "ATLAS_TRANSCRIPTOMIC"},
    ])
    assert at_metrics.at_coverage(graph, "CCN20230722", runs_root=tmp_path) == []


def test_format_at_coverage_flags_unresolved(tmp_path):
    rows = [
        {"node_id": "n1", "dataset_accession": "GEO:GSE1", "source_label": "Foo",
         "run_ref": "at_run_x"},
        {"node_id": "n2", "dataset_accession": "GEO:GSE1", "source_label": "Bar",
         "run_ref": None},
    ]
    out = at_metrics.format_at_coverage(rows, "CCN20230722")
    assert "UNRESOLVED" in out
    assert "1 UNRESOLVED" in out
    assert "at_run_x" in out


def test_format_at_coverage_empty_message():
    assert "Nothing to attempt" in at_metrics.format_at_coverage([], "CCN20230722")


# ─── at_hits_for_node (Stage A discovery, at_source_sets-driven) ──────


def test_at_hits_for_node_single_source(tmp_path):
    _make_run(tmp_path, "at_run_20260101_a_mmc_wmbv1", "GEO:GSE1", "CCN20230722", "Foo")
    hits = at_metrics.at_hits_for_node(
        [{"dataset_accession": "GEO:GSE1", "source_label": "Foo"}],
        "CCN20230722", runs_root=tmp_path,
    )
    # _make_run writes one supertype row (0216 Sst Gaba_3) at f1 0.67
    assert "CS20230722_SUPT_0216" in hits
    h = hits["CS20230722_SUPT_0216"]
    assert h["f1"] == pytest.approx(0.67)
    assert h["target_level"] == "supertype"
    assert h["source_label"] == "Foo"
    assert h["source_dataset_accession"] == "GEO:GSE1"


def test_at_hits_for_node_merges_multi_source_best_f1_wins(tmp_path):
    # Two sources, same dataset, that both land on the same accession at
    # different F1 — the higher-F1 hit must win.
    run = tmp_path / "at_run_20260101_multi_mmc_wmbv1"
    _write(
        run / "manifest.yaml",
        "id: at_run_20260101_multi_mmc_wmbv1\nrecord_type: AnnotationTransferRun\n"
        "target_taxonomy_id: CCN20230722\nsource_dataset_accession: GEO:GSE1\n",
    )
    _write(
        run / "f1_matrix.csv",
        "source_label,level,target_name,n_cells,coverage,purity,f1,mean_boot,median_boot\n"
        "Lo,supertype,0216 Sst Gaba_3,10,0.5,0.5,0.30,0.9,0.9\n"
        "Hi,supertype,0216 Sst Gaba_3,20,0.9,0.9,0.80,0.9,0.9\n",
    )
    at_metrics.migrate_run(run)
    hits = at_metrics.at_hits_for_node(
        [
            {"dataset_accession": "GEO:GSE1", "source_label": "Lo"},
            {"dataset_accession": "GEO:GSE1", "source_label": "Hi"},
        ],
        "CCN20230722", runs_root=tmp_path,
    )
    assert hits["CS20230722_SUPT_0216"]["f1"] == pytest.approx(0.80)
    assert hits["CS20230722_SUPT_0216"]["source_label"] == "Hi"


def test_at_hits_for_node_f1_floor_filters(tmp_path):
    run = tmp_path / "at_run_20260101_floor_mmc_wmbv1"
    _write(
        run / "manifest.yaml",
        "id: at_run_20260101_floor_mmc_wmbv1\nrecord_type: AnnotationTransferRun\n"
        "target_taxonomy_id: CCN20230722\nsource_dataset_accession: GEO:GSE1\n",
    )
    _write(
        run / "f1_matrix.csv",
        "source_label,level,target_name,n_cells,coverage,purity,f1,mean_boot,median_boot\n"
        "Foo,supertype,0216 Sst Gaba_3,10,0.5,0.5,0.30,0.9,0.9\n"
        "Foo,cluster,0768 Sst Gaba_3,3,0.1,0.1,0.05,0.9,0.9\n",
    )
    at_metrics.migrate_run(run)
    hits = at_metrics.at_hits_for_node(
        [{"dataset_accession": "GEO:GSE1", "source_label": "Foo"}],
        "CCN20230722", runs_root=tmp_path, f1_floor=0.2,
    )
    # 0.30 kept, 0.05 dropped by floor
    assert set(hits) == {"CS20230722_SUPT_0216"}


def test_at_hits_for_node_unresolved_source_skipped(tmp_path, capsys):
    _make_run(tmp_path, "at_run_20260101_a_mmc_wmbv1", "GEO:GSE1", "CCN20230722", "Foo")
    hits = at_metrics.at_hits_for_node(
        [{"dataset_accession": "GEO:NOPE", "source_label": "Foo"}],
        "CCN20230722", runs_root=tmp_path,
    )
    assert hits == {}
    assert "no AT run resolves" in capsys.readouterr().err


def test_at_hits_for_node_empty_when_no_source_sets(tmp_path):
    assert at_metrics.at_hits_for_node([], "CCN20230722", runs_root=tmp_path) == {}
