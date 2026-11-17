"""Gene identity layer: fetch, DB load, name resolution, hook check (#216)."""

from __future__ import annotations

import gzip
import json
import sqlite3
import urllib.error
from pathlib import Path

import h5py
import pytest

from evidencell import gene_identity as gi
from evidencell.gene_identity import (
    AMBIGUOUS,
    CASE_INSENSITIVE_SYMBOL,
    EXACT_SYMBOL,
    NO_MATCH,
    OVERRIDE,
    PINNED_ID,
    UNIQUE_SYNONYM,
    check_marker_gene_ids,
    load_gene_tables,
    marker_gene_ids,
    normalise_name,
    read_gene_ids,
    resolve_names,
    write_gene_ids,
)

_ROWS = [
    # ensembl, stats symbol, ncbi, label, synonyms
    ("ENSMUSG01", "Pvalb", "NCBIGene:19293", "Pvalb", ["PV", "parvalbumin"]),
    ("ENSMUSG02", "Calb1", "NCBIGene:12307", "Calb1", ["CB", "calbindin"]),
    ("ENSMUSG03", "Ctsb", "NCBIGene:13030", "Ctsb", ["CB", "cathepsin B"]),
    ("ENSMUSG04", "Car8", "NCBIGene:12319", "Ca8", ["CA-VIII"]),
    ("ENSMUSG05", "Htr3a", "NCBIGene:15561", "Htr3a", ["5-HT3a", "5HT3A"]),
    ("ENSMUSG06", "Gm1992", None, None, []),
    ("ENSMUSG07", "Sst", "NCBIGene:20604", "Sst", ["SST", "somatostatin"]),
]


def _rows() -> list[dict]:
    return [
        {
            "ensembl_id": e, "stats_symbol": s, "stats_col": i, "ncbi_gene_id": n,
            "label": lab, "taxon": "NCBITaxon:10090" if n else None,
            "equivalent_ids": ["MGI:1"] if n else [], "synonyms": [s, *syn] if n else [],
        }
        for i, (e, s, n, lab, syn) in enumerate(_ROWS)
    ]


@pytest.fixture
def tax_dir(tmp_path: Path) -> Path:
    d = tmp_path / "TAX"
    d.mkdir()
    write_gene_ids(d / "gene_ids.tsv.gz", {"taxonomy_id": "TAX", "stats_sha256": "abc"}, _rows())
    return d


@pytest.fixture
def con(tax_dir: Path):
    c = sqlite3.connect(":memory:")
    load_gene_tables(c, tax_dir)
    yield c
    c.close()


def test_normalise_name():
    assert normalise_name("5-HT3a") == "5ht3a"
    assert normalise_name("Calbindin D28k") == "calbindind28k"
    assert normalise_name("GAD_67") == "gad67"


def test_gene_ids_round_trip_and_is_deterministic(tmp_path, tax_dir):
    meta, rows = read_gene_ids(tax_dir / "gene_ids.tsv.gz")
    assert meta == {"taxonomy_id": "TAX", "stats_sha256": "abc"}
    assert rows[0]["synonyms"] == ["Pvalb", "PV", "parvalbumin"]
    assert rows[5]["ncbi_gene_id"] is None and rows[5]["stats_col"] == 5
    again = tmp_path / "again.tsv.gz"
    write_gene_ids(again, meta, rows)
    assert again.read_bytes() == (tax_dir / "gene_ids.tsv.gz").read_bytes()


def test_load_records_provenance_meta(con):
    assert gi.gene_ids_meta(con) == {"taxonomy_id": "TAX", "stats_sha256": "abc"}
    assert con.execute("SELECT COUNT(*) FROM genes").fetchone()[0] == len(_ROWS)


def test_no_gene_ids_file_leaves_tables_empty(tmp_path):
    c = sqlite3.connect(":memory:")
    assert load_gene_tables(c, tmp_path) == 0
    with pytest.raises(gi.GeneIdsUnavailable):
        resolve_names(c, ["Pvalb"])


