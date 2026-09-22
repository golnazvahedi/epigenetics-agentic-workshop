#!/usr/bin/env python3
"""Generate the simulated workshop datasets.

All data produced here are SIMULATED. They are shaped like real epigenomics
outputs (differential ATAC-seq peaks, an RNA-seq counts matrix, a sample
sheet) so the exercises feel authentic, but no real experiment is behind
them. A few defects are planted on purpose — the exercises ask attendees to
find them. Run from the repo root:

    python3 tools/generate_data.py
"""

import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(20260922)
OUT = Path(__file__).resolve().parent.parent / "track-a" / "data"
OUT.mkdir(parents=True, exist_ok=True)

IMMUNE_GENES = [
    "Tcf7", "Lef1", "Ets1", "Ets2", "Runx1", "Runx3", "Gata3", "Tbx21",
    "Foxp3", "Rorc", "Bcl11b", "Ikzf1", "Ikzf2", "Ikzf3", "Batf", "Irf4",
    "Stat1", "Stat3", "Stat4", "Stat5a", "Stat5b", "Il2ra", "Il7r", "Il2rb",
    "Cd4", "Cd8a", "Cd8b1", "Cd3e", "Cd28", "Ctla4", "Pdcd1", "Lag3",
    "Ifng", "Il4", "Il17a", "Il21", "Tnf", "Ccr7", "Sell", "Klrg1",
    "Prdm1", "Bach2", "Zeb2", "Id2", "Id3", "Myb", "Myc", "Notch1",
    "Rag1", "Rag2", "Dntt", "Satb1", "Ctcf", "Smc1a", "Rad21", "Ezh2",
    "Dnmt3a", "Tet2", "Kdm6b", "Hdac3", "Ep300", "Crebbp", "Brd4", "Smarca4",
]
CHROMS = [f"chr{i}" for i in range(1, 20)] + ["chrX"]

# ---------------------------------------------------------------- peaks ----
n = 1500
chrom = rng.choice(CHROMS, n)
start = rng.integers(1_000_000, 120_000_000, n)
width = rng.integers(200, 1500, n)
end = start + width
log2fc = rng.normal(0, 1.4, n)
# make ~15% clearly differential
hits = rng.choice(n, int(n * 0.15), replace=False)
log2fc[hits] += rng.choice([-1, 1], hits.size) * rng.uniform(2, 4, hits.size)
pval = np.clip(np.exp(-np.abs(log2fc) * rng.uniform(2, 5, n)), 1e-300, 1.0)
order = np.argsort(pval)
fdr = np.empty(n)
fdr[order] = np.minimum.accumulate((pval[order] * n / np.arange(1, n + 1))[::-1])[::-1]
fdr = np.clip(fdr, 0, 1)

peaks = pd.DataFrame({
    "peak_id": [f"peak_{i:05d}" for i in range(1, n + 1)],
    "chrom": chrom,
    "start": start,
    "end": end,
    "log2FC_Treg_vs_Tconv": log2fc.round(3),
    "pvalue": pval,
    "FDR": fdr,
    "nearest_gene": rng.choice(IMMUNE_GENES, n),
    "distance_to_TSS": rng.integers(-50_000, 50_000, n),
})

# ---- planted defects (the guided exercise asks the agent to flag these) ----
bad = rng.choice(n, 8, replace=False)
peaks.loc[bad, "end"] = peaks.loc[bad, "start"] - rng.integers(100, 500, 8)  # end < start
peaks.loc[rng.choice(n, 5, replace=False), "pvalue"] = np.nan               # missing p-values
peaks.loc[rng.choice(n, 3, replace=False), "chrom"] = "chr23"               # no mouse chr23
peaks = pd.concat([peaks, peaks.sample(4, random_state=1)])                  # duplicated rows
peaks.to_csv(OUT / "differential_peaks.csv", index=False)

# ------------------------------------------------------------- counts ------
genes = [f"{g}" for g in IMMUNE_GENES] + [f"Gene{i:04d}" for i in range(1, 737)]
n_genes = len(genes)
samples = [f"{c}_rep{r}" for c in ("Tconv", "Treg") for r in range(1, 7)]
base = rng.lognormal(5, 1.5, n_genes)
counts = np.vstack([
    rng.negative_binomial(20, 20 / (20 + base * (1 + rng.normal(0, 0.05, n_genes))))
    for _ in samples
]).T.astype(float)
# differential structure so PCA separates conditions
de = rng.choice(n_genes, 120, replace=False)
effect = 2.0 ** (rng.choice([-1, 1], de.size) * rng.uniform(1, 3, de.size))
counts[np.ix_(de, range(6, 12))] = (counts[np.ix_(de, range(6, 12))].T * effect).T
counts = np.round(counts).astype(int)
pd.DataFrame(counts, index=pd.Index(genes, name="gene"), columns=samples) \
    .to_csv(OUT / "counts_matrix.csv")

# ------------------------------------------------- messy sample sheet ------
messy = """Vahedi Lab -- RNA-seq submission,,,,,
Prepared by J.D.,,,last edited Fall,,
,,,,,
sample,Condition ,harvest date,Sorted Population,replicate,notes
TCONV_1,conventional,03/02/2026,CD4+ CD25-,1,
tconv-2,Conventional,2026-03-02,CD4+CD25-,2,
Tconv_rep3,conv,3/2/26,CD4+ CD25neg,3,low yield
TCONV_4,conventional,03/09/2026,CD4+ CD25-,4,
tconv 5,Conventional,March 9 2026,CD4+CD25-,5,
Tconv_6,conv.,3/9/2026,CD4+ CD25-,6,repeat of #5??
TREG_1,regulatory,03/02/2026,CD4+ CD25hi,1,
treg-2,Regulatory,2026-03-02,CD4+CD25hi,2,
Treg_rep3,reg,3/2/26,CD4+ CD25 high,3,
TREG_4,regulatory,03/09/2026,CD4+ CD25hi,4,  RIN 6.8
treg 5,Regulatory,March 9 2026,CD4+CD25hi,5,
TREG_1,regulatory,03/02/2026,CD4+ CD25hi,1,duplicate row?
"""
(OUT / "sample_sheet_messy.csv").write_text(messy)

print("Wrote:", *[p.name for p in sorted(OUT.glob('*'))], sep="\n  ")
