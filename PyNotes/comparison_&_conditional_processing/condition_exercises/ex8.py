'''
Hardways Roll.
Accept d1 and d2 as input. First check to see if they're in proper range for the dice. If not
print a message.

Otherwise check for a hard ways bet pay out. Hard 4 and 10 pays 7:1; Hard 6 and 8 pays 9:1;
easy 4, 6, 8 or any 7 loses. Everything else, the bet still stands.
'''

d1, d2 = int(input('Dice 1 value: ')), int(input('Dice 2 value: '))

if d1 in range(1,7):
	if d2 in range(1,7):
		pass
else:
	print('Dice value out of range. Should be within 1-6!')


#####################
# Dont understand how to play Hardways Roll.
# Will get back to this exercise later.
#####################