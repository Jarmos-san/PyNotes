# Variables

- Variables are names the program assigns to the results of the various expressions which enable us to identify new objects and the state of those objects.
- Variables can have three state changes: _**variable creations**_, _**object assignment**_, _**object change**_, which indicates when the program can exit.
- Points to keep in mind about creating variables:
    + Python variables **MUST** contain atleast one letter and can have a string of numbers, letters or even `_`'s to any length.
    + Names that start with `_` and ends with another `_` has special significance and shouldn't be used elsewhere.
    + The new variables are assigned after an expression using the **assignment** statement which can also be deleted using the **del** statement.
- Python variables are just more than any labels as they carry certain consequences alongwith them.
    + Multiple variables referring to a common mutable object can change the state of the common object.
    + Python object fully defines it's own _type_ according to it's representation, range of values and allowed operations on the object.
    + Variables referring to objects can be independent of the object itself which means that variables that are in distinct namespace can reference to the same object.
- Python assigns a name to every variable object and it's visibility is considered as the _scope_. A variable with a _global scope_ can be referenced anywhere while one with a _local scope_ can only be referenced with a limited suite of statements.
- Python also collects every variable into seperate pools, called _namespaces_. These are created as part of evaluating a body of a function or an object. Thus there's one single _**global**_ namespace and numerous _**local**_ namespaces.

Assignment
-------
- _**Assignment**_ statements are used prominently for the purpose of preserving objects created by an expression.
- There're three types of assignment:
    + Basic assignment, _**syntax:**_ `variable = expression`.
    + Augmented assignment, _**syntax:**_ `variable += expression`.
    + Multiple assignment which can assign multiple variables at a time considering both sides has equal number of elements. _**Example:**_ `x1, x2 = 2,3`