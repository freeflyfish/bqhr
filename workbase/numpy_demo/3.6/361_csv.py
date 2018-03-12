# coding:utf-8

import numpy as np

h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5), unpack=True)
print('highest=', np.max(h))
print('lowest=', np.min(l))

print('Spread hrgh price', np.ptp(h))
print('Spread low price', np.ptp(l))
c = np.loadtxt('data.csv', delimiter=',', usecols=(5,), unpack=True)
print(c)
print('median =', np.median(c))

sorted_close = np.msort(c)
print('sorted =', sorted_close)
