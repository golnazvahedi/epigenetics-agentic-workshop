# Pod 3 — Reproduce a Published Figure

*Morning topic: agents doing real, multi-step analysis (with sub-agents)*

**The idea:** the most honest stress test of agentic analysis — start from a
published open-access figure and its GEO accession, and direct an agent end
to end (fetch → process → analyze → plot) until your figure matches theirs.
Where it diverges is where the discussion gets good: genome builds, package
versions, silent parameter defaults, undocumented filtering.

## Deliverable

Your figure next to the published one, plus an honest list of every place
you had to make a decision the paper didn't specify.

## Steps

1. **Pick the target.** Constraints that keep this achievable in ~3 hours:
   - Open access paper, data on GEO **with processed files** (counts
     matrices, peak calls) — do *not* start from raw FASTQs today.
   - A figure computable from one processed file: a PCA, a volcano, a
     heatmap, a TSS enrichment profile. Not a genome-browser screenshot.

   TAs will have 1–2 pre-vetted picks ready (paper + accession + which
   figure panel). If choosing your own, spend ≤15 minutes deciding.
2. **Brief the agent like a collaborator:** give it the accession, the
   figure panel (describe it or paste the image), and the constraint list
   above. Ask for a plan before it starts.
3. **Let it run — but keep the checkpoint habit:** after download, after
   loading, after the stats, ask it to show intermediate numbers (how many
   samples? how many features survived filtering?) and compare against the
   paper's reported numbers before plotting.
4. **Split with sub-agents** where natural: one fetches and inventories the
   GEO supplementary files while another drafts the analysis against the
   expected file shape.

## Demo (4 min)

Side-by-side figures, then your decision list: "the paper never said ___,
we guessed ___, and it changed the figure like this."

## Where agents go confidently wrong here

It will produce *a* beautiful figure long before it produces *the* figure —
and will describe near-matches as matches. Quantify the comparison where you
can (same n? same axis ranges? same top genes?) instead of eyeballing.
