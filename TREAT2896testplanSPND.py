# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:23:18 2018

@author: Jacob Miske
"""
import numpy as np
import scipy as sp
from scipy import signal
from matplotlib import pyplot as plt

#For 2895 TREAT Test Plan
fname = "061218spnd1_1ms.csv"
data2896 = open(fname, "r")
data2896 = data2896.read()
data2896 = data2896.split('\n')
data2896 = data2896[:3200000]
#length2895 = len(data2895[:,1])
#range2895 = range(length2895)

#Plot raw data from 2895
plt.plot(range(3200000), data2896, 'blue')
plt.grid(); plt.xlabel('Data Points'); plt.ylabel('Detector Ouput')
plt.title('TREAT 2896T Detector Output')
plt.savefig('TREAT 2896T Raw Output.svg')
plt.show()

data2896filtered = sp.signal.savgol_filter(data2896, 35, 3)

#Plot filtered data from 2895
plt.plot(range(3200000), data2896filtered, 'orange')
plt.grid(); plt.xlabel('Data Points'); plt.ylabel('Detector Ouput')
plt.title('TREAT 2896T Detector Output')
plt.savefig('TREAT 2896T Filtered Output.svg')
plt.show()



