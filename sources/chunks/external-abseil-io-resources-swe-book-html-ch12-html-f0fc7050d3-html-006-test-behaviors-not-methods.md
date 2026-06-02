---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

## Test Behaviors, Not Methods

The first instinct of many engineers is to try to match the structure of their tests to the structure of their code such that every production method has a corresponding test method.      This pattern can be convenient at first, but over time it leads to problems: as the method being tested grows more complex, its test also grows in complexity and becomes more difficult to reason about. For example, consider the snippet of code in A transaction snippet, which displays the results of a transaction.
  Example 12-8. A transaction snippet
```go

public void displayTransactionResults(User user, Transaction transaction) {
  ui.showMessage("You bought a " + transaction.getItemName());
  if (user.getBalance() < LOW_BALANCE_THRESHOLD) {
    ui.showMessage("Warning: your balance is low!");
  }
}
```

It wouldn’t be uncommon to find a test covering both of the messages that might be shown by the  method, as  presented in A method-driven test.
  Example 12-9. A method-driven test
```go

@Test
public void testDisplayTransactionResults() {
  transactionProcessor.displayTransactionResults(
      newUserWithBalance(
          LOW_BALANCE_THRESHOLD.plus(dollars(2))),
      new Transaction("Some Item", dollars(3)));

  assertThat(ui.getText()).contains("You bought a Some Item");
  assertThat(ui.getText()).contains("your balance is low");
}
```

With such tests, it’s likely that the test started out covering only the first method. Later, an engineer expanded the test when the second message was added (violating the idea of unchanging tests that we discussed earlier). This modification sets a bad precedent: as the method under test becomes more complex and implements more functionality, its unit test will become increasingly convoluted and grow more and more difficult to work with.

The problem is that framing tests around methods can naturally encourage unclear tests because a single method often does a few different things under the hood and might have several tricky edge and corner cases.  There’s a better way: rather than writing a test for each method, write a test for each _behavior._4 A behavior is any guarantee that a system makes about how it will respond to a series of inputs while in a particular state.5 Behaviors can often be expressed using the words "given," "when," and "then" <https://oreil.ly/I9IvR>: “_Given_ that a bank  account is empty, _when_ attempting to withdraw money from it, _then_ the transaction is rejected." The mapping between methods and behaviors is many-to-many: most nontrivial methods implement multiple behaviors, and some behaviors rely on the interaction of multiple methods. The previous example can be rewritten using behavior-driven tests, as presented in A behavior-driven test.
  Example 12-10. A behavior-driven test
```go

@Test
public void displayTransactionResults_showsItemName() {
  transactionProcessor.displayTransactionResults(
      new User(), new Transaction("Some Item"));
  assertThat(ui.getText()).contains("You bought a Some Item");
}

@Test
public void displayTransactionResults_showsLowBalanceWarning() {
  transactionProcessor.displayTransactionResults(
      newUserWithBalance(
          LOW_BALANCE_THRESHOLD.plus(dollars(2))),
      new Transaction("Some Item", dollars(3)));
  assertThat(ui.getText()).contains("your balance is low");
}
```

The extra boilerplate required to split apart the single test is more than worth it <https://oreil.ly/hcoon>, and the resulting tests are much clearer than the original test. Behavior-driven tests tend to be clearer than method-oriented tests for several reasons. First, they read more like natural language, allowing them to be naturally understood rather than requiring laborious mental parsing. Second, they more clearly express cause and effect <https://oreil.ly/dAd3k> because each test is more limited in scope. Finally, the fact that each test is short and descriptive makes it easier to see what functionality is already tested and encourages engineers to add new streamlined test methods instead of piling onto existing methods.

### Structure tests to emphasize behaviors

Thinking about tests as being coupled to behaviors instead of methods significantly affects how they should be structured.    Remember that every behavior has three parts: a "given" component that defines how the system is set up, a "when" component that defines the action to be taken on the system, and a "then" component that validates the result.6 Tests are clearest when this structure is explicit.  Some frameworks like Cucumber <https://cucumber.io> and Spock <http://spockframework.org> directly bake in given/when/then. Other languages can use whitespace and optional comments to make the structure stand out, such as that shown in A well-structured test.
  Example 12-11. A well-structured test
```go

@Test
public void transferFundsShouldMoveMoneyBetweenAccounts() {
  // Given two accounts with initial balances of $150 and $20
  Account account1 = newAccountWithBalance(usd(150));
  Account account2 = newAccountWithBalance(usd(20));

  // When transferring $100 from the first to the second account
  bank.transferFunds(account1, account2, usd(100));

  // Then the new account balances should reflect the transfer
  assertThat(account1.getBalance()).isEqualTo(usd(50));
  assertThat(account2.getBalance()).isEqualTo(usd(120));
}
```

