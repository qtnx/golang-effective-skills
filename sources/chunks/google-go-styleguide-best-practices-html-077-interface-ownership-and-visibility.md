---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/best-practices.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Interface ownership and visibility

-
**Do not export interface types unnecessarily:** If an interface is only used internally within a package to satisfy a specific logic flow, keep the interface unexported. Exporting an interface commits you to maintaining that API for external callers.

-
**The consumer defines the interface:** In Go, interfaces generally belong in the package that uses them, not the package that implements them. The consumer should define only the methods they actually use GoTip #78: Minimal Viable Interfaces, adhering to the idea that the bigger the interface, the weaker the abstraction.

There are common scenarios where it often makes sense for the producer (the package providing the logic) to export the interface:

-
**The interface is the product:** When a package’s primary purpose is to provide a common protocol that many different implementations must follow, the producer defines the interface. For example, io.Writer, hash.Hash. The concept of “protocol” includes aspects like documentation about critical behaviors (e.g., expected use case, edge cases, concurrency) that need to be centrally and canonically explicated. Another prominent example of this is generated interfaces from protobuf. It doesn’t abstract a specific behavior, it defines a boundary. Its purpose is to ensure that your server implementation exactly matches the schema defined in the `.proto` file. Here, the interface serves as a rigid legal contract between the service and its clients.

For large systems, if the interface lives inside a huge implementation package, every client is forced to import the entire world just to reference the interface. You may define the interface in a standalone, implementation-free package, avoiding unnecessary symbols and potential circular dependencies. This is also the same philosophy used by generated code from protobuf.

-
**Prevent interface bloat:** In large codebases, maintenance becomes difficult if numerous packages utilize the same `AuthService` while each defining an identical `type Authorizer interface`. While Go often favors a little copying over a little dependency, keep in mind that maintaining perfectly mirrored interfaces (see point above) across many packages can create an unnecessary burden.

-
**Resolve circular dependency:** see an example below.
