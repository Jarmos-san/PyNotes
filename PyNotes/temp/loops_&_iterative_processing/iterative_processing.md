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
- The `for` statement in Python iterares over the items of a sequence which could be a list, a string or a string. The list created from the `range()` function is quite often used by the `for` statement to iterate over.

_**Syntax:**_
```Python
for variable in iterable:
    statement(s)
```
- The syntax shows a `for` statement followed by an indented block. The indented block can contain any number of statements or even other indented `for`/`if` statements.
- Although there're a number of ways to create the necessary iterable collection to be used within the `for` statement, the `range()` function is used quite often as mentioned in the example [here]().

_**Example:**_
```Python
for var in range(5):
    print(var)

#Output 
0
1
2
3
4
```

The `while` Statement
----------
The `while` statement, in Python repeatedly executes a target statement as long as the given condition is `True`. The condition can be any given expression and when it's `False`, the `while` statement stops execution immediately.

_**Syntax:**_
```Python
while expression:
    statement(s)
```

_**Example:**_
```Python
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")
```

_Output:_
```Python
The count is: 0
The count is: 1
The count is: 2
The count is: 3
The count is: 4
The count is: 5
The count is: 6
The count is: 7
The count is: 8
Good bye!
```

_**References:**_
- [thefourtheye's Answer on Stack Overflow](https://stackoverflow.com/a/19389957/8604951)
- [Aaron Hall's Answer on Stack Overflow](https://stackoverflow.com/a/39711683/8604951)
- [`for` Loop Statements - Tutorialspoint](https://www.tutorialspoint.com/python3/python_for_loop.htm)
- [`while` Loop Statements - Tutorialspoint](https://www.tutorialspoint.com/python3/python_while_loop.htm)
- [`while` Loops - Python Tutorial](https://www.python-course.eu/python3_loops.php)