"""On-demand expression accessor over the MapMyCells stats HDF5 (#189),
keyed by gene identity (#216)."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import h5py
import numpy as np
import pytest

from evidencell import expression_cache as ec
from evidencell.expression_cache import (
    AMBIGUOUS_SYMBOL,
    NO_ENSEMBL_MAPPING,
    ExpressionUnavailable,
)
from evidencell.gene_identity import load_gene_tables, write_gene_ids
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
_GENES = ["ENS_SST", "ENS_PVALB", "ENS_GAD1", "ENS_CALB1", "ENS_CTSB"]
# Per-cluster sums over cells; with n_cells below the means are:
#   CLUS_1 (n=2): Sst 10, Pvalb 0, Gad1 4, Calb1 1, Ctsb 3
#   CLUS_2 (n=1): Sst 4,  Pvalb 1, Gad1 4, Calb1 0, Ctsb 3
#   CLUS_3 (n=1): Sst 0,  Pvalb 6, Gad1 2, Calb1 5, Ctsb 3
_SUMS = np.array([
    [20.0, 0.0, 8.0, 2.0, 6.0],
    [4.0, 1.0, 4.0, 0.0, 3.0],
    [0.0, 6.0, 2.0, 5.0, 3.0],
])
_N_CELLS = np.array([2, 1, 1])
_GENE_ROWS = [
    # ensembl, symbol, ncbi, synonyms — "CB" is claimed by Calb1 and Ctsb
    ("ENS_SST", "Sst", "NCBIGene:20604", ["SST", "somatostatin"]),
    ("ENS_PVALB", "Pvalb", "NCBIGene:19293", ["PV", "parvalbumin"]),
    ("ENS_GAD1", "Gad1", "NCBIGene:14415", ["GAD67"]),
    ("ENS_CALB1", "Calb1", "NCBIGene:12307", ["CB", "calbindin"]),
    ("ENS_CTSB", "Ctsb", "NCBIGene:13030", ["CB", "cathepsin B"]),
]


def _write_stats(path: Path, sums: np.ndarray = _SUMS) -> Path:
    with h5py.File(path, "w") as f:
        f["col_names"] = json.dumps(_GENES).encode()
        f["cluster_to_row"] = json.dumps({"CLUS_1": 0, "CLUS_2": 1, "CLUS_3": 2}).encode()
        f["n_cells"] = _N_CELLS
        f["sum"] = sums
    return path


def _write_gene_ids(tax_dir: Path, stats: Path) -> None:
    write_gene_ids(
        tax_dir / "gene_ids.tsv.gz",
        {"taxonomy_id": "TINY", "stats_file": stats.name, "stats_sha256": ec._sha256(stats)},
        [
            {
                "ensembl_id": ens, "stats_symbol": sym, "stats_col": i, "ncbi_gene_id": ncbi,
                "label": sym, "taxon": "NCBITaxon:10090", "equivalent_ids": [],
                "synonyms": [sym, *syns],
            }
            for i, (ens, sym, ncbi, syns) in enumerate(_GENE_ROWS)
        ],
    )


@pytest.fixture
def stats(tmp_path: Path) -> Path:
    return _write_stats(tmp_path / "tiny_stats.h5")


@pytest.fixture
def tax_dir(tmp_path: Path, stats: Path) -> Path:
    d = tmp_path / "TINY"
    d.mkdir()
    _write_gene_ids(d, stats)
    return d


def _make_db(path: Path, tax_dir: Path, stats: Path) -> TaxonomyDB:
    with sqlite3.connect(path) as con:
        con.executescript(_DDL)
        con.executemany(
            "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, parent_id, "
            "taxonomy_rank, taxonomy_level) VALUES (?, ?, ?, 'TINY', ?, ?, ?)",
            [(n, n, n, parent, rank, level) for n, parent, rank, level in _NODES],
        )
        load_gene_tables(con, tax_dir)
        con.commit()
    return TaxonomyDB(path, stats_path=stats)


@pytest.fixture
def db(tmp_path: Path, tax_dir: Path, stats: Path) -> TaxonomyDB:
    return _make_db(tmp_path / "TINY.db", tax_dir, stats)


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


def test_only_requested_genes_are_cached_by_ensembl_id(db):
    db.expression(["Sst"])
    with db._connect() as con:
        cached = {r[0] for r in con.execute("SELECT ensembl_id FROM expression_genes")}
        genes = {r[0] for r in con.execute("SELECT DISTINCT ensembl_id FROM node_expression")}
    assert cached == {"ENS_SST"} and genes == {"ENS_SST"}


def test_names_for_one_gene_share_one_cache_entry(db):
    out = db.expression(["Pvalb", "PV", "parvalbumin"], accessions=["CLUS_3"])
    assert out.values == {"CLUS_3": {"Pvalb": 6.0, "PV": 6.0, "parvalbumin": 6.0}}
    assert {n: m.method for n, m in out.genes.items()} == {
        "Pvalb": "EXACT_SYMBOL", "PV": "UNIQUE_SYNONYM", "parvalbumin": "UNIQUE_SYNONYM",
    }
    assert out.gene_symbol("PV") == "Pvalb"
    with db._connect() as con:
        assert con.execute("SELECT COUNT(*) FROM expression_genes").fetchone()[0] == 1


def test_cached_genes_are_served_without_the_stats_file(db, stats):
    db.expression(["Sst"])
    stats.unlink()
    out = db.expression(["SST"], accessions=["CLUS_1"])  # another name, same gene
    assert out.values == {"CLUS_1": {"SST": 10.0}}


def test_missing_stats_file_fails_closed_with_fetch_command(db, stats):
    stats.unlink()
    with pytest.raises(ExpressionUnavailable, match="just fetch-mapmycells TINY"):
        db.expression(["Sst"])


def test_missing_gene_tables_fail_closed(tmp_path, stats):
    empty = tmp_path / "EMPTY"
    empty.mkdir()
    db = _make_db(tmp_path / "E.db", empty, stats)
    with pytest.raises(ExpressionUnavailable, match="just build-gene-ids"):
        db.expression(["Sst"])


def test_unmeasurable_names_are_recorded_not_silent(db):
    out = db.expression(["Sst", "Nosuchgene", "CB"])
    assert out.not_measured == {"Nosuchgene": NO_ENSEMBL_MAPPING, "CB": AMBIGUOUS_SYMBOL}
    assert [c.stats_symbol for c in out.genes["CB"].claimants] == ["Calb1", "Ctsb"]
    assert all("CB" not in v and "Nosuchgene" not in v for v in out.values.values())


def test_curated_ncbi_gene_id_settles_an_ambiguous_name(db):
    out = db.expression(["CB"], accessions=["CLUS_3"], gene_ids={"CB": "NCBIGene:12307"})
    assert out.not_measured == {}
    assert out.values == {"CLUS_3": {"CB": 5.0}}
    assert out.genes["CB"].method == "PINNED_ID"


def test_foreign_species_id_falls_back_to_the_name(db):
    """A human SST ID isn't a mouse gene: the name resolves instead."""
    out = db.expression(["SST"], accessions=["CLUS_1"], gene_ids={"SST": "NCBIGene:6750"})
    assert out.values == {"CLUS_1": {"SST": 10.0}}
    assert out.genes["SST"].method == "CASE_INSENSITIVE_SYMBOL"


