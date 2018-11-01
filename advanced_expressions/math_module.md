# The `math` Module #

The `math` module is available using the `import math` statement. Some of the common functions are noted down as follows:

Trigonometric Functions
---------

- `acos(x)` - Returns an arc cosine of `x` in radians.
- `asin(x)` - Returns an arc sine of `x` in radians.
- `atan(x)` - Returns an arc tangent of `x` in radians.
- `atan2(y, x)` - Returns an arc tangent of `y/x` resulting in radians.
- `cos(x)` - Returns cosine of `x` in radians.
- `cosh(x)` - Returns an hyperbolic cosine of `x` in radians.
- `exp(x)` - Returns `e**x`, or an inverse of _log(x)_.
- `hypot(y,x)` - Returns the Ecludian distance `(x**2 + y**2)**1/2` or the lenght of the hypotenuse of a right angle triangle with height of _replaceable_ value in `y` and `x`.
- `log(x)` - Returns the natural logarithm(base e) of `x`.
- `log10(x)` - Returns the natural logarithm(base 10) of `x`.
- `pow(x, y)` - Returns the value of `x` with y as an exponent like so `x**y`.
- `sin(x)` - Returns the sine value of `x`.
- `sinh(x)` - Returns the hyperbolic sine value of `x` in radians.
- `sqrt(x)` - Returns the square root value of `x` in radians.
- `tan(x)` - Returns the tangent value of `x` in radians.
- `tanh(x)` - Returns the hyperbolic tangent of `x` in radians.

Floating-point Number Functions
-------------

- `ceil(x)` - Next larger whole number of the specified floating-number x.

```Python
>>>import math
>>>math.ceil(5.1)
6.0
>>>math.ceil(-5.1)
-5.0  
```

- `fabs(x)` - Absolute value of the real x.
- `floor(x)` - Next smaller whole number.

```Python
>>>import math
>>>math.floor(5.9)
5.0
>>>math.floor(-5.9)
-6.0
```

- `fmod(x, y)` - Returns a floating-point remainder after division of x/y.
- `modf(x)` - Creates a tuple with the fractional and the integer parts of x.

```Python
>>>math.modf(123.456)
(0.456, 123)
```

- `frexp(x)` - Returns an unwinded version of the usual base-2 floating point representation.
- `ldexp(m, e)` - Calculates m * 2**e, the inverse of `frexp(x)`.
