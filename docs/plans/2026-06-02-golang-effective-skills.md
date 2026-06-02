# Golang Effective Skills Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Turn this workspace into a polished public GitHub repository for a source-backed Go skills pack that agents and subagents can load by task without wasting context.

**Architecture:** Publish a repo named `golang-effective-skills` with root-level GitHub community files, self-contained validation/install scripts, downloaded source provenance, and a compact MVP skill set under `skills/`. Use one real router skill plus task-specific skills; keep full source documents and generated chunks outside skill bodies so agents load only the relevant context.

**Tech Stack:** Codex skill format, Markdown references, Python standard library scripts, shell install/validate scripts, GitHub Actions, `rg`, `gofmt`, `go test`, source provenance files.

---

## Public Repo Strategy

Build for two audiences:

- **Agents:** need tiny, task-routed `SKILL.md` files with source anchors and adjacent-skill routing.
- **Humans on GitHub:** need a clear README, install command, skill table, examples, license/provenance, roadmap, and contribution path.

Repository name:

```text
golang-effective-skills
```

Recommended GitHub topics:

```text
golang
go
codex
codex-skills
ai-agents
developer-tools
code-review
go-style-guide
effective-go
testing
concurrency
performance
open-source
```

## Design Decision

Use a task-based skill split, not a document-based split.

MVP skills:

- `golang-effective`: real router skill and baseline workflow for broad Go implementation, refactor, debugging, and review tasks.
- `go-style-core`: clarity, simplicity, concision, maintainability, consistency, formatting, and local-style policy.
- `go-naming-api-design`: package names, exported APIs, comments, receiver names, stutter, constructors, interfaces at API boundaries.
- `go-errors-panics`: error returns, wrapping, sentinel/custom errors, panic/recover, logging errors once, testable error behavior.
- `go-testing`: table tests, subtests, helpers, useful failures, package choice, deterministic tests, examples, benchmarks.
- `go-code-review-checklist`: findings-first Go review checklist that routes into the other skills.

Backlog skills:

- `go-concurrency-context`
- `go-interfaces-generics`
- `go-performance-allocations`
- `go-project-structure-tooling`

Why this split:

- Agents work by task, not by source document.
- The router prevents loading all guidance into every Go request.
- A smaller MVP is easier to validate, install, explain, and star.
- Backlog skills can be added after the core pack proves useful.

Rejected alternatives:

- Top-level `ROUTER.md` only: easy for humans, but it is not a Codex skill and will not trigger like `skills/golang-effective/SKILL.md`.
- Single monolithic skill: high context cost and weak task targeting.
- Ten skills in the first release: more surface area to validate before the repo has social proof.

## Skill Format Rules

Every skill folder must follow Codex skill anatomy:

```text
skills/<skill-name>/
  SKILL.md
  agents/openai.yaml
  references/
    checklist.md
    source-map.md
```

`SKILL.md` frontmatter must contain only:

```yaml
---
name: skill-name
description: Clear trigger description with when-to-use details.
---
```

Do not put `version`, `context_budget`, `sources`, or `load_when` in `SKILL.md` frontmatter. Put UI metadata in `agents/openai.yaml`; put source detail in `references/source-map.md`; put public documentation at repo root or under `docs/`, not inside skill folders.

## Context Budget Rules

- Keep each MVP `SKILL.md` under roughly 150 lines.
- Keep each `references/*.md` file under roughly 120 lines.
- Load one primary skill and at most two adjacent skills.
- Never load full source docs for normal coding/review tasks.
- Load source chunks only when grounding, resolving conflict, or quoting a rule.
- Prefer source line pointers and concise summaries over long excerpts.

## Source Priority Policy

Use this precedence when guidance conflicts:

1. User request and repository-specific style.
2. Go compiler, `gofmt`, `go test`, `go vet`, race detector, and project tooling.
3. Go language spec and current Go docs.
4. Effective Go as baseline idiom, with caveat that it is not a complete modern modules/generics guide.
5. Google Go Style Guide decisions for normative style questions.
6. Uber Go Style Guide for pragmatic service/application code conventions.
7. Local consistency in the touched package.

