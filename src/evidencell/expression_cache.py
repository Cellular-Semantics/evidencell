"""On-demand atlas expression, cached in the taxonomy SQLite DB (#189).

Expression values are derived data: they come from the MapMyCells
precomputed-stats HDF5 for a taxonomy, not from the taxonomy YAML. This
module reads them one gene column at a time and caches them in two DB
tables:

- ``node_expression(node_id, symbol, ensembl_id, mean_expression)`` — one
  row per atlas node × cached gene. Leaf (rank-0) values are the stats
  file's per-cluster means; every non-leaf node gets the n_cells-weighted
  mean of its rank-0 descendants. With ``n_cells == 1`` throughout (WMBv1)
  that is a plain, unweighted average of cluster means.
- ``expression_genes(symbol, ensembl_id, status, source_file,
  source_sha256, loaded_at)`` — which genes are cached and from which
  file. ``status`` is ``MEASURED``, or a not-measured reason
  (``NO_ENSEMBL_MAPPING``, ``NOT_IN_STATS``) so an unmeasurable gene is a
  recorded gap, never a silent empty result.

``just build-taxonomy-db`` creates both tables empty; they fill on use.
Consumers go through :meth:`TaxonomyDB.expression`, which calls
:func:`ensure_genes` then :func:`query`.

File locations come from the existing registry, not new config: the stats
file is ``conf/mapmycells/{taxonomy_id}/{basename of stats_s3_url}`` (the
URL from ``annotation_transfer/src/annotation_transfer/taxonomies.py``,
which is where ``just fetch-mapmycells`` writes it) and the gene mapping is
``conf/gene_mapping_{taxonomy_id}.tsv``.

The cache is dropped (and reloads on use) when the stats file's sha256,
the gene mapping TSV or the protein-alias table changes — each one decides
which column, if any, a symbol reads.

Fail closed: a gene that is not cached and cannot be loaded (stats file or
gene mapping missing) raises :class:`ExpressionUnavailable` with the fix.

Stats format: ``sum`` is the per-cluster sum of expression over cells and
``n_cells`` the cell count, so a cluster mean is ``sum / n_cells``. The
WMBv1 file (``precomputed_stats_ABC_revision_230821.h5``) was built from
cluster means with ``n_cells == 1`` throughout, so its ``sum`` already is
the mean; dividing keeps files built from real cell sums correct too.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sqlite3
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

MEASURED = "MEASURED"
NO_ENSEMBL_MAPPING = "NO_ENSEMBL_MAPPING"
NOT_IN_STATS = "NOT_IN_STATS"

_FINGERPRINT_KEY = "expression_stats_fingerprint"
_RESOLUTION_KEY = "expression_resolution_fingerprint"


class ExpressionUnavailable(RuntimeError):
    """Expression is needed but can't be read (stats file / mapping missing)."""


@dataclass
class ExpressionLookup:
    """Result of an expression query.

    ``values``: ``{node_id: {symbol: mean_expression}}`` for measured genes.
    ``not_measured``: ``{symbol: reason}`` for genes that can't be measured.
    ``source_file``: basename of the stats file the cache was filled from.
    """

    values: dict[str, dict[str, float]] = field(default_factory=dict)
    not_measured: dict[str, str] = field(default_factory=dict)
    source_file: str | None = None

    def for_node(self, accession: str) -> dict[str, float]:
        return self.values.get(_node_id(accession), {})


# ── File locations (registry-driven) ─────────────────────────────────────────


def _load_registry() -> dict:
    """Load ``_BUILTIN_TAXONOMIES`` from the annotation_transfer registry.

    annotation_transfer is not installed into the evidencell environment
    (the justfile reaches it via PYTHONPATH), so load the module by path.
    """
    from evidencell.paths import repo_root

    name = "_evidencell_at_taxonomies"
    if name not in sys.modules:
        path = (
            repo_root() / "annotation_transfer" / "src" / "annotation_transfer" / "taxonomies.py"
        )
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None or not path.is_file():
            raise ExpressionUnavailable(f"MapMyCells taxonomy registry not found at {path}")
        module = importlib.util.module_from_spec(spec)
        # Registered before exec: the module's dataclasses resolve their
        # annotations through sys.modules.
        sys.modules[name] = module
        try:
            spec.loader.exec_module(module)
        except Exception:
            del sys.modules[name]
            raise
    return sys.modules[name]._BUILTIN_TAXONOMIES


