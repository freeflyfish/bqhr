# coding:utf-8
import time
import numpy


def func(fnc):
    def adder(n):
        start = time.time()
        fnc(n)
        end = time.time() - start
        return end

    return adder


# 传统代码
# @func
def pythonsum(n):
    a, b, c = list(range(n)), list(range(n)), []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c


# numpy 代码
# @func
def numpysum(n):
    a, b = numpy.arange(n) ** 2, numpy.arange(n) ** 3
    c = a + b
    return c


print(pythonsum(2))
print(numpysum(5))
