---
source_name: "External Linked Documentation"
source_url: "https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully"
source_path: "sources/raw/external/dave-cheney-net-2016-04-27-dont-just-check-errors-handle-them-gracefully-a37809db60.html"
license_ref: ""
---

# Errors are just values

## Never inspect the output of error.Error

As an aside, I believe you should never inspect the output of the `error.Error` method. The `Error` method on the `error` interface exists for humans, not code.

The contents of that string belong in a log file, or displayed on screen. You shouldn’t try to change the behaviour of your program by inspecting it.

I know that sometimes this isn’t possible, and as someone pointed out on twitter, this advice doesn’t apply to writing tests. Never the less, comparing the string form of an error is, in my opinion, a code smell, and you should try to avoid it.

# Errors are just values

## Sentinel errors become part of your public API

If your public function or method returns an error of a particular value then that value must be public, and of course documented. This adds to the surface area of your API.

If your API defines an interface which returns a specific error, all implementations of that interface will be restricted to returning only that error, even if they could provide a more descriptive error.

We see this with `io.Reader`. Functions like `io.Copy` require a reader implementation to return _exactly_ `io.EOF` to signal to the caller _no more data, but that isn’t an error_.
