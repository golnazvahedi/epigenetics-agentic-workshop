# Card 3 — Plot Without Coding

**Task:** do a first-pass expression analysis without writing a line of code
yourself.

**Data:** [`data/counts_matrix.csv`](data/counts_matrix.csv) — a **real**
bulk RNA-seq counts matrix from the Vahedi lab: naive follicular B cells
sorted from mouse spleen, 24,596 genes × 4 samples (`CTCFBSKO_rep4`,
`CTCFBSKO_rep5`, `WT_rep4`, `WT_rep5`; a CTCF-binding-site knockout versus
wild type). The lab's own DESeq2 result for the same samples is in
[`data/differential_genes.tsv`](data/differential_genes.tsv) — keep it
closed until the stretch goal. Details in [`data/README.md`](data/README.md).

**Do this:**

1. Ask:
   > Using `track-a/data/counts_matrix.csv`, run a PCA of the samples
   > (normalize the counts sensibly first) and plot PC1 vs PC2 colored by
   > genotype. Do the genotypes separate?
2. Then iterate **by conversation**, the way you'd direct a student:
   > Now show me a heatmap of the top 50 most variable genes, samples
   > clustered, with a genotype color bar. Protein-coding genes only.
3. Don't like the figure? Say so in plain English — "make the labels
   readable", "use a diverging colormap", "drop the gene names". Iterating
   on a figure by talking is half the value of these tools.
4. **Verify:** ask the agent *what normalization it chose and why*, and what
   it makes of having only two replicates per group. Make it justify itself.

**Success looks like:** a PCA plot where you can explain what you're looking
at, and a heatmap you've iterated on at least twice.

**Stretch goal:**
> Which genes differ most between CTCFBSKO and WT? Rank them. Then compare
> your ranking with `track-a/data/differential_genes.tsv`, the lab's DESeq2
> output for these exact samples. Do the top hits agree? Which direction
> does `log2FoldChange` point in that file — and how can you tell?

(Real data, real trap: in that file a *negative* fold change means the gene
is **higher in the knockout** — `Jun` has roughly twice the counts in
CTCFBSKO yet a log2FC of −1.13. Nothing in the file says so. Did the agent
check the direction against the raw counts, or did it assume? Also notice
that `padj` is `NA` for most genes — ask why, and what a careless
`padj < 0.05` filter does with them.)
