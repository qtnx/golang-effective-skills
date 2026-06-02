# Architecture

The repository uses progressive disclosure.

## Layers

1. `skills/*/SKILL.md`: compact task workflow loaded when a skill triggers.
2. `skills/*/references/*.md`: concise checklists and source maps loaded only
   when the task needs detail.
3. `agents/*.md`: reusable role profiles that orchestrate skills for
   implementation or review subagents.
4. `sources/chunks/*.md`: generated source chunks used for grounding,
   conflict resolution, and source-backed updates.
5. `sources/raw/*`: downloaded upstream documents kept for provenance and
   regeneration.

## Routing

`golang-effective` is the entry point for broad Go work. It selects one primary
skill and at most two adjacent skills. Normal coding and review tasks should
not load full source documents.

## Source Priority

1. User request and repository-specific style.
2. Go compiler, formatter, tests, vet, race detector, and project tooling.
3. Go language spec and current Go docs.
4. Effective Go as baseline idiom.
5. Google Go Style Guide decisions.
6. Uber Go Style Guide for application/service conventions.
7. Local consistency in the touched package.
