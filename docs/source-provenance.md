# Source Provenance

Downloaded on 2026-06-02 for building a compact, source-backed Go skills pack.

This repository is not an official Google, Go, or Uber project. The skill text,
scripts, fixtures, and packaging are curated derivative guidance built from the
source documents listed below.

## Google Go Style Guide

Primary URLs:

- https://google.github.io/styleguide/go/index.html#gotip
- https://google.github.io/styleguide/go/guide
- https://google.github.io/styleguide/go/decisions
- https://google.github.io/styleguide/go/best-practices

Raw Markdown URLs:

- https://raw.githubusercontent.com/google/styleguide/gh-pages/go/index.md
- https://raw.githubusercontent.com/google/styleguide/gh-pages/go/guide.md
- https://raw.githubusercontent.com/google/styleguide/gh-pages/go/decisions.md
- https://raw.githubusercontent.com/google/styleguide/gh-pages/go/best-practices.md

Local files:

- `sources/raw/google-go-styleguide/index.html`
- `sources/raw/google-go-styleguide/guide.html`
- `sources/raw/google-go-styleguide/decisions.html`
- `sources/raw/google-go-styleguide/best-practices.html`
- `sources/raw/google-go-styleguide/index.md`
- `sources/raw/google-go-styleguide/guide.md`
- `sources/raw/google-go-styleguide/decisions.md`
- `sources/raw/google-go-styleguide/best-practices.md`
- `sources/raw/google-go-styleguide/*.headers.txt`

License:

- `sources/licenses/google-styleguide-LICENSE.txt`

Notes:

- The linked Google page is an index. The full guide content is split across
  `guide`, `decisions`, and `best-practices`.
- The Markdown source files are preferred for chunking and source anchors.

## Effective Go

Primary URL:

- https://go.dev/doc/effective_go

Local files:

- `sources/raw/effective-go/effective_go.html`
- `sources/raw/effective-go/headers.txt`

License:

- `sources/licenses/go-LICENSE.txt`

Notes:

- The public page is HTML.
- Treat Effective Go as baseline Go idiom, not as a complete modern guide for
  modules, generics, or the full current ecosystem.

## Uber Go Style Guide

Primary URL:

- https://github.com/uber-go/guide/blob/master/style.md

Downloaded raw source:

- https://raw.githubusercontent.com/uber-go/guide/master/style.md

Local files:

- `sources/raw/uber-go-guide/style.md`
- `sources/raw/uber-go-guide/headers.txt`

License:

- `sources/licenses/uber-go-guide-LICENSE.txt`

Notes:

- The raw Markdown file is preferred over GitHub-rendered HTML.

## External Linked Documentation

The source chunk pipeline scans generated chunks for absolute documentation
links and fetches a conservative allowlist of linked docs into
`sources/raw/external/`.

Local files:

- `sources/raw/external/`
- `sources/raw/external-docs-manifest.json`

Current manifest:

- Fetched docs: 121
- Skipped URLs: 70
- Failed URLs: 0

Notes:

- `scripts/fetch_external_docs.py` normalizes duplicate Go domains such as
  `blog.golang.org` to `go.dev/blog`.
- Source-code viewers such as `go.googlesource.com/go/.../src/...` and
  `go.dev/src/...` are skipped because they are not documentation chunks.
- The generated manifest records every fetched, skipped, and failed URL plus
  the chunk paths that referenced it.
- External linked docs retain their original site licenses. This repository
  does not assign a single license to those cached documents.
