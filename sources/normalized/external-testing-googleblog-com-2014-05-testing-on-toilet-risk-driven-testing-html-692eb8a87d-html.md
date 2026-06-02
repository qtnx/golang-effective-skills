Google Testing Blog: Testing on the Toilet: Risk-Driven Testing

##   Testing on the Toilet: Risk-Driven Testing  <https://testing.googleblog.com/2014/05/testing-on-toilet-risk-driven-testing.html>
      _by Peter Arrenbrecht_

 _This article was adapted from a Google Testing on the Toilet <http://googletesting.blogspot.com/2007/01/introducing-testing-on-toilet.html> (TotT) episode. You can download a printer-friendly version <https://docs.google.com/document/d/1QfmhsvpiCx__rcU0sr03Lu1fM1yhE8P9atyTgeLbRAQ/edit?usp=sharing> of this TotT episode and post it in your office. _

 **We are all conditioned to write tests** as we code: unit, functional, UI—the whole shebang. We are professionals, after all. Many of us like how small tests let us work quickly, and how larger tests inspire safety and closure. Or we may just anticipate flak during review. We are so used to these tests that often **we no longer question why we write them**. This can be wasteful and dangerous.

 **Tests are a means to an end:** To **reduce the key risks** of a project, and to **get the biggest bang for the buck**. This bang may not always come from the tests that standard practice has you write, or not even from tests at all.

 Two examples:

  _“We built a new debugging aid. We wrote unit, integration, and UI tests. We were ready to launch.”_

 Outstanding practice. **Missing the mark.**

 Our key risks were that we'd corrupt our data or bring down our servers for the sake of a debugging aid. None of the tests addressed this, but they gave a false sense of safety and “being done”.
 **We stopped the launch.**

  _“We wanted to turn down a feature, so we needed to alert affected users. Again we had unit and integration tests, and even one expensive end-to-end test.”_

 Standard practice. **Wasted effort.**

 The alert was so critical it actually needed end-to-end coverage for all scenarios. But it would be live for only three releases. The cheapest effective test? Manual testing before each release.

 **A Better Approach: Risks First **

 For every project or feature, **think about testing**. Brainstorm your key risks and your best options to reduce them. **Do this at the start** so you don't waste effort and can adapt your design. **Write them down** as a QA design so you can point to it in reviews and discussions.

 To be sure, **standard practice remains a good idea in most cases** (hence it’s standard). Small tests are cheap and speed up coding and maintenance, and larger tests safeguard core use-cases and integration.

 **Just remember**: Your tests are a means. **The bang is what counts**. It’s your job to **maximize it**.

####  1 comment :

-

The term "cheapest effective test" is a great choice of words -- a great reminder for both manual and automation testers to communicate effectively especially in the test planning phase! Test planning should to take into account the for the "bang for the buck" and "return on investment" for manual and automated testing effort from the get go.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/3751070536254843965>
Replies
Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2014/06/gtac-2014-coming-to-seattlekirkland-in.html>    _  _  <https://testing.googleblog.com/2014/05/testing-on-toilet-effective-testing.html>

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

-    ▼     2014  <https://testing.googleblog.com/2014/> (24)
-    ►     Dec  <https://testing.googleblog.com/2014/12/> (2)

-    ►     Nov  <https://testing.googleblog.com/2014/11/> (1)

-    ►     Oct  <https://testing.googleblog.com/2014/10/> (2)

-    ►     Sep  <https://testing.googleblog.com/2014/09/> (2)

-    ►     Aug  <https://testing.googleblog.com/2014/08/> (2)

-    ►     Jul  <https://testing.googleblog.com/2014/07/> (3)

-    ►     Jun  <https://testing.googleblog.com/2014/06/> (3)

-    ▼     May  <https://testing.googleblog.com/2014/05/> (2)
-   Testing on the Toilet: Risk-Driven Testing  <https://testing.googleblog.com/2014/05/testing-on-toilet-risk-driven-testing.html>
-   Testing on the Toilet: Effective Testing  <https://testing.googleblog.com/2014/05/testing-on-toilet-effective-testing.html>

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
