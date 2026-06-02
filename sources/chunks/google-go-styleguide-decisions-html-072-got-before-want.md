---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.html"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Got before want

Test outputs should include the actual value that the function returned before printing the value that was expected. A standard format for printing test outputs is `YourFunc(%v) = %v, want %v`. Where you would write “actual” and “expected”, prefer using the words “got” and “want”, respectively.

For diffs, directionality is less apparent, and as such it is important to include a key to aid in interpreting the failure. See the section on printing diffs. Whichever diff order you use in your failure messages, you should explicitly indicate it as a part of the failure message, because existing code is inconsistent about the ordering.
