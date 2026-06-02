# Contributing

Contributions should make the skill pack easier for agents to use without
loading unnecessary context.

## Ground Rules

- Keep each skill task-specific.
- Keep `SKILL.md` concise and procedural.
- Put detailed guidance in `references/*.md`.
- Use source anchors instead of long quotations.
- Validate before opening a pull request.

## Skill Format

`SKILL.md` frontmatter must contain only:

```yaml
---
name: skill-name
description: Clear trigger description with when-to-use details.
---
```

Do not add `version`, `context_budget`, `sources`, or `load_when` to the
frontmatter. Put UI metadata in `agents/openai.yaml` and source details in
`references/source-map.md`.

## Adding or Updating a Skill

1. Decide the task the skill serves.
2. Add or update `skills/<skill-name>/SKILL.md`.
3. Add concise source-backed references under `references/`.
4. Add source chunk pointers in `references/source-map.md`.
5. Add or update a fixture under `fixtures/go-style/` if behavior changed.
6. Run validation:

```bash
python3 scripts/validate_skills.py skills
```

## Pull Request Checklist

- `SKILL.md` frontmatter contains only `name` and `description`.
- Skill body stays concise.
- References are source-backed.
- Validation passes.
- README/docs are updated if public behavior changes.

## Special Agents

Root-level agent profiles live under `agents/*.md`. Use them for reusable
subagent roles that orchestrate skills, such as implementation or review.

Agent profile frontmatter must contain:

```yaml
---
name: go-implementer
description: Long trigger description.
model: inherit
---
```

Validate agent profiles with:

```bash
python3 scripts/validate_agents.py agents
```
