# The `random` Module #

The `random` module contains a large number of functions for working with distributions of random numbers on Python and these numbers can be accessed using the `import random` statement. Some of the commonly used functions are:

- `choice(sequence)` - Chooses a random number from the sequence _sequence_.

```Python
>>>import random
>>>random.choice( ['red', 'black', 'green'] )
'red'
```

- `random()` - A random floating point number, _r_, such that 0 <= _r_ <= 1.0
- `randrange(start, stop, step)` - Returns a random number from `range(start, stop, step)`.
- `randint()` - Returns a random number, _r_, such that _a_ <= _r_ <= _b_ but includes both endpoints unlike `randrange()`.
- `uniform(a, b)` - Returns a random floating-point number, _r_ such that _a_ <= _r_ <= b.