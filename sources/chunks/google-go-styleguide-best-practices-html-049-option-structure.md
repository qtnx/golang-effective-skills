---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Option structure

An option structure is a struct type that collects some or all of the arguments of a function or method, that is then passed as the last argument to the function or method. (The struct should be exported only if it is used in an exported function.)

Using an option structure has a number of benefits:

- The struct literal includes both fields and values for each argument, which makes them self-documenting and harder to swap.
- Irrelevant or “default” fields can be omitted.
- Callers can share the option struct and write helpers to operate on it.
- Structs provide cleaner per-field documentation than function arguments.
- Option structs can grow over time without impacting call-sites.

Here is an example of a function that could be improved:

```go
// Bad:
func EnableReplication(ctx context.Context, config *replicator.Config, primaryRegions, readonlyRegions []string, replicateExisting, overwritePolicies bool, replicationInterval time.Duration, copyWorkers int, healthWatcher health.Watcher) {
    // ...
}

```

The function above could be rewritten with an option structure as follows:

```go
// Good:
type ReplicationOptions struct {
    Config              *replicator.Config
    PrimaryRegions      []string
    ReadonlyRegions     []string
    ReplicateExisting   bool
    OverwritePolicies   bool
    ReplicationInterval time.Duration
    CopyWorkers         int
    HealthWatcher       health.Watcher
}

func EnableReplication(ctx context.Context, opts ReplicationOptions) {
    // ...
}

```

The function can then be called in a different package:

```go
// Good:
func foo(ctx context.Context) {
    // Complex call:
    storage.EnableReplication(ctx, storage.ReplicationOptions{
        Config:              config,
        PrimaryRegions:      []string{"us-east1", "us-central2", "us-west3"},
        ReadonlyRegions:     []string{"us-east5", "us-central6"},
        OverwritePolicies:   true,
        ReplicationInterval: 1 * time.Hour,
        CopyWorkers:         100,
        HealthWatcher:       watcher,
    })

    // Simple call:
    storage.EnableReplication(ctx, storage.ReplicationOptions{
        Config:         config,
        PrimaryRegions: []string{"us-east1", "us-central2", "us-west3"},
    })
}

```

**Note:** Contexts are never included in option structs.

This option is often preferred when some of the following apply:

- All callers need to specify one or more of the options.
- A large number of callers need to provide many options.
- The options are shared between multiple functions that the user will call.
