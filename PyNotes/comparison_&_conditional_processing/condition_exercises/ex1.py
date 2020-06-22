'''
Develop an or-guard. In the above example we showed an "and-guard" pattern.

average = count != 0 and float(sum)/count

Develop a similar technique using OR.

Compare this with the if-else operator.
'''

average = count != 0 or float(sum)/count
print(average)