## Target Repository Layout

```text
golang-effective-skills/
  README.md
  LICENSE
  NOTICE.md
  THIRD_PARTY_NOTICES.md
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  SECURITY.md
  .gitignore
  .github/
    ISSUE_TEMPLATE/
      bug_report.yml
      skill_request.yml
    workflows/
      validate.yml
    pull_request_template.md
  skills/
    golang-effective/
    go-style-core/
    go-naming-api-design/
    go-errors-panics/
    go-testing/
    go-code-review-checklist/
  sources/
    raw/
    normalized/
    chunks/
    licenses/
    manifest.json
  scripts/
    extract_doc_headings.py
    chunk_sources.py
    validate_skills.py
    install.sh
  fixtures/
    go-style/
  docs/
    architecture.md
    source-provenance.md
    roadmap.md
    plans/
```

## Task 1: Reorganize Current Source Docs

**Files:**
- Move: `source-docs/google-go-styleguide/*` to `sources/raw/google-go-styleguide/`
- Move: `source-docs/effective-go/*` to `sources/raw/effective-go/`
- Move: `source-docs/uber-go-guide/*` to `sources/raw/uber-go-guide/`
- Move/update: `source-docs/MANIFEST.md` to `docs/source-provenance.md`
- Create: `sources/licenses/google-styleguide-LICENSE.txt`
- Create: `sources/licenses/uber-go-guide-LICENSE.txt`
- Create: `sources/licenses/go-LICENSE.txt`
- Create: `THIRD_PARTY_NOTICES.md`
- Delete empty: `source-docs/`

**Step 1: Create target directories**

Run:

```bash
mkdir -p sources/raw/google-go-styleguide sources/raw/effective-go sources/raw/uber-go-guide sources/licenses docs
```

Expected: directories exist.

**Step 2: Move downloaded files**

Run:

```bash
mv source-docs/google-go-styleguide/* sources/raw/google-go-styleguide/
mv source-docs/effective-go/* sources/raw/effective-go/
mv source-docs/uber-go-guide/* sources/raw/uber-go-guide/
mv source-docs/MANIFEST.md docs/source-provenance.md
rmdir source-docs/google-go-styleguide source-docs/effective-go source-docs/uber-go-guide source-docs
```

Expected: no `source-docs/` remains; all source files live under `sources/raw/`.

**Step 3: Download upstream license files**

Run:

```bash
curl -L --fail --silent --show-error -o sources/licenses/google-styleguide-LICENSE.txt https://raw.githubusercontent.com/google/styleguide/gh-pages/LICENSE
curl -L --fail --silent --show-error -o sources/licenses/uber-go-guide-LICENSE.txt https://raw.githubusercontent.com/uber-go/guide/master/LICENSE
curl -L --fail --silent --show-error -o sources/licenses/go-LICENSE.txt https://raw.githubusercontent.com/golang/go/master/LICENSE
```

Expected:

- Google Style Guide license starts with Creative Commons Attribution 3.0 text.
- Uber Go Style Guide license starts with Apache License 2.0 text.
- Go license starts with Go Authors copyright and BSD-style redistribution terms.

**Step 4: Write `THIRD_PARTY_NOTICES.md`**

Include:

- Source name.
- Source URL.
- Local paths.
- Retrieval date.
- License file path.
- Note that the skill pack is a curated derivative/reference pack, not an official Google, Go, or Uber project.

**Step 5: Commit source organization**

Run:

```bash
git add sources docs/source-provenance.md THIRD_PARTY_NOTICES.md
git commit -m "chore: organize source corpus and notices"
```

