'''
How Much Does The Atmosphere Weigh? Part 2. From Slicing Pizzas, Racing Turtles, and 
Further Adventures in Applied Mathematics,[Banks02].

The exercise How Much Does the Atmosphere Weigh, Part 1 assumes the earth to be an 
entirely flat sphere. The averge height of the land is actually 840m. We can use the 
ideal gas law to compute the pressure at this elevation and refine the number a little further. 

Pressure at a given elevation
P = P0*e**((mg/RT)*z)

Molecular weight of air, m = 28.96*10**-3kg/mol.
m = 28.96*10**-3

Gas constant, R, in joule/(K.mol).
R = 8.314

Gravity, g, in m/sec**2.
g = 9.82

Temperatur, T, in K(kelvin) based on temperature C in C(celsius). We'll assume that is 15 C.
T = 273 + C

Elevation z in meters, m.
z = 840

This pressure can be used over land, and the pressure computed in How much does the atmosphere Weigh
in Part I can be used for the air over the oceans. How much land has this reduced pressure?
Reference materials gives the following areas in m**2, square meters.

ocean area = A0 = 3.61*10**14
land area = A1 = 1.49*10**14

Weight of atmosphere, adjusted for land elevation
M1 = P0*g*A0 + P*g*A1
'''
import math

# Air pressure(at sea level)
P0 = 1.01325e5

# Gravity acceleration
g = 9.82

# Pressure over ocean(A0) and land(A1)
A0 = 3.61e14
A1 = 1.49e14

#land elevation
z = 840

# Molecular weight of air
m = 28.96e-3

# Gas Constant
R = 8.314

# Temperature
C = 15 #temp in Celsius
T = 273 + C #temp in Kelvin

# Pressure at elevation
P = P0*pow(math.e, (m*g/R*T)*z)

# Weight of atmoshere adjusted for land elevation
M1 = (P0*g*A0) + (P*g*A1)

print('Adjusted weight of atmosphere over land: ', M1)