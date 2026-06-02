---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Best Practices for Interaction Testing

When performing  interaction testing, following these practices can reduce some of the impact of the aforementioned downsides.

### Prefer to perform interaction testing only for state-changing functions

When a system under  test calls a function on a dependency, that  call falls into one of two categories:
  State-changing Functions that have side effects on the world outside the system under test. Examples: `sendEmail()`, `saveRecord()`, `logAccess()`. Non-state-changing Functions that don’t  have side effects; they return information about the world outside the system under test and don’t modify anything. Examples: `getUser()`, `findResults()`, `readFile()`.
In general, you should perform interaction testing only for functions that are state-changing. Performing interaction testing for non-state-changing functions is usually redundant given that the system under test will use the return value of the function to do other work that you can assert. The interaction itself is not an important detail for correctness, because it has no side effects.

Performing interaction testing for non-state-changing functions makes your test brittle because you’ll need to update the test anytime the pattern of interactions changes. It also makes the test less readable given that the additional assertions make it more difficult to determine which assertions are important for ensuring correctness of the code. By contrast, state-changing interactions represent something useful that your code is doing to change state somewhere else.

State-changing and non-state-changing interactions demonstrates interaction testing on both state-changing and non-state-changing functions.
  Example 13-17. State-changing and non-state-changing interactions
```go

@Test public void grantUserPermission() {
  UserAuthorizer userAuthorizer =
      new UserAuthorizer(**mockUserService**, **mockPermissionDatabase**);
  when(**mockPermissionService**.**getPermission**(FAKE_USER)).thenReturn(EMPTY);

  // Call the system under test.
  userAuthorizer.grantPermission(USER_ACCESS);

  // addPermission() is state-changing, so it is reasonable to perform
  // interaction testing to validate that it was called.
  verify(**mockPermissionDatabase**).**addPermission**(FAKE_USER, USER_ACCESS);

  // getPermission() is non-state-changing, so this line of code isn’t
  // needed. One clue that interaction testing may not be needed:
  // getPermission() was already stubbed earlier in this test.
  verify(**mockPermissionDatabase**).**getPermission**(FAKE_USER);
}
```

### Avoid overspecification

In Unit Testing, we discuss why it is useful to test behaviors rather than methods. This means that a test method should focus  on verifying one behavior of a method or class rather than trying  to verify multiple behaviors in a single test.

When performing interaction testing, we should aim to apply the same principle by avoiding overspecifying which functions and arguments are validated. This leads to tests that are clearer and more concise. It also leads to tests that are resilient to changes made to behaviors that are outside the scope of each test, so fewer tests will fail if a change is made to a way a function is called.

Overspecified interaction tests illustrates interaction testing with overspecification. The intention of the test is to validate that the user’s name is included in the greeting prompt, but the test will fail if unrelated behavior is changed.
  Example 13-18. Overspecified interaction tests
```go

@Test public void displayGreeting_renderUserName() {
  when(mockUserService.getUserName()).thenReturn("Fake User");
  userGreeter.displayGreeting(); // Call the system under test.

  // The test will fail if any of the arguments to setText() are changed.
  verify(**userPrompt**).**setText**("Fake User", "Good morning!", "Version 2.1");

  // The test will fail if setIcon() is not called, even though this
  // behavior is incidental to the test since it is not related to
  // validating the user name.
  verify(**userPrompt**).**setIcon**(IMAGE_SUNSHINE);
}
```

Well-specified interaction tests illustrates interaction testing with more care in specifying relevant arguments and functions. The behaviors being tested are split into separate tests, and each test validates the minimum amount necessary for ensuring  the behavior it is testing is correct.
  Example 13-19. Well-specified interaction tests
```go

@Test public void displayGreeting_renderUserName() {
  when(mockUserService.getUserName()).thenReturn("Fake User");
  userGreeter.displayGreeting(); // Call the system under test.
  verify(**userPrompter**).**setText**(eq("Fake User"), any(), any());
}
@Test public void displayGreeting_timeIsMorning_useMorningSettings() {
  setTimeOfDay(TIME_MORNING);
  userGreeter.displayGreeting(); // Call the system under test.
  verify(**userPrompt**).**setText**(any(), eq("Good morning!"), any());
  verify(**userPrompt**).**setIcon**(IMAGE_SUNSHINE);
}
```

# Conclusion

We’ve  learned that  test doubles are crucial to engineering velocity because they can help comprehensively test your code and ensure that your tests run fast. On the other hand, misusing them can be a major drain on productivity because they can lead to tests that are unclear, brittle, and less effective. This is why it’s important for engineers to understand the best practices for how to effectively apply test doubles.

There is often no exact answer regarding whether to use a real implementation or a test double, or which test double technique to use. An engineer might need to make some trade-offs when deciding the proper approach for their use case.

Although test doubles are great for working around dependencies that are difficult to use in tests, if you want to maximize confidence in your code, at some point you still want to exercise these dependencies in tests. The next chapter will cover larger-scope testing, for which these dependencies are used regardless of their suitability for unit tests; for example, even if they are slow or nondeterministic.

# TL;DRs

-
A real implementation should be preferred over a test double.

-
A fake is often the ideal solution if a real implementation can’t be used in a test.

-
Overuse of stubbing leads to tests that are unclear and brittle.

-
Interaction testing should be avoided when possible: it leads to tests that are brittle because it exposes implementation  details of the system under test.

CC BY-NC-ND 4.0 <https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode>
