Assignment 5 contains two problems.

The first one is Periodic fitting of Munich data. 
The figure is shown in JingSun_Assignment5_Problem1.png


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















The second problem is SDSS data fitting.
Three ways are requred: linear, quadratic, and periodic (I use cosine here)
The figure is shown in JingSun_Assignment5_Problem2_fit.png.
And a zoomed in version is shown in JingSun_Assignment5_Problem2_zoom-in.png



# (a) The parameters are as below

# Linear-fit:
# y=m*x+b
# Slope m=1.058, intercept b=-42.319

# Quadratic-fit
# y=(q[0]*(x**2))+(q[1]*x)+q[2]
# q[0]=5.855, q[1]=-350.323, q[2]=5227.679

# Periodic cosine fit
# f(t)=a*cos(2*pi*t+b)+c
# a=63.056, b=0, c=-10.556



# (b)

# None of them did a good job on fitting. 
# After zooming in to the yrange of (-15,-5), I feel the cosine fit seems contains more points.
# So, I think the consine is better than other two.