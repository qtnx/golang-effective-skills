---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

## Write Clear Failure Messages

One last aspect of clarity has to do not with how a test is written, but with what an engineer sees when it fails.    In an ideal world, an engineer could diagnose a problem just from reading its failure message in a log or report without ever having to look at the test itself. A good failure message contains much the same information as the test’s name: it should clearly express the desired outcome, the actual outcome, and any relevant parameters.

Here’s an example of a bad failure message:

```go

Test failed: account is closed
```

Did the test fail because the account was closed, or was the account expected to be closed and the test failed because it wasn’t? A better failure message clearly distinguishes the expected from the actual state and gives more context about the result:

```go

Expected an account in state CLOSED, but got account:
    <{name: "my-account", state: "OPEN"}
```

Good libraries can help make it easier to write useful failure messages.   Consider the assertions in An assertion using the Truth library in a Java test, the first of which  uses classical JUnit asserts, and the second of which uses Truth <https://truth.dev>, an assertion library developed by Google:
  Example 12-17. An assertion using the Truth library
```go

Set<String> colors = ImmutableSet.of("red", "green", "blue");
assertTrue(colors.contains("orange"));  // JUnit
assertThat(colors).contains("orange");  // Truth
```

Because the first assertion only receives a Boolean value, it is only able to give a generic error message like "expected <true> but was <false>," which isn’t very informative in a failing test output. Because the second assertion explicitly receives the subject of the assertion, it is able to give a much more useful error message <https://oreil.ly/RFUEN>: "AssertionError: <[red, green, blue]> should have contained <orange>."

Not all  languages have  such helpers available, but it should always be possible to manually specify the important information in the failure message. For example, test assertions in Go conventionally look like A test assertion in Go.
  Example 12-18. A test assertion in Go
```go

result := Add(2, 3)
if result != 5 {
  t.Errorf("Add(2, 3) = %v, want %v", result, 5)
}
```

# Tests and Code Sharing: DAMP, Not DRY

One final  aspect of  writing clear tests and avoiding brittleness has to do with code sharing.   Most software attempts to achieve a principle called DRY—"Don’t Repeat Yourself." DRY states  that software is easier to maintain if every concept is canonically represented in one place and code duplication is kept to a minimum. This approach is especially valuable in making changes easier because an engineer needs to update only one piece of code rather than tracking down multiple references. The downside to such consolidation is that it can make code unclear, requiring readers to follow chains of references to understand what the code is doing.

In normal production code, that downside is usually a small price to pay for making code easier to change and work with. But this cost/benefit analysis plays out a little differently in the context of test code. Good tests are designed to be stable, and in fact you usually _want_ them to break when the system being tested changes. So DRY doesn’t have quite as much benefit when it comes to test code. At the same time, the costs of complexity are greater for tests: production code has the benefit of a test suite to ensure that it keeps working as it becomes complex, whereas tests must stand by themselves, risking bugs if they aren’t self-evidently correct. As mentioned earlier, something has gone wrong if tests start becoming complex enough that it feels like they need their own tests to ensure that they’re working properly. 

Instead of  being completely DRY, test code should  often strive to be DAMP <https://oreil.ly/5VPs2>—that is, to promote "Descriptive And Meaningful Phrases." A little bit of duplication is OK in tests so long as that duplication makes the test simpler and clearer.  To illustrate, A test that is too DRY presents some tests that are far too DRY.
  Example 12-19. A test that is too DRY
```go

@Test
public void shouldAllowMultipleUsers() {
  List<User> users = createUsers(false, false);
  Forum forum = createForumAndRegisterUsers(users);
  validateForumAndUsers(forum, users);
}

@Test
public void shouldNotAllowBannedUsers() {
  List<User> users = createUsers(true);
  Forum forum = createForumAndRegisterUsers(users);
  validateForumAndUsers(forum, users);
}

// Lots more tests...

private static List<User> createUsers(boolean... banned) {
  List<User> users = new ArrayList<>();
  for (boolean isBanned : banned) {
    users.add(newUser()
        .setState(isBanned ? State.BANNED : State.NORMAL)
        .build());
  }
  return users;
}

private static Forum createForumAndRegisterUsers(List<User> users) {
  Forum forum = new Forum();
  for (User user : users) {
    try {
      forum.register(user);
    } catch(BannedUserException ignored) {}
  }
  return forum;
}

private static void validateForumAndUsers(Forum forum, List<User> users) {
  assertThat(forum.isReachable()).isTrue();
  for (User user : users) {
    assertThat(forum.hasRegisteredUser(user))
        .isEqualTo(user.getState() == State.BANNED);
  }
}
```

The problems  in this code should be apparent based on the previous discussion of clarity. For one, although the test bodies are very concise, they are not complete: important details are hidden away in helper methods that the reader can’t see without having to scroll to a completely different part of the file.   Those helpers are also full of logic that makes them more difficult to verify at a glance (did you spot the bug?). The test becomes much clearer when it’s rewritten to use DAMP, as shown in Tests should be DAMP.
  Example 12-20. Tests should be DAMP
```go

@Test
public void shouldAllowMultipleUsers() {
  User user1 = newUser().setState(State.NORMAL).build();
  User user2 = newUser().setState(State.NORMAL).build();

  Forum forum = new Forum();
  forum.register(user1);
  forum.register(user2);

  assertThat(forum.hasRegisteredUser(user1)).isTrue();
  assertThat(forum.hasRegisteredUser(user2)).isTrue();
}

@Test
public void shouldNotRegisterBannedUsers() {
  User user = newUser().setState(State.BANNED).build();

  Forum forum = new Forum();
  try {
    forum.register(user);
  } catch(BannedUserException ignored) {}

  assertThat(forum.hasRegisteredUser(user)).isFalse();
}
```

These tests have more duplication, and the test bodies are a bit longer, but the extra verbosity is worth it. Each individual test is far more meaningful and can be understood entirely without leaving the test body. A reader of these tests can feel confident that the tests do what they claim to do and aren’t hiding any bugs.

DAMP is not a replacement for DRY; it is complementary to it.   Helper methods and test infrastructure can still help make tests clearer by making them more concise, factoring out repetitive steps whose details aren’t relevant to the particular behavior being tested. The important point is that such refactoring should be done with an eye toward making tests more descriptive and meaningful, and not solely in the name of reducing repetition. The rest of this section will explore common patterns for sharing code across tests.
