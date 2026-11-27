"""Gene identity: one ID layer between classical markers and atlas expression (#216).

Classical markers come from papers as protein names, abbreviations and
symbols (``PV``, ``CB``, ``mGluR1``, ``Sst``); atlas expression is keyed by
the Ensembl IDs in the MapMyCells stats file. This module joins the two on
gene identifiers instead of free-text symbols.

Three parts:

- **Fetch** (network, rare) — :func:`fetch_gene_ids`, ``just build-gene-ids
  {tid}``. Reads the stats file's Ensembl IDs, normalises them through
  Translator NodeNormalization (Ensembl → NCBIGene + label + taxon) and
  pulls each gene's names from Translator Name Resolver ``/synonyms``.
  Writes ``kb/taxonomy/{tid}/gene_ids.tsv.gz`` (committed) with a header
  recording the Translator versions, fetch date and the stats file's sha256.
  Re-fetching is a deliberate refresh that shows up as a reviewed diff.
- **Load** (offline, every ``build-taxonomy-db``) — :func:`load_gene_tables`
  fills the ``genes`` and ``gene_synonyms`` tables from that file.
- **Resolve** — :func:`resolve_names` turns marker names into genes of the
  taxonomy, in this order:

  1. ``PINNED_ID``: the marker's ``ncbi_gene_id`` is a gene of this taxonomy.
     A pin that isn't (a gene of another species) resolves by the marker's
     official ``symbol`` instead — that symbol only, compared ignoring case,
     never synonyms — as ``PINNED_SYMBOL`` (rat Calb1 → the mouse gene named
     Calb1). A pin with no symbol, or whose symbol isn't exactly one gene
     here, is ``PIN_NOT_IN_TAXONOMY``: a pin never falls back to the marker's
     name. A curated marker with no ``ncbi_gene_id`` is ``NO_GENE_ID`` and is
     not resolved by name (#244). Markers of one node that share a name but
     carry different pins are ``CONFLICTING_PINS``: a pin is one marker's
     gene and is never applied to another marker that happens to share its
     wording.
  2. ``EXACT_SYMBOL``: the name is a gene's symbol (stats symbol or current
     label), case-sensitive; then ``CASE_INSENSITIVE_SYMBOL``, compared
     after :func:`normalise_name` (a symbol beats other genes' synonyms).
  3. ``UNIQUE_SYNONYM``: exactly one gene lists the name as a synonym.

  Two or more claimants is ``AMBIGUOUS`` and none is ``NO_MATCH``: neither
  is guessed. A curator (or curating agent) settles the name per marker
  and records the choice as the marker's ``symbol`` + ``ncbi_gene_id``;
  there is no taxonomy-wide name → gene table. Claimant counting runs over
  the taxonomy's gene universe, which is right for whole-transcriptome stats
  files (WMB, HMBA) but would give false "unique" results for a targeted
  panel.

The hook check (:func:`check_marker_gene_ids`) validates every
``ncbi_gene_id`` written to ``kb/graphs`` against NodeNormalization: the ID
exists, belongs to the node's species, and the marker's ``symbol`` is the
gene's official symbol (#244). ``symbol`` and ``ncbi_gene_id`` are set
together or not at all; ``name_in_source`` (the source's wording) is never
checked. Lookups are cached in ``conf/gene_id_cache.json``
(gitignored) and seeded from the committed ``gene_ids.tsv.gz`` files, so the
check runs offline for genes already seen; it soft-skips, loudly, when an
uncached ID can't be looked up.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping

from evidencell.expression_cache import ExpressionUnavailable

# Overridable for tests (e.g. an unreachable URL to exercise the soft skip).
NODENORM_URL = os.environ.get(
    "EVIDENCELL_NODENORM_URL", "https://nodenormalization-sri.renci.org"
)
NAMERES_URL = os.environ.get("EVIDENCELL_NAMERES_URL", "https://name-resolution-sri.renci.org")

GENE_IDS_FILE = "gene_ids.tsv.gz"

GENE_IDS_COLUMNS = (
    "ensembl_id", "stats_symbol", "stats_col", "ncbi_gene_id", "label",
    "taxon", "equivalent_ids", "synonyms",
)

# Resolution methods (accepted) and failure reasons.
PINNED_ID = "PINNED_ID"
PINNED_SYMBOL = "PINNED_SYMBOL"  # pin from another species, reached by its official symbol
EXACT_SYMBOL = "EXACT_SYMBOL"
CASE_INSENSITIVE_SYMBOL = "CASE_INSENSITIVE_SYMBOL"
UNIQUE_SYNONYM = "UNIQUE_SYNONYM"
AMBIGUOUS = "AMBIGUOUS"
NO_MATCH = "NO_MATCH"
NO_GENE_ID = "NO_GENE_ID"  # curated marker with no ncbi_gene_id: not resolved by name
PIN_NOT_IN_TAXONOMY = "PIN_NOT_IN_TAXONOMY"  # pinned gene (or its symbol) isn't here
CONFLICTING_PINS = "CONFLICTING_PINS"  # one name, different pins on one node
ACCEPTED_METHODS = (
    PINNED_ID, PINNED_SYMBOL, EXACT_SYMBOL, CASE_INSENSITIVE_SYMBOL, UNIQUE_SYNONYM,
)

GENE_DDL = """\
CREATE TABLE IF NOT EXISTS genes (
  ensembl_id     TEXT PRIMARY KEY,
  stats_symbol   TEXT NOT NULL,
  stats_col      INTEGER NOT NULL,
  ncbi_gene_id   TEXT,
  label          TEXT,
  taxon          TEXT,
  symbol_norm    TEXT NOT NULL,
  label_norm     TEXT
);

