# Validation

## Local Validation

Run:

```bash
python3 scripts/validate_skills.py skills
python3 scripts/validate_agents.py agents
```

Expected:

- All MVP skill folders pass frontmatter, metadata, reference, and line-budget
  checks.
- All special agent profiles pass frontmatter and role-body checks.

## Fixture Coverage

| Fixture | Intended Skill | Seeded Issues |
| --- | --- | --- |
| `fixtures/go-style/bad_style.go` | `go-style-core` | comment repeats code, unnecessary `else`, nested flow |
| `fixtures/go-style/bad_api.go` | `go-naming-api-design` | stutter, `Get` getter, long receiver name, broad interface |
| `fixtures/go-style/bad_errors.go` | `go-errors-panics` | capitalized punctuated error, log-and-return, panic on runtime error |
| `fixtures/go-style/bad_tests_test.go` | `go-testing` | unnamed table rows, weak failure message, helper missing `t.Helper()` |
| `fixtures/go-style/bad_review_bundle.go` | `go-code-review-checklist` | goroutine lifetime bug, premature return, missing cancellation path, printf logging |

## Forward-Test Prompts

These prompts are intentionally written without expected answers.

```text
Use $go-style-core at ./skills/go-style-core to review fixtures/go-style/bad_style.go. Return only actionable findings with file and line references.
```

```text
Use $go-naming-api-design at ./skills/go-naming-api-design to review fixtures/go-style/bad_api.go. Return only actionable findings with file and line references.
```

```text
Use $go-errors-panics at ./skills/go-errors-panics to review fixtures/go-style/bad_errors.go. Return only actionable findings with file and line references.
```

```text
Use $go-testing at ./skills/go-testing to review fixtures/go-style/bad_tests_test.go. Return only actionable findings with file and line references.
```

```text
Use $go-code-review-checklist at ./skills/go-code-review-checklist to review fixtures/go-style/bad_review_bundle.go. Return only actionable findings with file and line references.
```

## Current Forward-Test Status

No subagent forward-test has been run in this implementation pass. The prompts
above are ready for a delegated validation pass when the maintainer explicitly
chooses to run one.
