# Pod 1 — The Lab Protocol Book

*Morning topic: skills & CLAUDE.md (context engineering)*

**The idea:** every wet lab has a protocol book — the antibody dilutions,
the sort gates, the fixation times — written once, followed by everyone, so
a new student doesn't reinvent (or corrupt) the protocol. **A skill is the
computational version of a protocol.** It's a named instruction file your
agent loads when the task matches: "this is how *our lab* does a first-pass
differential analysis." Written once by one person; from then on, everyone
in the lab types one line and gets the lab-standard result.

This pod builds the protocol book in two acts — first for the lab, then for
the individual — using the real datasets in
[`../track-a/data/`](../track-a/data/).

## Act 1 — the lab-level skill (one protocol, everyone benefits)

**First, watch the failure.** In a fresh session, everyone in the pod asks:

> Analyze track-a/data/differential_genes.tsv and give me a first-pass
> report.

Compare screens. You'll get N different reports: different thresholds,
different plots, and — with this file — at least one silent error, because
nothing tells the agent that a *negative* fold change means higher in the
knockout, or that `padj` is NA for 85% of genes. Generic agent, generic
guesses. Save the worst one for the demo.

**Now write the protocol.** As a pod, build one skill — call it
`deseq2-first-pass` — that encodes how your (fictional or real) lab does
this, e.g.:

- **Verify before plotting:** confirm the fold-change direction against the
  raw counts for 3 top genes; report which group is the reference. Never
  assume.
- **Handle the traps:** state how many genes have `padj = NA` and why;
  never silently drop them with a `padj < 0.05` filter.
- **Lab conventions:** padj < 0.05 and |log2FC| > 1; colorblind-safe
  palette; PCA + volcano + top-25 table; protein-coding genes only in
  heatmaps; mouse = mm10 unless stated.
- **Standard output:** everything into `results/YYYY-MM-DD_<dataset>/`,
  plus a draft methods paragraph with `[PLACEHOLDER]` for anything the
  data can't prove.

Install it (each tool has its own mechanism — in Claude Code, a folder
under `.claude/skills/`), open fresh sessions, and ask **the same one-line
question again.** Now every screen in the pod shows the *same* lab-standard
report, direction verified, NA genes accounted for. That's the moment:
one person wrote the protocol once, and the whole lab's floor just rose.

## Act 2 — the member-level layer (same protocol, my project)

Protocols are shared; projects are personal. Each pod member now writes a
small **personal** context on top — a `CLAUDE.md` or personal skill with
their project's facts, invented or real:

> *My project: CTCF-binding-site knockout in follicular B cells. Comparison
> of interest: CTCFBSKO vs WT, WT is the reference. My genes of interest:
> Jun, Myc, Irf4, Ccr7. I always want PDFs, and figures sized for a
> two-column paper.*

(Someone else in the pod plays a different "member": the H3K27ac peaks
file is their project, TCF-1 KO vs EV, interested in T cell factors.)

Everyone asks the identical one-liner — *"run our first-pass analysis on my
data"* — and each member's agent now produces a **different, correct,
project-specific report in the same lab style**: right file, right
reference group, their genes highlighted, their format preferences. Lab
protocol + personal layer, composing.

## Demo

Three screens: (1) the ugliest no-skill report from Act 1 — ideally one
that got the fold-change direction wrong; (2) the same prompt with the lab
skill — identical, correct output on every laptop; (3) two members, same
one-line prompt, two different project-correct reports. Close by showing
the skill file itself: it's just a page of English. That's the whole trick.

## More protocols worth writing back home (steal these)

- **Genome-build guardrail:** "any coordinate operation must state the
  build; if mixing files, prove they match or stop" — the mm10/mm39 and
  hg19/hg38 disaster preventer.
- **Peak annotation, our way:** nearest-TSS rules, distance cutoffs, which
  annotation source, how to report ambiguous assignments.
- **GEO submission checklist:** validate an md5-summed, metadata-complete
  submission folder from a samples table.
- **Lab figure style:** fonts, palette, panel sizing — so every draft
  figure is journal-ready.
- **New-student onboarding:** "set up an analysis folder our way" — the
  protocol that teaches the protocol.

## Where agents go confidently wrong here

A skill is followed only as well as it's written — vague lines ("QC the
data appropriately") get vague obedience, and an over-long skill gets
selectively ignored. And protocols rot: who owns `deseq2-first-pass` when
the lab switches to mm39? Treat skills like bench protocols — an owner, a
version, a review date.
