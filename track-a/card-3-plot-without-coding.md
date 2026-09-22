# Card 3 — Plot Without Coding

**Task:** do a first-pass expression analysis without writing a line of code
yourself.

**Data:** [`data/counts_matrix.csv`](data/counts_matrix.csv) — a simulated
RNA-seq counts matrix (800 genes × 12 samples: `Tconv_rep1–6`,
`Treg_rep1–6`).

**Do this:**

1. Ask:
   > Using `track-a/data/counts_matrix.csv`, run a PCA of the samples
   > (normalize the counts sensibly first) and plot PC1 vs PC2 colored by
   > condition. Do the conditions separate?
2. Then iterate **by conversation**, the way you'd direct a student:
   > Now show me a heatmap of the top 50 most variable genes, samples
   > clustered, with a condition color bar.
3. Don't like the figure? Say so in plain English — "make the labels
   readable", "use a diverging colormap", "drop the gene names". Iterating
   on a figure by talking is half the value of these tools.
4. **Verify:** ask the agent *what normalization it chose and why*, and
   whether any sample looks like an outlier. Make it justify itself.

**Success looks like:** a PCA plot where you can explain what you're looking
at, and a heatmap you've iterated on at least twice.

**Stretch goal:**
> Which genes drive the separation between Treg and Tconv? Give me a ranked
> table, and tell me which of them are known T cell regulators.

(The simulated data seeds real immune gene names — see if it finds `Foxp3`,
`Il2ra`, `Ctla4`... and remember: this dataset is simulated, so any *biology*
the agent narrates about it is decoration. Real data goes in, real caution
comes out.)
