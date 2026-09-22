# Vahedi lab — analysis conventions (workshop copy)

These are the lab's standing definitions. Follow them in every analysis in
this project unless I explicitly override them.

## Organism and coordinates

- All data are **mouse, mm10 (GRCm38)**.
- Chromosome names are Ensembl-style with **no `chr` prefix** (`1`…`19`,
  `X`, `Y`). When using external annotation, convert naming to match before
  intersecting — never mix `chr1` and `1` silently.

## The peak table (`track-a/data/differential_peaks.csv`)

- H3K27ac ChIP-seq, DN3 thymocyte cell line. Two groups: TCF-1 knockout
  (`KO`) and empty-vector control (`EV`).
- `log2FoldChange` is **KO relative to EV**: positive = more H3K27ac in the
  knockout ("gained"), negative = less ("lost").
- **Differential (DE) peaks** = `padj < 0.05`.

## Genomic classification

- **Promoter peak:** the peak overlaps a window of **±5 kb around an
  annotated TSS** (Ensembl GRCm38 gene annotation).
- **Enhancer peak:** any peak that is **not** a promoter peak.
- When reporting promoter/enhancer composition of DE peaks, report
  **gained and lost peaks separately** as well as combined.

## Reporting

- Always state the annotation source and version used.
- Show the counts behind every percentage.