This level of description isn’t always necessary in trivial tests, and it’s usually sufficient to omit the comments and rely on whitespace to make the sections clear. However, explicit comments can make more sophisticated tests easier to understand. This pattern makes it possible to read tests at three levels of granularity:

-
A reader can start by looking at the test method name (discussed below) to get a rough description of the behavior being tested.

-
If that’s not enough, the reader can look at the given/when/then comments for a formal description of the behavior.

-
Finally, a reader can look at the actual code to see precisely how that behavior is expressed.

This pattern is  most commonly violated by interspersing assertions among multiple calls to the system under test (i.e., combining the "when" and "then" blocks). Merging the "then" and "when" blocks in this way can make the test less clear because it makes it difficult to distinguish the action being performed from the expected result.

When a test does want to validate each step in a multistep process, it’s acceptable to define alternating sequences of when/then blocks. Long blocks can also be made more descriptive by splitting them up with the word "and." Alternating when/then blocks within a test shows what a relatively complex, behavior-driven test might look like. 
  Example 12-12. Alternating when/then blocks within a test
```go

@Test
public void shouldTimeOutConnections() {
  // Given two users
  User user1 = newUser();
  User user2 = newUser();

  // And an empty connection pool with a 10-minute timeout
  Pool pool = newPool(Duration.minutes(10));

  // When connecting both users to the pool
  pool.connect(user1);
  pool.connect(user2);

  // Then the pool should have two connections
  assertThat(pool.getConnections()).hasSize(2);

  // When waiting for 20 minutes
  clock.advance(Duration.minutes(20));

  // Then the pool should have no connections
  assertThat(pool.getConnections()).isEmpty();

  // And each user should be disconnected
  assertThat(user1.isConnected()).isFalse();
  assertThat(user2.isConnected()).isFalse();
}
```

When writing such tests, be careful to ensure that you’re not inadvertently testing multiple behaviors at the same time. Each test should cover only a single behavior, and the vast majority of unit tests require only one "when" and one "then" block.

### Name tests after the behavior being tested

Method-oriented  tests are usually named  after the method being tested (e.g., a test for the `updateBalance` method is usually called `testUpdateBalance`). With more focused behavior-driven tests, we have a lot more flexibility and the chance to convey useful information in the test’s name. The test name is very important: it will often be the first or only token visible in failure reports, so it’s your best opportunity to communicate the problem when the test breaks. It’s also the most straightforward way to express the intent of the test.

A test’s name should summarize the behavior it is testing. A good name describes both the actions that are being taken on a system and the expected outcome <https://oreil.ly/8eqqv>. Test names will sometimes include additional information like the state of the system or its environment before taking action on it. Some languages and frameworks make this easier than others by allowing tests to be nested within one another and named using strings, such as in Some sample nested naming patterns, which uses Jasmine <https://jasmine.github.io>.
  Example 12-13. Some sample nested naming patterns
```go

describe("multiplication", function() {
  describe("with a positive number", function() {
    var positiveNumber = 10;
    it("is positive with another positive number", function() {
      expect(positiveNumber * 10).toBeGreaterThan(0);
    });
    it("is negative with a negative number", function() {
      expect(positiveNumber * -10).toBeLessThan(0);
    });
  });
  describe("with a negative number", function() {
    var negativeNumber = 10;
    it("is negative with a positive number", function() {
      expect(negativeNumber * 10).toBeLessThan(0);
    });
    it("is positive with another negative number", function() {
      expect(negativeNumber * -10).toBeGreaterThan(0);
    });
  });
});
```

Other languages  require us to encode all of this information in a method name, leading to method naming patterns like that shown in Some sample method naming patterns.
  Example 12-14. Some sample method naming patterns
```go

multiplyingTwoPositiveNumbersShouldReturnAPositiveNumber
multiply_positiveAndNegative_returnsNegative
divide_byZero_throwsException
```

Names like this are much more verbose than we’d normally want to write for methods in production code, but the use case is different: we never need to write code that calls these, and their names frequently need to be read by humans in reports. Hence, the extra verbosity is warranted.

Many different naming strategies are acceptable so long as they’re used consistently within a single test class. A good trick if you’re stuck is to try starting the test name with the word "should." When taken with the name of the class being tested, this naming scheme allows the test name to be read as a sentence. For example, a test of a `BankAccount` class named `shouldNotAllowWithdrawalsWhenBalanceIsEmpty` can be read as "BankAccount should not allow withdrawals when balance is empty." By reading the names of all the test methods in a suite, you should get a good sense of the behaviors implemented by the system under test. Such names also help ensure that the test stays focused on a single behavior: if you need to use the word "and" in a test name, there’s a good chance that you’re actually testing multiple behaviors and should be writing multiple tests!
