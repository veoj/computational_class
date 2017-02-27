# PHYS 50733 Computational Physics
# Assignment 1
# Date: Jan 29, 2017---20:27





#Problem 1: Converting from decimal to binary representation.
#I named an algorithm as "ten_two". The code is as below:

def ten_two(x_base10):
	from numpy import arange,log2,zeros,copy
	n_array=arange(x_base10)
	digit=arange(x_base10)
	all_zero=zeros(x_base10)
	seperate=arange(x_base10)
	for i in n_array:
		if i>log2(x_base10):
			digit[i]=0
		elif i==log2(x_base10):
			all_zero[i]=1
			digit=copy(all_zero)
		elif i==0:
			digit[i]=x_base10%2
		else:
			digit[i]=(x_base10//(2**i))%2
		seperate[i]=digit[i]*(10**i)
	x_base2=sum(seperate)
	return x_base2

# This is the function I created for the convertion.
# After run this function in terminal, type:
	#print(ten_two(x))--------where x is a integer in base 10
# THen it will return the integer in base 2





#Problem 2: Altitude of a satellite

#	(a)
# According to Keplers 3rd law of planetary motion, we have:
# (a**3)/(T**2)=k, where k is a constant, and:
#		k=(G*M)/(4*(pi**2))
# in which, T is the period of satellite, 
# G is Newton's gravitational constant,
# M is the mass of the Earth,
# a is the radius of the orbit, and:
#		a=R+h
#	R is the radius of Earth, h is the altitude.
# Based on the equation above, 
#		a**3=(G*M*(T**2))/(4*(pi**2))
# So,
# 		a=((G*M*(T**2))/(4*(pi**2)))**(1/3)
# As a=R+h, so:
#		h=(((G*M*(T**2))/(4*(pi**2)))**(1/3))-R
# Proved.


#	(b)
# I wrote a function to calculate the altitude of satellite.
# The T need to be in the unit of second.
# 1 s == 1 s
# 1 min == 60 s
# 1 h == 3600 s
def altitude_satellite(T_satellite):
	import math
	G_newton=6.67*(10**(-11))
	M_earth=5.97*(10**24)
	R_earth=6.371*(10**6)# I convert 'km' to 'm'
	h_altitude=(((G_newton*M_earth*(T_satellite**2))\
		/(4*(math.pi**2)))**(1/3))-R_earth
	return ['%.2e' % h_altitude,'meter'],\
		['%.2e' % (h_altitude/1000),'kilometer']
# Input the value of satellite's period(in the unit of second)
#	After run this function, type in:
#		print(altitude_satellite(T_satellite in seconds))
# The output will be the altitude
# The altitude will be in the unit of m and km.


#	(c)
# When the period is 1 day(24 hours)
#	T=24*3600
print(altitude_satellite(24*3600))
#	The altitude is 3.59e+04 km.
# When the period is 90 minutes
#	T=90*60
print(altitude_satellite(90*60))
#	The altitude is 2.79e+02 km.
# When the period is 45 minutes
#	T=45*60
print(altitude_satellite(45*60))
#	The altitude is -2.18e+03 km.
# From the last one, it can be concluded that:
#	a satellite of Earth cannot have a period smaller than 45 min.
#	Also, it can be infered that:
#	a satellite will have smaller period when it's closer to Earth.


#	(d)
# The geosynchronous satellite has a period slightly less than 24h,
# because the Earth rotates in less than 24h,
# it rotates in 23.93 hours.
# When the period is 23.93 hours, 
#	T=23.93*3600
print(altitude_satellite(23.93*3600))
#	The altitude is 3.58e+04 km.
print(altitude_satellite(24*3600)-altitude_satellite(23.93*3600))
# The difference is about 100 km.
# The satellite with a period of 23.93 hours is 100km closer.