CREATE TABLE IF NOT EXISTS gene_synonyms (
  ncbi_gene_id   TEXT NOT NULL,
  synonym        TEXT NOT NULL,
  synonym_norm   TEXT NOT NULL,
  source         TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_genes_ncbi        ON genes(ncbi_gene_id);
CREATE INDEX IF NOT EXISTS idx_genes_symbol      ON genes(stats_symbol);
CREATE INDEX IF NOT EXISTS idx_genes_symbol_norm ON genes(symbol_norm);
CREATE INDEX IF NOT EXISTS idx_genes_label_norm  ON genes(label_norm);
CREATE INDEX IF NOT EXISTS idx_gene_syn_norm     ON gene_synonyms(synonym_norm);
"""

_GENE_META_KEY = "gene_ids_meta"

_NORM_STRIP = re.compile(r"[\s\-_]+")


def normalise_name(name: str) -> str:
    """Comparison form of a gene name: lowercased, spaces/hyphens/underscores
    removed (``5-HT3a`` → ``5ht3a``)."""
    return _NORM_STRIP.sub("", name).lower()


class GeneIdsUnavailable(ExpressionUnavailable):
    """The taxonomy has no gene identity table (``gene_ids.tsv.gz``)."""


# ── Translator clients ───────────────────────────────────────────────────────


def _http_json(
    url: str, payload: Any | None = None, *, timeout: float = 60, retries: int = 3
) -> Any:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json", "Accept": "application/json"}
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


_TAXON_SUFFIX = re.compile(r" \([A-Z][a-z]{3}\)$")


def _ncbi_from_nodenorm(entry: dict | None) -> dict | None:
    """Pick the NCBIGene record out of one NodeNorm result, or None."""
    if not entry:
        return None
    equivalents = entry.get("equivalent_identifiers") or []
    ncbi = next(
        (e for e in equivalents if str(e.get("identifier", "")).startswith("NCBIGene:")), None
    )
    taxa = entry.get("taxa") or (ncbi or {}).get("taxa") or []
    # Without an NCBIGene record the label is Ensembl's, e.g. "Gm2164 (Mmus)".
    label = (ncbi or {}).get("label") or (entry.get("id") or {}).get("label")
    return {
        "ncbi_gene_id": ncbi["identifier"] if ncbi else None,
        "label": _TAXON_SUFFIX.sub("", label) if label else None,
        "taxon": taxa[0] if taxa else None,
        "equivalent_ids": [
            e["identifier"] for e in equivalents
            if str(e.get("identifier", "")).split(":")[0] in ("MGI", "HGNC", "RGD")
        ],
    }


def nodenorm(
    curies: list[str], *, batch: int = 1000, timeout: float = 60, retries: int = 3
) -> dict[str, dict | None]:
    """Normalise CURIEs with NodeNormalization (``conflate: false``).

    Returns ``{curie: {ncbi_gene_id, label, taxon, equivalent_ids} | None}``.
    """
    out: dict[str, dict | None] = {}
    for i in range(0, len(curies), batch):
        chunk = curies[i:i + batch]
        res = _http_json(
            f"{NODENORM_URL}/get_normalized_nodes", {"curies": chunk, "conflate": False},
            timeout=timeout, retries=retries,
        )
        for c in chunk:
            out[c] = _ncbi_from_nodenorm(res.get(c))
    return out


def nameres_synonyms(
    ncbi_ids: list[str], *, batch: int = 250, timeout: float = 120, retries: int = 3
) -> dict[str, list[str]]:
    """Every name Name Resolver holds for each NCBIGene ID (``/synonyms``)."""
    out: dict[str, list[str]] = {}
    for i in range(0, len(ncbi_ids), batch):
        chunk = ncbi_ids[i:i + batch]
        res = _http_json(
            f"{NAMERES_URL}/synonyms", {"preferred_curies": chunk},
            timeout=timeout, retries=retries,
        )
        for c in chunk:
            rec = res.get(c) or {}
            out[c] = list(dict.fromkeys(rec.get("names") or []))
    return out


def nameres_lookup(name: str, taxon: str, *, limit: int = 10) -> list[dict]:
    """Name Resolver candidates for ``name`` among NCBIGene genes of ``taxon``.

    Always restricted to ``only_prefixes=NCBIGene``: with ``only_taxa`` alone,
    records without taxon metadata (MGI, FlyBase, ZFIN) slip through.
    """
    from urllib.parse import urlencode

    q = urlencode({
        "string": name, "biolink_type": "Gene", "only_taxa": taxon,
        "only_prefixes": "NCBIGene", "limit": limit, "autocomplete": "false",
    })
    res = _http_json(f"{NAMERES_URL}/lookup?{q}")
    return [
        {"ncbi_gene_id": r["curie"], "label": r.get("label"), "taxa": r.get("taxa") or []}
        for r in res or []
    ]


def translator_versions() -> dict[str, str | None]:
    """Babel / service versions for provenance headers."""
    out: dict[str, str | None] = {}
    for key, url in (("nodenorm", NODENORM_URL), ("nameres", NAMERES_URL)):
        try:
            st = _http_json(f"{url}/status", timeout=20, retries=2)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            st = {}
        out[f"{key}_babel_version"] = st.get("babel_version")
        out[f"{key}_version"] = st.get("version") if key == "nodenorm" else st.get("nameres_version")
    return out


# ── gene_ids.tsv.gz I/O ──────────────────────────────────────────────────────


def gene_ids_path(taxonomy_id: str) -> Path:
    from evidencell.paths import taxonomy_dir

    return taxonomy_dir(taxonomy_id) / GENE_IDS_FILE


def read_gene_ids(path: Path) -> tuple[dict[str, str], list[dict]]:
    """Read a ``gene_ids.tsv.gz``: ``(meta, rows)``.

    Meta lines precede the header as ``#key<TAB>value``. Row fields
    ``equivalent_ids`` / ``synonyms`` are ``|``-joined lists; ``stats_col``
    is an int; empty strings are None.
    """
    meta: dict[str, str] = {}
    rows: list[dict] = []
    with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
        lines = (ln for ln in fh)
        body: list[str] = []
        for ln in lines:
            if ln.startswith("#"):
                k, _, v = ln[1:].rstrip("\n").partition("\t")
                meta[k] = v
            else:
                body.append(ln)
                break
        body.extend(lines)
    for rec in csv.DictReader(io.StringIO("".join(body)), delimiter="\t"):
        row: dict[str, Any] = {k: (v or None) for k, v in rec.items()}
        row["stats_col"] = int(rec["stats_col"])
        row["equivalent_ids"] = rec["equivalent_ids"].split("|") if rec["equivalent_ids"] else []
        row["synonyms"] = rec["synonyms"].split("|") if rec["synonyms"] else []
        rows.append(row)
    return meta, rows


def write_gene_ids(path: Path, meta: Mapping[str, Any], rows: Iterable[Mapping]) -> None:
    """Write a ``gene_ids.tsv.gz`` deterministically (no mtime or filename in
    the gzip header), so a refresh that changes nothing produces no diff."""
    buf = io.StringIO()
    for k, v in meta.items():
        buf.write(f"#{k}\t{'' if v is None else v}\n")
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(GENE_IDS_COLUMNS)
    for r in rows:
        w.writerow([
            r["ensembl_id"], r["stats_symbol"], r["stats_col"], r.get("ncbi_gene_id") or "",
            r.get("label") or "", r.get("taxon") or "",
            "|".join(r.get("equivalent_ids") or []),
            "|".join(s.replace("|", "/") for s in r.get("synonyms") or []),
        ])
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw, gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as gz:
        gz.write(buf.getvalue().encode("utf-8"))


def choose_stats_symbol(prior: str | None, label: str | None, synonyms: list[str]) -> str | None:
    """The symbol a stats column goes by in atlas marker lists.

    A release-era symbol is kept when it is the current label or one of the
    gene's recorded names (a rename: ``Car8`` for Ca8, as WMB's lists use).
    Otherwise the current label wins: the legacy mygene mapping held errors
    (``Np65`` for Ncam1, ``M2R`` for Chrm2) that a kept symbol would carry
    into exact-symbol matches.
    """
    if not label:
        return prior
    if prior and (prior == label or normalise_name(prior) in {normalise_name(s) for s in synonyms}):
        return prior
    return label


def _prior_stats_symbols(taxonomy_id: str, out_path: Path) -> dict[str, str]:
    """Release-era symbols to keep stable across refreshes: from the existing
    ``gene_ids.tsv.gz`` if there is one, else from the legacy
    ``conf/gene_mapping_{tid}.tsv`` (the symbols the expression cache and
    atlas marker lists used before #216)."""
    from evidencell.paths import repo_root

    if out_path.is_file():
        _, rows = read_gene_ids(out_path)
        return {r["ensembl_id"]: r["stats_symbol"] for r in rows}
    legacy = repo_root() / "conf" / f"gene_mapping_{taxonomy_id}.tsv"
    out: dict[str, str] = {}
    if legacy.is_file():
        with legacy.open(encoding="utf-8") as fh:
            for rec in csv.DictReader(fh, delimiter="\t"):
                out[rec["ensembl_id"]] = rec["symbol"]
    return out


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def fetch_gene_ids(
    taxonomy_id: str,
    *,
    stats_path: Path | None = None,
    out_path: Path | None = None,
) -> Path:
    """Build ``kb/taxonomy/{tid}/gene_ids.tsv.gz`` from the stats file's
    Ensembl IDs via NodeNormalization + Name Resolver (network)."""
    import h5py

    from evidencell.expression_cache import stats_h5_path

    stats_path = stats_path or stats_h5_path(taxonomy_id)
    out_path = out_path or gene_ids_path(taxonomy_id)
    if not stats_path.is_file():
        raise FileNotFoundError(
            f"Stats file missing: {stats_path}. Run: just fetch-mapmycells {taxonomy_id}"
        )
    with h5py.File(str(stats_path), "r") as f:
        col_names: list[str] = json.loads(f["col_names"][()])
    # Versioned IDs (ENSMUSG….5) don't resolve in NodeNorm; the unversioned do.
    ensembl = [c.split(".", 1)[0] for c in col_names]
    print(f"  {len(ensembl):,} genes in {stats_path.name}", file=sys.stderr)

    prior = _prior_stats_symbols(taxonomy_id, out_path)
    t0 = time.time()
    norm = nodenorm([f"ENSEMBL:{e}" for e in ensembl])
    print(f"  NodeNorm: {time.time() - t0:.0f}s", file=sys.stderr)

    ncbi_ids = sorted({
        n["ncbi_gene_id"] for n in norm.values() if n and n.get("ncbi_gene_id")
    })
    t0 = time.time()
    syns = nameres_synonyms(ncbi_ids)
    print(f"  Name Resolver synonyms for {len(ncbi_ids):,} genes: {time.time() - t0:.0f}s",
          file=sys.stderr)

    rows = []
    for col, ens in enumerate(ensembl):
        n = norm.get(f"ENSEMBL:{ens}") or {}
        ncbi = n.get("ncbi_gene_id")
        label = n.get("label")
        synonyms = syns.get(ncbi, []) if ncbi else []
        rows.append({
            "ensembl_id": ens,
            "stats_symbol": choose_stats_symbol(prior.get(ens), label, synonyms) or ens,
            "stats_col": col,
            "ncbi_gene_id": ncbi,
            "label": label,
            "taxon": n.get("taxon"),
            "equivalent_ids": n.get("equivalent_ids") or [],
            "synonyms": synonyms,
        })
    n_ncbi = sum(1 for r in rows if r["ncbi_gene_id"])
    meta = {
        "taxonomy_id": taxonomy_id,
        "stats_file": stats_path.name,
        "stats_sha256": _sha256_file(stats_path),
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        **translator_versions(),
        "n_genes": len(rows),
        "n_ncbi": n_ncbi,
    }
    write_gene_ids(out_path, meta, rows)
    print(
        f"  Wrote {out_path}: {len(rows):,} genes, {n_ncbi:,} with NCBIGene "
        f"({100 * n_ncbi / max(1, len(rows)):.1f}%); the rest keep Ensembl as key",
        file=sys.stderr,
    )
    return out_path


# ── DB load ──────────────────────────────────────────────────────────────────


def load_gene_tables(con: sqlite3.Connection, taxonomy_dir: Path) -> int:
    """(Re)create and fill ``genes`` / ``gene_synonyms`` from the taxonomy's
    committed ``gene_ids.tsv.gz``. Returns the
    number of genes loaded (0 when the taxonomy has no gene_ids file)."""
    con.executescript("DROP TABLE IF EXISTS gene_synonyms; DROP TABLE IF EXISTS genes;")
    con.executescript(GENE_DDL)
    con.execute("CREATE TABLE IF NOT EXISTS _meta (key TEXT PRIMARY KEY, value TEXT)")
    con.execute("DELETE FROM _meta WHERE key = ?", (_GENE_META_KEY,))
    path = taxonomy_dir / GENE_IDS_FILE
    if not path.is_file():
        return 0
    meta, rows = read_gene_ids(path)
    con.executemany(
        "INSERT INTO genes VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                r["ensembl_id"], r["stats_symbol"], r["stats_col"], r["ncbi_gene_id"],
                r["label"], r["taxon"], normalise_name(r["stats_symbol"]),
                normalise_name(r["label"]) if r["label"] else None,
            )
            for r in rows
        ],
    )
    syn_rows = []
    for r in rows:
        if not r["ncbi_gene_id"]:
            continue
        for s in dict.fromkeys(r["synonyms"]):
            syn_rows.append((r["ncbi_gene_id"], s, normalise_name(s), "translator_nameres"))
    con.executemany("INSERT INTO gene_synonyms VALUES (?, ?, ?, ?)", syn_rows)
    con.execute(
        "INSERT OR REPLACE INTO _meta VALUES (?, ?)", (_GENE_META_KEY, json.dumps(meta))
    )
    return len(rows)


