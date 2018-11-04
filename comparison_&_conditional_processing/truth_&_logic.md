# Truth and Logic

Truthy and Falsy
------------
- Certain times Python expressions evaluate/change state depending on a specific condition. That _truth_ & _falsity_ of the state is represented as:
    + `False`, `0`, `None`, `" "`, `[ ]`, `( )`, `{ }` are all treated as `False`.
    + `True`, eveyrthing else that's not treated as `False`.
- Python evaluates the conditional expression/object using a _factory function_, `_bool(object)_` to output one of the explicit _Boolean_ objects.

Logical Operators
--------------
As mentioned earlier Python provides three _**Logical Operators**_ that operate on the Boolean domain. The truth of the _logical operators_ are as follows:

- Truth table, showing the evaluation of the _**not**_ operator.

    |x   |not x|
    |----|-----|
    |True|False|
    |False|True|

- Truth table, showing the evaluation of the _**and**_ operator.

    |x    |y    |x and y|
    |-----|-----|-------|
    |True |True |True   |
    |True |False|False  |
    |False|True |False  |
    |False|False|False  |

- Truth table, showing the evaluation of the _**or**_ operator.

    |x    |y    |x or y|
    |-----|-----|------|
    |True |True |True  |
    |True |False|True  |
    |False|True |True  |
    |False|False|False |

_**Note:**_ Python will return a `False` if the left-hand side is a `False` or of equivalent values is present.

_**Rerences:**_
- [Truth and Logic - Building Skills in Python](http://www.itmaybeahack.com/book/python-2.6/latex/BuildingSkillsinPython.pdf#section.8.1)
- [AND OR NOT - Logic Gates Explained - Computerphile](https://www.youtube.com/watch?v=UvI-AMAtrvE&t=334s)