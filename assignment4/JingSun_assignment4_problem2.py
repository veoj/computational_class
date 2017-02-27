# Monte Carlo integration

# (a)Show the probability distribution p(x)
from numpy import arange,linspace,exp
from pylab import plot,xlabel,ylabel,show,legend,xlim,ylim,title

x=linspace(1e-6,1.,1e6)
f=(x**(-1/2))/(exp(x)+1)
p=1/(2*(x**(1/2)))

plot(x,f,label='f(x)',color='red')
plot(x,p,label='p(x)',color='blue')
xlim(0,1)
ylim(0,10)
legend(loc='upper right')
show()
# It turns out that f and p are quite similar based on the graph.

# (b) Calculate the integral
# I=(2/N)*sum(1/(exp(x)+1))
from random import random
from numpy import exp

def f(x):
	return (x**(-1/2))/(exp(x)+1)

N=1000000
value=0
for i in range(N):
	x=random()
	value += (2/N)*(1/(exp(x)+1))

print(value)

