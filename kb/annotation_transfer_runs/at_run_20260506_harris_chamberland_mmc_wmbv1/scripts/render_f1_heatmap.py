"""Render Chamberland-subfamily F1 heatmap from at-score output.

Faceted: 1 row per source subfamily (Chrna2, Ndnf, Sst_Nos1, Sst_Tac1),
4 columns (class/subclass/supertype/cluster). For each panel show top-N
target groups with F1 scores. Inspired by the existing OLM AT figure.
"""
from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

OUT = Path('/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/annotation_transfer/data/harris2018/f1_heatmap_by_class.png')
F1 = Path('/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/annotation_transfer/data/harris2018/f1_chamberland_by_class.csv')
LEVELS = ['class', 'subclass', 'supertype', 'cluster']
SUBFAMS = ['Chrna2', 'Ndnf', 'Sst_Nos1', 'Sst_Tac1']  # exclude unassigned
TOP_N = 6

df = pd.read_csv(F1)

fig, axes = plt.subplots(len(SUBFAMS), len(LEVELS),
                         figsize=(13, 1.0 + 1.0*len(SUBFAMS)),
                         constrained_layout=True)

for i, sf in enumerate(SUBFAMS):
    sub_df = df[df['source_label'] == sf]
    for j, lvl in enumerate(LEVELS):
        ax = axes[i, j]
        d = sub_df[sub_df['level'] == lvl].nlargest(TOP_N, 'n_cells')
        if d.empty:
            ax.set_axis_off(); continue
        # bar chart of F1 with target name as label, colored by f1
        d = d.sort_values('n_cells', ascending=True)
        f1_vals = d['f1'].values
        labels = [f'{n}  (n={c})' for n, c in zip(d['target_name'], d['n_cells'])]
        cmap = mpl.colormaps['viridis']
        bars = ax.barh(labels, f1_vals,
                       color=[cmap(min(v, 1.0)) for v in f1_vals],
                       edgecolor='black', linewidth=0.3)
        ax.set_xlim(0, 1)
        ax.tick_params(axis='y', labelsize=7)
        ax.tick_params(axis='x', labelsize=7)
        if i == 0:
            ax.set_title(lvl, fontsize=9, fontweight='bold')
        if j == 0:
            ax.set_ylabel(f'Source: {sf}', fontsize=9, fontweight='bold')
        # annotate F1 on each bar
        for bar, f in zip(bars, f1_vals):
            ax.text(min(f + 0.02, 0.96), bar.get_y() + bar.get_height()/2,
                    f'{f:.2f}', va='center', fontsize=6.5)

fig.suptitle(
    'Annotation transfer: Harris 2018 CA1 inhibitory cells → WMBv1 (CCN20230722)\n'
    'Source labels: Chamberland 2024 subfamilies (Chrna2, Ndnf, Sst::Nos1, Sst::Tac1) computed from gene expression',
    fontsize=10, y=1.04
)
fig.savefig(OUT, dpi=160, bbox_inches='tight')
print(f'Wrote {OUT}')
