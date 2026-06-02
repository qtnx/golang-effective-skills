---
source_name: "External Linked Documentation"
source_url: "https://docs.bazel.build/versions/main/be/general.html"
source_path: "sources/raw/external/docs-bazel-build-versions-main-be-general-html-1d20475b8b.html"
license_ref: ""
---

# General Rules

##  config_setting

```go
config_setting(name, constraint_values, define_values, deprecation, distribs, features, flag_values, licenses, tags, testonly, values, visibility)
```

 Matches an expected configuration state (expressed as Bazel flags or platform constraints) for the purpose of triggering configurable attributes. See select for how to consume this rule and  Configurable attributes for an overview of the general feature.
#### Examples

The following matches any Bazel invocation that specifies `--compilation_mode=opt` or `-c opt` (either explicitly at the command line or implicitly from .bazelrc files):

```go

  config_setting(
      name = "simple",
      values = {"compilation_mode": "opt"}
  )

```

The following matches any Bazel invocation that builds for ARM and that applies the custom define `FOO=bar` (for instance, `bazel build --cpu=arm --define FOO=bar ... `):

```go

  config_setting(
      name = "two_conditions",
      values = {
          "cpu": "arm",
          "define": "FOO=bar"
      }
  )

```

The following matches any Bazel invocation that builds for a platform that has an x86_64 architecture and glibc version 2.25, assuming the existence of a `constraint_value` with label `//example:glibc_2_25`. Note that a platform still matches if it defines additional constraint values beyond these two.

```go

  config_setting(
      name = "64bit_glibc_2_25",
      constraint_values = [
          "@platforms//cpu:x86_64",
          "//example:glibc_2_25",
      ]
  )

```
 In all these cases, it's possible for the configuration to change within the build, for example if a target needs to be built for a different platform than its dep. This means that even when a `config_setting` doesn't match the top-level command-line flags, it may still match some build targets.
#### Notes

- See select for what happens when multiple `config_setting`s match the current configuration state.
- For flags that support shorthand forms (e.g. `--compilation_mode` vs. `-c`), `values` definitions must use the full form. These automatically match invocations using either form.
-  If a flag takes multiple values (like `--copt=-Da --copt=-Db` or a list-typed  Starlark flag <https://docs.bazel.build/versions/main/skylark/config.html#user-defined-build-settings>), `values = { "flag": "a" }` matches if `"a"` is present _anywhere_ in the actual list.
 `values = { "myflag": "a,b" }` works the same way: this matches `--myflag=a --myflag=b`, `--myflag=a --myflag=b --myflag=c`, `--myflag=a,b`, and `--myflag=c,b,a`. Exact semantics vary between flags. For example, `--copt` doesn't support multiple values _in the same instance_: `--copt=a,b` produces `["a,b"]` while `--copt=a --copt=b` produces `["a", "b"]` (so `values = { "copt": "a,b" }` matches the former but not the latter). But `--ios_multi_cpus` (for Apple rules) _does_: `-ios_multi_cpus=a,b` and `ios_multi_cpus=a --ios_multi_cpus=b ` both produce `["a", "b"]`. Check flag definitions and test your conditions carefully to verify exact expectations.

- If you need to define conditions that aren't modeled by built-in Bazel flags, use  Starlark-defined flags <https://docs.bazel.build/versions/main/skylark/config.html#user-defined-build-settings>. You can also use `--define`, but this offers weaker support and is not recommended. See here for more discussion.
- Avoid repeating identical `config_setting` definitions in different packages. Instead, reference a common `config_setting` that defined in a canonical package.
- `values`, `define_values`, and `constraint_values` can be used in any combination in the same `config_setting` but at least one must be set for any given `config_setting`.

### Arguments
        Attributes     `name`
`Name; required`

A unique name for this target.
     `constraint_values`
`List of labels; optional; nonconfigurable`
 The minimum set of `constraint_values` that the target platform must specify in order to match this `config_setting`. (The execution platform is not considered here.) Any additional constraint values that the platform has are ignored. See  Configurable Build Attributes <https://docs.bazel.build/versions/main/configurable-attributes.html#platforms> for details.
In the case where two `config_setting`s both match in the same `select`, this attribute is not considered for the purpose of determining whether one of the `config_setting`s is a specialization of the other. In other words, one `config_setting` cannot match a platform more strongly than another.     `define_values`
`Dictionary: String -> String; optional; nonconfigurable`
 The same as `values` but specifically for the `--define` flag.
`--define` is special because its syntax (`--define KEY=VAL`) means `KEY=VAL` is a _value_ from a Bazel flag perspective.

That means:
```go

            config_setting(
                name = "a_and_b",
                values = {
                    "define": "a=1",
                    "define": "b=2",
                })

```

doesn't work because the same key (`define`) appears twice in the dictionary. This attribute solves that problem:
```go

            config_setting(
                name = "a_and_b",
                define_values = {
                    "a": "1",
                    "b": "2",
                })

```

correctly matches `bazel build //foo --define a=1 --define b=2`.
`--define` can still appear in `values` with normal flag syntax, and can be mixed freely with this attribute as long as dictionary keys remain distinct.     `flag_values`
`null; optional; nonconfigurable`
 The same as `values` but for  Starlark-defined flags <https://docs.bazel.build/versions/main/skylark/config.html#user-defined-build-settings>.     `values`
`Dictionary: String -> String; optional; nonconfigurable`
 The set of configuration values that match this rule (expressed as Bazel flags)
This rule inherits the configuration of the configured target that references it in a `select` statement. It is considered to "match" a Bazel invocation if, for every entry in the dictionary, its configuration matches the entry's expected value. For example `values = {"compilation_mode": "opt"}` matches the invocations `bazel build --compilation_mode=opt ...` and `bazel build -c opt ...` on target-configured rules.

For convenience's sake, configuration values are specified as Bazel flags (without the preceding `"--"`). But keep in mind that the two are not the same. This is because targets can be built in multiple configurations within the same build. For example, a host configuration's "cpu" matches the value of `--host_cpu`, not `--cpu`. So different instances of the same `config_setting` may match the same invocation differently depending on the configuration of the rule using them.

If a flag is not explicitly set at the command line, its default value is used. If a key appears multiple times in the dictionary, only the last instance is used. If a key references a flag that can be set multiple times on the command line (e.g. `bazel build --copt=foo --copt=bar --copt=baz ...`), a match occurs if _any_ of those settings match.