@pytest.mark.parametrize(
    "name, method, symbol",
    [
        ("Pvalb", EXACT_SYMBOL, "Pvalb"),
        ("Car8", EXACT_SYMBOL, "Car8"),            # release-era stats symbol
        ("Ca8", EXACT_SYMBOL, "Car8"),             # current Translator label
        ("PVALB", CASE_INSENSITIVE_SYMBOL, "Pvalb"),
        ("PV", UNIQUE_SYNONYM, "Pvalb"),
        ("parvalbumin", UNIQUE_SYNONYM, "Pvalb"),
        ("5-HT3a", UNIQUE_SYNONYM, "Htr3a"),
        ("5HT3a", UNIQUE_SYNONYM, "Htr3a"),        # normalised synonym match
        ("Gm1992", EXACT_SYMBOL, "Gm1992"),        # no NCBIGene: Ensembl is the key
        ("SST", CASE_INSENSITIVE_SYMBOL, "Sst"),
    ],
)
def test_resolution_accepts(con, name, method, symbol):
    m = resolve_names(con, [name])[name]
    assert (m.method, m.gene.stats_symbol if m.gene else None) == (method, symbol)


def test_case_insensitive_symbol_beats_another_genes_synonym(tmp_path):
    d = tmp_path / "T2"
    d.mkdir()
    rows = _rows() + [{
        "ensembl_id": "ENSMUSG08", "stats_symbol": "Lmx1a", "stats_col": 7,
        "ncbi_gene_id": "NCBIGene:110648", "label": "Lmx1a", "taxon": "NCBITaxon:10090",
        "equivalent_ids": [], "synonyms": ["Lmx1a", "sst"],
    }]
    write_gene_ids(d / "gene_ids.tsv.gz", {}, rows)
    c = sqlite3.connect(":memory:")
    load_gene_tables(c, d)
    m = resolve_names(c, ["SST"])["SST"]
    assert (m.method, m.gene.stats_symbol) == (CASE_INSENSITIVE_SYMBOL, "Sst")
    assert [g.stats_symbol for g in m.claimants] == ["Lmx1a"]


def test_two_claimants_are_ambiguous_never_guessed(con):
    m = resolve_names(con, ["CB"])["CB"]
    assert m.method == AMBIGUOUS and m.gene is None
    assert sorted(c.stats_symbol for c in m.claimants) == ["Calb1", "Ctsb"]


def test_no_claimant_is_no_match(con):
    m = resolve_names(con, ["BrdU"])["BrdU"]
    assert m.method == NO_MATCH and m.gene is None and m.claimants == []


def test_pinned_id_wins(con):
    m = resolve_names(con, ["CB"], {"CB": "NCBIGene:12307"})["CB"]
    assert (m.method, m.gene.stats_symbol) == (PINNED_ID, "Calb1")


def test_pinned_id_of_another_species_falls_back_to_name(con):
    m = resolve_names(con, ["SST"], {"SST": "NCBIGene:6750"})["SST"]
    assert (m.method, m.gene.stats_symbol) == (CASE_INSENSITIVE_SYMBOL, "Sst")


def test_override_takes_precedence(tmp_path, tax_dir):
    (tax_dir / "gene_overrides.tsv").write_text(
        "# reviewed overrides\n"
        "name\tncbi_gene_id\tsymbol\trationale\treviewed_by\n"
        "CB\tNCBIGene:12307\tCalb1\tcalbindin in neuron papers\tDOS\n"
    )
    c = sqlite3.connect(":memory:")
    load_gene_tables(c, tax_dir)
    m = resolve_names(c, ["CB"])["CB"]
    assert (m.method, m.gene.stats_symbol) == (OVERRIDE, "Calb1")


def test_override_to_unknown_gene_is_rejected(tax_dir):
    (tax_dir / "gene_overrides.tsv").write_text(
        "name\tncbi_gene_id\tsymbol\trationale\treviewed_by\n"
        "CB\tNCBIGene:999\tX\twhy\tDOS\n"
    )
    with pytest.raises(ValueError, match="not a gene of this taxonomy"):
        load_gene_tables(sqlite3.connect(":memory:"), tax_dir)


