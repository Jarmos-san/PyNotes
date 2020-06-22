'''
Wind Chill. Wind Chill is used by meteorologists to describe the effect of cold and wind
combined. Given the wind speed in miles per hour, V, and the temperature in Farenheit, T, the
wind chill, w, is given by the formula below.

Wind Chill, new model
35.74 + 0.6215*T - 35.75*V**0.16 + 0.4275*T*V**0.16

Wind Chill, old model
0.081*(3.71*V**1/2 + 5.81 - 0.25*V)*(T-91.4) + 91.4

Wind speeds are for 0 to 40mph, above 40, the difference in wind speed doesn't have much practical
impact on how cold one would feel.

Write a print statement to compute the wind chill felt when it's -2 F and the wind is blowing 15mph.
'''
import math

#Temperature
T = -2

#Wind Speed
V = 15

#Wind chill
#Using new model formula
w_new = 35.74 + ((0.6215*T) - (35.75*math.pow(V, 0.16)) + (0.4275*T*math.pow(V, 0.16)))

#Using old model formula
w_old = 0.081*(3.71*math.sqrt(V) + 5.81 - 0.25*V)*(T-91.4) + 91.4

print('Wind chill with -2 F temperature and 15mph wind speed: ', int(w_new), 'F')
print('Wind chill with -2 F temperature and 15mph wind speed: ', int(w_old), 'F')