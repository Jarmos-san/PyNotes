# Functions
A _**Function**_ can be considered as a sequence of statements that performs certain specific computation which is named. Once the function is defined which basically means specifying a name for the function followed by the sequence of statements, it can be _**called**_ by the name.

- Creating a function gives an oppurtunity to name a group of statements enabling it to be more legible.

- Function make programs much more shorter and eliminates the need to repeat certain codes making it easier to change something all in one place.

- Dividing a long program into functions makes debugging easier.

- Well designed functions can be reused mutlple times for more than one programs. 

## Content
- [Functions Calls](https://github.com/Jarmos-san/PyNotes/blob/master/functions.md#function-calls)

- [Math Functions](https://github.com/Jarmos-san/PyNotes/edit/master/functions.md#math-fnctions)

- [Composition](https://github.com/Jarmos-san/PyNotes/edit/master/functions.md#composition)

- [Adding New Functions](https://github.com/Jarmos-san/PyNotes/edit/master/functions.md#adding-new-functions)

- [Defintions and Uses](https://github.com/Jarmos-san/PyNotes/edit/master/functions.md#definitions-and-uses)

- [Flow of Execution](https://github.com/Jarmos-san/PyNotes/edit/master/functions.md#flow-of-execution)

- [Variables, Parameters & Arguments](https://github.com/Jarmos-san/PyNotes/blob/master/functions.md#variabes-parameters--arguments)

- [Fruitful Functions and Void Functions](https://github.com/Jarmos-san/PyNotes/blob/master/functions.md#fruitful-functions--void-functions)


Function Calls
----
An example of a _**function call**_ would be as follows:

```Python
type(42)
<class 'int'>
```
The aforemention function is named as `type` which accepts one _**argument**_ inside parentheses and returns a value which is also known as the _**return value**_.

Math Functions
-----
Python already has certain built-in functions that can be _**imported**_ or called. One such example is the **Math Module** which is basically a file containing te collection of mathematical functions. But before these in-built functions can be used it's necessary to import it with an _**import statement**_. Like this:
```Python
import math
```
The above statement creates a _**module object**_ named math which enables the user to call every function within the math module. To access those functions, it's necessary to specify the name of the module and the name of the function seperated by a dot. This format is called the _**dot notation**_.

Example:
```Python
ratio = signal_power / noise_power
#math.log10 is the function
decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)
```

Composition
-----
A function can accept any other kind of expressions as an argument as well. For an instance;
```Python
x = math.sin(degrees / 360.0 * 2 * math.pi)

x = math.exp(math.log(x+1)
```
**NOTE: **But it's important to take care that the left side of the assignment statement has to be a variable name.

Adding New Functions
----
As mentioned earlier a function can defined by specifying the name of the function and the sequence of computation following it. This is known as the _**function definition**_.

_Example:_
```Python
def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print("I sleep all night and work all day.")
```
In the above example, the first like is called the _**header**_ and the lines succeding it is called the _**body**_. The header always ends with a `:` colon and the body have to be properly indented.

The first word used in the header of the function definition, `def` is a keyword that indicates that this is a function and `print_lyrics` is the function name. 

**NOTE:** The function names can start with _letters_, _numbers_ or _underscore_ but the first character of the function name shouldn't be a number.

Towards the end of the header are two `()` parantheses indicating that the function doesn't accept any arguments.

This way a _**function object**_ can be created which has type `function` and when called can be used inside another function.

_Example:_
```Python
def repeat_lyrics():
	print_lyrics()
	print_lyrics()
```	

Definitions and Uses
-----
Putting the above mentioned examples into one whole program, it should look like this;
```Python
def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print("I sleep all night and I work all day")
	
def repeat lyrics():
	print_lyrics()
	print_lyrics()
	
repeat_lyrics()
```
As observed the program contains two function definitions, namely `print_lyrics` and `repeat_lyrics` which would get executed just like any other statements but the statements inside the function wouldn't run until the function is called. Thus it's quite obvious that a function needs to be created before it can even run. So as part of an exercise if the function `repeat_lyrics()` is moved towards the beginning of the program, the following error would show up.
```Python
NameError: name' repeat_lyrics' is not defined
```

Flow of Execution
-----
It's important to keep in mind the order of statements run in so that the functions are executed smoothly. In order to achieve that the _**flow of execution**_ is followed. Since execution always begins at the first statement of the program and the statements are run one at a time.

A function when called usually takes a detour in the flow of execution and instead of going to the next statement, the flow jumps to the body of the function executing the statements inside the body and returning back to where the program picked up from.

Variabes, Parameters & Arguments
-----
Certain functions accept arguments and certain functions take more than one argument. Inside the function arguments are passed on to variables called _**parameters**_. 

_Example:_
```Python
# bruce is the parameter here
def print_twice(bruce):
	print(bruce)
	print(bruce)
```
The above example where a function `print_twice` is defined accepts an argument and the assigns it to a parameter named `bruce`. When the function is called, the value of the parameter is printed out twice.

_Example:_
```Python
# the string "spam" is assigned to the parameter "bruce"
print_twice(spam)
spam
spam
```

**NOTE:** The name of the variable passed as the argument has nothing to do with the the name of the parameter, in these case which was `bruce`. Also _parameters_ are local.

When a variable is created inside a function, it's considered **local** which means that it exists only inside the function.

_Example:_
```Python
def cat_twice(part1, part2):
	# Following part is local
	cat = part1 + part2
	print_twice(cat)

# Following variables are global
line1 = 'Bing tiddle'
line2 = 'tiddle bang'
cat_twice(line1, line2))
Bing tiddle tiddle bang
Bing tiddle tiddle bang
```
Thus it's obvious that calling `cat_twice` would destroy the variable `cat` and Python would raise an exception if we tried to print the variable `cat`.

Fruitful Functions & Void Functions
-----
Certain functions return results while some don't which are called _**fruitful functions**_ and _**void functions**_ repsectively, the former usually performs an action and isn't expected to return a value. 

When a _fruitful function_ is called, the return value can be stored into a variable or use it as part of an expression. 

**NOTE:** While in a script, a fruitful function is called all by itself, the return value is lost since it doesn't store the value or display the result.

While on the other hand _void functions_ might display certain things on the screen or have some effect after the computation is done but doesn't return a value. Printing the result of a _void function_ would return a special value called `None`

_Example:_
```Python
# print_twice performs an action and doesn't return a value
result = print_twice('Bing')
Bing
Bing

print(result)
None
```

**NOTE:** The string `'None'` is different from the value `None` since it's a special value and has it's own type.
```Python
type(None)
<class 'Nonetype'>
```

