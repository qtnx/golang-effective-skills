---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Error strings

<a id="TOC-ErrorStrings"></a>

Error strings should not be capitalized (unless beginning with an exported name,
a proper noun or an acronym) and should not end with punctuation. This is
because error strings usually appear within other context before being printed
to the user.

```go
// Bad:
err := fmt.Errorf("Something bad happened.")
```

```go
// Good:
err := fmt.Errorf("something bad happened")
```

On the other hand, the style for the full displayed message (logging, test
failure, API response, or other UI) depends, but should typically be
capitalized.

```go
// Good:
log.Infof("Operation aborted: %v", err)
log.Errorf("Operation aborted: %v", err)
t.Errorf("Op(%q) failed unexpectedly; err=%v", args, err)
```

<a id="handle-errors"></a>