def test_override_without_review_is_rejected(tax_dir):
    (tax_dir / "gene_overrides.tsv").write_text(
        "name\tncbi_gene_id\tsymbol\trationale\treviewed_by\n"
        "CB\tNCBIGene:12307\tCalb1\tcalbindin\t\n"
    )
    with pytest.raises(ValueError, match="reviewed_by"):
        load_gene_tables(sqlite3.connect(":memory:"), tax_dir)


def test_marker_gene_ids():
    node = {
        "defining_markers": [{"symbol": "PV", "ncbi_gene_id": "NCBIGene:19293"}, {"symbol": "X"}],
        "negative_markers": [{"symbol": "CB", "ncbi_gene_id": "NCBIGene:12307"}],
        "neuropeptides": ["Sst"],
    }
    assert marker_gene_ids(node) == {"PV": "NCBIGene:19293", "CB": "NCBIGene:12307"}


# ── Translator response parsing + fetch (network mocked) ─────────────────────


_NODENORM_PVALB = {
    "id": {"identifier": "NCBIGene:19293", "label": "Pvalb"},
    "equivalent_identifiers": [
        {"identifier": "NCBIGene:19293", "label": "Pvalb", "taxa": ["NCBITaxon:10090"]},
        {"identifier": "ENSEMBL:ENSMUSG00000005716", "label": "Pvalb (Mmus)"},
        {"identifier": "MGI:97821", "label": "Pvalb"},
    ],
    "taxa": ["NCBITaxon:10090"],
}


def test_nodenorm_parse():
    assert gi._ncbi_from_nodenorm(_NODENORM_PVALB) == {
        "ncbi_gene_id": "NCBIGene:19293", "label": "Pvalb",
        "taxon": "NCBITaxon:10090", "equivalent_ids": ["MGI:97821"],
    }
    assert gi._ncbi_from_nodenorm(None) is None


def test_fetch_strips_versions_and_keeps_prior_symbols(tmp_path, monkeypatch):
    stats = tmp_path / "s.h5"
    with h5py.File(stats, "w") as f:
        f["col_names"] = json.dumps(["ENSMUSG00000005716.5", "ENSMUSG00000099999"]).encode()
    out = tmp_path / "gene_ids.tsv.gz"
    write_gene_ids(out, {}, [{
        "ensembl_id": "ENSMUSG00000005716", "stats_symbol": "Pva", "stats_col": 0,
        "ncbi_gene_id": None, "label": None, "taxon": None, "equivalent_ids": [], "synonyms": [],
    }])
    seen: list[list[str]] = []

    def fake_nodenorm(curies, **kw):
        seen.append(curies)
        return {"ENSEMBL:ENSMUSG00000005716": gi._ncbi_from_nodenorm(_NODENORM_PVALB),
                "ENSEMBL:ENSMUSG00000099999": None}

    monkeypatch.setattr(gi, "nodenorm", fake_nodenorm)
    monkeypatch.setattr(
        gi, "nameres_synonyms", lambda ids, **kw: {"NCBIGene:19293": ["PV", "Pva"]}
    )
    monkeypatch.setattr(gi, "translator_versions", lambda: {"nodenorm_babel_version": "x"})
    gi.fetch_gene_ids("T", stats_path=stats, out_path=out)

    assert seen == [["ENSEMBL:ENSMUSG00000005716", "ENSEMBL:ENSMUSG00000099999"]]
    meta, rows = read_gene_ids(out)
    assert meta["stats_file"] == "s.h5" and meta["n_ncbi"] == "1"
    assert meta["nodenorm_babel_version"] == "x"
    assert rows[0]["stats_symbol"] == "Pva"  # a recorded name: stable across refreshes
    assert rows[0]["synonyms"] == ["PV", "Pva"]
    assert rows[1] == {
        "ensembl_id": "ENSMUSG00000099999", "stats_symbol": "ENSMUSG00000099999",
        "stats_col": 1, "ncbi_gene_id": None, "label": None, "taxon": None,
        "equivalent_ids": [], "synonyms": [],
    }


