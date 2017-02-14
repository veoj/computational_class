# Problem 2.
# The quadratic equation



# (a) standard formula
def standard(a,b,c):
	from math import sqrt
	x1_a=((-1*b)+sqrt((b**2)-(4*a*c)))/(2*a)
	x2_a=((-1*b)-sqrt((b**2)-(4*a*c)))/(2*a)
	return x1_a,x2_a

# The result for 0.001x^2+1000x+0.001=0 is:
# (-9.999894245993346e-07, -999999.999999)s



# (b) further correction
def correction(a,b,c):
	from math import sqrt
	x1_b=2*c/((-1*b)-sqrt((b**2)-(4*a*c)))
	x2_b=2*c/((-1*b)+sqrt((b**2)-(4*a*c)))
	return x1_b,x2_b

# The result for 0.001x^2+1000x+0.001=0 is:
# (-1.000000000001e-06, -1000010.5755125057)

# I think the whole point is to avoid to have a too small number in denominator.
# In part (a), x1_a works well, but x2_a has a problem.
# Because in x2_a, the numerator is a relatively large number, but the denominator is a very small number.
# In this case, x2_a cannot work very well.
# In part (b), x1_b has a very small denominator, that's why it has the same problem as x2_a
# So we need to avoid the usage of subtraction



# (c) in all case
def final(a,b,c):
	from math import sqrt
	x1=((-1*b)+sqrt((b**2)-(4*a*c)))/(2*a)
	x2=2*c/((-1*b)+sqrt((b**2)-(4*a*c)))
	return x1,x2

# The result for 0.001x^2+1000x+0.001=0 is:
# (-9.999894245993346e-07, -1000010.5755125057)