def gene_ids_meta(con: sqlite3.Connection) -> dict[str, str] | None:
    """Provenance header of the loaded ``gene_ids.tsv.gz``, or None."""
    try:
        row = con.execute("SELECT value FROM _meta WHERE key = ?", (_GENE_META_KEY,)).fetchone()
    except sqlite3.OperationalError:
        return None
    return json.loads(row[0]) if row else None


# ── Resolution ───────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Gene:
    ensembl_id: str
    stats_symbol: str
    stats_col: int
    ncbi_gene_id: str | None
    label: str | None


@dataclass
class GeneMatch:
    """How one marker name resolved against a taxonomy's genes.

    ``gene`` is set when ``method`` is one of :data:`ACCEPTED_METHODS`.
    ``claimants`` lists the competing genes for ``AMBIGUOUS``, and for
    ``CASE_INSENSITIVE_SYMBOL`` any other gene that lists the name as a
    synonym (accepted anyway: a symbol beats a synonym).
    """

    name: str
    method: str
    gene: Gene | None = None
    claimants: list[Gene] = field(default_factory=list)

    @property
    def resolved(self) -> bool:
        return self.gene is not None

    def to_dict(self) -> dict:
        def g(x: Gene) -> dict:
            return {
                "ncbi_gene_id": x.ncbi_gene_id, "symbol": x.stats_symbol,
                "label": x.label, "ensembl_id": x.ensembl_id,
            }

        return {
            "name": self.name, "method": self.method,
            "gene": g(self.gene) if self.gene else None,
            "claimants": [g(c) for c in self.claimants],
        }


