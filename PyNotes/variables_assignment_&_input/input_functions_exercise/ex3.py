'''
Periodic Payment. 
Input the principal, annual percentage rate and number of payments. Compute
the monthly payment. Be sure to divide rate by 12 and multiple payments by 12.
'''

# Mortgage exercise
#principal
p = int(input('How much is your principal amount?'))
#monthly interest rate
r = int(input('Rate of interest?')) / 12
#number of monthly payments
n = int(input('How long do you wish to keep it?')) * 12
#formula - I
m1 = p * r/(1-(1+r)**-n)
#formula - II
m2 = -r*p*(r+1)**n/(r+1)**n-1 
#formula - III
m3 = (-r*p*(r+1)**n)/((r+1)**n-1)*(r+1)

print('Cost of mortgage = ', int(m1))
print('Mortgage with payments due at the end of each period = ', int(m2))
print('Mortgage with paymens due at the beginning of each period = ', int(m3))