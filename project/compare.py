
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[2]:

N=[1,2,3,4,5,6,7]


# In[3]:

part_at=[0.1939,0.1947,0.1964,0.1954,0.1934,0.1941,0.1948]
part_ac=[0.0139,0.0139,0.0139,0.0139,0.0139,0.0139,0.0138]
part_ar=[1.7626,1.8152,1.7874,1.8158,1.8376,1.8245,1.8079]
print(np.average(part_at))
print(np.average(part_ac))
print(np.average(part_ar))


# In[4]:

part_b1t=[0.3496,0.2350,0.3388,0.2324,0.2907,0.3116,0.2724]
part_b1c=[0.0421,0.0267,0.0392,0.0272,0.0297,0.0324,0.0255]
part_b1r=[1.8471,1.8085,1.7892,1.7952,1.8189,1.8067,1.8270]
print(np.average(part_b1t))
print(np.average(part_b1c))
print(np.average(part_b1r))


# In[5]:

part_b100t=[0.1498,0.1547,0.1502,0.1413,0.1243,0.1461,0.1240]
part_b100c=[0.0090,0.0092,0.0087,0.0080,0.0065,0.0083,0.0063]
part_b100r=[1.8091,1.8282,1.8426,1.8233,1.7880,1.8496,1.7892]
print(np.average(part_b100t))
print(np.average(part_b100c))
print(np.average(part_b100r))


# In[6]:

part_ct=[0.1923,0.1837,0.1880,0.1958,0.1902,0.1960,0.1864]
part_cc=[0.0140,0.0141,0.0142,0.0141,0.0140,0.0142,0.0142]
part_cr=[2.1103,2.1095,2.1236,2.0948,2.1211,2.1070,2.1095]
print(np.average(part_ct))
print(np.average(part_cc))
print(np.average(part_cr))


# In[7]:

part_c1t=[0.2969,0.3139,0.2648,0.2540,0.3058,0.3083,0.2254]
part_c1c=[0.0946,0.0473,0.0333,0.0263,0.0417,0.0490,0.0245]
part_c1r=[2.1422,2.1169,2.1103,2.1128,2.1405,2.1153,2.0923]
print(np.average(part_c1t))
print(np.average(part_c1c))
print(np.average(part_c1r))


# In[8]:

part_c100t=[0.1532,0.1130,0.1388,0.1412,0.1397,0.1329,0.1215]
part_c100c=[0.0090,0.0055,0.0076,0.0079,0.0077,0.0071,0.0061]
part_c100r=[2.1161,2.1203,2.1120,2.0326,2.1070,2.0794,2.1707]
print(np.average(part_c100t))
print(np.average(part_c100c))
print(np.average(part_c100r))


# In[10]:

plt.plot(N,part_at,'-',label='a without distribution (twice)',color='red',linewidth=3.0)
plt.plot(N,part_ct,'-',label='a without distribution (three times)',color='blue',linewidth=3.0)
plt.plot(N,part_b1t,'-',label='a with distribution 1-100 steps(twice)',color='black',linewidth=3.0)
plt.plot(N,part_b100t,'-',label='a with distribution 100-200 steps(twice)',color='orange',linewidth=3.0)
plt.plot(N,part_c1t,'-',label='a with distribution 1-100 steps(three times)',color='purple',linewidth=3.0)
plt.plot(N,part_c100t,'-',label='a with distribution 100-200 steps(three times)',color='green',linewidth=3.0)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('through')
plt.show()





# In[11]:

plt.plot(N,part_ac,'-',label='b without distribution (twice)',color='red',linewidth=3.0)
plt.plot(N,part_cc,'-',label='b without distribution (three times)',color='blue',linewidth=3.0)
plt.plot(N,part_b1c,'-',label='b with distribution 1-100 steps(twice)',color='black',linewidth=3.0)
plt.plot(N,part_b100c,'-',label='b with distribution 100-200 steps(twice)',color='orange',linewidth=3.0)
plt.plot(N,part_c1c,'-',label='b with distribution 1-100 steps(three times)',color='purple',linewidth=3.0)
plt.plot(N,part_c100c,'-',label='b with distribution 100-200 steps(three times)',color='green',linewidth=3.0)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('captured')
plt.show()



# In[12]:

plt.plot(N,part_ar,'-',label='c without distribution (twice)',color='red',linewidth=3.0)
plt.plot(N,part_cr,'-',label='c without distribution (three times)',color='blue',linewidth=3.0)
plt.plot(N,part_b1r,'-',label='c with distribution 1-100 steps(twice)',color='black',linewidth=3.0)
plt.plot(N,part_b100r,'-',label='c with distribution 100-200 steps(twice)',color='orange',linewidth=3.0)
plt.plot(N,part_c1r,'-',label='c with distribution 1-100 steps(three times)',color='purple',linewidth=3.0)
plt.plot(N,part_c100r,'-',label='c with distribution 100-200 steps(three times)',color='green',linewidth=3.0)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('reactor')
plt.show()


# In[ ]:



