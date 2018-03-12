# coding:utf-8
from collections import Counter

# lis = [
#     [1, 2, 2, 1],
#     [3, 1, 2],
#     [1, 3, 2],
#     [2, 4],
#     [3, 1, 2],
#     [1, 3, 1, 1]
# ]
# lis = [
#     [2, 2, 2, 2],
#     [3, 1, 4],
#     [1, 3, 4],
#     [5, 3],
#     [3, 2, 3],
#     [2, 3, 2, 1]
# ]
lis = [
    [1, 2, 4],
    [2, 3, 2],
    [3, 4],
    [5, 2],
    [1, 3, 3],
    [6, 1]
]
# lis = [
#     [2, 2, 4, 2],
#     [3, 3, 3, 1],
#     [3, 5, 1],
#     [6, 3, 1],
#     [2, 4, 1, 3],
#     [6, 1, 1]
# ]

init = set([x[0] for x in lis])
min_lis = min([len(x) for x in lis])
dic = {}
for x in init:
    count = 0
    for y in lis:
        if int(x) == int(y[0]):
            count += 1
    dic[x] = count
max_x = max(dic.values())  # 得到第一次的长度
init1 = set([x[0] for x in lis])
min_lis1 = min([len(x) for x in lis])
dic1 = {}
for x in init:
    count = 0
    for y in lis:
        if int(x) == int(y[-1]):
            count += 1
    dic1[x] = count
max_t = max(dic1.values())  # 得到最后一次的长度

if max_x == len(lis) or max_t == len(lis):
    print(0)
else:
    # 根据长度开始筛选 组合当中的最大值
    n = 1
    while n + 1 <= min_lis:
        th = [sum(x[:n+1]) for x in lis]
        c = Counter(th)
        max_c = max(c.values())
        if max_x < max_c:
            max_x = max_c
        else:
            n += 1
    n = 1
    while n+1 < min_lis:
        th1 = [x[n + 1] for x in lis]
        c1 = Counter(th1)
        max_c1 = max(c1.values())
        print('maxc1', max_c1)
        if max_x < max_c1:
            max_x = max_c1
        else:
            n += 1
    if sum(lis[0]) >= len(lis)+min_lis:
        print(len(lis)-max_x)
    else:
        print(sum(lis[0]) - max_x)


# lis1 = [
#     [1, 2, 4],
#     [2, 3, 2],
#     [3, 4],
#     [5, 2],
#     [1, 3, 3],
#     [6, 1]
# ]

# init = lis[0][0]
# init1 = lis[0][0] + lis[0][1]
# count = 0
# count1 = 0
# sumer = sum(lis[0])  # 得到每层墙总数
# n = 0
# j = n +1
# 判断前两位相等的最多数量
# print(sumer)
# for x in lis:
#     if init == x[n]:
#         count += 1
# for x in lis:
#     if init1 == x[n]+x[j]:
#         count1 +=1
# print(count, count1)
# for x in lis:
#     sumer = sum(x)

#     x.sort()
#     if [1, 2, 3] == x or [1, 1, 1, 3] == x:
#         count += 1
# print('最终穿墙数:', len(lis) - count)
