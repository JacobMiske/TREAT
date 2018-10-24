# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:33:18 2018

@author: Jacob Miske
"""
import numpy as np
import scipy as sp
#from scipy import signal
from matplotlib import pyplot as plt

#For 2895 TREAT Test Plan
fname = r"061918MPFD2_1000ms.csv"
data2899 = open(fname, "r")
data2899 = data2899.read()
data2899 = data2899.split('\n')
data2899 = data2899[:3325]
#length2895 = len(data2895[:,1])
#range2895 = range(length2895)

#Plot raw data from 2895
plt.plot(range(3325), data2899, 'blue')
plt.grid(); plt.xlabel('Data Points'); plt.ylabel('Detector Ouput')
plt.title('TREAT 2899T Detector Output')
plt.savefig('TREAT 2899T Raw Output.svg')
plt.show()
data2899filtered = sp.signal.savgol_filter(data2899, 21, 3)

#Plot filtered data from 2895
plt.plot(range(3325), data2899filtered, 'orange')
plt.grid(); plt.xlabel('Data Points'); plt.ylabel('Detector Ouput')
plt.title('TREAT 2899T Detector Output')
plt.savefig('TREAT 2899T Filtered Output.svg')
plt.show()



