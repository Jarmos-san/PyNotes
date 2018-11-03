'''
Convert between |deg| C and |deg| F. Convert temperatures from one system to another. 
Conversion constants: 32 F = 0 C, 212 F = 100 C. The following two formalae converts 
between C(celsius) and F(Fahrenheit).

F = 32 + ((212-32)/100) * C
C = (F - 32) * (100/(212-32))

Create a print statement to convert 18 C to F.
Create a print statement to convert -4 F to C.
'''

#Farenheit conversion
print("F =", 32+(((212-32)/100)*18)) 
#Celsius conversion
print("C =", (-4-32)*100/(212-32)) 