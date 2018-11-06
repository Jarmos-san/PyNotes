'''
Field Roll.
Accept d1 and d2 as input. First check to see they're in proper range for dice. If not print
a message.

Otherwise, check any for any field bet pay out. A roll of 2 or 12 pays 2:1, print "pay 2"; 3, 4, 9,
10, 11 pays 1:1, print "pays even"; everything else loses, print 'loses'.
'''

d1, d2 = int(input('Value for first dice: ')), int(input('Value of second dice: '))
if d1 in range(1,7):
	if d2 in range(1,7):
		if d1+d2 == 2 or d1+d2 == 12:
			print('Pays 2')
		elif d1+d2 == 3 or d1+d2 == 4 or d1+d2 == 9 or d1+d2 == 10 or d1+d2 == 11:
			print('Pays even')
		else:
			print('Loses!!')
else:
	print('Dice value should be in range 1-6!')