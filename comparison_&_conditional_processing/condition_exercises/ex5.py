'''
Sort Three Numbers.
This is an exercise in constructing if-statements. Using only simple variables and if statements,
you should be able to get this work, a loop isn't needed.

Given 3 numbers (X, Y, Z) assign variables x, y, z so that x <= y <= z and x, y, z are from 
X, Y and Z. Use only a series of if-statements and assignment statements.

Hint. You must define the conditions under which you choose between x<-X, x<-Y or x<-Z. You 
will do a similar analysis for assigning values to y and z. Note that your analysis for setting y
will depend on the value set for x; similarly, your analysis for setting z will depend on values
set for x and y.
'''

X = 26
Y = 57
Z = 13

# if-else block for x
if X <= Y and X <= Z:
	x = X
	if Y <= Z:
		x = Y
	else:
		x = Z

# if-else block for y
elif X >= Y and Y <= Z:
	y = Y

# if-else block for z

print('x = ', x)
print('y = ', y)