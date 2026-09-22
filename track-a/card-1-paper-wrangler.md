# Card 1 — Paper Wrangler

**Task:** turn a paper into things you can actually use.

**Sample (included in this repo):**
[`data/scbasecount_paper.pdf`](data/scbasecount_paper.pdf) — the Arc
Institute's scBaseCount paper, redistributed here under its CC BY 4.0
license. It is a fitting choice for an agentic-AI workshop: the resource it
describes was itself built by an AI agent that reads the Sequence Read
Archive.

> Youngblut ND, Carpenter C, Nayebnazar A, et al. *scBaseCount: An AI
> agent-curated, standardized, auto-updated single-cell data repository.*
> Cell 189, 5932–5944 (2026). DOI:
> [10.1016/j.cell.2026.08.025](https://doi.org/10.1016/j.cell.2026.08.025)

Prefer a paper from your own field? Any open-access PDF works — the steps
are identical.

**Do this:**

1. Give the agent the PDF and ask for a summary **for a specific audience**:
   > Summarize this paper in 10 bullets for a lab-meeting audience of
   > immunologists who don't do computational work.
2. Then ask for structured extraction:
   > Extract every software tool, dataset, and public data accession
   > mentioned in this paper into a CSV with columns: item, type
   > (tool/dataset/accession), and what it was used for.
   This paper is dense with exactly these: the SRAgent and scRecounter
   tools, STARsolo, Google Cloud buckets, SRA accessions, model names.
   (For a wet-lab paper, extract antibodies/reagents/kits with vendor and
   catalog number instead.)
3. **Verify:** spot-check three rows of the CSV against the actual PDF.
   Did it invent an accession or a version number? This is the classic
   failure mode — catch it once here and you'll never fully trust an
   extraction again, which is the point.

**Success looks like:** a summary you'd actually present, and an extraction
CSV you've spot-checked.

**Stretch goal:** ask the agent to compare the paper's stated method against
its figures — "which figure demonstrates each claim in the abstract?" — and
watch where it reaches. Then a harder one: *"The paper says over 502
million cells. What fraction of the target SRA datasets had actually been
reprocessed at the time of writing, and where does the paper say so?"* The
repository was still being built when the paper went to press, and a
careless summary quotes only the headline number.
