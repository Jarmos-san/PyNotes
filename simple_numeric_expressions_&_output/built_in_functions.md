# Built-in Functions

Math Functions
------
- `abs(number)` - Returns the absolute value of the argument.
- `pow(x, y)` - Raise x to the y power, `x**y`.
- `round(number, digits)` - Round a _floating-point number_ to _ndigits_ beyong the decimal point.

String Functions
---------
Providing alternate representations of numeric values this list of functions expands on the _Numeric Conversion Functions_.
- `hex(number)` - Creates a _hexadecimal_ string representation of a number with a leading `0x` specifying that the string representation is a hexadecimal.

```Python
>>>hex(684)
'0x2ac'
```

- `oct(number)` - Creates _octal_ string representation of a number with a leading `0` specifying that the string is an octal and not a decimal.

```Python
>>>oct(509)
'0775'
```

- `bin(number)` - Creates a _binary_ representation of a number with a leading `0b` specifying that the string is a binary.

```Python
bin(509)
'0b111111101'
```

- `int(string, base)` - Creates an integer from a string `x`, where `x` must be a string in the given base. Default value of base is set _decimal_ if omitted.

```Python
>>>int('0775', 8)
509
>>>int('0x2ac', 16)
684
>>>int('101101101101', 2)
2925
```

- `str(object)` - Creates a string representation of an _object_. Used for more readability.
- `repr(object)` - Creates a string representation of an object but unlike the `str()` method, the `repr()` is much more unambiguous and focuses on containing the object's information.

Collection Function
---------
- `max(value, ...)` - Returns the largest value.

```Python
>>>max(1, 2, ,3)
3
```
- `min(value, ...)` - Returns the smallest value.

```Python
>>>min(1, 2, 3)
1
```

_**References:**_
- [Stack Overflow](https://stackoverflow.com/a/2626364/8604951)
- [Corey Schafer - Python Tutorial: `str()` vs `repr()`](https://www.youtube.com/watch?v=5cvM-crlDvg)