# Pod 3 — Reproduce a Published Figure

*Morning topic: agents doing real, multi-step analysis (with sub-agents)*

**The idea:** the most honest stress test of agentic analysis — start from a
published open-access figure and its GEO accession, and direct an agent end
to end (fetch → process → analyze → plot) until your figure matches theirs.
Where it diverges is where the discussion gets good: genome builds, package
versions, silent parameter defaults, undocumented filtering.

## Pre-vetted target (use this unless your pod has a better idea)

> Calderon D, Nguyen MLT, Mezger A, et al. *Landscape of
> stimulation-responsive chromatin across diverse human immune cells.*
> Nature Genetics (2019). DOI:
> [10.1038/s41588-019-0505-9](https://doi.org/10.1038/s41588-019-0505-9) ·
> open access at [PMC6858557](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6858557/)

- **Data:** GEO [GSE118189](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE118189)
  — human immune-cell ATAC-seq, 175 samples, 25 cell types, resting vs
  stimulated.
- **Processed file (verified, ~111 MB, no raw FASTQs needed):**

  ```bash
  curl -L -O https://ftp.ncbi.nlm.nih.gov/geo/series/GSE118nnn/GSE118189/suppl/GSE118189_ATAC_counts.txt.gz
  ```

- **Target figure:** the paper's global sample-level projection — samples
  clustering by cell type and lineage from the ATAC counts (Fig. 1 of the
  paper). Computable from the counts file alone: normalize, pick variable
  peaks, project (PCA/UMAP), color by cell type parsed from the sample
  names.

Pick your own target instead? Keep these constraints: open access; GEO has
**processed** files; the figure is computable from one file (PCA, volcano,
heatmap) — not a genome-browser screenshot. Spend at most 15 minutes
choosing.

## Steps

1. **Brief the agent like a collaborator** — give it the accession, the
   figure panel (describe it or paste the image), and the constraints, and
   demand a plan first. Suggested prompt:

   > I want to reproduce the global sample-clustering figure from Calderon
   > et al. 2019, "Landscape of stimulation-responsive chromatin across
   > diverse human immune cells" (Nature Genetics, GEO GSE118189). The
   > processed counts are in GSE118189_ATAC_counts.txt.gz in this folder —
   > use only that file, no raw data. Before writing any code, give me a
   > plan: how you'll load the matrix, normalize, select variable peaks,
   > project the samples (PCA or similar), and parse cell type and
   > stimulation state out of the sample names for coloring. Wait for my
   > OK, then execute step by step, and after each step show me the
   > numbers I should check against the paper — how many samples, how many
   > peaks, how many survived filtering — before you draw anything.

2. **Let it run — but keep the checkpoint habit:** at each step, compare
   the intermediate numbers it reports against the paper's before letting
   it plot. When your figure exists, ask:

   > Compare your figure against the published panel point by point: same
   > number of samples, same groupings, same axes? List every difference
   > and what would explain it.

3. **Split with sub-agents** where natural: one inventories the GEO files
   and parses sample metadata from the names while another drafts the
   analysis against the expected matrix shape.

## Demo

Side-by-side figures, then your decision list: "the paper never said ___,
we guessed ___, and it changed the figure like this."

## Where agents go confidently wrong here

It will produce *a* beautiful figure long before it produces *the* figure —
and will describe near-matches as matches. Quantify the comparison where you
can (same n? same axis ranges? same groupings?) instead of eyeballing.
