# Checklist

- Can the caller handle the failure, and does it get enough context?
- Is error identity intentionally exposed or intentionally hidden?
- Is `%w` used only when inspection matters?
- Are error strings lower-case and clean?
- Is each error logged at most once with useful context?
- Are panics limited to programmer errors or invariant violations?
- Do tests assert error semantics when public behavior depends on them?
