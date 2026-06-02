---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/context-and-structs"
source_path: "sources/raw/external/go-dev-blog-context-and-structs-bf5dd536db.html"
license_ref: ""
---

# The Go Blog

## Storing context in structs leads to confusion

Let’s inspect again the `Worker` example above with the disfavored context-in-struct approach. The problem with it is that when you store the context in a struct, you obscure lifetime to the callers, or worse intermingle two scopes together in unpredictable ways:

```go
type Worker struct {
  ctx context.Context
}

func New(ctx context.Context) *Worker {
  return &Worker{ctx: ctx}
}

func (w *Worker) Fetch() (*Work, error) {
  _ = w.ctx // A shared w.ctx is used for cancellation, deadlines, and metadata.
}

func (w *Worker) Process(work *Work) error {
  _ = w.ctx // A shared w.ctx is used for cancellation, deadlines, and metadata.
}

```

The `(*Worker).Fetch` and `(*Worker).Process` method both use a context stored in Worker. This prevents the callers of Fetch and Process (which may themselves have different contexts) from specifying a deadline, requesting cancellation, and attaching metadata on a per-call basis. For example: the user is unable to provide a deadline just for `(*Worker).Fetch`, or cancel just the `(*Worker).Process` call. The caller’s lifetime is intermingled with a shared context, and the context is scoped to the lifetime where the `Worker` is created.

The API is also much more confusing to users compared to the pass-as-argument approach. Users might ask themselves:

- Since `New` takes a `context.Context`, is the constructor doing work that needs cancellation or deadlines?
- Does the `context.Context` passed in to `New` apply to work in `(*Worker).Fetch` and `(*Worker).Process`? Neither? One but not the other?

The API would need a good deal of documentation to explicitly tell the user exactly what the `context.Context` is used for. The user might also have to read code rather than being able to rely on the structure of the API conveys.

And, finally, it can be quite dangerous to design a production-grade server whose requests don’t each have a context and thus can’t adequately honor cancellation. Without the ability to set per-call deadlines, your process could backlog <https://sre.google/sre-book/handling-overload/> and exhaust its resources (like memory)!
