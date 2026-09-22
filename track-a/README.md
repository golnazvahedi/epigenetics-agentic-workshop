# Track A — Zero to Agent

For attendees who have **never used an agentic AI tool**. By the end of the
afternoon you will have personally directed an agent through real tasks —
reading a paper, cleaning a table, plotting data, drafting text, fixing
code — and picked up the verify-before-trust habit.

## How the afternoon runs

| Time | What happens |
|---|---|
| 0:00–0:15 | **Launch check** — open your agent, run one throwaway prompt. TAs triage; if unfixable in 5 min, pair with a neighbor. |
| 0:15–0:45 | **Guided exercise** (below) — everyone does the same thing, projected at the front. |
| 0:45–1:45 | **Exercise cards** — pick any card, any order, at your own pace. TAs are roving. |
| 1:45–2:00 | Break (joint with Track B). |
| 2:00–2:40 | **Bring your own drudgery** — pick one real, *safe* task from your own work and try it. Ask a TA to help you scope it small. |
| 2:40–3:00 | **Share-out** — volunteers show one thing that worked or failed instructively. Failures are gold. |

## The guided exercise

Open your agent in this repo's folder and ask, in your own words:

> Explore `track-a/data/differential_peaks.csv`. Tell me what's in it, flag
> anything suspicious about the data, then make a volcano plot and a ranked
> table of the top 20 differential peaks by FDR.

Watch what happens — the agent inspects the file, writes and runs code, hits
problems, fixes them, and produces figures. Three things to notice:

1. **You described the goal, not the steps.** No copy-pasting code back and
   forth — that's the difference between a chatbot and an agent.
2. **The loop:** plan → act → check → adjust. You can interrupt it at any
   point.
3. **Interrogate the output.** There *are* problems planted in that file
   (impossible coordinates, missing values, a chromosome that doesn't
   exist, duplicated rows). Did the agent catch them? Ask it:
   *"How do I know this plot is right? Show me your checks."*

## The exercise cards

| Card | Exercise | You'll learn |
|---|---|---|
| 1 | [Paper wrangler](card-1-paper-wrangler.md) | Documents as input; structured extraction |
| 2 | [Sample-sheet rescue](card-2-sample-sheet-rescue.md) | Cleaning messy data; the change-log habit |
| 3 | [Plot without coding](card-3-plot-without-coding.md) | Real analysis by conversation |
| 4 | [Writing assistant](card-4-writing-assistant.md) | Agents on scientific text |
| 5 | [Debug my script](card-5-debug-my-script.md) | Agents reading and fixing code |

## Habits to take home

- Start small; slice big tasks.
- Give the agent **files**, not descriptions of files.
- Always ask the agent to show its verification.
- Never paste in what you can't afford to leak.
- Treat the agent as a tireless junior colleague — not an oracle.
