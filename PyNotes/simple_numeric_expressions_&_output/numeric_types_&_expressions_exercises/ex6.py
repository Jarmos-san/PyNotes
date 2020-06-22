'''
Craps Odds. What are the odds of winning in the first throw of the dice?

There are 36 possible rolls on 2 dice that roll up to values from 2 to 12. There is just one way 
to roll a 2, 6 ways to roll a 7, 1 way to roll a 12. We'll take this as given until next exercise
where we've enough Python to generate this information. 

Without spending a lot of time on probability theory, there are two basic rules we'll use time and
again. If any of the multiple alternate conditions needs to be true, usually expressed as 'or', we
add the probabilities. When there are several conditions that must be true, usually expressed as 
'and', we multiply the probabilities. 

Rolling a 3, for instance, is rolling a 1-2 or rolling a 2-1. We add the probabilities: 
1/36 + 1/36 = 2/36 = 1/18.

On a come out roll, we win immediately if 7 or 11 is rolled. There are two ways to roll 11(2/36)
or 6 ways to roll 7(6/36).

Write a print statement to print the odds of winning on the come out roll. This means rolling 7 or
rolling 11. Express this as a fraction, not as a decimal number; that means adding up the numerator
of each number and leaving the denominator as 36.
'''

#Probability of getting a 7
prob_7 = str()
print('Probability of getting a 7: ', '1/36 + 1/36 + 1/36 + 1/36 + 1/36 + 1/36 =', '6/36')

#Probability of getting an 11
prob_11 = str(1/36 + 1/36)
print('Probability of getting an 11: ', '1/36 + 1/36 =', '2/36')