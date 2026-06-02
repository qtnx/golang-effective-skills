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
##  Archive
 _  _

-    ►     2026  <https://testing.googleblog.com/2026/> (5)
-    ►     May  <https://testing.googleblog.com/2026/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2026/04/> (1)

-    ►     Mar  <https://testing.googleblog.com/2026/03/> (2)

-    ►     2025  <https://testing.googleblog.com/2025/> (3)
-    ►     Oct  <https://testing.googleblog.com/2025/10/> (1)

-    ►     Sep  <https://testing.googleblog.com/2025/09/> (1)

-    ►     Jan  <https://testing.googleblog.com/2025/01/> (1)

-    ►     2024  <https://testing.googleblog.com/2024/> (13)
-    ►     Dec  <https://testing.googleblog.com/2024/12/> (1)

-    ►     Oct  <https://testing.googleblog.com/2024/10/> (1)

-    ►     Sep  <https://testing.googleblog.com/2024/09/> (1)

-    ►     Aug  <https://testing.googleblog.com/2024/08/> (1)

-    ►     Jul  <https://testing.googleblog.com/2024/07/> (1)

-    ►     May  <https://testing.googleblog.com/2024/05/> (3)

-    ►     Apr  <https://testing.googleblog.com/2024/04/> (3)

-    ►     Mar  <https://testing.googleblog.com/2024/03/> (1)

-    ►     Feb  <https://testing.googleblog.com/2024/02/> (1)

-    ►     2023  <https://testing.googleblog.com/2023/> (14)
-    ►     Dec  <https://testing.googleblog.com/2023/12/> (2)

-    ►     Nov  <https://testing.googleblog.com/2023/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2023/10/> (5)

-    ►     Sep  <https://testing.googleblog.com/2023/09/> (3)

-    ►     Aug  <https://testing.googleblog.com/2023/08/> (1)

-    ►     Apr  <https://testing.googleblog.com/2023/04/> (1)

-    ►     2022  <https://testing.googleblog.com/2022/> (2)
-    ►     Feb  <https://testing.googleblog.com/2022/02/> (2)

-    ►     2021  <https://testing.googleblog.com/2021/> (3)
-    ►     Jun  <https://testing.googleblog.com/2021/06/> (1)

-    ►     Apr  <https://testing.googleblog.com/2021/04/> (1)

-    ►     Mar  <https://testing.googleblog.com/2021/03/> (1)

-    ►     2020  <https://testing.googleblog.com/2020/> (8)
-    ►     Dec  <https://testing.googleblog.com/2020/12/> (2)

-    ►     Nov  <https://testing.googleblog.com/2020/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2020/10/> (1)

-    ►     Aug  <https://testing.googleblog.com/2020/08/> (2)

-    ►     Jul  <https://testing.googleblog.com/2020/07/> (1)

-    ►     May  <https://testing.googleblog.com/2020/05/> (1)

-    ►     2019  <https://testing.googleblog.com/2019/> (4)
-    ►     Dec  <https://testing.googleblog.com/2019/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2019/11/> (1)

-    ►     Jul  <https://testing.googleblog.com/2019/07/> (1)

-    ►     Jan  <https://testing.googleblog.com/2019/01/> (1)

-    ►     2018  <https://testing.googleblog.com/2018/> (7)
-    ►     Nov  <https://testing.googleblog.com/2018/11/> (1)

-    ►     Sep  <https://testing.googleblog.com/2018/09/> (1)

-    ►     Jul  <https://testing.googleblog.com/2018/07/> (1)

-    ►     Jun  <https://testing.googleblog.com/2018/06/> (2)

-    ►     May  <https://testing.googleblog.com/2018/05/> (1)

-    ►     Feb  <https://testing.googleblog.com/2018/02/> (1)

-    ►     2017  <https://testing.googleblog.com/2017/> (17)
-    ►     Dec  <https://testing.googleblog.com/2017/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2017/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2017/10/> (1)

-    ►     Sep  <https://testing.googleblog.com/2017/09/> (1)

-    ►     Aug  <https://testing.googleblog.com/2017/08/> (1)

-    ►     Jul  <https://testing.googleblog.com/2017/07/> (2)

-    ►     Jun  <https://testing.googleblog.com/2017/06/> (2)

-    ►     May  <https://testing.googleblog.com/2017/05/> (3)

-    ►     Apr  <https://testing.googleblog.com/2017/04/> (2)

-    ►     Feb  <https://testing.googleblog.com/2017/02/> (1)

-    ►     Jan  <https://testing.googleblog.com/2017/01/> (2)

