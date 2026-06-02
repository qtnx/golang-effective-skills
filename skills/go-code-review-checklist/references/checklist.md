# Checklist

- Does the changed code compile and pass relevant tests?
- Has `gofmt` been applied?
- Does public API read correctly from the call site?
- Are error paths returned, wrapped, logged, and tested at the right layer?
- Does cancellation or cleanup happen when work can block or outlive a call?
- Do tests cover the main behavior and important failure paths?
- Are test failure messages useful?
- Is each new dependency, abstraction, or package boundary justified?
- Is any performance change backed by measurement?
