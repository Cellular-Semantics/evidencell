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
    CONFLICT,
    CONFLICTING_PINS,
    EXACT_SYMBOL,
    NO_GENE,
    NO_GENE_ID,
    NO_MATCH,
    PIN_NOT_IN_TAXONOMY,
    PINNED_ID,
    PINNED_SYMBOL,
    UNIQUE_SYNONYM,
    GeneIdsUnavailable,
    Pin,
    check_marker_gene_ids,
    load_gene_tables,
    marker_display,
    marker_gene_ids,
    marker_name,
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


def test_pin_without_symbol_is_never_resolved_by_name(con):
    """Review #1: a pin missing from the taxonomy, with no official symbol,
    fails visibly — it does not fall back to the marker's wording."""
    m = resolve_names(con, ["SST"], {"SST": "NCBIGene:6750"})["SST"]
    assert m.method == PIN_NOT_IN_TAXONOMY and m.gene is None


def test_pin_of_another_species_resolves_by_official_symbol(con):
    """A rat CB marker pinned to rat Calb1 reaches mouse Calb1 through its
    official symbol, not the ambiguous source wording (#244)."""
    m = resolve_names(con, ["CB"], {"CB": Pin("NCBIGene:83839", "Calb1")})["CB"]
    assert (m.method, m.gene.stats_symbol) == (PINNED_SYMBOL, "Calb1")


def test_pin_of_another_species_matches_its_symbol_ignoring_case(con):
    """Human PVALB on a mouse taxonomy reaches Pvalb."""
    m = resolve_names(con, ["PV"], {"PV": Pin("NCBIGene:5816", "PVALB")})["PV"]
    assert (m.method, m.gene.stats_symbol) == (PINNED_SYMBOL, "Pvalb")


@pytest.mark.parametrize("symbol", ["parvalbumin", "Sst1"])
def test_pin_symbol_fallback_never_uses_synonyms(con, symbol):
    """Review #1: the fallback is the official symbol only. A symbol that is
    merely some gene's synonym (or nobody's) is PIN_NOT_IN_TAXONOMY, never a
    UNIQUE_SYNONYM guess."""
    m = resolve_names(con, ["x"], {"x": Pin("NCBIGene:1", symbol)})["x"]
    assert m.method == PIN_NOT_IN_TAXONOMY and m.gene is None


def test_pin_not_in_taxonomy_is_reported_as_its_own_reason(con):
    from evidencell import expression_cache as ec

    matches = resolve_names(con, ["x"], {"x": Pin("NCBIGene:1", None)})
    assert ec.query(con, matches).not_measured == {"x": ec.PIN_NOT_IN_TAXONOMY}


def test_missing_gene_tables_message_names_the_taxonomy():
    """Review #9: the message carries the taxonomy id, not a literal {tid}."""
    c = sqlite3.connect(":memory:")
    with pytest.raises(GeneIdsUnavailable) as exc:
        resolve_names(c, ["Pvalb"], taxonomy_id="CCN20250428")
    msg = str(exc.value)
    assert "{tid}" not in msg and msg.count("CCN20250428") == 3


def test_curated_marker_without_gene_is_not_resolved_by_name(con):
    m = resolve_names(con, ["PV"], {"PV": NO_GENE})["PV"]
    assert m.method == NO_GENE_ID and m.gene is None


def test_no_taxonomy_wide_name_overrides(tax_dir):
    """A name several genes claim stays AMBIGUOUS whatever files sit in the
    taxonomy dir: it is settled per marker (symbol + ncbi_gene_id), not by a
    taxonomy-wide table (gene_overrides.tsv was removed)."""
    (tax_dir / "gene_overrides.tsv").write_text(
        "name\tncbi_gene_id\tsymbol\trationale\treviewed_by\n"
        "CB\tNCBIGene:12307\tCalb1\tcalbindin in neuron papers\tDOS\n"
    )
    c = sqlite3.connect(":memory:")
    load_gene_tables(c, tax_dir)
    m = resolve_names(c, ["CB"])["CB"]
    assert m.method == AMBIGUOUS and m.gene is None


