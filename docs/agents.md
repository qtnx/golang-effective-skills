# Special Agents

Special agents are reusable subagent profiles that orchestrate the smaller Go
skills in this repository.

They are different from `skills/*/agents/openai.yaml`:

- `skills/*/agents/openai.yaml` is UI metadata for a single skill.
- `agents/*.md` is a role profile for a focused worker or reviewer.

## `go-implementer`

Use when a Go task needs implementation, not just guidance.

Best fit:

- Feature implementation.
- Bug fixes.
- Refactors with a clear scope.
- Test additions or rewrites.
- Follow-through from a plan or issue.

Primary behavior:

- Reads local code first.
- Chooses a narrow implementation path.
- Uses Go skills only when relevant.
- Runs `gofmt` and targeted tests.
- Reports changed files and verification evidence.

Example:

```text
Use the go-implementer agent to implement the error handling cleanup described in this issue. Keep the scope narrow and run targeted tests.
```

## `go-best-practice-reviewer`

Use when Go code needs review before merge or after agent-generated changes.

Best fit:

- Pull request review.
- Final pass after implementation.
- Best-practice audit for generated Go code.
- Checking error handling, API names, tests, and style.

Primary behavior:

- Leads with findings.
- Orders findings by severity.
- Uses file and line references.
- Separates correctness risk from style preference.
- Routes into source-backed Go skills for detailed checks.

Example:

```text
Use the go-best-practice-reviewer agent to review this branch for Go correctness, tests, and idiomatic style. Return only actionable findings.
```

## Installation

`scripts/install.sh` installs both skills and root-level agent profiles by
default:

```bash
./scripts/install.sh
```

Install only agent profiles:

```bash
./scripts/install.sh --agents-only
```

Validate agent profile format:

```bash
python3 scripts/validate_agents.py agents
```
