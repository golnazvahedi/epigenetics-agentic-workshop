# Card 5 — Debug My Script

**Task:** hand the agent broken code — the thing it's best at — and watch it
read, run, and repair files rather than just chat.

**Data:** [`data/make_qc_report.py`](data/make_qc_report.py), which is
supposed to QC [`data/differential_peaks.csv`](data/differential_peaks.csv)
and draw a volcano plot. It crashes. And even after the crash is fixed, it
still produces wrong answers — there are **four planted bugs** in total (one
crash, three silent logic errors).

**Do this:**

1. First, see it fail yourself:
   ```bash
   cd track-a/data
   python3 make_qc_report.py differential_peaks.csv
   ```
2. Then hand it over:
   > `track-a/data/make_qc_report.py` crashes when I run it on
   > `differential_peaks.csv`. Fix it — but don't stop at the crash: check
   > the whole script for logic errors too. Explain every bug you find and
   > why it was wrong, then run the fixed script and show me the output.
3. **Verify:** it found the crash for sure — did it find all three silent
   bugs? (Sanity-check the output: can a peak have a *negative* width? Does
   "significant" mean FDR *above* the cutoff? Which way should a volcano
   plot point?) If it missed any, tell it what looks wrong in the output
   and let it hunt again — that's the real workflow.

**Success looks like:** a script that runs, four bugs explained, and output
you've sanity-checked against common sense.

**Stretch goal:** ask the agent to add the thing that would have caught these
bugs automatically:
> Write a few sanity checks/tests for this script so bugs like these get
> caught next time, and show me the tests failing on the original version.
