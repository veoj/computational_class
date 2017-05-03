
# coding: utf-8

# In[1]:

import random as ran
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math as math


# In[2]:

h=1
tmax=200
tpoints=np.arange(0,tmax+1,h)
#print(tpoints)

sample=10000
s_points=np.arange(0,sample+1,h)

mean=100
standard=20
A0=1/(standard*math.sqrt(2*3.14))
Z=(tpoints[1:tmax+1]-mean)/standard
dist=A0*np.exp(-1*(Z**2)/2)

#print(dist)
plt.plot(tpoints[1:tmax+1],dist)
plt.show()

print(sum(dist))
print(len(dist))



# In[3]:

dist_0=dist[0]
for i in range(tmax-1):
    if i == 0:
        dist[i]=dist_0
    else:
        dist[i]=dist[i]-dist[i-1]
        
#print(dist)
print(len(dist))


# In[4]:

dist2=dist[0:100]# steps from 1 to 100
dist1=dist[100:200]# steps from 101 to 200
print(len(dist1))
print(len(dist2))

frac1=ran.uniform(0,dist1[0])
est_1=mean+(standard*math.sqrt(-2*np.log(frac1/A0)))

est_1=int(est_1//1)

print(est_1)



frac2=ran.uniform(0,dist2[99])
est_2=mean-(standard*math.sqrt(-2*np.log(frac2/A0)))

est_2=int(est_2//1)

print(est_2)


# In[5]:

e1points=np.arange(0,est_1+1,h)
e2points=np.arange(0,est_2+1,h)

print(len(e1points))
print(len(e2points))


# In[6]:

first=1
p_same=3/4
p_change=1/4


# In[7]:

ele=first
pos1=first
position1=[]
pos2=first
position2=[]


# In[8]:

up=2
down=-2
right=1
left=-1


# In[9]:

# loop for capture possibility
for i in s_points:
    position1.append(pos1)
    ele = 1
    # 2nd move        
    if ran.random() > p_change:
        ele += right
        test = right
    else:
        if ran.random() > 1/2:
            ele += 0*up
            test = up
        else:
            ele += 0*down
            test = down
    # 3rd move  
    if test == right:
        if ran.random() > p_change:
            ele += right
            test = right
        else:
            if ran.random() > 1/2:
                ele += 0*up
                test = up
            else:
                ele += 0*down
                test = down
    else:
        if test == up:
            if ran.random() > p_change:
                ele += 0*up
                test = up
            else:
                if ran.random() > 1/2:
                    ele += left
                    test = left
                else:
                    ele += right
                    test = right
        else:
            if test == down:
                if ran.random() > p_change:
                    ele += 0*down
                    test = down
                else:
                    if ran.random() > 1/2:
                        ele += left
                        test = left
                    else:
                        ele += right
                        test = right
        # 4th and later move
        for t in range(3,est_1+1):
            if test == right:
                if ran.random() > p_change:
                    ele += right
                    test = right
                else:
                    if ran.random() > 1/2:
                        ele += 0*up
                        test = up
                    else:
                        ele += 0*down
                        test = down
            else:
                if test == up:
                    if ran.random() > p_change:
                        ele += 0*up
                        test = up
                    else:
                        if ran.random() > 1/2:
                            ele += left
                            test = left
                        else:
                            ele += right
                            test = right
                else:
                    if test == down:
                        if ran.random() > p_change:
                            ele += 0*down
                            test = down
                        else:
                            if ran.random() > 1/2:
                                ele += left
                                test = left
                            else:
                                ele += right
                                test = right
                    else:
                        if test == left:
                            if ran.random() > p_change:
                                ele += left
                                test = left
                            else:
                                if ran.random() > 1/2:
                                    ele += 0*up
                                    test = up
                                else:
                                    ele += 0*down
                                    test = down
    pos1 = ele


# In[10]:

print(position1)


# In[11]:

position1=position1[1:sample+1]
print(len(position1))


# In[12]:

reactor=[]
capture=[]
through=[]

num_r=0
num_c=0
num_t=0

size1=np.arange(0,est_1+1,h)
print(len(size1))


# In[13]:

for j in range(est_1+1):
    reactor.append(num_r)
    capture.append(num_c)
    through.append(num_t)
    x = size1[j]
    nt=0
    nc=0
    nr=0
    for i in range(sample):
        if position1[i] > x:
            nt += 1
        elif position1[i] > 0:
            nc += 1
        else:
            nr += 1
    if nr == 0:
        num_r = 0.001
    else:
        num_r = nr
    if nc == 0:
        num_c = 0.001
    else:
        num_c = nc
    if nt == 0:
        num_t = 0.001
    else:
        num_t = nt


# In[14]:

reactor_n=reactor[1:est_1+1]
capture_n=capture[1:est_1+1]
through_n=through[1:est_1+1]


# In[15]:

print(reactor_n)
print(len(reactor_n))


# In[16]:

print(capture_n)
print(len(capture_n))


# In[17]:

print(through_n)
print(len(through_n))


# In[18]:

print(size1[1:est_1+1])
print(len(size1[1:est_1+1]))


# In[19]:

size_array=np.array(size1[1:est_1+1])
through_array=np.array(through_n)
capture_array=np.array(capture_n)
reactor_array=np.array(reactor_n)
plt.plot(size_array,through_array,'-',label='through',color='red',linewidth=3.0)
plt.plot(size_array,capture_array,'-',label='capture',color='blue',linewidth=3.0)
plt.plot(size_array,reactor_array,'-',label='reactor',color='black',linewidth=3.0)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Size of the shield')
plt.ylabel('Number')
plt.show()





# In[20]:

P_through=through_array/sample
P_capture=capture_array/sample
P_reactor=reactor_array/sample

size1=size1[1:est_1+1]


# In[21]:

m_through,b_through=np.polyfit(size1,np.log(P_through),1)
print(m_through,b_through)


fit_t=m_through*size1+b_through
uncertainty_t=(1/tmax)*np.sum((fit_t-np.log(P_through))**2)#Standard Deviation
print(math.sqrt(uncertainty_t))


# In[22]:

m_capture,b_capture=np.polyfit(size1,np.log(P_capture),1)
print(m_capture,b_capture)


fit_c=m_capture*size1+b_capture
uncertainty_c=(1/tmax)*np.sum((fit_t-np.log(P_capture))**2)#Standard Deviation
print(math.sqrt(uncertainty_c))


# In[23]:

m_reactor,b_reactor=np.polyfit(size1,np.log(P_reactor),1)
print(m_reactor,b_reactor)


fit_t=m_reactor*size1+b_reactor
uncertainty_r=(1/tmax)*np.sum((fit_t-np.log(P_reactor))**2)#Standard Deviation
print(math.sqrt(uncertainty_r))


# In[ ]:




# In[ ]:



