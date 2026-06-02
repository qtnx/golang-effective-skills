---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

## Test State, Not Interactions

Another way that tests commonly  depend on implementation details involves not which methods of the system the test calls, but how the results of those calls are verified.  In general, there are two ways to verify that a system under test behaves as expected.  With _state testing_, you observe the system itself to see what it looks like after invoking with it. With _interaction testing_, you instead check that the system took an expected sequence of actions on its collaborators in response to invoking it <https://oreil.ly/3S8AL>. Many tests will perform a combination of state and interaction validation.

Interaction tests tend to be more brittle than state tests for the same reason that it’s more brittle to test a private method than to test a public method: interaction tests check _how_ a system arrived at its result, whereas usually you should care only _what_ the result is. A brittle interaction test illustrates a test that uses a test double (explained further in Test Doubles) to verify how  a system interacts with a database.
  Example 12-4. A brittle interaction test
```go

@Test
public void shouldWriteToDatabase() {
  accounts.createUser("foobar");
  verify(database).put("foobar");
}
```

The test verifies that a specific call was made against a database API, but there are a couple different ways it could go wrong:

-
If a bug in the system under test causes the record to be deleted from the database shortly after it was written, the test will pass even though we would have wanted it to fail.

-
If the system under test is refactored to call a slightly different API to write an equivalent record, the test will fail even though we would have wanted it to pass.

It’s much less brittle to directly test against the state of the system, as demonstrated in Testing against state.
  Example 12-5. Testing against state
```go

@Test
public void shouldCreateUsers() {
  accounts.createUser("foobar");
  assertThat(accounts.getUser("foobar")).isNotNull();
}
```

This test more accurately expresses what we care about: the state of the system under test after interacting with it.

The most common reason for problematic interaction tests is an over reliance on mocking frameworks.  These frameworks make it easy to create test doubles that record and verify every call made against them, and to use those doubles in place of real objects in tests. This strategy leads directly to brittle interaction tests, and so we tend to prefer the use of real objects in favor of mocked objects, as long as the real objects are fast and deterministic.
 Note
For a more extensive discussion of test doubles and mocking frameworks, when they should be used, and safer alternatives, see Test Doubles.

# Writing Clear Tests

Sooner or later, even if we’ve completely  avoided  brittleness, our tests will fail. Failure  is a good  thing—test failures provide useful signals to engineers, and are one of the main ways that a unit test provides value.

  Test failures happen for one of two reasons:3

-
The system under test has a problem or is incomplete. This result is exactly what tests are designed for: alerting you to bugs so that you can fix them.

-
The test itself is flawed. In this case, nothing is wrong with the system under test, but the test was specified incorrectly. If this was an existing test rather than one that you just wrote, this means that the test is brittle. The previous section discussed how to avoid brittle tests, but it’s rarely possible to eliminate them entirely.

When a test fails, an engineer’s first job is to identify which of these cases the failure falls into and then to diagnose the actual problem. The speed at which the engineer can do so depends on the test’s _clarity_. A clear test is one whose purpose for existing and reason for failing is immediately clear to the engineer diagnosing a failure. Tests fail to achieve clarity when their reasons for failure aren’t obvious or when it’s difficult to figure out why they were originally written. Clear tests also bring other benefits, such as documenting the system under test and more easily serving as a basis for new tests.

Test clarity becomes significant over time. Tests will often outlast the engineers who wrote them, and the requirements and understanding of a system will shift subtly as it ages. It’s entirely possible that a failing test might have been written years ago by an engineer no longer on the team, leaving no way to figure out its purpose or how to fix it. This stands in contrast with unclear production code, whose purpose you can usually determine with enough effort by looking at what calls it and what breaks when it’s removed. With an unclear test, you might never understand its purpose, since removing the test will have no effect other than (potentially) introducing a subtle hole in test coverage.

In the worst case, these obscure tests just end up getting deleted when engineers can’t figure out how to fix them. Not only does removing such tests introduce a hole in test coverage, but it also indicates that the test has been providing zero value for perhaps the entire period it has existed (which could have been years).

For a test suite to scale and be useful over time, it’s important that each individual test in that suite be as clear as possible. This section explores techniques and ways of thinking about tests to achieve clarity.