## Task 2: Add Public Repo Shell

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `NOTICE.md`
- Create: `CONTRIBUTING.md`
- Create: `CODE_OF_CONDUCT.md`
- Create: `SECURITY.md`
- Create: `.gitignore`
- Create: `.github/ISSUE_TEMPLATE/bug_report.yml`
- Create: `.github/ISSUE_TEMPLATE/skill_request.yml`
- Create: `.github/pull_request_template.md`
- Create: `.github/workflows/validate.yml`
- Create: `docs/architecture.md`
- Create: `docs/roadmap.md`

**Step 1: Write README**

The root `README.md` must include:

- One-sentence value proposition.
- Install snippet:

```bash
git clone https://github.com/<owner>/golang-effective-skills.git
cd golang-effective-skills
./scripts/install.sh
```

- Skill table with name, when to use, and status.
- Three example prompts.
- Repo layout.
- Source/provenance note.
- Link to `CONTRIBUTING.md`, `SECURITY.md`, and `THIRD_PARTY_NOTICES.md`.

**Step 2: Add root license**

Use `LICENSE` for this repo's original skill text, scripts, fixtures, and packaging. Recommended: MIT for adoption simplicity.

Add `NOTICE.md` explaining:

- Root license applies to original repository content.
- Upstream source documents keep their own licenses.
- See `THIRD_PARTY_NOTICES.md`.

**Step 3: Add contribution and security files**

`CONTRIBUTING.md` must explain:

- How to propose a skill.
- How to keep `SKILL.md` concise.
- How to add source anchors.
- How to run validation.

`SECURITY.md` must explain:

- Report malicious prompt-injection, unsafe install behavior, or source tampering privately.
- Do not open public issues with exploit details.

**Step 4: Add GitHub templates**

`bug_report.yml` fields:

- Skill name.
- Prompt/task.
- Expected behavior.
- Actual behavior.
- Relevant source anchor.

`skill_request.yml` fields:

- Proposed skill name.
- Task type.
- Why existing skills are insufficient.
- Candidate sources.

PR template checklist:

```text
- [ ] SKILL.md frontmatter contains only name and description.
- [ ] Skill body stays concise.
- [ ] References are source-backed.
- [ ] scripts/validate_skills.py passes.
- [ ] README/docs updated if public behavior changed.
```

**Step 5: Add GitHub Actions validation**

`.github/workflows/validate.yml`:

```yaml
name: validate

on:
  pull_request:
  push:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - run: python3 scripts/validate_skills.py skills
```

**Step 6: Commit public shell**

Run:

```bash
git add README.md LICENSE NOTICE.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md .github .gitignore docs
git commit -m "chore: add public repository shell"
```

## Task 3: Add Source Processing and Validation Scripts

**Files:**
- Create: `scripts/extract_doc_headings.py`
- Create: `scripts/chunk_sources.py`
- Create: `scripts/validate_skills.py`
- Create: `scripts/install.sh`
- Create generated: `sources/manifest.json`
- Create generated: `sources/normalized/*.md`
- Create generated: `sources/chunks/*.md`

**Step 1: Write heading extraction script**

Use only Python standard library.

Behavior:

- For Markdown, detect `^#{1,4} ` headings.
- For Effective Go HTML, detect `<h1>` through `<h4>` headings and strip tags.
- Print source path, line number, level, and heading text.

**Step 2: Write chunking script**

Use only Python standard library.

Behavior:

- Convert HTML headings and paragraphs/code blocks into readable Markdown where needed.
- Preserve Markdown sources as Markdown.
- Split by headings into chunk files.
- Add a compact source header to each chunk:

```md
---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---
```

**Step 3: Write validation script**

`scripts/validate_skills.py` must check:

- Every `skills/*/SKILL.md` exists.
- Skill folder name equals `name` in frontmatter.
- Frontmatter contains only `name` and `description`.
- `description` is non-empty and includes task triggers.
- `agents/openai.yaml` exists.
- Every referenced `references/*.md` file exists.
- No skill folder contains README, install guide, or changelog files.
- `SKILL.md` line count is below 150 for MVP skills.