def test_resolve_for_curation_remote_counts_exact_name_claimants(monkeypatch):
    monkeypatch.setattr(gi, "nameres_lookup", lambda name, taxon, **kw: [
        {"ncbi_gene_id": "NCBIGene:25248", "label": "Cnr1", "taxa": [taxon]},
        {"ncbi_gene_id": "NCBIGene:83839", "label": "Calb1", "taxa": [taxon]},
        {"ncbi_gene_id": "NCBIGene:64529", "label": "Ctsb", "taxa": [taxon]},
    ])
    monkeypatch.setattr(gi, "nameres_synonyms", lambda ids, **kw: {
        "NCBIGene:25248": ["CB1", "cannabinoid receptor 1"],
        "NCBIGene:83839": ["CB", "calbindin"],
        "NCBIGene:64529": ["CB", "cathepsin B"],
    })
    out = gi.resolve_for_curation(["CB"], taxon="NCBITaxon:10116")[0]
    assert out["method"] == AMBIGUOUS
    assert [c["label"] for c in out["claimants"]] == ["Calb1", "Ctsb"]


def test_resolve_for_curation_local(tmp_path, tax_dir, monkeypatch):
    import evidencell.paths as paths_mod

    db = tmp_path / "TAX.db"
    with sqlite3.connect(db) as c:
        load_gene_tables(c, tax_dir)
    monkeypatch.setattr(paths_mod, "taxonomy_db_path", lambda tid: db)
    out = gi.resolve_for_curation(["PV", "CB"], taxonomy_id="TAX")
    assert out[0]["method"] == UNIQUE_SYNONYM and out[0]["gene"]["ncbi_gene_id"] == "NCBIGene:19293"
    assert out[1]["method"] == AMBIGUOUS and len(out[1]["claimants"]) == 2


# ── Hook check ───────────────────────────────────────────────────────────────


def _graph(symbol: str, gid: str, species: str | None = "NCBITaxon:10090") -> dict:
    node: dict = {"id": "n1", "defining_markers": [{"symbol": symbol, "ncbi_gene_id": gid}]}
    if species:
        node["species"] = {"id": species, "label": "x"}
    return {"nodes": [node]}


@pytest.fixture
def cache(tmp_path: Path) -> Path:
    p = tmp_path / "cache.json"
    p.write_text(json.dumps({
        "NCBIGene:19293": {"label": "Pvalb", "taxon": "NCBITaxon:10090",
                           "names": ["PV", "parvalbumin"]},
        "NCBIGene:5816": {"label": "PVALB", "taxon": "NCBITaxon:9606", "names": ["PV"]},
        "NCBIGene:999999999": {"missing": True},
    }))
    return p


def _check(doc, cache, tmp_path, taxslim=None):
    return check_marker_gene_ids(
        doc, cache_path=cache, taxonomy_root=tmp_path / "none",
        taxslim=taxslim or tmp_path / "no.obo",
    )


def test_hook_check_accepts_synonym_symbol(cache, tmp_path):
    assert _check(_graph("PV", "NCBIGene:19293"), cache, tmp_path) == ([], [])


def test_hook_check_rejects_nonexistent_id(cache, tmp_path):
    errors, _ = _check(_graph("PV", "NCBIGene:999999999"), cache, tmp_path)
    assert len(errors) == 1 and "does not resolve" in errors[0]


def test_hook_check_rejects_symbol_mismatch(cache, tmp_path):
    errors, _ = _check(_graph("Sst", "NCBIGene:19293"), cache, tmp_path)
    assert len(errors) == 1 and "'Sst' is not its label or a known synonym" in errors[0]


