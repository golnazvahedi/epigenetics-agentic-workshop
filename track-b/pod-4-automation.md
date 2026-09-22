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
from someone's repo (fallback: the fixed version of
[`track-a/data/make_qc_report.py`](../track-a/data/make_qc_report.py)). Ask
the agent to write sanity tests — the assertions a careful postdoc checks by
eye: no negative peak widths, FDR in [0,1], sample count matches the sheet,
figures actually get written. Then have it *break the script on purpose* and
show the tests catching it.

**Option B — The paranoid-postdoc review agent.** Define a reusable review
persona/sub-agent with your lab's checklist (off-by-one genome coordinates?
0- vs 1-based? hardcoded paths? does the code match the methods section?).
Run it on two different scripts and compare what it catches — and what it
false-alarms on.

**Option C — The weekly preprint scan.** An agent workflow that queries
bioRxiv/PubMed for a topic (e.g., "3D chromatin organization in T cells"),
filters to genuinely new items, and writes a 5-bullet digest with links.
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
