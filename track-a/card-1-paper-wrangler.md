# Card 1 — Paper Wrangler

**Task:** turn a paper into things you can actually use.

**Sample (included in this repo):**
[`data/stripenn_paper.pdf`](data/stripenn_paper.pdf) — the Vahedi lab's
Stripenn paper, redistributed here under its CC BY 4.0 license:

> Yoon S, Chandra A, Vahedi G. *Stripenn detects architectural stripes from
> chromatin conformation data using computer vision.* Nature Communications
> (2022). DOI: [10.1038/s41467-022-29258-9](https://doi.org/10.1038/s41467-022-29258-9) ·
> [PMC8948182](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8948182/)

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
watch where it reaches.
