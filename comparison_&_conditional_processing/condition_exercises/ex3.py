'''
Field Win. 
Assume d1 and d2 have the numbers on 2 dice. The field pays on 2, 3, 4, 9, 10, 11 or 12.
Actually there are two conditions: 2 and 12 pay at one set of odds(2:1) and the other 5
number pays at even money. Write two conditions under which the field pays. 
'''
if d1+d2 == 2 or d1+d2 == 12:
	print('Field pays 2:1')
elif d1+d2 == 3 or d1+d2 == 4 or d1+d2 == 9 or d1+d2 == 10 or d1+d2 == 11:
	print('Field pays even money')
else:
	print('Loser!!')