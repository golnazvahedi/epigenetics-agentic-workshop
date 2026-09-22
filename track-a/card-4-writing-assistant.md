# Card 4 — Writing Assistant

**Task:** use an agent on scientific text — with the source-of-truth caveat
front and center.

**Sample (included in this repo):**
[`data/differential_peaks.csv`](data/differential_peaks.csv), a real DESeq2
table of differential H3K27ac ChIP-seq peaks (TCF-1 knockout vs empty-vector
control, DN3 thymocytes; see [`data/README.md`](data/README.md)). If you
haven't done the guided exercise yet, start with: *"Analyze
track-a/data/differential_peaks.csv: count the peaks at padj < 0.05 and
|log2FC| > 1, split by direction, and make a volcano plot"* — that gives you
an analysis to write about. Any safe text of your own (a talk outline,
bullet notes) works too.

**Do this:**

1. Methods paragraph, grounded in what actually happened:
   > Draft a methods paragraph describing the differential analysis you just
   > performed on differential_peaks.csv — only describe steps you actually
   > ran, and mark any place where you'd need information from me (genome
   > build, peak caller, how the union peak set was made, which group is the
   > reference, thresholds) with [PLACEHOLDER].
   The `[PLACEHOLDER]` instruction is the trick worth stealing: it converts
   the model's urge to fill gaps with plausible fiction into explicit
   questions for you. This file is a good test — it does *not* say which
   way the fold change points, so a truthful draft has to leave that blank.
2. Figure legend from bullets:
   > Turn these bullets into a figure legend: volcano plot; H3K27ac ChIP-seq,
   > TCF-1 KO vs EV in DN3 cells; red = padj < 0.05 and |log2FC| > 1;
   > n = 2 per group.
3. Tone transform — take any paragraph you have and ask for it three ways:
   for a grant's significance section, for a departmental newsletter, for a
   tweet-length summary.

**Verify:** read the methods draft line by line. Anything it asserted that
you didn't tell it and it couldn't have observed? (Common ones here: naming
a peak caller, mislabeling the H3K27ac ChIP-seq as a different assay, stating the reference
group.) That's the failure mode to develop a reflex for — in writing tasks
the agent's errors *sound* the most confident.

**Success looks like:** a methods paragraph where every claim is either true
or a `[PLACEHOLDER]`.

**Stretch goal:** paste in a (public!) reviewer-style critique — or ask the
agent to *play* Reviewer 2 on your paragraph — then have it draft the
response letter.
