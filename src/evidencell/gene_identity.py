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
  fills the ``genes`` and ``gene_synonyms`` tables from that file, plus the
  curated overrides in ``kb/taxonomy/{tid}/gene_overrides.tsv``.
- **Resolve** — :func:`resolve_names` turns marker names into genes of the
  taxonomy, in this order:

  1. ``PINNED_ID``: the marker's ``ncbi_gene_id`` is a gene of this taxonomy.
  2. ``OVERRIDE``: a reviewed override names exactly one gene.
  3. ``EXACT_SYMBOL``: the name is a gene's symbol (stats symbol or current
     label), case-sensitive; then ``CASE_INSENSITIVE_SYMBOL``, compared
     after :func:`normalise_name` (a symbol beats other genes' synonyms).
  4. ``UNIQUE_SYNONYM``: exactly one gene lists the name as a synonym.

  Two or more claimants is ``AMBIGUOUS`` and none is ``NO_MATCH``: neither
  is guessed. A curator (or curating agent) picks from the claimant list
  and records the choice as the marker's ``ncbi_gene_id`` or as an
  override. Claimant counting runs over the taxonomy's gene universe, which
  is right for whole-transcriptome stats files (WMB, HMBA) but would give
  false "unique" results for a targeted panel.

The hook check (:func:`check_marker_gene_ids`) validates every
``ncbi_gene_id`` written to ``kb/graphs`` against NodeNormalization: the ID
exists, belongs to the node's species, and the marker's symbol is its label
or one of its names. Lookups are cached in ``conf/gene_id_cache.json``
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
GENE_OVERRIDES_FILE = "gene_overrides.tsv"

GENE_IDS_COLUMNS = (
    "ensembl_id", "stats_symbol", "stats_col", "ncbi_gene_id", "label",
    "taxon", "equivalent_ids", "synonyms",
)
OVERRIDE_COLUMNS = ("name", "ncbi_gene_id", "symbol", "rationale", "reviewed_by")

# Resolution methods (accepted) and failure reasons.
PINNED_ID = "PINNED_ID"
OVERRIDE = "OVERRIDE"
EXACT_SYMBOL = "EXACT_SYMBOL"
CASE_INSENSITIVE_SYMBOL = "CASE_INSENSITIVE_SYMBOL"
UNIQUE_SYNONYM = "UNIQUE_SYNONYM"
AMBIGUOUS = "AMBIGUOUS"
NO_MATCH = "NO_MATCH"
ACCEPTED_METHODS = (PINNED_ID, OVERRIDE, EXACT_SYMBOL, CASE_INSENSITIVE_SYMBOL, UNIQUE_SYNONYM)

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


def gene_overrides_path(taxonomy_id: str) -> Path:
    from evidencell.paths import taxonomy_dir

    return taxonomy_dir(taxonomy_id) / GENE_OVERRIDES_FILE


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


def read_overrides(path: Path) -> list[dict]:
    """Read ``gene_overrides.tsv`` (``#`` comment lines allowed)."""
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as fh:
        lines = [ln for ln in fh if not ln.startswith("#") and ln.strip()]
    rows = list(csv.DictReader(lines, delimiter="\t"))
    for r in rows:
        missing = [c for c in ("name", "ncbi_gene_id", "rationale", "reviewed_by") if not r.get(c)]
        if missing:
            raise ValueError(f"{path}: override row {r} is missing {', '.join(missing)}")
    return rows


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
    committed ``gene_ids.tsv.gz`` and ``gene_overrides.tsv``. Returns the
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
    known = {r["ncbi_gene_id"] for r in rows if r["ncbi_gene_id"]}
    for o in read_overrides(taxonomy_dir / GENE_OVERRIDES_FILE):
        if o["ncbi_gene_id"] not in known:
            raise ValueError(
                f"{taxonomy_dir / GENE_OVERRIDES_FILE}: override {o['name']!r} → "
                f"{o['ncbi_gene_id']} is not a gene of this taxonomy ({GENE_IDS_FILE})"
            )
        syn_rows.append((o["ncbi_gene_id"], o["name"], normalise_name(o["name"]), "override"))
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


def resolve_name(con: sqlite3.Connection, name: str, ncbi_gene_id: str | None = None) -> GeneMatch:
    """Resolve one marker name (optionally pinned to an NCBIGene ID)."""
    if ncbi_gene_id:
        hits = _one_per_ncbi(_genes(con, "ncbi_gene_id = ?", (ncbi_gene_id,)))
        if hits:
            return GeneMatch(name, PINNED_ID, hits[0])
        # An ID from another species: fall through to the name, which is
        # how a rat or human marker reaches a mouse taxonomy's genes.
    norm = normalise_name(name)

    over = _one_per_ncbi(_genes(
        con,
        "ncbi_gene_id IN (SELECT ncbi_gene_id FROM gene_synonyms "
        "WHERE synonym_norm = ? AND source = 'override')",
        (norm,),
    ))
    if len(over) == 1:
        return GeneMatch(name, OVERRIDE, over[0])
    if len(over) > 1:
        return GeneMatch(name, AMBIGUOUS, claimants=over)

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
    by_symbol = _one_per_ncbi(_genes(con, "symbol_norm = ? OR label_norm = ?", (norm, norm)))
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
    gene_ids: Mapping[str, str] | None = None,
) -> dict[str, GeneMatch]:
    """Resolve marker names; ``gene_ids`` pins a name to its curated
    ``ncbi_gene_id``. Raises :class:`GeneIdsUnavailable` when the DB has no
    gene tables."""
    if not has_gene_tables(con):
        raise GeneIdsUnavailable(
            "The taxonomy DB has no gene identity tables. Commit "
            f"kb/taxonomy/{{tid}}/{GENE_IDS_FILE} (just build-gene-ids {{tid}}) and rebuild "
            "with just build-taxonomy-db {tid}."
        )
    gene_ids = gene_ids or {}
    return {n: resolve_name(con, n, gene_ids.get(n)) for n in dict.fromkeys(names) if n}


