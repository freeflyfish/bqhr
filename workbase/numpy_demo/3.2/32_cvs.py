# coding:utf-8

import numpy as np

# i2 = np.eye(2)
# print(i2)
#
# np.savetxt("eye.txt",i2)

c,v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)