_GENE_COLS = "ensembl_id, stats_symbol, stats_col, ncbi_gene_id, label"


def _genes(con: sqlite3.Connection, where: str, params: tuple) -> list[Gene]:
    return [
        Gene(*r)
        for r in con.execute(
            f"SELECT {_GENE_COLS} FROM genes WHERE {where} ORDER BY stats_col", params
        )
    ]


def _one_per_ncbi(genes: list[Gene]) -> list[Gene]:
    """Collapse genes sharing an NCBIGene ID (several Ensembl IDs → one gene)
    to the first stats column, so they count as one claimant."""
    seen: dict[str, Gene] = {}
    out: list[Gene] = []
    for g in genes:
        key = g.ncbi_gene_id or g.ensembl_id
        if key not in seen:
            seen[key] = g
            out.append(g)
    return out


def _prefer_ncbi(genes: list[Gene]) -> list[Gene]:
    """Of several genes sharing a symbol, keep the one with an NCBIGene ID
    when exactly one has it: the others are extra Ensembl models of the same
    locus (WMB has two ``Kiss1`` columns, one without an NCBIGene record)."""
    with_id = [g for g in genes if g.ncbi_gene_id]
    return with_id if len(genes) > 1 and len(with_id) == 1 else genes


def has_gene_tables(con: sqlite3.Connection) -> bool:
    try:
        return con.execute("SELECT COUNT(*) FROM genes").fetchone()[0] > 0
    except sqlite3.OperationalError:
        return False