-    ►     2016  <https://testing.googleblog.com/2016/> (15)
-    ►     Dec  <https://testing.googleblog.com/2016/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2016/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2016/10/> (1)

-    ►     Sep  <https://testing.googleblog.com/2016/09/> (2)

-    ►     Aug  <https://testing.googleblog.com/2016/08/> (1)

-    ►     Jun  <https://testing.googleblog.com/2016/06/> (2)

-    ►     May  <https://testing.googleblog.com/2016/05/> (3)

-    ►     Apr  <https://testing.googleblog.com/2016/04/> (1)

-    ►     Mar  <https://testing.googleblog.com/2016/03/> (1)

-    ►     Feb  <https://testing.googleblog.com/2016/02/> (1)

-    ►     2015  <https://testing.googleblog.com/2015/> (14)
-    ►     Dec  <https://testing.googleblog.com/2015/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2015/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2015/10/> (2)

-    ►     Aug  <https://testing.googleblog.com/2015/08/> (1)

-    ►     Jun  <https://testing.googleblog.com/2015/06/> (1)

-    ►     May  <https://testing.googleblog.com/2015/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2015/04/> (2)

-    ►     Mar  <https://testing.googleblog.com/2015/03/> (1)

-    ►     Feb  <https://testing.googleblog.com/2015/02/> (1)

-    ►     Jan  <https://testing.googleblog.com/2015/01/> (2)

-    ►     2014  <https://testing.googleblog.com/2014/> (24)
-    ►     Dec  <https://testing.googleblog.com/2014/12/> (2)

-    ►     Nov  <https://testing.googleblog.com/2014/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2014/10/> (2)

-    ►     Sep  <https://testing.googleblog.com/2014/09/> (2)

-    ►     Aug  <https://testing.googleblog.com/2014/08/> (2)

-    ►     Jul  <https://testing.googleblog.com/2014/07/> (3)

-    ►     Jun  <https://testing.googleblog.com/2014/06/> (3)

-    ►     May  <https://testing.googleblog.com/2014/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2014/04/> (2)

-    ►     Mar  <https://testing.googleblog.com/2014/03/> (2)

-    ►     Feb  <https://testing.googleblog.com/2014/02/> (1)

-    ►     Jan  <https://testing.googleblog.com/2014/01/> (2)

-    ►     2013  <https://testing.googleblog.com/2013/> (16)
-    ►     Dec  <https://testing.googleblog.com/2013/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2013/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2013/10/> (1)

-    ►     Aug  <https://testing.googleblog.com/2013/08/> (2)

-    ►     Jul  <https://testing.googleblog.com/2013/07/> (1)

-    ►     Jun  <https://testing.googleblog.com/2013/06/> (2)

-    ►     May  <https://testing.googleblog.com/2013/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2013/04/> (2)

-    ►     Mar  <https://testing.googleblog.com/2013/03/> (2)

-    ►     Jan  <https://testing.googleblog.com/2013/01/> (2)

-    ►     2012  <https://testing.googleblog.com/2012/> (11)
-    ►     Dec  <https://testing.googleblog.com/2012/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2012/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2012/10/> (3)

-    ►     Sep  <https://testing.googleblog.com/2012/09/> (1)

-    ►     Aug  <https://testing.googleblog.com/2012/08/> (4)

-    ►     2011  <https://testing.googleblog.com/2011/> (39)
-    ►     Nov  <https://testing.googleblog.com/2011/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2011/10/> (5)

-    ►     Sep  <https://testing.googleblog.com/2011/09/> (2)

-    ►     Aug  <https://testing.googleblog.com/2011/08/> (4)

-    ►     Jul  <https://testing.googleblog.com/2011/07/> (2)

-    ►     Jun  <https://testing.googleblog.com/2011/06/> (5)

-    ►     May  <https://testing.googleblog.com/2011/05/> (4)

-    ►     Apr  <https://testing.googleblog.com/2011/04/> (3)

-    ►     Mar  <https://testing.googleblog.com/2011/03/> (4)

-    ►     Feb  <https://testing.googleblog.com/2011/02/> (5)

-    ►     Jan  <https://testing.googleblog.com/2011/01/> (3)

-    ►     2010  <https://testing.googleblog.com/2010/> (37)
-    ►     Dec  <https://testing.googleblog.com/2010/12/> (3)

-    ►     Nov  <https://testing.googleblog.com/2010/11/> (3)

-    ►     Oct  <https://testing.googleblog.com/2010/10/> (4)

