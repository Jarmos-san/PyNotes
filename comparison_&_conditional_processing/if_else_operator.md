# The `if-else` Operator

In situations where the `if` statements can be oversized and ugly, the `if-else` operator or more commonly known as the _**Ternary Operator**_ are used.

_**Syntax:**_

```Python
expression if condition else expression
```

Python evaluates the middle _condition_ first which if true then the left-side expression is evaluated or otherwise the right-side expression.

_**Example:**_

```Python
# Program to demonstrate conditional operator 
a, b = 10, 20

# Copy value of a in min if a < b else copy b 
min = a if a < b else b 

print(min)
```

_**Refereneces:**_
- [Ternary Operator in Python - GeeksForGeeks](https://www.geeksforgeeks.org/ternary-operator-in-python/)
- [The `if-else` Operator](http://www.itmaybeahack.com/book/python-2.6/latex/BuildingSkillsinPython.pdf#section.8.6)