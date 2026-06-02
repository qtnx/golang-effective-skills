---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Variadic options

Using variadic options, exported functions are created which return closures that can be passed to the variadic (`...`) parameter of a function. The function takes as its parameters the values of the option (if any), and the returned closure accepts a mutable reference (usually a pointer to a struct type) that will be updated based on the inputs.

Using variadic options can provide a number of benefits:

- Options take no space at a call-site when no configuration is needed.
- Options are still values, so callers can share them, write helpers, and accumulate them.
- Options can accept multiple parameters (e.g. `cartesian.Translate(dx, dy int) TransformOption`).
- The option functions can return a named type to group options together in godoc.
- Packages can allow (or prevent) third-party packages to define (or from defining) their own options.

**Note:** Using variadic options requires a substantial amount of additional code (see the following example), so it should only be used when the advantages outweigh the overhead.

Here is an example of a function that could be improved:

```go
// Bad:
func EnableReplication(ctx context.Context, config *placer.Config, primaryCells, readonlyCells []string, replicateExisting, overwritePolicies bool, replicationInterval time.Duration, copyWorkers int, healthWatcher health.Watcher) {
  ...
}

```

The example above could be rewritten with variadic options as follows:

```go
// Good:
type replicationOptions struct {
    readonlyCells       []string
    replicateExisting   bool
    overwritePolicies   bool
    replicationInterval time.Duration
    copyWorkers         int
    healthWatcher       health.Watcher
}

// A ReplicationOption configures EnableReplication.
type ReplicationOption func(*replicationOptions)

// ReadonlyCells adds additional cells that should additionally
// contain read-only replicas of the data.
//
// Passing this option multiple times will add additional
// read-only cells.
//
// Default: none
func ReadonlyCells(cells ...string) ReplicationOption {
    return func(opts *replicationOptions) {
        opts.readonlyCells = append(opts.readonlyCells, cells...)
    }
}

// ReplicateExisting controls whether files that already exist in the
// primary cells will be replicated.  Otherwise, only newly-added
// files will be candidates for replication.
//
// Passing this option again will overwrite earlier values.
//
// Default: false
func ReplicateExisting(enabled bool) ReplicationOption {
    return func(opts *replicationOptions) {
        opts.replicateExisting = enabled
    }
}

// ... other options ...

// DefaultReplicationOptions control the default values before
// applying options passed to EnableReplication.
var DefaultReplicationOptions = []ReplicationOption{
    OverwritePolicies(true),
    ReplicationInterval(12 * time.Hour),
    CopyWorkers(10),
}

func EnableReplication(ctx context.Context, config *placer.Config, primaryCells []string, opts ...ReplicationOption) {
    var options replicationOptions
    for _, opt := range DefaultReplicationOptions {
        opt(&options)
    }
    for _, opt := range opts {
        opt(&options)
    }
}

```

The function can then be called in a different package:

```go
// Good:
func foo(ctx context.Context) {
    // Complex call:
    storage.EnableReplication(ctx, config, []string{"po", "is", "ea"},
        storage.ReadonlyCells("ix", "gg"),
        storage.OverwritePolicies(true),
        storage.ReplicationInterval(1*time.Hour),
        storage.CopyWorkers(100),
        storage.HealthWatcher(watcher),
    )

    // Simple call:
    storage.EnableReplication(ctx, config, []string{"po", "is", "ea"})
}

```

Prefer this option when many of the following apply:

- Most callers will not need to specify any options.
- Most options are used infrequently.
- There are a large number of options.
- Options require arguments.
- Options could fail or be set incorrectly (in which case the option function returns an `error`).
- Options require a lot of documentation that can be hard to fit in a struct.
- Users or other packages can provide custom options.

Options in this style should accept parameters rather than using presence to signal their value; the latter can make dynamic composition of arguments much more difficult. For example, binary settings should accept a boolean (e.g. `rpc.FailFast(enable bool)` is preferable to `rpc.EnableFailFast()`). An enumerated option should accept an enumerated constant (e.g. `log.Format(log.Capacitor)` is preferable to `log.CapacitorFormat()`). The alternative makes it much more difficult for users who must programmatically choose which options to pass; such users are forced to change the actual composition of the parameters rather than simply changing the arguments to the options. Don’t assume that all users will know the full set of options statically.

In general, options should be processed in order. If there is a conflict or if a non-cumulative option is passed multiple times, the last argument should win.

The parameter to the option function is generally unexported in this pattern, to restrict the options to being defined only within the package itself. This is a good default, though there may be times when it is appropriate to allow other packages to define options.

See Rob Pike’s original blog post and Dave Cheney’s talk for a more in-depth look at how these options can be used.
