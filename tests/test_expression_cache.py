"""On-demand expression accessor over the MapMyCells stats HDF5 (#189)."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import h5py
import numpy as np
import pytest

from evidencell import expression_cache as ec
from evidencell.expression_cache import (
    NO_ENSEMBL_MAPPING,
    NOT_IN_STATS,
    ExpressionUnavailable,
)
from evidencell.taxonomy_db import _DDL, TaxonomyDB

# Tiny taxonomy: SUBC_1 ─┬─ SUPT_1 ─┬─ CLUS_1
#                        │          └─ CLUS_2
#                        └─ SUPT_2 ─── CLUS_3
_NODES = [
    # node_id, parent_id, rank, level
    ("SUBC_1", None, 2, "subclass"),
    ("SUPT_1", "SUBC_1", 1, "supertype"),
    ("SUPT_2", "SUBC_1", 1, "supertype"),
    ("CLUS_1", "SUPT_1", 0, "cluster"),
    ("CLUS_2", "SUPT_1", 0, "cluster"),
    ("CLUS_3", "SUPT_2", 0, "cluster"),
]
_GENES = ["ENS_SST", "ENS_PVALB", "ENS_GAD1"]
# Per-cluster sums over cells; with n_cells below the means are:
#   CLUS_1 (n=2): Sst 10, Pvalb 0,   Gad1 4
#   CLUS_2 (n=1): Sst 4,  Pvalb 1,   Gad1 4
#   CLUS_3 (n=1): Sst 0,  Pvalb 6,   Gad1 2
_SUMS = np.array([
    [20.0, 0.0, 8.0],
    [4.0, 1.0, 4.0],
    [0.0, 6.0, 2.0],
])
_N_CELLS = np.array([2, 1, 1])


def _write_stats(path: Path, sums: np.ndarray = _SUMS) -> Path:
    with h5py.File(path, "w") as f:
        f["col_names"] = json.dumps(_GENES).encode()
        f["cluster_to_row"] = json.dumps({"CLUS_1": 0, "CLUS_2": 1, "CLUS_3": 2}).encode()
        f["n_cells"] = _N_CELLS
        f["sum"] = sums
    return path


@pytest.fixture
def stats(tmp_path: Path) -> Path:
    return _write_stats(tmp_path / "tiny_stats.h5")


@pytest.fixture
def mapping(tmp_path: Path) -> Path:
    p = tmp_path / "gene_mapping.tsv"
    p.write_text(
        "ensembl_id\tsymbol\n"
        "ENS_SST\tSst\n"
        "ENS_PVALB\tPvalb\n"
        "ENS_GAD1\tGad1\n"
        "ENS_GHOST\tGhost\n"  # mapped, but absent from the stats file
    )
    return p


@pytest.fixture
def db(tmp_path: Path, stats: Path, mapping: Path) -> TaxonomyDB:
    path = tmp_path / "TINY.db"
    with sqlite3.connect(path) as con:
        con.executescript(_DDL)
        con.executemany(
            "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, parent_id, "
            "taxonomy_rank, taxonomy_level) VALUES (?, ?, ?, 'TINY', ?, ?, ?)",
            [(n, n, n, parent, rank, level) for n, parent, rank, level in _NODES],
        )
        con.commit()
    return TaxonomyDB(path, stats_path=stats, gene_mapping_path=mapping)


def test_leaf_values_are_sum_over_n_cells(db):
    out = db.expression(["Sst", "Gad1"], ranks=[0])
    assert out.values == {
        "CLUS_1": {"Sst": 10.0, "Gad1": 4.0},
        "CLUS_2": {"Sst": 4.0, "Gad1": 4.0},
        "CLUS_3": {"Sst": 0.0, "Gad1": 2.0},
    }
    assert out.not_measured == {}
    assert out.source_file == "tiny_stats.h5"


def test_non_leaf_values_are_n_cells_weighted_means_of_leaves(db):
    out = db.expression(["Sst"], ranks=[1, 2])
    # SUPT_1: (20 + 4) / (2 + 1) = 8; SUPT_2: 0; SUBC_1: 24 / 4 = 6
    assert out.values["SUPT_1"]["Sst"] == pytest.approx(8.0)
    assert out.values["SUPT_2"]["Sst"] == pytest.approx(0.0)
    assert out.values["SUBC_1"]["Sst"] == pytest.approx(6.0)


def test_accession_filter_and_prefix(db):
    out = db.expression(["Pvalb"], accessions=["CCN:CLUS_3"])
    assert out.values == {"CLUS_3": {"Pvalb": 6.0}}
    assert out.for_node("CCN:CLUS_3") == {"Pvalb": 6.0}


def test_only_requested_genes_are_cached(db):
    db.expression(["Sst"])
    with db._connect() as con:
        cached = {r[0] for r in con.execute("SELECT symbol FROM expression_genes")}
        symbols = {r[0] for r in con.execute("SELECT DISTINCT symbol FROM node_expression")}
    assert cached == {"Sst"} and symbols == {"Sst"}


def test_cached_genes_are_served_without_the_stats_file(db, stats):
    db.expression(["Sst"])
    stats.unlink()
    out = db.expression(["Sst"], accessions=["CLUS_1"])
    assert out.values == {"CLUS_1": {"Sst": 10.0}}


def test_missing_stats_file_fails_closed_with_fetch_command(db, stats):
    stats.unlink()
    with pytest.raises(ExpressionUnavailable, match="just fetch-mapmycells TINY"):
        db.expression(["Sst"])


def test_missing_gene_mapping_fails_closed(db, mapping):
    mapping.unlink()
    with pytest.raises(ExpressionUnavailable, match="just generate-gene-mapping"):
        db.expression(["Sst"])


def test_unmeasurable_genes_are_recorded_not_silent(db):
    out = db.expression(["Sst", "Nosuchgene", "Ghost"])
    assert out.not_measured == {"Nosuchgene": NO_ENSEMBL_MAPPING, "Ghost": NOT_IN_STATS}
    assert all("Ghost" not in v and "Nosuchgene" not in v for v in out.values.values())
    # Recorded in the cache, so a later call reports them without reloading.
    with db._connect() as con:
        statuses = dict(con.execute("SELECT symbol, status FROM expression_genes"))
    assert statuses == {"Sst": "MEASURED", "Nosuchgene": NO_ENSEMBL_MAPPING, "Ghost": NOT_IN_STATS}


def test_protein_alias_resolves_to_gene(db):
    out = db.expression(["PV"], accessions=["CLUS_3"])
    assert out.values == {"CLUS_3": {"PV": 6.0}}


def test_new_stats_release_drops_and_reloads_cache(db, stats):
    db.expression(["Sst", "Pvalb"])
    _write_stats(stats, sums=_SUMS * 2)
    out = db.expression(["Sst"], accessions=["CLUS_2"])
    assert out.values == {"CLUS_2": {"Sst": 8.0}}
    with db._connect() as con:
        cached = {r[0] for r in con.execute("SELECT symbol FROM expression_genes")}
    assert cached == {"Sst"}  # Pvalb dropped with the stale release; reloads on use


def test_regenerated_gene_mapping_drops_not_measured(db, mapping):
    """#189 review: a NO_ENSEMBL_MAPPING row must not outlive a fix to the
    gene mapping TSV."""
    assert db.expression(["Nosuchgene"]).not_measured == {"Nosuchgene": NO_ENSEMBL_MAPPING}
    mapping.write_text(mapping.read_text() + "ENS_GAD1\tNosuchgene\n")
    out = db.expression(["Nosuchgene"], accessions=["CLUS_3"])
    assert out.not_measured == {}
    assert out.values == {"CLUS_3": {"Nosuchgene": 2.0}}


def test_alias_table_change_drops_not_measured(db, monkeypatch):
    """#189 review: likewise for a new PROTEIN_TO_GENE_ALIASES entry."""
    from evidencell import marker_aliases

    assert db.expression(["GAD-1"]).not_measured == {"GAD-1": NO_ENSEMBL_MAPPING}
    monkeypatch.setitem(marker_aliases.PROTEIN_TO_GENE_ALIASES, "GAD-1", "Gad1")
    out = db.expression(["GAD-1"], accessions=["CLUS_3"])
    assert out.not_measured == {}
    assert out.values == {"CLUS_3": {"GAD-1": 2.0}}


