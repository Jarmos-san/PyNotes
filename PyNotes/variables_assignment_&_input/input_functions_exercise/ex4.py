'''
Surface Air Consumption Rate. 
Write a short program will input the starting pressure, finalpressure, time and 
maximum depth. Compute and print the SACR
'''

#Diving exercise
#constant values
#starting pressure
s = int(input('What is the starting pressure?'))

#final pressure
f = int((input('What is the final pressure?')))

#SACR
c = int(input('What is the SACR?'))

#time
d1, d2 = int((input('Depth time?'))), int((input('Depth time?')))

#time estimates
t1 = (33*(s-f))/(c*(d1 + 33))
t2 = (33*(s-f))/(c*(d2 + 33))

print('To dive 60 ft it will take: ', int(t1), 'minutes')
print('To dive 70 ft it will take: ', int(t2), 'minutes')