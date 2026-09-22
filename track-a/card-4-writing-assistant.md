# Card 4 — Writing Assistant

**Task:** use an agent on scientific text — with the source-of-truth caveat
front and center.

**Data:** the analysis you (or the guided exercise) just ran on
[`data/differential_peaks.csv`](data/differential_peaks.csv), or any safe
text of your own (a talk outline, a course description, bullet notes).

**Do this:**

1. Methods paragraph, grounded in what actually happened:
   > Draft a methods paragraph describing the differential accessibility
   > analysis you just performed on differential_peaks.csv — only describe
   > steps you actually ran, and mark any place where you'd need
   > information from me (genome build, peak caller, thresholds) with
   > [PLACEHOLDER].
   The `[PLACEHOLDER]` instruction is the trick worth stealing: it converts
   the model's urge to fill gaps with plausible fiction into explicit
   questions for you.
2. Figure legend from bullets:
   > Turn these bullets into a figure legend: volcano plot; Treg vs Tconv
   > ATAC; red = FDR < 0.05 and |log2FC| > 1; n = 3 per group.
3. Tone transform — take any paragraph you have and ask for it three ways:
   for a grant's significance section, for a departmental newsletter, for a
   tweet-length summary.

**Verify:** read the methods draft line by line. Anything it asserted that
you didn't tell it and it couldn't have observed? That's the failure mode to
develop a reflex for — in writing tasks the agent's errors *sound* the most
confident.

**Success looks like:** a methods paragraph where every claim is either true
or a `[PLACEHOLDER]`.

**Stretch goal:** paste in a (public!) reviewer-style critique — or ask the
agent to *play* Reviewer 2 on your paragraph — then have it draft the
response letter.
