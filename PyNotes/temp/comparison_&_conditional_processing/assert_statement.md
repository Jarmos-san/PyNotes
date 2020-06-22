# The `assert` Statement

- An assertion is a condition where it's claimed that everything should be true at a certain point in the programme.
- It helps in reviewing the relationships between variables and other aspects of a code block, showing the effects of the `if` statements and the `for` or `while` loops.
- When a program is correct all the assertions are correct regardless of the input. While in case an error is raised atleast one assertion definitely ends up wrong.

_**Syntax:**_

```Python
assert condition

asset condition, expression
```
- If the _condition_ is true, the program is correct and the statement does nothing.
- if the _condition_ is false, the program halts raising an `AssertionError`.