@dataclass(frozen=True)
class Pin:
    """A curated marker's gene: ``ncbi_gene_id`` and its official ``symbol``.
    Both None means the marker is curated as having no single gene."""

    ncbi_gene_id: str | None
    symbol: str | None = None
    conflict: bool = False


NO_GENE = Pin(None, None)
CONFLICT = Pin(None, None, conflict=True)


def resolve_name(
    con: sqlite3.Connection, name: str, ncbi_gene_id: str | None = None,
    symbol: str | None = None,
) -> GeneMatch:
    """Resolve one marker name, optionally pinned to an NCBIGene ID (with
    the gene's official ``symbol``)."""
    if ncbi_gene_id:
        hits = _one_per_ncbi(_genes(con, "ncbi_gene_id = ?", (ncbi_gene_id,)))
        if hits:
            return GeneMatch(name, PINNED_ID, hits[0])
        # An ID from another species: its official symbol, ignoring case
        # (human PVALB → mouse Pvalb), is how a rat or human marker reaches
        # a mouse taxonomy's genes. Never synonyms, and never the marker's
        # own name: a pin is not re-guessed from wording.
        if not symbol:
            return GeneMatch(name, PIN_NOT_IN_TAXONOMY)
        norm = normalise_name(symbol)
        by_symbol = _prefer_ncbi(_one_per_ncbi(
            _genes(con, "symbol_norm = ? OR label_norm = ?", (norm, norm))
        ))
        if len(by_symbol) == 1:
            return GeneMatch(name, PINNED_SYMBOL, by_symbol[0])
        return GeneMatch(name, PIN_NOT_IN_TAXONOMY, claimants=by_symbol)
    norm = normalise_name(name)

    exact = _prefer_ncbi(_one_per_ncbi(_genes(con, "stats_symbol = ? OR label = ?", (name, name))))
    if len(exact) == 1:
        return GeneMatch(name, EXACT_SYMBOL, exact[0])
    if len(exact) > 1:
        return GeneMatch(name, AMBIGUOUS, claimants=exact)

    # A gene symbol in another case ("SST", a human-style symbol on a mouse
    # taxonomy) means that gene, even when some other gene lists the string
    # as a synonym (Lmx1a lists "sst", an allele name). Competing synonym
    # claimants are kept on the match for review.
    syn_claimants = _one_per_ncbi(_genes(
        con,
        "ncbi_gene_id IN (SELECT ncbi_gene_id FROM gene_synonyms WHERE synonym_norm = ?)",
        (norm,),
    ))
    by_symbol = _prefer_ncbi(_one_per_ncbi(
        _genes(con, "symbol_norm = ? OR label_norm = ?", (norm, norm))
    ))
    if len(by_symbol) == 1:
        others = [g for g in syn_claimants if g.ensembl_id != by_symbol[0].ensembl_id]
        return GeneMatch(name, CASE_INSENSITIVE_SYMBOL, by_symbol[0], claimants=others)
    if len(by_symbol) > 1:
        return GeneMatch(name, AMBIGUOUS, claimants=by_symbol)
    if len(syn_claimants) == 1:
        return GeneMatch(name, UNIQUE_SYNONYM, syn_claimants[0])
    if syn_claimants:
        return GeneMatch(name, AMBIGUOUS, claimants=syn_claimants)
    return GeneMatch(name, NO_MATCH)


def resolve_names(
    con: sqlite3.Connection,
    names: Iterable[str],
    gene_ids: Mapping[str, str | Pin] | None = None,
    *,
    taxonomy_id: str | None = None,
) -> dict[str, GeneMatch]:
    """Resolve marker names; ``gene_ids`` pins a name to its curated
    ``ncbi_gene_id``. Raises :class:`GeneIdsUnavailable` when the DB has no
    gene tables (``taxonomy_id`` names the taxonomy in that message)."""
    if not has_gene_tables(con):
        tid = taxonomy_id or "{taxonomy_id}"
        raise GeneIdsUnavailable(
            "The taxonomy DB has no gene identity tables. Commit "
            f"kb/taxonomy/{tid}/{GENE_IDS_FILE} (just build-gene-ids {tid}) and rebuild "
            f"with just build-taxonomy-db {tid}."
        )
    out: dict[str, GeneMatch] = {}
    for n in dict.fromkeys(names):
        if not n:
            continue
        pin = (gene_ids or {}).get(n)
        if isinstance(pin, str):
            pin = Pin(pin)
        if pin is None:
            out[n] = resolve_name(con, n)
        elif pin.conflict:
            out[n] = GeneMatch(n, CONFLICTING_PINS)
        elif pin.ncbi_gene_id is None:
            out[n] = GeneMatch(n, NO_GENE_ID)
        else:
            out[n] = resolve_name(con, n, pin.ncbi_gene_id, pin.symbol)
    return out


# ── Classical-node helpers ───────────────────────────────────────────────────

MARKER_FIELDS = ("defining_markers", "negative_markers", "neuropeptides")


def marker_name(m: Any) -> str:
    """A marker's name as its source writes it — the key consumers query and
    report by. Reads pre-#244 YAML, where ``symbol`` held the source wording."""
    if isinstance(m, str):
        return m
    if not isinstance(m, dict):
        return ""
    return m.get("name_in_source") or m.get("symbol") or ""


