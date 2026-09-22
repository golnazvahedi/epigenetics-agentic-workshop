#!/usr/bin/env python3
"""Generate the one SIMULATED workshop dataset: the messy sample sheet.

The differential peak table, the RNA-seq counts matrix and the DESeq2 gene
table are REAL lab data and are built by tools/prepare_real_data.py. Only
the sample sheet used by Card 2 is invented — its defects (junk header rows,
inconsistent names and dates, a duplicated row) are planted on purpose for
the exercise. Run from the repo root:

    python3 tools/generate_data.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "track-a" / "data"
OUT.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------- messy sample sheet ------
messy = """Vahedi Lab -- RNA-seq submission,,,,,
Prepared by J.D.,,,last edited Fall,,
,,,,,
sample,Condition ,harvest date,Sorted Population,replicate,notes
TCONV_1,conventional,03/02/2026,CD4+ CD25-,1,
tconv-2,Conventional,2026-03-02,CD4+CD25-,2,
Tconv_rep3,conv,3/2/26,CD4+ CD25neg,3,low yield
TCONV_4,conventional,03/09/2026,CD4+ CD25-,4,
tconv 5,Conventional,March 9 2026,CD4+CD25-,5,
Tconv_6,conv.,3/9/2026,CD4+ CD25-,6,repeat of #5??
TREG_1,regulatory,03/02/2026,CD4+ CD25hi,1,
treg-2,Regulatory,2026-03-02,CD4+CD25hi,2,
Treg_rep3,reg,3/2/26,CD4+ CD25 high,3,
TREG_4,regulatory,03/09/2026,CD4+ CD25hi,4,  RIN 6.8
treg 5,Regulatory,March 9 2026,CD4+CD25hi,5,
TREG_1,regulatory,03/02/2026,CD4+ CD25hi,1,duplicate row?
"""
(OUT / "sample_sheet_messy.csv").write_text(messy)

print("Wrote:", *[p.name for p in sorted(OUT.glob('*'))], sep="\n  ")
