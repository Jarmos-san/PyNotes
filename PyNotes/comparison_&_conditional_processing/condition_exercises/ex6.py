'''
Come Out Roll.
Accept d1 and d2 as input. First, check to see that they're in proper range for dice. if not
print a message.

Otherwise, determine the outcome if this is a come out roll. If the sum is 7 or 11, print winner.
If the sum is 2, 3 or 12, print loser. Otherwise print the point.
'''

d1, d2 = int(input('Dice first value: ')), int(input('Dice second value: '))

if d1 in range(1,7):
	if d2 in range(1,7):
		pass
else:
	print('Input values within range 1-6')

if d1+d2 == 7 or d1+d2 == 11:
	print('Winner!!')
elif d1+d2 == 2 or d1+d2 == 3 or d1+d2 == 12:
	print('Loser!!')
else:
	print('Points: ', d1+d2)