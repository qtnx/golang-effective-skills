# Architecture

The repository uses progressive disclosure.

## Layers

1. `skills/*/SKILL.md`: compact task workflow loaded when a skill triggers.
2. `skills/*/references/*.md`: checklists, examples, and source maps loaded
   by each skill's Load Protocol.
3. `agents/*.md`: reusable role profiles that orchestrate skills for
   implementation or review subagents.
4. `sources/index/chunks.sqlite`: local chunk retrieval DB with token counts,
   metadata, terms, and deterministic hashed embeddings.
5. `sources/chunks/*.md`: generated source chunks used for grounding,
   conflict resolution, and source-backed updates.
6. `sources/raw/*`: downloaded upstream documents and linked-doc cache kept for
   provenance and regeneration.

## Routing

`golang-effective` is the entry point for broad Go work. It selects one primary
skill and at most two adjacent skills. Normal coding and review tasks should
not load full source documents. Task skills load examples for calibration and
run `scripts/query_chunk_index.py` to retrieve source chunks that match the
issue. `source-map.md` remains a deterministic fallback and routing aid.

## Retrieval

`scripts/build_chunk_index.py` builds `sources/index/chunks.sqlite` from
`sources/chunks/*.md`. The DB stores approximate token counts and local hashed
n-gram embeddings. This keeps the repo self-contained: no API key or external
model is needed for source retrieval.

`scripts/query_chunk_index.py` accepts a natural-language query and optional
`--skill` bias, then returns ranked chunk paths, token counts, scores, source
URLs, and snippets. Agents should open only the returned chunks that fit the
task context budget.

## Source Priority

1. User request and repository-specific style.
2. Go compiler, formatter, tests, vet, race detector, and project tooling.
3. Go language spec and current Go docs.
4. Effective Go as baseline idiom.
5. Google Go Style Guide decisions.
6. Uber Go Style Guide for application/service conventions.
7. Local consistency in the touched package.
