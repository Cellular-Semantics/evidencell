# Gao 2023 PVT label re-derivation (DERIVED labels)

Input: 10307 neuronal nuclei (phase-1 Neurons 1-8, > 1000 genes), 33502 genes, 10 samples

## Step A: PVT vs neighbouring nuclei (paper phase 2; 6 PCs)
Resolution scan (res, n_clusters, silhouette): [(0.05, 4, 0.349), (0.1, 5, 0.393), (0.15, 5, 0.373), (0.2, 6, 0.369), (0.25, 6, 0.304), (0.3, 7, 0.323), (0.35, 9, 0.235), (0.4, 10, 0.211), (0.45, 11, 0.21), (0.5, 11, 0.205), (0.55, 13, 0.199), (0.6, 14, 0.2), (0.65, 15, 0.21), (0.7, 18, 0.209), (0.75, 18, 0.198), (0.8, 20, 0.172), (0.85, 20, 0.2), (0.9, 19, 0.189), (0.95, 21, 0.194), (1.0, 21, 0.192), (1.05, 23, 0.175), (1.1, 24, 0.192), (1.15, 24, 0.182), (1.2, 24, 0.189), (1.25, 27, 0.173), (1.3, 25, 0.183), (1.35, 26, 0.177), (1.4, 27, 0.179), (1.45, 29, 0.167), (1.5, 28, 0.163)]
Chosen resolution 0.6: 14 clusters (over-clustered; named by identity markers {"PVT": ["Gck", "C1ql3", "Hcn1"], "Hb": ["Tac2"], "MD": ["Adarb2"], "IMD": ["Cdh24"], "BSTpr": ["Gpr101"]}, threshold 0.1).
|    |    PVT |     Hb |     MD |    IMD |   BSTpr |   Adarb2 |   C1ql3 |   Cdh24 |   Gck |   Gpr101 |   Hcn1 |   Tac2 | named      |    n |
|---:|-------:|-------:|-------:|-------:|--------:|---------:|--------:|--------:|------:|---------:|-------:|-------:|:-----------|-----:|
|  0 | -0.419 |  0.767 |  0.073 | -0.081 |  -0.013 |     0.46 |    0.19 |    0.02 |  0.03 |     0    |   0.08 |   0.87 | Hb         |  821 |
|  1 |  0.245 | -0.078 | -0.207 | -0.051 |  -0.01  |     0.18 |    0.9  |    0.05 |  0.47 |     0    |   0.92 |   0.02 | PVT        |  944 |
|  2 |  0.248 | -0.057 | -0.183 | -0.048 |  -0.013 |     0.2  |    0.92 |    0.05 |  0.4  |     0    |   0.97 |   0.04 | PVT        | 1011 |
|  3 |  0.167 | -0.076 | -0.21  | -0.056 |  -0.011 |     0.17 |    0.86 |    0.04 |  0.29 |     0    |   0.9  |   0.03 | PVT        | 1348 |
|  4 | -0.015 | -0.073 |  0.322 |  0.041 |  -0.013 |     0.71 |    0.68 |    0.14 |  0.1  |     0    |   0.73 |   0.03 | MD         |  672 |
|  5 |  0.245 | -0.073 | -0.243 | -0.062 |  -0.013 |     0.14 |    0.91 |    0.04 |  0.54 |     0    |   0.84 |   0.03 | PVT        |  991 |
|  6 |  0.343 | -0.085 | -0.186 | -0.087 |  -0.014 |     0.2  |    0.9  |    0.01 |  0.75 |     0    |   0.93 |   0.02 | PVT        |  426 |
|  7 |  0.179 | -0.063 | -0.206 | -0.004 |  -0.009 |     0.18 |    0.83 |    0.09 |  0.54 |     0    |   0.72 |   0.04 | PVT        |  653 |
|  8 | -0.221 | -0.041 | -0.103 |  0.008 |   0.123 |     0.28 |    0.25 |    0.11 |  0.12 |     0.14 |   0.52 |   0.06 | BSTpr      |  852 |
|  9 | -0.354 | -0.065 |  0.611 |  0.089 |  -0.012 |     0.99 |    0.25 |    0.19 |  0.04 |     0    |   0.21 |   0.04 | MD         |  912 |
| 10 | -0.342 | -0.076 |  0.477 |  0.011 |  -0.014 |     0.86 |    0.31 |    0.11 |  0.02 |     0    |   0.21 |   0.02 | MD         |  402 |
| 11 | -0.308 | -0.055 |  0.533 |  0.278 |  -0.014 |     0.92 |    0.25 |    0.38 |  0.04 |     0    |   0.34 |   0.05 | MD         |  348 |
| 12 | -0.105 | -0.07  |  0.024 |  0.162 |  -0.003 |     0.41 |    0.56 |    0.26 |  0.12 |     0.01 |   0.56 |   0.03 | IMD        |  805 |
| 13 | -0.136 |  0.03  | -0.211 | -0.058 |   0.002 |     0.17 |    0.56 |    0.04 |  0.11 |     0.02 |   0.48 |   0.13 | unassigned |  122 |

