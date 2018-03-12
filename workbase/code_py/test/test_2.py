# coding :utf-8

import itertools
import re

# pattern = re.compile('[A-Z]{2}[A-Z]{2}')
# s = 'ABCD'
#
# for x in itertools.combinations_with_replacement(s, 4):
#     print(re.findall(pattern, ''.join(x)))


raw = 'BBBYYYYYY'  # BBBYYYYYY
pre = re.compile(r"((?P<t1>\S)(?P=t1)+)")
item = re.findall(pre, raw)
count = 0
for x in item:
    if len(x[0]) == 2 or len(x[0])==3:
        count +=1
    elif len(x[0]) > 3:
        count += int(len(x[0]) / 2)
print(count)



# if len(set(lis))==1:
#         count = len(raw) / 2
#         print(int(count))
# else:
#     for x in range(len(lis)):
#         if x + 1 < len(lis) and x + 2 < len(lis):
#             if lis[x] == lis[x+1] and lis[x] != lis[x+2]:
#                 count +=1
#
#     print(count)

# for x in set(lis):
#     for
#     print(x)
# print(count)

# s = 'ABCBOATERATCG'
# sumer = 0
# prn = re.compile('[A,T,C,G]{2,}')
# item = re.findall(prn,s)
# print(item)
# for x in item:
#     if sumer < len(x):
#         sumer = len(x)
# print(sumer)

# s = 'akasakaakasakasakaakas'  # 14  -- 22  - 8
# # s = 'abaababaab'
# # print(len(s))
# count = 2
# t = int(len(s) / 2)
# # print(t)
# print(len(s) % t)
# if t % 2 >=1:
#     t += 1
#
# print(t)
# # if t == 0:
#     print(len(s))
# else:
#     print(len(s[:t]))


# raw = 'pnzdljbnxrnofnpvmpkffvgiirohwedhvwtnwxfhfaonredbafudtdsxwehahcrpjguxsgjzoajnqyoshiazszfyuxlnrqdzhbucuqvhpsftvpliyspchmhfqqrjacbznoiacrsyszrxwsyrztmbqqtlggqhfviwqlvbbcztxhmepjrqbggzoxxpnrsolpwxusjxfdrrcrfqzynjnpgzpgagkerabtlrsivukmmzudccoybdvyeattqjxyk'  # BBBYYYYYY
# count = 0
# n = 0
# for k, v in {k: raw.count(k) for k in set(raw)}.items():
#     if v == 1:
#         count += 1
#     if v >= 2:
#         n += 1
# if 0 < n <= 2:
#     count += 1
# elif n >= 3:
#     count += n
# print(count)
# c = itertools.permutations('YYYNN', 5)
#
# for x in enumerate(c):
#     print(x)
#
# import copy



# line = input()
#
#
# str = line
#
# l = 0
#
# # for (var i=line.length; i > 0; i -= 2):
# for i in range(len(str)):
#     str = str.slice(0, i-2)
#     l = len(str)
#     if str.slice(0, l / 2) == str.slice(l / 2):
#         break









# print(l);
