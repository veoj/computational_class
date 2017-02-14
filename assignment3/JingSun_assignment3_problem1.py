# Problem 1.
# Plot STM data.

from pylab import imshow,show,colorbar,spectral
from numpy import loadtxt
data=loadtxt("/home/jing/chuan/stm.txt",float)
imshow(data,origin="lower",extent=[0,10,0,10])
spectral()
colorbar()
show()