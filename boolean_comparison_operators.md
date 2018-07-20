# Boolean and Compariso Operators

Contents:
- [Comparison Operators](https://github.com/Jarmos-san/PyNotes/blob/master/boolean_comparison_operators.md#comparison-operators)
- [Boolean Operators](https://github.com/Jarmos-san/PyNotes/blob/master/boolean_comparison_operators.md#boolean-operators)
- [Inverse Boolean](https://github.com/Jarmos-san/PyNotes/blob/master/boolean_comparison_operators.md#inverse-boolean)
- [Membership Operator](https://github.com/Jarmos-san/PyNotes/blob/master/boolean_comparison_operators.md#membership-operator)

Comparison Operators
----

```Python
# Less than Operator
<

# Greater than Operator
>

# Less than or Equal to
<=

# Greater than or Equal to
>=

# Outputs True when both elements are True
and

#Outputs True when either one element is True
or
```

Can be used in chain comparison operations.

**_Example:_**

```Python
24 >= 20 > 4 == 4 or 50 < 100 >40 != 40
True

"h" in var and "z" not in var3 and 10 > 4 != 50 and 4000 <= 5000
True
```


Boolean Operators
----

`True`: Numerical substitute is `1`.

`False`: Numerical substitute is `0`.

**_Example:_**

```Python
True
True

False
False

True == 1
True

False == 0
True

True and True
True

False and False
True

True and False
False

True or False
True

10 == 10
True

10 != 50
True

10 != 2
True

200 >= 2001
False

500 <= 3000
True

10 > 1 and 4 == 4
True

10 > 1 and 4 != 4
False
```

Inverse Boolean
----

The `not` statement is used to make inverse boolean output.

**_Example:_**

```Python
var = "house"
var2 = "cinema"
var3 = "temple"

"n" not in var
True

# Example of Chained Operations
"h" in var and "z" not in var3 and 10 > 4 != 50 and 4000 <= 5000
True
```
Membership Operator
-----
The `in` statement checks if a variable is available inside another variable or not.

**_Example:_**

```Python
var = "house"
var2 = "cinema"
var3 = "temple"

"o" in var
True

"n" in var
False

"n" not in var
True
```
