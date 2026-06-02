---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

#### Sentinel error placement

An exception to this rule is when wrapping sentinel errors. A sentinel error is an error that serves as a primary categorization of a failure. This helps observers quickly understand the nature of a failure (such as “not found” or “invalid argument”) without having to parse the entire error message. Identifying that error type as early as possible in the error string is beneficial.

Examples of sentinel errors include os errors (e.g., `os.ErrInvalid`) and package-level errors.

In these cases, placing the `%w` verb at the beginning of the error string can improve readability by immediately identifying the category of the error.

```go
// Good:
package parser

var ErrParse = fmt.Errorf("parse error")

// This is another package error that could be returned.
var ErrParseInvalidHeader = fmt.Errorf("%w: invalid header", ErrParse)

func parseHeader() error {
  err := checkHeader()
  return fmt.Errorf("%w: invalid character in header: %v", ErrParseInvalidHeader, err)
}

err := fmt.Errorf("%w: couldn't find fortune database: %v", ErrInternal, err)

```

Placing the status at the beginning ensures that the most relevant categorical information is most prominent.

```go
// Bad:
package parser

var ErrParse = fmt.Errorf("parse error")

// This is another package error that could be returned.
var ErrParseInvalidHeader = fmt.Errorf("%w: invalid header", ErrParse)

func parseHeader() error {
  err := checkHeader()
  return fmt.Errorf("invalid character in header: %v: %w", err, ErrParseInvalidHeader)
}

var ErrInternal = status.Error(codes.Internal, "internal")
err2 := fmt.Errorf("couldn't find fortune database: %v: %w", err, ErrInternal)

```

When you place it at the end, it makes it harder to identify the error category when reading the error text, as it’s buried in the specific error details.

See also:

- Go Tip #48: Error Sentinel Values
- Go Tip #106: Error Naming Conventions
