# Radioactive Decay

from random import random
from numpy import arange
from pylab import plot,xlabel,ylabel,show,legend,xlim,ylim,title

tau_Bi213=45*60
tau_Tl=2.2*60
tau_Pb=3.3*60

h=1.0
tmax=20000
tpoints=arange(0.0,tmax,h)

pPb=1-2**(-1*h/tau_Pb)
pTl=1-2**(-1*h/tau_Tl)
pBi213=1-2**(-1*h/tau_Bi213)

NBi213=10000
NPb=0
NTl=0
NBi209=0

Bi213points=[]
Pbpoints=[]
Tlpoints=[]
Bi209points=[]



for t in tpoints:
	Bi213points.append(NBi213)
	Pbpoints.append(NPb)
	Tlpoints.append(NTl)
	Bi209points.append(NBi209)
	decay_a=0
	decay_b=0
	decay_cPb=0
	decay_cTl=0
	#(a)from Pb 209 to Bi 209
	for i in range(NPb):
		if random()<pPb:
			decay_a += 1
	NPb -= decay_a
	NBi209 += decay_a
	#(b)from Tl209 to Pb 209
	for i in range(NTl):
		if random()<pTl:
			decay_b += 1
	NTl -= decay_b
	NPb += decay_b
	#(c)from Bi 213
	for i in range(NBi213):
		if random()<pBi213:
			if random()<0.0209:
				decay_cTl += 1
				decay_cPb += 0
			else:
				decay_cTl += 0
				decay_cPb += 1
	NBi213 -= (decay_cTl+decay_cPb)
	NTl += decay_cTl
	NPb += decay_cPb



plot(tpoints,Bi209points,label='Bi 209',color='red')
plot(tpoints,Pbpoints,label='Pb 209',color='gold')
plot(tpoints,Tlpoints,label='Tl 209',color='blue')
plot(tpoints,Bi213points,label='Bi 213',color='black')
xlabel("time")
ylabel("Number of atoms")
xlim(0,20000)
ylim(0,10000)
legend(loc='upper right')
title("Radioactive Decay")
show()