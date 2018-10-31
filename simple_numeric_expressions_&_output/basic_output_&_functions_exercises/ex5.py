'''Illegal Conversions. Try illegal conversions like int('A') or int('3+4j'). Why are 
exceptions raised? Why can't a simple value like a zero or a None be used instead?
'''

#Raises ValueError: Invalid literal for int() with base 10: 'A'
conversion_1 = int('A')
print(conversion_1)

conversion_2 = int('3+4j')
print(conversion_2)

#Exceptions are raised to notify the dev of potential errors in code.
#The number 0 or None are sometimes used as Python objects and thus
#cannot be used for making way around bugs or errors.