'''
Evaluate and Print Built-in Conversion Functions. Here are some more expressions for which
you can print the results.

- hex(1234)
- int(hex(1234), 16)
- long('0xab')
- int('0xab')
- int('0xab', 16)
- int('ab', 16)
- cmp(2, 3)
'''

print('Hexadecimal value: ', hex(1234))
print('Integer value of the above Hexadecimal value: ', int(hex(1234), 16))

#this isn't applicable to Python3 anymore
#print(long('0xab'))

#this raises an error
#print('Integer value: ', int('0xab'))

print('Integer value with base 16: ', int('0xab', 16))
print('Integer value: ', int('ab', 16))

#this raises an error
#print('Complex number: ', cmp(2, 3))