-    ►     Sep  <https://testing.googleblog.com/2010/09/> (8)

-    ►     Aug  <https://testing.googleblog.com/2010/08/> (3)

-    ►     Jul  <https://testing.googleblog.com/2010/07/> (3)

-    ►     Jun  <https://testing.googleblog.com/2010/06/> (2)

-    ►     May  <https://testing.googleblog.com/2010/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2010/04/> (3)

-    ►     Mar  <https://testing.googleblog.com/2010/03/> (3)

-    ►     Feb  <https://testing.googleblog.com/2010/02/> (2)

-    ►     Jan  <https://testing.googleblog.com/2010/01/> (1)

-    ►     2009  <https://testing.googleblog.com/2009/> (54)
-    ►     Dec  <https://testing.googleblog.com/2009/12/> (3)

-    ►     Nov  <https://testing.googleblog.com/2009/11/> (2)

-    ►     Oct  <https://testing.googleblog.com/2009/10/> (3)

-    ►     Sep  <https://testing.googleblog.com/2009/09/> (5)

-    ►     Aug  <https://testing.googleblog.com/2009/08/> (4)

-    ►     Jul  <https://testing.googleblog.com/2009/07/> (15)

-    ►     Jun  <https://testing.googleblog.com/2009/06/> (8)

-    ►     May  <https://testing.googleblog.com/2009/05/> (3)

-    ►     Apr  <https://testing.googleblog.com/2009/04/> (2)

-    ►     Feb  <https://testing.googleblog.com/2009/02/> (5)

-    ►     Jan  <https://testing.googleblog.com/2009/01/> (4)

-    ▼     2008  <https://testing.googleblog.com/2008/> (75)
-    ►     Dec  <https://testing.googleblog.com/2008/12/> (6)

-    ►     Nov  <https://testing.googleblog.com/2008/11/> (8)

-    ►     Oct  <https://testing.googleblog.com/2008/10/> (9)

-    ▼     Sep  <https://testing.googleblog.com/2008/09/> (8)
-   by Miško Hevery We talked about how it i...  <https://testing.googleblog.com/2008/09/by-miko-hevery-we-talked-about-how-it.html>
-   TotT: Mockin Ur Objectz  <https://testing.googleblog.com/2008/09/tott-mockin-ur-objectz.html>
-   Presubmit And Performance  <https://testing.googleblog.com/2008/09/presubmit-and-performance.html>
-   The Google Maps API Open Source Their Selenium Tes...  <https://testing.googleblog.com/2008/09/google-maps-api-open-sources-their.html>
-   Where Have all the "new" Operators Gone?  <https://testing.googleblog.com/2008/09/where-have-all-new-operators-gone.html>
-   Test first is fun!  <https://testing.googleblog.com/2008/09/test-first-is-fun_08.html>
-   My main() Method Is Better Than Yours  <https://testing.googleblog.com/2008/09/my-main-method-is-better-than-yours.html>
-   TotT: Data Driven Traps!  <https://testing.googleblog.com/2008/09/tott-data-driven-traps.html>

-    ►     Aug  <https://testing.googleblog.com/2008/08/> (9)

-    ►     Jul  <https://testing.googleblog.com/2008/07/> (9)

-    ►     Jun  <https://testing.googleblog.com/2008/06/> (6)

-    ►     May  <https://testing.googleblog.com/2008/05/> (6)

-    ►     Apr  <https://testing.googleblog.com/2008/04/> (4)

-    ►     Mar  <https://testing.googleblog.com/2008/03/> (4)

-    ►     Feb  <https://testing.googleblog.com/2008/02/> (4)

-    ►     Jan  <https://testing.googleblog.com/2008/01/> (2)

-    ►     2007  <https://testing.googleblog.com/2007/> (41)
-    ►     Oct  <https://testing.googleblog.com/2007/10/> (6)

-    ►     Sep  <https://testing.googleblog.com/2007/09/> (5)

-    ►     Aug  <https://testing.googleblog.com/2007/08/> (3)

-    ►     Jul  <https://testing.googleblog.com/2007/07/> (2)

-    ►     Jun  <https://testing.googleblog.com/2007/06/> (2)

-    ►     May  <https://testing.googleblog.com/2007/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2007/04/> (7)

-    ►     Mar  <https://testing.googleblog.com/2007/03/> (5)

-    ►     Feb  <https://testing.googleblog.com/2007/02/> (5)

-    ►     Jan  <https://testing.googleblog.com/2007/01/> (4)

## Feed
  <http://googletesting.blogspot.com/atom.xml>