def test_unchanged_resolution_keeps_the_cache(db, stats):
    db.expression(["Sst"])
    stats.unlink()  # a reload would now fail closed
    assert db.expression(["Sst"], accessions=["CLUS_1"]).values == {"CLUS_1": {"Sst": 10.0}}


def test_stats_hash_is_memoised_by_size_and_mtime(db, stats, monkeypatch):
    db.expression(["Sst"])
    calls: list[Path] = []
    monkeypatch.setattr(ec, "_sha256", lambda p: calls.append(p) or "x")
    db.expression(["Gad1"])
    assert calls == []


def test_rows_must_match_taxonomy(tmp_path, mapping):
    stats = tmp_path / "other.h5"
    with h5py.File(stats, "w") as f:
        f["col_names"] = json.dumps(_GENES).encode()
        f["cluster_to_row"] = json.dumps({"OTHER_1": 0}).encode()
        f["n_cells"] = np.array([1])
        f["sum"] = np.zeros((1, 3))
    path = tmp_path / "T.db"
    with sqlite3.connect(path) as con:
        con.executescript(_DDL)
        con.execute(
            "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, taxonomy_rank, "
            "taxonomy_level) VALUES ('CLUS_1', 'CLUS_1', 'c', 'T', 0, 'cluster')"
        )
    db = TaxonomyDB(path, stats_path=stats, gene_mapping_path=mapping)
    with pytest.raises(ExpressionUnavailable, match="cluster_to_row"):
        db.expression(["Sst"])


