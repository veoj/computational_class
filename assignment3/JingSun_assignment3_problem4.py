# Problem 4.
# Numerical Integral
# Gaussian Quadrature



def gauss_integral(x):
	from gaussxw import gaussxw
	from numpy import exp
	N=100
	a=0.0
	b=x
	t,w=gaussxw(N)
	tp=0.5*(b-a)*t+0.5*(b+a)
	wp=0.5*(b-a)*w
	s=0.0
	for k in range(N):
		s += wp[k]*(exp(tp[k]**2))
	return '%.2f' % s




from pylab import plot,show
from numpy import linspace,arange

x=linspace(0,3,30)
y=arange(30,dtype=float)
for i in range(0,30):
	y[i]=gauss_integral(x[i])

plot(x,y)
show()