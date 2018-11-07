# Iterative Processing

The `all()` And `any()` Function
-------------
- The `all()` and `any()` takes in iterables as their parameters and return `True` if _**all**_ or _**any**_(respectively) of all the elements in the iterable are `True`. 
- These functions are written such that they _keep looking_ for a condition until that allows them to stop evaluating. In other words, the `all()` function looks for `False` elements in the iterable and then return a `True` `if none of them were `False`. While the `any()` function checks for `True` elements and returns `False`, if none of them were `False`.
- The _**Truth Table**_ for the `all()` and `any()` function is as follows:

|                                         |   any   |   all   |
|-----------------------------------------|---------|---------|
| All Truthy values                       |  True   |  True   |
| All Falsy values                        |  False  |  False  |
| One Truthy value (all others are Falsy) |  True   |  False  |
| One Falsy value (all others are Truthy) |  True   |  False  |
| Empty Iterable                          |  False  |  True   |

_**Note:**_
- The empty iterable case is explained in the official documentation, like this

`any()` - Return `True` if any element of the iterable is true. If the iterable is empty, return `False`. Since none of the elements is true, it returns `False` in this case.

`all()` - Return `True` if all elements of the iterable are true (or if the iterable is empty). Since none of the elements is false, it returns `True` in this case. 

The `for` Statement
--------------


_**References:**_
- [thefourtheye's Answer on Stack Overflow](https://stackoverflow.com/a/19389957/8604951)
- [Aaron Hall's Answer on Stack Overflow](https://stackoverflow.com/a/39711683/8604951)