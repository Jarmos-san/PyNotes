'''
Periodic payment on Loan. How does a loan really cost?

Here are the versions of the standard mortgage payment calculations,
with m = payment, p = principal due, r = interest rate, n = number of payments.

Don't be surprised by the sign of the results; they're opposite the sign of the 
principle. With a positive principle, you get a negative number; you are paying a
down a principle.

formula - I
m = p * (r/(1-(1+r)**-n))

formula - II
Mortgage with payments due at the end of each period:
m = (-r*p(r+1)**n)/((r+1)**n-1) 

formula - III
Mortgage with paymens due at the beginning of each period:
m = (-r*p(r+1)**n)/((r+1)**n-1)*(r+1)

Use any of these forms to calculate the mortgage payments, m, due with principal, p, 
of $110,000, an interest rate, r, of 7.25% annually, and payments, n, of 30 years.
Note that banks actually process things monthly. So you'll have to divide 
the interest by 12 and multiply the number of payments by 12.
'''

print('Cost of mortgage = ', int(110000 * ((7.25/12)/(1 - (1+(7.25/12))**-(30*12)))
print('Mortgage with payments due at the end of each period = ', int(-(7.25/12)*110000*((7.25/12)+1)**(30*12)/((7.25/12)+1)**(30*12)-1))
print('Mortgage with paymens due at the beginning of each period = ', int((-(7.25/12)*110000*((7.25/12)+1)**(30*12)/(((7.25/12)+1)**(30*12-1)*((7.25/12)+1)))