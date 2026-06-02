---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

## Error handling

In Go, errors are values; they are created by code and consumed by code. Errors can be:

- Converted into diagnostic information for display to humans
- Used by the maintainer
- Interpreted by an end user

Error messages also show up across a variety of different surfaces including log messages, error dumps, and rendered UIs.

Code that processes (produces or consumes) errors should do so deliberately. It can be tempting to ignore or blindly propagate an error return value. However, it is always worth considering whether the current function in the call frame is positioned to handle the error most effectively. This is a large topic and it is hard to give categorical advice. Use your judgment, but keep the following considerations in mind:

- When creating an error value, decide whether to give it any structure.
- When handling an error, consider adding information that you have but that the caller and/or callee might not.
- See also guidance on error logging.

While it is usually not appropriate to ignore an error, a reasonable exception to this is when orchestrating related operations, where often only the first error is useful. Package `errgroup` provides a convenient abstraction for a group of operations that can all fail or be canceled as a group.

See also:

- Effective Go on errors
- A post by the Go Blog on errors
- Package `errors`
- Package `upspin.io/errors`
- GoTip #89: When to Use Canonical Status Codes as Errors
- GoTip #48: Error Sentinel Values
- GoTip #13: Designing Errors for Checking