def marker_display(m: Any) -> str:
    """``NeuN (Rbfox3)`` when the source wording differs from the official
    symbol, else the name alone."""
    name = marker_name(m)
    sym = m.get("symbol") if isinstance(m, dict) and "name_in_source" in m else None
    if sym and normalise_name(sym) != normalise_name(name):
        return f"{name} ({sym})"
    return name


def marker_gene_ids(node: dict) -> dict[str, Pin]:
    """``{name: Pin}`` for a classical node's markers — the pins passed to
    :func:`resolve_names`, keyed by :func:`marker_name`.

    A marker with ``ncbi_gene_id`` pins its gene (with its official symbol
    for cross-species fall-back). A ``name_in_source`` marker without one
    is curated as having no single gene (:data:`NO_GENE`) and is not
    resolved by name. Pre-#244 markers (``symbol`` only) without an ID are
    left out, so they resolve by name as before.

    Two markers sharing a name but not a pin (``CB`` as Calb1 among the
    defining markers and as Cnr1 among the negative ones) get
    :data:`CONFLICT`: neither is measured, rather than one marker's gene
    being applied to the other."""
    out: dict[str, Pin] = {}
    for key in MARKER_FIELDS:
        for m in node.get(key) or []:
            if not isinstance(m, dict) or not (name := marker_name(m)):
                continue
            if m.get("ncbi_gene_id"):
                sym = m.get("symbol") if "name_in_source" in m else None
                pin = Pin(m["ncbi_gene_id"], sym)
            elif "name_in_source" in m:
                pin = NO_GENE
            else:
                continue
            if out.get(name, pin) != pin:
                pin = CONFLICT
            out[name] = pin
    return out


# ── Curation-time resolution (agent-facing CLI) ──────────────────────────────


def resolve_for_curation(
    names: list[str], *, taxonomy_id: str | None = None, taxon: str | None = None
) -> list[dict]:
    """Candidate genes for marker names, for a curator to choose from.

    With ``taxonomy_id`` the local gene tables are used (offline). Otherwise
    Name Resolver is queried for ``taxon`` and candidates are kept only if
    the name is one of their exact names (normalised) — the same claimant
    count, over the species' full gene set.
    """
    if taxonomy_id:
        from evidencell.paths import taxonomy_db_path

        con = sqlite3.connect(taxonomy_db_path(taxonomy_id))
        try:
            return [m.to_dict() for m in resolve_names(con, names).values()]
        finally:
            con.close()
    if not taxon:
        raise ValueError("pass a taxonomy id or an NCBITaxon CURIE")
    out = []
    for name in names:
        cands = nameres_lookup(name, taxon)
        syns = nameres_synonyms([c["ncbi_gene_id"] for c in cands]) if cands else {}
        norm = normalise_name(name)
        claim = [
            c for c in cands
            if norm in {normalise_name(s) for s in syns.get(c["ncbi_gene_id"], [])}
            or normalise_name(c.get("label") or "") == norm
        ]
        exact = [c for c in claim if c.get("label") == name]
        if len(exact) == 1:
            method, gene = EXACT_SYMBOL, exact[0]
        elif len(claim) == 1:
            same = normalise_name(claim[0].get("label") or "") == norm
            method, gene = (CASE_INSENSITIVE_SYMBOL if same else UNIQUE_SYNONYM), claim[0]
        else:
            method, gene = (AMBIGUOUS if claim else NO_MATCH), None
        out.append({
            "name": name, "method": method, "taxon": taxon,
            "gene": {"ncbi_gene_id": gene["ncbi_gene_id"], "label": gene["label"]} if gene else None,
            "claimants": [
                {"ncbi_gene_id": c["ncbi_gene_id"], "label": c["label"]} for c in claim
            ] if method == AMBIGUOUS else [],
            "nameres_candidates": [
                {"ncbi_gene_id": c["ncbi_gene_id"], "label": c["label"]} for c in cands
            ] if method in (AMBIGUOUS, NO_MATCH) else [],
        })
    return out


# ── Hook check: ncbi_gene_id on KB markers ───────────────────────────────────


def gene_id_cache_path() -> Path:
    """``conf/gene_id_cache.json``, or ``$EVIDENCELL_GENE_ID_CACHE``."""
    from evidencell.paths import repo_root

    override = os.environ.get("EVIDENCELL_GENE_ID_CACHE")
    return Path(override) if override else repo_root() / "conf" / "gene_id_cache.json"


