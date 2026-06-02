---
source_name: "External Linked Documentation"
source_url: "https://testing.googleblog.com/2017/06/code-health-reduce-nesting-reduce.html"
source_path: "sources/raw/external/testing-googleblog-com-2017-06-code-health-reduce-nesting-reduce-html-ce11f99236.html"
license_ref: ""
---

Google Testing Blog: Code Health: Reduce Nesting, Reduce Complexity
##   Code Health: Reduce Nesting, Reduce Complexity  <https://testing.googleblog.com/2017/06/code-health-reduce-nesting-reduce.html>
      _This is another post in our Code Health <https://testing.googleblog.com/2017/04/code-health-googles-internal-code.html> series. A version of this post originally appeared in Google bathrooms worldwide as a Google Testing on the Toilet <https://testing.googleblog.com/2007/01/introducing-testing-on-toilet.html> episode. You can download a printer-friendly version <https://docs.google.com/document/d/12VE8zEDSp5s0WZSFY7eGn91WGbUE67ASvxZmmc-yFOM/edit?usp=sharing> to display in your office. _

 By Elliott Karpilovsky

 Deeply nested code hurts readability and is error-prone.** Try spotting the bug** in the two versions of this code:

     _Code with too much nesting_ _Code with less nesting_
```go
response = server.Call(request)

if response.GetStatus() == RPC.OK:
  if response.GetAuthorizedUser():
    if response.GetEnc() == 'utf-8':
      if response.GetRows():
        vals = [ParseRow(r) for r in
                response.GetRows()]
        avg = sum(vals) / len(vals)
        return avg, vals
      else:
        raise EmptyError()
    else:
      raise AuthError('unauthorized')
  else:
    raise ValueError('wrong encoding')
else:
  raise RpcError(response.GetStatus())
```

```go
response = server.Call(request)

if response.GetStatus() != RPC.OK:
  raise RpcError(response.GetStatus())

if not response.GetAuthorizedUser():
  raise ValueError('wrong encoding')

if response.GetEnc() != 'utf-8':
  raise AuthError('unauthorized')

if not response.GetRows():
  raise EmptyError()

vals = [ParseRow(r) for r in
        response.GetRows()]
avg = sum(vals) / len(vals)
return avg, vals
```

 Answer: the "_wrong encoding"_ and "_unauthorized"_ errors are swapped. **This bug is easier to see in the refactored version, since the checks occur right as the errors are handled.**

 The refactoring technique shown above is known as **_guard clauses_**. A guard clause checks a criterion and fails fast if it is not met. It decouples the computational logic from the error logic. By removing the cognitive gap between error checking and handling, it frees up mental processing power. As a result, **the refactored version is much easier to read and maintain**.
 **
** **Here are some rules of thumb for reducing nesting in your code**:

- Keep conditional blocks short. It increases readability by keeping things local.
- Consider refactoring when your loops and branches are more than 2 levels deep.
- Think about moving nested logic into separate functions. For example, if you need to loop through a list of objects that each contain a list (such as a protocol buffer with repeated fields), you can define a function to process each object instead of using a double nested loop.
 Reducing nesting results in more readable code, which leads to discoverable bugs, faster developer iteration, and increased stability. When you can, simplify!

####  5 comments :

-

Thanks for the article. I like the example. As a rule of thumb I'd add replace conditional with polymorphism if possible.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/2070069235183990629>
Replies
Reply

-

Aren't the following 2 logical checks flipped on the exceptions they should raise?

if not response.GetAuthorizedUser():
•• raise ValueError('wrong encoding')

if response.GetEnc() != 'utf-8':
•• raise AuthError('unauthorized')
ReplyDelete <https://www.blogger.com/comment/delete/15045980/3422601211037969758>
Replies
Reply

-

Regarding my logic flip comment lol. Disregard since I clearly see it was intentional after continuing with the artcile
ReplyDelete <https://www.blogger.com/comment/delete/15045980/6015931823685605036>
Replies
Reply

-

I recently refactored a too much nested logic check because I had the very impression it wasn't redeable. Glad to see that kind of article, I will keep this tip in mind.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/3346426588462160196>
Replies
Reply

-

The one difference I would have is if error0 else if errorN else { success }.
Slightly easier to immediately go, ah huh, error(s) then success paths. Thanks to less whitespace + usage of else keyword.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/47338031013709936>
Replies
Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2017/06/code-health-too-many-comments-on-your.html>    _  _  <https://testing.googleblog.com/2017/05/gtac-diversity-scholarship.html>

    _  _

## Feed
  <http://googletesting.blogspot.com/atom.xml>