def test_override_settles_an_ambiguous_name(tmp_path, tax_dir, stats):
    (tax_dir / "gene_overrides.tsv").write_text(
        "name\tncbi_gene_id\tsymbol\trationale\treviewed_by\n"
        "CB\tNCBIGene:12307\tCalb1\tcalbindin in neuron papers\ttest\n"
    )
    db = _make_db(tmp_path / "O.db", tax_dir, stats)
    out = db.expression(["CB"], accessions=["CLUS_3"])
    assert out.values == {"CLUS_3": {"CB": 5.0}}
    assert out.genes["CB"].method == "OVERRIDE"


def test_new_stats_release_is_refused_until_gene_ids_refresh(db, stats):
    """A stats file other than the one gene_ids.tsv.gz was built from can't
    be trusted: its columns may have moved."""
    db.expression(["Sst"])
    _write_stats(stats, sums=_SUMS * 2)
    with pytest.raises(ExpressionUnavailable, match="just build-gene-ids TINY"):
        db.expression(["Pvalb"])
    with db._connect() as con:  # the stale cache was dropped, not served
        assert con.execute("SELECT COUNT(*) FROM expression_genes").fetchone()[0] == 0


def test_new_stats_release_reloads_after_gene_ids_refresh(tmp_path, db, tax_dir, stats):
    db.expression(["Sst", "Pvalb"])
    _write_stats(stats, sums=_SUMS * 2)
    _write_gene_ids(tax_dir, stats)
    db = _make_db(tmp_path / "R.db", tax_dir, stats)
    assert db.expression(["Sst"], accessions=["CLUS_2"]).values == {"CLUS_2": {"Sst": 8.0}}


