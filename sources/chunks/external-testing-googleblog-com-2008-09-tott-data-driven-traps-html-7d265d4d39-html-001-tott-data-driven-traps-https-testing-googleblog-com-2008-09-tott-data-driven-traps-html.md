---
source_name: "External Linked Documentation"
source_url: "https://testing.googleblog.com/2008/09/tott-data-driven-traps.html"
source_path: "sources/raw/external/testing-googleblog-com-2008-09-tott-data-driven-traps-html-7d265d4d39.html"
license_ref: ""
---

Google Testing Blog: TotT: Data Driven Traps!
##   TotT: Data Driven Traps!  <https://testing.googleblog.com/2008/09/tott-data-driven-traps.html>
      When writing a unit test, it is tempting to exercise many scenarios by writing a data-driven test. For example, to test the function IsWord, you could write (ARRAYSIZE is a macro that returns the number of elements in an array):

const struct {const char* word; bool is_word;} test_data[] = {
  {"milk", true}, {"centre", false}, {"jklm", false},
};

TEST(IsWordTest, TestEverything) {
  for (int i = 0; i < ARRAYSIZE(test_data); i++)
    EXPECT_EQ(test_data[i].is_word, IsWord(test_data[i].word));
}

This keeps the test code short and makes it easy to add new tests but makes it hard to identify a failing test assertion (and to get the debugger to stop in the right place). As your code grows the test data tends to grow **faster than linearly**. For example, if you add a parameter called locale to IsWord, the test could become:

 Locale LOCALES[] = { Word::US, Word::UK, Word::France, ... };
const struct {const char* word; bool is_word[NUM_LOCALES];} data[] = {
  {"milk", {true, true, false, ...}}, // one bool per language
  {"centre", {false, true, true, ...}},
  {"jklm", {false, false, false, ...}}
};

TEST(IsWordTest, TestEverything) {
  for (int i = 0; i < ARRAYSIZE(data); i++)
    for (int j = 0; j < ARRAYSIZE(LOCALES); j++)
      EXPECT_EQ(data[i].is_word[j], IsWord(data[i].word, LOCALES[i]));
}

The change was relatively easy to make: change the data structure, fill in the boolean values for other locales and add a loop to the test code. But even this small changed has made the test harder to read and slower as it repeats potentially unnecessary checks. In addition, both the test AND the code have changed. How do you know the test is not broken? (Actually, it is broken. Can you see the bug?) By contrast, **keeping the data in the test** gives us:

 TEST(IsWordTest, IsWordInMultipleLocales) {
  EXPECT_TRUE(IsWord("milk", Word::UK));
  EXPECT_TRUE(IsWord("milk", Word::US));
  EXPECT_FALSE(IsWord("milk", Word::France));
}

TEST(IsWordTest, IsWordWithNonExistentWord) { // 'jklm' test is not repeated
  EXPECT_FALSE(IsWord("jklm", Word::US)); // as it uses the same code path
}

The difference between these two code snippets is minor but real-life data-driven tests quickly become **unmanageable**. A complete example would not fit on this page but if you look at your code base, you will find a few specimens lurking in some (not-so) forgotten test classes. They can be identified by their large size, vague names and the fact that they provide little to no information about why they fail.

####  8 comments :

-

A good post on the importance of maintainable tests!
ReplyDelete <https://www.blogger.com/comment/delete/15045980/5225023950466398900>
Replies
Reply

-

This is an excellent post. It's too easy to use data the wrong way. Just had this discussion with someone yesterday, and I'm putting this on their desk.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/8197503562082617895>
Replies
Reply

-

I totally agree based on the example here. I wonder what you would propose for an alternative example. Where I work we keep 'models' in separate files from application source that uses them, and they all exist in a single directory. We have a rule that all model files must pass tests x, y, z ( I believer there's 12-15 of them). To accomplish this, there's a single test that iterates over each file in the directory and performs the same checks on each them.

Note that this is a simplified explanation, but this does allow us to add new 'models' over time without having to add tests for each one.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/8018006094930762597>
Replies
Reply

-

This comment has been removed by the author.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/2429911152623334134>
Replies
Reply

-

How can google which claims best Testing team lose out on this basic security vulnerabilities?? Check out here <http://codeinspections.blogspot.com/2008/09/security-issues-in-chrome-browser.html>
ReplyDelete <https://www.blogger.com/comment/delete/15045980/5715719812281399342>
Replies
Reply

-

BUG : LOCALES[i] should be LOCALES[j]
ReplyDelete <https://www.blogger.com/comment/delete/15045980/1430681449842366351>
Replies
Reply

-

So... you've picked a test where the test logic is a single assert, and shown that if the data becomes complex and you don't have any diagnostic information, you end up with an unmaintainable test. Or if you shove together two different types of tests (a series of positive tests and one negative one that gets repeated if you stuff it in the loop), you're doing useless work. OK, fair enough. But you go from there to the conclusion that data-driven testing is bad, and I don't buy it.

What about a situation where you're test logic is several lines? How large before the cutting and pasting is a more likely source of bugs than the data structure? Why not be sensible about defining the data and not mix positive and negative tests? Why not be sensible about error reporting and include an informative message with each line of data?

Yes, unit tests in particular tend towards minimalist logic, and in such cases pulling out the data doesn't buy you much, and can obscure things as you add cruft to compensate for the code's generality. But just because you can construct a test case that is a poor fit for the data-driven methodology does not prove that that methodology is universally unsound.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/5905201371745002463>
Replies
Reply

-

Maybe this is true with GTest, where rolling your own data-driven testing structures is necessary. Other testing frameworks build support for data-driven tests into the testing API in ways that are useful and easy to debug. I've had a lot of success writing, maintaining, and catching/fixing bugs using Qt's data-driven testing framework:

http://qt-project.org/doc/qt-4.8/qtestlib-tutorial2.html

When a test fails, it prints a human-readable description of the failing test case that is easy to correlate to the inputs, along with the expected and actual values that triggered the failure. Their implementation is easy to write, maintain, extend, and use. Don't knock the concept, improve the implementation ;-)
ReplyDelete <https://www.blogger.com/comment/delete/15045980/4558189104831833801>
Replies
Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2008/09/my-main-method-is-better-than-yours.html>    _  _  <https://testing.googleblog.com/2008/08/taming-beast.html>

    _  _

## Feed
  <http://googletesting.blogspot.com/atom.xml>
