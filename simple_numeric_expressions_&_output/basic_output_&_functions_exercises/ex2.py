'''
Evaluate and Print Expression. Write short scripts
to print the results of the following expressions.
In most places, changing integers to floating point
numbers produces a notably different result. For example
'(296/167)**2' and '(296.0/167.0)**2'. Use long as well as
complex types to see the difference.

- '355/113 * (1 - 0.0003/3522)'
- '22/17 + 37/47 + 88/83'
- '(553/312)**2'
'''

#print(complex('355/113*(1-0.0003/3522)'))
print(long('355/113*(1-0.0003/3522)'))

#print(complex('22/17+37/47+88/83'))
print(long('22/17 + 37/47 + 88/83'))

#print(complex('(553/312)**2'))
print(long('(553/312)**2'))