# Track A — Getting Started

For attendees who are **new to agentic AI tools**. The format is simple:
one guided exercise everyone does together, then exercise cards you work
through at your own pace, in any order. TAs are roving the whole time —
wave one over whenever you're stuck. If your setup dies, pair with a
neighbor; pairing is a feature.

Every exercise comes with its own sample data in [`data/`](data/) — you
never need your own. Two of the files are real Vahedi-lab datasets;
[`data/README.md`](data/README.md) says what they are. Read it *after* the
guided exercise and see how much of it the agent worked out on its own.

## The guided exercise (done together first)

Open your agent in this repo's folder and ask, in your own words:

> Explore `track-a/data/differential_peaks.csv`. Tell me what's in it, flag
> anything suspicious about the data, then make a volcano plot and a ranked
> table of the top 20 differential peaks by adjusted p-value.

Watch what happens — the agent inspects the file, writes and runs code, hits
problems, fixes them, and produces figures. Three things to notice:

1. **You described the goal, not the steps.** No copy-pasting code back and
   forth — that's the difference between a chatbot and an agent.
2. **The loop:** plan → act → check → adjust. You can interrupt it at any
   point.
3. **Interrogate the output.** This is a real DESeq2 table straight from a
   pipeline, and it has real quirks: chromosome names with no `chr` prefix,
   four p-values that are exactly zero (what does `-log10(0)` do to a
   volcano plot?), a 93-kb "peak", no gene names, and nothing that says
   which way the fold change points. Did the agent notice? Ask it:
   *"How do I know this plot is right? Show me your checks."* and
   *"Which group has more signal when log2FoldChange is positive, and how
   do you know?"* (It can't know from this file alone — that's the point.)

## The exercise cards (any order, your pace)

| Card | Exercise | Sample included | You'll learn |
|---|---|---|---|
| 1 | [Paper wrangler](card-1-paper-wrangler.md) | Stripenn paper (open access) | Documents as input; structured extraction |
| 2 | [Sample-sheet rescue](card-2-sample-sheet-rescue.md) | `data/sample_sheet_messy.csv` | Cleaning messy data; the change-log habit |
| 3 | [Plot without coding](card-3-plot-without-coding.md) | `data/counts_matrix.csv` + `data/differential_genes.tsv` | Real analysis by conversation |
| 4 | [Writing assistant](card-4-writing-assistant.md) | `data/differential_peaks.csv` + provided bullets | Agents on scientific text |
| 5 | [Debug my script](card-5-debug-my-script.md) | `data/make_qc_report.py` (4 planted bugs) | Agents reading and fixing code |

When you've done a few cards, try the same pattern on one real, *safe* task
from your own work — a public dataset, a talk outline, a figure you never
liked. Ask a TA to help you scope it small; the classic beginner mistake is
a task too big.

## Habits to take home

- Start small; slice big tasks.
- Give the agent **files**, not descriptions of files.
- Always ask the agent to show its verification.
- Never paste in what you can't afford to leak.
- Treat the agent as a tireless junior colleague — not an oracle.