def stats_h5_path(taxonomy_id: str) -> Path:
    """Canonical local path of a taxonomy's precomputed-stats HDF5."""
    from evidencell.paths import repo_root

    spec = _load_registry().get(taxonomy_id)
    if spec is None or not spec.stats_s3_url:
        raise ExpressionUnavailable(
            f"No MapMyCells stats file is registered for taxonomy {taxonomy_id} "
            "(annotation_transfer/src/annotation_transfer/taxonomies.py), so atlas "
            "expression can't be read for it."
        )
    name = Path(urlparse(spec.stats_s3_url).path).name
    return repo_root() / "conf" / "mapmycells" / taxonomy_id / name


def gene_mapping_path(taxonomy_id: str) -> Path:
    """Canonical local path of a taxonomy's symbol → Ensembl mapping TSV."""
    from evidencell.paths import repo_root

    return repo_root() / "conf" / f"gene_mapping_{taxonomy_id}.tsv"


def load_gene_mapping(mapping_path: str | Path) -> dict[str, str]:
    """Load symbol → Ensembl ID mapping from a TSV file.

    Expected format: header row naming 'symbol' and 'ensembl_id' columns.
    """
    mapping: dict[str, str] = {}
    with open(mapping_path, encoding="utf-8") as fh:
        header = fh.readline().strip().split("\t")
        sym_col = header.index("symbol")
        ens_col = header.index("ensembl_id")
        for line in fh:
            parts = line.strip().split("\t")
            if len(parts) > max(sym_col, ens_col):
                mapping[parts[sym_col]] = parts[ens_col]
    return mapping


# ── Cache maintenance ────────────────────────────────────────────────────────


def _node_id(accession: str) -> str:
    return accession.split(":", 1)[-1] if ":" in accession else accession


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _stats_sha256(con: sqlite3.Connection, stats_path: Path) -> str:
    """sha256 of the stats file, memoised in ``_meta`` by (path, size, mtime).

    Hashing a 1.4 GB file takes seconds; a stat() does not. The hash is
    recomputed only when the file's size or mtime changes.
    """
    st = stats_path.stat()
    fp = {"path": str(stats_path.resolve()), "size": st.st_size, "mtime_ns": st.st_mtime_ns}
    con.execute("CREATE TABLE IF NOT EXISTS _meta (key TEXT PRIMARY KEY, value TEXT)")
    row = con.execute("SELECT value FROM _meta WHERE key = ?", (_FINGERPRINT_KEY,)).fetchone()
    if row:
        stored = json.loads(row[0])
        if all(stored.get(k) == v for k, v in fp.items()):
            return stored["sha256"]
    sha = _sha256(stats_path)
    con.execute(
        "INSERT OR REPLACE INTO _meta VALUES (?, ?)",
        (_FINGERPRINT_KEY, json.dumps({**fp, "sha256": sha})),
    )
    return sha


def _drop_stale_cache(con: sqlite3.Connection, sha: str) -> None:
    """Drop the cache when it was filled from a different stats file release."""
    stale = con.execute(
        "SELECT COUNT(*) FROM expression_genes WHERE source_sha256 != ?", (sha,)
    ).fetchone()[0]
    if stale:
        print(
            f"  Stats file changed since the expression cache was filled — "
            f"dropping {stale} cached gene(s); they reload on use.",
            file=sys.stderr,
        )
        con.execute("DELETE FROM node_expression")
        con.execute("DELETE FROM expression_genes")


def _resolution_fingerprint(mapping_path: Path) -> dict[str, str | None]:
    """Hashes of what turns a symbol into a stats column: the gene mapping
    TSV and the protein-alias table. ``mapping`` is None when the TSV is
    absent."""
    from evidencell.marker_aliases import PROTEIN_TO_GENE_ALIASES

    aliases = json.dumps(sorted(PROTEIN_TO_GENE_ALIASES.items())).encode()
    return {
        "aliases": hashlib.sha256(aliases).hexdigest(),
        # Small (~1 MB): hashed directly on each call, unlike the stats file.
        "mapping": (
            hashlib.sha256(mapping_path.read_bytes()).hexdigest()
            if mapping_path.is_file() else None
        ),
    }