PVT nuclei: 5373 of 10307 (52.1%); paper: 5737 of 9845 (58.3%).
Identity counts: {"PVT": 5373, "MD": 2334, "BSTpr": 852, "Hb": 821, "IMD": 805, "unassigned": 122}; paper: MD 1758, IMD 609, BSTpr 879, Hb 862.

## Step B: PVT1-PVT5 (paper phase 3)
Scoring sets (Supp. 1c, pct.1 >= 0.3, pct_ratio >= 1.5, top 30 by pct_ratio): {"PVT1": ["Egflam", "Drd2", "Slc30a3", "Arhgef26", "Snx31", "Unc5b", "4933413L06Rik", "Ptger3", "Sema5b", "Mkx", "9130019P16Rik", "Adgrg2", "Oprk1", "4930598N05Rik", "Car8", "Jph1", "Mcub", "Mcf2", "Pcsk5", "Bdnf", "Lemd1", "Fbln1", "Gm28376", "Prlr", "Ralb", "Cda", "Gm15345", "Slc9b2", "Sfmbt2", "Gulp1"], "PVT2": ["Col12a1", "Trpm6", "Tmem26", "Pde3a", "Crybg1", "Sema5b", "5730419F03Rik", "Gm20713", "Trpc6", "Lypd6", "Xylt1", "Slc44a5", "Glis1", "Cast", "Epb41l2", "Igf1", "Col8a1", "Iqgap2", "Pdia5", "Tll1", "Gm1715", "Lemd1", "Tmem132cos", "Cpq", "Chrna7", "Itga8", "Nr2f1", "A330015K06Rik", "Adamts6", "Myo1e"], "PVT3": ["Maf", "Insrr", "Rerg", "Lamb1", "Satb2", "Htr1d", "C79798", "Rai14", "Ccdc187", "Glis3", "Bace2", "Map3k20", "Gda", "Abcc4", "Tspan9", "Cplx2", "Pparg", "Il6ra", "Bcl11b", "Lama3", "Cadps2", "Adamts18", "Dnah2", "Mak", "Gsg1l", "Pbx3", "Gm13481", "Gm26771", "Kcna1", "Nmbr"], "PVT4": ["Bmper", "Npsr1", "Actn2", "Adamts2", "Kirrel", "Hpcal1", "Ccdc187", "Sema3a", "Cemip", "Gm43948", "Gda", "Parm1", "Ankfn1", "Bcl11b", "Itgb8", "Glra3", "Col18a1", "Kcnj5", "Susd1", "Mylk", "Baiap3", "Dpy19l1", "Cpa6", "Cfap44", "Rab3b", "Nbl1", "Eda", "Rspo1", "Dctd", "Efnb3"], "PVT5": ["1700047F07Rik", "Slc22a3", "Drd3", "Cobll1", "Gsg1l", "Epb41l2", "Cyyr1", "Megf11", "Tmem132e", "Svil", "Glra2", "Mtus1", "Gdpd2", "Lemd1", "Lypd6b", "Myo1e", "Jph1", "Ppp1r14c", "Zhx2", "Rftn1", "Cox6a2", "Prrg4", "Ptger3", "Frmd6", "Gm12027", "Hsd17b7", "Mboat1", "Filip1", "Sh3rf3", "Ptchd4"]}
Missing from matrix: {"PVT1": [], "PVT2": [], "PVT3": [], "PVT4": [], "PVT5": []}

### B1 diagnostic: unsupervised re-clustering (18 PCs)
Resolution scan (res, n_clusters, silhouette): [(0.05, 2, 0.253), (0.075, 2, 0.237), (0.1, 2, 0.253), (0.125, 3, 0.115), (0.15, 3, 0.115), (0.175, 4, 0.119), (0.2, 4, 0.126), (0.225, 5, 0.135), (0.25, 5, 0.132), (0.275, 6, 0.126), (0.3, 7, 0.105), (0.325, 8, 0.123), (0.35, 7, 0.115), (0.375, 7, 0.111), (0.4, 8, 0.123), (0.425, 8, 0.118), (0.45, 8, 0.119), (0.475, 9, 0.118), (0.5, 10, 0.117), (0.525, 10, 0.119), (0.55, 11, 0.116), (0.575, 11, 0.114), (0.6, 10, 0.119), (0.625, 11, 0.115), (0.65, 12, 0.114), (0.675, 11, 0.117), (0.7, 12, 0.114), (0.725, 12, 0.112), (0.75, 13, 0.108), (0.775, 15, 0.109), (0.8, 14, 0.11)]
Five-cluster solutions, matched to PVT1-5 by mean marker-set z (Hungarian):
|   resolution |   silhouette | sizes                                                | best_match                                                        | mean_z_of_match                                         |
|-------------:|-------------:|:-----------------------------------------------------|:------------------------------------------------------------------|:--------------------------------------------------------|
|        0.225 |        0.135 | {"0": 237, "1": 685, "2": 2705, "3": 684, "4": 1062} | {"0": "PVT1", "1": "PVT5", "2": "PVT2", "3": "PVT4", "4": "PVT3"} | {"0": 0.49, "1": 1.07, "2": 0.59, "3": 1.77, "4": 1.57} |
|        0.25  |        0.132 | {"0": 631, "1": 1018, "2": 2319, "3": 681, "4": 724} | {"0": "PVT1", "1": "PVT3", "2": "PVT2", "3": "PVT4", "4": "PVT5"} | {"0": 0.42, "1": 1.64, "2": 0.72, "3": 1.77, "4": 1.06} |

