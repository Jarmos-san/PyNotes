# Strings

Content:
- [String Functions & Indexing](https://github.com/Jarmos-san/PyNotes/blob/master/strings.md#string-functions-and-indexing)
- [String Properties](https://github.com/Jarmos-san/PyNotes/blob/master/strings.md#string-properties)
- [String Methods](https://github.com/Jarmos-san/PyNotes/blob/master/strings.md#string-methods)
- [String Formatting](https://github.com/Jarmos-san/PyNotes/blob/master/strings.md#string-formatting)

Strings in Python are considered as "Sequences" to record text information which is rather useful to keep track of every elements in the string as a sequence. Thus strings can be manipulated/grabbed according to their index as Python interprets the sequence of elements in a string as an "immutable" order of arrangements.

A "string" can be created by wrapping a word within `" "/' '`(double/single quotations) 
Example:

```Python
# single word
'hello'

'hello'

# entire phrase
'This is a string'

'This is a string'

# printing strings
print('Hello World 1')
print ('Hello World 2')
print ('Use \n to print a new line')
print ('\n')
print ('See what I mean?')

Hello World 1
Hello World 2
Use 
to print a new line

See what I mean?
```

String Functions and Indexing
----
- `len()` can be used to check the length of a string
	_Example_:
	
	```Python
	len('hello world')
	11			# Even white spaces are counted as characters
	```

- Since Python stores strings as a sequence of elements, those strings can be indexed. Also something to be noted is that Python indexing starts at 0.

	- Indexing
	    
	    _Example_
	    
		```Python
		# assigning string value to a variable
		foo = 'hello world'
		```
		
	 - String Slicing
	    
	    _Example_ 
    		
		```Python
    		s[0]
    		'h'				# since h is the first index of the string variable 's'
    		s[3]
    		'l'
    		```

	 - Slicing
	The `:` can be used to perform string slicing as shown in the example below
			
    ```Python
    s = 'hello world'
    
    # grab everything to first index mentioned towards the end of the string
    s[1:]
    'ello world'
    
    # grab everything from the start to the mentioned index
    s[:3]
    'hel'
    
    # grab everything from start to beginning
    s[:]
    'hello world'
    
    # grab everything from the last index of the string
    s[-1]
    'dlrow olleh'
    
    # grab everything but with two steps
    s[::2]
    'hlowrd'
    
    # grab from the end
    # can be used to check for palindromes
    s[::-1]
    'dlroW olleH'
    ```

String Properties
------
- As mentioned earlier strings are _immutable_ which means that once created the elements of a string cannot be changed or created anew.
	
	_Example_:
	
    ```Python
    foo = 'hello world'
    s[0] = 'c'

    TypeError                              Traceback (most recent call last)
    <ipython-input-49-3a9c668aa5ab> in <module>()
          1 # Let's try to change the first letter to 'x'
    ----> 2 s[0] = 'x'

    TypeError: 'str' object does not support item assignment
    ```
As expected trying to change an element of a string would raise an error.

- Strings can be concatenated as well.
	
	_Example_:
    ```Python
    foo = 'hello world'
    
    foo + 'concatenate me!'
    'hello world concatenate me!'
    
    # string can be reassigned
     foo = foo + 'concatenate me'
     print('foo')
     'hello world concatenate me!'
    ```

- String repetition!
 	
	_Example_:
    ```Python
    foo = z
    foo * 5
    'zzzzz'
    ```
    
String Methods
----
Since everything in Python is an `object` strings as well, special built-in methods can be performed on the object itself.

_Example_:
```Python
foo = 'Hello World'

# upper case a string
foo.upper()
'HELLO WORLD'

# lower case a string
foo.lower()
'hello world'

# split string according to white spaces(by default)
foo.split()
'Hello', 'World'

# split() can also be used on specific elements
foo.split(W)
'Hello orld'
```

String Formatting
-----
The `.format()` method can be performed on strings to add formatted objects to the print statements

_Example_:
```Python
'Insert another string with curly brackets: {}'.format('The inserted string')
'Insert another string with curly brackets: The inserted string'
```
Refer to the [String Formatting methods](https://github.com/Jarmos-san/PyNotes/blob/master/string_formatting.md) notes for more information and proper usage of various `format` methods

_**Important Notes:**_
- The `print()`function is **NOT** a function in Python 2, rather it's a **STATEMENT**

```Python
# Python2 print syntax
print 'hello world'

# Python3 print syntax
print('hello world')
```
- There are various other ways to format a string which will be added later.