def _drop_cache_if_resolution_changed(con: sqlite3.Connection, mapping_path: Path) -> None:
    """Drop the cache when the gene mapping or alias table changed since it
    was filled: a cached ``NO_ENSEMBL_MAPPING`` (or a gene resolved to a
    different Ensembl ID) would otherwise outlive the fix until the next
    ``build-taxonomy-db``.

    With the mapping TSV absent only the alias table is compared, so a
    filled cache keeps serving without it.
    """
    current = _resolution_fingerprint(mapping_path)
    con.execute("CREATE TABLE IF NOT EXISTS _meta (key TEXT PRIMARY KEY, value TEXT)")
    row = con.execute("SELECT value FROM _meta WHERE key = ?", (_RESOLUTION_KEY,)).fetchone()
    stored = json.loads(row[0]) if row else {}
    changed = [
        k for k in ("aliases", "mapping")
        if current[k] is not None and stored.get(k) is not None and stored[k] != current[k]
    ]
    if changed:
        n = con.execute("SELECT COUNT(*) FROM expression_genes").fetchone()[0]
        if n:
            what = " and ".join(
                {"aliases": "protein-alias table", "mapping": f"gene mapping ({mapping_path.name})"}[k]
                for k in changed
            )
            print(
                f"  The {what} changed since the expression cache was filled — "
                f"dropping {n} cached gene(s); they reload on use.",
                file=sys.stderr,
            )
        con.execute("DELETE FROM node_expression")
        con.execute("DELETE FROM expression_genes")
    merged = {k: current[k] if current[k] is not None else stored.get(k) for k in current}
    if merged != stored:
        con.execute(
            "INSERT OR REPLACE INTO _meta VALUES (?, ?)", (_RESOLUTION_KEY, json.dumps(merged))
        )
        con.commit()


def _resolve_ensembl(symbol: str, mapping: dict[str, str]) -> str | None:
    from evidencell.marker_aliases import resolve_to_canonical_gene_symbol

    ens = mapping.get(symbol)
    if ens is None:
        canon = resolve_to_canonical_gene_symbol(symbol)
        if canon != symbol:
            ens = mapping.get(canon)
    return ens


def ensure_genes(
    con: sqlite3.Connection,
    taxonomy_id: str,
    symbols: Iterable[str],
    *,
    stats_path: Path,
    mapping_path: Path,
) -> None:
    """Make sure every symbol has an ``expression_genes`` row, loading
    uncached genes from the stats HDF5.

    Raises :class:`ExpressionUnavailable` if any symbol is uncached and the
    stats file or gene mapping is missing.
    """
    wanted = sorted({s for s in symbols if s})
    if not wanted:
        return

    have_stats = stats_path.is_file()
    sha = _stats_sha256(con, stats_path) if have_stats else None
    if sha is not None:
        _drop_stale_cache(con, sha)
    _drop_cache_if_resolution_changed(con, mapping_path)

    placeholders = ",".join("?" * len(wanted))
    cached = {
        r[0]
        for r in con.execute(
            f"SELECT symbol FROM expression_genes WHERE symbol IN ({placeholders})", wanted
        )
    }
    missing = [s for s in wanted if s not in cached]
    if not missing:
        return

    sample = ", ".join(missing[:8]) + (" …" if len(missing) > 8 else "")
    if not have_stats:
        raise ExpressionUnavailable(
            f"Atlas expression for {len(missing)} gene(s) ({sample}) is not cached in the "
            f"{taxonomy_id} taxonomy DB and the MapMyCells stats file is missing: "
            f"{stats_path}. Run: just fetch-mapmycells {taxonomy_id}"
        )
    if not mapping_path.is_file():
        raise ExpressionUnavailable(
            f"Atlas expression for {len(missing)} gene(s) ({sample}) needs the gene "
            f"mapping TSV, which is missing: {mapping_path}. Run: just "
            f"generate-gene-mapping {stats_path} {mapping_path}"
        )
    assert sha is not None
    _load_genes(con, missing, stats_path=stats_path, mapping_path=mapping_path, sha=sha)


def _leaf_descendants(con: sqlite3.Connection) -> tuple[list[str], dict[str, list[str]]]:
    """Return (rank-0 node ids, {non-leaf node id: rank-0 descendant ids})."""
    rows = con.execute("SELECT node_id, parent_id, taxonomy_rank FROM nodes").fetchall()
    children: dict[str, list[str]] = {}
    rank_of: dict[str, int | None] = {}
    for node_id, parent_id, rank in rows:
        rank_of[node_id] = rank
        if parent_id:
            children.setdefault(parent_id, []).append(node_id)
    leaves = [n for n, r in rank_of.items() if r == 0]
    out: dict[str, list[str]] = {}
    for node_id, rank in rank_of.items():
        if rank == 0 or node_id not in children:
            continue
        found: list[str] = []
        stack = list(children[node_id])
        seen: set[str] = set()
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            if rank_of.get(n) == 0:
                found.append(n)
            else:
                stack.extend(children.get(n, []))
        if found:
            out[node_id] = found
    return leaves, out


