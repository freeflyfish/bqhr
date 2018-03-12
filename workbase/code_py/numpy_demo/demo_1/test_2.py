# coding:utf-8
from ctypes import *

MAX = 1000
inf = 0x3fffffff
w = []
# w[MAX][MAX] = 0
link = []
# link[MAX] = 0
visx, visy = [], []
# visx[MAX], visy[MAX] = 0, 0
lx, ly = [], []
# lx[MAX], ly[MAX] = 0, 0
n, m = 0, 0


def can(t):
    visx[t] = 1
    for i in range(1, m + 1):
        if not visy[i] and lx[t] + ly[i] == w[t][i]:
            visy[i] = 1
            if link[i] == -1 or can(link[i]):
                link[i] = t
                return 1
    return 0


def km():
    sumer = 0
    memset(ly, 0, sizeof(ly))
    for i in range(1, n + 1):
        lx[i] = -inf
        for j in range(1, n + 1):
            if lx[i] < w[i][j]:
                lx[i] = w[i][j]
    memset(link, -1, sizeof(link))
    for i in range(1, n + 1):
        while 1:
            memset(visx, 0, sizeof(visx))
            memset(visy, 0, sizeof(visy))
            if can(i):
                break
            d = inf
            for j in range(1, n + 1):
                if visx[j]:
                    for k in range(1, m + 1):
                        if not visy[k]:
                            d = min(d, lx[j] + ly[k] - w[j][k])
            if d == inf:
                return -1
            for j in range(1, n + 1):
                if visx[j]:
                    lx[j] -= d
            for j in range(1, m + 1):
                if visy[j]:
                    ly[j] += d
    for i in range(1, m + 1):
        if link[i] > -1:
            sumer += w[link[i]][i]
        return sumer


def main():
    ans = 0
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, n+1):
            w[i][j] = int(input())
            ans += w[i][j]
    ans -=km()
    print(ans)
    return 0

if __name__ == '__main__':
    main()