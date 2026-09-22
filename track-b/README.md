# Track B — Level Up

For attendees who have **already used a coding agent** and want to leave with
something genuinely *agentic* working: a context layer for their own repo, an
MCP connection, a sub-agent pattern, or an end-to-end analysis reproduction.
Each challenge maps to a topic from the morning lectures.

## How it works

1. **Pick a challenge and form a pod** (3–5 people). Each pod writes one
   sentence before starting: *"By the demo, we will show ___."*
2. **Build.** TAs rotate between pods. At some point a TA will interrupt the
   room for two minutes to show a power move worth stealing (plan mode
   before a big change; spawning parallel sub-agents).
3. **Demo.** Every pod shows: what they built, one thing the agent nailed,
   and one thing it got confidently wrong. House rule: *a small thing that
   runs beats a big thing that almost runs.*

## The challenges

Every challenge has a ready-to-use sample, so no pod stalls hunting for
materials — bring-your-own project is encouraged, the sample is the floor.

| Pod | Challenge | Sample included | Morning topic |
|---|---|---|---|
| 1 | [Teach the agent your lab](pod-1-teach-the-agent-your-lab.md) | Real H3K27ac peak table + a ready-made lab `CLAUDE.md` (mm10, ±5 kb promoters) | Skills & CLAUDE.md |
| 2 | [Connect to the outside world](pod-2-mcp-connections.md) | Keyless REST endpoints (Ensembl, NCBI E-utilities) + a benchmark query | MCP |
| 3 | [Reproduce a published figure](pod-3-reproduce-a-figure.md) | Pre-vetted target: Calderon et al. 2019, GEO GSE118189 processed counts | Agents on real analysis |
| 4 | [Automate something recurring](pod-4-automation.md) | `track-a/data/make_qc_report.py` + a preprint-scan spec | Sub-agents & automation |

## Ground rules

- Same privacy rule as everywhere: no PHI, no unpublished data, no grant
  drafts. Public repos and simulated/public data only.
- Scope ruthlessly — cut features, not the demo.
- Keep a "confidently wrong" log as you go; the best moment of every demo
  is the failure you caught.
