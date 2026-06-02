---
source_name: "Uber Go Style Guide"
source_url: "https://github.com/uber-go/guide/blob/master/style.md"
source_path: "sources/raw/uber-go-guide/style.md"
license_ref: "sources/licenses/uber-go-guide-LICENSE.txt"
---

### Use `"time"` to handle time

Time is complicated. Incorrect assumptions often made about time include the
following.

1. A day has 24 hours
2. An hour has 60 minutes
3. A week has 7 days
4. A year has 365 days
5. [And a lot more](https://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time)

For example, *1* means that adding 24 hours to a time instant will not always
yield a new calendar day.

Therefore, always use the [`"time"`](https://pkg.go.dev/time) package when dealing with time because it
helps deal with these incorrect assumptions in a safer, more accurate manner.