def test_marker_gene_ids():
    node = {
        "defining_markers": [
            {"name_in_source": "PV", "symbol": "Pvalb", "ncbi_gene_id": "NCBIGene:19293"},
            {"name_in_source": "PSA-NCAM"},
        ],
        "negative_markers": [
            {"name_in_source": "CB", "symbol": "Calb1", "ncbi_gene_id": "NCBIGene:12307"},
        ],
        "neuropeptides": ["Sst"],
    }
    assert marker_gene_ids(node) == {
        "PV": Pin("NCBIGene:19293", "Pvalb"),
        "PSA-NCAM": NO_GENE,
        "CB": Pin("NCBIGene:12307", "Calb1"),
    }


def test_markers_sharing_a_name_keep_their_own_pins():
    """Review #3: one node's CB (Calb1) and CB (Cnr1) must not share a pin.
    Neither is measured rather than one gene standing for both."""
    node = {
        "defining_markers": [
            {"name_in_source": "CB", "symbol": "Calb1", "ncbi_gene_id": "NCBIGene:12307"},
        ],
        "negative_markers": [
            {"name_in_source": "CB", "symbol": "Cnr1", "ncbi_gene_id": "NCBIGene:12801"},
        ],
    }
    assert marker_gene_ids(node) == {"CB": CONFLICT}


def test_same_pin_twice_is_not_a_conflict():
    pv = {"name_in_source": "PV", "symbol": "Pvalb", "ncbi_gene_id": "NCBIGene:19293"}
    node = {"defining_markers": [pv], "neuropeptides": [dict(pv)]}
    assert marker_gene_ids(node) == {"PV": Pin("NCBIGene:19293", "Pvalb")}


def test_conflicting_pins_are_not_measured(con):
    from evidencell import expression_cache as ec

    matches = resolve_names(con, ["CB"], {"CB": CONFLICT})
    assert matches["CB"].method == CONFLICTING_PINS and matches["CB"].gene is None
    assert ec.query(con, matches).not_measured == {"CB": ec.CONFLICTING_PINS}


def test_marker_gene_ids_reads_pre_244_markers():
    """Legacy read path: ``symbol`` was the source wording; an ID pins it,
    and a marker without one is left to resolve by name."""
    node = {"defining_markers": [{"symbol": "PV", "ncbi_gene_id": "NCBIGene:19293"},
                                 {"symbol": "X"}]}
    assert marker_gene_ids(node) == {"PV": Pin("NCBIGene:19293", None)}


@pytest.mark.parametrize(
    "marker, name, display",
    [
        ({"name_in_source": "NeuN", "symbol": "Rbfox3"}, "NeuN", "NeuN (Rbfox3)"),
        ({"name_in_source": "SST", "symbol": "Sst"}, "SST", "SST"),
        ({"name_in_source": "PSA-NCAM"}, "PSA-NCAM", "PSA-NCAM"),
        ({"symbol": "PV"}, "PV", "PV"),  # pre-#244: symbol was the wording
        ("Sst", "Sst", "Sst"),
    ],
)
def test_marker_name_and_display(marker, name, display):
    assert (marker_name(marker), marker_display(marker)) == (name, display)


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


def _graph(symbol: str | None, gid: str | None, species: str | None = "NCBITaxon:10090",
           name: str = "PV") -> dict:
    m: dict = {"name_in_source": name}
    if symbol:
        m["symbol"] = symbol
    if gid:
        m["ncbi_gene_id"] = gid
    node: dict = {"id": "n1", "defining_markers": [m]}
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
        "NCBIGene:12307": {"label": "Calb1", "taxon": None, "names": []},
    }))
    return p


def _nodenorm_returns(monkeypatch, answer: dict):
    calls: list = []

    def fake(ids, **kw):
        calls.append(list(ids))
        return {i: answer.get(i) for i in ids}

    monkeypatch.setattr(gi, "nodenorm", fake)
    monkeypatch.setattr(gi, "nameres_synonyms", lambda ids, **kw: {})
    return calls


def _check(doc, cache, tmp_path, taxslim=None):
    return check_marker_gene_ids(
        doc, cache_path=cache, taxonomy_root=tmp_path / "none",
        taxslim=taxslim or tmp_path / "no.obo",
    )


def test_hook_check_accepts_official_symbol(cache, tmp_path):
    assert _check(_graph("Pvalb", "NCBIGene:19293"), cache, tmp_path) == ([], [])