@pytest.fixture
def taxslim(tmp_path: Path, monkeypatch) -> Path:
    obo = tmp_path / "taxslim.obo"
    obo.write_text(
        "[Term]\nid: NCBITaxon:9606\nis_a: NCBITaxon:9605 ! Homo\n\n"
        "[Term]\nid: NCBITaxon:9605\nis_a: NCBITaxon:9443 ! Primates\n\n"
        "[Term]\nid: NCBITaxon:10090\nis_a: NCBITaxon:10088 ! Mus\n\n"
        "[Term]\nid: NCBITaxon:10116\nis_a: NCBITaxon:10114 ! Rattus\n"
    )
    monkeypatch.setattr(gi, "_TAXON_PARENTS", None)
    return obo


def test_hook_check_rejects_species_mismatch(cache, tmp_path, taxslim):
    errors, _ = _check(
        _graph("PV", "NCBIGene:19293", "NCBITaxon:10116"), cache, tmp_path, taxslim
    )
    assert len(errors) == 1 and "but the node's species is NCBITaxon:10116" in errors[0]


def test_hook_check_species_comes_from_graph_when_node_has_none(cache, tmp_path, taxslim):
    doc = _graph("PV", "NCBIGene:19293", species=None)
    doc["species"] = {"id": "NCBITaxon:10116"}
    errors, _ = _check(doc, cache, tmp_path, taxslim)
    assert len(errors) == 1 and "NCBITaxon:10116" in errors[0]


def test_hook_check_without_taxslim_reports_species_unchecked(cache, tmp_path, monkeypatch):
    monkeypatch.setattr(gi, "_TAXON_PARENTS", None)
    errors, unchecked = _check(_graph("PV", "NCBIGene:19293", "NCBITaxon:10116"), cache, tmp_path)
    assert errors == []
    assert unchecked and "just fetch-oak-dbs" in unchecked[0]


def test_hook_check_accepts_gene_of_descendant_taxon(cache, tmp_path, taxslim):
    obo = taxslim
    assert _check(_graph("PV", "NCBIGene:5816", "NCBITaxon:9443"), cache, tmp_path, obo)[0] == []
    errors, _ = _check(_graph("PV", "NCBIGene:5816", "NCBITaxon:10090"), cache, tmp_path, obo)
    assert errors and "NCBITaxon:9606 gene" in errors[0]


def test_hook_check_soft_skips_offline_uncached(cache, tmp_path, monkeypatch):
    def offline(*a, **kw):
        raise urllib.error.URLError("offline")

    monkeypatch.setattr(gi, "nodenorm", offline)
    errors, unchecked = _check(_graph("Gad1", "NCBIGene:14415"), cache, tmp_path)
    assert errors == [] and len(unchecked) == 1
    assert unchecked[0].startswith("NCBIGene:14415: Translator NodeNormalization unreachable")


def test_hook_check_looks_up_and_caches_new_ids(cache, tmp_path, monkeypatch):
    calls: list = []

    def fake_nodenorm(ids, **kw):
        calls.append(ids)
        return {"NCBIGene:14415": {"ncbi_gene_id": "NCBIGene:14415", "label": "Gad1",
                                   "taxon": "NCBITaxon:10090", "equivalent_ids": []}}

    monkeypatch.setattr(gi, "nodenorm", fake_nodenorm)
    monkeypatch.setattr(gi, "nameres_synonyms", lambda ids, **kw: {"NCBIGene:14415": ["GAD67"]})
    assert _check(_graph("GAD67", "NCBIGene:14415"), cache, tmp_path) == ([], [])
    assert _check(_graph("GAD67", "NCBIGene:14415"), cache, tmp_path) == ([], [])
    assert calls == [["NCBIGene:14415"]]  # second check served from the cache file
    assert json.loads(cache.read_text())["NCBIGene:14415"]["label"] == "Gad1"


def test_hook_check_seeds_from_committed_gene_ids(tmp_path, tax_dir, monkeypatch):
    def offline(*a, **kw):
        raise urllib.error.URLError("offline")

    monkeypatch.setattr(gi, "nodenorm", offline)
    errors, unchecked = check_marker_gene_ids(
        _graph("calbindin", "NCBIGene:12307"), cache_path=tmp_path / "c.json",
        taxonomy_root=tax_dir.parent, taxslim=tmp_path / "no.obo",
    )
    assert (errors, unchecked) == ([], [])


