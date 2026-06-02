---
source_name: "External Linked Documentation"
source_url: "https://go.dev/wiki/CodeReviewComments"
source_path: "sources/raw/external/go-dev-wiki-codereviewcomments-46376b7b23.html"
license_ref: ""
---

# Go Wiki: Go Code Review Comments

## Doc Comments

All top-level, exported names should have doc comments, as should non-trivial unexported type or function declarations. See https://go.dev/doc/effective_go#commentary <https://go.dev/doc/effective_go#commentary> for more information about commentary conventions.

# Go Wiki: Go Code Review Comments

## Don’t Panic

See https://go.dev/doc/effective_go#errors <https://go.dev/doc/effective_go#errors>. Don’t use panic for normal error handling. Use error and multiple return values.

# Go Wiki: Go Code Review Comments

## Error Strings

Error strings should not be capitalized (unless beginning with proper nouns or acronyms) or end with punctuation, since they are usually printed following other context. That is, use `fmt.Errorf("something bad")` not `fmt.Errorf("Something bad")`, so that `log.Printf("Reading %s: %v", filename, err)` formats without a spurious capital letter mid-message. This does not apply to logging, which is implicitly line-oriented and not combined inside other messages.
