---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Package names

In Go, package names must be concise and use only lowercase letters and numbers (e.g., `k8s`, `oauth2`). Multi-word package names should remain unbroken and in all lowercase (e.g., `tabwriter` instead of `tabWriter`, `TabWriter`, or `tab_writer`).

Avoid selecting package names that are likely to be shadowed by commonly used local variable names. For example, `usercount` is a better package name than `count`, since `count` is a commonly used variable name.

Go package names should not have underscores. If you need to import a package that does have one in its name (usually from generated or third party code), it must be renamed at import time to a name that is suitable for use in Go code.

An exception to this is that package names that are only imported by generated code may contain underscores. Specific examples include:

-
Using the `_test` suffix for unit tests that only exercise the exported API of a package (package `testing` calls these “black box tests”). For example, a package `linkedlist` must define its black box unit tests in a package named `linkedlist_test` (not `linked_list_test`)

-
Using underscores and the `_test` suffix for packages that specify functional or integration tests. For example, a linked list service integration test could be named `linked_list_service_test`

-
Using the `_test` suffix for package-level documentation examples

Avoid uninformative package names like `util`, `utility`, `common`, `helper`, `model`, `testhelper`, and so on that would tempt users of the package to rename it when importing. See:

- Guidance on so-called “utility packages”
- Go Tip #97: What’s in a Name
- Go Tip #108: The Power of a Good Package Name

When an imported package is renamed (e.g. `import foopb "path/to/foo_go_proto"`), the local name for the package must comply with the rules above, as the local name dictates how the symbols in the package are referenced in the file. If a given import is renamed in multiple files, particularly in the same or nearby packages, the same local name should be used wherever possible for consistency.

See also: Go blog post about package names.
