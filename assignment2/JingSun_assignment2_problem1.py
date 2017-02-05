# Problem 1.
# Special Relativity.
# x is in the unit of light year, 1 light year=9.4607e15 meters.
# There is one thing defined as frac_v, and v = frac_v*c.
# c is the speed of light, c=3e8 m/s.



# (a)
# This one is in the rest frame of an observation Earth.
# In this situation, distance=velocity*time.
# distance is x*9.4607e15 meters.
# velocity is v=frac_v*3e8 meter per second.
# the required time need to have a unit of year.
# 1 year=3.154e7 second
# the required time = t/3.154e7
# The input will be x and frac_v, and x has the unit of light year.
# The output will be the time in the unit of year.

def rest_time(x_ly,frac_v):
	light_speed=3e8
	ly_m=9.4607e15
	yr_s=3.154e7
	x_m=x_ly*ly_m
	v_ms=frac_v*light_speed
	time_s=x_m/v_ms
	time_yr=time_s/yr_s
	if frac_v>1:
		return 'Are you kidding me?'
	elif time_yr<1:
		return '%.2f' % time_yr,'year'
	else:
		return '%.2f' % time_yr,'years'

# The output of the program is shown in Figure problem1_a.png
# The answer for a planet 10 light years away with v=0.90c:
#		11.11 years
# The answer for a planet 10 light years away with v=0.98c:
#		10.20 years
# The answer for a planet 10 light years away with v=0.999c:
#		10.01 years



# (b)
# This one is perceived by a passenger on board the ship.
# In this situation, special relativity need to be considered.
# With Lorentz transformation:
# time_l=gama(time-(v*x/c**2))
# gama_2=1/(1-(frac_v**2))
# gama=sqrt(gama_2)
# The input will be x and frac_v:
# x has a unit of light year
# The output will be the time in the unit of year

def ship_time(x_ly,frac_v):
	from numpy import sqrt
	light_speed=3e8
	ly_m=9.4607e15
	yr_s=3.154e7
	x_m=x_ly*ly_m
	v_ms=frac_v*light_speed
	time_s=x_m/v_ms
	time_yr=time_s/yr_s
	gama_2=1/(1-(frac_v**2))
	gama=sqrt(gama_2)
	time_l_s=gama*(time_s-(v_ms*x_m/light_speed**2))
	time_l_yr=time_l_s/yr_s
	if frac_v>1:
		return 'Are you kidding me?'
	elif time_l_yr<1:
		return '%.2f' % time_l_yr,'year'
	else:
		return '%.2f' % time_l_yr,'years'

# The output of the program is shown in Figure problem1_b.png
# The answer for a planet 10 light years away with v=0.90c:
#		4.84 years
# The answer for a planet 10 light years away with v=0.98c:
#		2.03 years
# The answer for a planet 10 light years away with v=0.999c:
#		0.45 years