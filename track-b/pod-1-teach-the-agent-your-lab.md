# Pod 1 — Teach the Agent Your Lab

*Morning topic: skills & CLAUDE.md (context engineering)*

**The idea:** an agent is generic until you give it your lab's context. A
`CLAUDE.md` (or the equivalent context file in your tool) is where a lab
writes down its definitions and conventions once — genome build, what
"promoter" means, what counts as differential — so every member's agent
answers with the *lab's* definitions instead of its own guesses. This pod
demonstrates that with one deceptively simple question, asked twice.

**Data:** [`../track-a/data/differential_peaks.csv`](../track-a/data/differential_peaks.csv)
— the real DESeq2 table of differential H3K27ac peaks. Note what it does
*not* contain: no gene annotation, no genome build, no stated thresholds.

## Act 1 — no CLAUDE.md, no skills: watch the answers diverge

Everyone in the pod opens a **fresh session** (no context files anywhere)
and asks the identical question:

> Using track-a/data/differential_peaks.csv, tell me the percentage of
> differential peaks at promoters versus enhancers.

Let each agent run to completion, then compare screens. To answer at all,
each agent had to silently decide:

- **Which genome build** to annotate against (the file doesn't say; the
  chromosome names have no `chr` prefix — did it even notice?);
- **What "differential" means** — padj < 0.05? padj < 0.05 *and*
  |log2FC| > 1? all 49,781 peaks?;
- **What a "promoter" is** — ±1 kb of a TSS? ±2 kb? 2 kb up / 500 bp down?
  Which annotation source?;
- **What an "enhancer" is** — everything else? distal + a chromatin mark it
  doesn't have?

Four hidden decisions, each defensible, all unstated. The pod will get
genuinely different percentages — sometimes wildly different — every one
delivered with confidence. Write the numbers on a whiteboard next to each
other. **Save the spread for the demo; it's the whole argument.**

## Act 2 — the lab's CLAUDE.md: same question, one answer

Now drop in the lab's context file —
[`pod-1-lab-context/CLAUDE.md`](pod-1-lab-context/CLAUDE.md), provided in
this repo — which pins the definitions:

- Mouse, **mm10** (GRCm38); chromosome names are Ensembl-style, no `chr`
  prefix.
- **Differential** = padj < 0.05.
- **Promoter** = within **±5 kb** of an annotated TSS (Ensembl GRCm38).
- **Enhancer** = any peak that is not a promoter peak.
- `log2FoldChange` is KO relative to EV control; report gained and lost
  peaks separately.

Copy it into the working folder (in Claude Code, a `CLAUDE.md` in the
project root is loaded automatically; other tools have an equivalent),
open fresh sessions, and ask **the exact same question again.**

Every screen now shows the same analysis: mm10 annotation, ±5 kb promoter
windows, one DE definition, gained and lost reported separately. Nobody
retyped the rules and nobody will forget them next month — that's the
point. One person wrote the lab's definitions once; every member's agent
now answers like a member of *this* lab.

**Then push on it.** Ask a follow-up that isn't covered — "what fraction of
the enhancer peaks are intergenic?" — and watch the agent fall back to
guessing again. The lesson cuts both ways: the context file is load-bearing
exactly where it's explicit, and silent everywhere it isn't. Add the
missing definition, re-ask, and see it hold.

## Demo

The whiteboard of Act 1's scattered percentages next to Act 2's single
reproducible answer, then the CLAUDE.md itself on screen: half a page of
plain English. Close with the question for the room — *what are the five
definitions your own lab would put in this file?*

## Stretch goal — from lab file to personal layer

Promote the promoter/enhancer classification into a reusable **skill**
("annotate a peak table the lab's way") so it can be invoked on any future
peak file, not just this one. Then let each pod member add a personal
layer on top of the lab file — *their* project, *their* comparison of
interest, *their* figure preferences — and confirm the same one-line
question now also respects the personal context. Lab conventions + member
context, composing.

## Where agents go confidently wrong here

Act 1 *is* the failure mode: not a crash, but a confident answer built on
four invisible assumptions. The subtler trap is a stale context file — a
CLAUDE.md that still says mm10 after the lab moves to mm39 turns every
analysis quietly wrong. Treat the file like a bench protocol: an owner, a
version, a review date.
