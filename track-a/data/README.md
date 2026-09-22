# Sample data

Two of the files here are **real bulk data from the Vahedi lab** (mouse,
mm10), shared for teaching. Please use them inside the workshop only and do
not redistribute them without asking. One file (the sample sheet) is
simulated. The scripts that produced every file are in [`tools/`](../../tools/).

| File | What it is | Built by |
|---|---|---|
| `differential_peaks.csv` | Real DESeq2 differential **H3K27ac ChIP-seq** peaks | `tools/prepare_real_data.py` |
| `differential_genes.tsv` | Real DESeq2 differential **RNA-seq** genes, with raw counts | `tools/prepare_real_data.py` |
| `counts_matrix.csv` | The raw counts from `differential_genes.tsv`, nothing else | `tools/prepare_real_data.py` |
| `sample_sheet_messy.csv` | Simulated messy RNA-seq submission sheet (Card 2) | `tools/generate_data.py` |
| `make_qc_report.py` | Deliberately broken QC script (Track B, Pod 4) | hand-written |
| `scbasecount_paper.pdf` | Open-access paper, Youngblut et al. Cell 2026, CC BY 4.0 (Card 1) | — |

## `differential_peaks.csv` — H3K27ac, TCF-1 knockout vs control

- **Experiment:** H3K27ac ChIP-seq in a DN3 thymocyte cell line. Two groups,
  two replicates each: TCF-1 knockout (`KO`) and empty-vector control (`EV`).
  Part of the revision of the lab's TCF-1 3D genome paper.
- **Analysis:** reads counted on a union peak set (49,781 regions), DESeq2
  with `design = ~ Genotype`, `EV` as the reference level.
- **Direction:** `log2FoldChange` is **KO relative to EV**. Positive means
  more H3K27ac in the knockout. Verified against the per-sample normalized
  counts, not just the code.
- **Columns:** `peak_id` (row index of the union peak set), `chr`, `start`,
  `end`, then standard DESeq2 output: `baseMean`, `log2FoldChange`, `lfcSE`,
  `stat`, `pvalue`, `padj`.
- **Headline numbers:** 15,653 peaks at padj < 0.05. At padj < 0.05 and
  |log2FC| > 1: 2,202 gained and 3,056 lost in the knockout.
- **Real-world quirks worth noticing** (nothing was planted, this is how the
  file came out of the pipeline):
  - chromosome names have **no `chr` prefix** (`12`, `X`, `Y`);
  - four peaks have `pvalue` and `padj` of **exactly 0** (floating-point
    underflow), so `-log10` gives infinity;
  - peak widths range from 180 bp to **93,567 bp**, because union peaks merge
    neighbouring regions;
  - there is **no gene annotation** column;
  - **no `padj` values are missing**, which is unusual for DESeq2 output and
    means the table was filtered before it was saved;
  - the fold-change direction is not stated anywhere in the file.

## `differential_genes.tsv` and `counts_matrix.csv` — B-cell RNA-seq

- **Experiment:** bulk RNA-seq of naive follicular B cells sorted from
  mouse spleen. Two groups, two replicates each: a CTCF-binding-site
  knockout (`CTCFBSKO`) and wild type (`WT`). Libraries are shallow, about
  3.5 to 4.4 million assigned reads each.
- **Analysis:** STAR gene counts (Ensembl GRCm38), DESeq2 with
  `design = ~ condition`. Genes with zero counts in all samples were removed
  before testing.
- **Direction:** `log2FoldChange` is **WT relative to CTCFBSKO**. Positive
  means higher in wild type, so *lower* in the knockout. Check it yourself:
  `Jun` has counts 3465 and 4023 in the knockout versus 1718 and 2237 in
  wild type, and its fold change is −1.13.
- **Columns:** `Gene_ID` (Ensembl), raw counts `CTCFBSKO_rep4`,
  `CTCFBSKO_rep5`, `WT_rep4`, `WT_rep5`, standard DESeq2 output, then
  `gene_symbol` and `gene_type`. Sample names were shortened from the
  sequencing-core names; the numbers are untouched.
- **Headline numbers:** 24,596 genes; 3,614 passed DESeq2's independent
  filtering; 60 at padj < 0.05. Top hits: Jun, Plk2, Myc, Cd83, Irf4, Irs2,
  Ccr7, Nr4a1.
- **Real-world quirks worth noticing:**
  - `padj` is **NA for 20,982 genes** (independent filtering of low-count
    genes), so a naive `padj < 0.05` filter silently drops them;
  - 16 gene symbols are **duplicated** across different Ensembl IDs;
  - only **two replicates per group**, so any PCA or outlier judgement is
    on thin ice;
  - a third of the genes are pseudogenes, lincRNAs and other non-coding
    biotypes, which is a reasonable thing to filter before a heatmap.
