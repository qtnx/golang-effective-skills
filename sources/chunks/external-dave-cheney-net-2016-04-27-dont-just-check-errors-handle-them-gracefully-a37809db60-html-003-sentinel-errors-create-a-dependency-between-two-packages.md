---
source_name: "External Linked Documentation"
source_url: "https://dave.cheney.net/2016/04/27/dont-just-check-errors-handle-them-gracefully"
source_path: "sources/raw/external/dave-cheney-net-2016-04-27-dont-just-check-errors-handle-them-gracefully-a37809db60.html"
license_ref: ""
---

# Errors are just values

## Sentinel errors create a dependency between two packages

By far the worst problem with sentinel error values is they create a source code dependency between two packages. As an example, to check if an error is equal to `io.EOF`, your code must import the `io` package.

This specific example does not sound so bad, because it is quite common, but imagine the coupling that exists when many packages in your project export error values, which other packages in your project must import to check for specific error conditions.

Having worked in a large project that toyed with this pattern, I can tell you that the spectre of bad design–in the form of an import loop–was never far from our minds.
