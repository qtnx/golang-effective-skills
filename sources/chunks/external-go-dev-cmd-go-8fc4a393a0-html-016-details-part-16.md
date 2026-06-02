---
source_name: "External Linked Documentation"
source_url: "https://go.dev/cmd/go/"
source_path: "sources/raw/external/go-dev-cmd-go-8fc4a393a0.html"
license_ref: ""
---

# golang.org/x/text/language

The version control command restrictions only apply when using direct version control access to download code. When downloading modules from a proxy, 'go get' uses the proxy protocol instead, which is always permitted. By default, the 'go get' command uses the Go module mirror (proxy.golang.org) for public packages and only falls back to version control for private packages or when the mirror refuses to serve a public package (typically for legal reasons). Therefore, clients can still access public code served from Bazaar, Fossil, or Subversion repositories by default, because those downloads use the Go module mirror, which takes on the security risk of running the version control commands using a custom sandbox.

The GOVCS variable can be used to change the allowed version control systems for specific packages (identified by a module or import path). The GOVCS variable applies when building package in both module-aware mode and GOPATH mode. When using modules, the patterns match against the module path. When using GOPATH, the patterns match against the import path corresponding to the root of the version control repository.

The general form of the GOVCS setting is a comma-separated list of pattern:vcslist rules. The pattern is a glob pattern that must match one or more leading elements of the module or import path. The vcslist is a pipe-separated list of allowed version control commands, or "all" to allow use of any known command, or "off" to disallow all commands. Note that if a module matches a pattern with vcslist "off", it may still be downloaded if the origin server uses the "mod" scheme, which instructs the go command to download the module using the GOPROXY protocol. The earliest matching pattern in the list applies, even if later patterns might also match.

For example, consider:

```go
GOVCS=github.com:git,evil.com:off,*:git|hg

```

With this setting, code with a module or import path beginning with github.com/ can only use git; paths on evil.com cannot use any version control command, and all other paths (* matches everything) can use only git or hg.

The special patterns "public" and "private" match public and private module or import paths. A path is private if it matches the GOPRIVATE variable; otherwise it is public.

If no rules in the GOVCS variable match a particular module or import path, the 'go get' command applies its default rule, which can now be summarized in GOVCS notation as 'public:git|hg,private:all'.

To allow unfettered use of any version control system for any package, use:

```go
GOVCS=*:all

```

To disable all use of version control, use:

```go
GOVCS=*:off

```

The 'go env -w' command (see 'go help env') can be used to set the GOVCS variable for future go command invocations.