### B2 assignment from the published marker sets
Counts: {"PVT1": 1373, "PVT2": 952, "PVT3": 1013, "PVT4": 953, "PVT5": 1082}
Margin (best - second z): median 0.71; 38% of nuclei < 0.5; per label median {"PVT1": 0.51, "PVT2": 0.62, "PVT3": 1.13, "PVT4": 0.91, "PVT5": 0.7}

Validation on held-out Supp. 1c DEGs (not used for scoring):
| label   |   n_heldout_degs |   r_log_pct_ratio |   median_derived_minus_published_pct1 |   frac_heldout_with_derived_ratio_gt1 |
|:--------|-----------------:|------------------:|--------------------------------------:|--------------------------------------:|
| PVT1    |              319 |             0.771 |                                -0.004 |                                 0.796 |
| PVT2    |              148 |             0.927 |                                -0.023 |                                 0.973 |
| PVT3    |              716 |             0.953 |                                -0.008 |                                 0.904 |
| PVT4    |              260 |             0.94  |                                -0.006 |                                 0.969 |
| PVT5    |              408 |             0.873 |                                -0.018 |                                 0.98  |

ISH markers (pct expressing per derived label; published pct.1/pct.2 where the gene is a Supp. 1c DEG of that cluster):
| gene    |   PVT1 |   PVT2 |   PVT3 |   PVT4 |   PVT5 |
|:--------|-------:|-------:|-------:|-------:|-------:|
| Col12a1 |  0.266 |  0.769 |  0.043 |  0.069 |  0.29  |
| Drd2    |  0.343 |  0.251 |  0.03  |  0.106 |  0.223 |
| Drd3    |  0.272 |  0.174 |  0.382 |  0.352 |  0.53  |
| Esr1    |  0.26  |  0.245 |  0.047 |  0.081 |  0.119 |
| Hcrtr1  |  0.026 |  0.023 |  0.067 |  0.161 |  0.036 |
| Npffr1  |  0.023 |  0.023 |  0.192 |  0.078 |  0.036 |
| gene    | label   |   derived_pct |   published_pct1 |   published_pct2 | in_scoring_set   |
|:--------|:--------|--------------:|-----------------:|-----------------:|:-----------------|
| Esr1    | PVT1    |         0.26  |            0.239 |            0.078 | False            |
| Col12a1 | PVT2    |         0.769 |            0.788 |            0.148 | True             |
| Npffr1  | PVT3    |         0.192 |            0.193 |            0.032 | False            |
| Hcrtr1  | PVT4    |         0.161 |            0.197 |            0.026 | False            |
| Drd3    | PVT3    |         0.382 |            0.383 |            0.183 | False            |
| Drd3    | PVT5    |         0.53  |            0.594 |            0.174 | True             |
| Drd2    | PVT1    |         0.343 |            0.318 |            0.095 | True             |

wrote labels_pvt_clusters.json: {"MD neuron (derived)": 2334, "PVT1": 1373, "PVT5": 1082, "PVT3": 1013, "PVT4": 953, "PVT2": 952, "BSTpr neuron (derived)": 852, "Hb neuron (derived)": 821, "IMD neuron (derived)": 805, "non-PVT neuron, unassigned (derived)": 122}

wrote labels_pvt_pooled.json: {"PVT": 5373, "MD neuron (derived)": 2334, "BSTpr neuron (derived)": 852, "Hb neuron (derived)": 821, "IMD neuron (derived)": 805, "non-PVT neuron, unassigned (derived)": 122}

wrote labels_pvt_ap.json: {"MD neuron (derived)": 2334, "pPVT-biased (PVT1+PVT2)": 2325, "aPVT-biased (PVT3+PVT4)": 1966, "pan-PVT (PVT5)": 1082, "BSTpr neuron (derived)": 852, "Hb neuron (derived)": 821, "IMD neuron (derived)": 805, "non-PVT neuron, unassigned (derived)": 122}
