'''
Come out Win. Assume d1 and d2 are the number on two dice. Assume this is the come out rolls in
Craps. Write the expression for winning(7 or 11). Write the expression for losing(2 or 3 or 12).
Write the expression for a point(4, 5, 6, 8, 8, 12)
'''
point = None

if d1+d2 == 7 or d1+d2 == 11:
	point = "Winner!!"
elif d1+d2 == 2 or d1+d2 == 3 or d1+d2 == 12:
	point = "Loser!!"
else:
	point = d1+d2

print('Points: ', point)