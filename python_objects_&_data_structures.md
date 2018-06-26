# Python Objects & Data Structures
Might move indivual topics to their respective files later as per convinience and subject to how long this file might get over time.

Numbers
-----
Although Python accepts various types of numbers, these notes mainly focused on two types of numbers; **Integers**(`int`) and **Floating Point**(`float`). The remaing of the other types will added later as my convenience or feel free to make a PR, any sort of will be greatly appreciated!

- **Integers**(`int`) - Integers are just whole numbers, positive/negative. Refer to tbale below to see an example. 
 
- **Floating Pointing number**(`float`) - Floating point numbers on the other hand are denoted by numbers which has decimal points in them or with an exponential(e). Refer to table below to see an example.
							
| Example   |Number Type|
|-----------|-----------|
|1,2,-5,1000|	Integers|
|1.2,-0.5,2e2,3E2| Floating-point numbers|

Basic Arithmetic
-------

Python can perform basic arithmetic just like a nomral calculator would do. But on a side-note it's important to remember the arithmetic notations used and the differences between Python 2 and 3.

Examples given below:
```Python
# Addition
2 + 2
4

# Subtraction
3 - 4
-1

# Multiplication
2 * 2
4

# Division(in Python2)
4/2
2

# Division(in Python3.x)
4//2
2

# Exponents
2 ** 3
8

# Roots
2 ** 0.5			#Since square root can be represented as n^1/2

# Order of Operations
2 + 10 * 3 + 3
35

# Parenthesis are used to specify order
(2 + 10) * (3 + 3)
120
```

Assigning Variables
-----
Numbers can be assigned to variables.
The following rules are to be followed for assigning variables. While these list shows guidelines only for naming variables, the whole guide can be found at [PEP8](https://www.python.org/dev/peps/pep-0008/?#naming-conventions):
1. Names can not start with a number.
2. The underscore `_` is preferred over white-spaces.
3. Use of any of these symbols should be avoided at all cost `:'",<>/?|\()[email protected]#$%^&*~-+`.
4. Variable names are usually all lowercase.

Example:
```Python
# Created an object called "a" and assigned the number 15 to it
a = 5

# Calling "a" in a Python script would output "5" as a result
print(a)
5

# Variables can be added according to their variables
a + a
10

# variables can be reassigned
a = 10
a
10
```