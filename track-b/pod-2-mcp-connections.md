# Pod 2 — Connect to the Outside World (MCP)

*Morning topic: Model Context Protocol*

**The idea:** out of the box, an agent can only touch your filesystem and
whatever it can install. MCP gives it *tools* — live access to PubMed, GEO,
genome annotation, your institute's services. This pod wires one up and
proves it with a query the bare agent couldn't answer.

## Deliverable

A live, reproducible query through an MCP connection. Benchmark query:

> Find human regulatory T cell ATAC-seq datasets deposited in GEO since
> 2024 and tabulate them: accession, title, sample count, platform.

(Or invent a benchmark that matters to your pod — the shape is "current,
structured, from a live database.")

## Two routes — pick by ambition

**Route 1 — use an existing server (faster, do this first).** Find and
install a community MCP server for a bio resource: PubMed/NCBI E-utilities,
GEO, UCSC, Ensembl. Configure it into your agent, run the benchmark query,
sanity-check the results against the website by hand.

**Route 2 — build a minimal server (the real learning).** Have the agent
write you a tiny MCP server (Python SDK is easiest) exposing one or two
tools around a REST API that doesn't need a key — e.g.:

- Ensembl REST (`/lookup/symbol`, `/overlap/region`) — "what genes are in
  this region?"
- ENCODE search API — "find ChIP-seq experiments for this factor."
- NCBI E-utilities — esearch/esummary against GEO DataSets.

Wire it into your agent config and run the benchmark. Yes, the agent can
write the server *and* then use it — that loop is the demo.

## Demo

The benchmark query answered live, plus your hand-check: was the table
complete and correct against the source website?

## Where agents go confidently wrong here

Retrieval ≠ truth: the agent will happily summarize whatever the API
returned, including a query that silently matched the wrong organism or
assay. The hand-check against the website *is* the lesson.
