# Pod 1 — Teach the Agent Your Lab

*Morning topic: skills & CLAUDE.md (context engineering)*

**The idea:** an agent is generic until you give it your lab's context. The
highest-leverage thing a lab can build is the context layer — because one
person writes it once and everyone's agent gets smarter. This pod builds
that layer for a real project and **measures the difference**.

## Deliverable

A repo containing a `CLAUDE.md` (or equivalent agent-context file) plus one
reusable skill, and a with-vs-without comparison you can show in the demo.

## Steps

1. **Pick a repo.** Best: someone in the pod's real analysis repo (public or
   safely shareable). Fallback: this repo — pretend `track-a/data/` is your
   lab's standard output format.
2. **Write the context file.** Capture what a new student would need to be
   told: what the project is, where data lives, naming conventions, genome
   build, which scripts are canonical vs. abandoned, coding style, what
   "done" means (e.g., "every figure script writes to `figures/` and is
   re-runnable from scratch").
3. **Build one skill.** A reusable, named procedure the agent can execute on
   demand. Good candidates:
   - "Generate our standard QC report from a differential peaks file"
     (spec: the checks to run, the plots to make, the report format).
   - "Set up a new analysis subfolder the way our lab does it."
4. **Measure it.** Run the same realistic task in a fresh session *with* and
   *without* the context layer. Save both transcripts. Where did the
   context change the outcome — fewer wrong guesses? right conventions?
   fewer questions back at you?

## Demo (4 min)

Show the task running with the context layer, then the ugliest moment from
the without-context transcript.

## Where agents go confidently wrong here

Context files rot. Ask: what happens in 6 months when the conventions
change? Discuss who owns the file — treat it like a lab protocol, with an
owner and a review date.