def test_hook_check_ignores_name_in_source(cache, tmp_path):
    """The source's wording is never checked — any name may pin any gene
    as long as symbol is that gene's official symbol (#244)."""
    doc = _graph("Pvalb", "NCBIGene:19293", name="anti-PV clone 235")
    assert _check(doc, cache, tmp_path) == ([], [])


def test_hook_check_rejects_nonexistent_id(cache, tmp_path, monkeypatch):
    _nodenorm_returns(monkeypatch, {})
    errors, _ = _check(_graph("Pvalb", "NCBIGene:999999999"), cache, tmp_path)
    assert len(errors) == 1 and "does not resolve" in errors[0]


def test_hook_check_does_not_cache_a_failed_lookup(cache, tmp_path, monkeypatch):
    """Review #6: a gene NodeNorm doesn't return (a passing gap) is looked
    up again next time, not stored as missing for good."""
    calls = _nodenorm_returns(monkeypatch, {})
    doc = _graph("Pvalb", "NCBIGene:999999999")
    assert _check(doc, cache, tmp_path)[0]
    assert _check(doc, cache, tmp_path)[0]
    assert calls == [["NCBIGene:999999999"], ["NCBIGene:999999999"]]
    assert "NCBIGene:999999999" not in json.loads(cache.read_text())


def test_hook_check_drops_old_negative_entries(cache, tmp_path, monkeypatch):
    """Review #6: a {"missing": true} left by an older version is looked up
    again (here the gene is found, so the edit passes)."""
    data = json.loads(cache.read_text())
    data["NCBIGene:14415"] = {"missing": True}
    cache.write_text(json.dumps(data))
    _nodenorm_returns(monkeypatch, {"NCBIGene:14415": {
        "ncbi_gene_id": "NCBIGene:14415", "label": "Gad1", "taxon": "NCBITaxon:10090",
        "equivalent_ids": [],
    }})
    assert _check(_graph("Gad1", "NCBIGene:14415", "NCBITaxon:10090"), cache, tmp_path)[0] == []


def test_hook_check_reports_a_replaced_id(cache, tmp_path, monkeypatch):
    """Review #6: NodeNorm answering with another NCBIGene ID (merged or
    replaced record) names the replacement."""
    _nodenorm_returns(monkeypatch, {"NCBIGene:1": {
        "ncbi_gene_id": "NCBIGene:2", "label": "Gad1", "taxon": "NCBITaxon:10090",
        "equivalent_ids": [],
    }})
    errors, _ = _check(_graph("Gad1", "NCBIGene:1"), cache, tmp_path)
    assert len(errors) == 1 and "NodeNormalization gives NCBIGene:2" in errors[0]


def test_hook_check_rejects_symbol_mismatch(cache, tmp_path):
    errors, _ = _check(_graph("Sst", "NCBIGene:19293"), cache, tmp_path)
    assert len(errors) == 1 and "symbol must be its official symbol 'Pvalb', not 'Sst'" in errors[0]


def test_hook_check_rejects_synonym_as_symbol(cache, tmp_path):
    """A known synonym is not the official symbol: it belongs in name_in_source."""
    errors, _ = _check(_graph("PV", "NCBIGene:19293"), cache, tmp_path)
    assert len(errors) == 1 and "official symbol 'Pvalb', not 'PV'" in errors[0]


@pytest.mark.parametrize("symbol, gid, lack", [("Pvalb", None, "no ncbi_gene_id"),
                                               (None, "NCBIGene:19293", "no symbol")])
def test_hook_check_requires_symbol_and_id_together(cache, tmp_path, symbol, gid, lack):
    errors, _ = _check(_graph(symbol, gid), cache, tmp_path)
    assert len(errors) == 1 and lack in errors[0]


def test_hook_check_accepts_marker_with_no_gene(cache, tmp_path):
    assert _check(_graph(None, None, name="PSA-NCAM"), cache, tmp_path) == ([], [])


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
        _graph("Pvalb", "NCBIGene:19293", "NCBITaxon:10116"), cache, tmp_path, taxslim
    )
    assert len(errors) == 1 and "but the node's species is NCBITaxon:10116" in errors[0]


