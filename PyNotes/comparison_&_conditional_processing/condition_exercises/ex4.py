'''
Hardways.
Assume d1 and d2 have the numbers on 2 dice. A hardway proposition is 4, 6, 8 or 10 with
both the die having same value. It's the hard way to get the number. A hard 4, for instance
is d1+d2 == 4 and d1 == d2. An easy 4 is d1+d2 == 4 and d1 != d2.
'''

if (d1+d2 == 4 or d1+d2 == 6 or d1+d2 == 8 or d1+d2 == 10) and d1 = d2:
	print('Winner!!')