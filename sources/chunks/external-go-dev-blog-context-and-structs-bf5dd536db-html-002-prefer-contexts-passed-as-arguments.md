---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/context-and-structs"
source_path: "sources/raw/external/go-dev-blog-context-and-structs-bf5dd536db.html"
license_ref: ""
---

# The Go Blog

## Prefer contexts passed as arguments

To understand the advice to not store context in structs, let’s consider the preferred context-as-argument approach:

```go
// Worker fetches and adds works to a remote work orchestration server.
type Worker struct { /* … */ }

type Work struct { /* … */ }

func New() *Worker {
  return &Worker{}
}

func (w *Worker) Fetch(ctx context.Context) (*Work, error) {
  _ = ctx // A per-call ctx is used for cancellation, deadlines, and metadata.
}

func (w *Worker) Process(ctx context.Context, work *Work) error {
  _ = ctx // A per-call ctx is used for cancellation, deadlines, and metadata.
}

```

Here, the `(*Worker).Fetch` and `(*Worker).Process` methods both accept a context directly. With this pass-as-argument design, users can set per-call deadlines, cancellation, and metadata. And, it’s clear how the `context.Context` passed to each method will be used: there’s no expectation that a `context.Context` passed to one method will be used by any other method. This is because the context is scoped to as small an operation as it needs to be, which greatly increases the utility and clarity of `context` in this package.
