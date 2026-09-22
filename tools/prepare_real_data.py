#!/usr/bin/env python3
"""Build the real workshop datasets from Vahedi-lab DESeq2 outputs.

Two exercises use REAL bulk data (mouse, mm10). This script records exactly
how the repo copies were derived from the lab's DESeq2 result tables, so the
provenance is reproducible. It changes as little as possible: columns are
renamed only where the source header was unusable (an unnamed row-index
column, 60-character sample names), and no rows are added, removed, or
edited. See track-a/data/README.md for what each file contains.

Usage (paths default to the lab's locations on alvand):

    python3 tools/prepare_real_data.py [K27ac_results.csv] [CTCFBSKO_vs_WT_Naive.tsv]
"""

import sys
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent.parent / "track-a" / "data"
OUT.mkdir(parents=True, exist_ok=True)

PEAKS_SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
    "/mnt/alvand/golnaz/projects/TCF1_3D/DESeq/K27ac/DESeq_Union_K27ac_results.csv")
GENES_SRC = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(
    "/mnt/alvand/golnaz/projects/Ets1_R01/DESeq/Result/DESeq2_CTCFBSKO_vs_WT_FobB_Naive.tsv")

# ------------------------------------------------ differential peaks -------
# H3K27ac ChIP-seq, DN3 thymocyte line, TCF-1 knockout (KO) vs empty vector
# (EV), 2 replicates each. DESeq2 on a union peak set; design ~ Genotype with
# EV as the reference level, so log2FoldChange is KO relative to EV.
peaks = pd.read_csv(PEAKS_SRC)
peaks = peaks.rename(columns={peaks.columns[0]: "peak_id"})  # R row index of the union peak set
peaks.to_csv(OUT / "differential_peaks.csv", index=False)

# --------------------------------------------- differential genes ---------
# Bulk RNA-seq, splenic naive follicular B cells, CTCF-binding-site knockout
# (CTCFBSKO) vs wild type (WT), 2 replicates each. STAR gene counts, DESeq2.
# NOTE the direction: checked against the raw counts, log2FoldChange is WT
# relative to CTCFBSKO (positive = higher in WT, i.e. lower in the knockout).
# Raw counts for the four libraries are the four columns after Gene_ID.
genes = pd.read_csv(GENES_SRC, sep="\t")
short = {}
for c in genes.columns[1:5]:
    # RNAseq_Spleen_FoBcells_Naive_CTCFBSKO4_273473201_S15 -> CTCFBSKO_rep4
    tag = c.split("_Naive_")[1].split("_")[0]          # CTCFBSKO4 / WT4
    group, rep = tag.rstrip("0123456789"), tag[len(tag.rstrip("0123456789")):]
    short[c] = f"{group}_rep{rep}"
genes = genes.rename(columns=short)
genes.to_csv(OUT / "differential_genes.tsv", sep="\t", index=False)

# Plain counts matrix for the plot-by-conversation card (same numbers).
counts = genes[["Gene_ID", "gene_symbol", "gene_type", *short.values()]]
counts.to_csv(OUT / "counts_matrix.csv", index=False)

print("Wrote:")
for p in ("differential_peaks.csv", "differential_genes.tsv", "counts_matrix.csv"):
    df = pd.read_csv(OUT / p, sep="\t" if p.endswith(".tsv") else ",")
    print(f"  {p}: {df.shape[0]} rows x {df.shape[1]} cols")
