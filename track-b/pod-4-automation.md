# Pod 4 — Automate Something Recurring

*Morning topic: sub-agents, pipelines, and standing automation*

**The idea:** the compounding wins come from things that run *again*: tests
that guard a script, a review pass that runs on every change, a literature
scan that runs every week. Build one small standing automation and prove it
holds up by running it twice.

## Deliverable

One automation, run twice in the demo (or once live + once in a log),
plus the moment it caught something.

## Pick one

**Option A — Tests for a script that has none.** Take a real analysis script
from someone's repo (fallback:
[`track-a/data/make_qc_report.py`](../track-a/data/make_qc_report.py) — it
ships deliberately broken with four planted bugs, so have the agent fix it
first and explain each bug; that warm-up is part of the exercise).
Suggested prompt:

> track-a/data/make_qc_report.py is broken — it crashes on
> differential_peaks.csv and has silent logic errors beyond the crash. Fix
> it and explain every bug. Then write a small test suite of sanity checks
> a careful postdoc would do by eye — peak widths must be positive, padj in
> [0,1], the significance filter points the right way, the volcano plot
> file actually gets written — and prove the tests work by showing them
> fail on the original broken version.

Then have it *break the script on purpose* a different way and show the
tests catching it.

**Option B — The paranoid-postdoc review agent.** Define a reusable review
persona/sub-agent with your lab's checklist. Suggested prompt:

> Create a reusable "paranoid postdoc" code reviewer I can run on any
> analysis script in this repo. Its checklist: 0- vs 1-based coordinate
> mistakes, genome-build assumptions, hardcoded paths, silent dropping of
> NA values, filters pointing the wrong way, and whether the code matches
> what the comments/methods claim. Set it up as a sub-agent or skill, then
> run it on track-a/data/make_qc_report.py and report findings ranked by
> how badly each one would corrupt a result.

Run it on two different scripts and compare what it catches — and what it
false-alarms on.

**Option C — The weekly preprint scan.** An agent workflow that queries
bioRxiv/PubMed for a topic, filters to genuinely new items, and writes a
short digest. Suggested prompt:

> Build me a reusable literature-scan workflow: given a topic and a date
> window, query bioRxiv and PubMed, deduplicate, drop anything we've seen
> before, and write a 5-bullet digest with links — one sentence on why each
> paper matters to an epigenetics lab. Run it now for "3D chromatin
> organization in T cells" over the last 30 days, then package it so I can
> rerun it with one command for any topic.

Run it for two different topics or two date windows to show it generalizes.
Bonus: schedule it (cron, scheduled agent runs, or your tool's native
scheduler).

## Demo

Run it. Then run it again on different input. Show the catch (Option A/B)
or the digest (Option C), and what it got confidently wrong.

## Where agents go confidently wrong here

Automation multiplies whatever it's pointed at — including a wrong
assumption. The rule to leave with: every standing automation gets a human
checkpoint (a digest you read, a test report you glance at), never a silent
loop that acts on its own conclusions.
