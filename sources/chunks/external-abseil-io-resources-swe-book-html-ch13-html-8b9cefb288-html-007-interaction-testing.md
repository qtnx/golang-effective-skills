---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Interaction Testing

_Interaction testing_ <https://oreil.ly/zGfFn> is a way to validate _how_ a function is called without actually calling the implementation of the function.   A test should fail if a function isn’t called the correct way—for example, if the function isn’t called at all, it’s called too many times, or it’s called with the wrong arguments.

Interaction testing presents an instance of interaction testing. The `verify(...)` method from the Mockito mocking framework is used to validate that `lookupUser()` is called as expected.
  Example 13-9. Interaction testing
```go

// Pass in a test double that was created by a mocking framework.
AccessManager accessManager = new AccessManager(**mockAuthorizationService**);
accessManager.userHasAccess(USER_ID);

// The test will fail if accessManager.userHasAccess(USER_ID) didn’t call
// mockAuthorizationService.lookupUser(USER_ID).
verify(**mockAuthorizationService**).lookupUser(USER_ID);
```

Similar to stubbing, interaction testing is typically done through mocking frameworks.  This reduces boilerplate compared to manually creating new classes that contain code to keep track of how often a function is called and which arguments were passed in.

Interaction testing is sometimes called _mocking_ <https://oreil.ly/IfMoR>. We avoid this terminology in this chapter because it can be confused with mocking frameworks, which can be used for stubbing as well as for interaction testing. 

As discussed later in this chapter, interaction testing is useful in certain situations but should be avoided when possible because overuse can easily result in brittle tests. 

# Real Implementations

Although test doubles can be  invaluable testing tools, our first choice for tests is to use the  real implementations of the system under test’s dependencies; that is, the same implementations that are used in production code. Tests have higher fidelity when they execute code as it will be executed in production, and using real implementations helps accomplish this.

At Google, the preference for real implementations developed over time as we saw that overuse of mocking frameworks had a tendency to pollute tests with repetitive code that got out of sync with the real implementation and made refactoring difficult. We’ll look at this topic in more detail later in this chapter.

Preferring real implementations  in tests is known as _classical testing_ <https://oreil.ly/OWw7h>. There is also a style of testing known as _mockist testing_, in which the preference is to use mocking frameworks instead of real implementations.  Even though some people in the software industry practice mockist testing (including the creators of the first mocking frameworks <https://oreil.ly/_QWy7>), at Google, we have found that this style of testing is difficult to scale. It requires engineers to follow strict guidelines when designing the system under test <http://jmock.org/oopsla2004.pdf>, and the default behavior of most engineers at Google has been to write code in a way that is more suitable for the classical testing style.
