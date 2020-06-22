'''
How much does the atmosphere weigh? Part 1. From Slicing Pizza, Racing Turtles and Further 
Adventures in Applied Mathematics, pressure is measured in Newtons, N, kg.mg/sec**2. Air
Pressure is measured in Newtons of force per square meter, N/m**2.

Air Pressure(at sea level), P0. This is the long-term average.
p0 = 1.01325*10**5

Acceleration is measured in m/sec**2. Gravity acceleration(at sea leve) g.
g = 9.82

We can use g to get the the kg of mass from the force of air pressure P0. Apply the acceleration
of gravity(in m/sec**2) to the air pressure(in kg.m/sec**2). The result is mass of the atmosphere
in kilograms per square meter(kg/m**2).
Mm**2 = P0*g

Given the mass of air per square meter, we need to know how many square meters of surface to apply
this mass to.
Radius of Earth R in metters, m. This is an average radius; our planets isn't a perfect square.
R = 6.37*10**6

The area of a sphere.
A = 4.pi.r**2

Mass of atmosphere(in kg) is the weight per square meter, times the number of square meters.
Ma = P0*g*A

Check: Somewhere around 10**18 kg.
'''
import math

# Air pressure(at sea level)
P0 = 1.01325*math.pow(10, 5)

# Gravity acceleration
g = 9.82

# Average radius of Earth
r = 6.37*math.pow(10,6)

# Earth surface area
# math.pi is a floating number and not a func so shouldn't use ()
A = 4*math.pi*math.pow(r,2)

# Mass of atmosphere
Ma = P0*g*A

print('Weight of atmosphere: ', Ma)