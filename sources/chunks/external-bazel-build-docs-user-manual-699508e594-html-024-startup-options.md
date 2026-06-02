---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Miscellaneous commands and options

### Startup options

The options described in this section affect the startup of the Java virtual machine used by Bazel server process, and they apply to all subsequent commands handled by that server. If there is an already running Bazel server and the startup options do not match, it will be restarted.

All of the options described in this section must be specified using the `--key=value` or `--key value` syntax. Also, these options must appear _before_ the name of the Bazel command. Use `startup --key=value` to list these in a `.bazelrc` file.

#### `--output_base=dir`

This option requires a path argument, which must specify a writable directory. Bazel will use this location to write all its output. The output base is also the key by which the client locates the Bazel server. By changing the output base, you change the server which will handle the command.

By default, the output base is derived from the user's login name, and the name of the workspace directory (actually, its MD5 digest), so a typical value looks like: `/var/tmp/google/_bazel_johndoe/d41d8cd98f00b204e9800998ecf8427e`.
 **Note:** The client uses the output base to find the Bazel server instance, so if you specify a different output base in a Bazel command, a different server will be found (or started) to handle the request. It's possible to perform two concurrent builds in the same workspace directory by varying the output base.
For example:

```go

 OUTPUT_BASE=/var/tmp/google/_bazel_johndoe/custom_output_base
% bazel --output_base ${OUTPUT_BASE}1 build //foo  &  bazel --output_base ${OUTPUT_BASE}2 build //bar

```

In this command, the two Bazel commands run concurrently (because of the shell `&amp;` operator), each using a different Bazel server instance (because of the different output bases). In contrast, if the default output base was used in both commands, then both requests would be sent to the same server, which would handle them sequentially: building `//foo` first, followed by an incremental build of `//bar`.
 **Note:** We recommend you do not use an NFS or similar networked file system for the root directory, as the higher access latency will cause noticeably slower builds.
#### `--output_user_root=dir`

Points to the root directory where output and install bases are created. The directory must either not exist or be owned by the calling user. In the past, this was allowed to point to a directory shared among various users but it's not allowed any longer. This may be allowed once issue #11100 <https://github.com/bazelbuild/bazel/issues/11100> is addressed.

If the `--output_base` option is specified, it overrides using `--output_user_root` to calculate the output base.

The install base location is calculated based on `--output_user_root`, plus the MD5 identity of the Bazel embedded binaries.

You can use the `--output_user_root` option to choose an alternate base location for all of Bazel's output (install base and output base) if there is a better location in your filesystem layout.
 **Note:** We recommend you do not use an NFS or similar networked file system for the root directory, as the higher access latency will cause noticeably slower builds.
#### `--server_javabase=dir`

Specifies the Java virtual machine in which _Bazel itself_ runs. The value must be a path to the directory containing a JDK or JRE. It should not be a label. This option should appear before any Bazel command, for example:

```go

  % bazel --server_javabase=/usr/local/buildtools/java/jdk build //foo

```

This flag does _not_ affect the JVMs used by Bazel subprocesses such as applications, tests, tools, and so on. Use build options --javabase or --host_javabase instead.

This flag was previously named `--host_javabase` (sometimes referred to as the 'left-hand side' `--host_javabase`), but was renamed to avoid confusion with the build flag --host_javabase (sometimes referred to as the 'right-hand side' `--host_javabase`).

#### `--host_jvm_args=string`

Specifies a startup option to be passed to the Java virtual machine in which _Bazel itself_ runs. This can be used to set the stack size, for example:

```go

  % bazel --host_jvm_args="-Xss256K" build //foo

```

This option can be used multiple times with individual arguments. Note that setting this flag should rarely be needed. You can also pass a space-separated list of strings, each of which will be interpreted as a separate JVM argument, but this feature will soon be deprecated.

That this does _not_ affect any JVMs used by subprocesses of Bazel: applications, tests, tools, and so on. To pass JVM options to executable Java programs, whether run by `bazel run` or on the command-line, you should use the `--jvm_flags` argument which all `java_binary` and `java_test` programs support. Alternatively for tests, use `bazel test --test_arg=--jvm_flags=foo ...`.