# ── Committed WMB gene table ─────────────────────────────────────────────────


def test_committed_wmb_gene_ids_cover_the_stats_genes():
    """Acceptance (#216): > 99% of stats genes have a key — NCBIGene, or the
    Ensembl ID as fallback — and the provenance header is complete."""
    path = Path(__file__).resolve().parents[1] / "kb" / "taxonomy" / "CCN20230722" / "gene_ids.tsv.gz"
    meta, rows = read_gene_ids(path)
    for k in ("stats_file", "stats_sha256", "fetched_at", "nodenorm_babel_version",
              "nameres_babel_version"):
        assert meta.get(k), k
    assert len(rows) == int(meta["n_genes"])
    assert [r["stats_col"] for r in rows] == list(range(len(rows)))
    assert all(r["ensembl_id"] and "." not in r["ensembl_id"] for r in rows)
    assert sum(1 for r in rows if r["ncbi_gene_id"]) / len(rows) > 0.7
    assert all(r["taxon"] in (None, "NCBITaxon:10090") for r in rows)
    with gzip.open(path, "rt") as fh:
        assert fh.readline().startswith("#taxonomy_id\tCCN20230722")


def test_choose_stats_symbol():
    # A rename the gene still lists is kept (WMB marker lists use Car8).
    assert gi.choose_stats_symbol("Car8", "Ca8", ["Car8", "CA-VIII"]) == "Car8"
    # A legacy symbol the gene doesn't go by is a mapping error: label wins.
    assert gi.choose_stats_symbol("Np65", "Ncam1", ["NCAM", "CD56"]) == "Ncam1"
    assert gi.choose_stats_symbol(None, "Ncam1", []) == "Ncam1"
    assert gi.choose_stats_symbol("Gm1992", None, []) == "Gm1992"


def test_nodenorm_label_without_ncbi_drops_taxon_suffix():
    entry = {
        "id": {"identifier": "ENSEMBL:ENSMUSG00000098760", "label": "Gm2164 (Mmus)"},
        "equivalent_identifiers": [{"identifier": "ENSEMBL:ENSMUSG00000098760"}],
    }
    assert gi._ncbi_from_nodenorm(entry)["label"] == "Gm2164"


def test_duplicate_symbol_prefers_the_gene_with_an_ncbi_id(tmp_path):
    d = tmp_path / "T3"
    d.mkdir()
    rows = _rows() + [
        {"ensembl_id": "ENSMUSG09", "stats_symbol": "Kiss1", "stats_col": 7,
         "ncbi_gene_id": "NCBIGene:280287", "label": "Kiss1", "taxon": "NCBITaxon:10090",
         "equivalent_ids": [], "synonyms": ["Kiss1"]},
        {"ensembl_id": "ENSMUSG10", "stats_symbol": "Kiss1", "stats_col": 8,
         "ncbi_gene_id": None, "label": None, "taxon": None,
         "equivalent_ids": [], "synonyms": []},
    ]
    write_gene_ids(d / "gene_ids.tsv.gz", {}, rows)
    c = sqlite3.connect(":memory:")
    load_gene_tables(c, d)
    m = resolve_names(c, ["Kiss1"])["Kiss1"]
    assert (m.method, m.gene.ensembl_id) == (EXACT_SYMBOL, "ENSMUSG09")


def test_hook_check_accepts_reviewed_override_name(cache, tmp_path):
    tax = tmp_path / "taxroot" / "T"
    tax.mkdir(parents=True)
    (tax / "gene_overrides.tsv").write_text(
        "name\tncbi_gene_id\tsymbol\trationale\treviewed_by\n"
        "Parv-ab\tNCBIGene:19293\tPvalb\tantibody name\tDOS\n"
    )
    errors, _ = check_marker_gene_ids(
        _graph("Parv-ab", "NCBIGene:19293"), cache_path=cache,
        taxonomy_root=tmp_path / "taxroot", taxslim=tmp_path / "no.obo",
    )
    assert errors == []