**Step 4: Write install script**

`scripts/install.sh`:

- Resolve repo root.
- Resolve destination `${CODEX_HOME:-$HOME/.codex}/skills`.
- Copy `skills/*` into destination.
- Refuse to overwrite an existing destination skill unless `--force` is passed.
- Print installed skill names.

**Step 5: Generate source outputs**

Run:

```bash
python3 scripts/chunk_sources.py sources/raw sources
python3 scripts/validate_skills.py skills
```

Expected:

- `sources/manifest.json` exists.
- `sources/chunks/` contains chunked source sections.
- Validation currently passes once MVP skill folders are created.

**Step 6: Commit scripts**

Run:

```bash
git add scripts sources/manifest.json sources/normalized sources/chunks
git commit -m "chore: add source processing and validation scripts"
```

## Task 4: Scaffold MVP Skills

**Files:**
- Create: `skills/golang-effective/`
- Create: `skills/go-style-core/`
- Create: `skills/go-naming-api-design/`
- Create: `skills/go-errors-panics/`
- Create: `skills/go-testing/`
- Create: `skills/go-code-review-checklist/`

**Step 1: Initialize skill directories**

Prefer `skill-creator` initialization locally when available:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py" golang-effective --path ./skills --resources references
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py" go-style-core --path ./skills --resources references
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py" go-naming-api-design --path ./skills --resources references
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py" go-errors-panics --path ./skills --resources references
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py" go-testing --path ./skills --resources references
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py" go-code-review-checklist --path ./skills --resources references
```

If that path is not present, create the same folders manually with `SKILL.md`, `agents/openai.yaml`, and `references/`.

**Step 2: Remove placeholders**

Delete template placeholder references or examples that do not support the skill.

**Step 3: Commit scaffold**

Run:

```bash
git add skills
git commit -m "chore: scaffold MVP Go skills"
```

## Task 5: Implement Router Skill

**Files:**
- Modify: `skills/golang-effective/SKILL.md`
- Modify: `skills/golang-effective/agents/openai.yaml`
- Create: `skills/golang-effective/references/routing.md`
- Create: `skills/golang-effective/references/source-priority.md`

**Step 1: Write frontmatter**

Use:

```yaml
---
name: golang-effective
description: Source-backed Go task router and baseline workflow. Use when Codex is writing, refactoring, debugging, reviewing, or designing Go code and needs to choose the right Effective Go, Google Go Style, or Uber Go Style guidance without loading unnecessary context.
---
```

**Step 2: Write body**

Include:

- Start by identifying task type.
- Load one primary adjacent skill and at most two secondary skills.
- Do not load full source docs.
- Prefer local repository style when it does not harm correctness/readability.
- Run `gofmt` and project tests when editing Go code.
- Use source chunks only for grounding or conflict resolution.

**Step 3: Write routing reference**

Map signals:

```text
error, wrap, panic, recover, logging -> go-errors-panics
package, exported API, name, receiver, interface boundary -> go-naming-api-design
test, table test, helper, benchmark, golden -> go-testing
review, audit, PR, final pass -> go-code-review-checklist
style, idiomatic, readability, formatting -> go-style-core
goroutine, channel, context, cancellation -> backlog: go-concurrency-context
generic, any, interface ownership -> backlog: go-interfaces-generics
allocation, benchmark, pprof -> backlog: go-performance-allocations
module, internal, CI, lint -> backlog: go-project-structure-tooling
```

**Step 4: Validate**

Run:

```bash
python3 scripts/validate_skills.py skills
```

Expected: `golang-effective` passes.

## Task 6: Implement MVP Topic Skills

**Files:**
- Modify: `skills/go-style-core/SKILL.md`
- Modify: `skills/go-style-core/agents/openai.yaml`
- Create: `skills/go-style-core/references/checklist.md`
- Create: `skills/go-style-core/references/source-map.md`
- Repeat the same structure for:
  - `skills/go-naming-api-design/`
  - `skills/go-errors-panics/`
  - `skills/go-testing/`
  - `skills/go-code-review-checklist/`

**Step 1: `go-style-core`**

Cover:

- Clarity before cleverness.
- `gofmt` as baseline.
- Comments explain why, not obvious what.
- Local consistency with readability guardrail.
- Keep deep topics routed to adjacent skills.

Primary source anchors:

- `sources/raw/google-go-styleguide/guide.md`
- `sources/raw/google-go-styleguide/decisions.md`
- `sources/raw/effective-go/effective_go.html`
- `sources/raw/uber-go-guide/style.md`

**Step 2: `go-naming-api-design`**

Cover:

- Package names and exported names.
- Receiver names, getters, initialisms, repetition/stutter.
- Exported doc comments.
- Interface ownership and API call-site readability.

Primary source anchors:

- Google naming decisions and best practices.
- Effective Go names/interfaces sections.
- Uber package/function/import aliasing sections.

**Step 3: `go-errors-panics`**

Cover:

- Error returns and error strings.
- `%w`, `%v`, `errors.Is`, `errors.As`.
- Sentinel and custom error tradeoffs.
- Panic/recover policy.
- Logging errors once.
- Testing error semantics.

Primary source anchors:

- Google errors decisions and best practices.
- Effective Go errors, panic, recover.
- Uber errors section.

**Step 4: `go-testing`**

Cover:

- Table-driven tests.
- Subtests and row names.
- `t.Helper`.
- Useful failure messages with got/want/context.
- Same-package vs external-package tests.
- Deterministic tests for time, random, filesystem, network, concurrency.
- Benchmark setup outside measured section.

Primary source anchors:

- Google useful test failures.
- Google test structure.
- Google best-practices tests.
- Uber test tables.

**Step 5: `go-code-review-checklist`**

Cover:

- Findings-first review format.
- Correctness before style.
- Check compile/test/gofmt.
- Trace API, error, cancellation, test, package boundary, and dependency changes.
- Avoid generic style nits when local convention differs.

Primary source anchors:

- Router routing map.
- All MVP skill source maps.

**Step 6: Validate**

Run:

```bash
python3 scripts/validate_skills.py skills
```

Expected: all MVP skills pass.

**Step 7: Commit MVP skills**

Run:

```bash
git add skills
git commit -m "feat: add MVP Go skills"
```

## Task 7: Add Fixtures and Forward-Test

**Files:**
- Create: `fixtures/go-style/bad_style.go`
- Create: `fixtures/go-style/bad_api.go`
- Create: `fixtures/go-style/bad_errors.go`
- Create: `fixtures/go-style/bad_tests_test.go`
- Create: `fixtures/go-style/bad_review_bundle.go`
- Create: `docs/validation.md`

**Step 1: Create fixtures**

Each fixture should include two or three realistic issues from the relevant skill. Keep fixtures small enough to inspect quickly.

**Step 2: Run local validation**

Run:

```bash
python3 scripts/validate_skills.py skills
```

Expected: validation passes before forward-testing.

**Step 3: Forward-test with fresh agents**

Use prompts like:

```text
Use $go-testing at /path/to/repo/skills/go-testing to review fixtures/go-style/bad_tests_test.go. Return only actionable findings with file and line references.
```

Do not include expected answers in the prompt.

**Step 4: Record outcomes**

`docs/validation.md` should include:

- Prompt used.
- Skill used.
- Findings caught.
- Findings missed.
- Skill edits made after validation.

**Step 5: Commit fixtures and validation notes**

Run:

```bash
git add fixtures docs/validation.md
git commit -m "test: add Go skill validation fixtures"
```

## Task 8: Add Backlog Roadmap

**Files:**
- Modify: `docs/roadmap.md`
- Optionally create directories later:
  - `skills/go-concurrency-context/`
  - `skills/go-interfaces-generics/`
  - `skills/go-performance-allocations/`
  - `skills/go-project-structure-tooling/`

**Step 1: Document backlog skills**

For each backlog skill, write:

- Trigger signals.
- Why it is not in MVP.
- Primary sources.
- Validation fixture needed before release.

**Step 2: Add release milestones**

Milestones:

- `v0.1.0`: MVP six skills, install script, validation, README.
- `v0.2.0`: concurrency and interfaces/generics.
- `v0.3.0`: performance and project tooling.
- `v0.4.0`: company overlay examples.

**Step 3: Commit roadmap**

Run:

```bash
git add docs/roadmap.md
git commit -m "docs: add Go skill roadmap"
```

## Task 9: Final Public-Repo Verification

**Files:**
- All root repo files.
- All `skills/*/SKILL.md`.
- All `skills/*/agents/openai.yaml`.
- All `skills/*/references/*.md`.
- All `sources/*`.
- All scripts.

**Step 1: Check repo tree**

Run:

```bash
find . -maxdepth 3 -type f | sort
```

Expected:

- Root community files are present.
- MVP skills are present.
- No `README.md` exists inside any skill folder.
- Source corpus is under `sources/`, not `source-docs/`.

**Step 2: Validate skills**

Run:

```bash
python3 scripts/validate_skills.py skills
```

Expected: all MVP skills pass.

**Step 3: Check line budgets**

Run:

```bash
wc -l skills/*/SKILL.md skills/*/references/*.md
```

Expected:

- Each MVP `SKILL.md` is under roughly 150 lines.
- Each reference file is under roughly 120 lines unless justified by source-map density.

**Step 4: Check public docs**

Run:

```bash
rg -n "sandbox:|/Users/|/mnt/data|TODO|PLACEHOLDER" README.md docs skills scripts THIRD_PARTY_NOTICES.md NOTICE.md CONTRIBUTING.md SECURITY.md .github --glob '!docs/plans/**'
```

Expected: no sandbox links, absolute local paths, unresolved TODOs, or placeholders remain.

**Step 5: Check install script**

Run:

```bash
./scripts/install.sh --dry-run
```

Expected:

- Prints destination path.
- Lists skills that would be installed.
- Does not modify files during dry run.

**Step 6: Check GitHub Actions locally as much as possible**

Run:

```bash
python3 scripts/validate_skills.py skills
git status --short
```

Expected:

- Validator passes.
- Only intentional files are modified.

**Step 7: Initial public commit**

If this is still an unborn branch, make the first commit:

```bash
git add .
git commit -m "feat: publish Go effective skills MVP"
```

## Task 10: Publish Checklist

**Files:**
- No local file edits required unless verification finds gaps.

**Step 1: Create GitHub repository**

Recommended settings:

- Repository name: `golang-effective-skills`.
- Visibility: public.
- Description: `Source-backed Go skills for Codex agents: style, APIs, errors, tests, and review without context bloat.`
- Enable issues.
- Enable discussions after first users arrive.

**Step 2: Add topics**

Add the topics listed in `Public Repo Strategy`.

**Step 3: Push**

Run:

```bash
git remote add origin git@github.com:<owner>/golang-effective-skills.git
git push -u origin main
```

**Step 4: Create first release**

Release:

```text
v0.1.0
```

Release notes:

- MVP six skills.
- Source-backed routing.
- Install script.
- Validation script.
- Source provenance and notices.

**Step 5: Social proof README check**

Before sharing, verify the first README viewport answers:

- What is this?
- Why should an agent developer care?
- How do I install it?
- Which skills are included?
- Is the source provenance trustworthy?

## Execution Handoff

Plan updated and saved to `docs/plans/2026-06-02-golang-effective-skills.md`.

Recommended execution approach:

1. Implement Tasks 1-3 first to make the repo public-ready infrastructure reproducible.
2. Implement Tasks 4-7 for the MVP skill pack.
3. Run Task 9 before any publish/push.
4. Publish only after `README.md`, validation, notices, and install script are clean.
