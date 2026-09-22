# Card 1 — Paper Wrangler

**Task:** turn a paper into things you can actually use.

**Data:** any open-access paper PDF you like. Suggestions (download the PDF
first, then give the agent the file):

- Any recent open-access paper from your own field — PubMed Central PDFs
  work well.
- If you're stuck, pick one from the [Vahedi lab publication list](https://pubmed.ncbi.nlm.nih.gov/?term=vahedi+golnaz&sort=pubdate).

**Do this:**

1. Give the agent the PDF and ask for a summary **for a specific audience**:
   > Summarize this paper in 10 bullets for a lab-meeting audience of
   > immunologists who don't do computational work.
2. Then ask for structured extraction:
   > Extract every antibody, reagent, cell line, and kit mentioned in the
   > methods into a CSV with columns: item, vendor, catalog number (if
   > given), and what it was used for.
3. **Verify:** spot-check three rows of the CSV against the actual PDF.
   Did it invent a catalog number? (This is the classic failure mode —
   catch it once here and you'll never fully trust an extraction again,
   which is the point.)

**Success looks like:** a summary you'd actually present, and a reagent CSV
you've spot-checked.

**Stretch goal:** give it the paper's supplement too and ask it to
cross-reference — "which figures use which datasets, and where are the
data deposited?"
