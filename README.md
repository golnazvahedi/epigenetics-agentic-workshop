# Agentic AI Workshop — Penn Epigenetics Institute

Hands-on materials for the afternoon of the agentic AI workshop (instructor:
Sean Davis; morning lectures cover an introduction to agents, then skills,
MCP, and sub-agents). The afternoon splits into two tracks — pick yours:

| Track | Who it's for | Start here |
|---|---|---|
| **[Track A — Getting Started](track-a/)** | You're new to agentic AI: one guided exercise, then self-paced exercise cards | [track-a/README.md](track-a/README.md) |
| **[Track B — Level Up](track-b/)** | You've used a coding agent and want skills, MCP, sub-agents, and real analysis | [track-b/README.md](track-b/README.md) |

Every exercise and challenge ships with its own sample materials — two
real bulk datasets from the Vahedi lab (differential H3K27ac peaks and
B-cell RNA-seq, both mouse), a simulated sample sheet, a bundled
open-access paper, or a verified public data target — so nobody needs
their own data to participate.

## Setup (do this BEFORE the workshop)

1. **Install a coding agent and confirm it responds.** Recommended:
   [Claude Code](https://claude.com/claude-code) — the desktop app is the
   gentlest on-ramp; the CLI works too. Alternatives: Gemini CLI, GitHub
   Copilot agent mode, Codex.
2. **Bring a laptop and charger.** Track B: also have `git` installed and,
   ideally, one of your own projects cloned locally.
3. **Get this repo:**

   ```bash
   git clone https://github.com/golnazvahedi/epigenetics-agentic-workshop.git
   ```

   (Or download the ZIP from the green **Code** button.)

If your setup isn't working, come to the **lunch setup clinic** — TAs will
get you running before the afternoon starts.

## Ground rules

- **Privacy:** do not paste PHI, your own unpublished data, or grant drafts
  into any AI tool during the workshop. The exercises use **real mouse
  datasets shared by the Vahedi lab for this purpose** plus one simulated
  sample sheet (see [`track-a/data/README.md`](track-a/data/README.md) for
  what each file is and where it came from) — you never need your own.
- **Verify:** the recurring habit of the day. Whenever an agent produces a
  result, ask it *"how do I know this is right?"* and make it show its work.
- **Pair up:** if your setup dies, share a laptop. Pairing is a feature.

## What's here

```
track-a/            Beginner track: 5 exercise cards + guided exercise
track-a/data/       Real DESeq2 tables (H3K27ac peaks, B-cell RNA-seq) + one simulated sample sheet
track-b/            Experienced track: 4 pod challenge briefs
tools/              Scripts that built the datasets (prepare_real_data.py, generate_data.py)
```

## After the workshop

Drop your best prompt, CLAUDE.md, or skill into a pull request against
`community/` — the goal is that this repo leaves the institute a starter
kit, not just a memory. Office hours with the TAs will be announced ~2–3
weeks after the workshop.
