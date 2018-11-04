# Conditional Processing

The `if` Statement
--------
- The `if` statement provides a certain condition right after the `if` statement, succeeded by a suite of expressions which are executed if the condition is true.
- The suit is an indented block of statements which are executed only after the previous condition evaluates to `True`. Inside this indented block of statements, any kind of statements can exist, even indented `if` statements.

_**Syntax:**_ 

```Python
if condition:
    expression
```
_**Example:**_

```Python
if d1+d2 == 7 or d1+d2 == 11:
    print('Winner', d1+d2)
```

In the aforementioned example, Python evaluates the left-side first which if true, the whole `or` expression is True and then the suite in the indented block is executed.

The `elif` Clause
--------------
- The `elif` clauses is more of a short-form of the `else-if` clause and the syntax for it is also quite similar to the `if` statement.

_**Syntax:**_

```Python
elif condition:
    expression
```

_**Example:**_
```Python
result = None
if d1+d2 == 7 or d1+d2 == 11:
    result = 'Winner!!'
elif d1+d2 == 2 or d1+d2 == 3 or d1+d2 == 12:
    result = 'Loser!!'
print(result)
```
The aforementioned example would print `"Winner!!` if the two die rolls up to either a 7 or an 11.

The `else` Clause
------------
- The `else` clause in Python works as a _catch-all_ suite at the end of all the conditions which is achieved by adding an `else` clause towards the end of the code block.

_**Syntax:**_
```Python
else:
    suite
```

_**Example:**_
```Python
point = None
if d1+d2 == 7 or d1+d2 == 11:
    point = "Winner!!"
elif d1+d2 == 2 or d1+d2 == 3 or d1+d2 == 12:
    point = "Loser!!"
else:
    point = d1+d2
print(point)
```