class _GeneRecordCache:
    """NCBIGene ID → ``{label, taxon, names}``.

    Backed by ``conf/gene_id_cache.json`` and seeded from every committed
    ``kb/taxonomy/*/gene_ids.tsv.gz``; misses go to NodeNorm + Name Resolver.
    Only genes that were found are stored. An ID NodeNorm doesn't return as
    itself comes back as ``{"missing": True}`` (with ``replaced_by`` when
    NodeNorm gave another NCBIGene ID — a merged or replaced record) but is
    looked up again next time, so a passing Translator gap never becomes a
    lasting block. Negative entries left by older versions are dropped on
    load.
    """

    def __init__(self, path: Path, taxonomy_root: Path | None) -> None:
        self.path = path
        self.taxonomy_root = taxonomy_root
        self.data: dict[str, dict] = {}
        if path.is_file():
            try:
                self.data = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                self.data = {}
        self._dirty = False
        stale = [k for k, v in self.data.items() if not isinstance(v, dict) or v.get("missing")]
        for k in stale:
            del self.data[k]
        self._dirty = bool(stale)

    def _seed(self, wanted: set[str]) -> None:
        if not self.taxonomy_root or not wanted:
            return
        for f in sorted(self.taxonomy_root.glob(f"*/{GENE_IDS_FILE}")):
            _, rows = read_gene_ids(f)
            for r in rows:
                nid = r["ncbi_gene_id"]
                if nid in wanted and nid not in self.data:
                    self.data[nid] = {
                        "label": r["label"], "taxon": r["taxon"],
                        "names": r["synonyms"],
                    }
                    self._dirty = True
            wanted = wanted - self.data.keys()
            if not wanted:
                return

    def get(self, ids: set[str]) -> tuple[dict[str, dict], list[str]]:
        """Records for ``ids`` and the IDs that couldn't be looked up."""
        self._seed(ids - self.data.keys())
        missing = sorted(ids - self.data.keys())
        unreachable: list[str] = []
        not_found: dict[str, dict] = {}
        if missing:
            try:
                # Short timeouts: this runs inside the pre-edit hook.
                norm = nodenorm(missing, timeout=20, retries=1)
                found = [
                    i for i in missing if (n := norm.get(i)) and n.get("ncbi_gene_id") == i
                ]
                names = nameres_synonyms(found, timeout=30, retries=1) if found else {}
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
                unreachable = missing
            else:
                for i in missing:
                    n = norm.get(i)
                    if n and n.get("ncbi_gene_id") == i:
                        self.data[i] = {
                            "label": n["label"], "taxon": n["taxon"], "names": names.get(i, []),
                        }
                        self._dirty = True
                    else:
                        replaced_by = (n or {}).get("ncbi_gene_id")
                        not_found[i] = {"missing": True, "replaced_by": replaced_by}
        records = {i: self.data[i] for i in ids if i in self.data}
        return {**records, **not_found}, unreachable

    def save(self) -> None:
        if not self._dirty:
            return
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text(json.dumps(self.data, sort_keys=True), encoding="utf-8")
        except OSError:
            pass


def lookup_gene_records(
    ids: set[str], *, cache_path: Path | None = None, taxonomy_root: Path | None = None
) -> tuple[dict[str, dict], list[str]]:
    """NCBIGene IDs → records, as the hook check sees them: ``({id: {label,
    taxon, names} | {missing: True, replaced_by}}, unreachable IDs)``.

    ``label`` is the gene's official symbol. Same cache and Translator
    lookups as :func:`check_marker_gene_ids`, so an ID written with this
    symbol passes the pre-edit hook."""
    from evidencell.paths import repo_root

    cache = _GeneRecordCache(
        cache_path or gene_id_cache_path(),
        taxonomy_root if taxonomy_root is not None else repo_root() / "kb" / "taxonomy",
    )
    out = cache.get(ids)
    cache.save()
    return out


GENE_DESCRIPTOR_FIELDS = (*MARKER_FIELDS, "merfish_markers", "markers")


def iter_gene_descriptors(
    doc: dict, *, edges: bool = True
) -> Iterator[tuple[str, dict, str | None]]:
    """(holder id, marker, species) for every GeneDescriptor in a KB graph:
    the marker lists of ``nodes[*]`` (including ``marker_sets[*].genes``)
    and, with ``edges``, of ``edges[*].evidence[*]`` (atlas metadata
    evidence). Species is the node's, else the graph's; edge evidence takes
    the graph's."""
    def sid(x: Any) -> str | None:
        return x.get("id") if isinstance(x, dict) else x

    graph_species = sid(doc.get("species"))
    holders: list[tuple[str, dict, str | None]] = []
    for node in doc.get("nodes") or []:
        if isinstance(node, dict):
            holders.append(
                (node.get("id", "?"), node, sid(node.get("species")) or graph_species)
            )
    for edge in (doc.get("edges") or []) if edges else []:
        if not isinstance(edge, dict):
            continue
        for i, ev in enumerate(edge.get("evidence") or []):
            if isinstance(ev, dict):
                holders.append((f"{edge.get('id', '?')} evidence[{i}]", ev, graph_species))
    for holder_id, holder, species in holders:
        for key in GENE_DESCRIPTOR_FIELDS:
            for m in holder.get(key) or []:
                if isinstance(m, dict):
                    yield holder_id, m, species
        for ms in holder.get("marker_sets") or []:
            if not isinstance(ms, dict):
                continue
            for m in ms.get("genes") or []:
                if isinstance(m, dict):
                    yield f"{holder_id} marker_set {ms.get('id', '?')}", m, species


def _iter_marker_ids(doc: dict) -> Iterator[tuple[str, dict, str | None]]:
    """Node markers that carry an ``ncbi_gene_id`` or a ``symbol``.

    Edge-evidence markers are not checked here. A gene on an edge must be
    consistent with the two nodes it links (the taxonomy DB node and the
    graph node), not looked up on its own; that check, with cross-species
    mapping, is future work."""
    for holder_id, m, species in iter_gene_descriptors(doc, edges=False):
        if m.get("ncbi_gene_id") or m.get("symbol"):
            yield holder_id, m, species


_TAXON_PARENTS: dict[str, str] | None = None


def _taxon_is_a(child: str, ancestor: str, taxslim: Path | None) -> bool | None:
    """Whether NCBITaxon ``child`` is ``ancestor`` or below it, from the
    taxslim OBO. None when the OBO isn't available."""
    global _TAXON_PARENTS
    if child == ancestor:
        return True
    if _TAXON_PARENTS is None:
        if taxslim is None or not taxslim.is_file():
            return None
        parents: dict[str, str] = {}
        cur: str | None = None
        with taxslim.open(encoding="utf-8") as fh:
            for ln in fh:
                if ln.startswith("id: NCBITaxon:"):
                    cur = ln[4:].strip()
                elif ln.startswith("is_a: NCBITaxon:") and cur and cur not in parents:
                    parents[cur] = ln[6:].split("!")[0].strip()
        _TAXON_PARENTS = parents
    node: str | None = child
    seen: set[str] = set()
    while node and node not in seen:
        if node == ancestor:
            return True
        seen.add(node)
        node = _TAXON_PARENTS.get(node)
    return False


