"""Canonical protein-name → mouse-gene-symbol aliases.

Single source of truth for the mapping used by Stage B emit
(``stage_b_emit._resolve_symbol``), the property-comparison refresher
(``refresh_property_comparisons``), and the legacy value-refresher
(``refresh_expression_pcs._resolve_lookup_keys``).

Keep entries short and biologically obvious; if a symbol is ambiguous
across species or contexts, add it to the per-call lookup logic rather
than here. Treat this map as case-sensitive — both sides written in
the canonical form used in evidencell KB graphs.

Add entries here when a new classical-side marker symbol fails to
match the atlas-side canonical gene symbol. After adding, no other
code needs to change: every consumer reuses
:func:`resolve_to_canonical_gene_symbol`.
"""

from __future__ import annotations

# Common protein-name → mouse-gene-symbol aliases. Lower-priority
# than exact-match: when looking up a value for a symbol, callers
# typically try the symbol verbatim first, then its alias resolution.
PROTEIN_TO_GENE_ALIASES: dict[str, str] = {
    "mGluR1": "Grm1",
    "mGluR5": "Grm5",
    "GFAP":   "Gfap",
    "PV":     "Pvalb",
    "GAD67":  "Gad1",
    "GAD65":  "Gad2",
    "CR":     "Calb2",
    "CB":     "Calb1",
    "CCK":    "Cck",
    "NPY":    "Npy",
    "VIP":    "Vip",
    "SST":    "Sst",
    "NOS":    "Nos1",
    "5-HT3a": "Htr3a",
    "5HT3a":  "Htr3a",
    "5HT3aR": "Htr3a",
}


def resolve_to_canonical_gene_symbol(symbol: str) -> str:
    """Return the canonical mouse gene symbol for an input symbol.

    If ``symbol`` is in :data:`PROTEIN_TO_GENE_ALIASES`, returns the
    mapped gene symbol; otherwise returns ``symbol`` verbatim.
    """
    return PROTEIN_TO_GENE_ALIASES.get(symbol, symbol)
