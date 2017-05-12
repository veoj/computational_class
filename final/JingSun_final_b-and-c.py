
# coding: utf-8

# In[1]:

import numpy as np
import math as math
import matplotlib.pyplot as plt


# In[2]:

kb=1.38e-23#Boltzmanns constant, in the unit of J/K
hp=6.626e-34#Planck constant, in the unit of J s
vc=3.0e8#The speed of light, in the unit of m/s
lam1=6.0e-7#lower desired wavelength, in the unit of m
lam2=7.5e-7#higher desired wavelength,in the unit of m


# In[3]:

#The peak locates around 5600K according the results in part (a), and the interval is 100K in part a
Tlow=5500
Thigh=5700
tem=np.arange(Tlow,Thigh+1,1)#Temperature in the unit of K
#Temperature array
num_t=len(tem)
print(num_t)


# In[4]:

b=hp*vc/(lam1*kb*tem)#upper limitation of integral
a=hp*vc/(lam2*kb*tem)#lower limitation of integral
N=100
h=(b-a)/N


# In[5]:

def x(lam,temp):
    x=hp*vc/(lam*kb*temp)
    return x


# In[6]:

def fx(x):
    fx=(x**3)/((np.exp(x))-1)
    return fx


# In[7]:

R=[]
tempR=[]
#create the 2D array
Rt=np.zeros([N+1,N+1],float)
record=0


# In[8]:

for t in range(num_t):
    R.append(record)
    tempR.append(Rt)
    
    temp=tem[t]
    at=a[t]
    bt=b[t]
    fa=fx(at)
    fb=fx(bt)
    
    s=0.5*(fa+fb)
 
    Rt[0,0]=s
    for i in range(1,N+1):
        ht=(bt-at)/i
        for k in range(1,i):
            s += fx(at+(k*ht))
        Rt[i,0]=ht*s 
        for m in range(0,i):
            Rt[i,m+1]=Rt[i,m]+(1/((4**(m+1))-1))*(Rt[i,m]-Rt[i-1,m])
    record=Rt[N,N]*15.0/(np.pi**4)


# In[9]:

print(Rt)


# In[10]:

#print(R)
print(len(R))


# In[11]:

#use the formular 6.121 in textbook
gamma=-5#it is negative because we are looking for a maximum value
step=10000
Ra=np.asarray(R)
x1=5500
x2=5700

xpoints=np.arange(len(R))
#ypoints=Ra

for i in range(step):
    if i == 0:
        xpoints[i]=x1
    if i == 1:
        xpoints[i]=x2
    if i == 2:
        xpoints[i]=int(xpoints[i-1]+(gamma*((Ra[i-1]-Ra[i-2])/(xpoints[i-1]-xpoints[i-2]))))

    if i > 2 and i < len(R):
        if xpoints[i-1]-xpoints[i-2] == 0:
            xpoints[i] = xpoints[i-1]
        else:
            xpoints[i]=int(xpoints[i-1]+(gamma*((Ra[i-1]-Ra[i-2])/(xpoints[i-1]-xpoints[i-2]))))
        #xpoints[i]=x_temp//1


# In[12]:

print(xpoints)


# In[13]:

print(xpoints[len(xpoints)-1])


# So,the temperature of maximum efficiency of the light bulb is 5501 K.
# But it is not practical to run a tungsten-filament light bult at this temperature, 
# because the melting point of tungsten is about 3700 K.

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



