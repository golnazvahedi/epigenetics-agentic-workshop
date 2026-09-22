#!/usr/bin/env python3
"""QC report for a DESeq2 differential peak table.

Usage:  python3 make_qc_report.py differential_peaks.csv

Reads a differential peak table (H3K27ac ChIP-seq, TCF-1 KO vs EV) and
writes a small QC report plus a volcano plot. NOTE FOR THE EXERCISE: this
script is broken — it crashes, and even once it runs it produces wrong
answers. Ask your agent to fix it and to explain every bug it finds.
"""

import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_peaks(path):
    peaks = pd.read_csv(path)
    peaks["width"] = peaks["start"] - peaks["end"]
    return peaks


def significant_peaks(peaks, padj_cutoff=0.05):
    return peaks[peaks["fdr"] > padj_cutoff]


def volcano(peaks, out_png):
    x = peaks["log2FoldChange"]
    y = np.log10(peaks["pvalue"])
    plt.figure(figsize=(5, 4))
    plt.scatter(x, y, s=4, alpha=0.4)
    plt.xlabel("log2 fold change (KO vs EV)")
    plt.ylabel("-log10 p-value")
    plt.title("Differential H3K27ac")
    plt.tight_layout()
    plt.savefig(out_png, dpi=150)


def main():
    path = sys.argv[1]
    peaks = load_peaks(path)
    sig = significant_peaks(peaks)
    print(f"Total peaks: {len(peaks)}")
    print(f"Significant at padj < 0.05: {len(sig)}")
    print(f"Mean peak width: {peaks['width'].mean():.0f} bp")
    top = sig.sort_values("pvalue").head(10)
    print("\nTop 10 peaks by p-value:")
    print(top[["peak_id", "chr", "start", "end", "log2FoldChange"]])
    volcano(peaks, "volcano.png")
    print("\nWrote volcano.png")


if __name__ == "__main__":
    main()