def check_marker_gene_ids(
    doc: dict,
    *,
    cache_path: Path | None = None,
    taxonomy_root: Path | None = None,
    taxslim: Path | None = None,
) -> tuple[list[str], list[str]]:
    """Validate every ``ncbi_gene_id`` and ``symbol`` on a KB graph's markers.

    ``symbol`` and ``ncbi_gene_id`` must be set together (#244). Each ID must
    exist in NodeNormalization as an NCBIGene gene, belong to the node's
    species (or graph species; a gene of a descendant taxon is accepted,
    e.g. a human gene on a Primates node), and ``symbol`` must be the gene's
    official symbol exactly (its NodeNormalization label). ``name_in_source``
    — the source's wording — is not checked. (A pre-#244 marker without
    ``name_in_source`` fails schema validation before this runs.)

    Returns ``(errors, unchecked)``: ``unchecked`` lists ``"ID: reason"``
    for checks that could not run — the ID could not be looked up (offline
    and not cached), or its species could not be compared (no node or graph
    species, no taxon for the gene, or a gene of another taxon and no
    taxslim OBO to test descent) — reported as a soft skip.

    Covers node marker lists only; edge-evidence markers are unchecked
    (see :func:`_iter_marker_ids`).
    """
    from evidencell.paths import repo_root

    entries = list(_iter_marker_ids(doc))
    if not entries:
        return [], []
    errors: list[str] = []
    paired = []
    for node_id, m, species in entries:
        name = marker_name(m)
        if bool(m.get("symbol")) != bool(m.get("ncbi_gene_id")):
            have, lack = ("symbol", "ncbi_gene_id") if m.get("symbol") else ("ncbi_gene_id", "symbol")
            errors.append(
                f"{node_id}: marker {name!r} has {have} but no {lack} — set both (the gene "
                "and its official symbol) or neither; the source's wording goes in "
                "name_in_source (see docs/marker_gene_ids.md)"
            )
        elif m.get("ncbi_gene_id"):
            paired.append((node_id, m, species))
    entries = paired
    if not entries:
        return errors, []
    root = repo_root()
    cache = _GeneRecordCache(
        cache_path or gene_id_cache_path(),
        taxonomy_root if taxonomy_root is not None else root / "kb" / "taxonomy",
    )
    taxslim = taxslim if taxslim is not None else root / "conf" / "oak_dbs" / "taxslim.obo"
    records, unreachable = cache.get({e[1]["ncbi_gene_id"] for e in entries})
    cache.save()

    unchecked = [f"{i}: Translator NodeNormalization unreachable, not cached" for i in unreachable]
    for node_id, m, species in entries:
        nid = m["ncbi_gene_id"]
        symbol = m.get("symbol") or ""
        rec = records.get(nid)
        if rec is None:
            continue
        where = f"{node_id}: marker {marker_name(m)!r} ncbi_gene_id {nid}"
        if rec.get("missing"):
            if rec.get("replaced_by"):
                errors.append(
                    f"{where} is not a current NCBI gene ID: NodeNormalization gives "
                    f"{rec['replaced_by']} (a merged or replaced record) — check that "
                    "gene and use its ID and official symbol"
                )
            else:
                errors.append(f"{where} does not resolve to an NCBI gene (NodeNormalization)")
            continue
        if not species:
            unchecked.append(
                f"{nid}: species not compared — {node_id} has no species and the graph "
                "has none"
            )
        elif not rec.get("taxon"):
            unchecked.append(f"{nid}: species not compared — no taxon in NodeNormalization")
        else:
            ok = _taxon_is_a(rec["taxon"], species, taxslim)
            if ok is False:
                errors.append(
                    f"{where} is a {rec['taxon']} gene ({rec['label']}), "
                    f"but the node's species is {species}"
                )
            elif ok is None:
                unchecked.append(
                    f"{nid}: species {rec['taxon']} vs node {species} not compared — "
                    "taxslim OBO missing (run `just fetch-oak-dbs`)"
                )
        if symbol != rec.get("label"):
            errors.append(
                f"{where} is {rec['label']}; symbol must be its official symbol "
                f"{rec['label']!r}, not {symbol!r}. The source's wording goes in "
                "name_in_source (see docs/marker_gene_ids.md)."
            )
    return errors, unchecked


# ── CLI ──────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="python -m evidencell.gene_identity")
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="build kb/taxonomy/{tid}/gene_ids.tsv.gz (network)")
    f.add_argument("taxonomy_id")
    f.add_argument("--stats", type=Path, default=None)

    r = sub.add_parser("resolve", help="candidate genes for marker names (JSON)")
    r.add_argument("names", nargs="+")
    g = r.add_mutually_exclusive_group(required=True)
    g.add_argument("--taxonomy", help="resolve against this taxonomy's gene tables (offline)")
    g.add_argument("--taxon", help="resolve via Name Resolver for this NCBITaxon CURIE")

    args = p.parse_args(argv)
    if args.cmd == "fetch":
        fetch_gene_ids(args.taxonomy_id, stats_path=args.stats)
    elif args.cmd == "resolve":
        try:
            res = resolve_for_curation(args.names, taxonomy_id=args.taxonomy, taxon=args.taxon)
        except GeneIdsUnavailable as exc:
            sys.exit(f"ERROR: {exc}")
        print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