# ── Classical-node helpers ───────────────────────────────────────────────────

MARKER_FIELDS = ("defining_markers", "negative_markers", "neuropeptides")


def marker_gene_ids(node: dict) -> dict[str, str]:
    """``{symbol: ncbi_gene_id}`` for a classical node's markers that carry
    a curated ID — the pins passed to :func:`resolve_names`."""
    out: dict[str, str] = {}
    for key in MARKER_FIELDS:
        for m in node.get(key) or []:
            if isinstance(m, dict) and m.get("symbol") and m.get("ncbi_gene_id"):
                out.setdefault(m["symbol"], m["ncbi_gene_id"])
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
    """NCBIGene ID → ``{label, taxon, names}`` (or ``{"missing": True}``).

    Backed by ``conf/gene_id_cache.json`` and seeded from every committed
    ``kb/taxonomy/*/gene_ids.tsv.gz``; misses go to NodeNorm + Name Resolver.
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
                    else:
                        self.data[i] = {"missing": True}
                self._dirty = True
        return {i: self.data[i] for i in ids if i in self.data}, unreachable

    def save(self) -> None:
        if not self._dirty:
            return
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text(json.dumps(self.data, sort_keys=True), encoding="utf-8")
        except OSError:
            pass


def _iter_marker_ids(doc: dict) -> Iterator[tuple[str, str, str, str | None]]:
    """(node_id, symbol, ncbi_gene_id, species) for every GeneDescriptor in a
    KB graph that carries an ``ncbi_gene_id``."""
    def sid(x: Any) -> str | None:
        return x.get("id") if isinstance(x, dict) else x

    graph_species = sid(doc.get("species"))
    for node in doc.get("nodes") or []:
        if not isinstance(node, dict):
            continue
        species = sid(node.get("species")) or graph_species
        for key in (*MARKER_FIELDS, "merfish_markers", "markers"):
            for m in node.get(key) or []:
                if isinstance(m, dict) and m.get("ncbi_gene_id"):
                    yield node.get("id", "?"), m.get("symbol") or "", m["ncbi_gene_id"], species


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
    """Validate every ``ncbi_gene_id`` on a KB graph's markers.

    Each ID must exist in NodeNormalization as an NCBIGene gene, belong to
    the node's species (or graph species; a gene of a descendant taxon is
    accepted, e.g. a human gene on a Primates node), and the marker's
    ``symbol`` must be the gene's label, one of its names, or a reviewed
    override name for it in a ``kb/taxonomy/*/gene_overrides.tsv``
    (compared after :func:`normalise_name`).

    Returns ``(errors, unchecked)``: ``unchecked`` lists ``"ID: reason"``
    for checks that could not run — the ID could not be looked up (offline
    and not cached), or its species could not be compared (gene of another
    taxon and no taxslim OBO to test descent) — reported as a soft skip.
    """
    from evidencell.paths import repo_root

    entries = list(_iter_marker_ids(doc))
    if not entries:
        return [], []
    root = repo_root()
    cache = _GeneRecordCache(
        cache_path or gene_id_cache_path(),
        taxonomy_root if taxonomy_root is not None else root / "kb" / "taxonomy",
    )
    taxslim = taxslim if taxslim is not None else root / "conf" / "oak_dbs" / "taxslim.obo"
    records, unreachable = cache.get({e[2] for e in entries})
    cache.save()
    # Reviewed overrides are curated names for their gene (TuJ1 → Tubb3).
    override_names: dict[str, set[str]] = {}
    tax_root = cache.taxonomy_root
    for f in sorted(tax_root.glob(f"*/{GENE_OVERRIDES_FILE}")) if tax_root else []:
        for o in read_overrides(f):
            override_names.setdefault(o["ncbi_gene_id"], set()).add(normalise_name(o["name"]))

    unchecked = [f"{i}: Translator NodeNormalization unreachable, not cached" for i in unreachable]
    errors: list[str] = []
    for node_id, symbol, nid, species in entries:
        rec = records.get(nid)
        if rec is None:
            continue
        where = f"{node_id}: marker {symbol!r} ncbi_gene_id {nid}"
        if rec.get("missing"):
            errors.append(f"{where} does not resolve to an NCBI gene (NodeNormalization)")
            continue
        if species and rec.get("taxon"):
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
        names = {normalise_name(n) for n in [rec.get("label") or "", *rec.get("names", [])]}
        names |= override_names.get(nid, set())
        if symbol and normalise_name(symbol) not in names:
            errors.append(
                f"{where} is {rec['label']}; {symbol!r} is not its label or a known "
                "synonym. Check the ID, or resolve the name with "
                "`just resolve-gene-names` (see the gene-id-curation skill)."
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