def test_build_from_yaml_ignores_yaml_expression(tmp_path):
    """#189: build-taxonomy-db no longer loads expression; cache starts empty."""
    import yaml

    tax_dir = tmp_path / "TINY"
    tax_dir.mkdir()
    (tax_dir / "cluster.yaml").write_text(yaml.safe_dump({
        "taxonomy_id": "TINY",
        "taxonomy_rank": 0,
        "nodes": [{
            "id": "TINY:CLUS_1",
            "name": "c1",
            "cell_set_accession": "CLUS_1",
            "taxonomy_id": "TINY",
            "taxonomy_level": "CLUSTER",
            "precomputed_expression": {
                "source": "old.h5",
                "genes": [{"symbol": "Sst", "mean_expression": 9.0}],
            },
        }],
    }))
    db = TaxonomyDB(tmp_path / "TINY.db")
    db.build_from_yaml(tax_dir)
    with db._connect() as con:
        assert con.execute("SELECT COUNT(*) FROM nodes").fetchone()[0] == 1
        assert con.execute("SELECT COUNT(*) FROM node_expression").fetchone()[0] == 0
        assert con.execute("SELECT COUNT(*) FROM expression_genes").fetchone()[0] == 0


def test_stats_path_comes_from_registry(monkeypatch, tmp_path):
    import evidencell.paths as paths_mod

    monkeypatch.setattr(paths_mod, "repo_root", lambda: Path(__file__).resolve().parents[1])
    p = ec.stats_h5_path("CCN20230722")
    assert p.parts[-3:] == ("mapmycells", "CCN20230722", "precomputed_stats_ABC_revision_230821.h5")
    with pytest.raises(ExpressionUnavailable, match="No MapMyCells stats file is registered"):
        ec.stats_h5_path("NOT_A_TAXONOMY")


# ── Real-data regression (#189) ──────────────────────────────────────────────

_REGRESSION_FIXTURE = Path(__file__).parent / "fixtures" / "expression_regression_CCN20230722.json"


@pytest.mark.integration
def test_accessor_matches_former_yaml_values_on_wmb():
    """The accessor reproduces the precomputed_expression values that lived
    in kb/taxonomy/CCN20230722 YAML before #189 (a frozen 50-node × 14-gene
    sample; the full 697,961-value comparison was run when the blocks were
    removed). Needs the WMB stats file and a built taxonomy DB."""
    from evidencell.paths import taxonomy_db_path

    db_path = taxonomy_db_path("CCN20230722")
    stats = ec.stats_h5_path("CCN20230722")
    if not stats.is_file() or not db_path.is_file():
        pytest.skip("needs `just fetch-mapmycells CCN20230722` and `just build-taxonomy-db CCN20230722`")
    ref = json.loads(_REGRESSION_FIXTURE.read_text())
    expected = ref["values"]
    genes = sorted({g for v in expected.values() for g in v})
    out = TaxonomyDB(db_path).expression(genes, accessions=list(expected))
    assert out.source_file == ref["stats_file"]
    for node, vals in expected.items():
        for gene, val in vals.items():
            assert round(out.values[node][gene], 2) == pytest.approx(val, abs=0.0051), (node, gene)
