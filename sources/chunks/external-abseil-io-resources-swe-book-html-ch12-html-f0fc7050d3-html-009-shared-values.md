---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

## Shared Values

Many tests are structured  by defining a set of shared  values to be used by tests and then by defining the tests that cover various cases for how these values interact. Shared values with ambiguous names illustrates what such tests look like.
  Example 12-21. Shared values with ambiguous names
```go

private static final Account ACCOUNT_1 = Account.newBuilder()
    .setState(AccountState.OPEN).setBalance(50).build();

private static final Account ACCOUNT_2 = Account.newBuilder()
    .setState(AccountState.CLOSED).setBalance(0).build();

private static final Item ITEM = Item.newBuilder()
    .setName("Cheeseburger").setPrice(100).build();

// Hundreds of lines of other tests...

@Test
public void canBuyItem_returnsFalseForClosedAccounts() {
  assertThat(store.canBuyItem(ITEM, ACCOUNT_1)).isFalse();
}

@Test
public void canBuyItem_returnsFalseWhenBalanceInsufficient() {
  assertThat(store.canBuyItem(ITEM, ACCOUNT_2)).isFalse();
}
```

This strategy can make tests very concise, but it causes problems as the test suite grows. For one, it can be difficult to understand why a particular value was chosen for a test. In Shared values with ambiguous names, the test names fortunately clarify which scenarios are being tested, but you still need to scroll up to the definitions to confirm that `ACCOUNT_1` and `ACCOUNT_2` are appropriate for those scenarios. More descriptive constant names (e.g., `CLOSED_ACCOUNT` and `ACCOUNT_WITH_LOW_BALANCE`) help a bit, but they still make it more difficult to see the exact details of the value being tested, and the ease of reusing these values can encourage engineers to do so even when the name doesn’t exactly describe what the test needs.

Engineers are usually drawn to using shared constants because constructing individual values in each test can be verbose.  A better way to accomplish this goal is to construct data using helper methods <https://oreil.ly/Jc4VJ> (see Shared values using helper methods) that require the test author to specify only values they care about, and setting reasonable defaults7 for all other values. This construction is trivial to do in languages that support named parameters, but languages without named parameters  can use constructs such as the _Builder_ pattern to emulate them (often with the assistance of tools such as AutoValue <https://oreil.ly/cVYK6>):
  Example 12-22. Shared values using helper methods
```go

# A helper method wraps a constructor by defining arbitrary defaults for
# each of its parameters.
def newContact(
    firstName="Grace", lastName="Hopper", phoneNumber="555-123-4567"):
  return Contact(firstName, lastName, phoneNumber)

# Tests call the helper, specifying values for only the parameters that they
# care about.
def test_fullNameShouldCombineFirstAndLastNames(self):
  def contact = newContact(firstName="Ada", lastName="Lovelace")
  self.assertEqual(contact.fullName(), "Ada Lovelace")

// Languages like Java that don’t support named parameters can emulate them
// by returning a mutable "builder" object that represents the value under
// construction.
private static Contact.Builder newContact() {
  return Contact.newBuilder()
    .setFirstName("Grace")
    .setLastName("Hopper")
    .setPhoneNumber("555-123-4567");
}

// Tests then call methods on the builder to overwrite only the parameters
// that they care about, then call build() to get a real value out of the
// builder.
@Test
public void fullNameShouldCombineFirstAndLastNames() {
  Contact contact = newContact()
      .setFirstName("Ada")
      .setLastName("Lovelace")
      .build();
  assertThat(contact.getFullName()).isEqualTo("Ada Lovelace");
}
```

Using helper methods to construct these values allows each test to create the exact values it needs without having to worry about specifying irrelevant information or conflicting with other tests.
