abseil / Tip of the Week #45: Avoid Flags, Especially in Library Code                          <https://github.com/abseil/>

-  C++ Tips
-  TotW #1: `string_view`
-  TotW #3: String Concatenation and `operator+` vs. `StrCat()`
-  TotW #3: String Concatenation and operator+ vs. StrCat()
-  TotW #5: Disappearing Act
-  TotW #5: Disappearing Act
-  Performance TotW #7: Optimizing for application productivity
-  Performance TotW #9: Optimizations past their prime
-  TotW #10: Splitting Strings, not Hairs
-  TotW #11: Return Policy
-  TotW #18: String Formatting with Substitute
-  Performance TotW #21: Improving the efficiency of your regular expressions
-  TotW #24: Copies, Abbrv.
-  Performance TotW #26: Fixing things with hashtable profiling
-  TotW #36: New Join API
-  Performance TotW #39: Beware microbenchmarks bearing gifts
-  TotW #42: Prefer Factory Functions to Initializer Methods
-  TotW #45: Avoid Flags, Especially in Library Code
-  TotW #49: Argument-Dependent Lookup
-  Performance TotW #52: Configuration knobs considered harmful
-  Performance TotW #53: Precise C++ benchmark measurements with Hardware Performance Counters
-  TotW #55: Name Counting and unique_ptr
-  TotW #59: Joining Tuples
-  Performance TotW #60: In-process profiling: lessons learned
-  TotW #61: Default Member Initializers
-  Performance TotW #62: Identifying and reducing memory bandwidth needs
-  Performance TotW #64: More Moore with better API design
-  TotW #64: Raw String Literals
-  TotW #65: Putting Things in their Place
-  Performance TotW #70: Defining and measuring optimization success
-  Performance TotW #72: Optimizing optimization
-  Performance TotW #74: Avoid sweeping street lights under rugs
-  TotW #74: Delegating and Inheriting Constructors
-  Performance TotW #75: How to microbenchmark
-  TotW #76: Use `absl::Status`
-  TotW #77: Temporaries, Moves, and Copies
-  Performance TotW #79: Make at most one tradeoff at a time
-  Performance TotW #83: Reducing memory indirections
-  TotW #86: Enumerating with Class
-  Performance TotW #87: Two-way doors
-  Performance TotW #88: Measurement methodology: Avoid the jelly beans trap
-  TotW #88: Initialization: =, (), and {}
-  Performance TotW #90: How to estimate
-  TotW #90: Retired Flags
-  Performance TotW #93: Robots never sleep
-  TotW #93: using absl::Span
-  Performance TotW #94: Decision making in a data-imperfect world
-  TotW #94: Callsite Readability and bool Parameters
-  Performance TotW #95: Spooky action at a distance
-  Performance TotW #97: Virtuous ecosystem cycles
-  Performance TotW #98: Measurement has an ROI
-  Performance TotW #99: Illuminating the processor core with llvm-mca
-  TotW #99: Nonmember Interface Etiquette
-  TotW #101: Return Values, References, and Lifetimes
-  TotW #103: Flags Are Globals
-  TotW #107: Reference Lifetime Extension
-  TotW #108: Avoid `std::bind`
-  TotW #109: Meaningful `const` in Function Declarations
-  TotW #112: emplace vs. push_back
-  TotW #116: Keeping References on Arguments
-  TotW #117: Copy Elision and Pass-by-value
-  TotW #119: Using-declarations and namespace aliases
-  TotW #120: Return Values are Untouchable
-  TotW #122: Test Fixtures, Clarity, and Dataflow
-  TotW #123: `absl::optional` and `std::unique_ptr`
-  TotW #124: `absl::StrFormat()`
-  TotW #126: `make_unique` is the new `new`
-  TotW #130: Namespace Naming
-  TotW #131: Special Member Functions and `= default`
-  TotW #134: `make_unique` and `private` Constructors.
-  TotW #135: Test the Contract, not the Implementation
-  TotW #136: Unordered Containers
-  TotW #140: Constants: Safe Idioms
-  TotW #141: Beware Implicit Conversions to `bool`
-  TotW #142: Multi-parameter Constructors and `explicit`
-  TotW #143: C++11 Deleted Functions (`= delete`)
-  TotW #144: Heterogeneous Lookup in Associative Containers
-  TotW #146: Default vs Value Initialization
-  TotW #147: Use Exhaustive `switch` Statements Responsibly
-  TotW #148: Overload Sets
-  TotW #149: Object Lifetimes vs. `= delete`
-  TotW #152: `AbslHashValue` and You
-  TotW #153: Don't Use using-directives
-  TotW #158: Abseil Associative containers and `contains()`
-  TotW #161: Good Locals and Bad Locals
-  TotW #163: Passing `std::optional` parameters
-  TotW #165: `if` and `switch` statements with initializers
-  TotW #166: When a Copy is not a Copy
-  TotW #168: `inline` Variables
-  TotW #171: Avoid Sentinel Values
-  TotW #172: Designated Initializers
-  TotW #173: Wrapping Arguments in Option Structs
-  TotW #175: Changes to Literal Constants in C++14 and C++17.
-  TotW #176: Prefer Return Values to Output Parameters
-  TotW #177: Assignability vs. Data Member Types
-  TotW #180: Avoiding Dangling References
-  TotW #181: Accessing the value of a StatusOr<T>
-  TotW #182: Initialize Your Ints!
-  TotW #186: Prefer to Put Functions in the Unnamed Namespace
-  TotW #187: `std::unique_ptr` Must Be Moved
-  TotW #188: Be Careful With Smart-Pointer Function Parameters
-  TotW #197: Reader Locks Should Be Rare
-  TotW #198: Tag Types
-  TotW #215: Stringifying Custom Types with `AbslStringify()`
-  TotW #218: Designing Extension Points With FTADLE
-  TotW #224: Avoid `vector.at()`
-  TotW #227: Be Careful with Empty Containers and Unsigned Arithmetic
-  TotW #229: Ranked Overloads for Template Metaprogramming
-  TotW #231: Between Here and There: Some Minor Overlooked Algorithms
-  TotW #232: When to Use `auto` for Variable Declarations
-  TotW #234: Pass by Value, by Pointer, or by Reference?

