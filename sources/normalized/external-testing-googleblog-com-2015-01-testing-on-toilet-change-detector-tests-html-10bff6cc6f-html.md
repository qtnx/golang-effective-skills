Google Testing Blog: Testing on the Toilet: Change-Detector Tests Considered Harmful

##   Testing on the Toilet: Change-Detector Tests Considered Harmful  <https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html>
      _by Alex Eagle

 This article was adapted from a Google Testing on the Toilet <http://googletesting.blogspot.com/2007/01/introducing-testing-on-toilet.html> (TotT) episode. You can download a printer-friendly version <https://docs.google.com/document/d/13k8AsgYdF-2TJx9QIHHvPiuV3JMbsrMLkWmmjdYBLVg/edit?usp=sharing> of this TotT episode and post it in your office. _

 You have just finished refactoring some code without modifying its behavior. Then you run the tests before committing and… a bunch of unit tests are failing. **While fixing the tests, you get a sense that you are wasting time by mechanically applying the same transformation to many tests.** Maybe you introduced a parameter in a method, and now must update 100 callers of that method in tests to pass an empty string.

 **What does it look like to write tests mechanically?** Here is an absurd but obvious way:

```go
// Production code:
def abs(i: Int)
  return (i < 0) ? i * -1 : i

// Test code:
for (line: String in File(prod_source).read_lines())
  switch (line.number)
    1: assert line.content equals "def abs(i: Int)"
    2: assert line.content equals "  return (i < 0) ? i * -1 : i"
```

 **That test is clearly not useful**: it contains an exact copy of the code under test and acts like a checksum. **A correct or incorrect program is equally likely to pass** a test that is a derivative of the code under test. No one is really writing tests like that, but how different is it from this next example?

```go
// Production code:
def process(w: Work)
  firstPart.process(w)
  secondPart.process(w)

// Test code:
part1 = mock(FirstPart)
part2 = mock(SecondPart)
w = Work()
Processor(part1, part2).process(w)
verify_in_order
  was_called part1.process(w)
  was_called part2.process(w)
```

 It is tempting to write a test like this because it requires little thought and will run quickly. **This is a change-detector test**—it is a transformation of the same information in the code under test—and **it breaks in response to any change to the production code, without verifying correct behavior** of either the original or modified production code.

 **Change detectors provide negative value**, since the tests do not catch any defects, and the added maintenance cost slows down development. These tests should be re-written or deleted.

####  2 comments :

-

This topic is very much related to that of testing behavior versus implementation. In this case, the examples given are very simple. What if your process function looked more like this :

def process(w: Work)
 firstResult = firstPart.process(w)
 secondPart.process(w, firstResult)

In this case, would it not be acceptable for your unit test to validate that the secondPart's process method is being called with the result of the firstPart.process as parameter? Or perhaps a slightly more complex case, one where the Processor modifies the result from the firstPart's process and passes that to the secondPart.

Writing unit tests that are not change detectors sounds like a good objective. But, when coding in a system that is very service oriented, it is not always possible to write unit tests that are not change detectors and that test only behavior as opposed to implementation. In those cases, writing tests that validate function calls seems like the fastest way to achieve confidence that your code works.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/8028448860298130774>
Replies
-

There are also other aspects on testing than just running your code. Good written tests document your code and help others getting around. Tests provide a safety net for refactoring. Change-detector tests as described above do not add any clarity, and you cannot safely refactor stuff if you know for sure that you need to adapt the tests afterwards to get them passing again.

When you think about your example: can you really be "confident that your code works"? What if someone completely changes firstPart - your test would still pass, because you mock everything, even if the process function might not work anymore.
Delete <https://www.blogger.com/comment/delete/15045980/2563666534509864769>
Replies
Reply

Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2015/02/the-first-annual-testing-on-toilet.html>    _  _  <https://testing.googleblog.com/2015/01/testing-on-toilet-prefer-testing-public.html>

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

-    ▼     2015  <https://testing.googleblog.com/2015/> (14)
-    ►     Dec  <https://testing.googleblog.com/2015/12/> (1)

-    ►     Nov  <https://testing.googleblog.com/2015/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2015/10/> (2)

-    ►     Aug  <https://testing.googleblog.com/2015/08/> (1)

-    ►     Jun  <https://testing.googleblog.com/2015/06/> (1)

-    ►     May  <https://testing.googleblog.com/2015/05/> (2)

-    ►     Apr  <https://testing.googleblog.com/2015/04/> (2)

-    ►     Mar  <https://testing.googleblog.com/2015/03/> (1)

-    ►     Feb  <https://testing.googleblog.com/2015/02/> (1)

-    ▼     Jan  <https://testing.googleblog.com/2015/01/> (2)
-   Testing on the Toilet: Change-Detector Tests Consi...  <https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html>
-   Testing on the Toilet: Prefer Testing Public APIs ...  <https://testing.googleblog.com/2015/01/testing-on-toilet-prefer-testing-public.html>

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

-    ►     2008  <https://testing.googleblog.com/2008/> (75)
-    ►     Dec  <https://testing.googleblog.com/2008/12/> (6)

-    ►     Nov  <https://testing.googleblog.com/2008/11/> (8)

-    ►     Oct  <https://testing.googleblog.com/2008/10/> (9)

-    ►     Sep  <https://testing.googleblog.com/2008/09/> (8)

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
