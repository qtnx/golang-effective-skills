---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

## Test via Public APIs

Now that we  understand  our goal, let’s look at some practices for making sure that tests don’t need to change unless the requirements of the system being tested change. By far the most important way to ensure this is to write tests that invoke the system being tested in the same way its users would; that is, make calls against its public API rather than its implementation details <https://oreil.ly/ijat0>. If tests work the same way as the system’s users, by definition, change that breaks a test might also break a user. As an additional bonus, such tests can serve as useful examples and documentation for users.

Consider A transaction API, which validates a transaction and saves it to a database.
  Example 12-1. A transaction API
```go

public void processTransaction(Transaction transaction) {
  if (isValid(transaction)) {
    saveToDatabase(transaction);
  }
}

private boolean isValid(Transaction t) {
  return t.getAmount() < t.getSender().getBalance();
}

private void saveToDatabase(Transaction t) {
  String s = t.getSender() + "," + t.getRecipient() + "," + t.getAmount();
  database.put(t.getId(), s);
}

public void setAccountBalance(String accountName, int balance) {
  // Write the balance to the database directly
}

public void getAccountBalance(String accountName) {
  // Read transactions from the database to determine the account balance
}
```

A tempting way to test this code would be to remove the "private" visibility modifiers and test the implementation logic directly, as demonstrated in A naive test of a transaction API’s implementation.
  Example 12-2. A naive test of a transaction API’s implementation
```go

@Test
public void emptyAccountShouldNotBeValid() {
  assertThat(processor.isValid(newTransaction().setSender(EMPTY_ACCOUNT)))
      .isFalse();
}

@Test
public void shouldSaveSerializedData() {
  processor.saveToDatabase(newTransaction()
      .setId(123)
      .setSender("me")
      .setRecipient("you")
      .setAmount(100));
  assertThat(database.get(123)).isEqualTo("me,you,100");
}
```

This test interacts with the transaction processor in a much different way than its real users would: it peers into the system’s internal state and calls methods that aren’t publicly exposed as part of the system’s API. As a result, the test is brittle, and almost any refactoring of the system under test (such as renaming its methods, factoring them out into a helper class, or changing the serialization format) would cause the test to break, even if such a change would be invisible to the class’s real users.

Instead, the same test coverage can be achieved by testing only against the class’s public API, as shown in Testing the public API.2
  Example 12-3. Testing the public API
```go

@Test
public void shouldTransferFunds() {
  processor.setAccountBalance("me", 150);
  processor.setAccountBalance("you", 20);

  processor.processTransaction(newTransaction()
      .setSender("me")
      .setRecipient("you")
      .setAmount(100));

  assertThat(processor.getAccountBalance("me")).isEqualTo(50);
  assertThat(processor.getAccountBalance("you")).isEqualTo(120);
}

@Test
public void shouldNotPerformInvalidTransactions() {
  processor.setAccountBalance("me", 50);
  processor.setAccountBalance("you", 20);

  processor.processTransaction(newTransaction()
      .setSender("me")
      .setRecipient("you")
      .setAmount(100));

  assertThat(processor.getAccountBalance("me")).isEqualTo(50);
  assertThat(processor.getAccountBalance("you")).isEqualTo(20);
}
```

Tests using only public APIs are, by definition, accessing the system under test in the same manner that its users would. Such tests are more realistic and less brittle because they form explicit contracts: if such a test breaks, it implies that an existing user of the system will also be broken. Testing only these contracts means that you’re free to do whatever internal refactoring of the system you want without having to worry about making tedious changes to tests.

It’s not always clear what constitutes a "public API," and the question really gets to the heart of what a "unit" is in unit testing.   Units can be as small as an individual function or as broad as a set of several related packages/modules. When we say "public API" in this context, we’re really talking about the API exposed by that unit to third parties outside of the team that owns the code. This doesn’t always align with the notion of visibility provided by some programming languages; for example, classes in Java might define themselves as "public" to be accessible by other packages in the same unit but are not intended for use by other parties outside of the unit. Some languages like Python have no built-in notion of visibility (often relying on conventions like prefixing private method names with underscores), and build systems like Bazel <https://bazel.build> can further restrict who is allowed to depend on APIs declared public by the programming language.

Defining an appropriate scope for a unit  and hence what should be considered the public API is more art than science, but here are some rules of thumb:

-
If a method or class exists only to support one or two other classes (i.e., it is a "helper class"), it probably shouldn’t be considered its own unit, and its functionality should be tested through those classes instead of directly.

-
If a package or class is designed to be accessible by anyone without having to consult with its owners, it almost certainly constitutes a unit that should be tested directly, where its tests access the unit in the same way that the users would.

-
If a package or class can be accessed only by the people who own it, but it is designed to provide a general piece of functionality useful in a range of contexts (i.e., it is a "support library"), it should also be considered a unit and tested directly. This will usually create some redundancy in testing given that the support library’s code will be covered both by its own tests and the tests of its users. However, such redundancy can be valuable: without it, a gap in test coverage could be introduced if one of the library’s users (and its tests) were ever removed.

At Google, we’ve found that engineers sometimes need to be persuaded that testing via public APIs is better than testing against implementation details. The reluctance is understandable because it’s often much easier to write tests focused on the piece of code you just wrote rather than figuring out how that code affects the system as a whole. Nevertheless, we have found it valuable to encourage such practices, as the extra upfront effort pays for itself many times over in reduced maintenance burden. Testing against public APIs won’t completely prevent brittleness, but it’s the most important thing you can do to ensure that your tests fail only in the event of meaningful changes to your system.