def _load_genes(
    con: sqlite3.Connection,
    symbols: list[str],
    *,
    stats_path: Path,
    mapping_path: Path,
    sha: str,
) -> None:
    import h5py
    import numpy as np

    mapping = load_gene_mapping(mapping_path)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    source = stats_path.name

    with h5py.File(str(stats_path), "r") as f:
        col_names: list[str] = json.loads(f["col_names"][()])
        cluster_to_row: dict[str, int] = json.loads(f["cluster_to_row"][()])
        n_cells = np.asarray(f["n_cells"][:], dtype=float)
        ens_to_col = {e: i for i, e in enumerate(col_names)}

        status: dict[str, tuple[str | None, str]] = {}  # symbol → (ensembl, status)
        measured: list[tuple[str, str, int]] = []  # (symbol, ensembl, col)
        for sym in symbols:
            ens = _resolve_ensembl(sym, mapping)
            if ens is None:
                status[sym] = (None, NO_ENSEMBL_MAPPING)
            elif ens not in ens_to_col:
                status[sym] = (ens, NOT_IN_STATS)
            else:
                status[sym] = (ens, MEASURED)
                measured.append((sym, ens, ens_to_col[ens]))

        node_rows: list[tuple[str, str, str, float]] = []
        if measured:
            # Read only the needed columns, never the whole matrix. h5py needs
            # increasing indices for a fancy selection.
            cols = sorted({c for _, _, c in measured})
            col_pos = {c: i for i, c in enumerate(cols)}
            sums = np.asarray(f["sum"][:, cols], dtype=float)

            leaves, descendants = _leaf_descendants(con)
            leaf_row = {n: cluster_to_row[n] for n in leaves if n in cluster_to_row}
            if not leaf_row:
                raise ExpressionUnavailable(
                    f"None of the taxonomy's leaf node ids appear in the stats file's "
                    f"cluster_to_row ({stats_path}); is it the right file for this taxonomy?"
                )

            def _emit(node_id: str, rows: list[int]) -> None:
                total = n_cells[rows].sum()
                if total <= 0:
                    return
                means = sums[rows].sum(axis=0) / total
                for sym, ens, col in measured:
                    node_rows.append((node_id, sym, ens, float(means[col_pos[col]])))

            for node_id, row in leaf_row.items():
                _emit(node_id, [row])
            for node_id, leaf_ids in descendants.items():
                rows = [leaf_row[n] for n in leaf_ids if n in leaf_row]
                if rows:
                    _emit(node_id, rows)

    con.executemany("INSERT OR REPLACE INTO node_expression VALUES (?, ?, ?, ?)", node_rows)
    con.executemany(
        "INSERT OR REPLACE INTO expression_genes VALUES (?, ?, ?, ?, ?, ?)",
        [(sym, ens, st, source, sha, now) for sym, (ens, st) in status.items()],
    )
    con.commit()
    n_measured = sum(1 for _, st in status.values() if st == MEASURED)
    print(
        f"  Loaded expression for {n_measured}/{len(symbols)} gene(s) from {source} "
        f"into the taxonomy DB cache",
        file=sys.stderr,
    )


# ── Query ────────────────────────────────────────────────────────────────────


def query(
    con: sqlite3.Connection,
    symbols: Iterable[str],
    *,
    accessions: Iterable[str] | None = None,
    ranks: Iterable[int] | None = None,
) -> ExpressionLookup:
    """Read cached expression for ``symbols``.

    Restrict nodes with ``accessions`` and/or ``ranks``; with neither,
    every node is returned. Call :func:`ensure_genes` first.
    """
    wanted = sorted({s for s in symbols if s})
    out = ExpressionLookup()
    if not wanted:
        return out
    sym_ph = ",".join("?" * len(wanted))
    for sym, st in con.execute(
        f"SELECT symbol, status FROM expression_genes WHERE symbol IN ({sym_ph})", wanted
    ):
        if st != MEASURED:
            out.not_measured[sym] = st
    row = con.execute(
        f"SELECT source_file FROM expression_genes WHERE symbol IN ({sym_ph}) LIMIT 1", wanted
    ).fetchone()
    out.source_file = row[0] if row else None

    sql = (
        "SELECT e.node_id, e.symbol, e.mean_expression FROM node_expression e "
        f"JOIN nodes n ON n.node_id = e.node_id WHERE e.symbol IN ({sym_ph})"
    )
    params: list = list(wanted)
    if accessions is not None:
        ids = sorted({_node_id(a) for a in accessions if a})
        if not ids:
            return out
        sql += f" AND e.node_id IN ({','.join('?' * len(ids))})"
        params += ids
    if ranks is not None:
        rank_list = sorted(set(ranks))
        sql += f" AND n.taxonomy_rank IN ({','.join('?' * len(rank_list))})"
        params += rank_list
    for node_id, sym, val in con.execute(sql, params):
        out.values.setdefault(node_id, {})[sym] = float(val)
    return out