def test_hook_check_species_comes_from_graph_when_node_has_none(cache, tmp_path, taxslim):
    doc = _graph("Pvalb", "NCBIGene:19293", species=None)
    doc["species"] = {"id": "NCBITaxon:10116"}
    errors, _ = _check(doc, cache, tmp_path, taxslim)
    assert len(errors) == 1 and "NCBITaxon:10116" in errors[0]


def test_hook_check_reports_species_unchecked_when_node_has_none(cache, tmp_path, taxslim):
    """Review #5: no node or graph species → the species check is listed
    as not run, never skipped silently."""
    errors, unchecked = _check(_graph("Pvalb", "NCBIGene:19293", species=None), cache,
                               tmp_path, taxslim)
    assert errors == []
    assert unchecked == [
        "NCBIGene:19293: species not compared — n1 has no species and the graph has none"
    ]


def test_hook_check_reports_species_unchecked_when_gene_has_no_taxon(cache, tmp_path, taxslim):
    errors, unchecked = _check(_graph("Calb1", "NCBIGene:12307", "NCBITaxon:10090"), cache,
                               tmp_path, taxslim)
    assert errors == []
    assert unchecked == ["NCBIGene:12307: species not compared — no taxon in NodeNormalization"]


def test_hook_check_leaves_edge_evidence_markers_unchecked(cache, tmp_path, taxslim):
    """Review #4 (deferred): a gene on an edge must be checked for
    consistency with the two nodes it links, not looked up on its own (the
    graph's species is wrong for atlas genes). Until that lands, edge
    markers are not checked."""
    doc = {"species": {"id": "NCBITaxon:10090"}, "nodes": [], "edges": [{
        "id": "e1", "evidence": [{"evidence_type": "ATLAS_METADATA", "defining_markers": [
            {"name_in_source": "Sst", "symbol": "Pvalb"},
            {"name_in_source": "Pvalb", "symbol": "Sst", "ncbi_gene_id": "NCBIGene:19293"},
            {"name_in_source": "PVALB", "symbol": "PVALB", "ncbi_gene_id": "NCBIGene:5816"},
        ]}],
    }]}
    assert _check(doc, cache, tmp_path, taxslim) == ([], [])


def test_hook_check_without_taxslim_reports_species_unchecked(cache, tmp_path, monkeypatch):
    monkeypatch.setattr(gi, "_TAXON_PARENTS", None)
    errors, unchecked = _check(_graph("Pvalb", "NCBIGene:19293", "NCBITaxon:10116"), cache, tmp_path)
    assert errors == []
    assert unchecked and "just fetch-oak-dbs" in unchecked[0]


def test_hook_check_accepts_gene_of_descendant_taxon(cache, tmp_path, taxslim):
    obo = taxslim
    assert _check(_graph("PVALB", "NCBIGene:5816", "NCBITaxon:9443"), cache, tmp_path, obo)[0] == []
    errors, _ = _check(_graph("PVALB", "NCBIGene:5816", "NCBITaxon:10090"), cache, tmp_path, obo)
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
    assert _check(_graph("Gad1", "NCBIGene:14415", name="GAD67"), cache, tmp_path) == ([], [])
    assert _check(_graph("Gad1", "NCBIGene:14415", name="GAD67"), cache, tmp_path) == ([], [])
    assert calls == [["NCBIGene:14415"]]  # second check served from the cache file
    assert json.loads(cache.read_text())["NCBIGene:14415"]["label"] == "Gad1"


def test_hook_check_seeds_from_committed_gene_ids(tmp_path, tax_dir, monkeypatch):
    def offline(*a, **kw):
        raise urllib.error.URLError("offline")

    monkeypatch.setattr(gi, "nodenorm", offline)
    errors, unchecked = check_marker_gene_ids(
        _graph("Calb1", "NCBIGene:12307", name="calbindin"), cache_path=tmp_path / "c.json",
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


@pytest.mark.parametrize("name, method", [("Kiss1", EXACT_SYMBOL),
                                          ("KISS1", CASE_INSENSITIVE_SYMBOL)])
def test_duplicate_symbol_prefers_the_gene_with_an_ncbi_id(tmp_path, name, method):
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
    m = resolve_names(c, [name])[name]
    # Review #2: the case-insensitive branch collapses duplicate Ensembl
    # models of one locus too, instead of calling them AMBIGUOUS.
    assert (m.method, m.gene.ensembl_id) == (method, "ENSMUSG09")
