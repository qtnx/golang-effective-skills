---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Prefer Realism Over Isolation

Using real implementations for dependencies makes the system under test more realistic  given that  all code in these real implementations will be executed in the test. In contrast, a test that utilizes test doubles isolates the system under test from its dependencies so that the test does not execute code in the dependencies of the system under test.

We prefer realistic tests because they give more confidence that the system under test is working properly. If unit tests rely too much on test doubles, an engineer might need to run integration tests or manually verify that their feature is working as expected in order to gain this same level of confidence. Carrying out these extra tasks can slow down development and can even allow bugs to slip through if engineers skip these tasks entirely when they are too time consuming to carry out compared to running unit tests.

Replacing all dependencies of a class with test doubles  arbitrarily isolates the system under test to the implementation that the author happens to put directly into the class and excludes implementation that happens to be in different classes. However, a good test should be independent of implementation—it should be written in terms of the API being tested rather than in terms of how the implementation is structured.

Using real implementations can cause your test to fail if there is a bug in the real implementation. This is good! You _want_ your tests to fail in such cases because it indicates that your code won’t work properly in production.   Sometimes, a bug in a real implementation can cause a cascade of test failures because other tests that use the real implementation might fail, too. But with good developer tools, such as a Continuous Integration (CI) system, it is usually easy to track down the change that caused the failure.
  Case Study: @DoNotMock
At Google, we’ve seen enough tests that over-rely on mocking frameworks to motivate  the creation of the `@DoNotMock` annotation in Java, which is available as part of the ErrorProne <https://github.com/google/error-prone> static analysis tool.  This annotation is a way for  API owners to declare, "this type should not be mocked because better alternatives exist.”

If an engineer attempts to use a mocking framework to create an instance of a class or interface that has been annotated as `@DoNotMock`, as demonstrated in The @DoNotMock annotation, they will see an error directing them to use a more suitable test strategy, such as a real implementation or a fake. This annotation is most commonly used for value objects that are simple enough to use as-is, as well as for APIs that have well-engineered fakes available.
  Example 13-10. The @DoNotMock annotation
```go

@DoNotMock("Use SimpleQuery.create() instead of mocking.")
public abstract class Query {
  public abstract String getQueryValue();
}
```

Why would an API owner care? In short, it severely constrains the API owner’s ability to make changes to their implementation over time. As we’ll explore later in the chapter, every time a mocking framework is used for stubbing or interaction testing, it duplicates behavior provided by the API.

When the API owner wants to change their API, they might find that it has been mocked thousands or even tens of thousands of times throughout Google’s codebase! These test doubles are very likely to exhibit behavior that violates the API contract of the type being mocked—for instance, returning null for a method that can never return null. Had the tests used the real implementation or a fake, the API owner could make changes to their implementation without first fixing thousands of flawed tests.