#### `--host_jvm_debug`

This option causes the Java virtual machine to wait for a connection from a JDWP-compliant debugger before calling the main method of _Bazel itself_. This is primarily intended for use by Bazel developers.
 **Note:** This does _not_ affect any JVMs used by subprocesses of Bazel: applications, tests, tools, etc.
#### `--autodetect_server_javabase`

This option causes Bazel to automatically search for an installed JDK on startup, and to fall back to the installed JRE if the embedded JRE isn't available. `--explicit_server_javabase` can be used to pick an explicit JRE to run Bazel with.

#### `--batch`

Batch mode causes Bazel to not use the standard client/server mode, but instead runs a bazel java process for a single command, which has been used for more predictable semantics with respect to signal handling, job control, and environment variable inheritance, and is necessary for running bazel in a chroot jail.

Batch mode retains proper queueing semantics within the same output_base. That is, simultaneous invocations will be processed in order, without overlap. If a batch mode Bazel is run on a client with a running server, it first kills the server before processing the command.

Bazel will run slower in batch mode, or with the alternatives described above. This is because, among other things, the build file cache is memory-resident, so it is not preserved between sequential batch invocations. Therefore, using batch mode often makes more sense in cases where performance is less critical, such as continuous builds.
 **Warning:** `--batch` is sufficiently slower than standard client/server mode. Additionally it might not support all of the features and optimizations which are made possible by a persistent Bazel server. If you're using `--batch` for the purpose of build isolation, you should use the command option `--nokeep_state_after_build`, which guarantees that no incremental in-memory state is kept between builds. In order to restart the Bazel server and JVM after a build, please explicitly do so using the "shutdown" command.
#### `--max_idle_secs=n`

This option specifies how long, in seconds, the Bazel server process should wait after the last client request, before it exits. The default value is 10800 (3 hours). `--max_idle_secs=0` will cause the Bazel server process to persist indefinitely.
 **Note:** this flag is only read if Bazel needs to start a new server. Changing this option will not cause the server to restart.**Note:** system sleep time where a build is not running is counted as idle time.
This option may be used by scripts that invoke Bazel to ensure that they do not leave Bazel server processes on a user's machine when they would not be running otherwise. For example, a presubmit script might wish to invoke `bazel query` to ensure that a user's pending change does not introduce unwanted dependencies. However, if the user has not done a recent build in that workspace, it would be undesirable for the presubmit script to start a Bazel server just for it to remain idle for the rest of the day. By specifying a small value of `--max_idle_secs` in the query request, the script can ensure that _if_ it caused a new server to start, that server will exit promptly, but if instead there was already a server running, that server will continue to run until it has been idle for the usual time. Of course, the existing server's idle timer will be reset.

#### `--[no]shutdown_on_low_sys_mem`

If enabled and `--max_idle_secs` is set to a positive duration, after the build server has been idle for a while, shut down the server when the system is low on memory. Linux only.

In addition to running an idle check corresponding to max_idle_secs, the build server will starts monitoring available system memory after the server has been idle for some time. If the available system memory becomes critically low, the server will exit.

#### `--[no]block_for_lock`

If enabled, Bazel will wait for other Bazel commands holding the server lock to complete before progressing. If disabled, Bazel will exit in error if it cannot immediately acquire the lock and proceed.

Developers might use this in presubmit checks to avoid long waits caused by another Bazel command in the same client.

#### `--io_nice_level=n`

Sets a level from 0-7 for best-effort IO scheduling. 0 is highest priority, 7 is lowest. The anticipatory scheduler may only honor up to priority 4. Negative values are ignored.

#### `--batch_cpu_scheduling`

Use `batch` CPU scheduling for Bazel. This policy is useful for workloads that are non-interactive, but do not want to lower their nice value. See 'man 2 sched_setscheduler'. This policy may provide for better system interactivity at the expense of Bazel throughput.
