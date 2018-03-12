import numpy as np
import os

data = os.path.dirname(__file__)
print(os.path.join(data, 'data.csv'))

c, v = np.loadtxt(os.path.join(data, 'data.csv'), delimiter=',', usecols=(6, 7), unpack=True)
vwap = np.average(c, weights=v)
print("VWAP=", vwap)