# Tip of the Week #45: Avoid Flags, Especially in Library Code

Originally posted as TotW #45 on June 3, 2013

*by Titus Winters

_“What I really want is the behavior of my code to be controlled by a global variable that cannot be statically predicted, whose usage is incompletely logged, and which can only be removed from my code with great difficulty.” – Nobody, Ever_

The common use of flags in production code, especially within libraries, is a mistake. Don’t use flags unless it is truly necessary. There, we said it.

Flags are global variables, only worse: you can’t know the value of that variable by reading the code. A flag may not only be set at startup, but could potentially be changed later through arbitrary means. If you run a server in your binary, there is usually no guarantee that the value of your flag will remain unchanged from cycle to cycle, nor any notification if it were to change, nor any means for looking for such a change.

If your production environment logs the invocation of every binary directly, and stores those logs, great. Most environments don’t work that way. For library code, this uncertainty is especially nefarious: how can you tell when use of a particular feature is actually dead? The simple answer is: you can’t.

Flags also make it challenging to put the final stake in dead code. During migrations to new backends, you’d _think_ that removing legacy code would simply be a matter of removing unnecessary build dependencies and issuing history’s most satisfying `git rm`. You’d be wrong. If your legacy binary has hundreds of flags defined and referenced by production code, simply removing the dead code would cause massive problems for your release engineers: almost no jobs would start up after such a change.

The worst part of all of this? An analysis that was done at Google during early 2012 found that the majority of C++ flags had never actually varied, as far as we can tell within the data retention limits described above.

Flags are appropriate in certain use cases, however: debugging without flag-enabled backtraces just wouldn’t be the same. Feature flags, when handled properly (and cleaned up afterward), are perfectly justified. Knobs that genuinely need to be tweaked by heroic SREs are a handy safety net. More broadly, flags used to pass name/value inputs to a binary, and used only in `main()`, are much more maintainable than positional parameters.

Even given those caveats, it’s time that we all take a good hard look at our usage of flags. The next time you’re tempted to add a flag to your library, spend a while looking for a better way. Pass configuration explicitly: this is almost always easier to reason about properly, and is certainly easier to maintain. Consider making numeric flags into compile-time constants. If you encounter new flags in code reviews, push back. Every flag introduction should be justified.

     <http://feeds.feedburner.com/abseilio>