def test_column_mismatch_is_refused(tmp_path, tax_dir, stats):
    """gene_ids rows must point at their own Ensembl column."""
    with h5py.File(stats, "r+") as f:
        del f["col_names"]
        f["col_names"] = json.dumps(list(reversed(_GENES))).encode()
    meta_free = tmp_path / "NOMETA"
    meta_free.mkdir()
    write_gene_ids(
        meta_free / "gene_ids.tsv.gz", {},
        [{"ensembl_id": "ENS_SST", "stats_symbol": "Sst", "stats_col": 0,
          "ncbi_gene_id": "NCBIGene:20604", "label": "Sst", "taxon": None,
          "equivalent_ids": [], "synonyms": []}],
    )
    db = _make_db(tmp_path / "M.db", meta_free, stats)
    with pytest.raises(ExpressionUnavailable, match="column 0 is not ENS_SST"):
        db.expression(["Sst"])


def test_stats_hash_is_memoised_by_size_and_mtime(db, stats, monkeypatch):
    db.expression(["Sst"])
    calls: list[Path] = []
    monkeypatch.setattr(ec, "_sha256", lambda p: calls.append(p) or "x")
    db.expression(["Sst"])
    assert calls == []


def test_rows_must_match_taxonomy(tmp_path, tax_dir):
    stats = tmp_path / "other.h5"
    with h5py.File(stats, "w") as f:
        f["col_names"] = json.dumps(_GENES).encode()
        f["cluster_to_row"] = json.dumps({"OTHER_1": 0}).encode()
        f["n_cells"] = np.array([1])
        f["sum"] = np.zeros((1, 5))
    other = tmp_path / "OTHER"
    other.mkdir()
    _write_gene_ids(other, stats)
    path = tmp_path / "T.db"
    with sqlite3.connect(path) as con:
        con.executescript(_DDL)
        con.execute(
            "INSERT INTO nodes(node_id, short_form, label, taxonomy_id, taxonomy_rank, "
            "taxonomy_level) VALUES ('CLUS_1', 'CLUS_1', 'c', 'T', 0, 'cluster')"
        )
        load_gene_tables(con, other)
    db = TaxonomyDB(path, stats_path=stats)
    with pytest.raises(ExpressionUnavailable, match="cluster_to_row"):
        db.expression(["Sst"])


def test_build_from_yaml_ignores_yaml_expression(tmp_path):
    """#189: build-taxonomy-db no longer loads expression; cache starts empty.
    #216: it loads the gene tables when gene_ids.tsv.gz is present."""
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
    stats = _write_stats(tmp_path / "s.h5")
    _write_gene_ids(tax_dir, stats)
    db = TaxonomyDB(tmp_path / "TINY.db")
    db.build_from_yaml(tax_dir)
    with db._connect() as con:
        assert con.execute("SELECT COUNT(*) FROM nodes").fetchone()[0] == 1
        assert con.execute("SELECT COUNT(*) FROM node_expression").fetchone()[0] == 0
        assert con.execute("SELECT COUNT(*) FROM expression_genes").fetchone()[0] == 0
        assert con.execute("SELECT COUNT(*) FROM genes").fetchone()[0] == len(_GENE_ROWS)


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
