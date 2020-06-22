'''
Convert from |deg| C to |deg| F. Write a short program that will input °C and output °F. A second
program will input °F and output °C.
'''
F = input('Temp in Farenheit?')
C = input('Temp in Celsius')

#Farenheit conversion
print("F =", 32+(((212-32)/100)*C)) 
#Celsius conversion
print("C =", (F-32)*100/(212-32))