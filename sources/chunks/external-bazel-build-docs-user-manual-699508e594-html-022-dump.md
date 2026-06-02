---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Miscellaneous commands and options

### `dump`

The `dump` command prints to stdout a dump of the internal state of the Bazel server. This command is intended primarily for use by Bazel developers, so the output of this command is not specified, and is subject to change.

By default, command will just print help message outlining possible options to dump specific areas of the Bazel state. In order to dump internal state, at least one of the options must be specified.

Following options are supported:

- `--action_cache` dumps action cache content.
- `--packages` dumps package cache content.
- `--skyframe` dumps state of internal Bazel dependency graph.
- `--rules` dumps rule summary for each rule and aspect class, including counts and action counts. This includes both native and Starlark rules. If memory tracking is enabled, then the rules' memory consumption is also printed.
- `--skylark_memory` dumps a pprof <https://github.com/google/pprof> compatible .gz file to the specified path. You must enable memory tracking for this to work.

#### Memory tracking

Some `dump` commands require memory tracking. To turn this on, you have to pass startup flags to Bazel:

- `--host_jvm_args=-javaagent:$BAZEL/third_party/allocation_instrumenter/java-allocation-instrumenter-3.3.4.jar`
- `--host_jvm_args=-DRULE_MEMORY_TRACKER=1`

The java-agent is checked into Bazel at `third_party/allocation_instrumenter/java-allocation-instrumenter-3.3.4.jar`, so make sure you adjust `$BAZEL` for where you keep your Bazel repository.

Do not forget to keep passing these options to Bazel for every command or the server will restart.

Example:

```go

    % bazel --host_jvm_args=-javaagent:$BAZEL/third_party/allocation_instrumenter/java-allocation-instrumenter-3.3.4.jar \
    --host_jvm_args=-DRULE_MEMORY_TRACKER=1 \
    build --nobuild <targets>

    # Dump rules
    % bazel --host_jvm_args=-javaagent:$BAZEL/third_party/allocation_instrumenter/java-allocation-instrumenter-3.3.4.jar \
    --host_jvm_args=-DRULE_MEMORY_TRACKER=1 \
    dump --rules

    # Dump Starlark heap and analyze it with pprof
    % bazel --host_jvm_args=-javaagent:$BAZEL/third_party/allocation_instrumenter/java-allocation-instrumenter-3.3.4.jar \
    --host_jvm_args=-DRULE_MEMORY_TRACKER=1 \
    dump --skylark_memory=$HOME/prof.gz
    % pprof -flame $HOME/prof.gz

```
