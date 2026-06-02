---
source_name: "External Linked Documentation"
source_url: "https://docs.bazel.build/versions/main/be/general.html"
source_path: "sources/raw/external/docs-bazel-build-versions-main-be-general-html-1d20475b8b.html"
license_ref: ""
---

# General Rules

##  filegroup

```go
filegroup(name, srcs, data, compatible_with, deprecation, distribs, features, licenses, output_group, restricted_to, tags, target_compatible_with, testonly, visibility)
```

 Use `filegroup` to give a convenient name to a collection of targets. These can then be referenced from other rules.

 Using `filegroup` is encouraged instead of referencing directories directly. The latter is unsound since the build system does not have full knowledge of all files below the directory, so it may not rebuild when these files change. When combined with glob, `filegroup` can ensure that all files are explicitly known to the build system.

#### Examples

 To create a `filegroup` consisting of two source files, do

```go

filegroup(
    name = "mygroup",
    srcs = [
        "a_file.txt",
        "some/subdirectory/another_file.txt",
    ],
)

```

 Or, use a `glob` to grovel a testdata directory:

```go

filegroup(
    name = "exported_testdata",
    srcs = glob([
        "testdata/*.dat",
        "testdata/logs/**/*.log",
    ]),
)

```

 To make use of these definitions, reference the `filegroup` with a label from any rule:

```go

cc_library(
    name = "my_library",
    srcs = ["foo.cc"],
    data = [
        "//my_package:exported_testdata",
        "//my_package:mygroup",
    ],
)

```

### Arguments
        Attributes     `name`
`Name; required`

A unique name for this target.
     `srcs`
`List of labels; optional`
 The list of targets that are members of the file group.
 It is common to use the result of a glob expression for the value of the `srcs` attribute.
     `data`
`List of labels; optional`
 The list of files needed by this rule at runtime.
 Targets named in the `data` attribute will be added to the `runfiles` of this `filegroup` rule. When the `filegroup` is referenced in the `data` attribute of another rule its `runfiles` will be added to the `runfiles` of the depending rule. See the data dependencies section and general documentation of `data` for more information about how to depend on and use data files.
     `output_group`
`String; optional`
 The output group from which to gather artifacts from sources. If this attribute is specified, artifacts from the specified output group of the dependencies will be exported instead of the default output group.
An "output group" is a category of output artifacts of a target, specified in that rule's implementation.
