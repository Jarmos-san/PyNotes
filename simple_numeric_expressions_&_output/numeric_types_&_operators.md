# Numeric Types and Operators

By default Python comes packed in with four built-in types of numbers: _**plain integers**_, _**long integers**_, _**floating point numbers**_ and _**complex numbers**_. These numbers can all be coerced from one type to another as well as be made available to the standard **arithmetic operators** mentioned as folows; 

Arithmetic Operators
---------

| Operator  |  Description                                         | Syntax |
|-----------|------------------------------------------------------|--------|
|  +  |  Addition: adds two operands                               | x + y  |
|  -  |  Subtraction: subtracts two operands                       | x - y  |
|  *  |  Multiplication: multiplies two operands                   | x * y  |
|  /  |  Division (float): divides the first operand by the second | x / y  |
|  // |  Division (floor): divides the first operand by the second | x // y |
|  %  |  Modulus: returns the remainder when first operand is divided by the second                                              | x % y  |

Logical Operators
-------------
Python provides three useful _Logical Operators_, namely, the **and**, **or** and **not**. This will be referenced further ahead as we progress more, available [here]]().

Ternary Operators
-------------
Ternary Operators also known as _conditional expressions_ are operators that evaluate based on the condition being `True` or `False`. It allows to test a single-line condition replacing the multi-line `if-else` code block. A detailed excerpt can be accessed [here]().

Plain Integers:
------
- Python integers are 32 bits long and it's range is -2,147,483,648 to 2,147,483.
- These integers are represented as strings of decimal digits and without punctuation or a leading zero.
- Python also supports programming in _binary_, _octal_ and _hexadecimal_.
    + Numbers with a leading '0' is considered _**octal**_ and uses to digits 0 to 7.
    + Numbers with a leading '0x' or '0X' are considered as _**hexadecimal**_ and uses the number 0 - 9, plus 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F'.
    + Numbers with leading '0b' or '0B' are considered as _**binary**_ and uses number 0 to 1.

Long Integers:
-----
- Contrary to _plain integers_, _long integers_ have longer arbitrary length and can represent an exact answer when required but operates slower than plain integers.
- Long integers are represented by a succeeding capital 'L' or a small' l' but Python can convert to long integers when required.
- Although, Python can convert between ultra-fast integers and slow-but-larger integers, an explicit conversion can be forced using the `int()` or `long()` function.

Floating-point Numbers:
-------
Floating-point Numbers are represented using 64 bits and are written in two forms: 
- A simple string of digits that includes a decimal point.
- A more complex form that includes an explicit exponent.

_**Example:**_
```Python
.0625
0.0625
6.25E-2
625E-4
```

Complex Numbers:
---------
- _**Complex Numbers**_ are created with adding a real number with an imaginary number like `2 + 14j`. 
- Python will always enclose these numbers with `()`, like `(2+14j)`.

_**References:**_

- [Building Skills in Python](http://www.itmaybeahack.com/book/python-2.6/latex/BuildingSkillsinPython.pdf#section.5.2)
- [Python 4 Astronomers](https://python4astronomers.github.io/python/types.html)
- [Real Python](https://realpython.com/python-data-types/)
- [Programmiz - Python Data Types](https://www.programiz.com/python-programming/variables-datatypes)
- [Linuxtopia - Python Numberic Types and Operators](https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch04s02.html)