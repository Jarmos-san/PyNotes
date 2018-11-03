'''
Surface Air Consumption Rate. SACR is used by SCUBA divers to predict air used at a particular
depth. For each dive, we convert our air consumption at that dive's depth to a normalised air
consumption at the surface. Given depth(in feets), d, starting tank pressure(psi), s, final tank
pressure(psi), f, and time(in minutes) of t, SACR, c, is given by the following formula;

c = (33*(s-f))/(t*(d+33))

Typical values for pressure are a starting pressure of 3000 and final pressure of 500.

A medium dive might have a depth of 60 feet, time of 60 minutes.

A deeper dive might be of 100 feet for 15 minutes.

A shallower dive might be 30 feet for 60 minutes, but the ending pressure might be of 
1500. A typical c(consumption) value might be 12 to 18 for most people.

Given SACR, c, and a tank starting pressure, s, final pressure, f, we can plan a dive to depth
(in feet), d, for time, t(in minutes), using the formula. Usually the 33*(s-f)/c is a constant,
based on your SACR and tanks

33*(s-f)/c = t*(d+33)

For example, tanks you own might have a starting pressure of 2500 and ending pressure of 500, 
you might have a c(SACR) of 15.2. You can then find possible combinations of time and depth which
you can comfortably dive.

Write two print statements that shows how long one can dive at 60 feet and 70 feet.
'''

print('To dive 60 ft it will take: ', int((33*(2500-500))/(15.2*(60 + 33))), 'minutes')
print('To dive 70 ft it will take: ', int((33*(2500-500))/(15.2*(70 + 33))), 'minutes')