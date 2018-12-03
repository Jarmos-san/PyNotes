'''
Greatest Common Divisor. The greatest common divisor is the largest number which will evenly
divide two other numbers. 

Examples: GCD( 5, 10 ) = 5, the largest number that evenly divides 5 and 10. 
GCD( 21, 28 ) = 7, the largest number that divides 21 and 28. GCD’s are used to reduce fractions. 
Once you have the GCD of the numerator and denominator, they can both be divided by the GCD to 
reduce the fraction to simplest form. 21/28 reduces to 3/4.

Greatest Common Divisor of two integers, p and q

Loop 

Loop until p=q.
	swap. If p < q then swap p and q, pq.
	Subtract. If p > q then subtract q from p, p←p−q.
Result.
 Print p
 '''

 