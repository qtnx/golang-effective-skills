---
source_name: "External Linked Documentation"
source_url: "https://docs.bazel.build/versions/main/be/general.html"
source_path: "sources/raw/external/docs-bazel-build-versions-main-be-general-html-1d20475b8b.html"
license_ref: ""
---

##  genrule
```go
genrule(name, srcs, outs, cmd, cmd_bash, cmd_bat, cmd_ps, compatible_with, deprecation, distribs, exec_compatible_with, exec_properties, exec_tools, executable, features, licenses, local, message, output_licenses, output_to_bindir, restricted_to, tags, target_compatible_with, testonly, toolchains, tools, visibility)
```
A `genrule` generates one or more files using a user-defined Bash command.
 Genrules are generic build rules that you can use if there's no specific rule for the task. For example, you could run a Bash one-liner. If however you need to compile C++ files, stick to the existing `cc_*` rules, because all the heavy lifting has already been done for you.
 Do not use a genrule for running tests. There are special dispensations for tests and test results, including caching policies and environment variables. Tests generally need to be run after the build is complete and on the target architecture, whereas genrules are executed during the build and on the host architecture (the two may be different). If you need a general purpose testing rule, use `sh_test`.
#### Cross-compilation Considerations
 _See the user manual for more info about cross-compilation._
 While genrules run during a build, their outputs are often used after the build, for deployment or testing. Consider the example of compiling C code for a microcontroller: the compiler accepts C source files and generates code that runs on a microcontroller. The generated code obviously cannot run on the CPU that was used for building it, but the C compiler (if compiled from source) itself has to.
 The build system uses the host configuration to describe the machine(s) on which the build runs and the target configuration to describe the machine(s) on which the output of the build is supposed to run. It provides options to configure each of these and it segregates the corresponding files into separate directories to avoid conflicts.
 For genrules, the build system ensures that dependencies are built appropriately: `srcs` are built (if necessary) for the _target_ configuration, `tools` are built for the _host_ configuration, and the output is considered to be for the _target_ configuration. It also provides  "Make" variables that genrule commands can pass to the corresponding tools.
 It is intentional that genrule defines no `deps` attribute: other built-in rules use language-dependent meta information passed between the rules to automatically determine how to handle dependent rules, but this level of automation is not possible for genrules. Genrules work purely at the file and runfiles level.
#### Special Cases
 _Host-host compilation_: in some cases, the build system needs to run genrules such that the output can also be executed during the build. If for example a genrule builds some custom compiler which is subsequently used by another genrule, the first one has to produce its output for the host configuration, because that's where the compiler will run in the other genrule. In this case, the build system does the right thing automatically: it builds the `srcs` and `outs` of the first genrule for the host configuration instead of the target configuration. See the user manual for more info.
 _JDK & C++ Tooling_: to use a tool from the JDK or the C++ compiler suite, the build system provides a set of variables to use. See "Make" variable for details.
#### Genrule Environment
 The genrule command is executed by a Bash shell that is configured to fail when a command or a pipeline fails, using `set -e -o pipefail`.
 The build tool executes the Bash command in a sanitized process environment that defines only core variables such as `PATH`, `PWD`, `TMPDIR`, and a few others. To ensure that builds are reproducible, most variables defined in the user's shell environment are not passed though to the genrule's command. However, Bazel (but not Bazel) passes through the value of the user's `PATH` environment variable. Any change to the value of `PATH` will cause Bazel to re-execute the command on the next build.
 A genrule command should not access the network except to connect processes that are children of the command itself, though this is not currently enforced.
 The build system automatically deletes any existing output files, but creates any necessary parent directories before it runs a genrule. It also removes any output files in case of a failure.
#### General Advice
- Do ensure that tools run by a genrule are deterministic and hermetic. They should not write timestamps to their output, and they should use stable ordering for sets and maps, as well as write only relative file paths to the output, no absolute paths. Not following this rule will lead to unexpected build behavior (Bazel not rebuilding a genrule you thought it would) and degrade cache performance.
- Do use `$(location)` extensively, for outputs, tools and sources. Due to the segregation of output files for different configurations, genrules cannot rely on hard-coded and/or absolute paths.
- Do write a common Starlark macro in case the same or very similar genrules are used in multiple places. If the genrule is complex, consider implementing it in a script or as a Starlark rule. This improves readability as well as testability.
- Do make sure that the exit code correctly indicates success or failure of the genrule.
- Do not write informational messages to stdout or stderr. While useful for debugging, this can easily become noise; a successful genrule should be silent. On the other hand, a failing genrule should emit good error messages.
- `$$` evaluates to a `$`, a literal dollar-sign, so in order to invoke a shell command containing dollar-signs such as `ls $(dirname $x)`, one must escape it thus: `ls $$(dirname $$x)`.
- Avoid creating symlinks and directories. Bazel doesn't copy over the directory/symlink structure created by genrules and its dependency checking of directories is unsound.
- When referencing the genrule in other rules, you can use either the genrule's label or the labels of individual output files. Sometimes the one approach is more readable, sometimes the other: referencing outputs by name in a consuming rule's `srcs` will avoid unintentionally picking up other outputs of the genrule, but can be tedious if the genrule produces many outputs.
#### Examples
 This example generates `foo.h`. There are no sources, because the command doesn't take any input. The "binary" run by the command is a perl script in the same package as the genrule.
```go
genrule(
    name = "foo",
    srcs = [],
    outs = ["foo.h"],
    cmd = "./$(location create_foo.pl) > \"$@\"",
    tools = ["create_foo.pl"],
)
```
 The following example shows how to use a `filegroup`  and the outputs of another `genrule`. Note that using `$(SRCS)` instead of explicit `$(location)` directives would also work; this example uses the latter for sake of demonstration.
```go
genrule(
    name = "concat_all_files",
    srcs = [
        "//some:files",  # a filegroup with multiple files in it ==> $(location**s**)
        "//other:gen",   # a genrule with a single output ==> $(location)
    ],
    outs = ["concatenated.txt"],
    cmd = "cat $(locations //some:files) $(location //other:gen) > $@",
)
```
