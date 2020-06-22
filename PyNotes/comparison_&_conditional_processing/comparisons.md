# Comparisons

Basic Comparison
-----------
- Basic comparison corresponding to the similar mathematical functions like, _less than_, _less than or equal to_, _greater than_, _greater than or equal to_, _equal to_ and _not equal to_ represented as `<`, `<=`, `>`, `>=`, `==`, `!=` respectively.

Partial Evaluation
------------
- Logical operators, comparisons and math can be combined to perform _partial evaluations_ to prevent common mathematical mistakes like dividing by zero or the square root of a negative number, ect.

_**Example:**_
```Python
#returns error since dividing by 0
sum, count = 0, 0
average = sum/count
print(average)

#way around, average will print only if left-side expression is True
average = count != 0 and sum/count
print(average)
```

- The above example shows how `average` will only be evaluated if the right-side expressions evaluates to `True`

Floating-point comparisons
--------------------

Exact equality between tow floating-point number isn't always possible and certainly prone to various errors. Since certain repeating digits after the decimal point are truncated and are accumulated moving towards the left-side of the decimal point, thus the final floating-point number is represented as a real number with only a finite amount of binary precision. The following example is best to explain the situation of the floating-point number comparisons.

_**Example:**_ 

```Python
#!/usr/bin/env python
# Are two floating point values really completely equal?
a,b=1/3.0, 0.1/0.3
print(a, b, a==b)
print(abs(a-b)<0.00001)
```
When excuted displays this output

```
$ python floatequal.py
0.333333333333 0.333333333333 False
True
```