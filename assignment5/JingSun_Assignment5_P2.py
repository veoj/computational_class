# Problem 2: SDSS Data Fitting



import fitsio
import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit




fits_file=fitsio.FITS('/home/jing/chuan/allStar-l30e.2.fits')

print(fits_file)

print(fits_file[1])

cut=fits_file[1].where('GLAT>29 && GLAT<31')
subset=fits_file[1][cut]



glat_col=['GLAT']
data_glat=fitsio.read('/home/jing/chuan/allStar-l30e.2.fits',columns=glat_col)
x_glat=data_glat[cut]

x_glat.dtype
x_glat=x_glat.view(np.recarray)
x=x_glat.GLAT
xl=x.tolist()

vhelio_col=['VHELIO_AVG']
data_vhelio=fitsio.read('/home/jing/chuan/allStar-l30e.2.fits',columns=vhelio_col)
y_v=data_vhelio[cut]

y_v.dtype
y_v=y_v.view(np.recarray)
y=y_v.VHELIO_AVG
yl=y.tolist()

plt.plot(x,y,'.')
plt.show()



# (1) Linear fit

m,b=np.polyfit(xl,yl,1)
print(m,b)
# Slope m=1.058, intercept b=-42.319, y=m*x+b
xpoints=np.linspace(29,31,1000)
plt.plot(x_glat,y_v,'.')
plt.plot(xpoints,m*xpoints+b,label='Linear-fit',color='red',linewidth=3.0)
plt.legend()
plt.show()



# (2) Quadratic fit
q=np.polyfit(xl,yl,2)
print(q)
# y=(q[0]*(x**2))+(q[1]*x)+q[2]
# q[0]=5.855, q[1]=-350.323, q[2]=5227.679
xpoints=np.linspace(29,31,1000)
plt.plot(x_glat,y_v,'.',color='black')
plt.plot(xpoints,(q[0]*(xpoints**2))+(q[1]*xpoints)+q[2],label='Quadratic-fit',color='green',linewidth=3.0)
plt.legend()
plt.show()



# (3) Cosine Periodic

guess_amplitude=np.std(yl)
guess_phase=0
guess_offset=np.mean(yl)

p0=[guess_amplitude,guess_phase,guess_offset]

def my_fit(x,amplitude,phase,offset):
    return np.cos(x*2*np.pi+phase)*amplitude+offset

# f(t)=a*cos(2*pi*t+b)+c

fit=curve_fit(my_fit,xl,yl,p0=p0)
xpoints=np.linspace(29,31,1000)
data_fit=my_fit(xpoints,*fit[0])

print(p0)
# a=63.056, b=0, c=-10.556

plt.plot(xl,yl,'.',color='grey')

plt.plot(xpoints,m*xpoints+b,label='Linear-fit',color='blue',linewidth=1.0)
plt.plot(xpoints,(q[0]*(xpoints**2))+(q[1]*xpoints)+q[2],label='Quadratic-fit',color='green',linewidth=1.0)
plt.plot(xpoints,data_fit,label='Periodic-fit',color='red',linewidth=1.0)
plt.legend()
plt.xlabel("GLAT")
plt.ylabel("VHELIO_AVG")
plt.title("SDSS data")
plt.xlim(range(29,31))

plt.show()




plt.plot(xl,yl,'.',color='grey')

plt.plot(xpoints,m*xpoints+b,label='Linear-fit',color='blue',linewidth=1.0)
plt.plot(xpoints,(q[0]*(xpoints**2))+(q[1]*xpoints)+q[2],label='Quadratic-fit',color='green',linewidth=1.0)
plt.plot(xpoints,data_fit,label='Periodic-fit',color='red',linewidth=1.0)
plt.legend()
plt.xlabel("GLAT")
plt.ylabel("VHELIO_AVG")
plt.title("SDSS data")
plt.xlim(range(29,31))

plt.ylim(-15,-5)
plt.show()





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