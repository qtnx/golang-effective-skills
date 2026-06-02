---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Adding information to errors

When adding information to errors, avoid redundant information that the underlying error already provides. The `os` package, for instance, already includes path information in its errors.

```go
// Good:
if err := os.Open("settings.txt"); err != nil {
  return fmt.Errorf("launch codes unavailable: %v", err)
}

// Output:
//
// launch codes unavailable: open settings.txt: no such file or directory

```

Here, “launch codes unavailable” adds specific meaning to the `os.Open` error that’s relevant to the current function’s context, without duplicating the underlying file path information.

```go
// Bad:
if err := os.Open("settings.txt"); err != nil {
  return fmt.Errorf("could not open settings.txt: %v", err)
}

// Output:
//
// could not open settings.txt: open settings.txt: no such file or directory

```

Don’t add an annotation if its sole purpose is to indicate a failure without adding new information. The presence of an error sufficiently conveys the failure to the caller.

```go
// Bad:
return fmt.Errorf("failed: %v", err) // just return err instead

```

The choice between `%v` and `%w` when wrapping errors with `fmt.Errorf` is a nuanced decision that significantly impacts how errors are propagated handled, inspected, and documented within your application. The core principle is to make error values useful to their observers, whether those observers are humans or code.

-
**`%v` for simple annotation or new error**

The `%v` verb is your general-purpose tool for string formatting of any Go value, including errors. When used with `fmt.Errorf`, it embeds the string representation of an error (what its `Error()` method returns) into a new error value, dropping any structured information from the original error. Examples to use `%v`:

-
Adding interesting, non-redundant context: as in the example above.

-
Logging or displaying errors: When the primary goal is to present a human-readable error message in logs or to a user, and you don’t intend for the caller to programmatically `errors.Is` or `errors.As` the error (Note: `errors.Unwrap` is generally not recommended here as it doesn’t handle multi-errors).

-
Creating fresh, independent errors: Sometimes it is necessary to transform an error into a new error message, thereby hiding the specifics of the original error. This practice is particularly beneficial at system boundaries, including but not limited to RPC, IPC, and storage, where we translate domain-specific errors into a canonical error space.

```go
// Good:
func (*FortuneTeller) SuggestFortune(context.Context, *pb.SuggestionRequest) (*pb.SuggestionResponse, error) {
  // ...
  if err != nil {
    return nil, fmt.Errorf("couldn't find fortune database: %v", err)
  }
}

```

We could also explicitly annotate RPC code `Internal` to the example above.

```go
// Good:
import (
  "google.golang.org/grpc/codes"
  "google.golang.org/grpc/status"
)

func (*FortuneTeller) SuggestFortune(context.Context, *pb.SuggestionRequest) (*pb.SuggestionResponse, error) {
  // ...
  if err != nil {
    // Or use fmt.Errorf with the %w verb if deliberately wrapping an
    // error which the caller is meant to unwrap.
    return nil, status.Errorf(codes.Internal, "couldn't find fortune database", status.ErrInternal)
  }
}

```

-
**`%w` (wrap) for programmatic inspection and error chaining**

The `%w` verb is specifically designed for error wrapping. It creates a new error that provides an `Unwrap()` method, allowing callers to programmatically inspect the error chain using `errors.Is` and `errors.As`. Examples to use `%w`:

-
Adding context while preserving the original error for programmatic inspection: This is the primary use case within helpers of your application. You want to enrich an error with additional context (e.g., what operation was being performed when it failed) but still allow the caller to check if the underlying error is a specific sentinel error or type.

```go
// Good:
func (s *Server) internalFunction(ctx context.Context) error {
  // ...
  if err != nil {
    return fmt.Errorf("couldn't find remote file: %w", err)
  }
}

```

This allows a higher-level function to do `errors.Is(err, fs.ErrNotExist)` if the underlying error was `fs.ErrNotExist`, even though it’s wrapped.

At points where your system interacts with external systems like RPC, IPC, or storage, it’s often better to translate domain-specific errors into a standardized error space (e.g., gRPC status codes) rather than simply wrapping the raw underlying error with `%w`. The client typically doesn’t care about the exact internal file system error; they care about the canonical result (e.g., `Internal`, `NotFound`, `PermissionDenied`).

-
When you explicitly document and test the underlying errors you expose: If your package’s API guarantees that certain underlying errors can be unwrapped and checked by callers (e.g., “this function might return `ErrInvalidConfig` wrapped within a more general error”), then `%w` is appropriate. This forms part of your package’s contract.

See also:

- Error Documentation Conventions
- Blog post on error wrapping
