# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:37:09 2018

@author: Jacob Miske
"""
import numpy as np
import scipy as sp
from scipy import signal
from matplotlib import pyplot as plt

#For 2895 TREAT Test Plan
fname = "C2895T.DAT"
data2895 = np.fromfile(fname)
data2895 = data2895[1000:]
#length2895 = len(data2895[:,1])
#range2895 = range(length2895)

#Plot raw data from 2895
plt.plot(range(203722), data2895, 'blue')
plt.grid(); plt.xlabel('Data Points'); plt.ylabel('Detector Ouput')
plt.title('TREAT 2895T Detector Output')
plt.savefig('TREAT 2895T Raw Output.svg')

data2895filtered = sp.signal.savgol_filter(data2895, 171, 7)

#Plot filtered data from 2895
plt.plot(range(203722), data2895filtered, 'orange')
plt.grid(); plt.xlabel('Data Points'); plt.ylabel('Detector Ouput')
plt.title('TREAT 2895T Detector Output')
plt.savefig('TREAT 2895T Raw Output.svg')


