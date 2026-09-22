# Card 2 — Sample-Sheet Rescue

**Task:** clean a spreadsheet the way they actually arrive in real labs.

**Data:** [`data/sample_sheet_messy.csv`](data/sample_sheet_messy.csv) — a
simulated RNA-seq submission sheet with junk header rows, inconsistent
sample names, three different date formats, inconsistent condition labels,
and at least one duplicate row.

**Do this:**

1. Ask the agent:
   > Clean up `track-a/data/sample_sheet_messy.csv`: standardize the sample
   > names to one convention, normalize the dates to ISO format, make the
   > condition labels consistent, and flag anything that looks like a
   > duplicate or an error. Save the tidy version as a new file — do NOT
   > overwrite the original — and give me a list of every change you made.
2. Read the change log it gives you. This is the key habit: **never accept
   a silent cleanup.** If it didn't give you one, demand it.
3. **Verify:** how did it handle `Tconv_6` ("repeat of #5??") and the
   duplicated `TREG_1` row? These are judgment calls — a good agent flags
   them for *you* to decide rather than silently deleting data.

**Success looks like:** a tidy CSV, the original untouched, and a change log
you've actually read.

**Stretch goal:** ask the agent to write a small reusable script that would
apply the same cleanup rules to next month's sheet — your first taste of
turning a one-off fix into lab infrastructure.
