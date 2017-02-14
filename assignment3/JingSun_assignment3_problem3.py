# Problem 3.
# Heat capacity of a solid.



def cv(T):
	from numpy import exp
	V=1e-3
	rou=6.022e28
	kb=1.38e-23
	sd=428
	N=1000
	a=0.0
	b=sd/T
	h=(b-a)/N
	s=0.5*0+(0.5*((b**4)*exp(b))/((exp(b)-1)**2))
	for k in range(1,N):
		x=a+k*h
		s += ((x**4)*exp(x))/((exp(x)-1)**2)
	jifen=h*s
	ccc=9*V*rou*kb*((T/sd)**3)*jifen
	return '%.2f' % ccc



from pylab import plot,xlabel,ylabel,show
from numpy import linspace,arange

x=linspace(5,500,100)
y=arange(100,dtype=float)
for i in range(0,100):
	y[i]=cv(x[i])

plot(x,y)
xlabel("Temperature (K)")
ylabel("The heat capacity (J/K)")
show()