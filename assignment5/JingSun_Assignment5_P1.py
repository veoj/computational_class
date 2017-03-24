# Problem 1: Munich fitting



import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit

data = np.loadtxt("/home/jing/chuan/munich2008_2012.txt",float)
x_year=data[:,0]
y_temp=data[:,1]

guess_amplitude=np.std(y_temp)
guess_phase=0
guess_offset=np.mean(y_temp)

p0=[guess_amplitude,guess_phase,guess_offset]

def my_fit(x,amplitude,phase,offset):
    return np.cos(x*2*np.pi+phase)*amplitude+offset

# f(t)=a*cos(2*pi*t+b)+c

fit=curve_fit(my_fit,x_year,y_temp,p0=p0)

data_fit=my_fit(x_year,*fit[0])

plt.plot(x_year,y_temp,'.')
plt.plot(x_year,data_fit,label='after fitting',color='red',linewidth=3.0)
plt.legend()
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.title("Munich")
plt.xlim(range(2008,2012))
plt.ylim(-20,40)
plt.xticks(range(2008,2014),('2008','2009','2010','2011','2012','2013'))

plt.show()

print(p0)

print(np.mean(y_temp))
print(np.mean(data_fit))

print(np.max(data_fit))
print(np.min(data_fit))

print(my_fit(0,8.5,0,9.35))



# (a) 
# The best-fit values of the parameters are as below:
# a=8.50, b=0, c=9.35



# (b) 
# The average temperature in Munich is: 9.35234901271
# The average temperature in model is: 9.35234901349
# This two values are very close.

# The highest temperature (hottest time) predicted by the model is: 19.37
# The lowest temperature (lowest time) predicted by the model is: -0.67



# (c)
# The parameter b is the initial phase (phase offset) of this cosine function.
# It will show the value in the origin. In out case b=0.
# Use the my_fit function, we have the value of temperature as 17.85.
# Honestly, I don't think this value makes sense.
# The origin place in our case is at the beginning of 2008, which should be still in winter.
# Based on those values, I think we can guess those temperature is in the unit of centigrade.
# A temperature of 17.85 centigrade is a little too high in winter.

# But if it is in Texas.....it probably makes sense.