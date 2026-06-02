---
source_name: "External Linked Documentation"
source_url: "https://docs.bazel.build/versions/main/be/general.html"
source_path: "sources/raw/external/docs-bazel-build-versions-main-be-general-html-1d20475b8b.html"
license_ref: ""
---

# General Rules

General Rules - Bazel main
    **IMPORTANT:** The Bazel docs have moved! Please update your bookmark to https://bazel.build/reference/be/general <https://bazel.build/reference/be/general>
 You can read about <https://blog.bazel.build/2022/02/17/Launching-new-Bazel-site.html> the migration, and let us know what you think <https://forms.gle/onkAkr2ZwBmcbWXj7>.
# General Rules
## Rules

-   alias
-   config_setting
-   filegroup
-   genquery
-   genrule
-   test_suite

# General Rules

##  alias

```go
alias(name, actual, compatible_with, deprecation, features, restricted_to, tags, target_compatible_with, testonly, visibility)
```

 The `alias` rule creates another name a rule can be referred to as.

 Aliasing only works for "regular" targets. In particular, `package_group` and `test_suite` cannot be aliased.

 The alias rule has its own visibility declaration. In all other respects, it behaves like the rule it references with some minor exceptions:
-  Tests are not run if their alias is mentioned on the command line. To define an alias that runs the referenced test, use a `test_suite` rule with a single target in its `tests` attribute.
-  When defining environment groups, the aliases to `environment` rules are not supported. They are not supported in the `--target_environment` command line option, either.

#### Examples

```go

filegroup(
    name = "data",
    srcs = ["data.txt"],
)

alias(
    name = "other",
    actual = ":data",
)

```

### Arguments
        Attributes     `name`
`Name; required`

A unique name for this target.
     `actual`
`Label; required`
 The target this alias refers to. It does not need to be a rule, it can also be an input file.
