# String/Print Formatting

String/Print formatting can be prove to quite useful and at times time-saving for since it eliminates the need to manually concatenate strings with variables.
Although there are a number of way to accomplish this task, I'll keep adding more notes on to it as I come across more info.

- Print Formatting
    The basic type of print formatting is an example below.
    ```Python
    print('This is a string')
    'This is a string'
    ```
    
- String Formatting
	The `%s` can be used directly into the print statements to format a string without making any concatenations to it.
    ```Python
    foo = 'string'
    print('place another string with a modulus and foo: %foo' %(foo))
    ```
    
- Floating-Point Numbers
	To format floating-point numbers the syntax is `%n1.n2f` where `n1` is the number digits desired(leave empty for white space formatting) and the `n2` is number of decimal points desired.
    
    _Example_:
    
    ```Python
    Floating point numbers: 13.14
    print 'Floating point numbers: %1.2f' %(13.144)
	
    Floating point numbers: 13.14
	print 'Floating point numbers: %1.0f' %(13.144)
	
    Floating point numbers: 13
	print 'Floating point numbers: %1.5f' %(13.144)
	
    Floating point numbers: 13.14400
	print 'Floating point numbers: %10.2f' %(13.144)
	
    Floating point numbers:      13.14
	print 'Floating point numbers: %25.2f' %(13.144)
    ```
    
- Multiple Format Methods
	A tuple of multiple placeholder values can be passed to string format method within the print statements like the following
    
    ```Python
    print 'First: %s, Second: %1.2f, Third: %r' %('hi!',3.14,22)
	First: hi!, Second: 3.14, Third: 22
    ```
	
- Using the `str.format()` method
	`str.format()` is a popular method of formatting strings and print statements flawlessly. The syntax is also quite simple and the ease of use has made it quite popular.
    _Syntax_
    
    ```Python
    'String here {var1} then also {var2}'.format(var1='something1',var2='something2')
    ```
    _Example_
    
    ```Python
    print 'This is a string with an {p}'.format(p='insert')
	This is a string with an insert

	# Multiple times:
	print 'One: {p}, Two: {p}, Three: {p}'.format(p='Hi!')
	One: Hi!, Two: Hi!, Three: Hi!

	# Several Objects:
	print 'Object 1: {a}, Object 2: {b}, Object 3:{c}'.format(a=1,b='two',c=12.3)
	Object 1: 1, Object 2: two, Object 3: 12.3
    ```
    
- F-Strings(**Can be used only for Python3.6+**)
	Use of `f-strings` are usually recommended but can be used only for Python3.6 and later **ONLY**. The syntax is also simple and infact the easiest and probably the most readable among all the the string formatting methods.
**I personally prefer using the `f-strings` over the older `str.format()` method.**

    _Syntax_
    
    ```Python
  name = "Fred"
  f"He said his name is {name!r}."
  "He said his name is 'Fred'."

  f"He said his name is {repr(name)}."  # repr() is equivalent to !r
  "He said his name is 'Fred'."
  
  width = 10
  precision = 4
  value = decimal.Decimal("12.34567")
  f"result: {value:{width}.{precision}}"  # nested fields
  'result:      12.35'
  
  today = datetime(year=2017, month=1, day=27)
  f"{today:%B %d, %Y}"  # using date format specifier
  'January 27, 2017'
  
  number = 1024
  {number:#0x}"  # using integer format specifier
  '0x400'
    ```
For more information on `f-strings` refer to the [documentation](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals) and the [PEP498](https://www.python.org/dev/peps/pep-0498/?#id23) guidelines.
