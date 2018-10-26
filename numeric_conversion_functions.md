# Numeric Conversion Functions

Python can explicitly convert a number from one type to another although with a bit of a loss of precision. Since Python Python explicitly reduces the number of bits available or even adds bits which mightn't have any meaning to it. 

`int(x)`
-----
- This function generates an **integer** from the object `x`. 
- Truncates the digits towards the right of the decimal point if a floating-point is given.
- Complex numbers are converted directly.
- If `x` is a string, the `int()` function parses the string into an integer with an optional positive(+)/negative(-) sign.

_**Example:**_

```Python
>>>int('1234')
1234
>>>int(3.14159)
3
```

`float(x)`
--------
- This function generates a **float** from the object `x` and the object can be integer or a long integer which will be converted to a floating-point number automatically.
- Although **complex numbers** can't be turned into a float directly.
- Strings can also be converted into a float considering it must be a string of digits with an optional positive(+)/negative(-) sign.
- A string can be also be in the scientific notation and include an 'e' or 'E' followed by the exponent of the simple signed integer value.

_**Example:**_
```Python
>>>float(23)
23.0
>>>float("6.02E24")
6.0200000000000004e+24
>>>float(22/7)
3.14285714286
```

`long(x)`
---------------
- Generates a **long integer** from the object `x`.
- If `x` is a floating number, digits to the right of the decimal points are truncated as part of creating a long integer and replaced with an 'L'.

_**Example:**_
```Python
>>>long(2)
2L
>>>long(6.02E23)
601999999999999995805696L
>>>long(2**64)
18446744073709551616L
```

`complex(real, [imag])`
------------
- A complex number function has two parts, a _real_ and an _imaginary_.
- This generates a **complex number** from a _real_ and _imag_. When the _imag_ part is omitted, the default value is `0.0`
- This function can be called in different variations;
    + Two numeric parameters.
    + One numeric(so default _imag_ value is `0.0`). 
    + One string parameter

_**Example:**_
```Python
>>>complex(3,2)
(3+2j)
>>>complex(4)
(4+0j)
>>>complex("3+4j")
(3+4j)
```
