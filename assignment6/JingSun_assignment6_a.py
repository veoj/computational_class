import numpy as np
import pylab as py



g=9.81
l=0.19



def f(r,t):
    theta=r[0]
    omega=r[1]
    ftheta=omega
    fomega=-(g/l)*np.sin(theta)
    return np.array([ftheta,fomega],float)



a=0.0
b=10.0
N=5000
h=(b-a)/N



tpoints=np.arange(a,b,h)
xpoints=[]
ypoints=[]




r=np.array([174.0/180.*np.pi,0.],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1=h*f(r,t)
    k2=h*f(r+0.5*k1,t+0.5*h)
    k3=h*f(r+0.5*k2,t+0.5*h)
    k4=h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6




py.plot(tpoints,xpoints)
#py.plot(tpoints,ypoints)
py.xlabel("t")
py.ylabel("Angle of displacement")
py.show()


